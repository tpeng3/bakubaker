#--------------------------------------------------------------------------
# INITIALIZE THOUGHT INVENTORY
#--------------------------------------------------------------------------
init -1 python:
    sel_xpos = None
    sel_ypos = None

    class Item(store.object):
        def __init__(self, name, image="", tooltip="", flavors={}):
            self.name = name # name of item
            self.image = image # image url
            self.tooltip = tooltip # tooltip desc
            self.flavors = flavors # {flavor: amount}
            # flavors are temporary names, to be decided later 

    class Inventory(store.object):
        def __init__(self):
            self.items = []
            self.selected = []
            # self.trash = []
        def add(self, item):
            if item not in self.items:
                self.items.append(item)
        def toggleSelect(self, item):
            if item not in self.selected:
                self.selected.append(item)
            else:
                self.selected.remove(item)
        # def use(self, item):
        #     if item in self.items:
        #         self.items.remove(item)
        #         self.trash.append(item)
        #         self.selitem = None
        # def undo(self):
        #     if len(self.trash) > 0:
        #         item = self.trash.pop()
        #         self.add(item)
        #         return item
        #     return None
        def reset(self):
            for item in self.selected:
                self.toggleSelect(item)

    class CookStatus(store.object):
        def __init__(self, smashReq):
            self.flavors = {
                "spooky": 0,
                "spirit": 0,
                "wonder": 0
            }
            self.combo = 0
            self.smashReq = smashReq # [] list of ideal dish ingredients NAMES
            self.smash = False
        def update(self, item):
            if item in inventory.selected: # referencing inventory here feels like... bad practice... bUT HEY IT WORKS
                for flavor in item.flavors:
                    self.flavors[flavor] += item.flavors[flavor]
                if item in self.smashReq:
                    self.combo += 1
                else:
                    self.combo = 0
            else:
                for flavor in item.flavors:
                    self.flavors[flavor] -= item.flavors[flavor]
                self.combo = 0
        # def undo(self, item):
        #     if item:
        #         for flavor in item.flavors:
        #             self.flavors[flavor] -= item.flavors[flavor]
        def reset(self):
            self.flavors = {
                "spooky": 0,
                "spirit": 0,
                "wonder": 0
            }
            self.combo = 0
        def smash(self, skill): # "super smash" move
            # skill: {"cost": {"flavor":amount}, "boost": {"flavor":amount}}
            for flavor in skill.cost:
                cost = skill.cost[flavor]
                if cost < 1: # if cost is a percentage
                    transmute = self.flavors[flavor] * cost
                    self.flavors[flavor] -= transmute
                else: # else just subtract the cost
                    self.flavors[flavor] -= cost
            for flavor in skill.boost:
                boost = skill.boost[flavor]
                if boost == 0: # if boost is a 1:1 ratio conversion
                    self.flavors[flavor] += transmute
                if boost < 1: # if boost is a percentage
                    self.flavors[flavor] += self.flavors[flavor] * boost
                else: # else just add the cost
                    self.flavors[flavor] += boost
            self.smash = True
        def result(self, goal, zest): #goal is a {}, zest is a string with the focused attr
            for flavor in goal:
                if self.flavors[flavor] < goal[flavor]:
                    return -1 # did not meet requirements
            if self.smash and self.flavors[zest] > 100: # perfect score!
                return 1
            return 0 # ordinary score


#--------------------------------------------------------------------------
# CUSTOMIZE THOUGHT INVENTORY SCREEN
#--------------------------------------------------------------------------
screen inventory():
    zorder 2
    modal True
    frame:
        pass

    imagebutton:
        idle "gui/button/button_back.png"
        hover im.MatrixColor("gui/button/button_back.png", im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0))
        xalign 1.0 yalign 0
        action [ToggleScreen('inventory')]


    #TODO: add better positions for the inventory, after UI is decided
    hbox:
        for item in inventory.items:
            imagebutton:
                idle item.image
                action [Function(inventory.select, item)]
                tooltip item.tooltip

    # this is if we want to select any items to focus, otherwise we don't need this code
    if inventory.selitem is not None:
        text "sel item is" + inventory.selitem.name ypos 520

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            xalign 0.5 yalign 0.5 #tmp

#--------------------------------------------------------------------------
# DEFINE INGREDIENTS
#--------------------------------------------------------------------------
init python:
    kirby = Item("Kirby with Shortcake", image = "/images/items/item_kirby.png",
        tooltip="Free him...",
        flavors={
            "wonder": 999,
            "spirit": 999,
            "spooky": 999
        })
    dream_flour = Item("Dream Flour", image = "/images/items/item_kirby.png",
        tooltip="Dream Flour +30 wonder, -20 spirit", 
        flavors={
            "wonder": 30,
            "spirit": -20,
            "spooky": 0
        })
    nightmare_jelly = Item("Nightmare Jelly", image = "/images/items/item_kirby.png",
        tooltip="Nightmare Jelly +40 spooky", 
        flavors={
            "wonder": 0,
            "spirit": 0,
            "spooky": 40
        })
    spooky_jam = Item("Spooky Jam", image = "/images/items/item_kirby.png",
        tooltip="Spooky Jam +30 spooky, +10 wonder", 
        flavors={
            "wonder": 10,
            "spirit": 0,
            "spooky": 30
        })
    galaxy_milk = Item("Galaxy Milk", image = "/images/items/item_kirby.png",
        tooltip="Galaxy Milk +10 spirit, -5 spooky", 
        flavors={
            "wonder": 0,
            "spirit": 10,
            "spooky": -5
        })
    haunted_whip = Item("Haunted Whip", image = "/images/items/item_kirby.png",
        tooltip="Haunted Whip +20 spooky", 
        flavors={
            "wonder": 0,
            "spirit": 0,
            "spooky": 20
        })

    c_strawberry = Item("Creamy Strawberry", image = "/images/items/item_strawberry.png",
        tooltip="A tasty strawberry +20 spooky, +30 wonder", 
        flavors={
            "wonder": 30,
            "spirit": 20,
            "spooky": 0
        })
    
    
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
            self.selitem = None
            self.undo = []
        def add(self, item):
            if item not in self.items: # we don't want duplicates... or do we?
                self.items.append(item)
        def use(self, item):
            if item in self.items:
                self.items.remove(item)
                self.undo.append(item)
        def undo(self, item):
            if len(self.undo) != 0:
                print("hi")
                item = self.undo.pop()
                self.add(item)
        def select(self, item):
            self.selitem = item

    class CookStatus(store.object):
        def __init__(self):
            self.flavors = {
                "spooky": 0,
                "tension": 0,
                "spirit": 0,
                "wonder": 0
            }
        def update(self, item):
            for flavor in item.flavors:
                if flavor in self.flavors:
                    self.flavors[flavor] += item.flavors[flavor]
                else:
                    self.flavors[flavor] = item.flavors[flavor]
        def result(self, goal, zest): #goal is a {}, zest is a string with the focused attr
            for flavor in goal:
                if self.flavors[flavor] < goal[flavor]:
                    return -1 # did not meet requirements
            if self.flavors[zest] > 100: # perfect score!
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
            "spooky": 999,
            "spirit": 999,
            "tension": 999
        })
    dream_flour = Item("Dream Flour", image = "/images/items/item_kirby.png",
        tooltip="Dream Flour +30 wonder, -20 spirit", 
        flavors={
            "wonder": 30,
            "spooky": 0,
            "spirit": -20,
            "tension": 0
        })
    nightmare_jelly = Item("Nightmare Jelly", image = "/images/items/item_kirby.png",
        tooltip="Nightmare Jelly +40 spooky", 
        flavors={
            "wonder": 0,
            "spooky": 40,
            "spirit": 0,
            "tension": 0
        })
    spooky_jam = Item("Spooky Jam", image = "/images/items/item_kirby.png",
        tooltip="Spooky Jam +30 spooky, +10 wonder", 
        flavors={
            "wonder": 10,
            "spooky": 30,
            "spirit": 0,
            "tension": 0
        })
    galaxy_milk = Item("Galaxy Milk", image = "/images/items/item_kirby.png",
        tooltip="Galaxy Milk +10 spirit, -5 tension", 
        flavors={
            "wonder": 0,
            "spooky": 0,
            "spirit": 10,
            "tension": -5
        })
    haunted_whip = Item("Haunted Whip", image = "/images/items/item_kirby.png",
        tooltip="Haunted Whip +20 spooky, +20 tension", 
        flavors={
            "wonder": 0,
            "spooky": 20,
            "spirit": 0,
            "tension": 20
        })
    
    
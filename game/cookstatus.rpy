#--------------------------------------------------------------------------
# INITIALIZE COOKING INVENTORY
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
        
        def __repr__(self): # for printing
            return str(self.name)

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
            self.smashReq = smashReq # [] list of ideal dish ingredients
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
# COOKING INVENTORY SCREEN
#--------------------------------------------------------------------------
# Required: cook_status - I need to figure out how to save states between investigation/cooking
screen cooking(goal=[], zest=""):
    zorder 2
    modal True

    imagebutton: # go back to dream mode
        idle "goDream"
        hover "goDreamHov"
        mouse "hover"
        focus_mask True
        xalign 0 yalign 0
        action [Hide('cooking'), Jump("dream_case1")]

    textbutton "Reset":
        xalign 0.1 yalign 0.7
        # text_style "temp_button_text"
        action [Function(cook_status.reset), Function(inventory.reset)]

    imagebutton:
        idle "goEat"
        hover "goEatHov"
        mouse "hover"
        focus_mask True
        xalign 0.74 yalign 0.85
        action [Jump("cooking_done")]

    #TODO: add better positions for the inventory, after UI is decided
    $x = 420
    $y = 140
    for i, item in enumerate(inventory.items):
        if i % 3 == 0:
            $ x = 420
            $ y += 140
        # for now border is a seperate image but change later
        imagebutton:
            idle item.image
            xpos x ypos y
            action [Function(inventory.toggleSelect, item), Function(cook_status.update, item)]
            tooltip item
        if item in inventory.selected:
            add "selBorder":
                xpos x-6 ypos y-6
        $ x += 160

    $ tooltip = GetTooltip()
    if tooltip:
        fixed xmaximum 500:
            text "[tooltip.name]":
                xpos 600 ypos 710 #tmp
                xalign 0.5
                color "#000"
            text "[tooltip.tooltip]":
                xpos 600 ypos 760 #tmp
                xalign 0.5
                color "#000"

    # desired stats
    $ y = 0
    for flavor in goal:
        bar value StaticValue(cook_status.flavors[flavor], 100):
            xalign 0.75 ypos 110+y
            xmaximum 400
            ymaximum 4
        # if flavor == zest:
        #     text flavor color '#facade':
        #         xalign 0.6+x yalign 0.45
        # else:
        #     text flavor:
        #         xalign 0.6+x yalign 0.45
        text "{}/{}".format(cook_status.flavors[flavor], goal[flavor]):
            xalign 0.75 ypos 110+y
        $ y += 60

    # combo
    bar value StaticValue(cook_status.combo, 4):
        xalign 0.2 ypos 80
        xmaximum 400
        ymaximum 4
    text "Combo: {}/{}".format(cook_status.combo, 4):
        xalign 0.2 ypos 80

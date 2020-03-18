# generic labels for cooking
label cooking_start:
    hide screen focus_dialogue
    window hide
    $ renpy.pause(hard=True)

#--------------------------------------------------------------------------
# INITIALIZE COOKING INVENTORY
#--------------------------------------------------------------------------
init -1 python:
    class Item(store.object):
        def __init__(self, name, image="", tooltip="", flavor=0):
            self.name = name # name of item
            self.image = image # image url
            self.tooltip = tooltip # tooltip desc
            self.flavor = flavor # {flavor: amount}
        
        def __repr__(self): # for printing
            return str(self.name)

    class Inventory(store.object):
        def __init__(self):
            self.items = []
            self.selected = []
        def add(self, item):
            if item not in self.items:
                self.items.append(item)
        def drop(self, item):
            if item in self.items:
                self.items.remove(item)
        def toggleSelect(self, item):
            if item not in self.selected:
                self.selected.append(item)
            else:
                self.selected.remove(item)
        def reset(self):
            self.selected = []

    class CookStatus(store.object):
        def __init__(self, smashReq, goal, zest):
            self.flavor = 0
            self.combo = 0
            self.smashReq = smashReq # [] list of ideal dish ingredients
            self.goal = goal
            self.zest = zest
            self.smash = False
        def update(self, item, selected):
            total = 0
            if len(selected) > 0:
                for i in selected:
                    total += i.flavor
                self.flavor = total/len(selected)
            else:
                self.flavor = 0
            if item in selected and item in self.smashReq:
                self.combo += 1
            else:
                self.combo = 0
        # def update(self, item):
        #     if item in inventory.selected: # referencing inventory here feels like... bad practice... bUT HEY IT WORKS
        #         self.flavor += item.flavor
        #         if item in self.smashReq:
        #             self.combo += 1
        #         else:
        #             self.combo = 0
        #     else:
        #         self.flavor -= item.flavor
        #         self.combo = 0
        def reset(self):
            self.flavor = 0
            self.combo = 0
        def smashSkill(self, flavor): # simplified my code because what I had before was... overkill to get the job done _(:''3 save for another day
            self.flavor = self.goal
            self.smash = True
        def result(self): #goal is a {}, zest is a string with the focused attr
            result = abs(self.goal - self.flavor)
            if result >= 20:
                    return -1 # did not meet requirements
            if self.smash: # perfect score!
                return 1
            return 0 # ordinary score


#--------------------------------------------------------------------------
# COOKING INVENTORY SCREEN
#--------------------------------------------------------------------------
# Required: inventory, goal, zest
screen cooking(dish):
    zorder -10
    add "cookbook"
    add "cookbook2":
        xalign 0.5 yalign 0.5

    imagebutton: # go back to dream mode
        idle "goDream"
        hover "goDreamHov"
        mouse "hover"
        focus_mask True
        xalign 0 yalign 0
        action [Hide('cooking', transition=Dissolve(.8)), Jump("dream_return")]

    textbutton "Reset":
        xalign 0.8 yalign 0.1
        mouse "hover"
        action [Function(cook_status.reset), Function(inventory.reset)]

    imagebutton:
        idle "goEat"
        hover "goEatHov"
        mouse "hover"
        focus_mask True
        xalign 0.74 yalign 0.85
        action [Call(case+"_cook_done", result=cook_status.result())]

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
            mouse "hover"
            action [Function(inventory.toggleSelect, item), Function(cook_status.update, item, inventory.selected)]
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

    # desired stats, TODO: change the bars after UI is done
    bar value AnimatedValue(cook_status.flavor, 100):
        xalign 0.75 ypos 110
        xmaximum 400
        ymaximum 4
    text "{}/{}".format(cook_status.flavor, goal):
        xalign 0.75 ypos 110

    # combo
    text "Combo: {}".format(cook_status.combo):
        xalign 0.6 ypos 200

    if cook_status.result() == 0:
        add dish:
            xalign 0.7 yalign 0.62
            xanchor 0.5 yanchor 0.5
    elif cook_status.result() == 1:
        add dish+"Best":
            xalign 0.7 yalign 0.62
            xanchor 0.5 yanchor 0.5

    if set(inventory.selected) == set(cook_status.smashReq) and cook_status.combo == len(cook_status.smashReq) and cook_status.smash == False:
        imagebutton:
            idle "images/interactables/kirby.png"
            hover "images/interactables/kirby2.png"
            # action [Jump("smash_"+case), Function(cook_status.smashSkill, zest)] use a jump label when we want to throw in atls
            action [Function(cook_status.smashSkill, zest)]

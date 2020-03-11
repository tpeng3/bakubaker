# 'function' for updating background panning
label lookaround(bg, pos):
    scene expression bg with MoveTransition(1.8, time_warp=quad_time_warp):
        xpos 0 xoffset pos
    $ renpy.show_screen('dream', pos)
    $ renpy.pause(hard=True)

# --------------------------------------------------------------------------
# INITIALIZE INVESTIGATION CHOICES
# --------------------------------------------------------------------------
init -1 python:
    class Interactables(store.object):
        def __init__(self, name, image, page=0, actions={}):
            self.name = name # description of the action
            self.image = image # image url
            self.page = page # page on where the object gets placed
            self.actions = actions # dict of possible actions {actionName: jumpLabel)
            self.viewed = False

        def __repr__(self): # for printing
            return str({"name": self.name, "actions": self.actions})

        def view(self): # do we still need this...? Hm...
            self.viewed = True 

        def enable(self, label): 
            for action in self.actions:
                if action['label'] == label and "condition" in action:
                    action['condition'] = True
            return self
        def disable(self, label):
            for action in self.actions:
                if action['label'] == label and "condition" in action:
                    action['condition'] = False
            return self

    # ease function for panning, god my braincell is terrible at linear algebra though
    def quad_time_warp(x):
      return -2.0 * x**3 + 3.0 * x**2

    class Interactions(store.object):
        def __init__(self, itr_list=[]):
            self.list = itr_list
        def unlock(self, unlocked): # unlocked is a list of unlocked interactions
            for i in unlocked:
                if i not in self.list:
                    self.list.append(i)
        def complete(self, finished): # finished is a list of interactions to be removed
            for i in finished:
                if i in self.list:
                    self.list.remove(i)
        def update(self, interactable):
            for i, itr in enumerate(self.list):
                if itr.name == interactable.name:
                    self.list[i] = interactable


# --------------------------------------------------------------------------
# CUSTOMIZE INVESTIGATION SCREEN
# --------------------------------------------------------------------------
screen goCook():
    # switch to cooking mode
    imagebutton:
        idle "goCook"
        hover "goCookHov"
        xalign 1.0 yalign 0
        focus_mask True
        mouse "hover"
        action [Hide('dream'), Hide('goCook'), Jump('tina3')] # is it bad if I just slap the cooking screen on top
        # TODO: yeah it's bad, I worry about the game slowing down if too many images are loaded so need to look into switching tags?

# Required: interactions, bg, page_width, unlocked_pages- it bugs me that I have to use global variables
screen dream(pos=0):
    zorder -10
    $ mx, my = renpy.get_mouse_pos()

    # image positions are currently determined by "pages", will have to discuss if we want more precise x,y positions
    for i in interactions.list:
        $ actionable = [action for action in i.actions if action.get('condition', True)]
        imagebutton:
            idle i.image
            background
            xpos (i.page * page_width) + pos
            tooltip i
            focus_mask True
            mouse "hover"
            action [If(len(actionable) == 1,
                true = Call(actionable[0]['label']), # if there's only one action, jump immediately to label
                false = Show('dream_actions', actions=actionable, mx=int(mx), my=int(my)))]

    # hover tooltip
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip.name]":
            xalign 0.5 ypos 0.8 #tmp
            xanchor 0.0

    # background panning is divided into "pages" determined by an approximate width of the bg image
    if pos < 0:
        imagebutton:
            idle "goLeft"
            hover "goLeftHov"
            mouse "hover"
            xalign 0.0 yalign 0.5
            action [Hide('dream'), Call('lookaround', bg, pos+page_width)]
    if pos > -(page_width*unlocked_pages): # unlocked pages default at 0, but increases as more gets unlocked
        imagebutton:
            idle "goRight"
            hover "goRightHov"
            xalign 1.0 yalign 0.5
            action [Hide('dream'), Call('lookaround', bg, pos-page_width)]

# TODO: figure out how disable screen when advancing dialogue

# below doesn't work
# screen focus_dialogue:
#     modal True
#     zorder 100

#     frame:
#         area (50,50, 10, 10)
#         background Solid("#000c")
#         $ print "test"


screen dream_actions(actions={}, mx, my):
    # for cancelling/hiding dream_actions if you click away from the menu
    imagebutton:
        idle Solid("#0000")
        action Hide('dream_actions')

    $ ystart = 0
    for action in actions:
        textbutton action['name']:
            xpos mx ypos my+ystart
            xalign 0 yalign 0.5
            mouse "hover"
            action [Hide('dream_actions'), Call(action['label'])]
        $ystart += 40
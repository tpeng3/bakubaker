# below labels are dependent on a global bg and current_page variable that is set in the beginning of each case
label dream_start():
    if finished:
        show screen goCook()
    window hide
    hide screen focus_dialogue
    $ renpy.pause(hard=True)

label dream_return():
    show screen dream()
    jump dream_start

label disable_pause(next_label):
    show screen focus_dialogue # hacky way to disable imagebuttons while dialogue is happening
    jump expression next_label

transform panning(pstart, pend):
    yalign 0.5
    xanchor 0.0
    xpos pstart
    quad 1.8 xpos pend


# --------------------------------------------------------------------------
# INITIALIZE INVESTIGATION CHOICES
# --------------------------------------------------------------------------
init -1 python:
    class Interactables(store.object):
        def __init__(self, name, key, image, page=0, actions={}, state=""):
            self.name = name # description of the action
            self.key = key # name of the interactable since name isn't unique enough
            self.image = image # image url
            self.page = page # page on where the object gets placed
            self.actions = actions # dict of possible actions {actionName: jumpLabel)
            self.state = state # some sort of custom state needed for specific interactables
            self.viewed = False

        def __repr__(self): # for printing
            return str({"name": self.name, "actions": self.actions})

        def view(self):
            self.viewed = True
            return self

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
        def updateState(self, state):
            self.state = state
            return self

    class Interactions(store.object):
        def __init__(self, itr_list=[]):
            self.list = itr_list
        def unlock(self, unlocked): # unlocked is a list of unlocked interactions
            for i in unlocked:
                if i not in self.list:
                    self.list.append(i)
        def complete(self, finished): # finished is a list of interactions to be removed
            for i in finished:
                self.list = [itr for itr in self.list if not (itr.key == i.key)]
        def update(self, interactable): # update an interactable in the interactions list
            for i, itr in enumerate(self.list):
                if itr.key == interactable.key:
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
        action [Hide('dream', transition=Dissolve(.8)), Hide('goCook'), Jump(case+"_cook")]

# Related Global Variables: bg, total_pages, page_width, interactions, unlocked_pages
screen dream():
    default fixedposprev = 0
    default fixedposend = 0
    zorder -10

    fixed:
        at panning(fixedposprev, fixedposend)
        xsize page_width * total_pages
        add bg
        # populate interactables
        for i in interactions.list:
            $ actionable = [action for action in i.actions if action.get('condition', True)]
            imagebutton:
                idle i.image
                xpos (i.page * page_width)
                tooltip i
                focus_mask True
                mouse "hover"
                action [If(len(actionable) == 1,
                    true = [Call("disable_pause", next_label=actionable[0]['label'])], # if there's only one action, jump immediately to label
                    false = Show('dream_actions', actions=actionable, mousepos=renpy.get_mouse_pos()))]

    # hover tooltip
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip.name]":
            xalign 0.5 ypos 0.8 #tmp
            xanchor 0.0
            outlines [
                (0.2, '#14000C'+"22", -1,1), (0.4, '#14000C'+"22", -1,1),  (0.8, '#14000C'+"22", -1,1),
                (1.6, '#14000C'+"11", -1,1), (2.4, '#14000C'+"11", -1,1),  (3.2, '#14000C'+"11", -1,1)
            ]

    # background panning
    if current_page > 0:
        imagebutton:
            idle "goLeft"
            hover "goLeftHov"
            mouse "hover"
            xalign 0.02 yalign 0.5
            action [SetScreenVariable("fixedposprev", -current_page*page_width),
                    SetScreenVariable("fixedposend", (-current_page*page_width)+page_width),
                    SetVariable("current_page", current_page-1)]
    if current_page < unlocked_pages:
        imagebutton:
            idle "goRight"
            hover "goRightHov"
            xalign 0.98 yalign 0.5
            action [SetScreenVariable("fixedposprev", -current_page*page_width),
                    SetScreenVariable("fixedposend", (-current_page*page_width)-page_width),
                    SetVariable("current_page", current_page+1)]

screen focus_dialogue:
    zorder 0
    modal True
    imagebutton:
        idle Solid("#0000")
        action renpy.curry(renpy.end_interaction)(True)
    key "K_SPACE" action renpy.curry(renpy.end_interaction)(True)
 
screen dream_actions(actions={}, mousepos):
    # for cancelling/hiding dream_actions if you click away from the menu
    imagebutton:
        idle Solid("#0000")
        action Hide('dream_actions')
    $ mx, my = mousepos
    if mx > 1700:
        $malign = 1.0
    else:
        $malign = 0.0

    $ ystart = 0
    for action in actions:
        textbutton action['name']:
            xpos mx ypos my+ystart
            xalign malign yalign 0.5
            mouse "hover"
            action [Hide('dream_actions'), Show('focus_dialogue'), Call(action['label'])]
            # outlines [
            #     (0.2, '#14000C'+"22", -1,1), (0.4, '#14000C'+"22", -1,1),  (0.8, '#14000C'+"22", -1,1),
            #     (1.6, '#14000C'+"11", -1,1), (2.4, '#14000C'+"11", -1,1),  (3.2, '#14000C'+"11", -1,1)
            # ]
        $ystart += 40
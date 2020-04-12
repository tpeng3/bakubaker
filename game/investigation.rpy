# GENERIC LABELS
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

# SCREEN STYLES
style dreamacts is button:
    xminimum 524
    ysize 104
    padding (10, 10, 10, 10)
    background Frame("itrFrame", Borders(5, 1, 5, 1), tile=False)

style dreamacts_text is button_text:
    xalign 0.5
    yalign 0.5
    font persistent.pref_text_font
    idle_color "#EDD9C8"
    hover_color "#facade"
    outlines [
                (0.2, '#14000C'+"22", -1,1), (0.4, '#14000C'+"22", -1,1),  (0.8, '#14000C'+"22", -1,1),
                (1.6, '#14000C'+"11", -1,1), (2.4, '#14000C'+"11", -1,1),  (3.2, '#14000C'+"11", -1,1)
             ]

# SCREEN TRANSFORMATIONS
transform panning(pstart, pend):
    yalign 0.5
    xanchor 0.0
    xpos pstart
    quad 2.8 xpos pend

transform dreamfade(delay=0):
    alpha 0.0
    xoffset 30
    pause delay
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        linear 0.6 xoffset 0

transform itrfade():
    alpha 0.0
    linear 0.8 alpha 1.0

transform arrowleft():
    alpha 0.0 xalign 0.00
    pause 2.0
    linear 0.8 alpha 1.0 xalign 0.02

transform arrowright():
    alpha 0.0 xalign 0.995
    pause 2.0
    linear 0.8 alpha 1.0 xalign 0.98
    
# --------------------------------------------------------------------------
# INITIALIZE INVESTIGATION CHOICES
# --------------------------------------------------------------------------
init -1 python:
    class Interactables(store.object):
        def __init__(self, name, key, image, page=0, xstart=0, ystart=0, actions={}, state=""):
            self.name = name # description of the action
            self.key = key # name of the interactable since name isn't unique enough
            self.image = image # image url
            self.page = page # page on where the object gets placed
            self.xstart = xstart # top left corner position of image
            self.ystart = ystart
            self.actions = actions # dict of possible actions {actionName: jumpLabel)
            self.state = state # some sort of custom state needed for specific interactables
            self.viewed = False

        def __repr__(self): # for debug printing
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
        def updateImage(self, image, xpos=None, ypos=None):
            self.image = image
            if xpos:
                self.xstart = xpos
            if ypos:
                self.ystart = ypos
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
        hover_sound "audio/sfx/menuhover.ogg"
        activate_sound "audio/sfx/select.ogg"
        action [Hide('dream', transition=Dissolve(.8)), Hide('goCook'), Jump(case+"_cook")]

# Related Global Variables: bg, total_pages, page_width, interactions, unlocked_pages
screen dream():
    default fixedposprev = 0
    default fixedposend = 0
    default current_page = 0
    zorder -10

    fixed:
        at panning(fixedposprev, fixedposend)
        xsize page_width * total_pages
        add bg
        # populate interactables
        for i in interactions.list:
            $ actionable = [action for action in i.actions if action.get('condition', True)]
            if len(actionable) < 1:
                image i.image:
                    xpos (i.page * page_width) + i.xstart
                    ypos i.ystart
                    at itrfade()
            else:
                imagebutton:
                    idle i.image
                    xpos (i.page * page_width) + i.xstart
                    ypos i.ystart
                    tooltip i
                    focus_mask True
                    mouse "hover"
                    at itrfade()
                    action [If(len(actionable) == 1,
                        true = [Call("disable_pause", next_label=actionable[0]['label'])], # if there's only one action, jump immediately to label
                        false = Show('dream_actions', actions=actionable, mousepos=renpy.get_mouse_pos()))]

    # hover tooltip
    $ tooltip = GetTooltip()
    if tooltip:
        window:
            xalign 0.5 yalign 0.9
            xsize 524 ysize 104
            text "[tooltip.name]":
                xalign 0.5 yalign 0.5
                color "#EDD9C8"
                outlines [
                    (0.2, '#14000C'+"22", -1,1), (0.4, '#14000C'+"22", -1,1),  (0.8, '#14000C'+"22", -1,1),
                    (1.6, '#14000C'+"11", -1,1), (2.4, '#14000C'+"11", -1,1),  (3.2, '#14000C'+"11", -1,1)
                ]
            background Transform("itrFrame", alpha=persistent.say_window_alpha)

    # background panning
    if current_page > 0:
        imagebutton:
            idle "goLeft"
            hover "goLeftHov"
            mouse "hover"
            hover_sound "audio/sfx/menuhover.ogg"
            activate_sound "audio/sfx/select.ogg"
            xalign 0.02 yalign 0.5
            at arrowleft()
            action [SetScreenVariable("fixedposprev", -current_page*page_width),
                    SetScreenVariable("fixedposend", (-current_page*page_width)+page_width),
                    SetScreenVariable("current_page", current_page-1)]
    if current_page < unlocked_pages:
        imagebutton:
            idle "goRight"
            hover "goRightHov"
            hover_sound "audio/sfx/menuhover.ogg"
            activate_sound "audio/sfx/select.ogg"
            xalign 0.98 yalign 0.5
            at arrowright()
            action [SetScreenVariable("fixedposprev", -current_page*page_width),
                    SetScreenVariable("fixedposend", (-current_page*page_width)-page_width),
                    SetScreenVariable("current_page", current_page+1)]

screen focus_dialogue:
    zorder 0
    modal True
    imagebutton:
        idle Solid("#0000")
        action renpy.curry(renpy.end_interaction)(True)
    key "K_SPACE" action renpy.curry(renpy.end_interaction)(True)

screen get_ingredient(ingredient):
    zorder -1
    add "ingFrame":
        xalign 0.5
        yalign 0.5
    add "[ingredient]":
        xalign 0.5
        yalign 0.5
 
screen dream_actions(actions={}, mousepos):
    # for cancelling/hiding dream_actions if you click away from the menu
    imagebutton:
        idle Solid("#0000")
        action Hide('dream_actions')

    $ mx, my = mousepos
    if mx > gui.width - 530:
        $ mx = mx - 530
    if my > gui.height - (120 * len(actions)):
        $ my = my - (120 * len(actions))

    $ ystart = 0
    $ delay = 0

    vbox:
        xpos mx+10 ypos my
        spacing 10

        for action in actions:
            button:
                mouse "hover"
                hover_sound "audio/sfx/menuhover.ogg"
                activate_sound "audio/sfx/select.ogg"
                style "dreamacts"
                text action['name']:
                    style "dreamacts_text"
                action [Hide('dream_actions'), Show('focus_dialogue'), Call(action['label'])]
                at dreamfade(delay)
            $delay += 0.2
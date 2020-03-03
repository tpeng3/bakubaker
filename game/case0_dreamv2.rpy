label tina2:
    $ inventory = Inventory()
    $ finished = False
    # have to initialize scene bg as an expression for lookaround to work later
    $ bg = "dreamland"
    scene expression bg:
        xalign 0.5
    "I don't have anything here yet... but I will..."
    show screen dream_test2()
    jump dream_start2

label dream_start2:
    if finished:
        "OK I think I have a good idea of what to make."
        "Time to head back to the kitchen!"
        return
    window hide
    $ renpy.pause(hard=True)

label kirby_talk:
    if kirby not in inventory.items:
        $ inventory.add(kirby)
        "Hi Kirby!"
        "Kirby doesn't respond because they're a sticker."
    else:
        "It's just another day for Kirby in Dreamland..."
    jump dream_start2
    
label kirby_steal:
    "Now why would you want to do that?"
    jump dream_start2

screen dream_test2(pos=0):
    zorder -10
    $ mx, my = renpy.get_mouse_pos()
    $ screenName = 'dream_test2'
    $ bg = "dreamland"

    # kirby
    imagebutton:
        idle t_kirby.image
        xpos 360+pos yalign 0.55
        tooltip t_kirby.tooltip
        focus_mask True
        action [Show('dream_actions', actions=t_kirby.actions, mx=int(mx), my=int(my))]

    # image tooltip
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            xalign 0.2 ypos 0.2 #tmp
    

    # inventory button
    # technically we can (or should?) put this on a seperate screen
    imagebutton:
        idle "gui/button/button_thoughts.png"
        hover im.MatrixColor("gui/button/button_thoughts.png", im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0))
        xalign 1.0 yalign 0
        action [ToggleScreen('inventory')]

    # right now bg panning is updated by pos but we can also do align %, it's a matter of preference
    # TODO: calculate background position to hide the arrows accordingly
    $ a = renpy.get_image_bounds(bg)
    $ print a
    $ print pos

    # if pos >= 0:
    textbutton "Go left":
        xalign 1 yalign 0.5
        # xanchor 0 yanchor 0.5
        action [Hide(screenName), Call('lookaround', screenName, bg, pos+200)]
    # if pos <= gui.width:
    textbutton "Go right":
        xalign 0.8 yalign 0.5
        # xanchor 1 yanchor 0.5
        action [Hide(screenName), Call('lookaround', screenName, bg, pos-200)]


screen dream_actions(actions={}, mx, my):
    # TODO: hide dream_actions when player clicks away from the "menu"
    $ ystart = 0
    for action in actions:
        textbutton action:
            xpos mx ypos my+ystart
            xalign 0 yalign 0.5
            action [Hide('dream_actions'), Call(actions[action])]
        $ystart += 40

label tina:
    menu:
        "version 1 (page panning, hover outline click)":
            jump tina1
        "version 2 (hover tooltip, multiple actions options)":
            jump tina2

label tina1:
    $ inventory = Inventory()
    $ finished = False
    # have to initialize scene bg as an expression for lookaround to work later
    $ bg = "dreamland"
    scene expression bg:
        xalign 0.5
    show screen dream_test()
    jump dream_start

label dream_start:
    if finished:
        "OK I think I have a good idea of what to make."
        "Time to head back to the kitchen!"
        return
    window hide
    $ renpy.pause(hard=True)

label kirby:
    if kirby not in inventory.items:
        $ inventory.add(kirby)
        "Oh hey it's Kirby!"
        "what a good boi..."
    else:
        "It's just another day for Kirby in Dreamland..."
    jump dream_start
    

screen dream_test(pos=0):
    zorder -10

    # kirby
    imagebutton:
        idle "images/BG/bg_dreamland_kirby.png"
        hover "images/BG/bg_dreamland_kirby2.png"
        xpos 360+pos yalign 0.55
        focus_mask True
        action Jump('kirby')


    # inventory button
    # technically we can (or should?) put this on a seperate screen
    imagebutton:
        idle "gui/button/button_thoughts.png"
        hover im.MatrixColor("gui/button/button_thoughts.png", im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0))
        xalign 1.0 yalign 0
        action [ToggleScreen('inventory')]

    # right now bg panning is updated by pos but we can also do align %, it's a matter of preference
    # TODO: calculate background position to hide the arrows accordingly
    # if not pos >= 0:
    textbutton "Go left":
        xalign 1 yalign 0.5
        # xanchor 0 yanchor 0.5
        action [Hide('dream_test'), Call('lookaround', 'dream_test', 'dreamland', pos+200)]
    # if not pos <= gui.width:
    textbutton "Go right":
        xalign 0.8 yalign 0.5
        # xanchor 1 yanchor 0.5
        action [Hide('dream_test'), Call('lookaround', 'dream_test', 'dreamland', pos-200)]

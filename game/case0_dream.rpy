label tina:
    menu:
        "version 1 (page panning, hover outline click)":
            jump tina1
        "version 2 (hover tooltip, multiple actions options)":
            jump tina2
        "Hell's Kitchen":
            jump tina3

label tina1:
    $ inventory = Inventory()
    $ finished = False
    # have to initialize scene bg as an expression for lookaround to work later
    $ bg = "dreamland"
    scene expression bg:
        xalign 0.5
    "This version of dream has hover icons"
    show screen investigation()
    show screen dream_test()
    jump dream_start

label dream_start:
    if finished:
        "OK I think I have a good idea of what to make."
        "Time to head back to the kitchen!"
        jump tina3
    window hide
    $ renpy.pause(hard=True)

label kirby:
    if kirby not in inventory.items:
        $ inventory.add(kirby)
        dreamSom "Oh hey it's Kirby!"
        dreamSom "what a good boi..."
    else:
        "It's just another day for Kirby in Dreamland..."
    jump dream_start

label strawberry:
    dreamRem "That's an awfully large strawberry."
    jump dream_start
    

screen dream_test(pos=0):
    $ screenName = 'dream_test'
    zorder -10
    
    # TODO: make a dict map of all the imagebuttons? need to do research if that's the cleaner way to go about it
    # TODO: hide imagebuttons/labels so player doesn't accidentally click on them when viewing dialogue
    # kirby
    imagebutton:
        idle "images/BG/bg_dreamland_kirby.png"
        # hover "images/BG/bg_dreamland_kirby2.png" # if there's hover icons do we still want an outline?
        mouse "somnia"
        xpos 360+pos yalign 0.55
        focus_mask True
        action [Jump('kirby')]

    # strawberry
    imagebutton:
        idle "images/BG/bg_dreamland_strawberry.png"
        mouse "remerie"
        xpos 360+pos yalign 0.55
        focus_mask True
        action [Jump('strawberry')]

    # right now bg panning is updated by pos but we can also do align %, it's a matter of preference
    # TODO: calculate background position to hide the arrows accordingly
    # if not pos >= 0:
    textbutton "Go left":
        xalign 1 yalign 0.5
        # xanchor 0 yanchor 0.5
        action [Hide(screenName), Call('lookaround', 'dream_test', 'dreamland', pos+200)]
    # if not pos <= gui.width:
    textbutton "Go right":
        xalign 0.8 yalign 0.5
        # xanchor 1 yanchor 0.5
        action [Hide(screenName), Call('lookaround', 'dream_test', 'dreamland', pos-200)]
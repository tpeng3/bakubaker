label dream_case1:
    $ interaction = [t_kirby, t_rabbit, t_clocktower, t_strawberry, t_client]
    $ inventory = Inventory()
    $ finished = False
    # have to initialize scene bg as an expression for lookaround to work later
    $ bg = "wonderland"
    scene expression bg:
        xpos 0
    "Case 1 (tutorial) dream"
    $ interaction = [t_kirby, t_rabbit, t_clocktower, t_strawberry]
    show screen investigation()
    show screen dream_wonderland()
    jump dream_start1

label dream_start1:
    if finished:
        "OK I think I have a good idea of what to make."
        "Time to head back to the kitchen!"
        jump tina3
    window hide
    $ renpy.pause(hard=True)

label rabbit:
    "I'm late! I'm late!"
    $ interaction.pop()
    dreamRem neutral "I wonder what's the hurry..."
    jump dream_start1

label client:
    "*Mumble mumble...*"
    dreamSom neutral "There they are!"
    "*NYOOMS*"
    $ interaction = [t_kirby, t_rabbit, t_clocktower, t_strawberry]
    hide rabbitOne with fade
    dreamSom "Oh noooooooooo"
    jump dream_start1

label clocktower_time:
    "The time is 4:20"
    dreamSom "Blaze it."
    jump dream_start1

label clocktower_hands:
    dreamRem "Ghk... I can't move the hands."
    dreamSom "Time waits for no one."
    jump dream_start1

label clocktower_enter:
    dreamSom "Rumors say a great treasure is hidden inside the Ghost Tower."
    "Against proper judgement, you enter inside..."
    hide screen investigation
    hide screen dream_wonderland
    scene black with Dissolve(2.0)
    $ renpy.pause(2.0)
    jump tina3

label strawberry_look:
    dreamSom "That's a huge strawberry..."
    jump dream_start1

label strawberry_eat:
    if c_strawberry not in inventory.items:
        dreamSom "Oh I love strawberries!"
        $ inventory.add(c_strawberry)
        "Strawberry added to inventory."
    else:
        dreamRem "I wonder what we can make with this strawberry..."
    jump dream_start1


screen dream_wonderland(pos=0):
    zorder -10
    # TODO: look up if we should use tags to organize screens
    $ mx, my = renpy.get_mouse_pos()
    $ screenName = 'dream_wonderland'
    $ bg = "wonderland"
    

    # a part of my brain is screaming that I shouldn't make images with such large transparent pixels
    # this is my version of duct tape code, we can split interactions by "pages" afterwards if needed
    for i in interaction:
        imagebutton:
            idle i.image
            background
            # hover i.hover if we still want to do hover outlines
            xpos 3406+pos # calculate better positions later
            tooltip i
            focus_mask True
            mouse "hover"
            action [Show('dream_actions', actions=i.actions, mx=int(mx), my=int(my))]

    # image tooltip
    $ tooltip = GetTooltip()
    if tooltip:
        # image "[tooltip.icon]":
        #     xalign 0.48 ypos 0.8
        #     xanchor 1.0
        text "[tooltip.name]":
            xalign 0.5 ypos 0.8 #tmp
            xanchor 0.0


    # right now bg panning is updated by pos but we can also do align %, it's a matter of preference
    # TODO: calculate background position to hide the arrows accordingly
    # right now, I only did some manual calculations
    if pos < 0:
        imagebutton:
            idle "goLeft"
            hover "goLeftHov"
            mouse "hover"
            xalign 0.0 yalign 0.5
            action [Hide(screenName), Call('lookaround', screenName, bg, pos+1660)]
    if pos > -3320: # bg_wonderland width - 1660
        imagebutton:
            idle "goRight"
            hover "goRightHov"
            xalign 1.0 yalign 0.5
            action [Hide(screenName), Call('lookaround', screenName, bg, pos-1660)]



# doesn't work
# screen focus_dialogue:
#     modal True
#     zorder 100

#     frame:
#         area (50,50, 10, 10)
#         background Solid("#000c")
#         $ print "test"

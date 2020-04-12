# Positions -------------------------------------------------------------------
# So the bakus are positioned comfortably in their respective sides
transform left:
    yalign 1.0
    xalign -0.10
transform right:
    yalign 1.0
    xalign 1.05

transform blinking():
    alpha 0.0
    pause 1.0
    block:
        alpha 0.0
        pause 0.8
        linear 0.8 alpha 1.0
        pause 2.0
        linear 0.5 alpha 0.0
        repeat

# ATL
label splash_transition:
    show menuSplash:
        alpha 1.0
        pause(0.5)
        linear 1.0 alpha 0.0
    show menuFront:
        xalign 0.15 yalign 0.5
        easein_quad 2.0 xalign 0.85
    pause(2.5)
    return

label titlezone:
    show outside with dissolve:
        xanchor 0 yanchor 0
    show logo:
        alpha 0.0
        xalign 0.5 yalign 0.5
        zoom 0.8
        linear 0.5 alpha 1.0
        linear 3.0 zoom 1.0
        pause 1.0
        linear 2.0 alpha 0.0
    $ renpy.pause(delay=5, hard=True)
    play music storefront
    show outside:
        pause 5.0
        xanchor 0 yanchor 0
        xpos 0 ypos 0
        ease_quad 10.0 xpos 0 ypos -1080
    $ renpy.pause(delay=3, hard=False)
    return

label endscene:
    show outside:
        xanchor 0 yanchor 0
        xpos 0 ypos -1080
        xalign 0.5 yalign 0.85
    show fin:
        alpha 0.0
        xpos 0.5 ypos 0.5
        linear 4.0 alpha 1.0
    show outside:
        xanchor 0 yanchor 0
        xpos 0 ypos -1080
        xalign 0.5 yalign 0.85
        ease_quad 15.0 yalign 0.0
    $ renpy.pause(delay=20, hard=True)
    scene black with Dissolve(1.0)

label intodream:
    show enterdream:
        xanchor 0 yanchor 0
        xpos 0 ypos -2000
        ease_quad 8.0 ypos 0
    pause (8.0)
    play sound whoosh fadeout 1.0
    show cloud with dissolve
    return

image fin = Text("{size=50}{i}Thank you for playing!{/s}{/i}")

# Main Menu --------------------------------------------------------------------
transform back_clouds():
    xpos 0 ypos 0
    linear 2.0 ypos -20
    pause 0.5
    linear 2.0 ypos 0
    repeat

transform main_clouds():
    alpha 1.0
    choice:
        linear 3.0 alpha 0.30
        pause 0.2
        linear 2.5 alpha 1.0
    choice:
        linear 3.0 alpha 0.50
        pause 0.25
        linear 2.0 alpha 1.0
    repeat

# Splash screen ----------------------------------------------------------------
transform floating():
    choice:
        linear 1.6 ypos 20
        pause 0.2
        linear 1.6 ypos 12
    choice:
        linear 2.0 ypos 30
        pause 0.3
        linear 2.0 ypos 45
    choice:
        linear 1.6 ypos 20
        pause 0.2
        linear 1.8 ypos 45
    choice:
        linear 2.0 ypos 30
        pause 0.2
        linear 1.6 ypos 12
    pause 0.25
    repeat

define flash = Fade(.10, 0.0, .20, color="eee6d1")

# Cookin splashes!!! -----------------------------------------------------------
image cutin:
    contains:
        alpha 0.0
        "gui/overlay/confirm.png"
        ease 0.5 alpha 1.0
        pause 5.0
        ease 0.5 alpha 0.0
    contains:
        anchor (0.5,0.5)
        alpha 0.2 xpos -1.0 ypos 0.5
        "images/CG/smash.png"
        alpha 1.0
        ease_quad 1.0 xpos 0.5
        "images/CG/smash.png"
        pause 0.20
        linear 0.05 ypos 0.51
        "images/CG/smash1.png" with Dissolve(0.3, alpha=True)
        linear 0.05 ypos 0.5
        pause 0.35
        linear 0.05 ypos 0.51
        "images/CG/smash2a.png" with Dissolve(0.3, alpha=True)
        linear 0.05 ypos 0.5
        linear 0.10 zoom 1.5 truecenter
        "images/CG/smash2b.png"
        linear 0.15 zoom 1
        block:
            "images/CG/smash2a.png" with Dissolve(0.3, alpha=True)
            pause 0.30
            "images/CG/smash2b.png" with Dissolve(0.3, alpha=True)
            pause 0.30
            repeat 2
        "images/CG/smash2b.png" with Dissolve(0.5, alpha=True)
        linear 1.0 alpha 0.0

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
    show cloud with dissolve
    return

image fin = Text("{size=50}{i}Thank you for playing!{/s}{/i}")

# Main Menu --------------------------------------------------------------------
transform main_clouds():
    alpha 1.0 
    linear 3.0 alpha 0.30
    pause 0.2
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

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
    $ main_menu = True
    show screen main_menu with Dissolve(1.0)

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
        xanchor 0 yanchor 0
        xpos 0 ypos 0
        ease_quad 10.0 xpos 0 ypos -1080
    $ renpy.pause(delay=3, hard=False)
    return

# Main Menu --------------------------------------------------------------------
image main_menu_ani:
    contains:
        "gui/main_menu.png"
    contains:
        anim.Filmstrip ("images/cg/poppin.png", (1920,1080), (1,3), 0.20, loop=True)

# Splash screen ----------------------------------------------------------------
image splash_menu_ani:
    contains:
        anim.Filmstrip ("images/cg/poppin.png", (1920,1080), (1,3), 0.20, loop=True)
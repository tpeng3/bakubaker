# ATL shengigans I don't know where to PUT

image logo:
    "images/CG/logo.png"

image outside:
    "images/CG/outside.png"

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

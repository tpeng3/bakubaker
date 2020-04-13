# CREDITS SCREEN (we made it guys!!)

# Credits styles
style credits_style_text:
    xalign 0.0
    font persistent.pref_text_font
    idle_color "#EDD9C8"
    outlines [
                (0.2, '#14000C'+"22", -1,1), (0.4, '#14000C'+"22", -1,1),  (0.8, '#14000C'+"22", -1,1),
                (1.6, '#14000C'+"11", -1,1), (2.4, '#14000C'+"11", -1,1),  (3.2, '#14000C'+"11", -1,1)
             ]

# transform dropdown:
#     alpha 0.0
#     xpos 1000 ypos -300
#     ease_quad 3.0 ypos 180 alpha 1.0

transform creditsfade(delay=0):
    alpha 0.0
    xoffset 50
    pause delay
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        linear 0.6 xoffset 0

transform slideright:
    xpos -800 ypos 0 alpha 0.0 # need to change positions afterwards
    ease_quad 2.0 xpos -400 alpha 1.0

screen credits():
    default pagenum = 0
    default page_order = ["credits_cynthia", "credits_jay", "credits_tina", "credits_other"]

    modal True
    add "images/CG/incense_in.png"
    style_prefix "credits_style"

    use expression page_order[pagenum]

    if pagenum < len(page_order):
        imagebutton:
            idle Solid("#0000")
            activate_sound 'audio/sfx/itemget.ogg'
            action [Hide("credits_cynthia", transition=Dissolve(0.8)), SetScreenVariable("pagenum", pagenum+1)]
    else:
        imagebutton:
            idle Solid("#0000")
            activate_sound 'audio/sfx/itemget.ogg'
            action MainMenu()

label credit_roll:
    show screen credits() with Dissolve(2.0)
    $ renpy.pause(delay=2, hard=False)


screen credits_cynthia():
    image "images/CG/smash.png":
        at slideright

    vbox:
        xalign 0.85
        yalign 0.45
        xmaximum 800

        $ delay = 3.0
        for field in cynthia_page:
            text field:
                at creditsfade(delay)
            $ delay += 0.5

screen credits_jay():
    image "images/CG/smash.png":
        at slideright

    vbox:
        xalign 0.85
        yalign 0.45
        xmaximum 800

        $ delay = 3.0
        for field in jay_page:
            text field:
                at creditsfade(delay)
            $ delay += 0.5

screen credits_tina():
    image "images/CG/smash.png":
        at slideright

    vbox:
        xalign 0.85
        yalign 0.45
        xmaximum 800

        $ delay = 3.0
        for field in tina_page:
            text field:
                at creditsfade(delay)
            $ delay += 0.5

screen credits_other():
    image "images/CG/smash.png":
        at slideright

    vbox:
        xalign 0.85
        yalign 0.45
        xmaximum 800

        $ delay = 3.0
        for field in tina_page:
            text field:
                at creditsfade(delay)
            $ delay += 0.5


init python:
    cynthia_page = [
        "{size=60}Cynthia!!!!!!{/s}",
        "Rascally Enthusiast",
        "Washed: hands \nStayed: inside \nDidn't do a good job with this credits screen lol the code is Not Great",
        "Quote: Simple zest for life",
        "{ii}Tina please god help me clean this up{/ii}"
    ]

    jay_page = [
        "{size=60}JAY{/s}"
    ]

    tina_page = [
        "{size=60}Tina{/s}",
        "A Simple Frog",
        "Status: Probably shouldn't be staying up this late right now but the concept of time is fake.",
        "If two guys were on the moon and one killed the other with a rock would that be fucked up or what-",
        "{ii}OK I cleaned some parts but it's subject to change when we get these fields figured out.{/ii}"
    ]

    other_page = [
        "{size=60}Resources{/s}",
    ]
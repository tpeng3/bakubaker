# CREDITS SCREEN (we made it guys!!)
label credits_start:
    $ show_quick_menu = False
    show screen block_clicking
    show image "#D8CBC5"
    show screen credits_cynthia
    pause(14.0)
    hide screen credits_cynthia with Dissolve(0.8)
    show screen credits_jay
    pause(14.0)
    hide screen credits_jay with Dissolve(0.8)
    show screen credits_tina
    pause(14.0)
    hide screen credits_tina with Dissolve(0.8)
    show screen credits_other
    pause(14.0)
    hide screen credits_other with Dissolve(0.8)
    show image "#000" with Dissolve(0.8)
    show screen credits_thanks
    pause(10.0)
    hide screen credits_thanks with Dissolve(0.8)
    scene black with Dissolve(0.8)
    hide screen block_clicking
    $ MainMenu(confirm=False)()
    return

return

# Credits styles
# style credits_style_text:
#     idle_color "#B15B76"
#     outlines [
#                 (0.2, '#14000C'+"22", -1,1), (0.4, '#14000C'+"22", -1,1),  (0.8, '#14000C'+"22", -1,1),
#                 (1.6, '#14000C'+"11", -1,1), (2.4, '#14000C'+"11", -1,1),  (3.2, '#14000C'+"11", -1,1)
#              ]


transform creditsfade(delay=0):
    alpha 0.0
    xoffset 50
    pause delay
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        linear 0.6 xoffset 0

transform slideright:
    xpos 0 ypos 30 alpha 0.0
    ease_quad 2.0 xpos 100 alpha 1.0
transform slideleft:
    xpos 1200 ypos 0 alpha 0.0
    ease_quad 2.0 xpos 900 alpha 1.0
transform slidedown:
    zoom 0.8
    xpos 375 ypos 20 alpha 0.0
    ease_quad 2.0 ypos 80 alpha 1.0
transform inthecenter:
    zoom 0.8
    xpos 375 ypos 40 alpha 0.0
    ease_quad 2.0 alpha 1.0

screen credits_cynthia():
    zorder 99
    modal True
    image "images/CG/credits_cy.png":
        xoffset -20
        yoffset 10
        at slideright

    vbox:
        xalign 0.8
        yalign 0.45
        xmaximum 700

        $ delay = 3.0
        for field in cynthia_page:
            text field:
                color "#B15B76"
                at creditsfade(delay)
            $ delay += 0.5

screen credits_jay():
    zorder 99
    modal True
    image "images/CG/credits_j.png":
        yoffset 80
        at slideleft

    vbox:
        xalign 0.2
        yalign 0.45
        xmaximum 700

        $ delay = 3.0
        for field in jay_page:
            text field:
                color "#B15B76"
                at creditsfade(delay)
            $ delay += 0.5

screen credits_tina():
    zorder 99
    modal True
    image "images/CG/credits_t.png":
        xoffset -110
        yoffset 50
        at slideright

    vbox:
        xalign 0.8
        xoffset 200
        yalign 0.45
        xmaximum 700

        $ delay = 3.0
        for field in tina_page:
            text field:
                color "#B15B76"
                at creditsfade(delay)
            $ delay += 0.5

screen credits_other():
    zorder 99
    modal True
    image "images/CG/them.png":
        xoffset 200
        yoffset 400
        at slideleft

    vbox:
        xalign 0.25
        yalign 0.45
        xmaximum 800

        $ delay = 3.0
        for field in other_page:
            text field:
                color "#B15B76"
                at creditsfade(delay)
            $ delay += 0.5

screen credits_thanks():
    zorder 99
    modal True
    image "images/CG/thanks.png":
        at inthecenter

    image "images/CG/thankswords.png":
        xalign 0.5
        xoffset 640
        at slidedown

screen block_clicking():
    zorder 100
    modal True
    imagebutton:
        idle Solid("#0000")
        action NullAction()


init python:
    cynthia_page = [
        "{size=60}Cynthia{/s} - A Maverick" ,
        "{ii}Deranged Black Metal Girl Scout{/ii}",
        "Art:",
        " • Background art \n • Character concepts \n • Character design \n • Prop art",
        "Programming:",
        " • Animation \n • Visual novel section",
        "Narrative writing",
        "{qq}\"I got myself a paperclip.\"{/qq}"
    ]

    jay_page = [
        "{size=60}J{/s} - Idea {s}Gay{/s} Guy",
        "{ii}Humble Merchant of Somrems{/ii}",
        "Art:",
        " • Character art \n • Character design \n • UI design",
        "Story concept",
        "Story revision",
        "{qq}\"Pitched corny JRPG title \"Bon Appétit: Karmic Unrest\" for the BAKU acronym but alas...\"{/qq}"
    ]

    tina_page = [
        "{size=60}Tina{/s} - Hacky Code Enthusiast",
        "{ii}A Simple Frog{/ii}",
        "Character writing",
        "Programming:",
        " • Animation \n • Cooking section \n • Dream section",
        "Sound effects",
        "{qq}\"I hope you liked my clock puzzle that gave no helpful visual indicators whatsoever (I'm sorry)\"{/qq}"
    ]

    other_page = [
        "{size=60}Resources{/s}",
        "Open source music provided by:",
        "{a=http://amachamusic.chagasi.com/index.html}Amacha Music{/a}: {font=gui/fonts/MPLUS-light.ttf}午前2時の噴水{/font}",
        "{a=http://www.hmix.net/music_gallery/music_top.html}H/MIX Gallery{/a}: {font=gui/fonts/MPLUS-light.ttf}移動式井戸{/font}",
        "{a=http://musmus.main.jp/music.html}MusMus:{/a}",
        " • {font=gui/fonts/MPLUS-light.ttf}なめこ大臣の策謀 \n • 朝露の小庭{/font}",
        "{a=https://pocket-se.info/}Pocket Sound{/a}: {font=gui/fonts/MPLUS-light.ttf}やっぱりチョコは手作りね{/font}",
        "{a=https://www.soundofpicture.com/}Podington Bear:{/a}",
        " • Netherland \n • Peas Corps \n • Thick Irony",
        "Ren'Py GUI template provided by:",
        "{a=https://tofurocks.itch.io/renpy-gui-template}tofurocks{/a}",

    ]

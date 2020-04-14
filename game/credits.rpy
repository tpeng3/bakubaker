# CREDITS SCREEN (we made it guys!!)
label credits_start:
    scene Solid("#D8CBC5")
    show screen credits_cynthia
    pause(10.0)
    show screen credits_jay
    pause(10.0)
    show screen credits_tina
    pause(10.0)
    show screen credits_other
    pause(10.0)
    # show screen credits(pagenum=4) a thanks for playing! screen
    # pause(10.0)
return

image creditsBG = "#D8CBC5"

# Credits styles
style credits_style_text:
    xalign 0.0
    font persistent.pref_text_font
    idle_color "#EDD9C8"
    outlines [
                (0.2, '#14000C'+"22", -1,1), (0.4, '#14000C'+"22", -1,1),  (0.8, '#14000C'+"22", -1,1),
                (1.6, '#14000C'+"11", -1,1), (2.4, '#14000C'+"11", -1,1),  (3.2, '#14000C'+"11", -1,1)
             ]


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
transform inthecenter:
    zoom 0.8
    xpos 375 ypos 70 alpha 0.0
    ease_quad 2.0 alpha 1.0

screen credits(pagenum=0):
    modal True
    add "creditsBG"
    style_prefix "credits_style"
    $ page_order = ["credits_cynthia", "credits_jay", "credits_tina", "credits_other", "credits_thanks"]

    if pagenum < len(page_order)-1:
        use expression page_order[pagenum]

        imagebutton:
            idle Solid("#0000")
            activate_sound 'audio/sfx/itemget.ogg'
            action [Hide("credits_cynthia", transition=Dissolve(0.8)), SetScreenVariable("pagenum", pagenum+1)]
    else:
        use expression page_order[pagenum]

        imagebutton:
            idle Solid("#0000")
            activate_sound 'audio/sfx/itemget.ogg'
            action [Hide("creditsfade", transition=Dissolve(0.8)), MainMenu(confirm=False)]

screen credits_cynthia():
    image "images/CG/credits_cy.png":
        at slideright

    vbox:
        xalign 0.75
        yalign 0.45
        xmaximum 800

        $ delay = 3.0
        for field in cynthia_page:
            text field:
                at creditsfade(delay)
            $ delay += 0.5

screen credits_jay():
    image "images/CG/credits_j.png":
        at slideleft

    vbox:
        xalign 0.25
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
        xalign 0.75
        yalign 0.45
        xmaximum 800

        $ delay = 3.0
        for field in tina_page:
            text field:
                at creditsfade(delay)
            $ delay += 0.5

screen credits_other():
    image "images/CG/them.png":
        at slideleft

    vbox:
        xalign 0.25
        yalign 0.45
        xmaximum 800

        $ delay = 3.0
        for field in other_page:
            text field:
                at creditsfade(delay)
            $ delay += 0.5

screen credits_thanks():
    image "images/CG/thanks.png":
        at inthecenter

    vbox:
        xalign 0.5
        yalign 0.5
        xmaximum 800

        $ delay = 3.0
        for field in other_page:
            text field:
                at creditsfade(delay)
            $ delay += 0.5

init python:
    cynthia_page = [
        "{size=60}Cynthia{/s} - A Maverick" ,
        "{ii}Deranged Black Metal Girl Scout{/ii}",
        "Art:",
        " • Background art \n • Character concepts \n • Character design \n • Prop art",
        "Programming:",
        " • Animation \n • Visual novel section",
        "Narrative writing",
        "{i}\'I got myself a paperclip.\'{/i}"
    ]

    jay_page = [
        "{size=60}J{/s} - Idea {s}Gay{/s} Guy",
        "{ii}Humble Merchant of Somrems{/ii}",
        "Art:",
        " • Character art \n • Character design \n • UI design",
        "Story concept",
        "Story revision",
        "{i}\'Pitched corny JRPG title \"Bon Appétit: Karmic Unrest\" for the BAKU acronym but alas...'{/i}"
    ]

    tina_page = [
        "{size=60}Tina{/s} - Hacky Code Enthusiast",
        "{ii}A Simple Frog{/ii}",
        "Character writing",
        "Programming:",
        " • Animation \n • Cooking section \n • Dream section",
        "Sound effects",
        "\'If two guys were on the moon and one killed the other with a rock would that be fucked up or what-\'"
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

    thanks_page = [
        "{size=60}Tanks 4 play{/s}", # I actually dont know what this looks like bc I cant find a shortcut here so itll be a surprise for everyone lol

    ]

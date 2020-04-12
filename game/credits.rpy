# Credits screen
transform dropdown:
    alpha 0.0
    xpos 1000 ypos -300
    ease_quad 3.0 ypos 180 alpha 1.0

transform slideright:
    xpos -1000 ypos 0
    alpha 0.0
    ease_quad 4.0 xpos -400 alpha 1.0

screen credits():
    modal True
    add "images/CG/incense_in.png"

    vbox:
        xmaximum 800
        text "{size=60}Cynthia!!!!!!{/s}":
            at dropdown
        text "Rascally Enthusiast":
            at dropdown
        text "Washed: hands \nStayed: inside \nDidn't do a good job with this credits screen lol the code is Not Great":
            at dropdown
        text "Quote: Simple zest for life":
            at dropdown
        text "Follow my idiot ass on twitter for guaranteed sparse content":
            at dropdown
        text "{ii}Tina please god help me clean this up{/ii}":
            at dropdown

    image "images/CG/smash.png":
         at slideright

    imagebutton:
        idle Solid("#0000")
        activate_sound 'audio/sfx/itemget.ogg'
        action [Jump("credit_roll")]

label credit_roll:
    show screen credits() with Dissolve(2.0)
    $ renpy.pause(delay=2, hard=False)

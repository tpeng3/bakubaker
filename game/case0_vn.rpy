# Time to BREAK EVERYTHING

# Characters ------------------------------------------------------------------
# TODO def vn section character (TWEWY) // def dream section character (Ghost Trick profile)
define s = Character (None,
            color="48475a",
            window_background="gui/textboxSomnia.png",
            what_xalign = 0.5,
            what_textalign = 0.5
            )
define r = Character (None,
            image = "remy",
            color="ffcf89",
            window_background="gui/textboxRem.png",
            what_xalign = 0.50,
            what_textalign = 0.50,
            window_yalign = 0.10,
            window_xalign = 0.50
            )
define u = Character (None,
            window_background="gui/textboxTest.png",
            what_xalign = 0.5,
            what_textalign = 0.5
            )
# Positions -------------------------------------------------------------------
transform right:
    yalign 1.0
    xalign -0.25
transform left:
    yalign 1.0
    xalign 1.30

# -----------------------------------------------------------------------------
# Crop (x, y, width, height)
image somnia:
    LiveCrop ((0,0,500,500), "images/sprites/somnia.png")
    zoom 2.0

image remy:
    LiveCrop ((0,0,500,500), "images/sprites/remerie.png")
    zoom 2.0
image side remy neutral:
    LiveCrop ((-1100,100,1920,500), "images/sprites/remerie.png")
    zoom 1.25
# image side remy grump:
#     LiveCrop ((-1100,100,1920,500), "images/sprites/remerie grump.png")
#     zoom 1.25

# -----------------------------------------------------------------------------


label cynthia:

    show somnia at right
    show remy at left
    u "Two characters are enjoying the void."

    s "Remerie's grumpy as ever...!"
    r "Hey!!!"
    s "Remy... rat chef..."
    r "Please don't call me that."

    show pika
    s "Oh lord... he comin."
    r "A big good boy."

    scene future office

    u "Kirby is the titular protagonist of the Kirby series of video games owned by Nintendo and HAL Laboratory. As one of Nintendo's most famous and familiar icons..."

    u "Kirby's round appearance and ability to copy his foes' powers has made him a well-known figure in video games, consistently ranked as one of the most iconic video game characters."

return

# Time to BREAK EVERYTHING

# -----------------------------------------------------------------------------
define s = Character ("Somnia",
            color="48475a",
            window_background="gui/textboxSomnia.png",
            what_xalign = 0.5,
            what_textalign = 0.5
            )
define r = Character ("Remerie",
            image = "remy",
            color="ffcf89",
            window_background="gui/textboxRem.png",
            what_xalign = 0.5,
            what_textalign = 0.5
            )
define u = Character (None,
            window_background="gui/textboxTest.png",
            what_xalign = 0.5,
            what_textalign = 0.5
            )
# -----------------------------------------------------------------------------
# Crop (x, y, width, height)
image somnia:
    LiveCrop ((0,80,500,500), "images/sprites/somnia.png")
    zoom 1.25

image remy:
    "images/sprites/remerie.png"
    zoom 1.25
image side remy neutral:
    LiveCrop ((-1100,100,1920,500), "images/sprites/remerie.png")
    zoom 1.25
image side remy grump:
    LiveCrop ((-1100,100,1920,500), "images/sprites/remerie grump.png")
    zoom 1.25
# Side image test with Remy- probably not ideal since they keep flashing in and out. Cool that it works tho lol!!!

# -----------------------------------------------------------------------------


label cynthia:

    show somnia at left
    u "Two characters are enjoying the void."

    s "Remerie's grumpy as ever...!"
    r neutral "Hey!!!"
    s "Remy... rat chef..."
    r grump "Please don't call me that."

    scene future office

    u "Kirby is the titular protagonist of the Kirby series of video games owned by Nintendo and HAL Laboratory. As one of Nintendo's most famous and familiar icons..."

    u "Kirby's round appearance and ability to copy his foes' powers has made him a well-known figure in video games, consistently ranked as one of the most iconic video game characters."

return

# Time to BREAK EVERYTHING

init python:
    config.side_image_only_not_showing = False

# Characters ------------------------------------------------------------------
# TODO def vn section character (TWEWY) // def dream section character (Ghost Trick profile)
define s = Character (None, # Name is baked into textbox bubble
# Somnia
            color="48475a",
            window_background="gui/textboxSomnia.png",
            what_xalign = 0.50,
            what_yalign = 0.50,
            what_textalign = 0.50
            )
define dreamSom = Character ("Somnia",
            image = "somnia",
            color="ffcf89",
            window_background="gui/textboxTest.png",
            what_xalign = 0.50,
            what_textalign = 0.50,
            window_yalign = 0.025,
            window_xalign = 0.50
            )
define r = Character (None, # Name is baked into textbox bubble
# Remerie
            color="ffcf89",
            window_background="gui/textboxRem.png",
            what_xalign = 0.50,
            what_yalign = 0.50,
            what_textalign = 0.50,
            )
define dreamRem = Character ("Remerie",
            image = "remy",
            color="ffcf89",
            window_background="gui/textboxTest.png",
            what_xalign = 0.50,
            what_textalign = 0.50,
            window_yalign = 0.025,
            window_xalign = 0.50
            )
define u = Character (None,
            window_background="gui/textboxTest.png",
            what_xalign = 0.5,
            what_textalign = 0.5
            )
define dr = Character (None,
            image = None,
            color="ffcf89",
            window_background="gui/textboxTest.png",
            what_xalign = 0.50,
            what_textalign = 0.50,
            window_yalign = 0.025,
            window_xalign = 0.50
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
    Crop ((0,0,500,500), "images/sprites/somnia.png")
    zoom 2.0
image somnia neutral = "images/sprites/somnia.png"
image side somnia neutral:
    Crop ((100,50,300,300), "somnia neutral")
    zoom 1.2
image somnia spider = "images/sprites/somnia spider.png"
image side somnia spider:
    Crop ((100,50,300,300), "somnia spider")
    zoom 1.2

image remy:
    Crop ((0,0,500,500), "images/sprites/remerie.png")
    zoom 2.0
image remy neutral = "images/sprites/remerie.png"
image side remy neutral:
    Crop ((100,50,300,300), "remy neutral")
    zoom 1.2
image remy grump = "images/sprites/remerie grump.png"
image side remy grump:
    Crop ((100,50,300,300), "remy grump")
    zoom 1.2

# -----------------------------------------------------------------------------

label cynthia:

    scene sugarspace
    show somnia at right
    show remy at left
    u "Two characters are enjoying Sugar Space."

    s "Remerie's grumpy as ever...!"
    r "Hey!!!"
    s "Remy... rat chef..."
    r "Please don't call me that."

    show pika
    s "Let's jump into the dream!"

    scene black with dissolve
    show pika
    dr "They're now in the void."
    dreamRem neutral "Pikachu is an Electric-type Pokémon introduced in Generation I. It evolves from Pichu when leveled up with high friendship and evolves into Raichu when exposed to a Thunder Stone."
    dreamSom neutral "I didn't know you were a fan of Pokemon, Rem!!"
    dreamRem grump "S-shush..."
    dreamSom spider "Hehehe..."

    "Going to Dreamland..."
    jump tina

return

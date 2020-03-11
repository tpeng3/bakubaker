# Case 0 assets ---------------------------------------------------------------
image kriby = "images/BG/bg_dreamland_kirby.png"
image clocktower = "images/BG/dream1/clocktower.png"
image rabbit = "images/BG/dream1/rabbit.png"
image client = "images/BG/dream1/rabbitOne.png"
image strawberry = "images/BG/dream1/strawberry.png"

# Definitions
# Characters ------------------------------------------------------------------
define s = Character ("Somnia", # Name is baked into textbox bubble
# Somnia
            color="48475a",
            what_color="854d56",
            window_background="gui/textbox.png",
            # what_xalign = 0.50,
            # what_yalign = 0.50,
            # what_textalign = 0.50
            )
define dreamSom = Character ("Somnia", # Dream Somnia
            image = "somnia",
            color="ffcf89",
            what_color="854d56",
            window_background="gui/textbox.png",
            what_xalign = 0.50,
            what_textalign = 0.50,
            window_yalign = 0.025,
            window_xalign = 0.50
            )
define r = Character ("Remerie", # Name is baked into textbox bubble
# Remerie
            color="ffcf89",
            what_color="854d56",
            window_background="gui/textbox.png",
            # what_xalign = 0.50,
            # what_yalign = 0.50,
            # what_textalign = 0.50,
            )
define dreamRem = Character ("Remerie", # Dream Remerie
            image = "remy",
            color="ffcf89",
            what_color="854d56",
            window_background="gui/textbox.png",
            what_xalign = 0.50,
            what_textalign = 0.50,
            window_yalign = 0.025,
            window_xalign = 0.50
            )
define dr = Character (None, # Dream narration
            color="ffcf89",
            what_color="854d56",
            window_background="gui/textbox.png",
            what_xalign = 0.50,
            what_textalign = 0.50,
            window_yalign = 0.025,
            window_xalign = 0.50
            )
# Positions -------------------------------------------------------------------
# So the bakus are positioned comfortably in their respective sides
transform right:
    yalign 1.0
    xalign -0.20
transform left:
    yalign 1.0
    xalign 1.20

# Images and side images ------------------------------------------------------
# Crop (x, y, width, height)
image somnia:
    Crop ((0,0,800,900), "images/sprites/somnia.png")
image somnia neutral = "images/sprites/somnia.png"
image side somnia neutral:
    Crop ((100,50,500,400), "somnia neutral")
    zoom 0.8
image somnia spider = "images/sprites/somnia spider.png"
image side somnia spider:
    Crop ((100,50,500,400), "somnia spider")
    zoom 0.8

image remy:
    Crop ((0,0,800,900), "images/sprites/remerie.png")
image remy neutral = "images/sprites/remerie.png"
image side remy neutral:
    Crop ((100,50,500,400), "remy neutral")
    zoom 0.9
image remy grump = "images/sprites/remerie grump.png"
image side remy grump:
    Crop ((100,50,500,400), "remy grump")
    zoom 0.9

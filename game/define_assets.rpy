# Case 0 assets ---------------------------------------------------------------
image storefront = "images/BG/bg_storefront.png"
image dreamoffice = "images/BG/bg_dreamoffice.png"
image wonderland = "images/BG/bg_wonderland.png"

image client1:
    Crop ((0,0,800,900), "images/sprites/client1.png")

# Definitions
# Characters ------------------------------------------------------------------
define s = Character ("Somnia",
            color="48475a",
            what_color="854d56",
            )
define r = Character ("Remerie",
            color="ffcf89",
            what_color="854d56",
            )
define dr = Character (None, # Dream narration
            color="ffcf89",
            what_color="854d56",
            window_background="gui/textbox.png",
            window_yalign = 0.025,
            window_xalign = 0.50
            )
define dreamSom = Character ("Somnia", kind = dr, # Dream Somnia
            image = "somnia"
            )
define dreamRem = Character ("Remerie", kind = dr, # Dream Remerie
            image = "remy"
            )
# Clients ---------------------------------------------------------------------
define bun = Character ("Bunny",
            what_color="854d56",
            )

# Positions -------------------------------------------------------------------
# So the bakus are positioned comfortably in their respective sides
transform left:
    yalign 1.0
    xalign -0.15
transform right:
    yalign 1.0
    xalign 1.13

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

#--------------------------------------------------------------------------
# DEFINE CHARACTER VOICES
#--------------------------------------------------------------------------
init python:
    def s_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/sfx/voice_som2.ogg", channel="bleeps", loop=True, fadein=0.2, fadeout=1.0)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps",fadeout=1.0)
    def r_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/sfx/voice_rem.ogg", channel="bleeps", loop=True, fadein=0.2, fadeout=1.0)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps", fadeout=1.0)
    def m_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/sfx/voice_marchie.ogg", channel="bleeps", loop=True, fadein=0.2, fadeout=1.0)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps", fadeout=1.0)

# Definitions
# Characters ------------------------------------------------------------------
define s = Character ("Somnia",
            color="48475a",
            what_color="854d56",
            callback=s_beep
            )
define r = Character ("Remerie",
            color="ffcf89",
            what_color="854d56",
            callback=r_beep
            )
define dr = Character (None, # Dream narration
            color="ffcf89",
            what_color="fff",
            window_background="gui/dreambox.png",
            what_text_align = 0.50,
            window_yalign = 0.025,
            window_xalign = 0.50
            )
define dreamSom = Character ("Somnia", kind = dr, # Dream Somnia
            image = "somnia",
            callback = s_beep
            )
define dreamRem = Character ("Remerie", kind = dr, # Dream Remerie
            image = "remi",
            callback = r_beep
            )
# Clients ---------------------------------------------------------------------
define u = Character ("???", color="fff", what_color="854d56") # Unknown
define ml = Character ("Marcella Lapin",
            color="48475a",
            what_color="854d56",
            callback = m_beep
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
    Crop ((0,0,800,900), "images/sprites/test_somsprite.png")
image somnia neutral = "images/sprites/test_somsprite.png"
image side somnia neutral:
    Crop ((150,0,700,500), "somnia neutral")
    zoom 0.7

image remi:
    Crop ((0,0,800,900), "images/sprites/test_remsprite.png")
image remi neutral = "images/sprites/test_remsprite.png"
image side remi neutral:
    Crop ((150,0,700,500), "remi neutral")
    zoom 0.7

init python:
# -----------------------------------------------------------------------------
# Text tag because I'm lazy
    def interesting(tag, argument, contents):
        color = "#d14970"
        return [
                (renpy.TEXT_TAG, "color={}".format(color)),
                (renpy.TEXT_TAG, "i"),
                ] + contents + [
                (renpy.TEXT_TAG, "/color"),
                (renpy.TEXT_TAG, "/i")
                ]
    config.custom_text_tags["ii"] = interesting

    def smallText(tag, argument, contents):
        size = 18
        return [
                (renpy.TEXT_TAG, "size={}".format(size)),
                ] + contents + [
                (renpy.TEXT_TAG, "/size"),
                ]
    config.custom_text_tags["ss"] = smallText

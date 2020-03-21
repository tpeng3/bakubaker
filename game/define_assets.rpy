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

# Characters ------------------------------------------------------------------
define s = Character ("Somnia",
            image = "somnia",
            color="48475a",
            what_color="854d56",
            callback = s_beep,
            )
define sth = Character (kind = s,
            what_prefix='(', what_suffix=')', what_italic=True
            )
define r = Character ("Remerie",
            # image = "remi",
            color="e18b81",
            what_color="854d56",
            callback = r_beep
            )
define rth = Character (kind = r,
            what_prefix='(', what_suffix=')', what_italic=True
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
            color="48475a",
            image = "somnia",
            callback = s_beep
            )
define dreamRem = Character ("Remerie", kind = dr, # Dream Remerie
            color="e18b81",
            image = "remi",
            callback = r_beep
            )
# Clients ---------------------------------------------------------------------
define u = Character ("???", color="434952", what_color="854d56") # Unknown
define ml = Character ("Marcella Lapin",
            color="6f8f4d",
            what_color="854d56",
            callback = m_beep
            )
define uml = Character ("???", kind = ml) # Before Marcella intro)

# Positions -------------------------------------------------------------------
# So the bakus are positioned comfortably in their respective sides
transform left:
    yalign 1.0
    xalign -0.10
transform right:
    yalign 1.0
    xalign 1.05

# Images and side images ------------------------------------------------------
# Crop (x, y, width, height)
# There HAS TO BE A BETTER WAY... but I guess I only have to define them once anyway :wtflmao:

init python:
    # shorcuts to expression names if you need them, also a handy reference for available expressions
    somnia_map = {
        "ne": "neutral",
        "de": "delighted",
        "di": "disappoint",
        "ex": "excited",
        "gr": "grin",
        "sh": "shock",
        "bi": "bigshock",
        "th": "think"
    }
    remerie_map = {
        "ne": "neutral",
        "de": "dedicate",
        "fl": "flushed",
        "gr": "grin",
        "pe": "peeved",
        "sh": "shock",
        "bi": "bigshock",
        "sh": "sigh",
        "th": "think"
    }

    def display_somnia(st, at):
        somexpr = getattr(store, "somexpr", "ne")
        img = Image("images/sprites/somnia_{}.png".format(somnia_map[somexpr]))
        if not _last_say_who == "s":
            img = im.MatrixColor(Image(img), im.matrix.saturation(0.5) * im.matrix.brightness(-0.2))
        d = Crop((0,0,800,1050), img)
        d = Transform(d, zoom=0.85)
        return d, None

    def display_remerie(st, at):
        remexpr = getattr(store, "remexpr", "ne")
        img = Image("images/sprites/remerie_{}.png".format(remerie_map[remexpr]))
        if not _last_say_who == "r":
            img = im.MatrixColor(Image(img), im.matrix.saturation(0.5) * im.matrix.brightness(-0.2))
        d = Crop((0,0,800,1050), img)
        d = Transform(d, zoom=0.85)
        return d, None

    def define_side_remerie(): # define side images for rem
        for rem in remerie_map:
            d = Crop ((150,0,700,513), "images/sprites/somnia_{}.png".format(remerie_map[rem]))
            d = Transform(d, zoom=0.6)
            renpy.image(("side", rem), d)

image somnia = DynamicDisplayable(display_somnia)
image remerie = DynamicDisplayable(display_remerie)

# for loop for the side images since they don't need to be dynamic but heck no I'm not initiating images 50 times


# image side somnia bsh:
#     Crop ((150,0,700,513), "somnia bsh")
#     zoom 0.6
# image somnia de:
#     Crop ((0,0,800,1050), "images/sprites/somnia_delighted.png")
#     zoom 0.85
# image side somnia e:
#     Crop ((150,0,700,513), "somnia e")
#     zoom 0.6
# image somnia di:
#     Crop ((0,0,800,1050), "images/sprites/somnia_disappointed.png")
#     zoom 0.85
# image side somnia di:
#     Crop ((150,0,700,513), "somnia di")
#     zoom 0.6
# image somnia ex:
#     Crop ((0,0,800,1050), "images/sprites/somnia_excited.png")
#     zoom 0.85
# image side somnia ex:
#     Crop ((150,0,700,513), "somnia ex")
#     zoom 0.6
# image somnia gr:
#     Crop ((0,0,800,1050), "images/sprites/somnia_grin.png")
#     zoom 0.85
# image side somnia gr:
#     Crop ((150,0,700,513), "somnia gr")
#     zoom 0.6
# image somnia sh:
#     Crop ((0,0,800,1050), "images/sprites/somnia_shock.png")
#     zoom 0.85
# image side somnia sh:
#     Crop ((150,0,700,513), "somnia sh")
#     zoom 0.6
# image somnia th:
#     Crop ((0,0,800,1050), "images/sprites/somnia_think.png")
#     zoom 0.85
# image side somnia th:
#     Crop ((150,0,700,513), "somnia th")
#     zoom 0.6

# image remi:
#     Crop ((0,0,800,1050), "images/sprites/remerie_neutral.png")
#     zoom 0.85
image remi neutral:
    Crop ((0,0,800,1050), "images/sprites/remerie_neutral.png")
    zoom 0.85
image side remi neutral:
    Crop ((150,0,700,513), "remi neutral")
    zoom 0.6
image remi bsh:
    Crop ((0,0,800,1050), "images/sprites/remerie_bigshock.png")
    zoom 0.85
image side remi bsh:
    Crop ((150,0,700,513), "remi bsh")
    zoom 0.6
image remi de:
    Crop ((0,0,800,1050), "images/sprites/remerie_dedicate.png")
    zoom 0.85
image side remi de:
    Crop ((150,0,700,513), "remi de")
    zoom 0.6
image remi fl:
    Crop ((0,0,800,1050), "images/sprites/remerie_flushed.png")
    zoom 0.85
image side remi fl:
    Crop ((150,0,700,513), "remi fl")
    zoom 0.6
image remi gr:
    Crop ((0,0,800,1050), "images/sprites/remerie_grin.png")
    zoom 0.85
image side remi gr:
    Crop ((150,0,700,513), "remi gr")
    zoom 0.6
image remi pe:
    Crop ((0,0,800,1050), "images/sprites/remerie_peeved.png")
    zoom 0.85
image side remi pe:
    Crop ((150,0,700,513), "remi pe")
    zoom 0.6
image remi sh:
    Crop ((0,0,800,1050), "images/sprites/remerie_shock.png")
    zoom 0.85
image side remi sh:
    Crop ((150,0,700,513), "remi sh")
    zoom 0.6
image remi si:
    Crop ((0,0,800,1050), "images/sprites/remerie_sigh.png")
    zoom 0.85
image side remi si:
    Crop ((150,0,700,513), "remi si")
    zoom 0.6
image remi th:
    Crop ((0,0,800,1050), "images/sprites/remerie_think.png")
    zoom 0.85
image side remi th:
    Crop ((150,0,700,513), "remi th")
    zoom 0.6

init python:
# -----------------------------------------------------------------------------
# Text tag to remind myself of the miscellany thats missing proper names
# If we want text outlines
    # gui.dialogue_text_outlines = [ (1, "#141414", 0, 0) ]
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
# Shake -------------------------------------------------------------
init:
    python:
        import math
        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
init:
    $ sshake = Shake((0, 0, 0, 0), 0.5, dist=10)

# Character Voices ------------------------------------------------------------------
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
define s = DynamicCharacter ("somnia_name",
            image = "somnia",
            color="2D2D3E",
            what_color="7A445B",
            callback = s_beep,
            )
define sth = Character (kind = s,
            what_prefix='(', what_suffix=')', what_italic=True
            )
define r = DynamicCharacter ("remerie_name",
            image = "remi",
            color="2D2D3E",
            what_color="7A445B",
            callback = r_beep
            )
define rth = Character (kind = r,
            what_prefix='(', what_suffix=')', what_italic=True
            )
define dr = Character (None, # Narration
            color="ffcf89",
            what_color="EDD9C8",
            window_background="gui/textbox_dream.png",
            what_text_align = 0.50,
            window_yalign = 0.025,
            window_xalign = 0.50,
            what_outlines = [
             (0.2, '#14000C'+"22", -1,1), (0.4, '#14000C'+"22", -1,1),  (0.8, '#14000C'+"22", -1,1),
             (1.6, '#14000C'+"11", -1,1), (2.4, '#14000C'+"11", -1,1),  (3.2, '#14000C'+"11", -1,1)]
            )
define dt = Character (None, # Dream speech
            color="ffcf89",
            what_color="EDD9C8",
            window_background="gui/textbox_dreamtalk.png",
            window_yalign = 0.025,
            window_xalign = 0.50
            )
define dreamSom = Character ("Somnia", kind = dt, # Dream Somnia
            color="2D2D3E",
            image = "dreamSom",
            callback = s_beep
            )
define dreamRem = Character ("Remerie", kind = dt, # Dream Remerie
            color="2D2D3E",
            image = "dreamRem",
            callback = r_beep
            )
# Clients ---------------------------------------------------------------------
define u = Character (None, color="2D2D3E", what_color="7A445B")
define ml = DynamicCharacter ("marcella_name",
            image = "mar",
            color="2D2D3E",
            what_color="7A445B",
            callback = m_beep
            )
define dreamMar = Character ("Dream Marcella", kind = dt,
            color="2D2D3E",
            image = "mar",
            callback = m_beep
            )
define bun = DynamicCharacter ("bun_name", kind = dr,
            color="2D2D3E",
            what_color="fff",
            )
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
# I GOT YOU CYNTHIA!!!

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
        "si": "sigh",
        "th": "think"
    }
    marcella_map = {
        "ne": "neutral",
        "fr": "frown",
        "gr": "grin",
        "aw": "awake",
        "la": "laugh",
        "th": "think",
        "wo": "worry",
        "ya": "yawn",
    }

    def display_somnia(st, at):
        somexpr = getattr(store, "somexpr", "ne")
        img = Image("images/sprites/somnia_{}.png".format(somnia_map[somexpr]))
        if not _last_say_who == "u" and not _last_say_who == "s":
            img = im.MatrixColor(Image(img), im.matrix.saturation(0.45) * im.matrix.brightness(-0.1))
        d = Crop((0,0,800,1050), img)
        d = Transform(d, zoom=0.85)
        return d, None

    def display_remerie(st, at):
        remexpr = getattr(store, "remexpr", "ne")
        img = Image("images/sprites/remerie_{}.png".format(remerie_map[remexpr]))
        if not _last_say_who == "u" and not _last_say_who == "r":
            img = im.MatrixColor(Image(img), im.matrix.saturation(0.45) * im.matrix.brightness(-0.1))
        d = Crop((0,0,800,1050), img)
        d = Transform(d, zoom=0.85)
        return d, None

    def display_marcella(st, at):
        marexpr = getattr(store, "marexpr", "ne")
        img = Image("images/sprites/marcella_{}.png".format(marcella_map[marexpr]))
        if not _last_say_who == "ml":
            img = im.MatrixColor(Image(img), im.matrix.saturation(0.45) * im.matrix.brightness(-0.1))
        d = Crop((0,0,900,1050), img)
        d = Transform(d, zoom=0.85)
        return d, None

    # dream side images
    def define_side_somnia():
        for som in somnia_map:
            d = Crop ((150,0,800,513), "images/sprites/somnia_{}.png".format(somnia_map[som]))
            d = Transform(d, zoom=0.6)
            renpy.image(("side", "dreamSom", som), d)

    def define_side_remerie():
        for rem in remerie_map:
            d = Crop ((150,0,800,513), "images/sprites/remerie_{}.png".format(remerie_map[rem]))
            d = Transform(d, zoom=0.6)
            renpy.image(("side", "dreamRem", rem), d)

    define_side_somnia()
    define_side_remerie()

image somnia = DynamicDisplayable(display_somnia)
image remi = DynamicDisplayable(display_remerie)
image mar = DynamicDisplayable(display_marcella)

init python:
# -----------------------------------------------------------------------------
# Text tag to remind myself of the miscellany thats missing proper names
# If we want text outlines
    # drdialogue_text_outlines = [ (1, "#141414", 0, 0) ]
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

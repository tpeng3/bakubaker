# 'function' for updating background panning
label lookaround(screenName, bg, pos):
    scene expression bg with move:
        xalign 0.5 xoffset pos
    $ renpy.show_screen(screenName, pos)
    $ renpy.pause(hard=True)

    
# ignore below code, this is if we want to give multiple options for each interaction
# --------------------------------------------------------------------------
# INITIALIZE INVESTIGATION CHOICES
# --------------------------------------------------------------------------

init -1 python:
    class Probe(store.object):
        def __init__(self, name, image, tooltip="???", actions={},):
            self.name = name # description of the action
            self.image = image
            self.tooltip = tooltip
            self.actions = actions # dict of possible actions {actionName: jumpLabel)
            self.viewed = False

        def view(self):
            self.viewed = True

# --------------------------------------------------------------------------
# CUSTOMIZE INVESTIGATION SCREEN
# --------------------------------------------------------------------------

screen investigation():
    # inventory button
    imagebutton:
        idle "gui/button/button_thoughts.png"
        hover im.MatrixColor("gui/button/button_thoughts.png", im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0))
        xalign 1.0 yalign 0
        action [ToggleScreen('inventory')]


#--------------------------------------------------------------------------
# PROBE OBJECTS FOR TEST KITCHEN
#--------------------------------------------------------------------------
init python:
    t_kirby = Probe("Kirby", "images/BG/bg_dreamland_kirby.png", tooltip="Kirby",
        actions = {
            "Talk to Kirby": "kirby_talk",
            "Steal his Shortcake": "kirby_steal"
        }
    )


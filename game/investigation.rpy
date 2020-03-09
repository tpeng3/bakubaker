# 'function' for updating background panning
label lookaround(screenName, bg, pos):
    scene expression bg with MoveTransition(1.8, time_warp=quad_time_warp):
        xpos 0 xoffset pos
    $ renpy.show_screen(screenName, pos)
    $ renpy.pause(hard=True)

    
# ignore below code, this is if we want to give multiple options for each interaction
# --------------------------------------------------------------------------
# INITIALIZE INVESTIGATION CHOICES
# --------------------------------------------------------------------------
init -1 python:
    class Probe(store.object):
        def __init__(self, name, image, icon, actions={},):
            self.name = name # description of the action
            self.image = image
            self.icon = icon
            self.actions = actions # dict of possible actions {actionName: jumpLabel)
            self.viewed = False

        def view(self):
            self.viewed = True

    # ease function for panning, god my braincell is terrible at linear algebra though
    def quad_time_warp(x):
      return -2.0 * x**3 + 3.0 * x**2

# --------------------------------------------------------------------------
# CUSTOMIZE INVESTIGATION SCREEN
# --------------------------------------------------------------------------
screen investigation():
    # inventory button
    imagebutton:
        idle "gui/button/button_thoughts.png"
        hover im.MatrixColor("gui/button/button_thoughts.png", im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0))
        xalign 1.0 yalign 0
        mouse "hover"
        action [ToggleScreen('inventory')]


screen dream_actions(actions={}, mx, my):
    $ ystart = 0

    # for cancelling/hiding dream_actions if you click away from the menu
    imagebutton:
        idle Solid("#0000")
        action Hide('dream_actions')

    for action in actions:
        textbutton action:
            xpos mx ypos my+ystart
            xalign 0 yalign 0.5
            mouse "hover"
            action [Hide('dream_actions'), Call(actions[action])]
        $ystart += 40


#--------------------------------------------------------------------------
# THOUGHT OBJECTS TO INVESTIGATE IN THE DREAM
#--------------------------------------------------------------------------
init python:
    t_kirby = Probe("Kirby", "images/BG/bg_dreamland_kirby.png", icon="icon_somnia",
        actions = {
            "Talk to Kirby": "kirby_talk",
            "Steal his Shortcake": "kirby_steal"
        }
    )
    t_clocktower = Probe("Clocktower", "images/BG/dream1/clocktower.png", icon="icon_remerie",
        actions = {
            "Look at Time": "clocktower_time",
            "Move the Hands": "clocktower_hands",
            "Enter the Tower": "clocktower_enter"
        }
    )
    t_rabbit = Probe("Rabbit", "images/BG/dream1/rabbit.png", icon="icon_somnia",
        actions = {
            "Talk to Rabbit": "rabbit"
        }
    )
    t_strawberry = Probe("Strawberry", "images/BG/dream1/strawberry.png", icon="icon_somnia",
        actions = {
            "Look at Strawberry": "strawberry_look",
            "Eat Strawberry": "strawberry_eat"
        }
    )


label lookaround(pos):
    show dreamland with move:
        xalign 0.5 xoffset pos
    show screen dream_test(pos)
    $ renpy.pause(hard=True)
    
    # $ xpos = i

# ignore below code, this is if we want to give multiple options for each interaction (ported from onm jakf;jewk)
# --------------------------------------------------------------------------
# INITIALIZE INVESTIGATION CHOICES
# --------------------------------------------------------------------------

init -1 python:
    class Probe(store.object):
        def __init__(self, name, type, cost=0, label="", tooltip="???"):
            self.name = name # description of the action
            self.type = type # type of probe (observation -> action -> discussion)
            self.cost = cost # time cost of action
            self.label = label # label to jump to for discussion
            self.viewed = False
            self.tooltip = tooltip
        def view(self):
            self.viewed = True

#--------------------------------------------------------------------------
# PROBE OBJECTS FOR TEST KITCHEN
#--------------------------------------------------------------------------
init python:
    t_kirby = Probe("Look at the box of candy", 1, cost=10, label="view_candy", tooltip="Kirby")


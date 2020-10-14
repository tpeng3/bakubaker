# generic labels for cooking
label cooking_start:
    hide screen focus_dialogue
    window hide
    $ renpy.pause(hard=True)

label play_sound: # have to call this because sfx happens after combo is updated
    play sound "audio/sfx/combo{}.ogg".format(cook_status.combo)
    jump cooking_start

label cooking_particles(type="drop", x=0.5, y=0.5):
    if type == "drop":
        $ star_type = "yellow"
    elif type == "special":
        $ star_type = "rainbow"
    show expression (ParticleBurst("gui/particle_cloud.png", explodeTime=0.2, numParticles=6, particleTime=1.5, particleXSpeed=5.5, particleYSpeed = 5.5, zOrder=0).sm) onlayer screens:
            xpos x ypos y
            alpha 0.5
    show expression (ParticleBurst("gui/particle_star_{}.png".format(star_type), explodeTime=0.2, numParticles=6, particleTime=1.0, particleXSpeed=5.5, particleYSpeed = 5.5, zOrder=1).sm) onlayer screens:
            xpos x ypos y
    show expression (ParticleBurst("gui/particle_star2_{}.png".format(star_type), explodeTime=0.2, numParticles=3, particleTime=1.0, particleXSpeed=5, particleYSpeed=5, zOrder=1).sm) onlayer screens:
            xpos x ypos y
    show expression (ParticleBurst("gui/particle_star3_{}.png".format(star_type), explodeTime=0.2, numParticles=3, particleTime=1.0, particleXSpeed=5, particleYSpeed=5, zOrder=1).sm) onlayer screens:
            xpos x ypos y

transform focus_effect: # brighten ingredient on focus, tho we can do other effects too
    on idle:
        linear 0.2 additive 0
    on hover:
        linear 0.2 additive 0.1

transform diagonal:
    xpos 0 ypos 0
    linear 40.0 xpan -360 ypan -360
    xpan 0 ypan 0
    repeat

transform dish_appear:
    alpha 0.0
    xoffset 30
    pause delay
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        linear 0.6 xoffset 0

transform bubble_appear:
    alpha 0.0
    # xoffset 30
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        linear 0.6 xoffset 0

image cooksom_ready:
    block:
        "images/interactables/cooksom_ready1.png"
        pause(0.2)
        "images/interactables/cooksom_ready2.png"
        pause(0.2)
        repeat

image letscookGO:
    anim.Filmstrip ("gui/button/letscook_filmstrip.png", (480,139), (1,7), 0.10, loop=True)

style cooking_bubble:
    # background Frame(
    #     Transform("gui/frame.png", yzoom=-1), 
    #     left = Borders(32, 80, 88, 33)
    #     )
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

    # The distance between content and outer edge (left, top, right, base)
    # padding (24, 73, 23, 22)

    # minimum (121, 114)
    # anchor (1.0, 0.0)
    # offset (12, -7)

#--------------------------------------------------------------------------
# INITIALIZE COOKING INVENTORY
#--------------------------------------------------------------------------
init -1 python:
    class Item(store.object):
        def __init__(self, name, image="", tooltip="", key=""):
            self.name = name # name of item
            self.image = image # image url
            self.tooltip = tooltip # tooltip desc
            self.key = key # item key name (for labels)

        def __repr__(self): # for printing
            return str(self.name)

    class Inventory(store.object):
        def __init__(self):
            self.items = []
            self.selected = []
        def add(self, item):
            for i in self.items:
                if item.name == i.name:
                    return
            self.items.append(item)
        def drop(self, item):
            toremove = -1
            for i in self.items:
                if item.name == i.name:
                    toremove = i
            if toremove != -1:
                self.items.remove(toremove)
        def addToCauldron(self, item):
            self.selected.append(item)
        def reset(self):
            for dragitem in self.selected:
                dragitem.snap(cook_status.init_pos[dragitem.drag_name][0], cook_status.init_pos[dragitem.drag_name][1], 0)
            self.selected = []
        def findKey(self, name):
            for i in self.items:
                if name == i.name:
                    return i.key
            return "" 

    class CookStatus(store.object):
        def __init__(self, smashReq, dish):
            self.dish = dish
            self.smashReq = smashReq # [] list of ideal dish ingredients
            self.smash = False
            self.combo = 0
            self.init_pos = {} # default positions for all the ingredients
        def update(self, item):
            print("to be implemented")
            # we aren't doing combos anymore
        def savePos(self, item, x, y):
            self.init_pos[item.name] = (x, y)
        def reset(self):
            self.combo = 0
            self.smash = False
            inventory.reset()
        def result(self):
            if set(inventory.selected) != set(self.smashReq):
                    return -1 # did not meet requirements
            if self.smash: # perfect score!
                return 1
            return 0 # ordinary score

init python:
    def ingredient_activated(drags):
        # item_name = drags[0].drag_name
        # item_key = inventory.findKey(item_name)
        # renpy.show("strawberry", layer='overlay')
        renpy.show_screen("som_bubble", "on activated")
        renpy.restart_interaction() # holy heck somniarre from renpy discord I owe you my life!!!
        return True

    def ingredient_dragged(drags, drop):
        item_name = drags[0].drag_name
        item_key = inventory.findKey(item_name)
        if not drop:
            renpy.show_screen("som_bubble", "where are you dropping?!")
            drags[0].snap(cook_status.init_pos[item_name][0], cook_status.init_pos[item_name][1], 0) # x, y, seconds to move
            renpy.restart_interaction()
            # renpy.call(item_key+"_ondrop")
            return

        drags[0].snap(9999, 9999, 0) # x, y, seconds to move
        inventory.addToCauldron(drags[0])

        x, y = renpy.get_mouse_pos()

        for item in smashReq:
            if item_name == item.name:
                renpy.show_screen("som_bubble", "just dropped something nice!")
                renpy.call("cooking_particles", type="special", x=x-10, y=y-10)
                # renpy.call(item_key+"_ondropsuccess")
                return True

        renpy.show_screen("som_bubble", "just dropped")
        renpy.call("cooking_particles", type="drop", x=x-10, y=y-10)
        # renpy.call(item_key+"_ondropsuccess")
        return True


#--------------------------------------------------------------------------
# COOKING INVENTORY SCREEN
#--------------------------------------------------------------------------
# Required Global Variables: inventory, cook_status, goal
screen cooking():
    zorder -10

    if renpy.has_screen("dream"):
        $ renpy.stop_predict_screen("dream")
        $ renpy.stop_predict(
            "images/BG/bg_wonderland.png",
            "images/interactables/case1/*.png",
            "side dreamSom *",
            "side dreamRem *"
        )

    add "starry":
        at diagonal

    # somnia and remerie sprites
    if not renpy.get_screen("cook_result"):
        imagebutton:
            idle "cooksom"
            xpos 0 ypos 245
            mouse "hover"
            action [Jump(case+"_somcook")]
        imagebutton:
            idle "cookrem"
            xpos 1629 ypos 245
            mouse "hover"
            action [Jump(case+"_remcook")]

    # cookbook
    add "cookbook":
        xalign 0.5 yalign 0.5
    add "cauldron":
        xpos 903+147 ypos 250-5

    imagebutton: # go back to dream mode
        idle "goDream"
        hover "goDreamHov"
        mouse "hover"
        hover_sound "audio/sfx/menuhover.ogg"
        activate_sound "audio/sfx/select.ogg"
        focus_mask True
        xalign 0 yalign 0
        at itrfade()
        # action [Function(cook_status.reset), Hide('cooking', transition=Dissolve(.8)), Jump("dream_return")]
        action [Function(cook_status.reset), Hide('cooking', transition=Dissolve(.8)), Jump("testing_room")]

    # reset button
    textbutton "Reset":
        xalign 0.8 yalign 0.1
        mouse "hover"
        action Function(cook_status.reset)

    # serve button
    imagebutton:
        idle "goEat"
        hover "letscookGO"
        mouse "hover"
        hover_sound "audio/sfx/menuhover.ogg"
        at itrfade()
        focus_mask True
        xalign 0.74 yalign 0.83
        activate_sound "audio/sfx/donecooking.ogg"
        action [Jump("smash_"+case)]

    # inventory positions
    $ x = 400
    $ y = 284

    # ingredient "ghost" after images
    for i, item in enumerate(inventory.items):
        if i != 0 and i % 3 == 0:
            $ x = 400
            $ y += 150
        image item.image xpos x ypos y alpha 0.3
        $ x += 159

    $ x = 400
    $ y = 284
    # actual draggable ingredients
    draggroup:
        drag:
            drag_name "Cauldron"
            draggable False
            child "cauldron_drop"
            xpos 903+310 ypos 250+160
        for i, item in enumerate(inventory.items):
            if i != 0 and i % 3 == 0:
                $ x = 400
                $ y += 150
            $ cook_status.savePos(item, x, y)

            drag:
                drag_name item.name
                child item.image
                droppable False
                activated ingredient_activated
                dragged ingredient_dragged
                xpos x ypos y
            $ x += 159

    $ tooltip = GetTooltip()
    if tooltip:
        fixed xmaximum 500 xoffset 50:
            text "[tooltip.name]":
                xpos 600 ypos 745
                xalign 0.5
                color "#7c345e"
            text "{size=24}[tooltip.tooltip]{/size}":
                xpos 600 ypos 790
                xalign 0.5
                color "#483e54"

    # text txt:
    #     style "dreamacts_text"
    #     at dish_appear
    #     xpos 200 ypos 200

screen cook_result():
    zorder 0
    modal True
    imagebutton:
        idle Solid("#0008")

    if cook_status.result() == 1:
        image cook_status.dish+"Best":
            xalign 0.5 yalign 0.55
            xanchor 0.5 yanchor 0.5
            at dish_appear
    else:
        image cook_status.dish+"Best":
            xalign 0.5 yalign 0.55
            xanchor 0.5 yanchor 0.5
            at dish_appear

    textbutton "Start Over":
        xalign 0.4 yalign 0.8
        mouse "hover"
        action [Function(cook_status.reset), Hide("cook_result", transition=Dissolve(0.8))]

    textbutton "Serve!":
        xalign 0.6 yalign 0.8
        mouse "hover"
        action Jump("testing_room")

    # somnia and remerie sprites
    imagebutton:
        xpos 0 ypos 245
        idle "cooksom_ready"
        mouse "hover"
        # action [Jump("smash_"+case)] # use a jump label when we want to throw in atls

    imagebutton:
        idle "cookrem"
        xpos 1629 ypos 245
        mouse "hover"
        # action [Jump(case+"_remcook")]

screen som_bubble(txt="hello", duration=2.0):
    timer duration action [Hide("som_bubble")]

    # style_prefix "cooking_bubble"
    frame:
        style "cooking_bubble"
        xpos 120 ypos 800

        add Text(txt, slow=20, style="dreamacts_text"):
            at bubble_appear
            # xpos 200 ypos 200
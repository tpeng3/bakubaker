label tina3:
    # tmp shortcut to get all the items if you didn't get them from the dream
    scene cookbook
    $ inventory = Inventory()
    call inventory_stock
    "Welcome to Hell's Kitchen..."
    "Quick tutorial: you got a bunch of ingredients, and the goal is to add it together and reach the numbers in the middle."
    "Bonus points if you get the STARRED* attribute to 100!"
    $ goal = {"wonder": 10, "spooky": 40, "spirit": 20}
    $ smashReq = [dream_flour, galaxy_milk, c_strawberry]
    $ cook_status = CookStatus(smashReq=smashReq)
    show screen cooking_inventory(goal=goal, zest="wonder")
    jump cooking_start

label cooking_start:
    window hide
    $ renpy.pause(hard=True)

label cooking_done:
    $ result = cook_status.result(goal, zest="wonder")
    if result == -1:
        "Failed cooking, try again"
        jump tina3
    elif result == 0:
        "You made a thing! But it's only passing."
    elif result == 1:
        "Yayyyy you made a really good thing!! Congrats!!"
    return

label inventory_stock:
    python:
        for i in [c_strawberry, dream_flour, nightmare_jelly, spooky_jam, galaxy_milk, haunted_whip]:
            inventory.add(i)
    return

#--------------------------------------------------------------------------
# COOKING INVENTORY SCREEN
#--------------------------------------------------------------------------
screen cooking_inventory(goal, zest):
    zorder 2
    modal True

    imagebutton:
        idle "goDream"
        hover "goDreamHov"
        mouse "hover"
        focus_mask True
        xalign 0 yalign 0
        action [Jump("dream_start1")]

    textbutton "Reset":
        xalign 0.1 yalign 0.7
        # text_style "temp_button_text"
        action [Function(cook_status.reset), Function(inventory.reset)]

    imagebutton:
        idle "goEat"
        hover "goEatHov"
        mouse "hover"
        focus_mask True
        xalign 0.74 yalign 0.85
        action [Jump("cooking_done")]

    #TODO: add better positions for the inventory, after UI is decided
    $x = 420
    $y = 140
    for i, item in enumerate(inventory.items):
        if i % 3 == 0:
            $ x = 420
            $ y += 140
        # for now border is a seperate image but change later
        imagebutton:
            idle item.image
            xpos x ypos y
            action [Function(inventory.toggleSelect, item), Function(cook_status.update, item)]
            tooltip item
        if item in inventory.selected:
            add "selBorder":
                xpos x-6 ypos y-6
        $ x += 160

    $ tooltip = GetTooltip()
    if tooltip:
        fixed xmaximum 500:
            text "[tooltip.name]":
                xpos 600 ypos 710 #tmp
                xalign 0.5
                color "#000"
            text "[tooltip.tooltip]":
                xpos 600 ypos 760 #tmp
                xalign 0.5
                color "#000"

    # desired stats
    $ y = 0
    for flavor in goal:
        bar value StaticValue(cook_status.flavors[flavor], 100):
            xalign 0.75 ypos 110+y
            xmaximum 400
            ymaximum 4
        # if flavor == zest:
        #     text flavor color '#facade':
        #         xalign 0.6+x yalign 0.45
        # else:
        #     text flavor:
        #         xalign 0.6+x yalign 0.45
        text "{}/{}".format(cook_status.flavors[flavor], goal[flavor]):
            xalign 0.75 ypos 110+y
        $ y += 60

    # combo
    bar value StaticValue(cook_status.combo, 4):
        xalign 0.2 ypos 80
        xmaximum 400
        ymaximum 4
    text "Combo: {}/{}".format(cook_status.combo, 4):
        xalign 0.2 ypos 80
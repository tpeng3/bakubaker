label tina3:
    # tmp shortcut to get all the items if you didn't get them from the dream
    scene black
    $ inventory = Inventory()
    call inventory_stock
        
    "Welcome to Hell's Kitchen..."
    "Quick tutorial: you got a bunch of ingredients, and the goal is to add it together and reach the numbers in the middle."
    "Bonus points if you get the STARRED* attribute to 100!"
    $ goal = {"wonder": 10, "spooky": 40, "tension": 20, "spirit": 20}
    $ cook_status = CookStatus()
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

    #TODO: add better positions for the inventory, after UI is decided
    $x = 0
    hbox:
        for item in inventory.items:
            imagebutton:
                idle item.image
                xalign 0+x
                action [Function(inventory.select, item)]
                tooltip item
            $ x += 1

    if inventory.selitem:
        text "Selected Item: {}".format(inventory.selitem.name):
            xalign 0.1 yalign 0.55

    textbutton "Add Ingredient":
        xalign 0.1 yalign 0.6
        action [Function(cook_status.update, inventory.selitem), Function(inventory.use, inventory.selitem)]

    # TODO: I also want it to shortcut undo with right click)
    # textbutton "Undo":
    #     xalign 0.1 yalign 0.65
    #     action [Function(cook_status.undo(inventory.undo()))]

    textbutton "Reset":
        xalign 0.1 yalign 0.7
        action [Function(cook_status.reset), Function(inventory.reset)]

    textbutton "Done":
        xalign 0.1 yalign 0.75
        action [Jump("cooking_done")]

    textbutton "Return to Dream":
        xalign 0.1 yalign 0.80
        action [Jump("dream_start1")]

    # this is if we want to select any items to focus, otherwise we don't need this code
    # if inventory.selitem is not None:
    #     text "sel item is" + inventory.selitem.name ypos 520

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip.name]":
            xalign 0.8 yalign 0.0 #tmp
        text "[tooltip.tooltip]":
            xalign 0.8 yalign 0.1 #tmp

    # desired stats
    $ y = 0
    for flavor in goal:
        bar value StaticValue(cook_status.flavors[flavor], 100):
            xalign 0.6 yalign 0.45+y
            xmaximum 400
            ymaximum 20
        # if flavor == zest:
        #     text flavor color '#facade':
        #         xalign 0.6+x yalign 0.45
        # else:
        #     text flavor:
        #         xalign 0.6+x yalign 0.45
        text "{}/{}".format(cook_status.flavors[flavor], goal[flavor]):
            xalign 0.5 yalign 0.45+y
        $ y += 0.1
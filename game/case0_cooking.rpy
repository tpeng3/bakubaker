label tina3:
    # tmp shortcut to get all the items if you didn't get them from the dream
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

label inventory_stock:
    python:
        for i in [dream_flour, nightmare_jelly, spooky_jam, galaxy_milk, haunted_whip]:
            inventory.add(dream_flour)
    return

#--------------------------------------------------------------------------
# COOKING INVENTORY SCREEN
#--------------------------------------------------------------------------
screen cooking_inventory(goal, zest):
    zorder 2
    modal True

    #TODO: add better positions for the inventory, after UI is decided
    hbox:
        for item in inventory.items:
            imagebutton:
                idle item.image
                action [Function(inventory.select, item)]
                tooltip item.tooltip

    textbutton "Add Ingredient":
        xalign 0.2 yalign 0.6
        action [Function(inventory.use, item)]

    textbutton "Undo":
        xalign 0.2 yalign 0.65
        action [Function(inventory.undo, item)]

    # this is if we want to select any items to focus, otherwise we don't need this code
    # if inventory.selitem is not None:
    #     text "sel item is" + inventory.selitem.name ypos 520

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            xalign 0.9 yalign 0.5 #tmp

    # desired stats
    for flavor in goal:
        if flavor == zest:
            text flavor color '#facade'
        else:
            text flavor
        text "{}/{}".format(cook_status.flavors[flavor], goal[flavor])

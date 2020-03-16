label case1_cook:
    # tmp shortcut to get all the items if you didn't get them from the dream
    $ inventory = Inventory()
    call inventory_stock
    # "Welcome to Hell's Kitchen..."
    # "Quick tutorial: you got a bunch of ingredients, and the goal is to add it together and reach the numbers in the middle."
    # "Bonus points if you get the STARRED* attribute to 100!"
    $ goal = {"wonder": 10, "spooky": 40, "spirit": 20}
    $ smashReq = [dream_flour, galaxy_milk, c_strawberry, nightmare_jelly]
    $ zest = "wonder"
    $ cook_status = CookStatus(smashReq=smashReq, goal=goal, zest=zest)
    show screen cooking(dish="omelette")
    jump cooking_start

label case1_cook_done(result):
    show screen focus_dialogue
    if result == -1:
        "Failed cooking, try again"
        $ inventory.reset()
        $ cook_status.reset()
        jump cooking_start
    elif result == 0:
        "You made a thing! But it's only passing."
        $ MainMenu(confirm=False)
    elif result == 1:
        "Yayyyy you made a really good thing!! Congrats!!"
        $ MainMenu(confirm=False)

label inventory_stock:
    python:
        for i in [c_strawberry, dream_flour, nightmare_jelly, spooky_jam, galaxy_milk, haunted_whip]:
            inventory.add(i)
    return
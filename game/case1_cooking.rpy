label case1_cook:
    # tmp shortcut to get all the items if you didn't get them from the dream
    $ inventory = Inventory()
    call inventory_stock
    # "Welcome to Hell's Kitchen..."
    # "Quick tutorial: you got a bunch of ingredients, and the goal is to add it together and reach the numbers in the middle."
    # "Bonus points if you get the STARRED* attribute to 100!"
    $ goal = 69
    $ smashReq = [c_strawberry, c_bunnyapples, c_herbs, c_clockegg]
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
    elif result == 1:
        "Yayyyy you made a really good thing!! Congrats!!"
    hide screen cooking with Dissolve(0.8)
    hide screen focus_dialogue
    call case1_vn_end(result)

label inventory_stock:
    python:
        for i in [c_strawberry, c_bunnyapples, c_herbs, c_medicine, c_clockegg]:
            inventory.add(i)
    return
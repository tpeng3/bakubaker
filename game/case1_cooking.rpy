image cutin:
    anchor (0,0)
    xpos -1.0 ypos 0
    "images/CG/cutin.png"
    alpha 1.0
    ease 0.50 truecenter
    contains:
        "images/CG/cutin1.png"
        pause 0.20
        "images/CG/cutin2.png"
        pause 0.20
        repeat 3
    pause 1.0
    parallel:
        linear 1.0 zoom 2 truecenter
    parallel:
        linear 1.0 alpha 0.0
    pause 1.0

label case1_cook:
    play music cooking1
    # tmp shortcut to get all the items if you didn't get them from the dream
    $ inventory = Inventory()
    call inventory_stock from _call_inventory_stock
    # "Welcome to Hell's Kitchen..."
    # "Quick tutorial: you got a bunch of ingredients, and the goal is to add it together and reach the numbers in the middle."
    # "Bonus points if you get the STARRED* attribute to 100!"
    $ goal = 69
    $ smashReq = [c_strawberry, c_bunnyapples, c_herbs, c_clockegg]
    $ cook_status = CookStatus(smashReq=smashReq, goal=goal)
    show screen cooking(dish="omelette")
    jump cooking_start

label case1_somcook:
    show screen focus_dialogue
    s "helll yeaaaa"
    jump cooking_start

label case1_remcook:
    show screen focus_dialogue
    r "dam what are you up to now!!"
    jump cooking_start

label smash_case1:
    $ somnia_name = "Somnia"
    show cutin onlayer overlay
    s "Fuck yeah!!!!!!!!!!!!!!!!!!!!!!!"
    $ cook_status.smashSkill()
    jump cooking_start

label case1_cook_done(result):
    $ renpy.stop_predict_screen("cooking")
    $ renpy.stop_predict(
        "images/BG/starry.png",
        "images/BG/test_cookbook.png",
        "images/items/item_*.png",
        "images/items/dish_*.png",
    )
    show screen focus_dialogue
    if result == -1:
        "Failed cooking, try again"
        $ inventory.reset()
        $ cook_status.reset()
        jump cooking_start
    elif result == 0:
        s "Pretty good! Could use some more zing and pep, though."
        r "This looks serviceable."
    elif result == 1:
        s "Ah, such a dreamy looking dish! I almost don't want to eat it..."
        r "Not bad at all. Next time I'll be expecting more."
    hide screen cooking with Dissolve(0.8)
    hide screen focus_dialogue
    call case1_vn_end(result) from _call_case1_vn_end

label inventory_stock:
    python:
        for i in [c_strawberry, c_bunnyapples, c_herbs, c_medicine, c_clockegg]:
            inventory.add(i)
    return
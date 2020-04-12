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
    pause 2.0

label case1_cook:
    play music cooking1
    # tmp shortcut to get all the items if you didn't get them from the dream
    if len(inventory.items) == 0:
        $ inventory = Inventory()
        call inventory_stock from _call_inventory_stock
    $ smashReq = [c_strawberry, c_bunnyapples, c_herbs, c_clockegg]
    $ cook_status = CookStatus(smashReq=smashReq)
    show screen cooking(dish="omelette") with Dissolve (0.8)
    if not tutorial:
        show screen focus_dialogue
        pause 1.0
        r "Alright, let's begin whipping up a dream dish out of our available assets."
        r "As we learned from Marcella's dream, {b}time{/b} seems to be at the center of their woes."
        r "They appear to be in a state of perpectual disarray, unable to keep up with their ever-growing list of tasks."
        s "If we can eat away the worry, perhaps they'll feel less uneasy!"
        r "Right. Dream dishes are fickle so we have to make sure we use the right ingredients."
        r "One wrong step and we'll have to start over."
        s "This time we're a bit low on eggs, but let's do our best!"
        $ tutorial = True
    jump cooking_start

label case1_somcook:
    show screen focus_dialogue
    if not cook_status.smash:
        s "Hmm... A breakfast egg dish. What about we make some pancakes Remi?"
    else:
        s "It's done! Let's wrap up now."
    jump cooking_start

label case1_remcook:
    show screen focus_dialogue
    if not cook_status.smash:
        r "We don't have any flour so let's keep it simple."
        r "But if we want something sweet, we can add some fruit."
    else:
        r "Well in any case, we should clean up now."
    jump cooking_start

label smash_case1:
    $ somnia_name = "Somnia"
    show cutin onlayer overlay
    pause 3.0
    $ cook_status.smashSkill()
    play sound "audio/sfx/comboFULL.ogg"
    s "Viola~ "
    r "W-what did you do?!"
    s "Just a bit of {i}Somnia magic{/i}. I feel like it was missing something earlier."
    s "In this case, a spoonful of ketchup~"
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
    if result == 0:
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

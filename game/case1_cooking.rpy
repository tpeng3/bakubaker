label case1_cook:
    play music cooking1
    $ inventory.drop(c_bluebook) # these items aren't ingredients so drop them!!
    $ inventory.drop(c_redbook)

    # tmp shortcut to get all the items if you didn't get them from the dream
    if len(inventory.items) == 0:
        call inventory_stock from _call_inventory_stock
    $ smashReq = [c_strawberry, c_bunnyapples, c_herbs, c_clockegg]
    $ cook_status = CookStatus(smashReq=smashReq)
    show screen cooking(dish="omelette") with Dissolve (0.8)
    if not tutorial:
        show screen focus_dialogue
        pause 1.0
        r "Alright, let's begin whipping up a dream dish out of what we got."
        r "As we learned from Marcella's dream, {ii}time{/ii} seems to be the center of their woes."
        r "They appear to be in a state of perpectual disarray, unable to keep up with their ever-growing list of tasks."
        s "If we can eat away the worry, perhaps they'll feel less uneasy!"
        r "Right. Dream dishes are fickle so we have to make sure we use the right ingredients."
        r "One wrong step and we'll have to start over."
        s "This time we're a bit low on eggs, but let's do our best!"
        r "We should aim for a {ii}5 star dish.{/ii}"
        s "If you feel stuck Remi, we can bounce off ideas together! {ii}Just talk to me{/ii}, okay?"
        $ tutorial = True
    jump cooking_start

label case1_somcook:
    show screen focus_dialogue
    if not cook_status.smash:
        s "Hmm... A breakfast egg dish. Oh, what about an omelette?"
        r "What do you think, Remi?"
    else:
        s "It's done! Let's wrap up now."
    jump cooking_start

label case1_remcook:
    show screen focus_dialogue
    if not cook_status.smash:
        if c_strawberry not in inventory.items:
            r "Hm... It feels like we're missing an ingredient."
            r "I think I want to take a look again back in the dream."
        else:
            r "An omelette sounds good, but ingredients alone won't give us a 5 star dish."
            r "There must be something else we can add..."
    else:
        r "Well, in any case, we should clean up now."
    jump cooking_start

label smash_case1:
    show screen focus_dialogue
    $ somnia_name = "Somnia"
    show cutin onlayer overlay
    pause 5.0
    $ cook_status.smashSkill()
    play sound "audio/sfx/comboFULL.ogg"
    s "Viola~!"
    r "W-what did you do?!"
    s "Just a bit of {i}Somnia magic{/i}. I feel like it was missing something earlier."
    s "In this case, a spoonful of love~!"
    jump cooking_start

label case1_cook_done():
    $ renpy.stop_predict_screen("cooking")
    $ renpy.stop_predict(
        "images/BG/starry.png",
        "images/BG/test_cookbook.png",
        "images/items/item_*.png",
        "images/items/dish_*.png",
    )
    $ result = cook_status.result()
    show screen focus_dialogue
    if result == 0:
        s "Pretty good! Could use some more zing and pep, though."
        r "This looks serviceable."
    elif result == 1:
        s "Ah, such a dreamy looking dish! I almost don't want to eat it..."
        r "Not bad at all. Next time I'll be expecting more."
    hide screen focus_dialogue
    hide screen cooking with Dissolve(0.8)
    scene black with Dissolve (0.8)
    pause 1.0
    call case1_vn_end(result) from _call_case1_vn_end

label inventory_stock:
    python:
        for i in [c_strawberry, c_bunnyapples, c_herbs, c_medicine, c_clockegg]:
            inventory.add(i)
    return

#--------------------------------------------------------------------------
# TESTING COOKING ROOM
# refer to test_definitions.py for the list of ingredients and their relevant text
# refer to cookstatus.rpy for the cooking screen!
# btw don't try to cook in the actual story case rn it'll be broken because of my changes!! (・ω<)
#--------------------------------------------------------------------------
label test_cook:
    play music cooking1
    python: # adding the ingredients for testing
        for i in [c_strawberry, c_bunnyapples, c_herbs, c_medicine, c_clockegg]:
            inventory.add(i)
    $ smashReq = [c_strawberry, c_bunnyapples, c_herbs, c_clockegg]
    $ cook_status = CookStatus(smashReq=smashReq)
    show screen cooking(dish="omelette") with Dissolve (0.8)
    jump cooking_start

label test_somcook:
    show screen focus_dialogue
    if not cook_status.smash:
        s "Hmm... A breakfast egg dish. Oh, what about an omelette?"
        r "What do you think, Remi?"
    else:
        s "It's done! Let's wrap up now."
    jump cooking_start

label test_remcook:
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

label smash_test:
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

label test_cook_done():
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
    return
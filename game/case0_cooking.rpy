label cook_case1:
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

label cook_case1_done(result):
    if result == -1:
        "Failed cooking, try again"
        jump tina3
    elif result == 0:
        "You made a thing! But it's only passing AM I USING aaaaCACHE."
        jump listen
    elif result == 1:
        "Yayyyy you made a really good thing!! Congrats!!"
        $ renpy.MainMenu(confirm=False)

# OK THIS IS BROKEN, gonna have to debug another day...
label listen:
    "listen I just want to go back to the main menu why is it not progression"
    $ renpy.MainMenu(confirm=False)

label inventory_stock:
    python:
        for i in [c_strawberry, dream_flour, nightmare_jelly, spooky_jam, galaxy_milk, haunted_whip]:
            inventory.add(i)
    return


#--------------------------------------------------------------------------
# DEFINE INGREDIENTS
#--------------------------------------------------------------------------
init python:
    kirby = Item("Kirby with Shortcake", image = "/images/items/item_kirby.png",
        tooltip="Free him...",
        flavors={
            "wonder": 999,
            "spirit": 999,
            "spooky": 999
        })
    dream_flour = Item("Dream Flour", image = "/images/items/item_kirby.png",
        tooltip="Dream Flour +30 wonder, -20 spirit", 
        flavors={
            "wonder": 30,
            "spirit": 20,
            "spooky": 0
        })
    nightmare_jelly = Item("Nightmare Jelly", image = "/images/items/item_kirby.png",
        tooltip="Nightmare Jelly +40 spooky", 
        flavors={
            "wonder": 0,
            "spirit": 0,
            "spooky": 40
        })
    spooky_jam = Item("Spooky Jam", image = "/images/items/item_kirby.png",
        tooltip="Spooky Jam +30 spooky, +10 wonder", 
        flavors={
            "wonder": 10,
            "spirit": 0,
            "spooky": 30
        })
    galaxy_milk = Item("Galaxy Milk", image = "/images/items/item_kirby.png",
        tooltip="Galaxy Milk +10 spirit, -5 spooky", 
        flavors={
            "wonder": 0,
            "spirit": 10,
            "spooky": 5
        })
    haunted_whip = Item("Haunted Whip", image = "/images/items/item_kirby.png",
        tooltip="Haunted Whip +20 spooky", 
        flavors={
            "wonder": 0,
            "spirit": 0,
            "spooky": 20
        })

    c_strawberry = Item("Creamy Strawberry", image = "/images/items/item_strawberry.png",
        tooltip="A tasty strawberry +20 spooky, +30 wonder", 
        flavors={
            "wonder": 30,
            "spirit": 20,
            "spooky": 0
        })
    
    
label dream_case1:
    $ inventory = Inventory()
    $ itr_list = [t_kirby, t_rabbit, t_clocktower, t_strawberry, t_client] # starting interactions
    $ interactions = Interactions(itr_list)
    $ page_width = 1680 # width of a "page" to scroll
    $ unlocked_pages = 2 # default is 0 but set to 2 for testing purposes
    $ finished = False
    # have to initialize scene bg as an expression for lookaround to work later
    $ bg = "wonderland"
    scene expression bg:
        xpos 0
    "Case 1 (tutorial) dream"
    show screen dream()
    jump dream_start1

label dream_start1:
    # if finished:
    #     "OK I think I have a good idea of what to make."
    #     "Time to head back to the kitchen!"
    #     jump tina3
    window hide
    $ renpy.pause(hard=True)

label unlock_kitchen:
    show screen goCook()
    jump dream_start1

label rabbit:
    "I'm late! I'm late!"
    dreamRem neutral "I wonder what's the hurry..."
    jump dream_start1

label client_talk:
    "*Mumble mumble...*"
    dreamSom neutral "There they are!"
    "*NYOOMS*"
    $ interactions.complete([t_client])
    hide expression t_client.image with Dissolve(0.8)
    dreamSom "Oh noooooooooo"
    jump dream_start1

label clocktower_time:
    "The time is 4:20"
    dreamSom "Blaze it."
    jump dream_start1

label clocktower_hands:
    dreamRem "Ghk... I can't move the hands."
    dreamSom "Time waits for no one."
    jump dream_start1

label clocktower_enter:
    dreamSom "Rumors say a great treasure is hidden inside the Ghost Tower."
    "Against proper judgement, you enter inside..."
    hide screen investigation
    hide screen dream_wonderland
    scene black with Dissolve(2.0)
    $ renpy.pause(2.0)
    jump tina3

label strawberry_look:
    dreamSom "That's a huge strawberry..."
    $ interactions.update(t_strawberry.enable("strawberry_eat"))
    jump dream_start1

label strawberry_eat:
    if c_strawberry not in inventory.items:
        dreamSom "Oh I love strawberries!"
        $ inventory.add(c_strawberry)
        "Strawberry added to inventory."
    else:
        dreamRem "I wonder what we can make with this strawberry..."
    jump unlock_kitchen

    
#--------------------------------------------------------------------------
# THOUGHT OBJECTS TO INVESTIGATE IN THE DREAM
#--------------------------------------------------------------------------
init python:
    t_kirby = Interactables("Kirby", "images/interactables/kirby.png", page=0,
        actions = [
            {"name": "Talk to Kirby", "label": "kirby_talk"},
            {"name": "Steal his Shortcake", "label": "kirby_steal"}
        ]
    )
    t_client = Interactables("Mumbling Client", "images/interactables/case1/rabbitOne.png", page=0,
        actions = [
            {"name": "Talk to Rabbit", "label": "client_talk"}
        ]
    )
    t_clocktower = Interactables("Clocktower", "images/interactables/case1/clocktower.png", page=2,
        actions = [
            {"name": "Look at Time", "label": "clocktower_time"},
            {"name": "Move the Hands", "label": "clocktower_hands"},
            {"name": "Enter the Tower", "label": "clocktower_enter"}
        ]
    )
    t_rabbit = Interactables("Rabbit", "images/interactables/case1/rabbit.png", page=2,
        actions = [
            {"name": "Talk to Rabbit", "label": "rabbit"}
        ]
    )
    t_strawberry = Interactables("Strawberry", "images/interactables/case1/strawberry.png", page=2,
        actions = [
            {"name": "Look at Strawberry", "label": "strawberry_look"},
            {"name": "Eat Strawberry", "label": "strawberry_eat", "condition": False}
        ]
    )

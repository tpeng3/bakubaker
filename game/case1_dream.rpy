label tina:
    menu:
        "Dream Investigation":
            jump dream_case1
        "Hell's Kitchen":
            jump cook_case1

label dream_case1:
    python:
        case = "case1" # move this variable to be initialized in the vn portion later
        bg = "wonderland2" # background image
        page_width = 1720 # screen page width
        total_pages = 3 # total pages in investigation
        unlocked_pages = 2 # default is 0 but set to 2 for testing purposes
        inventory = Inventory()
        itr_list = [t_client, t_clocktower, t_strawberry] # starting interactions
        interactions = Interactions(itr_list)

        finished = True # default is false, but true for testing

    scene black
    "Case 1 (tutorial) dream"
    show screen dream()
    jump dream_start

label rabbit:
    "I'm late! I'm late!"
    $ interaction.pop()
    dreamRem neutral "I wonder what's the hurry..."
    jump dream_start

label client_talk:
    "*Mumble mumble...*"
    dreamSom neutral "There they are!"
    "*NYOOMS*"
    $ interactions.complete([t_client])
    hide expression t_client.image with Dissolve(0.2)
    dreamSom "Oh noooooooooo"
    jump dream_start

label clocktower_time:
    "The time is 4:20"
    dreamSom "Blaze it."
    jump dream_start

label clocktower_hands:
    dreamRem "Ghk... I can't move the hands."
    dreamSom "Time waits for no one."
    jump dream_start

label clocktower_enter:
    dreamSom "Rumors say a great treasure is hidden inside the Ghost Tower."
    "Against proper judgement, you enter inside..."
    jump dream_start

label strawberry_look:
    dreamSom "That's a huge strawberry..."
    $ interactions.update(t_strawberry.enable("strawberry_eat"))
    jump dream_start

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

#--------------------------------------------------------------------------
# CASE 1 INTERACTABLES
#--------------------------------------------------------------------------
init python:
    # PART ONE
    t_marcella_start = Interactables("Marcella Lapin", "marcella_start", "images/interactables/case1/rabbitOne.png", page=0,
        actions = [
            {"name": "Talk to Marcella", "label": "marcella_talk_start"}
        ]
    )
    t_bunnysquad = Interactables("Fluffle of Bunnies", "bunnysquad", "images/interactables/case1/bunny2.png", page=0,
        actions = [
            {"name": "Talk with Bunnies (Somnia)", "label": "bunnies_talk_som"},
            {"name": "Talk with Bunnies (Remerie)", "label": "bunnies_talk_rem"}
        ]
    )
    t_strawberry = Interactables("Giant Strawberry", "strawberry", "images/interactables/case1/strawberry.png", page=0,
        actions = [
            {"name": "Look at Strawberry", "label": "strawberry_look"}
        ]
    )

    # PART TWO 
    t_marcella_mid = Interactables("Marcella Lapin", "marcella_mid", "images/interactables/case1/rabbitOne.png", page=1,
        actions = [
            {"name": "Talk to Marcella", "label": "marcella_talk_mid1", "condition": True},
            {"name": "Talk to Marcella", "label": "marcella_talk_mid2", "condition": False},
        ]
    )
    t_medicine = Interactables("Bottle of Medicine", "medicine", "images/interactables/case1/medicine.png", page=1,
        actions = [
            {"name": "Find Medicine", "label": "medicine_find"}
        ]
    )
    t_debris = Interactables("Mounds of Papers", "debris", "images/interactables/case1/clocktower.png", page=1,
        actions = [
            {"name": "Inspect Pile", "label": "pile_inspect"}
        ]
    )
    t_bunny1 = Interactables("Quiet Bunny", "bunny1", "images/interactables/case1/bunny1.png", page=0,
        actions = [
            {"name": "Talk to Bunny", "label": "bunny1_talk", "condition": True},
            {"name": "Give the Medicine", "label": "bunny1_give", "condition": False},
            {"name": "Ask for Help", "label": "bunny1_help", "condition": False},
            {"name": "Chat with Bunny", "label": "bunny1_chat", "condition": False},
            {"name": "Ask for the Time", "label": "bunny1_time", "condition": False}
        ],
        state = False
    )
    t_bunny2 = Interactables("Energetic Bunny", "bunny2", "images/interactables/case1/bunny2.png", page=0,
        actions = [
            {"name": "Talk to Bunny", "label": "bunny2_talk", "condition": True},
            {"name": "Give the Medicine", "label": "bunny2_give", "condition": False},
            {"name": "Ask for Help", "label": "bunny2_help", "condition": False},
            {"name": "Chat with Bunny", "label": "bunny2_chat", "condition": False},
            {"name": "Ask for the Time", "label": "bunny2_time", "condition": False}
        ]
    )
    t_bunny3 = Interactables("Peevish Bunny", "bunny3", "images/interactables/case1/bunny3.png", page=1,
        actions = [
            {"name": "Talk to Bunny", "label": "bunny3_talk", "condition": True},
            {"name": "Give the Medicine", "label": "bunny3_give", "condition": False},
            {"name": "Ask for Help", "label": "bunny3_help", "condition": False},
            {"name": "Chat with Bunny", "label": "bunny3_chat", "condition": False},
            {"name": "Ask for the Time", "label": "bunny3_time", "condition": False}
        ]
    )
    t_bunny4 = Interactables("Studious Bunny", "bunny4", "images/interactables/case1/bunny4.png", page=1,
        actions = [
            {"name": "Talk to Bunny", "label": "bunny4_talk", "condition": True},
            {"name": "Give the Medicine", "label": "bunny4_give", "condition": False},
            {"name": "Ask for Help", "label": "bunny4_help", "condition": False},
            {"name": "Chat with Bunny", "label": "bunny4_chat", "condition": False},
            {"name": "Ask for the Time", "label": "bunny4_time", "condition": False}
        ]
    )
    t_bunny5 = Interactables("Clumsy Bunny", "bunny5", "images/interactables/case1/bunny5.png", page=1,
        actions = [
            {"name": "Talk to Bunny", "label": "bunny5_talk", "condition": True},
            {"name": "Give the Medicine", "label": "bunny5_give", "condition": False},
            {"name": "Ask for Help", "label": "bunny5_help", "condition": False},
            {"name": "Chat with Bunny", "label": "bunny5_chat", "condition": False},
            {"name": "Ask for the Time", "label": "bunny5_time", "condition": False}
        ],
        state = -1
    )
    t_flower1 = Interactables("White Rose", "flower1", "images/interactables/case1/flower1.png", page=0,
        actions = [
            {"name": "Paint the Rose", "label": "flower1_paint"}
        ]
    )
    t_flower2 = Interactables("White Rose", "flower2", "images/interactables/case1/flower2.png", page=0,
        actions = [
            {"name": "Paint the Rose", "label": "flower2_paint"}
        ]
    )
    t_flower3 = Interactables("White Rose", "flower3", "images/interactables/case1/flower3.png", page=0,
        actions = [
            {"name": "Paint the Rose", "label": "flower3_paint"}
        ]
    )
    t_flower4 = Interactables("White Rose", "flower4", "images/interactables/case1/flower4.png", page=1,
        actions = [
            {"name": "Paint the Rose", "label": "flower4_paint"}
        ]
    )
    t_flower5 = Interactables("White Rose", "flower5", "images/interactables/case1/flower5.png", page=1,
        actions = [
            {"name": "Paint the Rose", "label": "flower5_paint"}
        ]
    )
    t_flower6 = Interactables("White Rose", "flower6", "images/interactables/case1/flower6.png", page=1,
        actions = [
            {"name": "Paint the Rose", "label": "flower6_paint"}
        ]
    )
    t_flower7 = Interactables("White Rose", "flower7", "images/interactables/case1/flower7.png", page=1,
        actions = [
            {"name": "Paint the Rose", "label": "flower7_paint"}
        ]
    )

    # PART THREE
    t_marcella_end = Interactables("Marcella Lapin", "marcella_end", "images/interactables/case1/rabbitOne.png", page=2,
        actions = [
            {"name": "Talk to Marcella", "label": "marcella_talk_end", "condition": True},
        ]
    )
    t_clockface1 = Interactables("Clock", "clockface1", "images/interactables/case1/clockface1.png", page=0,
        actions = [
            {"name": "Inspect the Clock", "label": "clock1_inspect", "condition": True},
            {"name": "Move the Hour Hand Up", "label": "clock1_up", "condition": False},
            {"name": "Move the Hour Hand Down", "label": "clock1_down", "condition": False},
            {"name": "Move the Hour Hand Left", "label": "clock1_left", "condition": False},
            {"name": "Move the Hour Hand Right", "label": "clock1_right", "condition": False},
        ],
        state = "up"
    )
    t_clockface2 = Interactables("Clock", "clockface2", "images/interactables/case1/clockface2.png", page=1,
        actions = [
            {"name": "Inspect the Clock", "label": "clock2_inspect", "condition": True},
            {"name": "Move the Hour Hand Up", "label": "clock2_up", "condition": False},
            {"name": "Move the Hour Hand Down", "label": "clock2_down", "condition": False},
            {"name": "Move the Hour Hand Left", "label": "clock2_left", "condition": False},
            {"name": "Move the Hour Hand Right", "label": "clock2_right", "condition": False},
        ],
        state = "down"
    )
    t_clockface3 = Interactables("Clock", "clockface3", "images/interactables/case1/clockface3.png", page=2,
        actions = [
            {"name": "Inspect the Clock", "label": "clock3_inspect", "condition": True},
            {"name": "Move the Hour Hand Up", "label": "clock3_up", "condition": False},
            {"name": "Move the Hour Hand Down", "label": "clock3_down", "condition": False},
            {"name": "Move the Hour Hand Left", "label": "clock3_left", "condition": False},
            {"name": "Move the Hour Hand Right", "label": "clock3_right", "condition": False},
        ],
        state = "right"
    )
    t_clockface4 = Interactables("Clock", "clockface4", "images/interactables/case1/clockface4.png", page=2,
        actions = [
            {"name": "Inspect the Clock", "label": "clock4_inspect", "condition": True},
            {"name": "Move the Hour Hand Up", "label": "clock4_up", "condition": False},
            {"name": "Move the Hour Hand Down", "label": "clock4_down", "condition": False},
            {"name": "Move the Hour Hand Left", "label": "clock4_left", "condition": False},
            {"name": "Move the Hour Hand Right", "label": "clock4_right", "condition": False},
        ],
        state = "left"
    )

    
#--------------------------------------------------------------------------
# CASE 1 INGREDIENTS
#--------------------------------------------------------------------------
init python:
    kirby = Item("Kirby with Shortcake", image = "/images/items/item_kirby.png",
        tooltip="Free him...",
        flavor=999)
    c_strawberry = Item("Creamy Strawberry", image = "/images/items/item_strawberry.png",
        tooltip="A tasty strawberry +20 spooky, +30 wonder", 
        flavor=80)
    c_bunnyapples = Item("Bunny Apples", image = "/images/items/item_strawberry.png",
        tooltip="A tasty strawberry +20 spooky, +30 wonder", 
        flavor=60)
    c_herbs = Item("Fine Herbs", image = "/images/items/item_strawberry.png",
        tooltip="A tasty strawberry +20 spooky, +30 wonder", 
        flavor=80)
    c_medicine = Item("Cherry Ooze", image = "/images/items/item_strawberry.png",
        tooltip="A tasty strawberry +20 spooky, +30 wonder", 
        flavor=1)
    c_clockegg = Item("Clockface Egg", image = "/images/items/item_strawberry.png",
        tooltip="A tasty strawberry +20 spooky, +30 wonder", 
        flavor=20)
    c_bluebook = Item("Blue Book") # temporary variables because it's easier to keep track when they're in the inventory
    c_redbook = Item("Red Book")

    
    
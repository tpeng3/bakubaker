#--------------------------------------------------------------------------
# CASE 1 INTERACTABLES
#--------------------------------------------------------------------------
init python:
    # PART ONE
    t_somrem_start = Interactables("Somnia & Remerie", "somrem_start", "images/interactables/case1/somrem1.png", page=0,
        xstart=404, ystart=501,
        actions = [
            {"name": "Talk to SomRem", "label": "somrem_start_talk"}
        ],
        state = "start"
    )
    t_marcella_start = Interactables("Marcella Lapin", "marcella_start", "images/interactables/case1/marchie1.png", page=0,
        xstart=1250, ystart=621,
        actions = [
            {"name": "Talk to Marcella", "label": "marcella_talk_start"}
        ]
    )
    t_bunnysquad = Interactables("Fluffle of Bunnies", "bunnysquad", "images/interactables/case1/fluffle.png", page=0,
        xstart=1167, ystart=532,
        actions = [
            {"name": "Talk (Somnia)", "label": "bunnies_talk_som"},
            {"name": "Talk (Remerie)", "label": "bunnies_talk_rem"}
        ]
    )
    t_strawberry = Interactables("Giant Strawberry", "strawberry", "images/interactables/case1/strawberry.png", page=0,
        xstart=224, ystart=7,
        actions = [
            {"name": "Look at Strawberry", "label": "strawberry_look"}
        ]
    )

    # PART TWO
    t_marcella_mid = Interactables("Marcella Lapin", "marcella_mid", "images/interactables/case1/marchie2.png", page=1,
        xstart=1062, ystart=538,
        actions = [
            {"name": "Talk to Marcella", "label": "marcella_talk_mid"},
        ]
    )
    t_medicine = Interactables("Bottle of Medicine", "medicine", "images/interactables/case1/medicine.png", page=1,
        xstart=957, ystart=253,
        actions = [
            {"name": "Find Medicine", "label": "medicine_find"}
        ]
    )
    t_debris = Interactables("Mounds of Papers", "debris", "images/interactables/case1/debris4.png", page=1,
        xstart=999, ystart=0,
        actions = [
            {"name": "Inspect Pile", "label": "pile_inspect"}
        ],
        state = -1
    )
    t_bunny1 = Interactables("Quiet Bunny", "bunny1", "images/interactables/case1/bunny1.png", page=0,
        xstart=234, ystart=807,
        actions = [
            {"name": "Talk to Bunny", "label": "bunny1_talk", "condition": True},
            {"name": "Give the Medicine", "label": "bunny1_give", "condition": False},
            {"name": "Ask for Help", "label": "bunny1_help", "condition": False},
            {"name": "Chat with Bunny", "label": "bunny1_chat", "condition": False},
            {"name": "Ask for the Time", "label": "bunny1_time", "condition": False}
        ],
        state = "looking"
    )
    t_bunny2 = Interactables("Energetic Bunny", "bunny2", "images/interactables/case1/bunny2.png", page=0,
        xstart=892, ystart=430,
        #xstart=900, ystart=495, for bunny2sleep
        actions = [
            {"name": "Talk to Bunny", "label": "bunny2_talk", "condition": True},
            {"name": "Give the Medicine", "label": "bunny2_give", "condition": False},
            {"name": "Ask for Help", "label": "bunny2_help", "condition": False},
            {"name": "Chat with Bunny", "label": "bunny2_chat", "condition": False},
            {"name": "Ask for the Time", "label": "bunny2_time", "condition": False}
        ]
    )
    t_bunny3 = Interactables("Peevish Bunny", "bunny3", "images/interactables/case1/bunny3.png", page=1,
        xstart=293, ystart=130,
        actions = [
            {"name": "Talk to Bunny", "label": "bunny3_talk", "condition": True},
            {"name": "Give the Medicine", "label": "bunny3_give", "condition": False},
            {"name": "Ask for Help", "label": "bunny3_help", "condition": False},
            {"name": "Chat with Bunny", "label": "bunny3_chat", "condition": False},
            {"name": "Ask for the Time", "label": "bunny3_time", "condition": False}
        ]
    )
    t_bunny4 = Interactables("Studious Bunny", "bunny4", "images/interactables/case1/bunny4.png", page=1,
        xstart=885, ystart=399,
        actions = [
            {"name": "Talk to Bunny", "label": "bunny4_talk", "condition": True},
            {"name": "Give the Medicine", "label": "bunny4_give", "condition": False},
            {"name": "Ask for Help", "label": "bunny4_help", "condition": False},
            {"name": "Chat with Bunny", "label": "bunny4_chat", "condition": False},
            {"name": "Ask for the Time", "label": "bunny4_time", "condition": False}
        ]
    )
    t_bunny5 = Interactables("Clumsy Bunny", "bunny5", "images/interactables/case1/bunny5.png", page=1,
        xstart=1223, ystart=921,
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
        xstart=433, ystart=355,
        actions = [
            {"name": "Paint the Rose", "label": "flower1_paint", "condition": True}
        ]
    )
    t_flower2 = Interactables("White Rose", "flower2", "images/interactables/case1/flower2.png", page=0,
        xstart=818, ystart=974,
        actions = [
            {"name": "Paint the Rose", "label": "flower2_paint", "condition": True}
        ]
    )
    t_flower3 = Interactables("White Rose", "flower3", "images/interactables/case1/flower3.png", page=0,
        xstart=1482, ystart=212,
        actions = [
            {"name": "Paint the Rose", "label": "flower3_paint", "condition": True}
        ]
    )
    t_flower4 = Interactables("White Rose", "flower4", "images/interactables/case1/flower4.png", page=1,
        xstart=423, ystart=630,
        actions = [
            {"name": "Paint the Rose", "label": "flower4_paint", "condition": True}
        ]
    )
    t_flower5 = Interactables("White Rose", "flower5", "images/interactables/case1/flower5.png", page=1,
        xstart=250, ystart=811,
        actions = [
            {"name": "Paint the Rose", "label": "flower5_paint", "condition": True}
        ]
    )
    t_flower6 = Interactables("White Rose", "flower6", "images/interactables/case1/flower6.png", page=1,
        xstart=1497, ystart=949,
        actions = [
            {"name": "Paint the Rose", "label": "flower6_paint", "condition": True}
        ]
    )
    t_flower7 = Interactables("White Rose", "flower7", "images/interactables/case1/flower7.png", page=1,
        xstart=1433, ystart=8,
        actions = [
            {"name": "Paint the Rose", "label": "flower7_paint", "condition": True}
        ]
    )

    # PART THREE
    t_somrem_end = Interactables("Somnia & Remerie", "somrem_end", "images/interactables/case1/somrem3.png", page=2,
        xstart=487, ystart=762,
        actions = [
            {"name": "Talk to SomRem", "label": "somrem_end_talk", "condition": True},
        ]
    )
    t_marcella_end = Interactables("Marcella Lapin", "marcella_end", "images/interactables/case1/marchie3.png", page=2,
        xstart=1400, ystart=94,
        actions = [
            {"name": "Talk to Marcella", "label": "marcella_talk_end", "condition": True},
        ]
    )
    t_clockface1 = Interactables("Clock", "clockface1", "images/interactables/case1/clockface1.png", page=0,
        xstart=543, ystart=138,
        actions = [
            {"name": "Talk about Clock", "label": "clock1_talk", "condition": True},
            {"name": "Inspect the Clock", "label": "clock1_inspect", "condition": False},
            {"name": "Move the Hour Hand Up", "label": "clock1_up", "condition": False},
            {"name": "Move the Hour Hand Down", "label": "clock1_down", "condition": False},
            {"name": "Move the Hour Hand Left", "label": "clock1_left", "condition": False},
            {"name": "Move the Hour Hand Right", "label": "clock1_right", "condition": False},
        ],
        state = "up"
    )
    t_clockface2 = Interactables("Clock", "clockface2", "images/interactables/case1/clockface2.png", page=1,
        xstart=516, ystart=186,
        actions = [
            {"name": "Talk about Clock", "label": "clock2_talk", "condition": True},
            {"name": "Inspect the Clock", "label": "clock2_inspect", "condition": False},
            {"name": "Move the Hour Hand Up", "label": "clock2_up", "condition": False},
            {"name": "Move the Hour Hand Down", "label": "clock2_down", "condition": False},
            {"name": "Move the Hour Hand Left", "label": "clock2_left", "condition": False},
            {"name": "Move the Hour Hand Right", "label": "clock2_right", "condition": False},
        ],
        state = "down"
    )
    t_clockface3 = Interactables("Clock", "clockface3", "images/interactables/case1/clockface3.png", page=2,
        xstart=340, ystart=323,
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
        xstart=1130, ystart=613,
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
    c_strawberry = Item("Creamy Strawberry", image = "/images/items/item_strawberry.png",
        tooltip="A lovely red strawberry showing off it's ripeness. The cross-section looks like a heart!",
        flavor=10)
    c_bunnyapples = Item("Bunny Apples", image = "/images/items/item_apple.png",
        tooltip="Crisp apple slices cut in the shape of bunnies! Simply too cute to eat!",
        flavor=10)
    c_herbs = Item("Fine Herbs", image = "/images/items/item_herbs.png",
        tooltip="Delicately aromatic herbs that will add a light layer of woodsy flavor to any dish.",
        flavor=20)
    c_medicine = Item("Cherry Ooze", image = "/images/items/item_ooze.png",
        tooltip="It says \"Cherry\" on the label, but the bitter smell hints otherwise...",
        flavor=-20)
    c_clockegg = Item("Clockface Egg", image = "/images/items/item_egg.png",
        tooltip="Eggs finely decorated with a thin gold paint and what look to be clock hands.",
        flavor=40)
    c_bluebook = Item("Blue Book") # temporary variables because it's easier to keep track when they're in the inventory
    c_redbook = Item("Red Book")

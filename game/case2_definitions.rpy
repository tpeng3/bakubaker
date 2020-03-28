#--------------------------------------------------------------------------
# CASE 2 INTERACTABLES
#--------------------------------------------------------------------------
init python:
    # PART ONE
    t_closet_door = Interactables("Closet Door", "closet_door", "images/interactables/case1/rabbitOne.png", page=0,
        actions = [
            {"name": "Open the Door", "label": "door_open"}
        ]
    )
    t_agatha_start = Interactables("Agatha Kuprit", "agatha_start", "images/interactables/case1/bunny2.png", page=0,
        actions = [
            {"name": "Talk to Agatha", "label": "agatha_start_talk"}
        ]
    )
    t_blood = Interactables("Pool of Blood", "blood", "images/interactables/case1/bunny2.png", page=0,
        actions = [
            {"name": "Look at Blood", "label": "blood_look"},
            {"name": "Inspect Blood", "label": "blood_inspect"}
        ]
    )
    t_collection = Interactables("Priceless Collection", "collection", "images/interactables/case1/strawberry.png", page=0,
        actions = [
            {"name": "Inspect Collection", "label": "collection_look"},
            {"name": "Take a Whiff", "label": "collection_smell"}
        ]
    )
    t_closet = Interactables("Closet", "closet", "images/interactables/case1/strawberry.png", page=0,
        actions = [
            {"name": "Inspect Closet", "label": "closet_look"},
            {"name": "Take a Whiff", "label": "closet_smell"}
        ]
    )
    t_piano = Interactables("Piano", "piano", "images/interactables/case1/strawberry.png", page=0,
        actions = [
            {"name": "Inspect Piano", "label": "piano_look"},
            {"name": "Take a Whiff", "label": "piano_smell"}
        ]
    )
    t_window = Interactables("Window", "window", "images/interactables/case1/strawberry.png", page=0,
        actions = [
            {"name": "Inspect Window", "label": "window_look"},
            {"name": "Take a Whiff", "label": "window_smell"},
            {"name": "Take a Whiff", "label": "window_inspect"}
        ]
    )
    t_wallpaper = Interactables("Peeling Wallpaper", "wallpaper", "images/interactables/case1/strawberry.png", page=0,
        actions = [
            {"name": "Inspect Wallpaper", "label": "wallpaper_look"},
            {"name": "Take a Whiff", "label": "wallpaper_smell"}
        ]
    )

    # PART TWO
    t_agatha_mid = Interactables("Agatha Kuprit", "agatha_mid", "images/interactables/case1/rabbitOne.png", page=0,
        actions = [
            {"name": "Talk to Agatha", "label": "agatha_talk_mid"},
        ]
    )
    t_shards = Interactables("Broken Shards", "shards", "images/interactables/case1/medicine.png", page=0,
        actions = [
            {"name": "Inspect Broken Shards", "label": "shards_inspect"}
        ]
    )
    # t_window
    t_jewels = Interactables("Scattered Jewels", "jewels", "images/interactables/case1/clocktower.png", page=0,
        actions = [
            {"name": "Inspect Jewels", "label": "jewels_inspect"}
        ]
    )
    t_knife = Interactables("Knife", "bunny1", "images/interactables/case1/bunny1.png", page=0,
        actions = [
            {"name": "Inspect Knife", "label": "knife_inspect"},
            {"name": "Inspect Knife", "label": "knife_jam"}
        ],
        state = False
    )

    # PART THREE
    t_book_love = Interactables("Book on Love", "book_love", "images/interactables/case1/bunny2.png", page=0,
        actions = [
            {"name": "Did the victim have a lover?", "label": "book_love_lover", "condition": True},
            {"name": "Was the victim lonely?", "label": "book_love_lonely", "condition": False},
            {"name": "Was the victim trying to learn pickup lines?", "label": "book_love_pickup", "condition": False}
        ]
    )
    t_voucher = Interactables("Voucher", "voucher", "images/interactables/case1/bunny3.png", page=0,
        actions = [
            {"name": "Is this an event ticket?", "label": "voucher_ticket", "condition": True},
            {"name": "Is this a coupon?", "label": "voucher_coupon", "condition": False}
        ]
    )
    t_newspaper = Interactables("Newspaper", "newspaper", "images/interactables/case1/bunny4.png", page=0,
        actions = [
            {"name": "Check the Front", "label": "newspaper_front", "condition": True},
            {"name": "Check the Back", "label": "newspaper_back", "condition": False},
            {"name": "Check the Crossword", "label": "newspaper_crossword", "condition": False},
        ]
    )
    t_calendar = Interactables("Calendar", "calendar", "images/interactables/case1/bunny5.png", page=0,
        actions = [
            {"name": "Is there a birthday?", "label": "calendar_birthday", "condition": True},
            {"name": "Is there an event?", "label": "calendar_event", "condition": False},
            {"name": "Is there a leap day?", "label": "calendar_leap", "condition": False}
        ]
    )
    t_suits = Interactables("Patterned Suits", "suits", "images/interactables/case1/flower1.png", page=0,
        actions = [
            {"name": "Inspect the Suit", "label": "suits_inspect"},
            {"name": "Inspect the Pockets", "label": "suits_pockets"}
        ]
    )
    # t_knife
    # t_blood
   
    # PART THREE
    # t_agatha_end = Interactables("Agatha Kuprit", "agatha_end", "images/interactables/case1/rabbitOne.png", page=0,
    #     actions = [
    #         {"name": "An Antique Collector", "label": "agatha_end_antique", "condition": True},
    #         {"name": "An Old Famous Musician", "label": "agatha_end_famous", "condition": True},
    #         {"name": "A Lonely Young Musician", "label": "agatha_end_musician", "condition": True},
    #         {"name": "A Murder", "label": "agatha_end_murder", "condition": False},
    #         {"name": "Renovated Apartment", "label": "agatha_end_apartment", "condition": False},
    #         {"name": "Concert Performance", "label": "agatha_end_concert", "condition": False},
    #         {"name": "The Victim Himself", "label": "agatha_end_victim", "condition": False},
    #         {"name": "A Robber", "label": "agatha_end_concert", "condition": False},
    #         {"name": "Concert Performance", "label": "agatha_end_concert", "condition": False},
    #     ]
    # )

    t_piano_end = Interactables("Clock", "clockface1", "images/interactables/case1/clockface1.png", page=0,
        actions = [
            {"name": "Inspect the Piano", "label": "piano_read", "condition": True},
            {"name": "Play Do Re So La", "label": "piano_play1", "condition": False},
            {"name": "Play Do La Fa Mi", "label": "piano_play2", "condition": False},
            {"name": "Play Do Mi Fa La", "label": "piano_play3", "condition": False},
            {"name": "Play Do So Ti Mi", "label": "piano_play4", "condition": False},
        ],
        state = "up"
    )

#--------------------------------------------------------------------------
# CASE 2 INGREDIENTS
#--------------------------------------------------------------------------

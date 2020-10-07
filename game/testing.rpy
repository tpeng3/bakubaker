label testing_room:
    scene black with dissolve
    call initialize_case_test from _call_initialize_case_test # resets the variables in test_definitions.rpy
    $ case = "test"
    menu:
        "VN Testing Room":
            jump test_vn
        "Dream Testing Room":
            jump test_dream
        "Cooking Testing Room":
            jump test_cook
        "Attic Testing Room":
            jump test_attic

#--------------------------------------------------------------------------
# TESTING VN DIALOGUE ROOM
# refer to define_assets.py for the list of the character's expressions and text tags!
# refer to anims.py for available ATLs and transform positions to move the charas!
#--------------------------------------------------------------------------
label test_vn:
    $ _skipping = True # enable skipping option
    $ show_quick_menu = True
    $ somnia_name = "Somnia"
    $ remerie_name = "Remerie"
    $ marcella_name = "Marcella"
    scene storefront with dissolve
    $ somexpr = "gr"
    show somnia with dissolve
    s "This is the VN testing room!"
    $ somexpr = "ex"
    s "Use here for testing out expressions and cool new ATLs!"
    show somnia at right with ease
    $ remexpr = "th"
    show remi at left with dissolve
    r "Right now Tina doesn't know what to add here."
    $ somexpr = "ne"
    s "So here's random fill in text!"
    $ remexpr = "si"
    r "Ok, we're returning back to the testing room menu in 3..."
    $ somexpr = "de"
    r "2..."
    $ remexpr = "pe"
    r "1..."
    jump testing_room

#--------------------------------------------------------------------------
# TESTING ATTIC ROOM
#--------------------------------------------------------------------------
label test_attic:
    dr "There's nothing here!"
    dr "Returning to testing room menu..."
    jump testing_room
# The script of the game goes in this file.

# Unhide extras textbutton in navigation and following two lines if we wanna add this in the future??
# image extras_unlock = Text("{size=60}You've unlocked the Extras Menu. Access it through the Main Menu.{/s}", text_align=0.5)
# image devnotes_unlock = Text("{size=60}You've unlocked a special message. Access it through the Extras Menu.{/s}", text_align=0.5)

## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.

label splashscreen:
    scene black

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.caption:
        menu:
            dr "Would you like sound captions to go along with the story? They help describe music and sound effects in text."
            "On":
                $ persistent.sound_captions = True
            "Off":
                pass
        menu:
            dr "How about image captions? Game visuals will also be described in text."
            "On":
                $ persistent.image_captions = True
            "Off":
                pass
        dr "These options can be changed at any time in the {ii}Main Menu.{/ii}"
        ## This message will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.caption = True

    ## Here begins our splashscreen animation.
    pause(1.0)
    play music "audio/music/Peas_Corps.mp3"
    call screen click_start(skipflip=False) with Dissolve(1.0)

    ## The first time the game is launched, players cannot skip the animation.
    if not persistent.seen_splash:
        ## No input will be detected for the set time stated.
        ## Set this to be a little longer than how long the animation takes.
        $ renpy.pause(8.5, hard=True)
        $ persistent.seen_splash = True

    ## Players can skip the animation in subsequent launches of the game.
    else:
        if renpy.pause(8.5):
            jump skip_splash

    scene black
    with fade

    label skip_splash:
        pass

    return

## The game starts here.
label start:
    $ case = "case1"
    $ tutorial = False
    $ finished = False
    $ inventory = Inventory() # initialize inventory
    show screen keymap_screen
    jump case1_vn
    # menu:
    #     "Start at vn (beginning)":
    #         jump case1_vn
    #     "Start at dream":
    #         jump case1_dream
    #     "Start at cooking":
    #         jump case1_cook
    #     "Start at vn (after dream)":
    #         jump case1_vn_end
    #     "Credits":
    #         show screen credits()

label credits:
    # End Credits

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ show_quick_menu = False

    scene black with fade

    ## Find "End Credits Scroll" in screens.rpy to change text.
    call screen credits

    $ persistent.credits_seen = True

    # $ _game_menu_screen = "save"

    scene black
    with fade

    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:

        pass

    ## We re-enable the quickscreen as the credits are over.

    $ show_quick_menu = True

    ## Makes [result] work. This needs to be near the end of the game
    ## for it to work properly.
    $ percent()

    ## We display a screen that shows how much the player has seen and played of the game.
    show screen results

    centered "Fin"

    if persistent.game_clear:

        pass

    else:

        if readtotal == 100:

            $ achievement.grant("Completionist")
            show devnotes_unlock at truecenter

            $ persistent.game_clear = True

            ## The game will show our text displayable so the player can read it
            ## And only continue when there is input
            pause

    # This ends the game.
    return

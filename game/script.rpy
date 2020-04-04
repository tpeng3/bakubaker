# The script of the game goes in this file.

# Set up LayeredImage Sprites
layeredimage eileen:

    always "eileen_base"

    always "eileen_headband":
        yoffset 25

    group face auto:
        attribute happy default

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#f88787")
define e_nvl = Character("Eileen", color="#f88787", kind=nvl)
define nar_nvl = nvl_narrator

image extras_unlock = Text("{size=60}You've unlocked the Extras Menu. Access it through the Main Menu.{/s}", text_align=0.5)
image devnotes_unlock = Text("{size=60}You've unlocked a special message. Access it through the Extras Menu.{/s}", text_align=0.5)

## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.

label splashscreen:

    scene black

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.caption:

        menu:

            dr "Do you want sound captions on? They describe music and sound effects in text.{fast}"

            "On":

                $ persistent.sound_captions = True

            "Off":

                pass

        menu:

            dr "Do you want image captions on? They describe game visuals in text.{fast}"
            "On":

                $ persistent.image_captions = True

            "Off":

                pass

        dr "These options can be changed at any time in the menu.{fast}"

        ## This message will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.caption = True

    ## Here begins our splashscreen animation.
    call screen click_start with dissolve

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
    menu:
        "Start at vn (beginning)":
            jump case1_vn
        "Start at dream":
            jump case1_dream
        "Start at cooking":
            jump case1_cook

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

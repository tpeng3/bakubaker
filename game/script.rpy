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

## Setting up images for use in the splashscreen
image renpy_name = Text("{size=60}Made with Ren'Py [renpy.version_only]{/s}", text_align=0.5)

## The animation is kinda tacky so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html

image splash_anim_1:

    "gui/renpy-logo.png"
    xalign 0.5 yalign -0.5
    ease_quad 5.0 xalign 0.5 yalign 0.5 rotate 360
    linear 2.0 zoom 2.0

image splash_anim_2:
    "renpy_name"
    xalign 0.5 yalign 0.8 alpha 0.0
    pause 6.0
    linear 1.0 alpha 1.0

label splashscreen:

    scene black

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.caption:

        menu:

            "Do you want sound captions on? They describe music and sound effects in text.{fast}"

            "On":

                $ persistent.sound_captions = True

            "Off":

                pass

        menu:

            "Do you want image captions on? They describe game visuals in text.{fast}"
            "On":

                $ persistent.image_captions = True

            "Off":

                pass

        "These options can be changed at any time in the menu.{fast}"

        ## This message will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.caption = True

    ## Here begins our splashscreen animation.
    show splash_anim_1
    show splash_anim_2
    
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
    menu:
        "Accessibility Tutorial":
            jump accessibility
        "Tina's room for prototyping mechanics":
            jump tina


label accessibility:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite.

    show eileen happy at center:

        ## Sprite generated by Mannequin are fullbody, so we do need to
        ## move Eileen down slightly so she's not floating about.
        yoffset 250

    # Placing the effect after both image statements will apply said
    # effect on both images.
    
    with fade

    # This plays our music file in a way that if audio captions are on,
    # it will tell us the name of the song. This music plays at full volume
    # after 2 seconds and fades out after 2 seconds when stopped.
    $ play_music(garden,fadein=2.0,fadeout=2.0)

    # This unlocks the the achievement with the corresponding name
    $ achievement.grant("Beginning")

    # This adds an integer value to a point-based achievement.
    # To track how much of it has been earned, use a regular variable for now.
    $ achievement.progress("Point_Collector", 10)
    $ persistent.points += 10

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    # This changes the sprite's expression

    show eileen neutral with dissolve

    e "Once you add a story, pictures, and music, you can release it to the world!"

    show eileen happy with dissolve

    e "Haha, sorry. Had to get that out of the way first."

    e "Thanks for downloading this Baku Baker! After you play through this script, be sure to open up the files and adapt them to your project's needs."

    e "You can even make a copy of the entire {color=#32CD32}game{/color} folder and start your project from there."
    
    e "So now, let's demonstrate some of the custom Accessibility Options."

    e "When you run this project for the first time, you should have been able to adjust the Audio and Image Caption options."

    e "I'll make some sounds now. If Audio Captions are on, you'll see a notification in the top-left corner describing the sound."
    
    # This plays our sound file in a way that if audio captions are on,
    # it will describe the sound being played.
    $ play_sound(door)

    e "Let's close this so the breeze doesn't mess up my hair..."

    $ play_sound(drawer_open)

    e "Let me look for a pen..."

    $ play_sound(drawer_close)

    e "Not in there?"

    $ play_sound(drawer_open)

    e "Maybe here?"

    $ play_sound(drawer_close)

    e "Found it!"

    e "If you had your Audio Captions on, you should have seen something appear in the notification tab."

    e "Neat, right?"

    e "Now let's test Image Captions."

    show eileen at right with move

    ic "Eileen walks to the right of the room."

    e "Over here..."

    show eileen at left with move

    ic "Eileen walks to the left of the room."

    e "Now here..."

    show eileen at center with move

    ic "Eileen walks to the center of the room."

    e "And there we go!"

    e "If you had your Image Captions on, then you should have seen some extra narration describing my movements."

    e "This is done with the special {color=#32CD32}{i}ic{/i}{/color} speaker tag we defined in {color=#32CD32}{i}captiontool.rpy{/i}{/color}."

    e "Now, let's test the Screen Shake settings."

    $ shake()

    show eileen surprised with dissolve

    ic "The room shakes."

    e "Ah! An earthquake!"

    e "You can turn the screen shaking effect off in Preferences, just in case the motion makes you sick. One more time."

    $ shake()

    ic "The room shakes again."

    e "Now let's try NVL Mode."

    nar_nvl "NVL Mode is a different way of displaying text on the screen."

    e_nvl "Unlike ADV, past lines of dialogue are still displayed until it is cleared off."

    nar_nvl "Usually NVL will cover the entire screen, but you can adjust the size of the window to only cover a certain part if need be."

    nvl clear

    e_nvl "Not all games may need to use both ADV and NVL, but it's nice to have options as a developer."

    e_nvl "With that said, let's go somewhere else."

    nar_nvl "Eileen wonders where she should travel to."

    nvl clear

    stop music fadeout 1.0

    ## This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()

    menu:

        "Office":

            ## This empty label is solely for replay mode purposes.

            label office:

                pass

            e "To the office? Okay...?"

            $ achievement.grant("Office")

            $ play_music(business,fadein=2.0,fadeout=2.0)

            scene future_office
            show eileen angry at center:
                yoffset 250
            with fade

            e "Ugh, I don't like it here."

            "Eileen seems bothered by something."

        "Beach":

            label beach:

                pass

            e "The beach sounds fun!"

            $ achievement.grant("Beach")

            $ play_music(summer,fadein=2.0,fadeout=2.0)

            scene sort_of_beautiful_beach_day
            show eileen upset at center:
                yoffset 250
            with fade

            e "Oh shoot, I forgot my swimsuit."

            "Eileen seems upset by something."

    "Remember to check the History screen if you have not done so yet."

    ## This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()

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

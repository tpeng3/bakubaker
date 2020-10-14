## This is a resource name loader that will import the names of files from certain folders
## Intended as a way to quickly grab file names to use in accessibility.rpy, screens.rpy, and captiontool.rpy
## Remember to add commas to the end of each listed item
## As of RenPy7, basic images do not have to be defined (LayeredImages still need to be set up)

python early hide:
    @renpy.atl_warper
    def quad(t): # custom ease function for panning
      return -2.0 * t**3 + 3.0 * t**2

init -1:
    $ redefine_resources = False
    ## When you add, delete or rename an image or music resource, change redefine_resources to True and launch the project

## Sprites:
    image strawberry = Transform("/images/items/GET_strawberry.png")
    image apple = Transform("/images/items/GET_apple.png")
    image herbs = Transform("/images/items/GET_herbs.png")
    image ooze = Transform("/images/items/GET_ooze.png")
    image egg = Transform("/images/items/GET_egg.png")

    image clockup = "/images/items/clock_up.png"
    image clockleft = "/images/items/clock_left.png"
    image clockright = "/images/items/clock_right.png"
    image clockdown = "/images/items/clock_down.png"
    image clockhour = "/images/items/clock_hour.png"
    image clockhour_left = "/images/items/clock_hour.png"
    image clockhour_right = "/images/items/clock_hour.png"
    image clockhour_up = "/images/items/clock_hour.png"
    image clockhour_down = "/images/items/clock_hour.png"


    image cooksom = "images/interactables/cooksom.png"
    image cookrem = "images/interactables/cookrem.png"

    image omelette = "images/items/dish_omelette.png"
    image omeletteBest = "images/items/dish_omelette2.png"

## BG:
    image storefront = "images/BG/bg_storefront.png"
    image dreamoffice = "images/BG/bg_dreamoffice.png"
    image wonderland = "images/BG/bg_wonderland_v2.png"
    image black = "#000"
    image cloud = "#ebdcc3"

## UI:
    image menuSplash = "gui/overlay/menu_splash.png"
    image menuMain = "gui/overlay/menu_main.png"
    image menuFront = "gui/overlay/menufront.png"
    image menuBack:
        contains:
            xalign 0.85 yalign 0.5
            anim.Filmstrip ("images/cg/menuflip.png", (564,749), (1,5), 0.10, loop=False)
    image clickStart = "gui/button/clickstart.png"
    image snacks1 = "gui/overlay/snacks1.png"
    image snacks2 = "gui/overlay/snacks2.png"
    image snacks3 = "gui/overlay/snacks3.png"

    image cookCTC:
        contains:
            xalign 0.5 yalign 0.96
            "gui/ctc_1.png"
            zoom 0.7
            linear 0.15 yalign 0.95
            pause 0.25
            linear 0.10 yalign 0.96
            "gui/ctc_2.png"
            zoom 0.7
            xalign 0.5 yalign 0.95
            pause 0.25
            linear 0.15 yalign 0.96
            repeat
    image dreamCTC:
        contains:
            xalign 0.5 yalign 0.26
            "gui/dctc_1.png"
            zoom 0.7
            linear 0.15 yalign 0.25
            pause 0.25
            linear 0.10 yalign 0.26
            "gui/dctc_2.png"
            zoom 0.7
            xalign 0.5 yalign 0.25
            pause 0.25
            linear 0.15 yalign 0.26
            repeat
    image narrCTC:
        contains:
            xalign 0.5 yalign 0.27
            "gui/nctc_1.png"
            zoom 0.7
            linear 0.15 yalign 0.26
            pause 0.25
            linear 0.10 yalign 0.27
            "gui/nctc_2.png"
            zoom 0.7
            xalign 0.5 yalign 0.26
            pause 0.25
            linear 0.15 yalign 0.27
            repeat

    image goLeft = "gui/button/goleft.png"
    image goLeftHov = "gui/button/goleftHov.png"
    image goRight = "gui/button/goright.png"
    image goRightHov = "gui/button/gorightHov.png"
    image goCook = "gui/button/button_cookbook.png"
    image goCookHov = "gui/button/button_cookbook2.png"
    image goDream = "gui/button/button_dream.png"
    image goDreamHov = "gui/button/button_dream2.png"
    image goEat = "gui/button/button_cook.png"
    image goEatHov = "gui/button/button_cook2.png"
    image selBorder = "gui/selected.png"
    image itrFrame = "gui/frame_interactable.png"
    image ingFrame = "gui/frame_ingredient.png"
    image naviButton = "gui/button/navigation_idle_background.png"
    image naviHoverButton = "gui/button/navigation_hover_background.png"

## BGs:
    image wonderland2 = "images/BG/bg_wonderland_v2.png"
    image starry = "images/BG/starry.png"
    image cauldron:
        "images/BG/cauldronswirl.png"
        rotate 0
        linear 90.0 rotate 360
        repeat
    image cauldron_drop:
        "images/BG/cauldronswirl.png"
        alpha 0
        xanchor 0.5 yanchor 0.5
        size (180, 180)
    image cookbook = "images/BG/bg_cookbook.png"

## CGs:
    image logo = "images/CG/logo.png"
    image outside = "images/CG/outside.png"
    image enterdream = "images/CG/incense_todream.png"
    image incenseout = "images/CG/incense_out.png"
    image marchiecollapse = "images/CG/marchiecollapse.png"

## Music:
# init -2 python:
    define audio.splashscreen = "audio/music/Peas_Corps.mp3"
    define audio.storefront = "audio/music/MusMus-BGM-092.mp3"
    define audio.dreamoffice = "audio/music/gozennijinofunsui.mp3"
    define audio.weird = "audio/music/Thick_Irony.mp3"
    define audio.dream1 = "audio/music/MusMus-BGM-089.mp3"
    define audio.dream2 = "audio/music/r3.mp3"
    define audio.cooking1 = "audio/music/Netherland.mp3"
    define audio.cooking2 = "audio/music/Vibe_Drive.mp3"
    define audio.storeend = "audio/music/valentine.mp3"


## Music Caption:
    # Careless-Summer_Looping: _("")
    # Future-Business_v001: _("")
    # Sculpture-Garden_Looping: _("")
    # The-Concrete-Bakes_Looping: _("")

## SFX:
    define audio.rimshot = "audio/sfx/rimshot.ogg"
    define audio.bubble = "audio/sfx/bubble.ogg"
    define audio.clockdong = "audio/sfx/clockdong.ogg"
    define audio.clockring = "audio/sfx/clockring.ogg"
    define audio.clocktick = ["<silence 0.2>", "audio/sfx/clocktick.ogg"]
    define audio.clocktwist = "audio/sfx/clocktwist.ogg"
    define audio.donecooking = "audio/sfx/donecooking.ogg"
    define audio.itemget = "audio/sfx/itemget.ogg"
    define audio.trip = "audio/sfx/trip1.ogg"
    define audio.welcomedoor = "audio/sfx/welcomedoor.ogg"
    define audio.windchimes = "audio/sfx/windchimes.wav"
    define audio.paint = "audio/sfx/paint.ogg"
    define audio.yawn = "audio/sfx/yawn.ogg"
    define audio.incense = "audio/sfx/incense.ogg"
    define audio.thud = "audio/sfx/thud.ogg"
    define audio.whoosh = "audio/sfx/whoosh.ogg"
    define audio.paper = "audio/sfx/paper.ogg"

## SFX Caption:
    # Chest-Drawer_Close: _("")
    # Chest-Drawer_Open: _("")
    # Edge-of-Ocean: _("")
    # Interior-Door_Close: _("")













## Script to redefine the images:
## !!! DO NOT CHANGE THE CODE BELOW THIS POINT !!!
init -1 python:

    if redefine_resources:
        with open(renpy.loader.transfn('definitions.rpy'), 'rb') as f:
            s = f.read()
        f.closed
        pos = s.find('## Script to redefine the images')
        if pos>1:
            s=s[pos:]

        with open(renpy.loader.transfn('definitions.rpy'), 'wb') as f:
            f.write('## This is a resource name loader that will import the names of files from certain folders\n## Intended as a way to quickly grab file names to use in accessibility.rpy, screens.rpy, and captiontool.rpy\n## Remember to add commas to the end of each listed item\n## As of RenPy7, basic images do not have to be defined (LayeredImages still need to be set up)\r\ninit -1:\r\n    $ redefine_resources = False\n    ## When you add, delete or rename an image or music resource, change redefine_resources to True and launch the project\r\n\r\n')

            f.write('## Sprites:\r\n')
            for file in renpy.list_files():
                if file.startswith('images/sprites') and (file.endswith('.png') or file.endswith('.webp')):
                    name = file.replace('images/sprites/','').replace('/', ' ').replace('.png','').replace('.webp','')
                    img_str = 'image ' + name + ' = "' + file + '"'
                    f.write('    # ' + img_str + '\r\n')

            f.write('## BGs:\r\n')
            for file in renpy.list_files():
                if file.startswith('images/BG/') and (file.endswith('.png') or file.endswith('.webp') or file.endswith('.jpg')):
                    name = file.replace('images/BG/','').replace('/', ' ').replace('.png','').replace('.webp','').replace('.jpg','')
                    img_str = 'image ' + name + ' = "' + file + '"'
                    f.write('    # ' + img_str + '\r\n')

            f.write('## CGs:\r\n')
            for file in renpy.list_files():
                if file.startswith('images/CG/') and (file.endswith('.png') or file.endswith('.webp') or file.endswith('.jpg')):
                    name = file.replace('images/CG/','').replace('/', ' ').replace('.png','').replace('.webp','').replace('.jpg','')
                    img_str = 'image ' + name + ' = "' + file + '"'
                    f.write('    # ' + img_str + '\r\n')

            f.write('\r\n## Music:\r\n# init -2 python:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/music/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/music/','').replace('/', ' ').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + my_str + '\r\n')

            f.write('\r\n## Music Caption:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/music/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/music/','').replace('/', ' ').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + name + ': _("")' + '\r\n')

            f.write('\r\n## SFX:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/sfx/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/sfx/','').replace('/', ' ').replace(' ', '_').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + my_str + '\r\n')

            f.write('\r\n## SFX Caption:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/sfx/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/sfx/','').replace('/', ' ').replace(' ', '_').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + name + ': _("")' + '\r\n')
            f.write('\r\n')
        f.closed

        with open(renpy.loader.transfn('definitions.rpy'), 'ab') as f:
            f.write(s)
        f.closed

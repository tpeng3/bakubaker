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
    # image eileen_base = "images/sprites/eileen_base.png"
    # image eileen_face_angry = "images/sprites/eileen_face_angry.png"
    # image eileen_face_happy = "images/sprites/eileen_face_happy.png"
    # image eileen_face_neutral = "images/sprites/eileen_face_neutral.png"
    # image eileen_face_surprised = "images/sprites/eileen_face_surprised.png"
    # image eileen_face_upset = "images/sprites/eileen_face_upset.png"

    image omelette = "images/items/dish_omelette.png"
    image omeletteBest = "images/items/dish_omelette2.png"

    # Case 1 assets ---------------------------------------------------------------
    image storefront = "images/BG/bg_storefront.png"
    image dreamoffice = "images/BG/bg_dreamoffice.png"
    image wonderland = "images/BG/bg_wonderland_v2.png"

    image marchie:
        Crop ((0,0,800,900), "images/sprites/client1.png")


## UI:
    image goLeft = "gui/button/goleft.png"
    image goLeftHov = "gui/button/goleftHov.png"
    image goRight = "gui/button/goright.png"
    image goRightHov = "gui/button/gorightHov.png"
    image icon_somnia = "gui/mouse_somnia.png"
    image icon_remerie = "gui/mouse_remerie.png"
    image goCook = "gui/button/button_cookbook.png"
    image goCookHov = "gui/button/button_cookbook2.png"
    image goDream = "gui/button/button_dream.png"
    image goDreamHov = "gui/button/button_dream2.png"
    image goEat = "gui/button/button_cook.png"
    image goEatHov = "gui/button/button_cook2.png"
    image selBorder = "gui/selected.png"

## BGs:
    # image future_office = "images/BG/future_office.jpg"
    # image room = "images/BG/room.jpg"
    # image sort_of_beautiful_beach_day = "images/BG/sort_of_beautiful_beach_day.jpg"
    image wonderland2 = "images/BG/bg_wonderland_v2.png"

    image cookbook = "images/BG/bg_cookbook.png"
    image cookbook2 = "images/BG/test_cookbook.png"

## CGs:
    # image cg_locked = "images/CG/cg_locked.jpg"

## Music:
# init -2 python:
    # Careless-Summer_Looping = "audio/music/Careless-Summer_Looping.mp3"
    # Future-Business_v001 = "audio/music/Future-Business_v001.mp3"
    # Sculpture-Garden_Looping = "audio/music/Sculpture-Garden_Looping.mp3"
    # The-Concrete-Bakes_Looping = "audio/music/The-Concrete-Bakes_Looping.mp3"
    define audio.storefront = "audio/music/MusMus-BGM-092.mp3"
    define audio.dreamoffice = "audio/music/gozennijinofunsui.mp3"
    define audio.weird = "audio/music/Thick_Irony.mp3"
    define audio.dream1 = "audio/music/MusMus-BGM-089.mp3"
    # define audio.dream2 = "audio/music/-"
    define audio.cooking1 = "audio/music/Netherland.mp3"
    define audio.cooking2 = "audio/music/Vibe_Drive.mp3"

## Music Caption:
    # Careless-Summer_Looping: _("")
    # Future-Business_v001: _("")
    # Sculpture-Garden_Looping: _("")
    # The-Concrete-Bakes_Looping: _("")

## SFX:
    # Chest-Drawer_Close = "audio/sfx/Chest-Drawer_Close.mp3"
    # Chest-Drawer_Open = "audio/sfx/Chest-Drawer_Open.mp3"
    # Edge-of-Ocean = "audio/sfx/Edge-of-Ocean.mp3"
    # Interior-Door_Close = "audio/sfx/Interior-Door_Close.mp3"
    define audio.rimshot = "audio/sfx/rimshot.ogg"

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

#--------------------------------------------------------------------------
# INITIALIZE THOUGHT INVENTORY
#--------------------------------------------------------------------------
init -1 python:
    inv_page = 0 # initial page of the inventory screen
    sel_xpos = None
    sel_ypos = None

    class Item(store.object):
        def __init__(self, name, image="", tooltip=""):
            self.name = name # name of item
            self.image = image # image url
            self.tooltip = tooltip # tooltip desc

    class Inventory(store.object):
        def __init__(self):
            self.items = []
            self.selitem = None
        def add(self, item):
            if item not in self.items: # we don't want duplicates
                self.items.append(item)
        def remove(self, item):
            self.items.remove(item)
        def select(self, item):
            self.selitem = item

#--------------------------------------------------------------------------
# CUSTOMIZE THOUGHT INVENTORY SCREEN
#--------------------------------------------------------------------------
screen inventory():
    zorder 2
    modal True
    frame:
        pass

    imagebutton:
        idle "gui/button/button_back.png"
        hover im.MatrixColor("gui/button/button_back.png", im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0))
        xalign 1.0 yalign 0
        action [ToggleScreen('inventory')]


    #TODO: add better positions for the inventory, after UI is decided
    hbox:
        for item in inventory.items:
            imagebutton:
                idle item.image
                action [Function(inventory.select, item)]
                tooltip item.tooltip

    # this is if we want to select any items to focus, otherwise we don't need this code
    # if inventory.selitem is not None:
    #     text "sel item is" + inventory.selitem.name ypos 520

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            xalign 0.5 yalign 0.5 #tmp

#--------------------------------------------------------------------------
# DEFINE ITEMS (thoughts)
#--------------------------------------------------------------------------
init python:
    kirby = Item("Kirby with Shortcake", image = "/images/items/item_kirby.png",
        tooltip="Free him...")
    
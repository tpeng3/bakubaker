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
    textbutton "close inventory" xpos 1000 ypos 520 action Hide('inventory')

    hbox:
        for item in inventory.items:
            imagebutton:
                idle item.image
                action [Function(inventory.select, item)]
                tooltip item.tooltip

    if inventory.selitem is not None:
        text "sel item is" + inventory.selitem.name ypos 520

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]"

#--------------------------------------------------------------------------
# DEFINE ITEMS (thoughts)
#--------------------------------------------------------------------------
init python:
    item_cake = Item("Imaginary Cake", image = "[insert image path]",
        tooltip="this is a temp item, here to show the format of initializing items")
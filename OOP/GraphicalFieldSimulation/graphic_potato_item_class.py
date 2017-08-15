from OOP.GraphicalFieldSimulation.graphic_crop_item_class import CropGraphicsPixmapItem
from OOP.potato_class import Potato


class PotatoGraphicsPixmapItem(CropGraphicsPixmapItem):
    """this class provides a graphical representation of a potato"""

    # constructor
    def __init__(self):
        self.available_graphics = [":/potato_seed.png", ":/potato_seedling.png", ":/potato_young.png",
                                   ":/potato_mature.png", ":/potato_old.png"]
        super().__init__(self.available_graphics)

        self.crop = Potato()

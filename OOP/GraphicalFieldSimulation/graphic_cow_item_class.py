from GraphicalFieldSimulation.cow_class import Cow
from GraphicalFieldSimulation.graphic_animal_item_class import AnimalGraphicsPixmapItem



class CowGraphicsPixmapItem(AnimalGraphicsPixmapItem):
    """this class provides a graphical representation of a cow"""

    # constructor
    def __init__(self):
        self.available_graphics = [":/cow_baby.png", ":/cow_poor.png", ":/cow_fine.png", ":/cow_prime.png"]
        super().__init__(self.available_graphics)

        self.animal = Cow("")

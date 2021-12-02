from ursina import *
from ursina import texture
from ursina import text

class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (.5,.8),
            origin = (-.5,.5),
            position = (-.3,.4),
            texture = 'white_cube',
            texture_scale = (5,8),
            color = color.dark_gray
        )
        self.item_parent = Entity(parent=self,scale=(1/5,1/8))

if __name__ == '__main__':
    app = Ursina()
    inventory = Inventory()
    item = Button(parent = inventory.item_parent,origin=(-.5,.5),color=color.red,position=(0,0))
    item = Button(parent = inventory.item_parent,origin=(-.5,.5),color=color.green,position=(2,0))
    app.run()
from GameObjects.GameObject import GameObject

class Bat(GameObject):
    
    width = 10
    height = 100

    def __init__(self, x):
        self.x = x


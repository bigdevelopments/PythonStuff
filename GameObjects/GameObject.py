class GameObject:

    x = 0
    y = 0
    dx = 0
    dy = 0

    def tick(self):
        self.x+=self.dx
        self.y+=self.dy

    def draw(self, screen):
        pass

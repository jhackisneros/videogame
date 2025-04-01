class entity:
    def __init__(self,x,y,imagen):
        self.x = x
        self.y = y
        self.imagen = imagen
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
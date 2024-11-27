class Object():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isMoved = False

    def move(self, map):
        return
class Ex:

    def init(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

class Extended(Ex):
    def init(self, x, y, z, color=None):
        super(Extended, self).init(x, y, z)
        if not color:
            self.color = "Gray"

    def volume_and_color(self):
        return self.x * self.y * self.z, self.color


if __name__== '__main__':
    a = Extended(4, 10, 3)
    print(a.volume())
    print(a.volume_and_color())
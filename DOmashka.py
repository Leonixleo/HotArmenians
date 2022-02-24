

class Ex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z


class Ex2(Ex):
    pass


class Extended(Ex):
    def __init__(self, x, y, z, color=None):
        super(Extended, self).__init__(x,y,z)
        if not color:
            self.color ="Mwvane"

    def volume_and_color(self):
        return self.x * self.y * self.z, self.color

if __name__ =='__main__':
    a = Extended(6, 15, 38)
    print(a.volume())
    print(a.volume_and_color())


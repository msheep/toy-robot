class Robot(object):
    global _directions
    _directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.f = ""
        self.min_x = 0
        self.min_y = 0
        self.max_x = 4
        self.max_y = 4

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = int(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = int(value)

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = value

    def place(self, x, y, f):
        try:
            for val in (x, y):
                if int(val) not in range(0, 5):
                    print("ERROR: Invalid position ", val)
                    return
            if f not in _directions:
                print("ERROR: Invalid direction ", f)
                return
            self.x = x
            self.y = y
            self.f = f
        except (TypeError, ValueError):
            print("ERROR: Invalid position ", x, y)
            return False

    def move(self):
        if self.f == "NORTH" and self.y != self.max_y:
            self.y += 1
        elif self.f == "EAST" and self.x != self.max_x:
            self.x += 1
        elif self.f == "SOUTH" and self.y != self.min_y:
            self.y -= 1
        elif self.f == "WEST" and self.x != self.min_x:
            self.x -= 1

    def turn_left(self):
        current_index = _directions.index(self.f)
        self.f = _directions[current_index - 1]

    def turn_right(self):
        if self.f == _directions[-1]:
            self.f = _directions[0]
        else:
            current_index = _directions.index(self.f)
            self.f = _directions[current_index + 1]

    def report(self):
        print ("OUTPUT: ", self.x, self.y, self.f)

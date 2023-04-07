class Point:
    _x = 0
    _y = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set(self, x, y):
        self._x = x
        self._y = y

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


p1 = Point(1, 1)

print(p1.x, p1.y)
p1.set(5,5)
print(p1.x, p1.y)
print(p1.length())

p2 = Point(1, 1)
print(p1.x, p1.y)
print(p1._x, p1._y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, origin, width, hight):
        self.origin = origin
        self.width = width
        self.hight = hight

    def get_area(self):
        return self.width * self.hight

    def print_coordinates(self):
        top_right_corner = self.origin.x + self.width
        bottom_left_corner = self.origin.y + self.hight
        print('Starting Point (X)): ' + str(self.origin.x))
        print('Starting Point (Y)): ' + str(self.origin.y))
        print('End Point X-Axis (Top Right): ' + str(top_right_corner))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left_corner))


def build_rectangle():
    rectangle_origin = Point(50, 100)
    rectangle = Rectangle(rectangle_origin, 90, 10)

    return rectangle


rectangle = build_rectangle()

print(rectangle.get_area())
rectangle.print_coordinates()

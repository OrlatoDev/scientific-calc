from Calc import Calc
from math import sqrt, pi

class AreasAndVolumes(Calc):
    def rectangle_area(self, x, y):
        return x * y

    def triangle_area(self, b, h):
        return (b * h) / 2

    def hexagon_area(self, x):
        return (3 * sqrt(3) / 2) * x**2

    def circle_area(self, r, pi = pi):
        return pi * r**2

    def rectangular_prism_volume(self, l, w, h):
        return l * w * h

    def pyramid_volume(self, b, h):
        return 1 / 3 * b * h

    def sphere_volume(self, r, pi = pi):
        return 4 / 3 * pi * r**3
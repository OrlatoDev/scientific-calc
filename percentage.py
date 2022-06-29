from Calc import Calc

class Percentage(Calc):
    def percent_of(self, percent, value):
        return round(percent / 100 * value, 2)

    def percent_x_out_of_y(self, x, y):
        return f"{x} is {x * 100 / y}% out of {y}"
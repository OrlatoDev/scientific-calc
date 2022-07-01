from pip import main
from Calc import Calc

from equations import Equations
from units_converter import UnitsConverter
from areas_and_volumes import AreasAndVolumes
from percentage import Percentage
from factorial import Factorial
from binary import Binary

c = Calc()

main_options = [
    "Equations and Algebra", 
    "Units Converter",
    "Areas and Volumes",
    "Percentage", 
    "Factorial",
    "Binary Converter",
    "GCD (Greatest Common Divisor)",
    "LCM (Least Common Multiple)",
    "Averages",
    "Quit"
]

while c.running:
    c.menu("Scientific Calculator", main_options)
    main_response = c.get_response(main_options)

    if main_response == 0:
        fde = Equations()

        options = [
            "Calc",
            "Quit"
        ]

        while fde.running:
            fde.menu("Equations and Algebra", options)
            response = fde.get_response(options)

            if response == 0:
                print("\nTips: ")
                print("1. for simple operations use the default symbols (+, -, *, /, =)")
                print("2. for exponentiation use ** (to write 2² use 2**2)")
                print("3. for rooting use sqrt() (to write √2 use sqrt(2))\n")
                eq = str(input("Type your equation: "))

                fde.print_success("Result(s): ")
                fde.solve(eq)
                fde.await_action()

    elif main_response == 1:
        uc = UnitsConverter()

        options = [
            "Centimeters and Meters",
            "Kilometers and Meters",
            "Miles and Meters",
            "Quit"
        ]

        while uc.running:
            uc.menu("Units Converter", options)
            response = uc.get_response(options)

            if response == 0:
                print("leave blank what you want to find out")
                centimeters = input("centimeters: ")
                meters = input("meters: ")

                if uc.centimetersAndMeters(centimeters, meters) == 1:
                    uc.print_error("Error, follow the instructions...")
                    uc.await_action()

                else:
                    uc.print_success("Result: " + str(uc.centimetersAndMeters(centimeters, meters)))
                    uc.await_action()

            elif response == 1:
                print("leave blank what you want to find out")
                kilometers = input("kilometers: ")
                meters = input("meters: ")

                if uc.kilometersAndMeters(kilometers, meters) == 1:
                    uc.print_error("Error, follow the instructions...")
                    uc.await_action()

                else:
                    uc.print_success("Result: " + str(uc.kilometersAndMeters(kilometers, meters)))
                    uc.await_action()

            elif response == 2:
                print("leave blank what you want to find out")
                miles = input("miles: ")
                meters = input("meters: ")

                if uc.milesAndMeters(miles, meters) == 1:
                    uc.print_error("Error, follow the instructions...")
                    uc.await_action()

                else:
                    uc.print_success("Result: " + str(uc.milesAndMeters(miles, meters)))
                    uc.await_action()

    elif main_response == 2:
        aav = AreasAndVolumes()

        options = [
            "Rectangle (area)",
            "Triangle (area)",
            "Hexagon (area)",
            "Circle (area)",
            "Rectangular Prism (volume)",
            "Pyramid (volume)",
            "Sphere (volume)",
            "Quit"
        ]

        while aav.running:
            aav.menu("Areas and Volumes", options)
            response = aav.get_response(options)

            if response == 0:
                x = float(input("(width) x: "))
                y = float(input("(height) y: "))

                aav.print_success("Result: " + str(aav.rectangle_area(x, y)))
                aav.await_action()

            elif response == 1:
                b = float(input("(base) b: "))
                h = float(input("(height) h: "))

                aav.print_success("Result: " + str(aav.triangle_area(b, h)))
                aav.await_action()

            elif response == 2:
                x = float(input("(sides size) x: "))

                aav.print_success("Result: " + str(aav.hexagon_area(x)))
                aav.await_action()   

            elif response == 3:
                r = float(input("(radius) r: "))

                try:
                    pi = float(input("(blank to default) pi: "))
                    aav.print_success("Result: " + str(aav.circle_area(r, pi)))
                except:
                    aav.print_success("Result: " + str(aav.circle_area(r)))
                
                aav.await_action()

            elif response == 4:
                l = float(input("(length) l: "))
                x = float(input("(width) x: "))
                y = float(input("(height) y: "))

                aav.print_success("Result: " + str(aav.rectangular_prism_volume(l, x, y)))
                aav.await_action()

            elif response == 5:
                b = float(input("(base area) b: "))
                h = float(input("(height) h: "))

                aav.print_success("Result: " + str(aav.pyramid_volume(b, h)))
                aav.await_action()

            elif response == 6:
                r = float(input("(radius) r: "))

                try:
                    pi = float(input("(blank to default) pi: "))
                    aav.print_success("Result: " + str(aav.sphere_volume(r, pi)))
                except:
                    aav.print_success("Result: " + str(aav.sphere_volume(r)))
                
                aav.await_action()

    elif main_response == 3:
        pct = Percentage()

        options = [
            "% from x value",
            "How many % is x out of y",
            "Quit"
        ]

        while pct.running:
            pct.menu("Percentage", options)
            response = pct.get_response(options)

            if response == 0:
                percent = float(input("%: "))
                value = float(input("of: "))

                pct.print_success("Result: " + str(pct.percent_of(percent, value)))
                pct.await_action()

            elif response == 1:
                x = float(input("x: "))
                y = float(input("y: "))

                pct.print_success("Result: " + str(pct.percent_x_out_of_y(x, y)))
                pct.await_action()

    elif main_response == 4:
        fct = Factorial()

        options = [
            "Calc",
            "Quit"
        ]

        while fct.running:
            fct.menu("Factorial", options)
            response = fct.get_response(options)

            if response == 0:
                x = int(input("x: "))

                fct.print_success("Result: " + str(fct.factorial(x)))
                fct.await_action()

    elif main_response == 5:
        binc = Binary()

        options = [
            "Binary to Decimal",
            "Decimal to Binary",
            "Quit"
        ]

        while binc.running:
            binc.menu("Binary Converter", options)
            response = binc.get_response(options)

            if response == 0:
                b = str(input("Binary: "))

                binc.print_success("Result: " + str(binc.toDec(b)))
                binc.await_action()

            elif response == 1:
                d = int(input("Decimal: "))

                binc.print_success("Result: " + str(binc.toBinary(d)))
                binc.await_action()
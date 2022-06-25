# scientific calculator
from Calc import Calc

from equations import Equations
from units_converter import UnitsConverter
from areas_and_volumes import AreasAndVolumes
from percentage import Percentage

c = Calc()

main_options = [
    "Equations", 
    "Units Converter",
    "Areas and Volumes",
    "Percentage", 
    "Quit"
]

while c.running:
    c.menu("Scientific Calculator", main_options)
    main_response = c.get_response(main_options)

    # equations
    if main_response == 0:
        fde = Equations()

        options = [
            "Calc",
            "Quit"
        ]

        while fde.running:
            fde.menu("Equations", options)
            response = fde.get_response(options)

            if response == 0:
                eq = str(input("Type your equation: "))

                fde.print_success("Result(s): ")
                fde.solve(eq)
                fde.await_action()

    # units converter
    elif main_response == 1:
        uc = UnitsConverter()

        options = [
            "cm and m",
            "ml and l",
            "Quit"
        ]

        while uc.running:
            uc.menu("Units Converter", options)
            response = uc.get_response(options)

    # areas and volumes
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

            # rectangle area
            if response == 0:
                x = float(input("(width) x: "))
                y = float(input("(height) y: "))

                aav.print_success("Result: " + str(aav.rectangle_area(x, y)))
                aav.await_action()

            # triangle area
            elif response == 1:
                b = float(input("(base) b: "))
                h = float(input("(height) h: "))

                aav.print_success("Result: " + str(aav.triangle_area(b, h)))
                aav.await_action()

            # hexagon area
            elif response == 2:
                x = float(input("(sides size) x: "))

                aav.print_success("Result: " + str(aav.hexagon_area(x)))
                aav.await_action()   

            # circle area
            elif response == 3:
                r = float(input("(radius) r: "))

                try:
                    pi = float(input("(blank to default) pi: "))
                    aav.print_success("Result: " + str(aav.circle_area(r, pi)))
                except:
                    aav.print_success("Result: " + str(aav.circle_area(r)))
                
                aav.await_action()

            # rectangular prism volume
            elif response == 4:
                l = float(input("(length) l: "))
                x = float(input("(width) x: "))
                y = float(input("(height) y: "))

                aav.print_success("Result: " + str(aav.rectangular_prism_volume(l, x, y)))
                aav.await_action()

            # pyramid volume
            elif response == 5:
                b = float(input("(base area) b: "))
                h = float(input("(height) h: "))

                aav.print_success("Result: " + str(aav.pyramid_volume(b, h)))
                aav.await_action()

            # sphere volume
            elif response == 6:
                r = float(input("(radius) r: "))

                try:
                    pi = float(input("(blank to default) pi: "))
                    aav.print_success("Result: " + str(aav.sphere_volume(r, pi)))
                except:
                    aav.print_success("Result: " + str(aav.sphere_volume(r)))
                
                aav.await_action()

    # percentage
    elif main_response == 3:
        pct = Percentage()

        options = [
            "% from x value",
            "Quit"
        ]

        while pct.running:
            pct.menu("Percentage", options)
            response = pct.get_response(options)
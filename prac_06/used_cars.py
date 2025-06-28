"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    new_car = Car("limo", 100)
    new_car.add_fuel(20)
    # print(f"Car has fuel: {new_car.fuel}")
    new_car.drive(115)
    # print(f"Car has fuel: {new_car.fuel}")
    print(new_car)


main()

import math

print("CS112: Computer Programming 1")
print("ACTIVITY: \"OBJECTS & CLASSES\" ")
print("Created by: Artjohn Clark E. Dinorog | CS 1E")
print()


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * radius ** 2
        self.parameter = 2 * math.pi * radius

    def getArea(self):
        print(f"The area of the circle with radius {self.radius} is {self.area:.2f}")

    def getParameter(self):
        print(f"The parameter of the circle with radius {self.radius} is {self.parameter:.2f}")


def get_user_radius(prompt):
    while True:
        user_radius = input(prompt)
        if user_radius.replace(".", "", 1).isdigit():  # Allowing float input
            return float(user_radius)
        else:
            print("> Please enter a valid number for the radius")


def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input in ['yes', 'no']:
            return user_input

        else:
            print("[Invalid input. Please enter 'yes' or 'no']\n")


while True:
    radius = get_user_radius("\nEnter a radius: ")
    circle = Circle(radius)
    circle.getArea()
    circle.getParameter()

    print()
    another = get_user_input("Do you want to try again? (yes/no): ")
    if another != 'yes':
        break
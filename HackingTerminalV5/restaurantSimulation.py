from commands import Command
from Loggingin import data
from text import *

styleToString = {
    1: "American",
    2: "Italian",
    3: "Japanese",
    4: "German",
    5: "Mediterranean",
    6: "Indian"
}


class Restaurant:
    def __init__(self, name: str, style: int):
        self.name = name
        self.style = styleToString[style]


class RestaurantSimulation(Command):
    def __init__(self, name: str, aliases: list, description: str):
        super().__init__(name, aliases, description)

    def Purpose(self):
        print(f"Starting {self.name}..")
        self.Setup()

    def Setup(self):
        print(f"Hello {data.LOGGEDINUSER.upper()}, welcome to {self.name}. Please answer all of these questions.")
        name = input(Indent("Restaurant name: ", 4))
        rstyle = 0

        while True:
            style = input(Indent("Choose a cuisine. Type 0 to see the options: ", 4))

            try:
                style = int(style)

                if style <= 0 or style > 6:
                    print()
                    print(Indent("Invalid cuisine.", 6))

                    print("Available Cuisines: \n"
                          "1: American, \n"
                          "2: Italian, \n"
                          "3: Japanese,\n"
                          "4: German,\n"
                          "5: Mediterranean,\n"
                          "6: Indian")
                    print()
                else:
                    rstyle = style
                    break

            except Exception as e:
                print()
                print("Invalid cuisine, type 0 to see available cuisines")


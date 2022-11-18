import text
from Loggingin import data
from commands import GenerateQuadratic, Command, ListAllUsers
from restaurantSimulation import RestaurantSimulation

COMMANDS = [Command("exit", ["shutdown"], f"Terminates {data.NAME}"),
            ListAllUsers("list", ["showall"], "Lists user info"),
            GenerateQuadratic("GenerateQuadratic", ["gqe"], "Generates a quadratic equation"),
            RestaurantSimulation("Restaurant-Simulator", ["playrs"], "Opens Restaurant-Simulator")]


def ListenForCommands():
    inp = input(f"[{data.NAME}-Command-Listener]: ")

    for command in COMMANDS:
        command.CheckForCommand(inp)

        if inp == "help":
            for command in COMMANDS:
                print(text.Indent(f"- {command.name.upper()}: {command.description}", 4))
            break
    print("")

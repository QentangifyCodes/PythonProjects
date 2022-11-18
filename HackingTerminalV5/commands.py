import random
import Loggingin.data as data
import text


class Command:
    def __init__(self, name: str, aliases: list, description: str):
        self.name = name
        self.aliases = aliases
        self.description = description

    def CheckForCommand(self, cmdName: str):
        if cmdName.lower() == self.name or cmdName.lower() in self.aliases:
            self.Purpose()


    def Purpose(self):
        print(f"Terminating {data.NAME}")
        quit()


class ListAllUsers(Command):
    def __init__(self, name: str, aliases: list, description: str):
        super().__init__(name, aliases, description)

    def Purpose(self):
        if not data.LOGGEDINUSER.lower() in data.ADMINS:
            print(f"You can not use this command")
            return

        for user in data.USERS:
            print(text.Indent(f"- Name: {user.upper()} Password: {data.USERS[user]}", 4))


class GenerateQuadratic(Command):
    def __init__(self, name: str, aliases: list, description: str):
        super().__init__(name, aliases, description)

    def Purpose(self):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

        d = a + b
        c = a * b

        print(text.Indent(f"Factor the following quadratic: x^2 + {d} x + {c}", 4))
        input(text.Indent("Press enter for the answer: ", 4))
        print(text.Indent(f"( x + {a} ) ( x + {b} )", 4))






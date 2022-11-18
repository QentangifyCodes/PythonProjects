import commandListener
from Loggingin import data

print(f"Hello, welcome to the {data.NAME}")
data.LoadUsers()
data.CheckForNewUser()
data.SaveUsers()
data.CheckForLogin()

running = True
while running:
    commandListener.ListenForCommands()

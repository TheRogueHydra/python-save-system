# Implementing a basic, JSON-based save system.
# Logins are saved as dictionaries in the logins.json file.

import json

with open("logins.json", "r") as logins:
    login_data = json.load(logins)

print("System booted.")
username = input("Enter username: ")
newUser = False

if len(login_data["logins"]) == 0:
    newUser = True

for i in login_data["logins"]:
    if username == i["username"]:
        accessPassword = i["password"]
        while True:
            password = input(f"Enter password for {username}: ")
            if password == accessPassword:
                print(f"Welcome back, {username}!")
                newUser = False
                break
            else:
                print("Incorrect password. Try again.")
        break
    else:
        newUser = True

if newUser:
    password = input(f"Enter a password for new user {username}: ")
    print(f"New user {username} with password {password}, welcome!")
    login_data["logins"].append({"username": username, "password": password})

    loginsNew = {
        "logins": login_data["logins"]
    }
    json_loginsNew = json.dumps(loginsNew, indent=4)

    with open("logins.json", "w") as logins:
        logins.write(json_loginsNew)
import json

if __name__ == "__main__":
    FILE_NAME = input("Enter the file name: ")
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    account = input("Enter website/account: ")
    user_details = {"name": name, "username": username, "password": password, "account": account}

    json_details = json.dumps(user_details, indent=4)

    with open(FILE_NAME, "w+") as f:
        f.write(json_details)



user = {}
status = ""

def displayMenu():
    status = input("Are you registered user? y/n press q to quit: ")
    if status == ("y"):
        oldUser()
    elif status == "n":
        newUser() 
def  newUser():
    creatLogin = input("creat login name: ")  

    if creatLogin in user:
        print("\nLogin name already exist!\n")
    else:
        creatPassw = input("Create password: ")
        user[creatLogin] = creatPassw
        print("\nUser created\n")
def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in user and user[login] == passw:
        print("\nLogin successful!\n ")
    else:
        print("\nUser doesn't exist or wrong password!\n")
while status != ("q"):
    displayMenu()

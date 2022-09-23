master_pwd = input("What is the Master Password? ")

#Fuctions to both options

def view():
    with open("Passwords.txt", 'r' ) as passwords: #with to auto close the file, Mode A = append
        for line in passwords.readlines():
            data = line.rstrip() #remove \n at the end of the saved file
            user, passw = data.split(" | ") # Sepearating the username and password list


def add():
    username = input("Enter Account Username: ")
    pwd = input ("Enter Account Password: ")

    with open("Passwords.txt", 'a' ) as passwords: #with to auto close the file, Mode A = append
            passwords.write(username + " | " + pwd + "\n")

#Selecting what mode the user is in
while True:
    pwdMode = input("Would you like to add a new password, Remove an existing password, or view saved passwords? (add/view/remove or Q to Quit): ").lower()

    if pwdMode == "q":
        break
    elif pwdMode == "view":    
        view()
    elif pwdMode == "add":
        add()
    elif pwdMode == "Remove":
        pass
    else:
        print("Invlid mode")
        continue
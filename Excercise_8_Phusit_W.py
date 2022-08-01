water = 10
bread = 20
banana = 8
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "user" and passwordInput == "1234":
    print("-------------------------------")
    print("----- Welcome to 7-12Shop -----")
    print("please select an option below")
    print("1. Water")
    print("2. Bread")
    print("3. Banana")
    select = int(input("Option :"))
    if select == 1:
        item = "Water"
        number = int(input("Enter number of item :"))
        total = water * number
    elif select == 2:
        item = "Bread"
        number = int(input("Enter number of item :"))
        total = bread * number
    elif select == 3:
        item = "Banana"
        number = int(input("Enter number of item :"))
        total = banana * number
    else:
        item = "Not found"
        number = 0
        total = 0
    print("-----------------------")
    print(item, "---------------", "x", number, "\ntotal =", total, "BTH")
elif usernameInput.upper() == "CUSTOMER" and passwordInput != 1234:
    print("Your password is incorrect.\n Please try again")
else:
    print("Your username is incorrect. \n Please try again")
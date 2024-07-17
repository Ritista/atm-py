print("===========ATM============")
pin = int(input("enter your pin: "))

if pin == 1234:
    print("Welcome to ATM")
    print("1. Check balance")
    print("2. Withdraw money")
    amount = 10000
    option = int(input("Enter your option: "))
    if option == 1:
        print("Your balance is: ", amount)
    elif option == 2:
        new_amount = int(input("Enter the amount to withdraw: "))
        if new_amount > amount:
            print("Insufficient balance")
        else:
            rem = amount - new_amount
            print("Withdraw amount is", new_amount)
            print("Remaining balance is", rem)
    else:
        print("Invalid option")
else:
    print("invalid pin")

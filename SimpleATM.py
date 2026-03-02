balance = 10000
print("Welcome To Kolade's ATM Machine")
while True:
    print("____Menu____")
    print("1. Check Balance: ")
    print("2. Deposit Money: ")
    print("3. Withdraw Money: ")
    print("4. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Your Balance is: ", balance)

    elif choice == "2":
          amount = float(input("Enter amount to deposit: "))
          if amount > 0:
             balance += amount
             print("Deposit Successful")
          else:
             print("Deposit Failed! Invalid amount")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance and amount > 0:
             balance -= amount
             print("Withdrawal Successful")
        else:
             print("Withdrawal Failed! Invalid amount")
    elif choice == "4":
        print("Thank you for using this ATM")
        break
    else:
        print("Invalid choice")



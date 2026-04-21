
try:
    file = open("Bank.txt" , "r")
    file.seek(0)
    print("Welcome to the Bank")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")

    choice = int(input("Enter the choice :"))
    Lines = file.readlines()


    def checkbalance(nam):
        for i in range(0 , len(Lines),3):
            user = Lines[i].strip()
            bal = Lines[i+1].strip()

            username = user.split(":")[1].strip()
            balance = bal.split(":")[1].strip()

            if(nam.lower() == username.lower()):
                print(username)
                print(balance)


    def Deposit(nam , amount):
        Found = False
        Updated_user =[]
        for i in range(0 ,len(Lines), 3):
            if Lines[i].strip() == "":
                continue
            user = Lines[i].strip()
            bal = Lines[i+1].strip()

            username = user.split(":")[1].strip()
            balance = bal.split(":")[1].strip()

            if(nam.lower() == username.lower()):
                Found = True
                balance = int(balance) + amount

            Updated_user.append(f" Name :{username} \n")
            Updated_user.append(f"Balance : {balance} \n")
            Updated_user.append("\n")
            
        if not Found:
                print("User not found")
                return
        with open("Bank.txt" , "w")as file:
                file.writelines(Updated_user)
                print("Deposit successful")
            
            

    def Withdrawal():
     try:
        amount = int(input("Enter the amount :"))
        customer = input("Enter the username :")
        Found = False
        Updated_user =[]
        for i in range(0, len(Lines),3):
            if Lines[i].strip() =="":
                continue
            user = Lines[i].strip()
            bal = Lines[i+1].strip()
            username = user.split(":")[1].strip()
            balance = bal.split(":")[1].strip()
            if(customer.lower() == username.lower()):
                    Found = True
                    if int(balance) < amount:
                        print("Insufficient balance")
                        return
                    balance = int(balance) - amount
            Updated_user.append(f" Name :{username} \n")
            Updated_user.append(f"Balance : {balance} \n")
            Updated_user.append("\n")

        if not Found:
                print("User not found")
                return
        with open("Bank.txt" , "w")as file:
                file.writelines(Updated_user)
                print("Withdrawal successful")
     except ValueError:
            print("Please enter a valid amount.")

    if choice == 1 :
        user =input("Enter the Name ")
        checkbalance(user)

    elif choice ==2 :
        user = input("Enter the username :")
        Amount = int(input("Enter the amount :"))
        Deposit(user ,Amount)
    elif choice ==3 :
        Withdrawal()

except Exception as e:
    print("An error occurred:", str(e))

finally:
  file.close()
  print("Thank you meet you again")



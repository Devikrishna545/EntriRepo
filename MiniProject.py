class Bankaccount:
    def __init__(self):
        self.balance = 1000
        print("Welcome to the ATM")

    def deposit(self):
        amount = float(input("Enter the amount to be deposited:"))
        self.balance += amount
        print("the deposited amount is:", amount)

    def withdrawl(self):
        amount = float(input("Enter the amount to withdraw:"))
        if self.balance >= amount:
            self.balance -= amount
            print("the amount withdrawn is :", amount)
        else:
            print("Insufficient balance.")

    def checkbalance(self):
        print("the balance amount is ", self.balance)


class Login(Bankaccount):
    def __init__(self):
        super().__init__()
        user = input("Enter your Username:")
        password = input("Enter your Password:")
        self.user = user
        self.password = password

    def loginuser(self):
        if self.user == "Devi" and self.password == "Devi123":
            print("You have successfully logged in")
            do = int(input("enter 1 to deposit \n 2 to withdraw \n 3 to check balance"))
            match do:
                case 1:
                    self.deposit()
                    self.checkbalance()
                case 2:
                    self.withdrawl()
                    self.checkbalance()
                case 3:
                    self.checkbalance()
                case _:
                    print("incorrect option")

        else:
            print("Incorrect username or password")

    def exit(self):
        print("You are successfully exited ,see you later")


a = int(input("press 1 to login"))
if a == 1:
    newuser = Login()
    newuser.loginuser()

else:
    print("Press the correct number to login")

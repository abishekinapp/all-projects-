class Account :

        def __init__(self):
            self.account_bal = int(1000)
            name = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}

        def deposit(self,dep_amount):
            self.account_bal += dep_amount

        def withdraw(self,draw_amount):
            if draw_amount <= self.account_bal:
                self.account_bal-= draw_amount
            else:
                print("insufficient balance")

        def veiw_bal(self):
            print("the account balance is ",self.account_bal)

option = int(input(
    "------------------------------------------------------\n"
    "|                        MENU                        |\n"
    "------------------------------------------------------\n"
    "| 1.Deposit money to a account                       |\n"
    "| 2.Withdraw money from a account                    |\n"
    "| 3.Transfer money from a account ot another account |\n"
    "| 4.Veiw balance of a account                        |\n"
    "------------------------------------------------------\n"))

name = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}

obj1 = Account()
obj2 = Account()
obj3 = Account()
obj4 = Account()

while option in [1,2,3,4]:
     flag = int(0)
     if option == 1:
        acc= int(input ("enter the account number :"))
        print("acoount holder name :" , name[acc])
        dep_amount= int(input("enter the amount to be deposited :"))
        if acc == int(1):
            obj1.deposit(dep_amount)
        elif acc == int(2):
            obj2.deposit(dep_amount)
        elif acc == int(3):
            obj3.deposit(dep_amount)
        elif acc == int(4):
            obj4.deposit(dep_amount)


     elif option == 2:
        acc= int(input ("enter the account number :"))
        print("account holder name :" , name[acc])
        draw_amount =int(input("enter the amount to be drawn :"))
        if acc == int(1):
            obj1.withdraw(draw_amount)
        elif acc == int(2):
            obj2.withdraw(draw_amount)
        elif acc == int(3):
            obj3.withdraw(draw_amount)
        elif acc == int(4):
            obj4.withdraw(draw_amount)

     elif option == 3:
        From_acc= int(input ("enter the account number from which ammout is to be transfered :"))
        To_acc=int(input ("enter the account number to which ammout is to be transfered :"))
        print("acoount name of the transferer:" , name[From_acc])
        print("acoount name of the reciever:", name[To_acc])
        trans_amount= int(input('enter the amount to be transfered :'))


        if From_acc == int(1):
            if obj1.account_bal<=trans_amount:
                flag=int(1)
            else:
                obj1.withdraw(trans_amount)
        elif From_acc == int(2):
            if obj2.account_bal <= trans_amount:flag=int(1)
            else:
                obj2.withdraw(trans_amount)
        elif From_acc == int(3):
            if obj3.account_bal <= trans_amount:flag=int(1)
            else:
                obj3.withdraw(trans_amount)
        elif From_acc == int(4):
            if obj4.account_bal <= trans_amount:flag=int(1)
            else:
                obj4.withdraw(trans_amount)

        while flag !=1:
            if To_acc == int(1):
                obj1.deposit(trans_amount)
            elif To_acc == int(2):
                obj2.deposit(trans_amount)
            elif To_acc == int(3):
                obj3.deposit(trans_amount)
            elif To_acc == int(4):
                obj4.deposit(trans_amount)
            break


     elif option == 4:
         acc = int(input("enter the account number :"))

         if acc == int(1):
             obj1.veiw_bal()
         elif acc == int(2):
             obj2.veiw_bal()
         elif acc == int(3):
             obj3.veiw_bal()
         elif acc == int(4):
             obj4.veiw_bal()

     option = int(input('\n\n'
    "------------------------------------------------------\n"
    "|                       MENU                         |\n"
    "------------------------------------------------------\n"
    "| 1.Deposit money to a account                       |\n"
    "| 2.Withdraw money from a account                    |\n"
    "| 3.Transfer money from a account ot another account |\n"
    "| 4.Veiw balance of a account                        |\n"
    "------------------------------------------------------\n"))

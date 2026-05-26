from os import name


class Student:
    def method1(self):
        print("method1")
    def method2(self):
        print("method2")

        obj=Student()
        obj.method1()
        obj1=Student()
        obj1.method1()

class collage:
        def __init__(self):
            print("constructor")
        def method1(self):
            print("method1")
        def method2(self):
            print("method2")
obj=collage()
obj1=collage()

class Student:
        def __init__(self,name,mark):
            self.name=name
            self.mark=mark
        def method1(self):
            print("method1")
        def method2(self):
            print("method2")

obj=Student("nivin",85)
obj1=Student("shijin",75)



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"


        


# Create an account for Alice with an initial balance of 1000
account = BankAccount("Alice", 1000)

# Deposit 500
account.deposit(500)
print("Balance after deposit:", account.balance)

# Withdraw 1200
result = account.withdraw(1200)
print("Withdraw result:", result)
print("Balance after withdrawal:", account.balance)

# Try to withdraw 500 again
result = account.withdraw(500)
print("Second withdraw result:", result)
print("Final balance:", account.balance)
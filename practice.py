# class Counter:
#     def __init__(self):
#         self.count = 0   #the data this object remembers

#     def increase(self):
#         self.count = self.count + 1   # add one to THIS object's count

#     def show(self):
#         print(self.count)   # print THIS object's count

# a = Counter()  # a is a Counter object
# b = Counter()  # b is a different Counter object

# a.increase()  # poke a
# a.increase()  # poke a again
# b.increase()  # poke b once

# a.show()  # prints 2
# b.show()  # prints 1

class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def show(self):
        print(self.balance)

john = BankAccount()
jack = BankAccount()

john.deposit(100)
jack.deposit(50)

john.show()  # prints 100
jack.show()  # prints 50
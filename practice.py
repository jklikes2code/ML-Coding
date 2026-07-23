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

# class BankAccount:
#     def __init__(self):
#         self.balance = 0
    
#     def deposit(self, amount):
#         self.balance += amount
    
#     def show(self):
#         print(self.balance)

# john = BankAccount()
# jack = BankAccount()

# john.deposit(100)
# jack.deposit(50)

# john.show()  # prints 100
# jack.show()  # prints 50

# scores = {"Sam": 90, "Alex": 85, "Jo": 78}
# print(scores)

# print(scores["Sam"])  # looks up Sam, prints 90
# print(scores["Jo"]) # looks up Jo, prints 78

# scores["Pat"] = 100  # adds a new key-value pair
# scores["Sam"] = 95  # updates Sam's score
# print(scores)

# print("Alex" in scores) #True because Alex is a key
# print("Riley" in scores) #False because Riley is not a key

# #checks whether Alex is a valid key in scores
# if "Alex" in scores:
#     print("Alex has a score of", scores["Alex"])
# else:
#     print("No score for Alex yet")

# for name in scores:
#     print(name) #prints all the keys, but not the values

# for name in scores:
#     print(name, "-->", scores[name]) #prints all keys and their respective values

# menu = {
#     "coffee": {"small": 2, "large": 3},
#     "tea": {"small": 1, "large": 2}
# }

# print(menu["coffee"]) # prints the entire inner dictionary
# print(menu["coffee"]["large"]) # reaches inside the inner dictionary

# menu["coffee"]["large"] = 4 # change the large coffee price to 4
# menu["tea"]["medium"] = 2 # add a brand new size for tea
# print(menu["coffee"]["large"]) # prints 4
# print(menu["tea"]) # prints the inner dictionary for tea, now including the new "medium" size

ages = {"Sam": 25, "Alex": 30, "Jo": 22}
print(ages["Sam"])  # prints 25
ages["Jose"] = 28  # adds a new key-value pair

# checks to see if "Jo" is a valid key
if "Jo" in ages:
    print("Jo's age is", ages["Jo"])
else:
    print("No age for Jo yet")

for name in ages:
    print(name, "is", ages[name], "years old")  # prints all keys and their respective values

classes = {
    "Math": {"teacher": "Mr. Smith", "room": 101},
    "Science": {"teacher": "Ms. Johnson", "room": 202},
    "Reading": {"teacher": "Mrs. Lee", "room": 303},
    "History": {"teacher": "Mr. Brown", "room": 404}    
}
print(classes["Math"]["teacher"])  # prints "Mr. Smith"

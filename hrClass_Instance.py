import sys

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")


class Person:
    def __init__(self, initialAge):         # init method with a constructor as parameter
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0                    # Instance Variable
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)                     # Instantiation->creation of an instance of a class
    p.amIOld()                          # Here, p is an instance-object
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")

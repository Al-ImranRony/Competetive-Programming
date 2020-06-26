import sys

# sys.stdout = open("output.txt", "w")
# sys.stdin = open("input.txt", "r")

class Person:
    def __init__(self, firstName, lastName, idNum):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
    def printInPerson(self):
        print("Name:", self.lastName + "," , self.firstName)
        print("ID:", self.idNum)

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        Person.__init__(self, firstName, lastName, idNum)
        self.scores = scores
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if avg >= 90:
            return 'O'
        elif avg >= 80:
            return 'E'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'P'
        elif avg >= 40:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNumber = line[2]
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNumber, scores)
s.printInPerson()
print("Grade:", s.calculate())
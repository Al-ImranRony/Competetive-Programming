import sys

sys.stdin  = open("input.txt", "r")
sys.stdout  = open("output.txt", "w")

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LLsolution():
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        current = head
        newNode = Node(data)
        if current is not None:
            while current.next is not None:
                current = current.next
            current.next = newNode
        else:
            head = newNode
        return head

mylist = LLsolution()
t = int(input())
head=None
for i in range(t):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head)

import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        cur = head
        newNode = Node(data)
        if cur is not None:
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode
        else:
            head = newNode
        return head

    def display(self, head):
        cur = head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

    def removeDuplicates(self, head):
        # data elements are in non-decreasing order
        cur = head
        while cur.next is not None:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


thelist = Solution()
t = int(input())
head = None
for i in range(t):
    data = int(input())
    head = thelist.insert(head, data)
head = thelist.removeDuplicates(head)
thelist.display(head)

'''
Linked List with two-pointer approach - LeetCode
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = ListNode()
        self.count = 0

    def insertItem(self, val):
        # TODO: Insert a new node & count
        new_node = ListNode(val)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.count += 1

    def display(self):
        # TODO: Shows the elements in the list
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.val)
            print(cur_node)                   # Showing the data address for each elements
        print(elems)

    def goToMiddle(self):
        run = self.head.next
        while run and run.next:
            self.head = self.head.next
            run = run.next.next

        self.display()


# Create a linked list
theList = LinkedList()

# Insert some items
theList.insertItem(1)
theList.insertItem(3)
theList.insertItem(7)
theList.insertItem(11)
theList.insertItem(33)
theList.display()

theList.goToMiddle()
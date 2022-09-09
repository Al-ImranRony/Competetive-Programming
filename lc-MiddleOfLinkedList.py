'''
Linked List with two-pointer approach - LeetCode
'''

class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList(object):
    def insertItem(self, val):
        # TODO: Insert a new node & count
        new_node = ListNode(val)
        cur_node = ListNode(0)
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        # count += 1

    def display(self, head):
        # TODO: Shows the elements in the list
        elems = []
        cur_node = head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.val)
            print(cur_node)                   # Showing the data address for each elements
        print(elems)

    def goToMiddle(self, head):
        mid = run = head

        while run and run.next:
            mid = mid.next
            run = run.next.next

        return mid


# Create a linked list
theList = LinkedList()
# theList.display(0)

# Insert some items
theList.insertItem(1)
theList.insertItem(3)
theList.insertItem(7)
theList.insertItem(11)
theList.insertItem(33)

theList.goToMiddle(ListNode(0))
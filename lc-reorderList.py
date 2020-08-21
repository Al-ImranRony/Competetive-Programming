# LeetCode Aug challenge 20

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self): 
        self.head = None

    def push(self, data): 
        new_node = ListNode(data) 
        new_node.next = self.head 
        self.head = new_node

    def reorderList(self) -> None:
        if not self.head: return 
        
        cur, ans = self.head, []
        while cur:
            ans.append(cur)            # Append all nodes value to ans array
            cur = cur.next             # Update current 

        mid = len(ans)//2
        for i in range(mid):
            ans[i].next = ans[-(i+1)]    # first to last node
            ans[-(i+1)].next = ans[i+1]  # last to second node
            
        ans[mid].next = None  

        temp = self.head           
        while temp:
            print(temp.val)
            temp = temp.next


# Driver program to test above functions 
llist = Solution()
llist.push(1) 
llist.push(2) 
llist.push(3) 
llist.push(4)

llist.reorderList()

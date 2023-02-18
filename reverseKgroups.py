# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
1 2 3 4  #2
initialize stack
loop till len stack == k while putting nodes in stack
recurse with next pointer, return head

if len stack == k, pop from stack make next pointer point to the top of the stack, if stack is empty make last node point to the next reference

1 2 3 4  #2
3 4
4-> 3

'''

def reverseList(node:ListNode):
    if not node.next: return (node,node) 
    next = node.next
    tail = reverseList(next)
    next.next = node
    node.next= None
    return (tail[0],node)

def reverseKGroup(head:ListNode, k:int):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
      
        if not head:return None
        counter = 0 
        curr = head
        tail = None
        while curr and counter!=k:
            tail = curr
            curr=curr.next
            counter+=1
        if counter!=k: return head
        next = reverseKGroup(curr,k)
        tail.next = None
        head,lastNode = reverseList(head)
        lastNode.next = next
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = reverseKGroup(node1,3)
while head:
    print(head.val)
    head=head.next


        
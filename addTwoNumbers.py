class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

'''
342 + 465 = 807

2 4 3
5 6 4

carry = 1
9 9 9 9 9 9 9
9 9 9 9
8 9 9 9 0 0 0 1

'''

def addTwoNumbers(l1,l2):
    dummyHead = ListNode(None)
    curr = dummyHead
    carry = 0
    while l1 or l2:
        if l1 and l2:
            res = l1.val + l2.val + carry
            carry = 0
            if res>=10: res, carry = res-10, 1
            curr.next = ListNode(res)
            curr = curr.next
            l1,l2 = l1.next,l2.next
        elif l1:
            res = l1.val + carry
            if res>=10: res, carry = res-10, 1
            curr.next = ListNode(res)
            curr = curr.next
            l1= l1.next
        elif l2:
            res = l2.val + carry
            if res>=10: res, carry = res-10, 1
            curr.next = ListNode(res)
            curr = curr.next
            l2= l2.next
    if carry: curr.next = ListNode(carry)
    return dummyHead.next

node = addTwoNumbers(node1,node4)
while node:
    print(node.val, end=' ')
    node = node.next
        



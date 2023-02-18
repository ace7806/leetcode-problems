class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node1.next = node2
node2.next = node3
node4 = ListNode(1)
node5 = ListNode(1)
node6 = ListNode(1)
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
    outputStack = []
    def top():
        return outputStack[-1] if outputStack else None
    carry = 0
    stack1 = []
    stack2= []
    while l1:
        stack1.append(l1)
        l1 = l1.next
    while l2:
        stack2.append(l2)
        l2 = l2.next
    while stack1 or stack2:
        if stack1 and stack2:
            res = stack1.pop().val + stack2.pop().val + carry
        elif stack1:
            res = stack1.pop().val + carry
        elif stack2:
            res = stack2.pop().val + carry
        carry = 0
        if res>=10: res, carry = res-10, 1
        outputStack.append(ListNode(res,top()))
    if carry: outputStack.append(ListNode(carry,top()))
    return top()

node = addTwoNumbers(node1,node4)
while node:
    print(node.val, end=' ')
    node = node.next
        



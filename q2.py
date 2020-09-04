#Original question: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
	# store the tens digits of the result
        tens = 0
	# declare the linked list for result
        result = ListNode()
	# declare a variable that points to the head of the result linked list
        head = result
        
	# since the input linked list are not empty, store the 1st bit of result
        result.val = (l1.val + l2.val) % 10
        tens = (int)((l1.val + l2.val)/10)
        l1 = l1.next
        l2 = l2.next
        
	# traverse the linked list untill both lists are empty
        while l1 is not None or l2 is not None:
            if (l1 == None and l2 != None):
                nextNode = ListNode()
                nextNode.val = (l2.val + tens)%10
                tens = (int)((l2.val + tens)/10)
                l2 = l2.next
                result.next = nextNode
                result = result.next
            elif (l2 == None and l1 != None):
                nextNode = ListNode()
                nextNode.val = (l1.val + tens)%10
                tens = (int)((l1.val + tens)/10)
                l1 = l1.next
                result.next = nextNode
                result = result.next
            else:
                nextNode = ListNode()
                nextNode.val = (l1.val + l2.val + tens) % 10
                tens = (int)((l1.val + l2.val + tens)/10)
                result.next = nextNode
                result = result.next
                l1 = l1.next
                l2 = l2.next
        if (tens != 0):
            nextNode = ListNode()
            nextNode.val = tens
            result.next = nextNode
        return head
                
        

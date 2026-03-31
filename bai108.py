# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val  # Store the value of the node
#         self.next = next  # Pointer to the next node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to simplify result list construction
        dummy = ListNode(0)
        temp = dummy  # Pointer to traverse the result list
        carry = 0  # Variable to store carry from addition

        # Loop until both linked lists are fully processed
        while l1 or l2:
            value = carry  # Start with carry from the previous sum

            # Add value from l1 if it exists
            value += l1.val if l1 else 0

            # Add value from l2 if it exists
            value += l2.val if l2 else 0

            # If sum is greater than 9, store last digit and set carry to 1
            if value > 9:
                carry = 1
                temp.next = ListNode(value % 10)  # Store only the last digit
            else:
                temp.next = ListNode(value)  # Store the sum directly
                carry = 0  # Reset carry

            temp = temp.next  # Move to the next node in the result list

            # Move to the next nodes in l1 and l2 if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # If there's any remaining carry, add a new node
        temp.next = ListNode(carry) if carry else None

        return dummy.next  # Return the result list (excluding dummy node)
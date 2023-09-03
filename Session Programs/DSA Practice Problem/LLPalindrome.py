# Implement a Python function to determine if a singly linked list is a palindrome. 
# You can't use additional data structures; solve it in O(n) time and O(1) space.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    second_half = reverse_linked_list(slow.next)
    slow.next = None  # Cut off the first half from the second half

    # Step 3: Compare the first half with the reversed second half
    return is_equal(head, second_half)

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def is_equal(head1, head2):
    while head1 and head2:
        if head1.value != head2.value:
            return False
        head1 = head1.next
        head2 = head2.next
    return True

# Example usage:
# Create a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print(is_palindrome(head))  # Output: True

# Create a non-palindrome linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(is_palindrome(head))  # Output: False
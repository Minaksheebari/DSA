# Write a Python function that finds the intersection point of two singly linked lists. 
# If the lists do not intersect, return None. Optimize for time and space complexity.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def get_intersection_node(headA, headB):
    lenA, lenB = 0, 0
    nodeA, nodeB = headA, headB

    # Find the lengths of both linked lists
    while nodeA:
        lenA += 1
        nodeA = nodeA.next

    while nodeB:
        lenB += 1
        nodeB = nodeB.next

    # Reset the pointers to the beginning of the lists
    nodeA, nodeB = headA, headB

    # Move the pointer of the longer list forward by the difference in lengths
    if lenA > lenB:
        for _ in range(lenA - lenB):
            nodeA = nodeA.next
    elif lenB > lenA:
        for _ in range(lenB - lenA):
            nodeB = nodeB.next

    # Traverse both lists simultaneously until the intersection point is found
    while nodeA and nodeB:
        if nodeA == nodeB:
            return nodeA
        nodeA = nodeA.next
        nodeB = nodeB.next

    # If no intersection point is found, return None
    return None

# Example usage:
# Create two intersecting linked lists: 1 -> 2 -> 3 -> 4 and 7 -> 8
common_node = ListNode(7, ListNode(8))
listA = ListNode(1, ListNode(2, ListNode(3, ListNode(4, common_node))))
listB = ListNode(7, ListNode(8, common_node))

intersection_node = get_intersection_node(listA, listB)
if intersection_node:
    print("Intersection point value:", intersection_node.value)
else:
    print("No intersection")

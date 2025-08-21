# Step 1: Define a Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Step 2: Build Linked List [2,4,6,8,10,12]
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)

# (Optional) Create a cycle for testing
# head.next.next.next.next.next.next = head.next  # make 12 → 4

# Step 3: Function to detect cycle
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next       # 1 step
        fast = fast.next.next  # 2 steps
        if slow == fast:
            return True  # they met, loop exists

    return False

# Test
print(has_cycle(head))  # Output: False (no cycle)

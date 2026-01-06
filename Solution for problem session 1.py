'''Given a linked list containing the names of the 2n kids, 
in order of the original line formed in front of Jen’s truck 
(where the first node contains the name of the first kid in line), 
describe an O(n)-time algorithm to modify the linked list to reverse 
the order of the last half of the list. Your algorithm should not 
make any new linked list nodes or instantiate any new 
non-constant-sized data structures during its operation.'''

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self, names):
        if not names:
            self.head = None
            return
        self.head = Node(names[0])
        curr = self.head
        for name in names[1:]:
            curr.next = Node(name)
            curr = curr.next

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.name)
            curr = curr.next
        return result

def reorder_students(L):
    # Step 0: Calculate n (2n total students)
    total_count = 0
    curr = L.head
    while curr:
        total_count += 1
        curr = curr.next
    n = total_count // 2 #

    if n == 0: return L

    # STAGE 1: Find the nth node 'a' and (n+1)st node 'b'
    # Finding the nth node requires traversing next pointers n-1 times
    a = L.head
    for _ in range(n - 1): #
        a = a.next
    
    b = a.next #
    # 'c' will eventually be the 2nth node

    # STAGE 2: Reverse the arrows (The core logic you're intuiting)
    # We maintain pointers to current node x and node before it xp
    x_p = a  # Start by pointing b back to a
    x = b
    
    # Repeat n times to relink all n nodes in the last half
    for _ in range(n):
        x_n = x.next   # Record node xn after x so we don't lose the chain
        x.next = x_p   # Relink x to point to the node before it xp in O(1)
        
        # Move pointers forward: maintaining properties for the next node
        x_p = x        
        x = x_n        
    
    # At the end of the loop, xp is node 'c' (the original last node)
    c = x_p

    # STAGE 3: Final relinking
    # Change next pointer of a and b to point to c and nothing respectively
    a.next = c
    b.next = None

    return L

# --- Testing the logic ---
students = ["Student 1", "Student 2", "Student 3", "Student 4"] # 2n = 4, so n = 2
ll = LinkedList(students)

print(f"Original Line: {ll.to_list()}")
reorder_students(ll)
print(f"Reordered Line: {ll.to_list()}")
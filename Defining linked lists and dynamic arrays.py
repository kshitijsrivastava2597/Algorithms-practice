class Linked_List_Node:
    
    def __init__(self, x): # O(1)
        self.item = x
        self.next = None

    def later_node(self, i): # O(i)
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)
    
class Linked_List_Seq:

    def __init__(self): # O(1)
        self.head = None
        self.size = 0

    def __len__(self): return self.size # O(1)

    def __iter__(self): # O(n) iter_seq
        node = self.head
        while node:
            yield node.item # yield creates a generator function that pauses execution and returns a value to the caller while maintaining its state, allowing it to resume later from where it left off
            node = node.next 

    def build(self, X): # O(n)
        for a in reversed(X):
            self.insert_first(a)

    def get_at(self, i): # O(i)
        node = self.head.later_node(i)
        return node.item
    
    def set_at(self, i, x): # O(i)
        node = self.head.later_node(i)
        node.item = x
    
    def insert_first(self, x): # O(1)
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self): # O(1)
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x
    
    def insert_at(self, i, x): # O(i)
        if i == 0:
            self.insert_first(x)
            return
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1
    def delete_at(self, i): # O(i)
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x # O(n)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): return self.delete_at(len(self) - 1)

class Dynamic_Array_Seq(Array_Seq):

    def __init__(self, r = 2): # O(1)
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self): return self.size # O(1)

    def __iter__(self): # O(n)
        for i in range(len(self)): yield self.A[i]

    def build(self, X): # O(n)
        for a in X: self.insert_last(a)

    def _compute_bounds(self): # O(1)
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _resize(self, n): # O(1) or O(n)
        if (self.lower < n < self.upper): return
        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()
    
    def insert_last(self, x): # O(1)a
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1
        
    def delete_last(self): # O(1)a
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)
        
    def insert_at(self, i, x): # O(n)
        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.A, i + 1)
        self.A[i] = x
        
    def delete_at(self, i): # O(n)
        x = self.A[i]
        self._copy_forward(i + 1, self.size - (i + 1), self.A, i)
        self.delete_last()
        return x

def insert_first(self, x): self.insert_at(0, x) # O(n)

def delete_first(self): return self.delete_at(0)




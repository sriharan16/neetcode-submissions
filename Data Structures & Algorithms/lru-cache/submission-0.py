class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.l = Node(0,0)
        self.r = Node(0,0)

        self.l.next = self.r
        self.r.prev = self.l

    
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def insert(self, node):
        prv, nxt = self.r.prev, self.r

        node.prev = prv
        node.next = nxt

        prv.next = nxt.prev = node

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            del self.cache[self.l.next.key]
            self.remove(self.l.next)
        

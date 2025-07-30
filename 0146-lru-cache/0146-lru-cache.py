class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size =0 
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
    def put(self, key: int, value: int) -> None:

        # check if key is already inside
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return 
        else:
            if self.size == self.capacity:
                last_node = self.tail.prev
                self.remove(last_node)
                del self.cache[last_node.key]
                self.size-=1
            
            node = Node(key,value)
            self.add(node)
            self.size+=1
            self.cache[key] = node
            return

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
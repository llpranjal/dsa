class Node:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        #set it up as a dummy nodes for each entry
        self.map = [Node() for _ in range(1000)]
    
    def hash(self, key):
        return key % 1000

    def put(self, key: int, value: int) -> None:
        #dummy node cur
        cur = self.map[self.hash(key)]

        #update value otherwise append
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next

        cur.next = Node(key, value, None)


    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
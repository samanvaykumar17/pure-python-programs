"""
Linked List implementation in python
"""

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_at_end(self, data):
        node = Node(data)
        if not self.head:
            print("list empty, adding first node")
            self.head = node
        else:
            if not self.head.next:
                print("list has just one node, adding second node")
                self.head.next = node
            else:
                print("list has multiple nodes, adding new node")
                pointer = self.head
                while pointer.next:
                    #print("pointer --> ", pointer.data, pointer.next)
                    pointer = pointer.next
                pointer.next = node

    def display(self):
        print("------displaying------")
        ptr = self.head
        print(ptr.data)
        while ptr.next:
            ptr = ptr.next
            print(ptr.data)

 
if __name__ == "__main__":
    l = LinkedList()
    l.add_node_at_end(10)
    l.add_node_at_end(20)
    l.add_node_at_end(30)
    l.add_node_at_end(40)
    l.add_node_at_end(50)
    l.add_node_at_end(60)
    l.display()

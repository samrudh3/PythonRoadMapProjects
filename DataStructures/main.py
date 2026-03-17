class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(2)
n2 = Node(3)
n3 = Node(4)

n1.next = n2
n2.next = n3

current = n1

while current:
    print(current.data)
    current = current.next
    
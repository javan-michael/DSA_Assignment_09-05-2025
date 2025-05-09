# Node class for doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link nodes both ways
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# Print the list
current = node1
while current:
    print(current.data, end=" <-> ")
    current = current.next
print("None")

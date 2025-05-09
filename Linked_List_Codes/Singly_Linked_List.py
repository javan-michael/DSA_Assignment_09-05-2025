# Node class creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Linking of nodes together
node1.next = node2
node2.next = node3

# Print the linked list
current = node1
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
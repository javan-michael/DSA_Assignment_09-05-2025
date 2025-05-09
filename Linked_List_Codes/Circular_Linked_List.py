# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create three nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Connect nodes in a circle
node1.next = node2      # 1 points to 2
node2.next = node3      # 2 points to 3
node3.next = node1      # 3 points back to 1 (making it circular)

# Print the circular list (make one complete loop)
current = node1
count = 0
while count < 6:        # Print 6 elements to show the circular nature
    print(current.data, end=" -> ")
    current = current.next
    count += 1
print("...")            # Shows that the list continues
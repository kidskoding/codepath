class Node:
    # Each LinkedList's Node contains
    # 1. a value containing the data that is held in the node (`value`)
    # 2. a reference to the next node in a LinkedList (`next`). at the beginning, this is None because we won't have any
    # other node to chain onto
    def __init__(self, value):
        self.value = value
        self.next = None

# 3 individual nodes
student1 = Node('Alice')
student2 = Node('Bob')
student3 = Node('Carol')

# Using .next will allow the chaining functionality that is present in a LinkedList because that is how nodes will get
# a reference to another
# 
# The example below results in a LinkedList of
# Alice -> Bob -> Carol
student1.next = student2
student2.next = student3

# ------------------------------------------------------------------------------------ #

# Looping through a LinkedList

# 1. Create a variable, current, that marks the beginning of the LinkedList (in this example, student1)
# 2. When looping through a LinkedList, move the current node until there are no more elements remaining. We no that there
# won't be anymore elements that remain when we don't have a current node (it is equal to None)
# 3. Move forward in the LinkedList by migrating current to the next node in the LinkedList (current.next) -> current = current.next
current = student1
while current:
    print(current.value)
    current = current.next

# ------------------------------------------------------------------------------------ #

# LinkedLists

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_line(self):
        current = self.head
        while current:
            print(current.value, end=' ->')
            current = current.next
        print('None')

roster = LinkedList()
roster.add('Alice')
roster.add('Bob')
roster.add('Carol')
# roster.print_line()

roster2 = LinkedList()
roster2.print_line()

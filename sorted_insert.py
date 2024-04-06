class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    new_node = Node(data)
    current = head
    while current.next and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head
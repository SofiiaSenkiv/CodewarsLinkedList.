class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    # your code goes here.
    reversed_list_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return reversed_list_head

class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
def linked_list_from_string(s):
    head = None
    for i in s.split('->')[-2::-1]:
        head = Node(int(i),head)
    return head
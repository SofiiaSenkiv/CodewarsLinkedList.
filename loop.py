def loop_size(node):
    visited = set()
    current = node
    count = 0
    while current not in visited:
        visited.add(current)
        current = current.next
        count += 1
    repeat_point = current
    current = current.next
    loop_length = 1
    while current != repeat_point:
        current = current.next
        loop_length += 1
    return loop_length
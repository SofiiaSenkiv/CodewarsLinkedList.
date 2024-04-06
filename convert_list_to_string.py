def stringify(lst):
    result = ""
    current = lst
    while current:
        result += str(current.data) + " -> "
        current = current.next
    result += "None"
    return result
def read_input(filename):
    f = open(filename, 'r')
    n = int(f.readline().strip())
    data = f.readline().strip().split()
    f.close()
    return n, to_linked_list(data)

def write_output(filename, head):
    f = open(filename, 'w')
    curr = head
    while curr is not None:
        f.write(curr[0] + ' ')
        curr = curr[1]
    f.close()

def to_linked_list(values):
    if len(values) == 0:
        return None
    head = [values[0], None]
    current = head
    i = 1
    while i < len(values):
        node = [values[i], None]
        current[1] = node
        current = node
        i = i + 1
    return head

def get_length(head):
    count = 0
    current = head
    while current is not None:
        count = count + 1
        current = current[1]
    return count

def get_node_at(head, index):
    current = head
    i = 0
    while i < index and current is not None:
        current = current[1]
        i = i + 1
    return current

def swap_nodes_values(node1, node2):
    temp = node1[0]
    node1[0] = node2[0]
    node2[0] = temp

def swap_first_last_n(head, n):
    length = get_length(head)
    if n <= 0 or n * 2 > length:
        return head

    i = 0
    while i < n:
        node_start = get_node_at(head, i)
        node_end = get_node_at(head, length - n + i)
        swap_nodes_values(node_start, node_end)
        i = i + 1
    return head

def main():
    n, head = read_input('input.txt')
    head = swap_first_last_n(head, n)
    write_output('output.txt', head)

main()
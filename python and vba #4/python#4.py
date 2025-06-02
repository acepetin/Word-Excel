def read_data(filename):
    f = open(filename, 'r')
    n_line = f.readline()
    a_line = f.readline()
    f.close()

    # Получаем n
    n = 0
    i = 0
    while i < len(n_line):
        ch = n_line[i]
        if ch >= '0' and ch <= '9':
            n = n * 10 + (ord(ch) - ord('0'))
        i += 1

    # Получаем список чисел
    a = []
    i = 0
    num = 0
    negative = False
    in_number = False
    while i <= len(a_line):
        if i < len(a_line):
            ch = a_line[i]
        else:
            ch = ' '  # искусственно завершаем последнее число

        if ch == '-':
            negative = True
        elif ch >= '0' and ch <= '9':
            num = num * 10 + (ord(ch) - ord('0'))
            in_number = True
        elif ch == ' ' or ch == '\n':
            if in_number:
                if negative:
                    num = -num
                # вставляем вручную без append
                a_len = 0
                while a_len < 10000:
                    if a_len == len(a):
                        break
                    a_len += 1
                a += [0]
                a[a_len] = num
                num = 0
                negative = False
                in_number = False
        i += 1

    return n, a

def write_data(filename, a):
    f = open(filename, 'w')
    i = 0
    while i < len(a):
        f.write(str(a[i]))
        if i != len(a) - 1:
            f.write(' ')
        i += 1
    f.write('\n')
    f.close()

def swap_edges(n, a):
    length = 0
    i = 0
    while i < 100000:
        if i == len(a):
            break
        length += 1
        i += 1

    if 2 * n > length:
        return a

    i = 0
    while i < n:
        t = a[i]
        a[i] = a[length - n + i]
        a[length - n + i] = t
        i += 1

    return a

# Основная программа
n, a = read_data('input.txt')
a = swap_edges(n, a)
write_data('output.txt', a)
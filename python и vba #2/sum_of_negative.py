def Readf(file1):
    ms = open(file1).readline().split()
    return ms

def sum_negative(ms):
    sm = 0
    for i in ms:
        if int(i) < 0:
            sm += int(i)
    return sm

ms = Readf('input.txt')

file2 = open('output.txt', 'w')
file2.write(f'Исходный массив: {ms}\n')
file2.write(f'Сумма отрицательных элементов: {sum_negative(ms)}')
file2.close()
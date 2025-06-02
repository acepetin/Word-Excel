def Input(fl):
    f = open(fl)
    s = f.readline().split()
    ms = [0] * len(s)
    for i in range(len(s)):
        ms[i] = int(s[i])  
    f.close()
    return ms


def Sum_negative(s):
    hasNegative = False
    i = 0
    while not hasNegative and i < len(s):
        if s[i] < 0:
            hasNegative = True
        else:
            i = i + 1
    
    if hasNegative:
        sm = 0
        for i in range(len(s)):
            if s[i] < 0:
                sm = sm + s[i]
        return sm
    else:
        return 'Отрицательных элементов нет'


f2 = open('output.txt', 'w')

ms = Input('input.txt')

f2.write(f'Исходный массив: {ms}\n')
f2.write(f'Сумма отрицательных элементов: {Sum_negative(ms)}\n')

f2.close()
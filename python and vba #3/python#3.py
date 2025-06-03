def Input(fl):
    f = open(fl)
    num = int(f.readline().strip())
    
    matrix = []
    for line in f:
        s = line.strip().split()
        row = [int(x) for x in s]
        matrix.append(row)
    f.close()
    return num, matrix

def HasElementsAbove(matrix, num):
    for row in matrix:
        for value in row:
            if value > num:
                return True
    return False

def ProcessMatrix(matrix, num):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > num:
                matrix[i][j] = matrix[i][j] / num

def WriteResult(fname, original, processed, has_changes):
    f = open(fname, 'w')
    
    f.write("Исходная матрица:\n")
    for row in original:
        f.write(' '.join(str(x) for x in row) + '\n')
    
    if has_changes:
        f.write("\nРезультат обработки:\n")
        for row in processed:
            f.write(' '.join(str(x) for x in row) + '\n')
    else:
        f.write("\nНет элементов больше заданного числа\n")
    
    f.close()

# Основной код
input_file = 'input.txt'
output_file = 'output.txt'

num, matrix = Input(input_file)
original_matrix = [row[:] for row in matrix]
has_elements = HasElementsAbove(matrix, num)

if has_elements:
    ProcessMatrix(matrix, num)

WriteResult(output_file, original_matrix, matrix, has_elements)
def Input(fl):
    f = open(fl)
    num = int(f.readline().strip())
    
    matrix = []
    for line in f:
        s = line.strip().split()
        row = [0] * len(s)
        for i in range(len(s)):
            row[i] = int(s[i])
        matrix += [row]
    f.close()
    return num, matrix

def HasElementsAbove(matrix, num):

    rows = len(matrix)
    cols = len(matrix[0])
    
    i = 0
    found = False
    while not found and i < rows:
        j = 0
        while not found and j < cols:
            if matrix[i][j] > num:
                found = True
            j += 1
        i += 1
    return found

def ProcessMatrix(matrix, num):
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    result = [[0]*cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] > num:
                result[i][j] = matrix[i][j] / num
            else:
                result[i][j] = matrix[i][j]
    return result

def WriteResult(fname, orig_matrix, proc_matrix, has_changes):
   
    f = open(fname, 'w')
    
    f.write("Исходная матрица:\n")
    for row in orig_matrix:
        f.write(' '.join(str(x) for x in row) + '\n')
    
    if has_changes:
        f.write("\nРезультат обработки:\n")
        for row in proc_matrix:
            f.write(' '.join(str(x) for x in row) + '\n')
    else:
        f.write("\nНет элементов больше заданного числа\n")
    
    f.close()


input_file = 'input.txt'
output_file = 'output.txt'

num, matrix = Input(input_file)
has_elements = HasElementsAbove(matrix, num)
processed_matrix = ProcessMatrix(matrix, num) if has_elements else matrix

WriteResult(output_file, matrix, processed_matrix, has_elements)

from copy import deepcopy

def Print(matrix):

    row = len(matrix)
    col = len(matrix[0])
    result=[]

    for i in range(row):
        print("\n")
        for j in range(col):
            if (j == len(matrix[0])-1) :
                result.append(matrix[i][j])
            print(matrix[i][j], "|", end=" ")

    print("\n\n",result)

def create_matrix(equation, result):

    Copy = deepcopy(equation)

    for i in range(len(Copy)):
        Copy[i].append(result[i])

    return Copy

def gauss_jordan_elimination(equations, results):

    matrix = create_matrix(equations, results)

    for k in range(len(matrix)):
        for j in range(len(matrix)-1, k, -1):
            temp = matrix[j][k]
            for i in range(len(matrix[0])):
                matrix[j][i] = -temp / matrix[k][k] * matrix[k][i] + matrix[j][i]

    for k in range(len(matrix)-1, 0, -1):
        for j in range(k):
            temp = matrix[j][k]
            for i in range(len(matrix[0])):
                matrix[j][i] = -temp / matrix[k][k] * matrix[k][i] + matrix[j][i]

    for j in range(len(matrix)):
        temp = matrix[j][j]
        for i in range(len(matrix[0])):
            matrix[j][i] = matrix[j][i] / temp

    return matrix

#matrix_2 = [[1, 2, 1, 8], [2, -1, 1, 3], [3, 3, -2, 3]]
#matrix = [[1, 1, 2, 4], [2, -1, -1, 2], [1, 2, 3, 6]]

equation = [[1, 1, -1, 1], [0, 2, 1, -1], [1, 0, -1, 1], [-1, -1, 1, 0]]
equation_result = [2, 5, 0, -4]

Print(gauss_jordan_elimination(equation, equation_result))
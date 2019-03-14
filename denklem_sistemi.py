def yazdir (matrix, row, col):
    for i in range(row):
        print("\n")
        for j in range(col):
            print(matrix[i][j], "|", end=" ")

def gauss_jordan_eleminasyon(matrix):

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

matrix_2 = [[1, 2, 1, 8], [2, -1, 1, 3], [3, 3, -2, 3]]
matrix = [[1, 1, 2, 4], [2, -1, -1, 2], [1, 2, 3, 6]]
matrix_3 = [[1, 1, -1, 1, 2], [0, 2, 1, -1, 5], [1, 0, -1, 1, 0], [-1, -1, 1, 0, -4]]

yazdir(gauss_jordan_eleminasyon(matrix_3), 4, 5)
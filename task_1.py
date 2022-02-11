class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        str1 = ''
        for i in range(len(self.matrix_list)):
            for k in self.matrix_list[i]:
                str1 += f'{k:<3d} '
            str1 += '\n'
        return str1

    def __add__(self, other):
        if len(self.matrix_list) == len(other.matrix_list) and len(self.matrix_list[0]) == len(other.matrix_list[0]):
            result_list = []
            for i in range(len(self.matrix_list)):
                result_list.append([])
                for k in range(len(self.matrix_list[i])):
                    result_list[i].append(self.matrix_list[i][k] + other.matrix_list[i][k])
            return Matrix(result_list)
        else:
            return ('Матрицы разного размера')


matrix_3x2_1 = [[1, 2], [3, 4], [5, 6]]
matrix_3x2_2 = [[7, 8], [9, 10], [11, 12]]
matrix_4x4_3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix_4x4_4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matr_1 = Matrix(matrix_3x2_1)
matr_2 = Matrix(matrix_3x2_2)
matr_3 = Matrix(matrix_4x4_3)
matr_4 = Matrix(matrix_4x4_4)
print('1-я матрица:')
print(matr_1)
print('2-я матрица:')
print(matr_2)
print('3-я матрица:')
print(matr_3)
print('4-я матрица:')
print(matr_4)
print(matr_1 + matr_2)
print(matr_3 + matr_4)
print(matr_3 + matr_1)

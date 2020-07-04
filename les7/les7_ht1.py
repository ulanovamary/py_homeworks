class Matrix:
    def __init__(self, matrix_list):
        self._matrix_list = matrix_list


    def __str__(self):
        return str('\n'.join('\t'.join([str(j) for j in i]) for i in self._matrix_list))


    def matr_print (self, i, j):
       print(self._matrix_list[i][j])


    def __add__(self, other):
        matr = Matrix(
            [
                ([self._matrix_list[i][j] + other._matrix_list[i][j] for j in range(len(self._matrix_list[0]))])
                for i in range(len(other._matrix_list))
            ]
        )
        return matr

a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])

print(a.__add__(b))


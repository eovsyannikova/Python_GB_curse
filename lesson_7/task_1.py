

class Matrix:

    def __init__(self, matrix):
        self.matrix_list = matrix

    def __add__(self, other):
        return Matrix([[x + y for x, y in zip(i, j)] for i, j in zip(self.matrix_list, other.matrix_list)])

    def __str__(self):
        return '\n'.join(map(str, self.matrix_list))


my_list_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
my_list_2 = [[13, 15, 132], [12, 14, 16], [-11, 164, -18]]

a = Matrix(my_list_1)
b = Matrix(my_list_2)


print(a + b)




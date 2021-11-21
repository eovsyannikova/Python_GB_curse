class Complex:
    def __init__(self, i_number):
        self.i_number = i_number

    def __add__(self, other):
        return Complex(self.i_number + other.i_number)

    def __mul__(self, other):

        return Complex(self.i_number * other.i_number)

    def __str__(self):
        return f"{self.i_number}"


c_1 = Complex(2 + 3j)
c_2 = Complex(-1 + 1j)
print(f'Результат сложения комлпексных чисел: {c_1 + c_2}')
print(f'Результат сложения комлпексных чисел: {c_1 * c_2}')



# Немного другой вариант
# import re
#
#
# class Complex:
#     def __init__(self, i_number):
#         self.i_number = i_number.replace(' ', '')
#         self.index = self.i_number.find('i')
#         self.nums = (re.findall(r'-?\d+', self.i_number))
#         self.nums = [int(i) for i in self.nums]
#
#     def __add__(self, other):
#         a = self.nums[0]+other.nums[0]
#         b = self.nums[1]+other.nums[1]
#         z = (str(a) + str(b)+'i') if b < 0 else (str(a) + "+" + str(b)+'i')
#         return Complex(z)
#
#     def __mul__(self, other):
#         a = self.nums[0]
#         b = self.nums[1]
#         c = other.nums[0]
#         d = other.nums[1]
#         z = str(a * c - b * d) + str(a * d + c * b) + 'i'
#         return Complex(z)
#
#     def __str__(self):
#         return f"{self.i_number}"
#
#

# c_1 = Complex('2+ 3i')
# c_2 = Complex('-1+1i')
# print(f'Результат сложения комлпексных чисел: {c_1 + c_2}')
# print(f'Результат сложения комлпексных чисел: {c_1 * c_2}')





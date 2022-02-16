class Complex:

    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        return Complex(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        return Complex(self.real_part * other.real_part - self.imaginary_part * other.imaginary_part,
                       self.real_part * other.imaginary_part + other.real_part * self.imaginary_part)


compl1 = Complex(5, 2)
compl2 = Complex(3, 7)
print((5 + 2j) + (3 + 7j))
print(f'{(compl1 + compl2).real_part} + {(compl1 + compl2).imaginary_part}j')
print((5 + 2j) * (3 + 7j))
print(f'{(compl1 * compl2).real_part} + {(compl1 * compl2).imaginary_part}j')

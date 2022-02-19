








class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                     self.real * other.imaginary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"


my_complex_number = Complex(9, 5)
my_complex_number_2 = Complex(-5, 6)
print(f"Сумма: {my_complex_number + my_complex_number_2}")
print(f"Произведение: {my_complex_number * my_complex_number_2}")

my_number = complex(9, 5)
my_number_2 = complex(-5, 6)

print(my_number+my_number_2)
print(my_number*my_number_2)
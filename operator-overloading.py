class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __lt__(self, other):
        return (self.real**2 + self.imag**2) < (other.real**2 + other.imag**2)

    def __le__(self, other):
        return (self.real**2 + self.imag**2) <= (other.real**2 + other.imag**2)

# Example Usage
c1 = Complex(3, 2)
c2 = Complex(1, 7)

print(f"c1 + c2 = {c1 + c2}")
print(f"c1 - c2 = {c1 - c2}")
print(f"c1 * c2 = {c1 * c2}")
print(f"c1 / c2 = {c1 / c2}")
print(f"c1 == c2? {c1 == c2}")
print(f"c1 < c2? {c1 < c2}")
print(f"c1 <= c2? {c1 <= c2}")

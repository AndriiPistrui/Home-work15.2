from math import gcd


class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b
        self._reduce()

    def _reduce(self):
        # Скорочуємо дріб
        g = gcd(self.a, self.b)
        self.a //= g
        self.b //= g

    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other):
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        if new_a < 0:
            raise ValueError("Resulting fraction is negative, which is not supported")
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


# Тестові приклади
f_a = Fraction(2, 3)
f_b = Fraction(1, 2)
f_c = f_b + f_a
print(f_c)  # Виводимо результат додавання для перевірки
f_d = f_b * f_a
print(f_d)  # Виводимо результат множення для перевірки
f_e = f_a - f_b
print(f_e)  # Виводимо результат віднімання для перевірки

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(1, 2)
assert f_1 == f_2  # True
print('OK')

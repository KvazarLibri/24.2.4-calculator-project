import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.adding(3, 2) == 5  # Используем метод adding

    def test_subtract(self):
        assert self.calc.subtraction(5, 3) == 2  # Используем метод subtraction

    def test_multiply(self):
        assert self.calc.multiply(4, 3) == 12  # Используем метод multiply

    def test_divide(self):
        assert self.calc.division(10, 2) == 5  # Используем метод division

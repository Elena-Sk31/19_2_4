from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(2, 2) == 4

    def test_multiply_failed(self):
        assert self.calc.multiply(2, 2) != 5

    def test_division(self):
        assert self.calc.division(4, 2) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(4, 2) == 2

    def test_adding(self):
        assert self.calc.adding(2, 2) == 4

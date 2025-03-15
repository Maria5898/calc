import logging
from abc import ABC, abstractmethod

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Модель (Model)
class ComplexNumber:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'({self.real} + {self.imag}i)'

# Интерфейс для операций (абстрактный класс)
class Operation(ABC):
    @abstractmethod
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        pass

# Операции
class Addition(Operation):
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        result = ComplexNumber(a.real + b.real, a.imag + b.imag)
        logging.info(f'Сложение: {a} + {b} = {result}')
        return result

class Multiplication(Operation):
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        real = a.real * b.real - a.imag * b.imag
        imag = a.real * b.imag + a.imag * b.real
        result = ComplexNumber(real, imag)
        logging.info(f'Умножение: {a} * {b} = {result}')
        return result

class Division(Operation):
    def execute(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        if b.real == 0 and b.imag == 0:
            logging.error("Деление на ноль!")
            raise ValueError("Нельзя делить на ноль!")
        denominator = b.real**2 + b.imag**2
        real = (a.real * b.real + a.imag * b.imag) / denominator
        imag = (a.imag * b.real - a.real * b.imag) / denominator
        result = ComplexNumber(real, imag)
        logging.info(f'Деление: {a} / {b} = {result}')
        return result

# Контроллер (Controller)
class Calculator:
    def __init__(self, operation: Operation):
        self.operation = operation

    def calculate(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        return self.operation.execute(a, b)

# Пример использования
if __name__ == "__main__":
    num1 = ComplexNumber(4, 3)
    num2 = ComplexNumber(2, -1)
    
    calc = Calculator(Addition())
    print("Сложение:", calc.calculate(num1, num2))
    
    calc = Calculator(Multiplication())
    print("Умножение:", calc.calculate(num1, num2))
    
    calc = Calculator(Division())
    print("Деление:", calc.calculate(num1, num2))

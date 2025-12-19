# Файл test.py
import unittest
from random import choice, randint
from app import Figure, Name  # імпортуємо з app.py


class TestFigure(unittest.TestCase):
    def setUp(self):
        """Виконується перед кожним тестом"""
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
    
    def test_figure_type(self):
        """Тестуємо чи правильно повертається тип фігури"""
        self.assertEqual(self.figure, self.obj.get_figure_type)
    
    def test_figure_length(self):
        """Тестуємо чи правильно повертається довжина"""
        self.assertEqual(self.length, self.obj.get_figure_length)
    
    def test_invalid_figure(self):
        """Тестуємо створення невірної фігури"""
        with self.assertRaises(AssertionError):
            Figure("коло", 1)
    
    def test_zero_length(self):
        """Тестуємо створення фігури з нульовою довжиною"""
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)


class TestName(unittest.TestCase):
    def test_valid_name(self):
        """Тестуємо валідне ім'я"""
        name_obj = Name("Павло", "програмування")
        self.assertEqual(name_obj.name, "Павло")
        self.assertEqual(name_obj.hobby, "програмування")
    
    def test_invalid_name(self):
        """Тестуємо невірне ім'я"""
        with self.assertRaises(ValueError):
            Name("Невідомий", "щось")
    
    def test_empty_hobby(self):
        """Тестуємо пусте хоббі"""
        with self.assertRaises(ValueError):
            Name("Богдан", "")


if __name__ == '__main__':
    unittest.main(verbosity=2)
# Лабораторна робота 3: Тестування

## Мета
Навчитися тестувати Python код за допомогою assert, unittest та pytest.

## Файли
- `app.py` - основні класи Figure та Name
- `test.py` - юніт тести
- `simple_tests.py` - прості тести assert

## 1. Перевірка assert
### Код:
```python
number = -1
assert number > 0, "число має бути більшим за нуль!"
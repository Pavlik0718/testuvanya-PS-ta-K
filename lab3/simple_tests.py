# Прості тести assert
print("=== 1. ПЕРЕВІРКА ASSERT ===")

# 1. Простий assert
number = -1
try:
    assert number > 0, "число має бути більшим за нуль!"
    print("Assert пройшов")
except AssertionError as e:
    print(f"Assert помилка: {e}")

# 2. Перевірка вводу з клавіатури
print("\n=== 2. ПЕРЕВІРКА INPUT ===")
a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"Введене число: {a}")

# 3. Тестування класу Figure
print("\n=== 3. ТЕСТУВАННЯ КЛАСУ FIGURE ===")

# Валідний об'єкт
print("Створюємо валідну фігуру:")
try:
    c = Figure("квадрат", 5)
    print(f"  Успішно: {c.type}, довжина: {c.length}")
except AssertionError as e:
    print(f"  Помилка: {e}")

# Невалідний тип
print("\nСпробуємо створити невірну фігуру:")
try:
    d = Figure("трапеція", 10)
except AssertionError as e:
    print(f"  Очікувана помилка: {e}")

# Невалідна довжина
print("\nСпробуємо створити фігуру з нульовою довжиною:")
try:
    e = Figure("трикутник", 0)
except AssertionError as e:
    print(f"  Очікувана помилка: {e}")
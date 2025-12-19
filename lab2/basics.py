# 1. ТИПИ ДАНИХ
print("=== 1. ТИПИ ДАНИХ ===")
a = "Павло"  # Текст
b = 25  # Число
c = ["яблуко", "банан", "апельсин"]  # Список
d = {"ім'я": "Павло", "вік": 18}  # Словник
e = ("яблуко", "банан")  # Кортеж
f = {"яблуко", "банан", "яблуко"}  # Множина

print("Текст:", a)
print("Число:", b)
print("Список:", c)
print("Словник:", d)
print("Кортеж:", e)
print("Множина:", f)

# 2. КОНСТАНТИ
print("\n=== 2. КОНСТАНТИ ===")
print("True =", True)
print("False =", False)
print("None =", None)

# 3. ВБУДОВАНІ ФУНКЦІЇ
print("\n=== 3. ВБУДОВАНІ ФУНКЦІЇ ===")
print("Довжина тексту 'Привіт':", len("Привіт"))
print("Модуль числа -10:", abs(-10))
print("Сума чисел 1,2,3,4,5:", sum([1, 2, 3, 4, 5]))

# 4. ЦИКЛИ
print("\n=== 4. ЦИКЛИ ===")
print("Цикл for:")
for i in range(3):
    print(f"  Крок {i}")

print("\nЦикл while:")
count = 0
while count < 3:
    print(f"  Лічильник: {count}")
    count += 1

# 5. УМОВИ
print("\n=== 5. УМОВИ ===")
number = 10

if number > 0:
    print(f"Число {number} додатнє")
elif number < 0:
    print(f"Число {number} від'ємне")
else:
    print("Це нуль")

# 6. ПОМИЛКИ
print("\n=== 6. ОБРОБКА ПОМИЛОК ===")
try:
    result = 10 / 0
    print("Результат:", result)
except ZeroDivisionError:
    print("Помилка: ділити на нуль не можна!")
finally:
    print("Це виконається завжди")

# 7. КОНТЕКСТ-МЕНЕДЖЕР (робота з файлами)
print("\n=== 7. РОБОТА З ФАЙЛАМИ ===")
# Створимо тестовий файл
with open("test.txt", "w") as file:
    file.write("Це тестовий файл\n")
    file.write("Для прикладу роботи з with\n")

# Прочитаємо його
with open("test.txt", "r") as file:
    print("Вміст файлу:")
    for line in file:
        print("  ", line.strip())

# 8. LAMBDA-ФУНКЦІЇ
print("\n=== 8. LAMBDA-ФУНКЦІЇ ===")
# Звичайна функція
def додати(x, y):
    return x + y

# Lambda-функція
додати_лямбда = lambda x, y: x + y

print("Звичайна функція: 5 + 3 =", додати(5, 3))
print("Lambda-функція: 5 + 3 =", додати_лямбда(5, 3))
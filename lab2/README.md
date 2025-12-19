# Python — коротко для новачка

## Типи даних

python
a = 10        # int
b = 3.14      # float
c = "Привіт"  # str
d = True      # bool


## Ввід / вивід

python
name = input("Ім'я: ")
age = int(input("Вік: "))
print(name, age)


## Умови

python
if age >= 18:
    print("Повнолітній")
else:
    print("Неповнолітній")


## Цикл for

python
for i in range(3):
    print(i)


## Цикл while

python
i = 0
while i < 3:
    print(i)
    i += 1


## Функції

python
def greet(name):
    return "Привіт " + name

print(greet("Павло"))




## Міні-приклад (усе разом)

python
def check(n):
    if n % 2 == 0:
        print("Парне")
    else:
        print("Непарне")

num = int(input("Число: "))
check(num)

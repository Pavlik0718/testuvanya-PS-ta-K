name = input("Введи своє ім'я: ")
year_of_birth = int(input("Введи рік народження: "))

current_year = 2025
age = current_year - year_of_birth

print("Привіт,", name)
print("Тобі", age, "років")

if age >= 18:
    print("Ти повнолітній")
else:
    print("Ти ще неповнолітній")

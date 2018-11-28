
def get_sum(num_one, num_two):
    try:
        summa = int(num_one) + int(num_two)
        return f"Сумма: {summa}"
    except ValueError:
        return "Введите правильные числа"


num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
print(get_sum(num1, num2))

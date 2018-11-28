input_age = int(input("Введите свой возраст: "))


def age(age):
    if age < 7:
        return "Вы ходите в детский сад"
    elif 6 < age < 17:
        return "Вы учитесь в школе"
    elif 16 < age < 21:
        return "Вы учитесь в ВУЗе"
    elif 20 < age < 60:
        return "Вы работаете"
    elif age > 59:
        return "Вы на пенсии"
    else:
        return "Неправильно введен возраст"


print(age(input_age))

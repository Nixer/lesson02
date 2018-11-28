def ask_user():
    qa = {"Как дела?": "Хорошо!",
          "Что делаешь?": "Программирую",
          "Как тебя зовут?": "MacPro"}
    while True:
        try:
            q = input("Твой вопрос?: ")
            if q in qa:
                print(qa[q])
            elif q.lower() == "пока":
                print("Пока!")
                break
            else:
                print("Не знаю ответа!")
        except KeyboardInterrupt:
            print("\nПока!")
            break


ask_user()

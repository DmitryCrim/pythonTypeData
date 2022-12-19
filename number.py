pin = 1234
print ("Пожалуйства Ваш пин-код: ")
user_pin = int(input())
if pin == user_pin:
    print("Какую сумму вы хотите снять")
else:
    print("Ошибка, введите корректный пин-код, у Вас осталост 2 попытки")
    user_pin = int(input())
    if pin == user_pin:
        print("Какую сумму вы хотите снять")
    else:
        print("Ошибка, введите корректный пин-код, у Вас осталост 1 попытка")
        user_pin = int(input())
        if pin == user_pin:
            print("Пин-код введен правильно")
        else:
            print("Карта заблокирована")


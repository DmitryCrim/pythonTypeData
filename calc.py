znak = input('Введите знак + - * /')
a = input('Введите первое значение')
b = input('Введите второе значение')
if znak == '+':
    c = int(a) + int(b)
    print(c)
elif znak == '-':
    c = int(a) - int(b)
    print(c)
elif znak == '*':
    c = int(a) * int(b)
    print(c)
elif znak == '/':
    if int(b) == 0:
        print('Error')
    else:
     c = int(a) / int(b)
     print(c)



# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")
#stepik_4.1_only_plus
print ("Введите первое число:")
number1 = int(input())
print ("Введите второе число:")
number2 = int(input())
print ("Введите третье число:")
number3 = int(input())
if number1 <= 0:
    number1 = 0
if number2 <= 0:
    number2 = 0
if number3 <= 0:
    number3 = 0

print (number1 + number2 + number3)
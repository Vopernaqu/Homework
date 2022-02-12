number = int(input("Введите целое положительное число: "))
i = 0

while number > 1 :
    i += 1
    number /= 10
print(i)



result = 1
b = int(input("Введите целое нечётное число: "))
n = b
a = 1
while n != a :
    n -= 2
    result = result + b
    b -= 2
print(result)

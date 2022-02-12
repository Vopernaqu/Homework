result = 0
a = 1/2
b = int(input("Введите кол-во слогаемых: "))
c = 0
while c!=b :
    result += a
    a /= 2
    c += 1
print(result)

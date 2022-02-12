#1
man = {'first_name': "Artem",
       'last_name': "Gurtovenko",
       'age' : 13,
       'city' : "Kharkiv"
        }
for i in man.values() :
    print(i)
print("-"*40)
#2
numbers = {
        "Sofia" : 2,
        "Artem" : 6,
        "Andrey" : 9,
        "Max" : 7,
        "Timur" : 33,
           }
for a, b in numbers.items() :
    print(f"{a}:{b}")
print("-"*40)
#3
gloss = {
        "if":"Логический оператор 'eсли', выполняеться если условие True",
        "while":"Цикл while выполняется если пока условие False",
        "list":"Лист-список набор строк, чисел и т.д.",
        "int":"функция int превращяет число в целое",
        "float":"функция float превращяет число в вещественое"
        }
print(f"if:{gloss['if']}\n"
      f"while:{gloss['while']}\n"
      f"list:{gloss['list']}\n"
      f"int:{gloss['int']}\n"
      f"float:{gloss['float']}")
print("-"*40)
#4
for c, d in gloss.items() :
    print(f"{c}:{d}")
print("-"*40)
#5
rivers = {
         "nile" : "egypt",
         "amazon" : "brasil", #Большая часть
         "missouri" : "usa"
         }
for f, k in rivers.items() :
    print(f"The {f.title()} runs through {k.title()}")
    print(f.title())
    print(k.title())


#1
def display_message() :
    print("Теперь я знаю функцию")
display_message()
print("-" * 50)
#2
def favorite_book(title) :
    print(f"One of my favorite books is {title}")
title = str(input("Your favorite book:"))
favorite_book(title)
print("-" * 50)
#3
def make_shirt(size, text) :
    print(f"Ваш размер футболки {size}, а надпись {text}")
size = int(input("Размер футболки: "))
text = input("Текст:")
make_shirt(size, text)
print("-" * 50)
#4
make_shirt("L", "I love Python")
make_shirt(size, text)
print("-" * 50)
#5
def describe_city(city, country) :
    print(f"{city} is in {country}")
describe_city("Reykjavik", "Iceland")
i = 0
k = int(input("Сколько городов вам надо:"))
while i != k :
    city = input("Город: ")
    country = input("Страна: ")
    i += 1
    describe_city(city, country)



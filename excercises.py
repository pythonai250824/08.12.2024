
################### 2
# for i in range(7, 31 + 2, 2)


####################### 4
for i in range(1, 45 + 1, 1):
    print(i, end=' ')
    if i % 3 and i % 5 == 0:
        print("FizzBuzz", end="")
    elif i % 3 == 0:
        print("Fizz", end="")
    elif i % 5 == 0:
        print("Buzz", end="")
    else:
        print(i)
    # if i % 5 and i % 3 == 0:
    #     print("FizzBuzz", end="")

    # 15
    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print("Buzz", end="")


# [ { id: 1, name: 'itay' }, { id: 2 }, {color: red} ]
# id
########################## 6
def remove_attr(people: list[dict], key: str) -> None:
    for person in people:  # for-each
        if key in person:  # same if key in person.keys():
            del person[key]

people: list[dict] = [
    {"id": 1, "name": "Alice", "age": 28, "city": "New York"},
    {"id": 2, "name": "Bob", "age": 35, "city": "Los Angeles"},
    {"id": 3, "name": "Charlie", "age": 24, "city": "Chicago"},
    {"id": 4, "name": "Diana", "age": 30, "city": "Houston"}
]
sorted(people, key=lambda p: p['age'])
remove_attr(people, 'name')
print()
for p in people:
    print(p)

[1,2,3,-1].sort(key = lambda x: x ** 2)

filter([1, 4, -2, 3, 0, 2, -100], lambda x: x > 0)

def is_positive(x) -> bool:
    return x > 0

filter([1, 4, -2, 3, 0, 2, -100], is_positive)
filter([1, 4, -2, 3, 0, 2, -100], lambda x: x > 0)
map([1, 4, -2, 3, 0, 2, -100], lambda x: x ** 2)
['danny', 'zvi', 'sharon'].sort(key=lambda w: len(w))
sorted(['danny', 'zvi', 'sharon'], key=lambda w: len(w))

def add(x, y):
    return x + y

add = lambda x, y: x + y

'''
Write a python program that gets user input (use input() function for this).
The first input will be the user full name
Second input will be the user age
Third input will be the user email
Write validation for each input provided by the user and allow the user to try again in case the user provided invalid input.

Validation for full name input → string type with 2 words for first name and last name.
Validation for age input → int type between 1 - 130.
Validation for email input → string type with ‘@’ inside.
'''

########### 21
def validate_name (name: str) -> bool:
    # return len(name.split()) == 2
    # longer
    if len(name.split()) == 2:
        return True
    else:
        return False

while True:
    user_name: str = input('user name? ')
    if validate_name(user_name):
        break

age: int = int(input('age? '))
email: str = input('email? ')

##################### regular expression, regex
import re
#  rule = "w^2"

# while True:
    # email --> ^[^@]+@[^\s@]+\.[^\s@]+$

while True:
    user_name: str = input('user name? ')
    if re.match("w^2", user_name):
        break
    pwd: str = input('user pwd? ')
    if re.match( r"^[A-Z](?=.*[!@#$%^&*(),.?\":{}|<>])[A-Za-z\d!@#$%^&*(),.?\":{}|<>]{7,}$", pwd):
        break
    # email --> ^[^@]+@[^\s@]+\.[^\s@]+$




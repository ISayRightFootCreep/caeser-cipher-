list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
a = int(input("how many shifts? positive for left, negative for right  "))

if a > 0:
    for i in range(a):
        list.append(list.pop(0))
elif a < 0:
    a = a * -1
    for i in range(a):
        list.insert(0, list.pop())
print(list)











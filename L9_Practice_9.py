# Напишіть квадрат із зірочок
n = int(input())
for i in range(n):
    qdt = ["*" for m in range(n)]
    print(*qdt)
    # звездочка перед принтом списка раскроет список, и напечатает его элементы без кавычек
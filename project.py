def main(a):
    while True:
        try:
            a = int(input("Введите число: "))
            break
        except ValueError:
           print("Это не число")
        if a == "":
           print("Вы не чего не ввели")
    print(a)
main(1)

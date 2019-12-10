def main(a):
    while True:
        try:
            a = int(input("Введите число: "))
        except ValueError:
           print("Это не число")
        c = str(a)
        print("Хорошое число:"+c)
main(1)

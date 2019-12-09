def main(a):
    while True:
       try:
           a = int(input("Введите число: "))
           break
       except ValueError:
           print("Это не число")
       if a == "":
           print("Здесь пусто")
       else:
           print(a)
main()

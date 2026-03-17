luvut = []

while True:
    syote = input("Anna luku:")

    if syote =="":
        break

    luvut.append (int(syote))

    luvut.sort(reverse=True)

    print(luvut[:5])
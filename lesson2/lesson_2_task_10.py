def bank(x, y):
    for n in range(y):
        x= x + (x * 0.1)
    return x

x=float(input("Депозит: "))
y=int(input("Срок: "))

print(bank(x, y))
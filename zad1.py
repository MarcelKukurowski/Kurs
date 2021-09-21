import math
a = input("Podaj a")
b = input("Podaj b")
c = input("Podaj c")

a = int(a)
b = int(b)
c = int(c)

delta = math.pow(b,2)-(4*a*c)

if(delta < 0 ):
    print("Nie ma miejsc zerowych")
elif(delta == 0):
    x1 = -b/(2*a)
    print(f"Funkcja zawiera 1 miejsce zerowe: {x1}")
else:
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print(f"Funkcja zawiera 2 miejsca zerowe: {x1} oraz {x2}")


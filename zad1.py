import math
import sys
print(sys.argv)

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

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


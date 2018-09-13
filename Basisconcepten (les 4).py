import math

print(math.sqrt(3**2 + 4**2))
print((math.sqrt(3**2 + 4**2)) == 5 )
pi = math.pi
A = str(pi*10**2)
print("A=πr2" + "   " + "A: " + A)
print(5**2+5**2 < 7)

list = ([3, 7, -2, 12])
print(max(list) - min(list))

letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
hoeveelheid = ([letters.count("A"), letters.count("B"), letters.count("C")])
print(hoeveelheid)

name = input("Enter your name: ")
age = int(input("Enter your name: "))
print(name + ",you'll be " + str(age + 1) + " next year!")
import sys

time = lambda x: x*x
space = lambda d: d+d
consciousness = lambda e: e/e
Self = lambda f: f-f
def reversenum(number):
    reversed_number = ""
    while number > 0:
        reversed_number += str(number % 10)
        number //= 10
    return int(reversed_number)
time2 = lambda x2: x2*(reversenum(x2))
space2 = lambda d2: d2+(reversenum(d2))
consciousness2 = lambda e2: e2/(reversenum(e2))
self2 = lambda f2: f2-(reversenum(f2))
evaluate = 0
for letter in sys.argv[1]:
    evaluate += ord(letter)

F = [evaluate]
print("\033[31m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m x*x Time:\033[0m")
entrance = print(list(map(time, F)))
print("\033[31m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m d+d Space:\033[0m")
escalate = print(list(map(space, F)))
print("\033[31m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m e/e Consciousness:\033[0m")
assimilate = print(list(map(consciousness, F)))
print("\033[31m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m f-f Self:\033[0m")
individualize = print(list(map(Self, F)))
print("")
print("\033[34m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m x2*(reversenum(x2)) Time:\033[0m")
Exit = print(list(map(time2, F)))
print("\033[34m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m d2+(reversenum(d2)) Space:\033[0m")
Calm = print(list(map(space2, F)))
print("\033[34m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m e2/(reversenum(e2)) Consciousness:\033[0m")
Solve = print(list(map(consciousness2, F)))
print("\033[34m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m f2-(reversenum(f2)) Self:\033[0m")
Coagula = print(list(map(self2, F)))
print("")
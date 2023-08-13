import sys

time = lambda x: x*x
space = lambda d: d+d
consciousness = lambda e: e/e
Self = lambda f: f-f
def reverse(number):
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10
    return reversed_number
time2 = lambda x2: x2*(reverse(x2))
space2 = lambda d2: d2+(reverse(d2))
consciousness2 = lambda e2: e2/(reverse(e2))
self2 = lambda f2: f2-(reverse(f2))

evaluate = int(sys.argv[1])
evaluate2 = int(1)
F = []
while(evaluate2 <= evaluate):
    F.append(evaluate2)
    entrance = print(list(map(time, F)))
    escalate = print(list(map(space, F)))
    assimilate = print(list(map(consciousness, F)))
    individualize = print(list(map(Self, F)))
    print("\033[31m*****"+str(evaluate2)+"*****\033[0m")
    print("\033[32m x*x Time:\033[0m")
    entrance
    print("\033[32m d+d Space:\033[0m")
    escalate
    print("\033[32m e/e Consciousness:\033[0m")
    assimilate
    print("\033[32m f-f Self:\033[0m")
    individualize
    print("")
    Exit = print(list(map(time2, F)))
    Calm = print(list(map(space2, F)))
    Solve = print(list(map(consciousness2, F)))
    Coagula = print(list(map(self2, F)))
    print("\033[34m*****"+str(evaluate2)+"*****\033[0m")
    print("\033[32m x2*(reverse(x2)) Time:\033[0m")
    Exit
    print("\033[32m d2+(reverse(d2)) Space:\033[0m")
    Calm
    print("\033[32m e2/(reverse(e2)) Consciousness:\033[0m")
    Solve
    print("\033[32m f2-(reverse(f2)) Self:\033[0m")
    Coagula
    print("")
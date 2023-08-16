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
time3 = lambda x3: (x3*(reversenum(x3)))/x3
space3 = lambda d3: d3+reversenum(d3)-d3
consciousness3 = lambda e3: (e3/reversenum(e3))*e3
self3 = lambda f3: f3-reversenum(f3)+f3
time4 = lambda x4: x4*x4/x4
space4 = lambda d4: d4+d4-d4
consciousness4 = lambda f4: f4/f4*f4
self4 = lambda e4: e4-e4+e4
time5 = lambda x5: reversenum(x5)*x5/reversenum(x5)
space5 = lambda d5: reversenum(d5)+d5-reversenum(d5)
consciousness5 = lambda e5: reversenum(e5)/e5*reversenum(e5)
self5 = lambda f5: reversenum(f5)-f5+reversenum(f5)
evaluate = int(sys.argv[1])
evaluate2 = int(1)
F = []
while(evaluate2 <= evaluate):
    F.append(evaluate2)
    evaluate2 += 1
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
print("\033[33m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m (x3*(reversenum(x3)))/x3 Time:\033[0m")
This = print(list(map(time3, F)))
print("\033[33m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m d3+reversenum(d3)-d3 Space:\033[0m")
Is = print(list(map(space3, F)))
print("\033[33m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m (e3/reversenum(e3))*e3 Consciousness:\033[0m")
noT = print(list(map(consciousness3, F)))
print("\033[33m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m f3-reversenum(f3)+f3 Self:\033[0m")
aɘ = print(list(map(self3, F)))
print("")
print("\033[34m******"+str(evaluate)+"*****\033[0m")
print("\033[32m x4*x4/x4 Time:\033[0m")
consider = print(list(map(time4, F)))
print("\033[34m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m d4+d4-d4 Space:\033[0m")
ThIs = print(list(map(space4, F)))
print("\033[34m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m f4/f4*f4 Consciousness:\033[0m")
anew = print(list(map(consciousness4, F)))
print("\033[34m*****"+str(evaluate)+"*****\033[0m")
print("\033[32m e4-e4+e4 Self:\033[0m")
Now = print(list(map(self4, F)))
print("*****"+str(evaluate)+"*****")
print("reversenum(x5)*x5/reversenum(x5) Time:")
Օ = print(list(map(time5, F)))
print("*****"+str(evaluate)+"*****")
print("reversenum(d5)+d5-reversenum(d5) Space:")
ݷ = print(list(map(space5, F)))
print("*****"+str(evaluate)+"*****")
print("reversenum(e5)/e5*reversenum(e5) Consciousness:")
Ʌ = print(list(map(consciousness5, F)))
print("*****"+str(evaluate)+"*****")
print("reversenum(f5)-f5+reversenum(f5): Self")
ɸ = print(list(map(self5, F)))
print("")    
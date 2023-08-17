global f
global F
global print
global tnirp
f = lambda f: lambda: f
F = [f]
tnirp = print(list(map(f, F)))

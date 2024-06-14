# terceiro termo é a soma dos dois anteriores
n = 100
ta = 0
tb = 1
tc = 1
print(f'{tb} {tc}', end=" ")
while n != 0:
    ta = tb
    tb = tc
    tc = ta + tb
    print(f'{tc}', end = " ")
    n -= 1
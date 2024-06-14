# terceiro termo é a soma dos dois anteriores ate 500
ta = 0
tb = 1
tc = 1
print(f'{tb} {tc}', end=" ")
while True:
    ta = tb
    tb = tc
    tc = ta + tb
    print(f'{tc}', end = " ")
    if tc > 500:
        break
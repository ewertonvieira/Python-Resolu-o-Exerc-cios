base = int(input('Base: '))
expoente = int(input('Base: '))
i = 0; expo = 1
while i < expoente:
    expo *= base
    i += 1
print(expo)
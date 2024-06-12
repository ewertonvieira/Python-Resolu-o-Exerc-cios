country_a = 80000 # 3% crescimento ao ano
country_b = 200000 # 1.5% crescimento ao ano
count = 0
aux = 0
# Numero de anos que A leva para superar B:
while country_a < country_b:
    country_a *= (3/100)
    country_b *= (1.5/100)
    count += 1
    
print(count)
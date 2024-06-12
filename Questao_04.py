country_a = 80000 # 3% crescimento ao ano
country_b = 200000 # 1.5% crescimento ao ano
count = 0
# Numero de anos que A leva para superar B:
while country_a < country_b:
    country_a += country_a * 0.03
    country_b += country_b * 0.015
    count += 1
    
print(count)
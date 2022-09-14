c = int(input("Zadajte sumu v €: "))

s = c // 100; c = c - s*100
p = c // 50; c = c - p*50
d = c // 20; c = c - d*20
dd = c // 10; c = c - dd*10
pp = c // 5; c = c - pp*5
j = c // 2; c = c - j*2

print("Zadaná hodnota: ", c, "€")
print("100€:", s)
print("50€:", p)
print("20€:", d)
print("10€:", dd)
print("5€:", pp)
print("1€:", j)

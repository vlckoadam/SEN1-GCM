import datetime

c = int(input("Zadajte čas v sekundách: "))
d = str(datetime.timedelta(seconds=c))

print("Zadaná hodnota:", c, "sekúnd")
print(d)



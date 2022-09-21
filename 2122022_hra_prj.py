import random
from subprocess import call

f = open('hihi.txt', 'r')
hl = f.read()

print("--------------------------")
print("|                        |")
print("|      Mária ChatBox     |")
print("|                        |")
print("--------------------------")
n = input("Zadaj svoje meno: ")

list = ["Choď sa osprchovať", "Už si sa sprchoval?", "To čo máte chlapci?", "A to ako vám napadlo?", "Chlapci už zhasnínajte",
        "Ideš na omšu?", "JARO HARAAG!!", f'Zavolám vychošovi, {n}',"Povysávať a potom aj umyť podlahu!", f"Zavolám otcovi, {n}",
        "Bol si v sprche", "Neviem ti odpovedať", "Ideš na šport?"]
call("clear")
print("Ahoj, ", n)
t = input()
if len(t)==0:
    exit()

while len(t)>=1:
    call("clear")
    n = input()
    if n == "Nie" in "Choď sa osprchovať":
        print("Máš čas do 21:3O!!!")
    if n == ["Ahoj", "Čau", "cc"]:
        print("Ako sa máš?")
    print(random.choice(list))
    if len(n)==0:
        break




















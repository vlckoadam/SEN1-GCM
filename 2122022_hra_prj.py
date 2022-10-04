import random

list = ["Choď sa osprchovať", "Už si sa sprchoval?", "To čo máte chlapci?", "A to ako vám napadlo?", "Chlapci už zhasnínajte",
        "Ideš na omšu?", "JARO HARAAG!!", 'Zavolám vychošovi, %',"Povysávať a potom aj umyť podlahu!", "Zavolám otcovi, %",
        "Bol si v sprche", "Neviem ti odpovedať", "Ideš na šport?", "Ideš do kaplnky?", "Pustím ťa do kaplnky"]

def hra():    
    print("--------------------------")
    print("|                        |")
    print("|      Mária ChatBox     |")
    print("|                        |")
    print("--------------------------")
    n = input("Zadaj svoje meno: ")
    chat(n)

def koniec():
    a = input("Naozaj chceš ukončiť hru? [A/N]")
    if a == "A" or "a":
        hra()
    if a == "N" or "n":
        exit()
     

def chat(n):
    print("Mária: Ahoj, ", n, "\n")
    t = input(n + ": ")
    print("Mária: ", random.choice(list).replace("%", n))
    tt = input(n + ": ")
    while len(tt)>1:
        if tt == ["Nie", "nie", "nn"] in list[1:2]:
            print("Mária: Máš čas do 21:30!!")
        elif tt == ["Ahoj", "čau", "cc"]:
            print("Mária: Ako si sa mal v škole?")
        elif tt == "Pozdrav Pán Boh":
            print("Mária: POZDRAV PÁÁÁÁÁÁN BOH")
        else:
            print("Mária: ", random.choice(list).replace("%", n))
            tt

    if len(tt) == 0:
        koniec()

def repeat():
    hh = input("Pre spustenie programu zadaj heslo:\n")
    while hh != "MARIA":
        hh = input("Zlé heslo opakuj\n")
    hra()
     

repeat()










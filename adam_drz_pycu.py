from random import randint

def uvod():
    print("1. Hráč\n2. Počítač")
    c = int(input(""))

    if c == 1:
        hra_hrac()
    if c == 2:
        pass


def hra_hrac():
    t = ["Kameň", "Papier", "Nožnice"]

    bot = t[randint(0,2)]

    hr = False

    while hr == False:
        print("######################")
        hr = input("Kameň, papier nožnice?\nHráč: ")
        if hr == bot:
            print("######################")
            print("Počítač vybral: "+bot)
            print("Remíza")
        elif hr == "Kameň":
            if bot == "Papier":
                print("######################")
                print("Počítač vybral: Papier")
                print("Prehral si!", bot, "zabalí", hr)
            else:
                print("######################")
                print("Počítač vybral: " + bot )
                print("Vyhral si!", hr, "rozbije", bot)

        elif hr == "Papier":
            if bot == "Nožnice":
                print("######################")
                print("Počítač vybral: " + bot )
                print("Prehral si", bot, "prestrihne", hr)
            else:
                print("######################")
                print("Vyhral si",hr, "zabalí", bot)
        elif hr== "Nožnice":
            if bot == "Kameň":
                print("######################")
                print("Počítač vybral: " + bot )
                print("Prehral si!", bot, "rozbije", hr)
            else:
                print("######################")
                print("Počítač vybral: " + bot )
                print("Vyhral si!", hr, "cut", bot)
        else:
            print("######################")
            print("Tvoj výber nie je správny. Skontroluj, či si napísal všetko gramaticky správne a s diaktritikou")


        hr = False
        bot = t[randint(0,2)]

def hra_bot():
    t = ["Kameň", "Papier", "Nožnice"]

    bot = t[randint(0,2)]

    bot2 = False

    while hr == False:
        print("######################")
        hr = input("Kameň, papier nožnice?\nHráč: ")
        if hr == bot:
            print("######################")
            print("Počítač vybral: "+bot)
            print("Remíza")
        elif hr == "Kameň":
            if bot == "Papier":
                print("######################")
                print("Počítač vybral: Papier")
                print("Prehral si!", bot, "zabalí", hr)
            else:
                print("######################")
                print("Počítač vybral: " + bot )
                print("Vyhral si!", hr, "rozbije", bot)

        elif hr == "Papier":
            if bot == "Nožnice":
                print("######################")
                print("Počítač vybral: " + bot )
                print("Prehral si", bot, "prestrihne", hr)
            else:
                print("######################")
                print("Vyhral si",hr, "zabalí", bot)
        elif hr== "Nožnice":
            if bot == "Kameň":
                print("######################")
                print("Počítač vybral: " + bot )
                print("Prehral si!", bot, "rozbije", hr)
            else:
                print("######################")
                print("Počítač vybral: " + bot )
                print("Vyhral si!", hr, "cut", bot)
        else:
            print("######################")
            print("Tvoj výber nie je správny. Skontroluj, či si napísal všetko gramaticky správne a s diaktritikou")


        hr = False
        bot = t[randint(0,2)]

uvod()

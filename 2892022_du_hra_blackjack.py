import random
import os

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def rozdaj(deck):
    nr = []
    for i in range(2):
        random.shuffle(deck)
        karta = deck.pop()
        if karta == 11:karta = "J"
        if karta == 12:karta = "Q"
        if karta == 13:karta = "K"
        if karta == 14:karta = "A"
        nr.append(karta)
    return nr

def hraj_znova():
    r = input("Chceš hrať znova? (A/N)").lower()
    if r == "A" or "a":
        dealer_nr = []
        hrac_nr = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
    else:
        print("Ukončujem hru")
        exit()

def total(nr):
    total = 0
    for karta in nr:
        if karta == "J" or karta == "Q" or karta == "K":
            total += 10
        elif karta == "A":
            if total >= 11:
                total += 11
            else:
                total += 11
        else:
            total += karta
    return total

def zobrat(nr):
    karta = deck.pop()
    if karta == 11:karta = "J"
    if karta == 12:karta = "Q"
    if karta == 13:karta = "K"
    if karta == 14:karta = "A"
    nr.append(karta)
    return nr

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_odp(dealer_nr, hrac_nr):
    clear()
    print("Dealer dostal " + str(dealer_nr) + " a má " + str(total(dealer_nr)))
    print("Ty si dostal " + str(hrac_nr) + " a máš " + str(total(hrac_nr)))

def blackjack(dealer_nr, hrac_nr):
    if total(hrac_nr) == 21:
        print_odp(dealer_nr, hrac_nr)
        print("Gratulujem! Vyhral si.\n")
        hraj_znova()
    elif total(dealer_nr) == 21:
        print_odp(dealer_nr, hrac_nr)
        print("Prepáč, ale prehral si.\n")
        hraj_znova()

def skore(dealer_nr, hrac_nr):
    if total(hrac_nr) == 21:
        print_odp(dealer_nr, hrac_nr)
        print("Gratulujem! Vyhral si.\n")
    elif total(dealer_nr) == 21:
        print_odp(dealer_nr, hrac_nr)
        print("Prepáč, ale prehral si.\n")
    elif total(hrac_nr) > 21:
        print_odp(dealer_nr, hrac_nr)
        print("Bohužiaľ si prekročil počet 21 a prehral si.\n")
    elif total(dealer_nr) > 21:
        print_odp(dealer_nr, hrac_nr)
        print("Dealer prekročil počet 21. Gratulujem, vyhral si!\n")
    elif total(hrac_nr) > total(dealer_nr):
        print_odp(dealer_nr, hrac_nr)
        print("Gratulujem! Máš väčšie skóre ako dealer. Vyhral si!\n")
    elif total(hrac_nr) < total(dealer_nr):
        print_odp(dealer_nr, hrac_nr)
        print("Dealer má väčšie skóre ako ty. Prehral si.\n")

def hra():
    vyber = 0
    print("------------------------")
    print("|                      |")
    print("|       BLACKJACK      |")
    print("|                      |")
    print("------------------------")
    dealer_nr = rozdaj(deck)
    hrac_nr = rozdaj(deck)
    blackjack(dealer_nr, hrac_nr)
    vyber = input("Chceš si zobrať kartu? [Z]\nChceš podržať ťah? [P]\nChceš ukončiť hru? [Q]\n")
    if vyber == "Z" or "z":
        zobrat(hrac_nr)
        while total(dealer_nr) < 17:
            zobrat(dealer_nr)
        skore(dealer_nr, hrac_nr)
    elif vyber == "P" or "p":
        while total(dealer_nr) < 17:
            zobrat(dealer_nr)
        skore(dealer_nr, hrac_nr)
        hraj_znova()
    elif vyber == "Q" or "q":
        print("Ukončujem hru")
        exit()

if __name__ == "__main__":
    hra()

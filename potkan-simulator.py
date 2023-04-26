import random
import time
import os

# JAZYKY + MAIN LOBBY

def svk():
    print("####################################################")
    print("#          🐀 SIMULÁCIA ŽIVOTA POTKANA 🐀         #")
    print("#                                                  #")
    print("#                                                  #")
    print("#        🐀 STLAČ [A] PRE SPUSTENIE HRY 🐀        #")
    print("#        🐀 STLAČ [X] PRE SKONČENIE HRY 🐀        #")
    print("#        🐀 STLAČ [L] PRE ZMENU JAZYKA🐀          #")
    print("#                                                  #")
    print("#                                                  #")
    print("####################################################")
    choose_svk = input("              Choose your answer:        ")
    if choose_svk == "A":
        hra_svk()   


def eng():
    print("####################################################")
    print("#            🐀 POTKAN LIFE SIMULATOR 🐀          #")
    print("#                                                  #")
    print("#                                                  #")
    print("#              🐀 PRESS [A] TO PLAY 🐀            #")
    print("#              🐀 PRESS [X] TO EXIT 🐀            #")
    print("#        🐀 PRESS [L] TO CHANGE LANGUAGE🐀        #")
    print("#                                                  #")
    print("#                                                  #")
    print("####################################################")
    choose_eng = input("              Vyber si odpoveď:        ")
    if choose_eng == "A":
        hra_eng()
def rus():
    print("####################################################")
    print("#          🐀 СИМУЛЯТОР КРЫСИНОЙ ЖИЗНИ 🐀         #")
    print("#                                                  #")
    print("#                                                  #")
    print("#       🐀 НАЖМИ [A], ЧТОБЫ НАЧАТЬ ИГРУ 🐀        #")
    print("#          🐀 НАЖМИ [X], ЧТОБЫ ВЫЙТИ 🐀           #")
    print("#       🐀 НАЖМИ [L], ЧТОБЫ ИЗМЕНИТЬ ЯЗЫК 🐀      #")
    print("#                                                  #")
    print("#                                                  #")
    print("####################################################")
    choose_rus = input("             Oтвечaй:        ")

def hun():
    print("####################################################")
    print("#          🐀 PÁTKÁNY ÉLET SZIMULÁTOR  🐀         #")
    print("#                                                  #")
    print("#                                                  #")
    print("# 🐀 NYOMJA MEG AZ [A], A JÁTÉK ELINDíTÁSÁHOZ 🐀  #")
    print("#   🐀 NYOMJA MEG AZ [X] GOMBOT A KILÉPÉSHEZ 🐀   #")
    print("#         🐀 NYOMJA MEG AZ [L] GOMBOT 🐀          #")
    print("#        🐀 A NYELV MEGVÁLTOZTATÁSÁHOZ 🐀         #")
    print("#                                                  #")
    print("####################################################")
    choose_hun = input("              Válsz:        ")

def ar():
    print("####################################################")
    print("#           🐀 محاكاة حياة الفئران  🐀          #")
    print("#                                                  #")
    print("#                                                  #")
    print("#            🐀 اضغط [A] لبدء اللعبة🐀           #")
    print("#               🐀 اضغط [X] للخروج 🐀            #")
    print("#           🐀 Nاضغط [L] لتغيير اللغة 🐀         #")
    print("#                                                  #")
    print("####################################################")
    choose_ar = input("              أَجِبْ:        ")



# INITIAL LANG SETUP
os.system("clear")
print("####################################################")
print("#            🐀 POTKAN LIFE SIMULATOR 🐀          #")
print("#                                                  #")
print("#                                                  #")
print("#              🐀  [1] SLOVAK    🐀               #")
print("#              🐀  [2] ENGLISH   🐀               #")
print("#              🐀  [3] RUSSIAN   🐀               #")
print("#              🐀  [4] HUNGARIAN 🐀               #")
print("#              🐀  [5] ARABIC    🐀               #")
print("#                                                  #")
print("#                                                  #")
print("####################################################")

choose = int(input("              Choose your language:        "))
if choose == 1:
    os.system("clear")
    svk()
elif choose == 2:
    os.system("clear")
    eng()
elif choose == 3:
    os.system("clear")
    rus()
elif choose == 4:
    os.system("clear")
    hun()
elif choose == 5:
    os.system("clear")
    ar()


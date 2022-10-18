def batoh():
    #batoh
    batoh = input("").split(" ")
    a = int(batoh[0])
    b = int(batoh[1])

    #predmety
    predmety = input("").split(" ")
    s = int(predmety[0])
    p = int(predmety[1])
    o = int(predmety[2])



    # Všetky čísla na vstupe sú v rozmedzí 1 až 1000
    if s and p > a or s and o > a or p and o > a:
        if s and p > b or s and o > b or p and o > b:
            print("Nie")  
            exit 
    elif s and p <= a or s and o <= a or p and o <= a:
        if s and p <= b or s and o <= b or p and o <= b:
            print("Ano")

batoh()
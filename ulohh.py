def decode(g:str):
    list = ["a", "ä", "e", "i", "o", "u",
            "A", "Ä", "E", "I", "O", "U"]
    coded = ""

    for i in (g):
        for j in i:
            if (i) in list:
                coded += "f"+i+"f"
            else:
                coded += ""+i+""

    
    return coded
    
print(decode("Adam Vlčko")) # fAfdfafm Vlčkfof

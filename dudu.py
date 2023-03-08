import tkinter as tk
import random

# vytvor okno s rozmiermi 500x500
window = tk.Tk()
window.geometry("500x500")

# vytvor canvas (plátno) na ktorom bude kreslený štvorec
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# funkcia na vykreslenie červeného štvorca na náhodnej pozícii
def draw_square():
    # vymaž obsah canvasu
    canvas.delete("all")
    # náhodne vygeneruj pozíciu štvorca
    x1 = random.randint(0, 450)
    y1 = random.randint(0, 450)
    x2 = x1 + 50
    y2 = y1 + 50
    # nakresli červený štvorec
    canvas.create_rectangle(x1, y1, x2, y2, fill="red")

# funkcia na zvýšenie skóre po kliknutí na štvorec
def increase_score(event):
    global score
    score += 1
    score_label.config(text="Score: " + str(score))

# inicializuj premennú pre skóre
score = 0

# vytvor label pre zobrazovanie skóre
score_label = tk.Label(window, text="Score: " + str(score))
score_label.pack()

# vykresli prvý štvorec
draw_square()

# pridaj funkciu na kliknutie myšou na canvas
canvas.bind("<Button-1>", increase_score)

# spusti hlavnú smyčku programu
window.mainloop()

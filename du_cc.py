from tkinter import *
import random

# Vytvorenie okna tkinter
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Vytvorenie náhodných bodov
points = []
for i in range(20):
    x = random.randint(50, 450)
    y = random.randint(50, 450)
    canvas.create_oval(x-2, y-2, x+2, y+2, fill='blue')
    points.append((x, y))

# Vytvorenie obdĺžnika z bodov
min_x = min(point[0] for point in points)
max_x = max(point[0] for point in points)
min_y = min(point[1] for point in points)
max_y = max(point[1] for point in points)
canvas.create_rectangle(min_x, min_y, max_x, max_y)

root.mainloop()

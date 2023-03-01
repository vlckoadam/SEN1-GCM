import tkinter as tk
import random

class Square:
    def __init__(self, canvas):
        self.canvas = canvas
        self.size = 50
        self.x = random.randint(0, canvas.winfo_width() - self.size)
        self.y = random.randint(0, canvas.winfo_height() - self.size)
        self.color = self.random_color()
        self.draw()

    def draw(self):
        self.canvas.delete("square")
        self.canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color, tags="square")
        self.size += random.randint(-10, 10)
        self.x += random.randint(-10, 10)
        self.y += random.randint(-10, 10)
        self.canvas.after(100, self.draw)

    def random_color(self):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        return random.choice(colors)

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

square = Square(canvas)

root.mainloop()

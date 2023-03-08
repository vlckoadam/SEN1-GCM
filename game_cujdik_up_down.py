import tkinter
import random

canvas = tkinter.Canvas(width="1000", height="600")
canvas.pack()

# stvorec
a = canvas.create_rectangle(100, 100, 130, 130, fill="red",tag="r")

# cierne veci
d_o = random.randrange(-200, 200)
h_o = d_o - 100 - random.randrange(-35, 50)
canvas.create_rectangle(400, 350 + d_o, 350, 600, fill="black", tag="b1")
canvas.create_rectangle(400, 0, 350, 200 + h_o, fill="black", tag="b2")



class g:
    canvas : tkinter.Canvas
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.canvas.bind_all("<Up>", self.u)
        self.canvas.bind_all("<Down>", self.d)
    
    def u(self, a):
        print("u")
        print(self.canvas.coords("r")[0], self.canvas.coords("r")[1])
        if self.canvas.coords("r")[1] > 5:
            self.canvas.move("r", 0, -5)
    
    def d(self, a):
        print("d")
        print(self.canvas.coords("r")[0], self.canvas.coords("r")[1])
        if self.canvas.coords("r")[1] < 600 :
            self.canvas.move("r", 0, 5)

while 1:
        canvas.move("b1", -10, 0)
        canvas.move("b2", -10, 0)
        canvas.after(200)
        canvas.update()  

g(canvas)
canvas.mainloop()

import tkinter
canvas = tkinter.Canvas(width=1000,height=600)
canvas.pack()

# Main pohyb
canvas.create_oval(50,75,20,25, width = 5, tag = "pi")
canvas.create_line(35,75,35,150, width = 5,tag = "pi")
canvas.create_line(35,150,45,180, width = 5,tag = "pi")
canvas.create_line(35,150,25,180, width = 5,tag = "pi")
canvas.create_line(35,150-75,25,150, width = 5,tag = "pi")
canvas.create_line(35,150-75,45,150, width = 5,tag = "pi")

# Semafor
canvas.create_rectangle(15,35,55,160, fill="gray")
canvas.create_line(35,75,35,250, width=10) 
canvas.create_oval(50,75,20,40,fill="red", tag="r")
canvas.create_oval(50,115,20,80, tag="o")
canvas.create_oval(50,155,20,120, tag="g")

# Cesta a auto
canvas.create_line (0, 250, 1000, 250, width=5)
canvas.create_line (0, 550, 1000, 550,width=5)
canvas.create_rectangle(700, 230, 900, 370, fill= "pink", tag= "c")
              
number=1
sem=1

while 1:
    if number == 1:
        if canvas.coords("pi")[2] < 800:
            canvas.move("pi", 5, 0)
            canvas.after(50)
            canvas.update()

        if canvas.coords("pi")[3] < 230 and canvas.coords("pi")[2] >= 800: 
            canvas.move("pi", 0, 5)
            canvas.after(50)
            canvas.update()

        if canvas.coords("pi")[3] >= 230 and canvas.coords("pi")[2] >= 800: 
            canvas.delete("pi")
            number = 0
    else:
        if sem == 1:

            if canvas.coords("c")[0] > 200:
                canvas.move("c", -5, 0)
                canvas.after(50)
                canvas.update()

            if canvas.coords("c")[0] <= 200:
                canvas.after(5000)
                canvas.update() 
                canvas.itemconfig("r", fill="gray")
                canvas.itemconfig("o", fill="orange")
                canvas.after(1000)
                canvas.update() 
                canvas.itemconfig("r", fill="gray")
                canvas.itemconfig("o", fill="gray")
                canvas.after(1000)
                canvas.update() 
                canvas.itemconfig("o", fill="black")
                canvas.itemconfig("g", fill="green")
                sem = 0
        #POHYB AUTA DALEJ        
        else:
            canvas.move("c", -5, 0)
            canvas.after(50)
            canvas.update()
                
tkinter.mainloop()

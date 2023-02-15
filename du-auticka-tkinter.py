import tkinter

def auticka():    
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
    canvas.create_line(35,75,35,250, width=10) 
    canvas.create_rectangle(15,35,55,160, fill="gray")
    canvas.create_oval(50,75,20,40,fill="red", tag="r")
    canvas.create_oval(50,115,20,80, tag="o")
    canvas.create_oval(50,155,20,120, tag="g")
    canvas.create_text(100, 100, text="červená", fill="red", tag="r_text")
    canvas.create_text(100, 140, text="oranžová", fill="orange", tag="o_text")
    canvas.create_text(100, 200, text="zelená", fill="green", tag="g_text")
    canvas.itemconfig("o_text", fill="white")
    canvas.itemconfig("g_text", fill="white")
    canvas.update()

    # Cesta a auto
    canvas.create_line (0, 250, 1000, 250, width=5)
    canvas.create_line (0, 550, 1000, 550,width=5)
    canvas.create_oval(700, 230, 900, 370, fill= "pink", tag= "c")
    canvas.create_oval(700, 355, 725, 325, fill="black", tag="c")
    canvas.create_oval(875, 355, 900, 325, fill="black", tag="c")
    # canvas.create_oval()
                
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
                    canvas.itemconfig("r_text", fill="white")
                    canvas.itemconfig("o_text", fill="orange")
                    canvas.after(1000)
                    canvas.update() 
                    canvas.itemconfig("r", fill="gray")
                    canvas.itemconfig("o", fill="orange")
                    canvas.itemconfig("o_text", fill="white")
                    canvas.itemconfig("g_text", fill="green")
                    canvas.after(1000)
                    canvas.update() 
                    canvas.itemconfig("o", fill="gray")
                    canvas.itemconfig("g", fill="green")
                    sem = 0
            #POHYB AUTA DALEJ        
            else:
                canvas.move("c", -5, 0)
                canvas.after(50)
                canvas.update()
                    
    tkinter.mainloop()

auticka()

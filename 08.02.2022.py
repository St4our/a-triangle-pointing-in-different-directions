from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import Tk, Canvas, Frame, BOTH

window = Tk()  
window.title("09-02-2022")  
window.geometry('670x200')

def niziver():
    root = Tk()
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))
    
    treug2=c.create_polygon([50,50],[420,50],[235,235], fill="red")
    treug=c.create_polygon([50,420],[420,420],[235,235], fill="red")
    root.mainloop()
    
 
def niz():
    root = Tk()
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))

    treug=c.create_polygon([50,420],[420,420],[235,235], fill="red")
    root.mainloop()

def ver():
    root = Tk()
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))

    treug=c.create_polygon([50,50],[420,50],[235,235], fill="red")
    root.mainloop()

def prav():
    root = Tk()
    #a= int(txt_a.get())
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))

    treug=c.create_polygon([50,50],[420,420],[420,50], fill="red")
    #line = c.create_line(50,50,a*42, a*42, width=4, fill="blue")
    #line2 = c.create_line(420,50,a*42, a*42, width=4, fill="blue")
    #line3 = c.create_line(50,450,a*42, a*42, width=4, fill="blue")
    root.mainloop()


def lev():
    root = Tk()
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))

    treug=c.create_polygon([50,50],[420,420],[50,420], fill="red")
    root.mainloop()

def dop1():
    root = Tk()
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))
    
    treug2=c.create_polygon([50,50],[50,420],[235,235], fill="red")
    treug=c.create_polygon([420,50],[420,420],[235,235], fill="red")
    root.mainloop()    
def dop2():
    root = Tk()
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))
    
    treug2=c.create_polygon([50,50],[50,420],[235,235], fill="red")

    root.mainloop()    
def dop3():
    root = Tk()
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))
    

    treug=c.create_polygon([420,50],[420,420],[235,235], fill="red")
    root.mainloop() 
def dop4():
    root = Tk()
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))

    treug=c.create_polygon([50,50],[50,420],[420,50], fill="red")

    root.mainloop()
def dop5():
    root = Tk()
    
    c = Canvas(root, width=700, height=700, bg="#e8f6fc")
    c.pack()
 
    c.create_rectangle(50, 50, 420, 420,
                       outline="#208211",
                       width=4,
                       activedash=(5, 4))

    treug=c.create_polygon([420,420],[50,420],[420,50], fill="red")

    root.mainloop()
#1
#текст
lbl_1 = Label(window, text="ВОООТ", font=("Arial Bold", 14), width=15)  
lbl_1.grid(column=0, row=0)


#______начало интервала______

lbl_a = Label(window, text="Число а", font=("Arial Bold", 12))  
lbl_a.grid(column=1, row=0)

txt_a=Entry(window,width=30, bg="#a5ff8f")  
txt_a.grid(column=2, row=0)
#______конец интервала______

lbl_b = Label(window, text="Цисло b", font=("Arial Bold", 12))  
lbl_b.grid(column=1, row=1)

txt_b=Entry(window,width=30, bg="#a5ff8f")  
txt_b.grid(column=2, row=1)


#кнопки

knopka1 = Button(window, text="Треугольник снизу", width=20, bg= 'blue', command=niz)  
knopka1.grid(column=0, row=3) 

knopka1 = Button(window, text="Треугольник сверху", width=20, bg= 'red', command=ver)  
knopka1.grid(column=1, row=3) 

knopka1 = Button(window, text="Треугольник вправо", width=20, bg= 'white', command=prav)  
knopka1.grid(column=2, row=3)

knopka1 = Button(window, text="Треугольник влево", width=20, bg= 'yellow', command=lev)  
knopka1.grid(column=3, row=3)

knopka1 = Button(window, text="Внизу и вверху", width=20, bg= 'orange', command=niziver)  
knopka1.grid(column=0, row=4)

knopka1 = Button(window, text="Еще1", width=20, bg= 'blue', command=dop1)  
knopka1.grid(column=1, row=4) 

knopka1 = Button(window, text="Еще2", width=20, bg= 'red', command=dop2)  
knopka1.grid(column=2, row=4) 

knopka1 = Button(window, text="Еще3", width=20, bg= 'white', command=dop3)  
knopka1.grid(column=3, row=4)

knopka1 = Button(window, text="Еще4", width=20, bg= 'yellow', command=dop4)  
knopka1.grid(column=0, row=5)

knopka1 = Button(window, text="Еще5", width=20, bg= 'orange', command=dop5)  
knopka1.grid(column=1, row=5)

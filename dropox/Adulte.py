from tkinter import *
from tkinter import ttk
def adulte():
    xs=Tk();xs.geometry("480x320+780+0");xs.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/corps.png")
    fond=ttk.Label(xs,image=img ).place(x=0,y=0)
    ############################### Boutton# fonction adulte et enfant à ajouter
    BP_A_M=Button(xs,text="Manuel",border=2,activebackground="#39a8ff",command=None,width=10,height=2, bg="#39a8ff",font=("Verdana Pro Cond Black",16))
    BP_A_M.place(x=50,y=100)
    BP_A_A=Button(xs,text="Auto",border=2,activebackground="#39a8ff",command=None,width=10,height=2, bg="#39a8ff",font=("Verdana Pro Cond Black",16,))
    BP_A_A.place(x=50,y=190)
    ############################## Titre
    C1 = Canvas(xs, width=300, height=35, bg='#ffe093')
    C1.place(x=5,y=5)
    t1 = Label(xs, text="Simulateur de Système Digestif",bg="#ffe093",fg="#611de8",justify = LEFT,font=("Tw Cen MT Condensed Extra Bold",16,'bold'))
    t1.place(x=14,y=7)
    ##############################
    xs.mainloop()


adulte()
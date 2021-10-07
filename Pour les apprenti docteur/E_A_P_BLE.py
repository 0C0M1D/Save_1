from tkinter import *
from tkinter import ttk

def BLE():
    global slide,img_close,img_open,BP_open
    BLE=Tk()
    BLE.geometry("480x320+780+0")
    #BLE.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(BLE,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton# fonction adulte et enfant à ajouter |
    img_BLE=PhotoImage(file="converti/—Pngtree—bluetooth vector icon_4019690 - Copie.png")

    BP_BLE=Button(BLE,borderwidth=0,image=img_BLE,activebackground="yellow",command=None,width=104,height=102, bg="#8d2000",fg="white")
    BP_BLE.place(x=5,y=100)

    ############################## Titre
    C1 = Canvas(BLE, width=465, height=35, bg='#ffe093')
    C1.place(x=7,y=5)
    t1 = Label(BLE, text="Simulateur de Système Digestif",bg="#ffe093",fg="#611de8",justify = LEFT,font=("Wide Latin",12,"bold"))
    t1.place(x=10,y=10)
    ############################## Bouton retour
    retour=PhotoImage(file="converti/304729 - Copie__01.png")
    retour_label=Label(image=retour)
    BP_retour=Button(BLE,image=retour,command=None,borderwidth=0,bg="#5a0d00",activebackground="#5a0d00")
    BP_retour.place(x=5,y=280)
    #############################
    t2=Label(BLE,fg="black",bg="white",width=20,height=5,font=("Serif",12))
    t2.place(x=110,y=103)
    t3=Label(BLE,fg="white",bg="black",width=20,height=5,font=("Serif",12))
    t3.place(x=290,y=103)


    BLE.mainloop()


BLE()
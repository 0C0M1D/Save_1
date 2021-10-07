from tkinter import *
from tkinter import ttk
import pygame

pygame.mixer.init()
pygame.mixer.music.load("")
def Param():
    global slide,img_close,img_open,BP_open,x,key,BP_E_M
    E_A_P=Tk()
    E_A_P.geometry("480x320+780+0")
    x=0
    key=2
    #E_A_P.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(E_A_P,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton# fonction adulte et enfant à ajouter |
    BP_E_M=Button(E_A_P, text="Continuer",borderwidth=0,border=10,activebackground="red",command=BP_Manuel,width=30,height=1, bg="#7f599f",fg="white",font=("Bauhaus 93",12))
    BP_E_M.place(x=100,y=270)

    ############################## Titre
    C1 = Canvas(E_A_P, width=465, height=35, bg='#ffe093')
    C1.place(x=7,y=5)
    t1 = Label(E_A_P, text="Simulateur de Système Digestif",bg="#ffe093",fg="#611de8",justify = LEFT,font=("Wide Latin",12,"bold"))
    t1.place(x=10,y=10)
    ############################## Bouton retour
    retour=PhotoImage(file="converti/304729 - Copie__01.png")
    retour_label=Label(image=retour)
    BP_retour=Button(E_A_P,image=retour,command=retour1,borderwidth=0,bg="#5a0d00",activebackground="#5a0d00")
    BP_retour.place(x=5,y=280)
    ############################# Scale
    slide=Scale(E_A_P,from_=-1, to=1, orient="vertical",troughcolor="black",bg="#5a0d00",activebackground="yellow",width=450,highlightbackground="yellow",sliderlength="50")
    slide.place(x=5,y=150)


    t2=Label(E_A_P, text="Les niveaux de vitesses:\n -Si -1:lent\n -Si 0:normal\n -Si 1:rapide",fg="black",bg="white",justify = LEFT,font=("Serif",12))
    t2.place(x=2,y=50)
    t3=Label(E_A_P, text="Appuie sur le cadenas si tout est finis\n et si tu veux changer appuie à nouveau",fg="black",bg="white",justify = LEFT,font=("Serif",12))
    t3.place(x=205,y=50)
    ############################# BP_Cadenas
    img_open=PhotoImage(file="converti/—P2gtree—golden lock icon_50033937.png")

    img_close=PhotoImage(file="converti/—P2gtree—golden lock icon_50031937.png")

    BP_open=Button(E_A_P,image=img_open,command=opcl,borderwidth=0,bg="#9d2700",activebackground="#9d2700",width=50,height=50)
    BP_open.place(x=408,y=265)
    E_A_P.mainloop()

def opcl():
    global x,key
    slide.config(state=DISABLED)
    BP_open.config(image=img_close)

    key=2
    x+=1

    key-=1
    if x==2:
        slide.config(state=NORMAL)
        BP_open.config(image=img_open)
        x-=2
        key-=1
        #slide.state(DISABLED)
        #slide(state=DISABLED)
def retour1():
    print("test")



def BP_Manuel():
    global BP_E_M
    if key==1:

        BP_E_M.config(text="Nice :)",bg="green")
    else:
        BP_E_M.config(text="il faut chosir",bg="red")
Param()
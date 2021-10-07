from tkinter import *
from tkinter import ttk

def enfants():
    qs=Tk()
    qs.geometry("480x320+780+0")
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/GCDGFVH - Copie.png")
    fond=Label(qs,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton# fonction adulte et enfant à ajouter |
    BP_E_M=Button(qs,text="Manuel",borderwidth=0,border=10,activebackground="red",command= lambda x=0:test(qs, x),width=10,height=1, bg="#a6ff8a",font=("Bauhaus 93",12))
    BP_E_M.place(x=330,y=190)
    BP_E_A=Button(qs,text="Auto",borderwidth=0,border=10,activebackground="#39ceff",command=None,width=10,height=1, bg="#a6d1ff",font=("Bauhaus 93",12))
    BP_E_A.place(x=330,y=265)
    ############################## Titre
    C1 = Canvas(qs, width=470, height=35, bg='#ffe093')
    C1.place(x=5,y=5)
    t1 = Label(qs, text="Simulateur de Système Digestif",bg="#ffe093",fg="#611de8",justify = LEFT,font=("Wide Latin",12,"bold"))
    t1.place(x=15,y=10)
    ############################## Bouton retour
    retour=PhotoImage(file="converti/304729 - Copie__01.png")
    retour_label=Label(image=retour)
    BP_retour=Button(qs,image=retour,command=None,borderwidth=0,bg="#eae6da",activebackground="#eae6da")
    BP_retour.place(x=0,y=280)

    qs.mainloop()

enfants()
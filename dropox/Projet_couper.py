"""
Sommaire
    ###################
    # Originale--Menu #
    ###################

    #####################
    # Originale--Adulte #
    #####################
        ##########################
        # Originale--Adulte.Menu #
        ##########################
            ###############################
            # Originale--Adulte.Menu.Auto #
            ###############################
            #################################
            # Originale--Adulte.Menu.Manuel #
            #################################

    #####################
    # Originale--Enfant #
    #####################
        ##########################
        # Originale--Enfant.Menu #
        ##########################
            ###############################
            # Originale--Enfant.Menu.Auto #
            ###############################
            #################################
            # Originale--Enfant.Menu.Manuel #
            #################################
"""
from tkinter import *
from tkinter import ttk
import time
import pygame
import os
#os.chdir permet de répertorier le dossier
os.chdir("C:/Users/0iacu/OneDrive/Bureau/Développement/python/guizero/projet_BCC/fond/dropox/")


v = 1
n=1
pygame.mixer.pre_init
pygame.mixer.init()




###################
# Originale--Menu #
###################
def test(a, b):
    a.destroy()
    if b == 0:
        menu()
    elif b == 1:
        adulte()
    elif b == 2:
        enfant()
    elif b == 3:
        BLE()


def menu():
    os = Tk()
    os.geometry("480x320+780+0")
    os.overrideredirect(1)
    ###############################
    img = PhotoImage(file="converti/modif1.png")
    fond = Label(os, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton# fonction adulte et enfant à ajouter
    # Potentiel problème, trouver comment stocker et importer une police d'écriture lisible par python
    BP_A = Button(os,text="Adulte",borderwidth=0,border=10,font=("Tw Cen MT Condensed Extra Bold", 12),activebackground="red",command=lambda x=1: test(os, x),width=10,height=2,bg="#b01638")
    BP_A.place(x=40, y=235)
    BP_E = Button(os,text="Enfant",borderwidth=0,border=10,activebackground="#39ceff",command=lambda x=2: test(os, x), width=10,height=2,bg="#39ceff",font=("Tw Cen MT Condensed Extra Bold", 12) )
    BP_E.place(x=250, y=235)
    ############################## Titre
    C1 = Canvas(os, width=467, height=35, bg="#ffe093")
    C1.place(x=5, y=5)
    t1 = Label(os,text="Simulateur de Système Digestif",bg="#ffe093",fg="#611de8",justify=LEFT,font=("Tw Cen MT Condensed Extra Bold", 18, "bold"))
    t1.place(x=40, y=6)
    ##############################
    os.mainloop()



#####################
# Originale--Adulte #
#####################
##########################
# Originale--Adulte.Menu #
##########################
# Pour retirer les bordure de la fenetre
# os.overrideredirect(1)
def test_adulte(a, b):
    a.destroy()
    if b == 1:
        Param_A()
    elif b == 2:
        AM_auto1()
    elif b == 3:
        base_auto_A()


def adulte():
    pygame.mixer.music.stop()
    xs = Tk()
    xs.geometry("480x320+780+0")
    xs.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/maintenance.png")
    fond = ttk.Label(xs, image=img).place(x=0, y=0)
    ############################### Boutton# fonction adulte et enfant à ajouter
    BP_A_M = Button(
        xs,
        text="Manuel",
        border=2,
        activebackground="#39a8ff",
        command=lambda x=3: test_adulte(xs, x),
        width=10,
        height=2,
        bg="#39a8ff",
        font=("Verdana Pro Cond Black", 16),
    )
    BP_A_M.place(x=50, y=100)
    BP_A_A = Button(
        xs,
        text="Auto",
        border=2,
        activebackground="#39a8ff",
        command=lambda x=1: test_adulte(xs, x),
        width=10,
        height=2,
        bg="#39a8ff",
        font=(
            "Verdana Pro Cond Black",
            16,
        ),
    )
    BP_A_A.place(x=50, y=190)
    ############################## Titre
    C1 = Canvas(xs, width=300, height=35, bg="#ffe093")
    C1.place(x=5, y=5)
    t1 = Label(
        xs,
        text="Simulateur de Système Digestif",
        bg="#ffe093",
        fg="#611de8",
        justify=LEFT,
        font=("Tw Cen MT Condensed Extra Bold", 16, "bold"),
    )
    t1.place(x=14, y=7)
    ############################## Bouton retour
    retour = PhotoImage(file="converti/304729 - Copie__01.png")
    retour_label = Label(image=retour)
    BP_retour = Button(
        xs,
        image=retour,
        command=lambda x=1 - 1: test(xs, x),
        borderwidth=0,
        bg="#0c3b8b",
        activebackground="#0c3b8b",
    )
    BP_retour.place(x=5, y=280)

    xs.mainloop()


##########################
# Originale--Enfant.Menu #
##########################
def test_enfant(a, b):
    a.destroy()
    if b == 1:
        Param()
    elif b == 2:
        E_auto1
    elif b == 3:
        base_auto()


def enfant():
    pygame.mixer.music.stop()
    qs = Tk()
    qs.geometry("480x320+780+0")
    # Pour retirer les bordure de la fenetre
    qs.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/GCDGFVH - Copie.png")
    fond = Label(qs, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton# fonction adulte et enfant à ajouter |
    BP_E_M = Button(
        qs,
        text="Manuel",
        borderwidth=0,
        border=10,
        activebackground="red",
        command=lambda x=3: test_enfant(qs, x),
        width=10,
        height=1,
        bg="#a6ff8a",
        font=("Bauhaus 93", 12),
    )
    BP_E_M.place(x=330, y=190)
    BP_E_A = Button(
        qs,
        text="Auto",
        borderwidth=0,
        border=10,
        activebackground="#39ceff",
        command=lambda x=1: test_enfant(qs, x),
        width=10,
        height=1,
        bg="#a6d1ff",
        font=("Bauhaus 93", 12),
    )
    BP_E_A.place(x=330, y=265)
    ############################## Titre
    C1 = Canvas(qs, width=467, height=35, bg="#ffe093")
    C1.place(x=5, y=5)

    t1 = Label(
        qs,
        text="Simulateur de Système Digestif",
        bg="#ffe093",
        fg="#611de8",
        justify=LEFT,
        font=("Wide Latin", 12, "bold"),
    )
    t1.place(x=10, y=10)
    ############################## Bouton retour
    retour = PhotoImage(file="converti/304729 - Copie__01.png")
    retour_label = Label(image=retour)
    BP_retour = Button(
        qs,
        image=retour,
        command=lambda x=0: test(qs, x),
        borderwidth=0,
        bg="#eae6da",
        activebackground="#eae6da",
    )
    BP_retour.place(x=0, y=280)

    qs.mainloop()


###############################
# Originale--Enfant.Menu.Auto #
###############################
########################## Partie réglage de la vitesse de lecture
def Param():  # AUTO
    global slide, img_close, img_open, BP_open, x, key, BP_E_M, E_A_P,u
    E_A_P = Tk()
    E_A_P.geometry("480x320+780+0")
    x = 0
    u=0
    key = 2
    E_A_P.overrideredirect(1)
    v = 1


    # Pour retirer les bordure de la fenetre
    # os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond = Label(E_A_P, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton# fonction adulte et enfant à ajouter |
    BP_E_M = Button(
        E_A_P,
        text="Continuer",
        borderwidth=0,
        border=10,
        activebackground="red",
        command=BP_Manuel,
        width=30,
        height=1,
        bg="#7f599f",
        fg="white",
        font=("Bauhaus 93", 12),
    )
    BP_E_M.place(x=100, y=270)

    ############################## Titre
    C1 = Canvas(E_A_P, width=465, height=35, bg="#39ceff")
    C1.place(x=7, y=5)
    t1 = Label(
        E_A_P,
        text="Auto",
        bg="#39ceff",
        fg="black",
        justify=LEFT,
        font=("Wide Latin", 15, "bold"),
    )
    t1.place(x=200, y=10)
    ############################## Bouton retour
    retour = PhotoImage(file="converti/304729 - Copie__01.png")
    retour_label = Label(image=retour)
    BP_retour = Button(
        E_A_P,
        image=retour,
        command=retour1,
        borderwidth=0,
        bg="#5a0d00",
        activebackground="#5a0d00",
    )
    BP_retour.place(x=5, y=280)
    ############################# Scale
    slide = Scale(
        E_A_P,
        from_=-1,
        to=1,
        command=lancer,
        orient="vertical",
        troughcolor="black",
        bg="#5a0d00",
        activebackground="yellow",
        width=450,
        highlightbackground="yellow",
        sliderlength="50",
    )
    slide.place(x=5, y=150)
    BP_stop = Button(E_A_P, text="Stop Song", font=("Snap ITC", 15), command=ohlalal_stop)
    BP_stop.place(x=275, y=100)

    t2 = Label(
        E_A_P,
        text="Les niveaux de vitesses:\n -Si -1:lent\n -Si 0:normal\n -Si 1:rapide",
        fg="black",
        bg="white",
        justify=LEFT,
        font=("Serif", 12),
    )
    t2.place(x=2, y=50)
    t3 = Label(
        E_A_P,
        text="Appuie sur le cadenas si tout est finis\n et si tu veux changer appuie à nouveau",
        fg="black",
        bg="white",
        justify=LEFT,
        font=("Serif", 12),
    )
    t3.place(x=205, y=50)
    ############################# BP_Cadenas
    img_open = PhotoImage(file="converti/—P2gtree—golden lock icon_50033937.png")
    label_open = Label(image=img_open)
    img_close = PhotoImage(file="converti/—P2gtree—golden lock icon_50031937.png")
    label_close = Label(image=img_close)
    BP_open = Button(E_A_P,image=img_open,command=opcl,borderwidth=0,bg="#8c2000",activebackground="#8c2000",width=50,height=50,)
    BP_open.place(x=408, y=265)
    E_A_P.mainloop()

def ge_A():
    global u
    pygame.mixer.music.stop()

    u+=1

    if l==1:
        if u==2:
            u-=2
            test_enfant(auto_E,1)
    elif l==2:
        if u==2:
            u-=2
            test_enfant(auto_E,1)
    elif l==3:
        if u==2:
            u-=2
            test_enfant(auto_E,1)
    elif l==4:
        if u==2:
            u-=2
            test_enfant(auto_E,1)
    elif l==5:
        if u==2:
            u-=2
            test_enfant(auto_E,1)
    elif l==6:
        if u==2:
            u-=2
            test_enfant(auto_E,1)
    elif l==7:
        if u==2:
            u-=2
            test_enfant(auto_E,1)
    elif l==8:
        if u==2:
            u-=2
            test_enfant(auto_E,1)
def opcl():
    global x, key
    slide.config(state=DISABLED)
    BP_open.config(image=img_close)
    key = 2
    x += 1
    key -= 1
    if x == 2:
        slide.config(state=NORMAL)
        BP_open.config(image=img_open)
        x -= 2
        key -= 1
        # slide.state(DISABLED)
        # slide(state=DISABLED)


def retour1():

    test(E_A_P, 2)


def BP_Manuel():
    global BP_E_M
    if key == 1:
        #      print(key)

        auto__EM(E_A_P, 0)
    else:
        BP_E_M.config(text="il faut chosir", bg="red")


def lancer(b):
    global v

    if b == "-1":
        pygame.mixer.music.load("converti/audio/au cas ou/slow--smb_world_clear.wav")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        v = 1
    elif b == "0":
        pygame.mixer.music.load("converti/audio/au cas ou/smb_world_clear.wav")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        v = 2
    elif b == "1":
        pygame.mixer.music.load("converti/audio/au cas ou/speed--smb_world_clear.wav")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        v = 3





def auto__EM(a, b):
    a.destroy()
    if b == 0:
        EM_auto1()
    elif b == 1:
        EM_auto2()
    elif b == 2:
        EM_auto3()
    elif b == 3:
        EM_auto4()
    elif b == 4:
        EM_auto5()
    elif b == 5:
        EM_auto6()
    elif b == 6:
        EM_auto7()
    elif b == 7:
        EM_auto8()


def EM_auto1():

    global bouche,l,u,auto_E
    l=1
    if u==1:
        u-=1
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E = Tk()
    auto_E.geometry("480x320+780+0")
    auto_E.overrideredirect(1)
    bouche = 1
    audio_cplt()
    # auto_E.overrideredirect(1)
    # Pour retirer les bordure de la fenetre
    # os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond = Label(auto_E, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton#
    img_onoff = PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite = PhotoImage(file="converti/g.png")
    BP_onoff = Button(
        auto_E,
        borderwidth=0,
        image=img_onoff,
        bg="#dc5300",
        activebackground="#dc5300",
        command=ge_A,
        width=37,
        height=35,
    )
    BP_droite = Button(
        auto_E,
        borderwidth=0,
        image=img_droite,
        activebackground="#8d2000",
        command=lambda x=1: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_onoff.place(x=375, y=5)
    BP_droite.place(x=25, y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg="#39ceff")
    C1.place(x=125, y=5)
    t1 = Label(
        auto_E,
        text="Auto -- Bouche",
        bg="#39ceff",
        fg="black",
        justify=LEFT,
        font=("Wide Latin", 10, "bold"),
    )
    t1.place(x=155, y=12)
    ############################## Lorem ipsumn
    lorem = "Cavité située au bas du visage humain, communiquant avec l'appareil digestif et avec les voies respiratoires ."

    fram1 = Frame(auto_E)
    fram1.place(x=5, y=70, width=473, height=240)

    scrollbar = Scrollbar(fram1)
    scrollbar.pack(side=RIGHT, fill=Y)

    texte0 = Text(fram1, yscrollcommand=scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED);texte0.config(state=DISABLED);texte0.config(state=DISABLED)

    scrollbar.config(command=texte0.yview)



    tst = PhotoImage(file="converti/g.png")
    can_tst = Canvas(fram1, width=50, height=50, yscrollcommand=scrollbar.set)
    can_tst.create_image(140, 20, image=tst)
    can_tst.place(x=100, y=200)

    can_tst.config(yscrollcommand=scrollbar.set)
    can_tst.pack(side=LEFT, expand=True)



    auto_E.mainloop()


def EM_auto2():
    global Oesophage,l,u,auto_E
    l=2
    if u==1:
        u-=1
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E = Tk()
    auto_E.geometry("480x320+780+0")
    auto_E.overrideredirect(1)
    Oesophage = 1
    audio_cplt()
    # auto_E.overrideredirect(1)
    # Pour retirer les bordure de la fenetre
    # os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond = Label(auto_E, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton#
    img_onoff = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_4145409.png"
    )
    img_droite = PhotoImage(file="converti/g.png")
    img_gauche = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png"
    )
    BP_onoff = Button(
        auto_E,
        borderwidth=0,
        image=img_onoff,
        activebackground="#dc5300",
        command=ge_A,
        width=37,
        height=35,
        bg="#dc5300",
    )
    BP_droite = Button(
        auto_E,
        borderwidth=0,
        image=img_droite,
        activebackground="#8d2000",
        command=lambda x=2: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_gauche = Button(
        auto_E,
        borderwidth=0,
        image=img_gauche,
        activebackground="#8d2000",
        command=lambda x=0: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_onoff.place(x=375, y=5)
    BP_droite.place(x=60, y=5)
    BP_gauche.place(x=20, y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg="#39ceff")
    C1.place(x=125, y=5)
    t1 = Label(
        auto_E,
        text="Auto -- Oesophage",
        bg="#39ceff",
        fg="black",
        justify=LEFT,
        font=("Wide Latin", 10, "bold"),
    )
    t1.place(x=135, y=12)
    ############################## Lorem ipsumn
    lorem = " L'œsophage est le segment du tube digestif qui relie le pharynx au cardia de l'estomac ."
    fram1 = Frame(auto_E)
    fram1.place(x=5, y=70, width=473, height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack(side=RIGHT, fill=Y)
    texte0 = Text(fram1, yscrollcommand=scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command=texte0.yview)
    tst = PhotoImage(file="converti/g.png")
    can_tst = Canvas(fram1, width=50, height=50, yscrollcommand=scrollbar.set)
    can_tst.create_image(140, 20, image=tst)
    can_tst.place(x=100, y=200)

    can_tst.config(yscrollcommand=scrollbar.set)
    can_tst.pack(side=LEFT, expand=True)


    auto_E.mainloop()


def EM_auto3():
    global Intestin,l,u,auto_E
    Intestin = 1
    l=3
    if u==1:
        u-=1
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E = Tk()
    auto_E.geometry("480x320+780+0")
    auto_E.overrideredirect(1)
    audio_cplt()
    # auto_E.overrideredirect(1)
    # Pour retirer les bordure de la fenetre
    # os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond = Label(auto_E, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton#
    img_onoff = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_4145409.png"
    )
    img_droite = PhotoImage(file="converti/g.png")
    img_gauche = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png"
    )
    BP_onoff = Button(
        auto_E,
        borderwidth=0,
        image=img_onoff,
        activebackground="#dc5300",
        command=ge_A,
        width=37,
        height=35,
        bg="#dc5300",
    )
    BP_droite = Button(
        auto_E,
        borderwidth=0,
        image=img_droite,
        activebackground="#8d2000",
        command=lambda x=3: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_gauche = Button(
        auto_E,
        borderwidth=0,
        image=img_gauche,
        activebackground="#8d2000",
        command=lambda x=1: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_onoff.place(x=375, y=5)
    BP_droite.place(x=60, y=5)
    BP_gauche.place(x=20, y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg="#39ceff")
    C1.place(x=125, y=5)
    t1 = Label(
        auto_E,
        text="Auto -- Intestin",
        bg="#39ceff",
        fg="black",
        justify=LEFT,
        font=("Wide Latin", 10, "bold"),
    )
    t1.place(x=155, y=12)
    ############################## Lorem ipsumn
    lorem = "L'intestin est la partie de l'appareil digestif qui débute à l'estomac et se termine au côlon. Encore appelé gros intestin, c'est une sorte de tube torsadé serpentant à l'intérieur de l'abdomen sur plusieurs mètres. "
    fram1 = Frame(auto_E)
    fram1.place(x=5, y=70, width=473, height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack(side=RIGHT, fill=Y)
    texte0 = Text(fram1, yscrollcommand=scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command=texte0.yview)
    tst = PhotoImage(file="converti/g.png")
    can_tst = Canvas(fram1, width=50, height=50, yscrollcommand=scrollbar.set)
    can_tst.create_image(140, 20, image=tst)
    can_tst.place(x=100, y=200)

    can_tst.config(yscrollcommand=scrollbar.set)
    can_tst.pack(side=LEFT, expand=True)


    auto_E.mainloop()


def EM_auto4():
    global Pancreas,l,u,auto_E
    Pancreas = 1
    l=4
    if u==1:
        u-=1
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E = Tk()
    auto_E.geometry("480x320+780+0")
    auto_E.overrideredirect(1)
    audio_cplt()
    # auto_E.overrideredirect(1)
    # Pour retirer les bordure de la fenetre
    # os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond = Label(auto_E, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton#
    img_onoff = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_4145409.png"
    )
    img_droite = PhotoImage(file="converti/g.png")
    img_gauche = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png"
    )
    BP_onoff = Button(
        auto_E,
        borderwidth=0,
        image=img_onoff,
        activebackground="#dc5300",
        command=ge_A,
        width=37,
        height=35,
        bg="#dc5300",
    )
    BP_droite = Button(
        auto_E,
        borderwidth=0,
        image=img_droite,
        activebackground="#8d2000",
        command=lambda x=4: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_gauche = Button(
        auto_E,
        borderwidth=0,
        image=img_gauche,
        activebackground="#8d2000",
        command=lambda x=2: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_onoff.place(x=375, y=5)
    BP_droite.place(x=60, y=5)
    BP_gauche.place(x=20, y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg="#39ceff")
    C1.place(x=125, y=5)
    t1 = Label(
        auto_E,
        text="Auto -- Pancréas",
        bg="#39ceff",
        fg="black",
        justify=LEFT,
        font=("Wide Latin", 10, "bold"),
    )
    t1.place(x=145, y=12)

    ############################## Lorem ipsumn
    lorem = "Organe glandulaire situé dans l'abdomen, au-dessous et en arrière de l'estomac, qui sécrète le suc pancréatique (déversé dans l'intestin pour servir à la digestion) ainsi que deux hormones, l'insuline et le glucagon, excrétées dans le sang pour la régulation du métabolisme du glucose."
    fram1 = Frame(auto_E)
    fram1.place(x=5, y=70, width=473, height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack(side=RIGHT, fill=Y)
    texte0 = Text(fram1, yscrollcommand=scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command=texte0.yview)
    tst = PhotoImage(file="converti/g.png")
    can_tst = Canvas(fram1, width=50, height=50, yscrollcommand=scrollbar.set)
    can_tst.create_image(140, 20, image=tst)
    can_tst.place(x=100, y=200)

    can_tst.config(yscrollcommand=scrollbar.set)
    can_tst.pack(side=LEFT, expand=True)

    auto_E.mainloop()


def EM_auto5():
    global Foie,l,u,auto_E
    Foie = 1
    l=5
    if u==1:
        u-=1
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E = Tk()
    auto_E.geometry("480x320+780+0")
    auto_E.overrideredirect(1)
    audio_cplt()
    # auto_E.overrideredirect(1)
    # Pour retirer les bordure de la fenetre
    # os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond = Label(auto_E, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton#
    img_onoff = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_4145409.png"
    )
    img_droite = PhotoImage(file="converti/g.png")
    img_gauche = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png"
    )
    BP_onoff = Button(
        auto_E,
        borderwidth=0,
        image=img_onoff,
        activebackground="#dc5300",
        command=ge_A,
        width=37,
        height=35,
        bg="#dc5300",
    )
    BP_droite = Button(
        auto_E,
        borderwidth=0,
        image=img_droite,
        activebackground="#8d2000",
        command=lambda x=5: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_gauche = Button(
        auto_E,
        borderwidth=0,
        image=img_gauche,
        activebackground="#8d2000",
        command=lambda x=3: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_onoff.place(x=375, y=5)
    BP_droite.place(x=60, y=5)
    BP_gauche.place(x=20, y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg="#39ceff")
    C1.place(x=125, y=5)
    t1 = Label(
        auto_E,
        text="Auto -- Foie",
        bg="#39ceff",
        fg="black",
        justify=LEFT,
        font=("Wide Latin", 10, "bold"),
    )
    t1.place(x=175, y=12)
    ############################## Lorem ipsumn
    lorem = "Le foie est la plus volumineuse des glandes annexes du tube digestif. Il est doté d'une double fonction : il excrète la bile nécessaire à la digestion et joue un rôle dans le métabolisme du glucose, des protéines et de la coagulation. "
    fram1 = Frame(auto_E)
    fram1.place(x=5, y=70, width=473, height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack(side=RIGHT, fill=Y)
    texte0 = Text(fram1, yscrollcommand=scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command=texte0.yview)
    tst = PhotoImage(file="converti/g.png")
    can_tst = Canvas(fram1, width=50, height=50, yscrollcommand=scrollbar.set)
    can_tst.create_image(140, 20, image=tst)
    can_tst.place(x=100, y=200)

    can_tst.config(yscrollcommand=scrollbar.set)
    can_tst.pack(side=LEFT, expand=True)

    auto_E.mainloop()


def EM_auto6():
    global Cordon_bleu,l,u,auto_E
    Cordon_bleu = 1
    l=6
    if u==1:
        u-=1
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E = Tk()
    auto_E.geometry("480x320+780+0")
    auto_E.overrideredirect(1)
    audio_cplt()
    # auto_E.overrideredirect(1)
    # Pour retirer les bordure de la fenetre
    # os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond = Label(auto_E, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton#
    img_onoff = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_4145409.png"
    )
    img_droite = PhotoImage(file="converti/g.png")
    img_gauche = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png"
    )
    BP_onoff = Button(
        auto_E,
        borderwidth=0,
        image=img_onoff,
        activebackground="#dc5300",
        command=ge_A,
        width=37,
        height=35,
        bg="#dc5300",
    )
    BP_droite = Button(
        auto_E,
        borderwidth=0,
        image=img_droite,
        activebackground="#8d2000",
        command=lambda x=6: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_gauche = Button(
        auto_E,
        borderwidth=0,
        image=img_gauche,
        activebackground="#8d2000",
        command=lambda x=4: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_onoff.place(x=375, y=5)
    BP_droite.place(x=60, y=5)
    BP_gauche.place(x=20, y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=240, height=40, bg="#39ceff")
    C1.place(x=125, y=5)
    t1 = Label(
        auto_E,
        text="|Auto|\n Cordon ombilicale",
        bg="#39ceff",
        fg="black",
        justify=CENTER,
        font=("Wide Latin", 10),
    )
    t1.place(x=135, y=7)
    ############################## Lorem ipsumn
    lorem = "Le cordon ombilical est une sorte de tuyau qui relie le bébé au ventre de sa mère lorsqu'il est encore dedans. C'est par là que passent les nutriments nécessaires à l'enfant pour son bon développement. Il est nourri par les échanges de sang qui passe dans le cordon."
    fram1 = Frame(auto_E)
    fram1.place(x=5, y=70, width=473, height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack(side=RIGHT, fill=Y)
    texte0 = Text(fram1, yscrollcommand=scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command=texte0.yview)
    tst = PhotoImage(file="converti/g.png")
    can_tst = Canvas(fram1, width=50, height=50, yscrollcommand=scrollbar.set)
    can_tst.create_image(140, 20, image=tst)
    can_tst.place(x=100, y=200)

    can_tst.config(yscrollcommand=scrollbar.set)
    can_tst.pack(side=LEFT, expand=True)

    auto_E.mainloop()


def EM_auto7():
    global Estomac,l,u,auto_E
    Estomac = 1
    l=7
    if u==1:
        u-=1
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E = Tk()
    auto_E.geometry("480x320+780+0")
    auto_E.overrideredirect(1)
    audio_cplt()
    # auto_E.overrideredirect(1)
    # Pour retirer les bordure de la fenetre
    # os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond = Label(auto_E, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton#
    img_onoff = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_4145409.png"
    )
    img_droite = PhotoImage(file="converti/g.png")
    img_gauche = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png"
    )
    BP_onoff = Button(
        auto_E,
        borderwidth=0,
        image=img_onoff,
        activebackground="#dc5300",
        command=ge_A,
        width=37,
        height=35,
        bg="#dc5300",
    )
    BP_droite = Button(
        auto_E,
        borderwidth=0,
        image=img_droite,
        activebackground="#8d2000",
        command=lambda x=7: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_gauche = Button(
        auto_E,
        borderwidth=0,
        image=img_gauche,
        activebackground="#8d2000",
        command=lambda x=5: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_onoff.place(x=375, y=5)
    BP_droite.place(x=60, y=5)
    BP_gauche.place(x=20, y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg="#39ceff")
    C1.place(x=125, y=5)
    t1 = Label(
        auto_E,
        text="Auto -- Estomac",
        bg="#39ceff",
        fg="black",
        justify=LEFT,
        font=("Wide Latin", 10, "bold"),
    )
    t1.place(x=150, y=12)
    ############################## Lorem ipsumn
    lorem = "L'estomac est une sorte de poche située à l'intérieur du ventre, dans le haut de l'abdomen. Il est situé tout de suite après l'œsophage.Dans l'estomac se déroulent plusieurs étapes importantes de la digestion."
    fram1 = Frame(auto_E)
    fram1.place(x=5, y=70, width=473, height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack(side=RIGHT, fill=Y)
    texte0 = Text(fram1, yscrollcommand=scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command=texte0.yview)
    tst = PhotoImage(file="converti/g.png")
    can_tst = Canvas(fram1, width=50, height=50, yscrollcommand=scrollbar.set)
    can_tst.create_image(140, 20, image=tst)
    can_tst.place(x=100, y=200)

    can_tst.config(yscrollcommand=scrollbar.set)
    can_tst.pack(side=LEFT, expand=True)

    auto_E.mainloop()


def EM_auto8():
    global Vessie,l,u,auto_E
    l=8
    if u==1:
        u-=1
    Vessie = 1
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E = Tk()
    auto_E.geometry("480x320+780+0")
    auto_E.overrideredirect(1)
    audio_cplt()
    # auto_E.overrideredirect(1)
    # Pour retirer les bordure de la fenetre
    # os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img = PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond = Label(auto_E, image=img)
    fond.place(x=0, y=0)
    ############################### Boutton#
    img_onoff = PhotoImage(
        file="converti/—Pngtree—simple coral gradient button element_4145409.png"
    )
    img_droite = PhotoImage(file="converti/g.png")
    img_gauche = PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff = Button(
        auto_E,
        borderwidth=0,
        image=img_onoff,
        activebackground="#dc5300",
        command=ge_A,
        width=37,
        height=35,
        bg="#dc5300",
    )
    BP_droite = Button(
        auto_E,
        borderwidth=0,
        image=img_droite,
        activebackground="#8d2000",
        command=lambda x=2: test(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_gauche = Button(
        auto_E,
        borderwidth=0,
        image=img_gauche,
        activebackground="#8d2000",
        command=lambda x=6: auto__EM(auto_E, x),
        width=37,
        height=35,
        bg="#8d2000",
    )
    BP_onoff.place(x=375, y=5)
    BP_droite.place(x=60, y=5)
    BP_gauche.place(x=20, y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg="#39ceff")
    C1.place(x=125, y=5)
    t1 = Label(
        auto_E,
        text="Auto -- Vessie",
        bg="#39ceff",
        fg="black",
        justify=LEFT,
        font=("Wide Latin", 10, "bold"),
    )
    t1.place(x=155, y=12)
    ############################## Lorem ipsumn
    lorem = "La vessie est l'organe du système urinaire dont la fonction est de recevoir l'urine terminale produite par les reins puis de la conserver avant son évacuation au cours de la miction."
    fram1 = Frame(auto_E)
    fram1.place(x=5, y=70, width=473, height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack(side=RIGHT, fill=Y)
    texte0 = Text(fram1, yscrollcommand=scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command=texte0.yview)
    tst = PhotoImage(file="converti/g.png")
    can_tst = Canvas(fram1, width=50, height=50, yscrollcommand=scrollbar.set)
    can_tst.create_image(140, 20, image=tst)
    can_tst.place(x=100, y=200)

    can_tst.config(yscrollcommand=scrollbar.set)
    can_tst.pack(side=LEFT, expand=True)

    auto_E.mainloop()


#################################
# Originale--Enfant.Menu.Manuel #
#################################


def auto__E(a,b):####Du coup il manque le BLE et la lecture de doc
    global n
    a.destroy()
    if b == 0:
        E_auto1()
    elif b == 1:
        E_auto2()
    elif b==2:
        E_auto3()
    elif b==3:
        E_auto4()
    elif b==4:
        E_auto5()
    elif b==5:
        E_auto6()
    elif b==6:
        E_auto7()
    elif b==7:
        E_auto8()
    elif b==8:
        if n==1:
            ohlalal_stop()
            n-=1
        base_auto()
def base_auto():
    global t,o
    o=0
    t=Tk()
    n=0
    t.geometry("480x320+780+0")
    t.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(t,image=img)
    fond.place(x=0,y=0)
    ############################## Bouton retour
    retour=PhotoImage(file="converti/304729 - Copie__01.png")
    retour_label=Label(image=retour)
    BP_retour=Button(t,image=retour,command= lambda x=0:test(t, x),borderwidth=0,bg="#5a0d00",activebackground="#5a0d00")
    BP_retour.place(x=5,y=280)
    ############################## BP
    BP1=Button(t,borderwidth=0,text="Bouche",bg="#ffe093",activebackground="#ffe093",command=lambda x=0:auto__E(t,x),width=25,height=2)
    BP2=Button(t,borderwidth=0,text="Œsophage",bg="#ffe093",activebackground="#ffe093",command=lambda x=1:auto__E(t,x),width=25,height=2)
    BP3=Button(t,borderwidth=0,text="Intestin",bg="#ffe093",activebackground="#ffe093",command=lambda x=2:auto__E(t,x),width=25,height=2)
    BP4=Button(t,borderwidth=0,text="Pancréas",bg="#ffe093",activebackground="#ffe093",command=lambda x=3:auto__E(t,x),width=25,height=2)
    BP5=Button(t,borderwidth=0,text="Fœtus",bg="#ffe093",activebackground="#ffe093",command=lambda x=4:auto__E(t,x),width=25,height=2)
    BP6=Button(t,borderwidth=0,text="Cordon ombilicale",bg="#ffe093",activebackground="#ffe093",command=lambda x=5:auto__E(t,x),width=25,height=2)
    BP7=Button(t,borderwidth=0,text="Estomac",bg="#ffe093",activebackground="#ffe093",command=lambda x=6:auto__E(t,x),width=25,height=2)
    BP8=Button(t,borderwidth=0,text="Vessie",bg="#ffe093",activebackground="#ffe093",command=lambda x=7:auto__E(t,x),width=25,height=2)
    BP1.place(x=60,y=90)
    BP2.place(x=60,y=130)
    BP3.place(x=60,y=170)
    BP4.place(x=60,y=210)
    BP5.place(x=250,y=90)
    BP6.place(x=250,y=130)
    BP7.place(x=250,y=170)
    BP8.place(x=250,y=210)
    #############################
    C1 = Canvas(t, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(t, text="Manuel",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=200,y=12)
    #############################
    C2 = Canvas(t, width=231, height=35, bg='white')
    C2.place(x=125,y=285)
    t2 = Label(t, text="Une fois lancer Double tap sur\n le bouton pause pour exit",bg="white",fg="black",justify = CENTER,font=("Verdana",8))
    t2.place(x=155,y=288)
    t.mainloop()
def ge():
    global o
    pygame.mixer.music.stop()

    o+=1

    if z==1:
        if o==2:
            o-=2
            auto__E(auto_E1,8)
    elif z==2:
        if o==2:
            o-=2
            auto__E(auto_E2,8)
    elif z==3:
        if o==2:
            o-=2
            auto__E(auto_E3,8)
    elif z==4:
        if o==2:
            o-=2
            auto__E(auto_E4,8)
    elif z==5:
        if o==2:
            o-=2
            auto__E(auto_E5,8)
    elif z==6:
        if o==2:
            o-=2
            auto__E(auto_E6,8)
    elif z==7:
        if o==2:
            o-=2
            auto__E(auto_E7,8)
    elif z==8:
        if o==2:
            o-=2
            auto__E(auto_E8,8)
def retour2():
    #Modif pour faire retour avec bp retour sur ecran original.enfant.menu
    test(t,2)
def E_auto1():
    global auto_E1,z,o
    z=1
    if o==1:
        o-=1

    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E1=Tk()
    auto_E1.geometry("480x320+780+0")
    pygame.mixer.music.load("converti/audio/Organes/Bouche/slow.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    auto_E1.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E1,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    BP_onoff=Button(auto_E1,borderwidth=0,image=img_onoff,bg="#dc5300",activebackground="#dc5300",command=ge,width=37,height=35)
    BP_droite=Button(auto_E1,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=1:auto__E(auto_E1,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=25,y=5)
    ############################## Titre
    C1 = Canvas(auto_E1, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E1, text="Manuel -- Bouche",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=140,y=12)
    ############################## Lorem ipsumn
    lorem="Cavité située au bas du visage humain, communiquant avec l'appareil digestif et avec les voies respiratoires"
    fram1=Frame(auto_E1)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E1.mainloop()
def E_auto2():
    global auto_E2,z,o
    if o==1:
        o-=1
    z=2
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E2=Tk()
    auto_E2.geometry("480x320+780+0")
    pygame.mixer.music.load("converti/audio/Organes/Oesophage/slow.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    auto_E2.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E2,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E2,borderwidth=0,image=img_onoff,activebackground="#dc5300",command=ge,width=37,height=35, bg="#dc5300")
    BP_droite=Button(auto_E2,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=2:auto__E(auto_E2,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E2,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=0:auto__E(auto_E2,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E2, width=231, height=40, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E2, text="|Manuel|\n Oesophage",bg="#39ceff",fg="black",justify = CENTER,font=("Wide Latin",10,"bold"))
    t1.place(x=165,y=7)
    ############################## Lorem ipsumn
    lorem="L'œsophage est le segment du tube digestif qui relie le pharynx au cardia de l'estomac ."
    fram1=Frame(auto_E2)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E2.mainloop()
def E_auto3():
    global auto_E3,z,o
    if o==1:
        o-=1
    z=3


    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E3=Tk()
    auto_E3.geometry("480x320+780+0")
    pygame.mixer.music.load("converti/audio/Organes/Intestin/slow.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    auto_E3.overrideredirect(1)
    #Pour retirer les bordure de la fenetre

    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E3,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E3,borderwidth=0,image=img_onoff,activebackground="#dc5300",command=ge,width=37,height=35, bg="#dc5300")
    BP_droite=Button(auto_E3,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=3:auto__E(auto_E3,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E3,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=1:auto__E(auto_E3,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E3, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E3, text="Manuel -- Intestin",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=135,y=12)
    ############################## Lorem ipsumn
    lorem="L'intestin est la partie de l'appareil digestif qui débute à l'estomac et se termine au côlon. Encore appelé gros intestin, c'est une sorte de tube torsadé serpentant à l'intérieur de l'abdomen sur plusieurs mètres. "
    fram1=Frame(auto_E3)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E3.mainloop()
def E_auto4():
    global auto_E4,z,o
    if o==1:
        o-=1
    z=4
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E4=Tk()
    auto_E4.geometry("480x320+780+0")
    pygame.mixer.music.load("converti/audio/Organes/Pancreas/slow.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    auto_E4.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E4,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E4,borderwidth=0,image=img_onoff,activebackground="#dc5300",command=ge,width=37,height=35, bg="#dc5300")
    BP_droite=Button(auto_E4,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=4:auto__E(auto_E4,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E4,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=2:auto__E(auto_E4,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E4, width=234, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E4, text="Manuel -- Pancréas",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=127,y=12)

    ############################## Lorem ipsumn
    lorem="Organe glandulaire situé dans l'abdomen, au-dessous et en arrière de l'estomac, qui sécrète le suc pancréatique (déversé dans l'intestin pour servir à la digestion) ainsi que deux hormones, l'insuline et le glucagon, excrétées dans le sang pour la régulation du métabolisme du glucose."
    fram1=Frame(auto_E4)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E4.mainloop()
def E_auto5():
    global auto_E5,z,o
    if o==1:
        o-=1
    z=5


    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E5=Tk()
    auto_E5.geometry("480x320+780+0")
    pygame.mixer.music.load("converti/audio/Organes/Foie/slow.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    auto_E5.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E5,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E5,borderwidth=0,image=img_onoff,activebackground="#dc5300",command=ge,width=37,height=35, bg="#dc5300")
    BP_droite=Button(auto_E5,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=5:auto__E(auto_E5,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E5,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=3:auto__E(auto_E5,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E5, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E5, text="Manuel -- Foie",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=155,y=12)
    ############################## Lorem ipsumn
    lorem="Le foie est la plus volumineuse des glandes annexes du tube digestif. Il est doté d'une double fonction : il excrète la bile nécessaire à la digestion et joue un rôle dans le métabolisme du glucose, des protéines et de la coagulation."
    fram1=Frame(auto_E5)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E5.mainloop()
def E_auto6():
    global auto_E6,z,o
    if o==1:
        o-=1
    z=6
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E6=Tk()
    auto_E6.geometry("480x320+780+0")
    pygame.mixer.music.load("converti/audio/Organes/Cordon_bleu/slow.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    auto_E6.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E6,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E6,borderwidth=0,image=img_onoff,activebackground="#dc5300",command=ge,width=37,height=35, bg="#dc5300")
    BP_droite=Button(auto_E6,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=6:auto__E(auto_E6,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E6,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=4:auto__E(auto_E6,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E6, width=240, height=40, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E6,text="|Manuel|\n Cordon ombilicale",bg="#39ceff",fg="black",justify = CENTER,font=("Wide Latin",10))
    t1.place(x=135,y=7)
    ############################## Lorem ipsumn
    lorem="Le cordon ombilical est une sorte de tuyau qui relie le bébé au ventre de sa mère lorsqu'il est encore dedans. C'est par là que passent les nutriments nécessaires à l'enfant pour son bon développement. Il est nourri par les échanges de sang qui passe dans le cordon."
    fram1=Frame(auto_E6)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E6.mainloop()
def E_auto7():
    global auto_E7,z,o
    if o==1:
        o-=1
    z=7

    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E7=Tk()
    auto_E7.geometry("480x320+780+0")
    pygame.mixer.music.load("converti/audio/Organes/Estomac/slow.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    auto_E7.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E7,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E7,borderwidth=0,image=img_onoff,activebackground="#dc5300",command=ge,width=37,height=35, bg="#dc5300")
    BP_droite=Button(auto_E7,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=7:auto__E(auto_E7,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E7,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=5:auto__E(auto_E7,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E7, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E7, text="Manuel -- Estomac",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=130,y=12)
    ############################## Lorem ipsumn
    lorem="L'estomac est une sorte de poche située à l'intérieur du ventre, dans le haut de l'abdomen. Il est situé tout de suite après l'œsophage.Dans l'estomac se déroulent plusieurs étapes importantes de la digestion."
    fram1=Frame(auto_E7)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E7.mainloop()
def E_auto8():
    global auto_E8,z,o,n
    if o==1:
        o-=1
    z=8


    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E8=Tk()
    auto_E8.geometry("480x320+780+0")
    pygame.mixer.music.load("converti/audio/Organes/Vessie/slow.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    auto_E8.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E8,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E8,borderwidth=0,image=img_onoff,activebackground="#dc5300",command=ge,width=37,height=35, bg="#dc5300")
    BP_droite=Button(auto_E8,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=8:auto__E(auto_E8,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E8,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=6:auto__E(auto_E8,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E8, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E8, text="Manuel -- Vessie",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=150,y=12)
    ############################## Lorem ipsumn
    lorem="La vessie est l'organe du système urinaire dont la fonction est de recevoir l'urine terminale produite par les reins puis de la conserver avant son évacuation au cours de la miction."
    fram1=Frame(auto_E8)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side=LEFT, fill=BOTH);texte0.config(state=DISABLED)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E8.mainloop()

def audio_cplt():
    global bouche,Oesophage,Intestin,Pancreas,Foie,Cordon_bleu,Estomac,Vessie,sortie_audio
    if bouche== 1:
        if v==1:

            pygame.mixer.music.load("converti/audio/Organes/Bouche/slow.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()

        elif v==2:

            pygame.mixer.music.load("converti/audio/Organes/Bouche/normal.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()

        elif v==3:

            pygame.mixer.music.load("converti/audio/Organes/Bouche/speed.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        bouche-=1
        sortie_audio=1

    elif Oesophage== 1:

        if v==1:

            pygame.mixer.music.load("converti/audio/Organes/Oesophage/slow.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()


        elif v==2:
            pygame.mixer.music.load("converti/audio/Organes/Oesophage/normal.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()

        elif v==3:
            pygame.mixer.music.load("converti/audio/Organes/Oesophage/speed.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        Oesophage-=1
        sortie_audio=1

    elif Intestin== 1:
        if v==1:
            pygame.mixer.music.load("converti/audio/Organes/Intestin/slow.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()

        elif v==2:
            pygame.mixer.music.load("converti/audio/Organes/Intestin/normal.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()

        elif v==3:
            pygame.mixer.music.load("converti/audio/Organes/Intestin/speed.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        Intestin-=1
        sortie_audio=1

    elif Pancreas== 1:
        if v==1:
            pygame.mixer.music.load("converti/audio/Organes/Pancreas/slow.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()

        elif v==2:
            pygame.mixer.music.load("converti/audio/Organes/Pancreas/normal.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        elif v==3:
            pygame.mixer.music.load("converti/audio/Organes/Pancreas/speed.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        Pancreas-=1
        sortie_audio=1

    elif Foie== 1:
        if v==1:
            pygame.mixer.music.load("converti/audio/Organes/Foie/slow.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        elif v==2:
            pygame.mixer.music.load("converti/audio/Organes/Foie/normal.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        elif v==3:
            pygame.mixer.music.load("converti/audio/Organes/Foie/speed.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        Foie-=1
        sortie_audio=1
    elif Cordon_bleu== 1:
        if v==1:
            pygame.mixer.music.load("converti/audio/Organes/Cordon_bleu/slow.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        elif v==2:
            pygame.mixer.music.load("converti/audio/Organes/Cordon_bleu/normal.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        elif v==3:
            pygame.mixer.music.load("converti/audio/Organes/Cordon_bleu/speed.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        Cordon_bleu-=1
        sortie_audio=1
    elif Estomac== 1:
        if v==1:
            pygame.mixer.music.load("converti/audio/Organes/Estomac/slow.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        elif v==2:
            pygame.mixer.music.load("converti/audio/Organes/Estomac/normal.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        elif v==3:
            pygame.mixer.music.load("converti/audio/Organes/Estomac/speed.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        Estomac-=1
        sortie_audio=1
    elif Vessie== 1:
        if v==1:
            pygame.mixer.music.load("converti/audio/Organes/Vessie/slow.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        elif v==2:
            pygame.mixer.music.load("converti/audio/Organes/Vessie/normal.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        elif v==3:
            pygame.mixer.music.load("converti/audio/Organes/Vessie/speed.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
        Vessie-=1
        sortie_audio=1

def ohlalal_stop():
    pygame.mixer.music.stop()


if __name__ == "__main__":
    menu()
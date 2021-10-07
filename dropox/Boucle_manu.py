from tkinter import *
from tkinter import ttk
import time
import os
#os.chdir permet de répertorier le dossier
os.chdir("C:/Users/0iacu/OneDrive/Bureau/Développement/python/guizero/projet_BCC/fond/dropox/")
def auto__E(a,b):####Du coup il manque le BLE et la lecture de doc
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
        base_auto()
def base_auto():
    global t,o
    o=0
    t=Tk()
    t.geometry("480x320+780+0")

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

    print(o)
    o+=1
    print(o)
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
def retour1():
    #Modif pour faire retour avec bp retour sur ecran original.enfant.menu
    test(t,2)
def E_auto1():
    global auto_E1,z
    z=1
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E1=Tk()
    auto_E1.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
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
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E1)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side =LEFT, fill =BOTH)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E1.mainloop()
def E_auto2():
    global auto_E2,z
    z=2

    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E2=Tk()
    auto_E2.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
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
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E2)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side =LEFT, fill =BOTH)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E2.mainloop()
def E_auto3():
    global auto_E3,z
    z=3
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E3=Tk()
    auto_E3.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
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
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E3)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side =LEFT, fill =BOTH)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E3.mainloop()
def E_auto4():
    global auto_E4,z
    z=4
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E4=Tk()
    auto_E4.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
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
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E4)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side =LEFT, fill =BOTH)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E4.mainloop()
def E_auto5():
    global auto_E5,z
    z=5
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E5=Tk()
    auto_E5.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
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
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E5)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side =LEFT, fill =BOTH)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E5.mainloop()
def E_auto6():
    global auto_E6,z
    z=6
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E6=Tk()
    auto_E6.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
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
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E6)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side =LEFT, fill =BOTH)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E6.mainloop()
def E_auto7():
    global auto_E7,z
    z=7
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E7=Tk()
    auto_E7.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
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
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E7)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side =LEFT, fill =BOTH)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E7.mainloop()
def E_auto8():
    global auto_E8,z
    z=8
    ##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E8=Tk()
    auto_E8.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
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
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E8)
    fram1.place(x=5,y=70,width=473,height=240)
    scrollbar = Scrollbar(fram1)
    scrollbar.pack( side = RIGHT, fill = Y )
    texte0 =Text(fram1, yscrollcommand =scrollbar.set)
    texte0.insert(END, lorem)
    texte0.pack(side =LEFT, fill =BOTH)
    scrollbar.config(command =texte0.yview)
    tst=PhotoImage(file="converti/g.png")
    can_tst=Canvas(fram1,width=50,height=50,yscrollcommand =scrollbar.set)
    can_tst.create_image(140,20, image=tst)
    can_tst.place(x=100,y=200)

    can_tst.config(yscrollcommand =scrollbar.set)
    can_tst.pack(side =LEFT, expand =True)



    auto_E8.mainloop()
base_auto()
from tkinter import *
from tkinter import ttk

def auto__E(a,b):
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
        E_auto9()
def E_auto1():
##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E=Tk()
    auto_E.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    BP_onoff=Button(auto_E,borderwidth=0,image=img_onoff,bg="green",activebackground="#d25000",command=None,width=37,height=35)
    BP_droite=Button(auto_E,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=1:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=25,y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E, text="Auto -- Bouche",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=155,y=12)
    ############################## Lorem ipsumn
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E)
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



    auto_E.mainloop()

def E_auto2():
##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E=Tk()
    auto_E.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E,borderwidth=0,image=img_onoff,activebackground="#d25000",command=None,width=37,height=35, bg="yellow")
    BP_droite=Button(auto_E,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=2:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=0:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E, text="Auto -- Oesophage",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=135,y=12)
    ############################## Lorem ipsumn
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E)
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



    auto_E.mainloop()





def E_auto3():
##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E=Tk()
    auto_E.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E,borderwidth=0,image=img_onoff,activebackground="#d25000",command=None,width=37,height=35, bg="blue")
    BP_droite=Button(auto_E,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=3:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=1:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E, text="Auto -- Intestin",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=155,y=12)
    ############################## Lorem ipsumn
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E)
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



    auto_E.mainloop()



def E_auto4():
##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E=Tk()
    auto_E.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E,borderwidth=0,image=img_onoff,activebackground="#d25000",command=None,width=37,height=35, bg="darkblue")
    BP_droite=Button(auto_E,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=4:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=2:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E, text="Auto -- Pancréas",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=145,y=12)

    ############################## Lorem ipsumn
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E)
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



    auto_E.mainloop()




def E_auto5():
##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E=Tk()
    auto_E.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E,borderwidth=0,image=img_onoff,activebackground="#d25000",command=None,width=37,height=35, bg="gray")
    BP_droite=Button(auto_E,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=5:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=3:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E, text="Auto -- Foie",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=175,y=12)
    ############################## Lorem ipsumn
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E)
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



    auto_E.mainloop()




def E_auto6():
##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E=Tk()
    auto_E.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E,borderwidth=0,image=img_onoff,activebackground="#d25000",command=None,width=37,height=35, bg="pink")
    BP_droite=Button(auto_E,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=6:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=4:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=240, height=40, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E,text="Auto\n Cordon ombilicale",bg="#39ceff",fg="black",justify = CENTER,font=("Wide Latin",10))
    t1.place(x=135,y=7)
    ############################## Lorem ipsumn
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E)
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



    auto_E.mainloop()




def E_auto7():
##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E=Tk()
    auto_E.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E,borderwidth=0,image=img_onoff,activebackground="#d25000",command=None,width=37,height=35, bg="black")
    BP_droite=Button(auto_E,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=7:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=5:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E, text="Auto -- Estomac",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=150,y=12)
    ############################## Lorem ipsumn
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E)
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



    auto_E.mainloop()



def E_auto8():
##################j'arrive pas à placer d'image en dessous du texte dans la frame
    auto_E=Tk()
    auto_E.geometry("480x320+780+0")
    #auto_E.overrideredirect(1)
    #Pour retirer les bordure de la fenetre
    #os.overrideredirect(1)
    ############################### Permet de couper coller une image sur une autre
    img=PhotoImage(file="converti/Orange - Fond iPhone.png")
    fond=Label(auto_E,image=img )
    fond.place(x=0,y=0)
    ############################### Boutton#
    img_onoff=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_4145409.png")
    img_droite=PhotoImage(file="converti/g.png")
    img_gauche=PhotoImage(file="converti/—Pngtree—simple coral gradient button element_41245409 (1).png")
    BP_onoff=Button(auto_E,borderwidth=0,image=img_onoff,activebackground="#d25000",command=None,width=37,height=35, bg="white")
    BP_droite=Button(auto_E,borderwidth=0,image=img_droite,activebackground="#8d2000",command=lambda x=8:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_gauche=Button(auto_E,borderwidth=0,image=img_gauche,activebackground="#8d2000",command=lambda x=6:auto__E(auto_E,x),width=37,height=35, bg="#8d2000")
    BP_onoff.place(x=375,y=5)
    BP_droite.place(x=60,y=5)
    BP_gauche.place(x=20,y=5)
    ############################## Titre
    C1 = Canvas(auto_E, width=231, height=35, bg='#39ceff')
    C1.place(x=125,y=5)
    t1 = Label(auto_E, text="Auto -- Vessie",bg="#39ceff",fg="black",justify = LEFT,font=("Wide Latin",10,"bold"))
    t1.place(x=155,y=12)
    ############################## Lorem ipsumn
    lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel est magna. Vivamus auctor consequat lorem in tempor. Pellentesque sagittis facilisis quam sit amet elementum. Donec non mauris nec nibh bibendum malesuada. Morbi sagittis, enim vel tristique ornare, velit nisl consectetur magna, vitae faucibus neque lacus at ex. Vestibulum gravida facilisis blandit. Sed mauris tortor, tincidunt ut finibus vitae, eleifend non turpis. Donec ac sem interdum, feugiat purus vitae, elementum leo. Proin vitae tristique augue. Nulla non dui cursus, tempus nibh ultricies, congue velit. Proin risus massa, finibus vitae viverra a, posuere sed ante.

    Suspendisse non est vel tellus auctor mattis. Mauris sit amet mi ullamcorper, rutrum tellus non, porttitor enim. Donec condimentum vitae leo sit amet ullamcorper. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque ut leo lacinia, ultricies tortor sit amet, tincidunt urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sagittis pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin sit amet dignissim felis. Sed fringilla odio eget mi malesuada, vel varius sapien blandit. Fusce posuere neque non feugiat feugiat. Nunc gravida, sem condimentum auctor lacinia, elit sem laoreet ligula, id elementum elit ante vel lacus. Mauris et consequat nisi, in interdum velit.

    Vestibulum pharetra purus nec est posuere, quis aliquet magna malesuada. Integer quis tellus vitae est convallis facilisis nec non purus. Donec nec ligula gravida, pharetra ante ut, commodo mauris. Donec hendrerit consequat lorem, vel bibendum sapien pretium vel. In at libero ante. Mauris quis blandit tortor. Mauris venenatis orci sed viverra sollicitudin. Sed eu egestas libero, nec condimentum massa.

    Fusce dolor libero, faucibus id porta non, fringilla ultrices massa. Maecenas tincidunt urna in ex pharetra elementum. Phasellus tempor aliquam nulla, eget interdum nisi commodo a. Aliquam tincidunt ex at odio aliquam, id commodo leo posuere. Sed at neque luctus, ultricies felis id, porttitor tellus. Aenean vel hendrerit arcu. Maecenas sagittis eros eu risus finibus feugiat. Etiam iaculis rutrum leo in elementum.

    Nunc blandit facilisis dui nec fermentum. Nunc sit amet erat risus. Suspendisse bibendum ultrices lorem. Sed facilisis luctus odio, a ultricies magna volutpat non. Nulla facilisi. Nam vestibulum hendrerit lacus vel sollicitudin. Ut imperdiet lorem tellus, a dictum risus varius ut. Sed eget nisl tristique, pharetra odio non, venenatis quam. Suspendisse suscipit diam et ex pulvinar suscipit. Sed feugiat metus at eros malesuada, a porta nulla sollicitudin. Aliquam tempus justo sem, pellentesque vulputate elit ultrices in.

    """
    fram1=Frame(auto_E)
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



    auto_E.mainloop()






























E_auto1()
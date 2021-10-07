import random
b=random.randint(1,100)
print(b)
a=int(input("Veuillez taper un nb compris entre 0 à 100 : "))
essai=0 
while(a!=b):

   

    if(a==b):
        print("BRAVO !!! :")
        
        
        
    elif(a >b):
          print('C est loupe mais le nb est Inferieur x) ')
          essai+=1
          a=int(input("Ressayer 1 à 100 : "))
    else:
         print('Dommage le nb est superieur ;)')
         essai+=1
         a=int(input("Ressayer 1 à 100 : "))

         

print ("Nb :",essai,"essai")
    


            


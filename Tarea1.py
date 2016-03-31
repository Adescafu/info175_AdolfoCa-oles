import sys
import string
from Tkinter import *

def encrypt(palabra,n):
    caja=list(palabra)
    abecedario=string.ascii_lowercase
    caja_dos=list(abecedario)
    final=""
    
    for i in range(len(caja)):
        if caja[i]==" ":
            final=final+" "
        for j in  range(len(caja_dos)):
            if caja[i]==caja_dos[j]:
                final=final+caja_dos[j+n]
                
    print len(caja_dos)           
    return final
    
"""palabra=raw_input("ingrese una palabra: ")
n=input("ingrese un numero: ")
print encrypt(palabra,n)"""

def encryptdos(palabra):
    palabra=palabra.lower()
    final= ""
    for elem in palabra:
        if elem == 'c':
            final=final+'p'
        elif elem == 'p':
            final=final+'c'
        elif elem == 'o':
            final=final+'e'
        elif elem == 'e':
            final=final+'o'
        elif elem == 'l':
            final=final+'n'
        elif elem == 'n':
            final=final+'l'
        elif elem == 'a':
            final=final+'i'
        elif elem == 'i':
            final=final+'a'
        elif elem == 'r':
            final=final+'t'
        elif elem == 't':
            final=final+'r'
        else:
            final=final+elem
   
    return final

"""palabra=raw_input("ingrese una palabra: ")
print encryptdos(palabra)"""




raiz = Tk()
raiz.title("Encriptacion de frases")

vp = Frame(raiz)
vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

etiqueta = Label(vp,text="Ingrese una frase a encriptar: ")
etiqueta.grid(column=1,row=1,)

etiqueta = Label(vp,text="numero de desplazamiento: ")
etiqueta.grid(column=1,row=3,)

palabra=""
entrada_txt = Entry(vp,width=10,textvariable=palabra)
entrada_txt.grid(column=2,row=1)

num=0
entrada_txt = Entry(vp,width=10,textvariable=num)
entrada_txt.grid(column=2,row=3)

boton = Button(vp,text="Encriptar!",command=encrypt(palabra,num))
boton.grid(column=2,row=80)



raiz.mainloop()


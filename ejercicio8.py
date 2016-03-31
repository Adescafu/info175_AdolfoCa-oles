import string
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
    
palabra=raw_input("ingrese una palabra: ")
n=input("ingrese un numero: ")
print encrypt(palabra,n)

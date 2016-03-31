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

palabra=raw_input("ingrese una palabra: ")
print encryptdos(palabra)

from cosas import *

def main():
    l1= libro.libro_planeta("El perfume", autor("Patrick","PS"), 1980)
    #Cambiar seudonimo
    l1.autor.pseudonimo = l1.autor.seudonimo.lower()
    print(l1)
    print("------------Herencia--------------")
    al2 = Alumno("Jose", 19, "318203", "ICO", 9)
    print(vars(al2))
main()
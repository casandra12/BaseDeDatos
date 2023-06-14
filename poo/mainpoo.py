from cosas import alumno

def main():
    """
    al1 = alumno()
    print (al1)
    al2 = alumno ()
    print(al1.facultad)
    print(al2.facultad)
    print(alumno.facultad)

    print(".....")
    al1.facultad = "fes aragon EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(alumno.facultad)
    print(" un vistazo a los objetos")
    print(vars(al1))
    print(vars(al2))
    print(" modificar atributos ")
    all.edad = 999
    print(vars(al1))
    print(vars(al2))
    """
    al1= alumno("diego", 19, "ICO")
    al2 = alumno("monse", 20, "derecho")
    print(vars(al1))
    al1.__edad = 333
    print (al1.__edad)
    print(vars(al1))

main()








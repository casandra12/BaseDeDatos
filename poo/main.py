from cosas import alumno, perro

def main():
    al1 = alumno("monse", 19, "ico")
    print(vars(al1))
    al1.__nombre = "monse "
    print(vars(al1))
    al1.set_nombre("diego")
    print(vars(al1))
    print("------to string-------")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(5)
    print("------perro-------")
    perro1= perro("poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "de la calle"
    print(vars(perro1))
    perro1.__raza = "otra"
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.43
    print(perro1)
    cachoro = perro.es_cachorro(perro1.edad)
    print(cachoro)
    perro.dormir()
    danes = perro.perro_grande(0.8)
    print(danes)


main()
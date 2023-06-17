from COSAS import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(per1.descripcion)

    print("-----------Herencia-alumno----------------")
    al1 = Alumno("Jose", 19, "318203", "ICO")
    print(al1)
    print(al1.descripcion + "\n-------------------------------------")

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("--------------herencia-profesor-----------------")
    prof1 = Profesor("Jesus", 30+16, 654136, "Ingenieria de software")
    print(prof1)
    prof1.dormir()

    print("--------------Herencia-ayudante-prof-------------------")
    ayt1 = Ayudante_profesor("Adrian", 20, "2415324", "ICO", "2554635", "Ingenieria software", 4)
    print(ayt1)
    ayt1.dormir()
    ayt1.nombre = "Juancho"
    ayt1.dar_clase("POO")
    print(ayt1)

main()
class Alumno:
    numAlumnos = 0
    sumaNotas = 0
    def __init__(self, name, nota):
        self.name = name
        self.nota = nota
        Alumno.numAlumnos += 1
        Alumno.sumaNotas += nota
    def mostrarNombreNota(self):
        return self.name, self.nota
    def mostrarNumAlumnos(self):
        return(Alumno.numAlumnos)
    def mostrarSumNotas(self):
        return(Alumno.sumaNotas)
    def mostrarNotaMedia(self):
        if Alumno.numAlumnos > 0:
            return(Alumno.sumaNotas/Alumno.numAlumnos)
        else:
            return('NO hay alumnos')


alumno1 = Alumno('juan', 51)
alumno2 = Alumno('pepe', 60)
alumno3 = Alumno('ramiro', 70)
alumno4 = Alumno('pedro', 80)
print(alumno1.mostrarNombreNota(), alumno1.numAlumnos)
print(alumno2.mostrarNombreNota(), alumno1.sumaNotas)
print(alumno3.mostrarNombreNota(), alumno1.mostrarNotaMedia())
alumno1


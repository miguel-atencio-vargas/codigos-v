class Complejo:
    def __init__(self, parteReal, parteImaginaria):
        self.r = parteReal
        self.i = parteImaginaria
x = Complejo(3.0, -4.5)
print(x.r, x.i)

class Perro:
    tipo = 'canino'
    def __init__(self, nombre):
        self.nombre = nombre
d = Perro('perkins')
e = Perro('lucho')

print(d.nombre, d.tipo)
print(e.nombre, e.tipo)
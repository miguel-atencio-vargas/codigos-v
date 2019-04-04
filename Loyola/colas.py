""" 
colas.py 

Inteligencia Artificial, tercer curso INGENIERIA DE SISTEMAS -
UNIVERSIDAD LOYOLA.


Definición de clases para Pilas (LIFO),Colas (FIFO) y Colas con prioridad. 


El código que se usa en este módulo está basado principalmente en el código
Python que se proporciona con el libro "Artificial Intelligence: A Modern
Approach" de S. Russell y P. Norvig (http://code.google.com/p/aima-python,
módulo utils.py). """

import bisect # Necesario para las listas con prioridad

class Cola:
    """Clase abstracta/interfaz para colas de tres tipos:
        PilaLIFO(): Pilas
        ColaFIFO(): Colas.
        ColaPrioridad(orden, f): Colas ordenadas según f.
    Cualquiera de ellos soporta los siguientes métodos y funciones:
        q.append(item)  -- incluir un elemento en la cola q
        q.extend(items) -- equivalente a: for x in items: q.append(x)
        q.pop()         -- devuelve (y lo quita) el primero de la cola
        len(q)          -- número de elementos en q (also q.__len())
        item in q       -- responde a la pregunta ¿item está en q?
        
    En el caso particular de PilaLIFO(), no será una instance de Cola, ya que
    directamente usaremos listas. Las otras dos sí serán definidas como
    subclase de esta clase Cola."""

    def __init__(self):
        abstract

    def extend(self, items):
        for item in items: self.append(item)

def PilaLIFO():
    """Devuelve la lista vacía, que tomaremos como una pila LIFO vacía."""
    return []

class ColaFIFO(Cola):
    """Definición de colas 'primero que entra, primero que sale'.  Se usan
    listas y la cola que representan es la que se forma si se recorre la lista
    de izquierda a derecha. Para eliminar un elemento de la cola, simplemente
    consideramos que el inicio de la cola cambia a la siguiente posición a la
    derecha. Para ello, llevamos un contador con el índice que indica el
    comienzo de la cola, y lo incrementaremos cuando se hace pop().  A partir de
    cinco, eliminamos la "basura" cuando más de la mitad de la lista esté
    eliminada (para ello, reemplazamos la lista por la sublista de los
    elementos "vivos")."""
    
    def __init__(self):
        self.A = []
        self.comienzo = 0

    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.comienzo

    def extend(self, items):
        self.A.extend(items)

    def pop(self):
        e = self.A[self.comienzo]
        self.comienzo += 1
        if self.comienzo > 5 and self.comienzo > len(self.A)/2:
            self.A = self.A[self.comienzo:]
            self.comienzo = 0
        return e

    def __contains__(self, item):
        return item in self.A[self.comienzo:]

    def __str__(self):
        return str(self.A[self.comienzo:])
        
class ColaPrioridad(Cola):
    """Cola ordenada respecto a un valor dado por una función f, que la clase
    tiene como atributo de dato. Admite orden creciente (min) y orden
    decreciente (max). Si el orden es min, el método pop devuelve y elimina el
    elemento de la cola con menor f(x). Si el orden es max, devuelve y elimina
    el de mayor f(x). En realidad, los elementos quie se guardan en la cola
    son tuplas (f(x),x). En Python, las tuplas se comparan lexicográficamente,
    así que se mantendrán ordenadas por su valor f(x). La pertenencia a la
    cola (x in C) se comprueba con x e ignorando f(x). Soporta además acceso
    como en diccionarios, ignorando igualmente el valor de f(x)"""


    def __init__(self, orden=min, f=lambda x: x):
        self.A=[]
        self.orden=orden 
        self.f=f

    def append(self, item): 
        bisect.insort(self.A, (self.f(item), item))

    def __len__(self):
        return len(self.A)

    def pop(self):
        if self.orden == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]

    def __contains__(self, item):
        for (_, x) in self.A:
            if x == item: return True
        return False

    def __getitem__(self, clave):
        for _, item in self.A:
            if item == clave:
                return item

    def __delitem__(self, clave):
        for i, (valor, item) in enumerate(self.A):
            if item == clave:
                self.A.pop(i)
                return

    def __str__(self):
        return str(self.A)

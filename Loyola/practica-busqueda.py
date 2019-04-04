# practica ALGORITMOS DE BUSQUEDA
# Inteligencia Artificial, tercer curso INGENIERIA DE SISTEMAS -
# Universidad Loyola.
# Luis Lorgio

# Práctica 1: Búsqueda
# ====================

# En esta práctica se verá la implementación en Python de los principales
# algoritmos de búsqueda vistos en clase. Veremos cómo se comportan con el
# problema del 8 puzzle, también visto en clase. La práctica tiene tres partes
# bien diferenciadas:

# Parte I: Representación de problemas de espacios de estados. Veremos una
# técnica general para hacerlo, y en particular se implementará el problema del
# ocho puzzle.

# Parte II: Algoritmos de búsqueda en espacios de estados. Veremos algunos
# patrones genéricos de búsqueda, y cómo los algorimos vistos en clase son casos
# particulares de esos algoritmos genéricos. 

# Parte III: Experimentación con los algoritmos implementados. Se comprobarán
# algunas propiedades de los algoritmos, usándolos para resolución de problemas
# de ocho puzzle.


# El código que se usa en esta práctica está basado principalmente en el
# código Python que se proporciona con el libro "Artificial Intelligence: A
# Modern Approach" de S. Russell y P. Norvig
# (http://code.google.com/p/aima-python, módulo search.py). Las modificaciones
# al código (algunas para adaptarlo a Python 3)




# Necesitaremos el siguiente módulo "colas" que se proporciona con la
# práctica:
from colas import *


#===============================================
# PARTE I. REPRESENTACIÓN DE ESPACIOS DE ESTADOS
#===============================================



# Recuérdese que según lo que se ha visto en clase, la implementación de la
# representación de un problema de espacio de estados consiste en:

# * Representar estados y acciones mediante una estructura de datos.
# * Definir: estado_inicial, es_estado_final(_), acciones(_), aplica(_,_) y
#   coste_de_aplicar_accion, si el problema tiene coste.

# La siguiente clase Problema representa este esquema general de cualquier
# problema de espacio de estados. Un problema concreto será una subclase de
# Problema, y requerirá implementar acciones, aplica y eventualmente __init__,
# es_estado_final y  coste_de_aplicar_accion. 


class Problema(object):
    """Clase abstracta para un problema de espacio de estados. Los problemas
    concretos habría que definirlos como subclases de Problema, implementando
    acciones, aplica y eventualmente __init__, es_estado_final y
    coste_de_aplicar_accion. Una vez hecho esto, se han de crear instancias de
    dicha subclase, que serán la entrada a los distintos algoritmos de
    resolución mediante búsqueda."""  


    def __init__(self, estado_inicial, estado_final=None):
        """El constructor de la clase especifica el estado inicial y
        puede que un estado_final, si es que es único. Las subclases podrían
        añadir otros argumentos"""
        
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final

    def acciones(self, estado):
        """Devuelve las acciones aplicables a un estado dado. Lo normal es
        que aquí se devuelva una lista, pero si hay muchas se podría devolver
        un iterador, ya que sería más eficiente."""
        abstract

    def aplica(self, estado, accion):
        """ Devuelve el estado resultante de aplicar accion a estado. Se
        supone que accion es aplicable a estado (es decir, debe ser una de las
        acciones de self.acciones(estado)."""
        abstract

    def es_estado_final(self, estado):
        """Devuelve True cuando estado es final. Por defecto, compara con el
        estado final, si éste se hubiera especificado al constructor. Si se da
        el caso de que no hubiera un único estado final, o se definiera
        mediante otro tipo de comprobación, habría que redefinir este método
        en la subclase.""" 
        return estado == self.estado_final

    def coste_de_aplicar_accion(self, estado, accion):
        """Devuelve el costo de aplicar accion a estado. Por defecto, este
        coste es 1. Reimplementar si el problema define otro coste """ 
        return 1

# Lo que sigue es un ejemplo de cómo definir un problema como subclase
# de problema. En concreto, el problema de las jarras, visto en clase:

class Jarras(Problema):
    """Problema de las jarras:
    Representaremos los estados como tuplas (x,y) de dos números enteros,
    donde x es el número de litros de la jarra de 4 e y es el número de litros
    de la jarra de 3"""

    def __init__(self):
        super().__init__((0,0))

    def acciones(self,estado):
        jarra_de_4=estado[0]
        jarra_de_3=estado[1]
        accs=list()
        if jarra_de_4 > 0:
            accs.append("vaciar jarra de 4")
            if jarra_de_3 < 3:
                accs.append("trasvasar de jarra de 4 a jarra de 3")
        if jarra_de_4 < 4:
            accs.append("llenar jarra de 4")
            if jarra_de_3 > 0:
                accs.append("trasvasar de jarra de 3 a jarra de 4")
        if jarra_de_3 > 0:
            accs.append("vaciar jarra de 3")
        if jarra_de_3 < 3:
            accs.append("llenar jarra de 3")
        return accs

    def aplica(self,estado,accion):
        j4=estado[0]
        j3=estado[1]
        if accion=="llenar jarra de 4":
            return (4,j3)
        elif accion=="llenar jarra de 3":
            return (j4,3)
        elif accion=="vaciar jarra de 4":
            return (0,j3)
        elif accion=="vaciar jarra de 3":
            return (j4,0)
        elif accion=="trasvasar de jarra de 4 a jarra de 3":
            return (j4-3+j3,3) if j3+j4 >= 3 else (0,j3+j4)
        else: #  "trasvasar de jarra de 3 a jarra de 4"
            return (j3+j4,0) if j3+j4 <= 4 else (4,j3-4+j4)

    def es_estado_final(self,estado):
        return estado[0]==2


# Ejemplos:

# >>> pj = Jarras()
# >>> pj.estado_inicial
# (0, 0)
# >>> pj.acciones(pj.estado_inicial)
# ['llenar jarra de 4', 'llenar jarra de 3']
# >>> pj.aplica(pj.estado_inicial,"llenar jarra de 4")
# (4, 0)
# >>> pj.coste_de_aplicar_accion(pj.estado_inicial,"llenar jarra de 4")
# 1
# >>> pj.es_estado_final(pj.estado_inicial)
# False

    
    
# ------------
# Ejercicio 1
# -----------    

# ---------------------------------------------------------------------------
# Definir la clase Ocho_Puzzle, que implementa la representación del
# problema del 8-puzzle visto en clase. Para ello, completar el código que se
# presenta a continuación, en los lugares marcados con interrogantes.
# ----------------------------------------------------------------------------


class Ocho_Puzzle(Problema):
    """Problema a del 8-puzzle.  Los estados serán tuplas de nueve elementos,
    permutaciones de los números del 0 al 8 (el 0 es el hueco). Representan la
    disposición de las fichas en el tablero, leídas por filas de arriba a
    abajo, y dentro de cada fila, de izquierda a derecha. Por ejemplo, el
    estado final será la tupla (1, 2, 3, 8, 0, 4, 7, 6, 5). Las cuatro
    acciones del problema las representaremos mediante las cadenas:
    "Mover hueco arriba", "Mover hueco abajo", "Mover hueco izquierda" y
    "Mover hueco dercha", respectivamente. 
    """
    def __init__(self,tablero_inicial):
        super().__init__(estado_inicial= tablero_inicial, estado_final=(1, 2, 3, 8, 0, 4, 7, 6, 5))

    def acciones(self,estado):
        pos_hueco=estado.index(0)
        accs=list()
        if pos_hueco not in (0,1,2):
            accs.append("Mover hueco arriba")
        if pos_hueco not in (0,3,6): 
            accs.append("Mover hueco izquierda")
        if pos_hueco not in (6,7,8): 
             accs.append("Mover hueco abajo")
        if pos_hueco not in (2,5,8):
             accs.append("Mover hueco derecha")
        return accs      

    def aplica(self,estado,accion):
        pos_hueco = estado.index(0)
        lista = list(estado)
        if accion == "Mover hueco arriba":
            lista[pos_hueco] = lista[pos_hueco-3]
            lista[pos_hueco-3] = 0
        if accion == "Mover hueco abajo":
            lista[pos_hueco] = lista[pos_hueco+3]
            lista[pos_hueco+3] = 0
        if accion == "Mover hueco derecha":
            lista[pos_hueco] = lista[pos_hueco+1]
            lista[pos_hueco+1] = 0
        if accion == "Mover hueco izquierda":
            lista[pos_hueco] = lista[pos_hueco-1]
            lista[pos_hueco-1] = 0
        return tuple(lista)
# Ejemplos que se pueden ejecutar una vez se ha definido la clase:

# >>> p8p_1 = Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))
# >>> p8p_1.estado_inicial
# (2, 8, 3, 1, 6, 4, 7, 0, 5)
# >>> p8p_1.estado_final
# (1, 2, 3, 8, 0, 4, 7, 6, 5)
# >>> p8p_1.acciones(p8p_1.estado_inicial)
# ['Mover hueco arriba', 'Mover hueco izquierda', 'Mover hueco derecha']
# >>> p8p_1.aplica(p8p_1.estado_inicial,"Mover hueco arriba")
# (2, 8, 3, 1, 0, 4, 7, 6, 5)
# >>> p8p_1.coste_de_aplicar_accion(p8p_1.estado_inicial,"Mover hueco arriba")
# 1

# ----------------------------------------------------------------------------


#===================================================
# PARTE II. IMPLEMENTACIÓN DE ALGORITMOS DE BÚSQUEDA
#===================================================

# En esta parte vamos a implementar los algoritmos de búsqueda en anchura,
# búsuqeda en profundidad, búsqueda óptima, búsqueda_primero_el_mejor y
# busqueda_a_estrella. Los dos primeros serán casos particulares de lo que
# llamaremos búsqueda_genérica (tal y como se ha visto en clase) y los otros
# tres serán casos particulares de búsqueda_con_prioridad (es decir, una
# búsqueda en la que la cola se gestiona en orden de una valoración dada).

# -----------
# Ejercico 2
# -----------

# ---------------------------------------------------------------------------
# Recordar de teoría que la generación de los aŕboles de búsqueda se hace a
# través de lo que llamamos nodo de búsqueda. Un nodo de búsqueda debe
# contener la siguiente información:
#     - El estado
#     - Un puntero al estado desde el que viene (padre)
#     - La acción que se ha aplicado al padre para que se obtenga el
#       estado del nodo
#     - Profundidad del nodo
#     - Coste del camino desde el estado inicial hasta el nodo.





# Definir la clase NODO, que implementa los nodos de un árbol de
# búsqueda. Para ello, completar el código que se presenta a continuación, en
# los lugares marcados con interrogantes.

# Ejemplo que se puede ejecutar una vez se define la clase:
#
# >>> p8p_1 = Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))
# >>> np8p_1=(Nodo(p8p_1.estado_inicial))
# >>> np8p_1.sucesores(p8p_1)
# [<Nodo (2, 8, 3, 1, 0, 4, 7, 6, 5)>, <Nodo (2, 8, 3, 1, 6, 4, 0, 7, 5)>, 
#   <Nodo (2, 8, 3, 1, 6, 4, 7, 5, 0)>]

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

class Nodo:
    """Nodos de un árbol de búsqueda. Un nodo se define como:
       - Un estado
       - Un puntero al estado desde el que viene (padre)
       - La acción que se ha aplicado al padre para que se obtenga el
         estado del nodo
       - Profundidad del nodo
       - Coste del camino desde el estado inicial hasta el nodo.
       
       Definimos además, entre otros, los siguientes métodos que se
       necesitarán para generar el aŕbol de búsqueda: 
       - Sucesor y sucesores de un nodo (resp. por una acción o por todas las
         acciones aplicables al estado del nodo) 
       - Camino (secuncia de nodos) que lleva del estado inicial al estado del
         nodo.
       - Solución (secuencia de acciones que llevan al estado) de un nodo.   
       """  

    def __init__(self, estado, padre=None, accion=None, coste_camino=0):
        self.estado=estado
        self.padre=padre
        self.accion=accion
        self.coste_camino=coste_camino
        self.profundidad=0
        if padre: 
            self.profundidad= self.profundidad + 1

    def __repr__(self):
        return "<Nodo {0}>".format(self.estado)

    def sucesor(self, problema, accion):
        """Sucesor de un nodo por una acción aplicable"""
        estado_suc = problema.aplica(self.estado, accion)
        return Nodo(estado_suc, self, accion,
                    problema.coste_de_aplicar_accion(self.estado,accion)+self.coste_camino)


    def sucesores(self, problema):
        """Lista de los nodos sucesores por todas las acciones que le sean
           aplicables""" 
        return [self.sucesor(problema, accion)
            for accion in problema.acciones(self.estado)]

    def camino(self):
        """Lista de nodos que forman el camino desde el inicial hasta el
           nodo.""" 
        nodo_aux, camino_inverso = self, []
        while nodo_aux:
            camino_inverso.append(nodo_aux)
            nodo_aux = nodo_aux.padre
        return list(reversed(camino_inverso))

    def solucion(self):
        """Secuencia de acciones desde el nodo inicial"""
        return [nodo.accion for nodo in self.camino()[1:]]

    def __eq__(self, other):
        """ Dos nodos son iguales si sus estados son iguales. Esto significa que
        cuando comprobemos pertenecia a una lista o a un conjunto (con"in"), sólo
        miramos los estados. Si hay que nirar, por ejemplo, algo del coste,
        habrá que hacerlo expresamente, como se hará en la
        buśqueda_con_prioridad"""
        
        return isinstance(other, Nodo) and self.estado == other.estado

    def __lt__(self, other): 
        """La definición del menor entre nodos se necesita porque cuando se
        introduce un nodo en la cola de prioridad, con la misma valoración que
        uno ya existente, se van a comparar los nodos y por tanto es necesario que
        esté definido el operador <"""  
        return True
    
    def __hash__(self):
        """Nótese que esta definición obliga a que los estados sean de un tipo
        de dato hashable"""
        return hash(self.estado)  
                                  
# -----------------------------------------------------------------------------

                                  
# -----------
# Ejercicio 3
# -----------

# Implementar la búsqueda genérica, tal y como se ha descrito en clase. Para
# ello, completar el código que se presenta a continuación, en los lugares
# marcados con interrogantes. En esta implementación se define cerrados como
# un conjunto de estados (tipo set) y abiertos como una cola de nodos.

def busqueda_generica(problema, abiertos):
    """Búsqueda genérica, tal y como se ha visto en clase; aquí
    abiertos es una cola que se puede gestionar de varias maneras. 
    Cuando se llama a la función, el argumento abiertos debe ser la cola
    vacía. 
    Téngase en cuenta que en esta búsqueda, para ver si se repite un nodo,
    sólo se mira el estado. Por tanto, las búsquedas que usan coste (óptima o
    A*, por ejemplo), no se pueden obtener como caso particular de ésta (serán
    casos particulares de búsqueda_con_prioridad"""


    abiertos.append(Nodo(problema.estado_inicial))
    cerrados = set()
    while abiertos:
        actual = abiertos.pop()  
        if problema.es_estado_final(actual.estado):
            return actual
        cerrados.add(actual.estado)
        nuevos_sucesores=(sucesor for sucesor in actual.sucesores(problema)
            if sucesor.estado not in cerrados
            and sucesor not in abiertos)
        abiertos.extend(nuevos_sucesores)
    return None



# La cola de abiertos se recibe como argumento y será una instancia de una de
# los tipos de colas que se definen en el módulo colas.py. Tener en cuenta que
# en este módulo, sea cual sea el tipo de cola, éstas soportan los métodos
# pop(), append(_) y extend(_), que respectivamente extraen el primer elemento
# de la cola o añaden un elemento o una lista de elementos a la cola. La
# gestión de la cola será algo interno al objeto cola.

# -------------------------------------------------------------------------------













# -----------
# Ejercicio 4
# -----------

# Usando la búsqueda genérica, implementar los algoritmos busqueda_en_anchura
# y busqueda_en_profundidad.
# Indicación: Iniciar abiertos con una cola LIFO o FIFO, respectiavmente. 

def busqueda_en_profundidad(problema):
    return busqueda_generica(problema, PilaLIFO())

def busqueda_en_anchura(problema):
    return busqueda_generica(problema, ColaFIFO())


# Ejemplos de uso:

# >>> busqueda_en_anchura(Jarras()).solucion()
# ['llenar jarra de 4', 'trasvasar de jarra de 4 a jarra de 3', 
#  'vaciar jarra de 3', 'trasvasar de jarra de 4 a jarra de 3', 
#  'llenar jarra de 4', 'trasvasar de jarra de 4 a jarra de 3']
# >>> busqueda_en_profundidad(Jarras()).solucion()
# ['llenar jarra de 3', 'trasvasar de jarra de 3 a jarra de 4', 
#  'llenar jarra de 3', 'trasvasar de jarra de 3 a jarra de 4', 
#  'vaciar jarra de 4', 'trasvasar de jarra de 3 a jarra de 4']
# >>> busqueda_en_anchura(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))).solucion()
# ['Mover hueco arriba', 'Mover hueco arriba', 'Mover hueco izquierda', 
#  'Mover hueco abajo', 'Mover hueco derecha']
# >>> busqueda_en_profundidad(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))).solucion()
# ['Mover hueco derecha', 'Mover hueco arriba', ... ] # ¡más de 3000 acciones!


# ---------------------------------------------------------------------------------
















# ---------------------------------------------------------------------------------



# ----------------------------------------------------------------

# La siguiente función búsqueda_con_prioridad(problema,f), define una
# búsqueda genérica en la que la cola de abiertos se gestiona como una cola
# con prioridad, ordenándo los nodos de menor a mayor valoración según
# f. Nótese que la búsqueda por primero el mejor, la búsqueda óptima y la
# búsqueda A* pueden verse como casos particulares de esta búsqueda, usando
# distintas "f".

# Esta búsqueda con prioridad varía respecto a la búsqueda genérica del
# ejercicio 3, en un detalle. Si se genera un nodo cuyo estado ya está en un
# nodo de abiertos pero con mayor coste, ha de ser incluidos en abiertos:

def busqueda_con_prioridad(problema, f):
    """Búsqueda que gestiona la cola de abiertos ordenando los nodos de menor
    a mayor valor de f. Tanto la búsqueda por primero el mejor, como la
    búsqueda óptima y la búsqueda A* son casos particulares de esta búsqueda,
    usando distintas f's (heurística, coste y coste más heurística,
    respectivamente)."""
    
    actual = Nodo(problema.estado_inicial)
    if problema.es_estado_final(actual.estado):
        return actual
    abiertos = ColaPrioridad(min, f)
    abiertos.append(actual)
    cerrados = set()
    while abiertos:
        actual = abiertos.pop()
        if problema.es_estado_final(actual.estado):
            return actual
        cerrados.add(actual.estado)
        for sucesor in actual.sucesores(problema):
            if sucesor.estado not in cerrados and sucesor not in abiertos:
                abiertos.append(sucesor)
            elif sucesor in abiertos:
                nodo_con_mismo_estado = abiertos[sucesor]
                if f(sucesor) < f(nodo_con_mismo_estado): 
                    del abiertos[nodo_con_mismo_estado]
                    abiertos.append(sucesor)
    return None



# -----------
# Ejercicio 5
# -----------

# Usando la búsqueda con prioridad definida anteriormente, implementar los
# algoritmos busqueda_optima, busqueda_primero_el_mejor y
# busqueda_a_estrella. Nótese que los dos últimos algoritmos, además del
# problema, reciben como entrada la función heurística que han de utilizar

def busqueda_primero_el_mejor(problema, h=None):
    return busqueda_con_prioridad(problema,lambda n: h(n.estado))
def busqueda_a_estrella(problema, h=None):
    return busqueda_con_prioridad(problema,lambda n: n.coste_camino + h(n.estado))
# ---------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------

#===============================================
# PARTE III. Experimentando
#===============================================


# -----------
# Ejercicio 6
# -----------


# Definir las dos funciones heurísticas para el 8 puzzle que se han visto en
# clase. Es decir:
# - h1_ocho_puzzle(estado): cuenta el número de casillas mal colocadas respecto
#   del estado final.
# - h2_ocho_puzzle_estado(estado): suma la distancia Manhattan desde cada casilla
#   a la posición en la que debería estar en el estado final. 

# Ejemplos:

# >>> h1_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))
# 4
# >>> h2_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))
# 5
# >>> h1_ocho_puzzle((5,2,3,0,4,8,7,6,1))
# 4
# >>> h2_ocho_puzzle((5,2,3,0,4,8,7,6,1))
# 11


# Completar el código que se presenta a continuación, en los lugares marcados
# con interrogantes. 

def h1_ocho_puzzle(estado):
    estado_final = (1,2,3,8,0,4,7,6,5)
    l = sum ([1 for i in range(9) if estado[i] == estado_final[i]])
    return l

def posiciones(estado):
    l = list()
    for i in estado:
        indice = estado.index(i)
        if indice in (0,1,2):
            l.append((i,0,estado.index(i)%3))
        if indice in (3,4,5):
            l.append((i,1,estado.index(i)%3))
        if indice in (6,7,8):
            l.append((i,2,estado.index(i)%3))                   
    return l
    
def h2_ocho_puzzle(estado):
    posiciones_final = (4,0,1,2,5,8,7,6,3)
    final_pos = posiciones(posiciones_final)
    estado_pos = posiciones(estado)
    suma = 0
    for i in final_pos:
        for j in range(9):
            if estado_pos[j][0] == i[0] and i[0]!=0:
                suma+= abs(i[1]-estado_pos[j][1])
                suma+= abs(i[2]-estado_pos[j][2])
    return suma
        






# ------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------

#============
# Ejercicio 7
#============
# Resolver usando búsqueda_coste: busqueda_primero_el_mejor 
# busqueda_a_estrella (con las dos heurísticas), 
# el problema del 8 puzzle para el siguiente estado inicial:

#              +---+---+---+
#              | 2 | 8 | 3 |
#              +---+---+---+
#              | 1 | 6 | 4 |
#              +---+---+---+
#              | 7 | H | 5 |
#              +---+---+---+
# ---------------------------------------------------------------------------------











# ---------------------------------------------------------------------------------
# La siguientes definiciones nos van a permitir experimentar con distintos
# estados iniciales, algoritmos y heurísticas, para resolver el
# 8-puzzle. Además se van a contar el número de nodos analizados durante la
# búsqueda:


class Problema_con_Analizados(Problema):

    """Es un problema que se comporta exactamente igual que el que recibe al
       inicializarse, y además incorpora un atributos nuevos para almacenar el
       número de nodos analizados durante la búsqueda. De esta manera, no
       tenemos que modificar el código del algorimo de búsqueda.""" 
         
    def __init__(self, problema):
        self.estado_inicial = problema.estado_inicial
        self.problema = problema
        self.analizados  = 0

    def acciones(self, estado):
        return self.problema.acciones(estado)

    def aplica(self, estado, accion):
        return self.problema.aplica(estado, accion)

    def es_estado_final(self, estado):
        self.analizados += 1
        return self.problema.es_estado_final(estado)

    def coste_de_aplicar_accion(self, estado, accion):
        return self.problema.coste_de_aplicar_accion(estado,accion)



def resuelve_ocho_puzzle(estado_inicial, algoritmo, h=None):
    """Función para aplicar un algoritmo de búsqueda dado al problema del ocho
       puzzle, con un estado inicial dado y (cuando el algoritmo lo necesite)
       una heurística dada.
       Ejemplo de uso:

       >>> resuelve_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5),busqueda_a_estrella,h2_ocho_puzzle)
       Solución: ['Mover hueco arriba', 'Mover hueco arriba', 'Mover hueco izquierda', 
                  'Mover hueco abajo', 'Mover hueco derecha']
       Algoritmo: busqueda_a_estrella
       Heurística: h2_ocho_puzzle
       Longitud de la solución: 5. Nodos analizados: 7
       """

    p8p=Problema_con_Analizados(Ocho_Puzzle(estado_inicial))
    sol= (algoritmo(p8p,h).solucion() if h else algoritmo(p8p).solucion()) 
    print("Solución: {0}".format(sol))
    print("Algoritmo: {0}".format(algoritmo.__name__))
    if h: 
        print("Heurística: {0}".format(h.__name__))
    else:
        pass
    print("Longitud de la solución: {0}. Nodos analizados: {1}".format(len(sol),p8p.analizados))


#============
# Ejercicio 8
#============

# Intentar resolver usando las distintas búsuqedas y en su caso, las distintas
# heurísticas, el problema del 8 puzzle para los siguientes estados iniciales:

#           E1              E2              E3              E4
#           
#     +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+    
#     | 2 | 8 | 3 |   | 4 | 8 | 1 |   | 2 | 1 | 6 |   | 5 | 2 | 3 |
#     +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
#     | 1 | 6 | 4 |   | 3 | H | 2 |   | 4 | H | 8 |   | H | 4 | 8 |
#     +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
#     | 7 | H | 5 |   | 7 | 6 | 5 |   | 7 | 5 | 3 |   | 7 | 6 | 1 |
#     +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
    
# Se pide, en cada caso, hacerlo con la función resuelve_ocho_puzzle, para
# obtener, además de la solución, la longitud (el coste) de la solución
# obtenida y el número de nodos analizados. Anotar los resultados en la
# siguiente tabla (L, longitud de la solución, NA, nodos analizados), y
# justificarlos con las distintas propiedades teóricas estudiadas.


#                                       E1           E2           E3          E4
                                
# Anchura                             L=            L=           L=          L=  
#                                     NA=           NA=          NA=         NA= 
                                                                              
# Profundidad                         L=            L=           L=          L=  
#                                     NA=           NA=          NA=         NA= 
                                                                              
# Óptima                              L=            L=           L=          L=  
#                                     NA=           NA=          NA=         NA= 
                                                                              
# Primero el mejor (h1)               L=            L=           L=          L=
#                                     NA=           NA=          NA=         NA=
                                                                              
# Primero el mejor (h2)               L=            L=           L=          L= 
#                                     NA=           NA=          NA=         NA=
                                                                              
# A* (h1)                             L=            L=           L=          L= 
#                                     NA=           NA=          NA=         NA=
                                                                              
# A* (h2)                             L=            L=           L=          L= 
#                                     NA=           NA=          NA=         NA=

# -----------------------------------------------------------------------------------------


















#---------------------------------------------------------------------------



#============
# Ejercicio 9
#============

# La siguiente heurística h3_ocho_puzzle se obtiene sumando a la heurística
# h2_ocho_puzzle una componente que cuantifica la "secuencialidad" en las
# casillas de un tablero, al recorrerlo en el sentido de las aguas del reloj
# ¿Es h3 admisble? Comprobar cómo se comporta esta heurística cuando se usa en
# A*, con cada uno de los estados anteriores. Comentar los resultados.


def h3_ocho_puzzle(estado):

    suc_ocho_puzzle ={0: 1, 1: 2, 2: 5, 3: 0, 4: 4, 5: 8, 6: 3, 7: 6, 8: 7}  

    def secuencialidad_aux(estado,i):
        
        val=estado[i]
        if val == 0:
            return 0
        elif i == 4:
            return 1
        else:
            i_sig=suc_ocho_puzzle[i]
            val_sig = (val+1 if val<8 else 1)
            return 0 if val_sig == estado[i_sig] else 2 

    def secuencialidad(estado):
        res= 0 
        for i in range(8): 
            res+=secuencialidad_aux(estado,i)
        return res    

    return h2_ocho_puzzle(estado) + 3*secuencialidad(estado)
                   

# ---------------------------------------------------------------------------


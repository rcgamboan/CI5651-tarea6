# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 6. Ejercicio 2

# Se utiliza un diccionario para representar el arbol
# de esta manera es mas sencillo trabajar con las conexiones entre los nodos
from collections import defaultdict

# Definimos la clase Nodo que representa un nodo en el árbol
class Node:
    def __init__(self, parent=-1):
        self.parent = parent  # El padre del nodo, inicialmente -1
        self.children = []  # La lista de hijos del nodo
        self.all = True  # Si todos los caminos desde este nodo son verdaderos
        self.any = False  # Si algún camino desde este nodo es verdadero

# DFS para preprocesar el árbol
# Se actualizan los valores de all y any para cada nodo
def dfs(v, p):
    for u in arbol[v]:
        if u == p: continue
        nodos[u].parent = v
        nodos[v].children.append(u)
        dfs(u, v)
        nodos[v].all &= nodos[u].all
        nodos[v].any |= nodos[u].any

# Función para responder a la consulta forall
# Se recorre el arbol desde el nodo y hasta el nodo x
# Si se alcanza el nodo x y no todos los caminos son verdaderos, se devuelve False
# Caso contrario, se devuelve True
# Si se llega a la raíz del árbol y no se ha encontrado un camino, se devuelve False
# En el peor caso se recorreran log N nodos, por lo que el tiempo de ejecución es O(log N)
def query_all(x, y):
    if x < y: 
        x,y = y,x
    while x != y or x != -1:
        if nodos[x].parent == y:
            if not nodos[x].all:
                return False
        x = nodos[x].parent
        if x == -1:
            print("No existe camino desde x hasta y")
            return False
    return True  # Si todos los caminos son verdaderos, devolvemos True

# Función para responder a la consulta exists
# Se recorre el arbol desde el nodo y hasta el nodo x o hasta que se encuentre un camino verdadero
# Si se alcanza el nodo x y algún camino es verdadero, se devuelve True
# Caso contrario, se devuelve False
# Si se llega a la raíz del árbol y no se ha encontrado un camino, se devuelve False
# En el peor caso se recorreran log N nodos, por lo que el tiempo de ejecución es O(log N)
def query_any(x, y):
    if x < y: 
        x,y = y,x
    while x != y or x != -1:
        if nodos[x].parent == y:
            if nodos[x].any:
                return True
        x = nodos[x].parent
        if x == -1:
            print("No existe camino desde x hasta y")
            return False
    return False


if __name__ == "__main__":
    # Definimos los nodos y las conexiones
    predicados = [True, False, True, True, False, True, False]
    conexiones = [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6), (6, 7)]
    cant_nodos = len(conexiones) + 1

    # Inicializamos el arbol y los nodos
    arbol = defaultdict(list)
    nodos = [Node() for i in range(cant_nodos+1)]

    # Establecemos los valores de all y any para cada nodo según el predicado p
    for i in range(1, cant_nodos+1):
        nodos[i].all = nodos[i].any = predicados[i-1]

    # Construimos el árbol en base a las conexiones
    for a, b in conexiones:
        arbol[a].append(b)
        arbol[b].append(a)

    # Preprocesamos el árbol con una búsqueda en profundidad
    dfs(1, 0)

    # Definimos las consultas de prueba
    queries = [('forall', 1, 4), ('exists', 1, 4), ('forall', 4, 7), ('exists', 4, 7), ('forall', 3, 5)]

    # Respondemos a las consultas
    for query, x, y in queries:
        if query == 'forall':
            print(query_all(x, y))
        else:
            print(query_any(x, y))



# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 6. Ejercicio 3

# Se utiliza un arbol de segmentos persistentes para resolver el problema
# Se usa como referencia la implementacion de arbol de segmentos persistente
# utilizada en el siguiente enlace: https://www.geeksforgeeks.org/persistent-segment-tree-set-1-introduction/

# Definicion de los nodos que integraran el arbol de segmentos
class Node:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

# Función para construir el árbol de segmentos
# Se crean todos los nodos con valor 0, ya que inicialmente no se ha agregado
# ningún valor al árbol de segmentos
# Tiempo de ejecución: O(N) ya que se llama N veces
def build(l, r):
    if l == r:
        return Node(val=0)
    mid = (l + r) // 2
    return Node(build(l, mid), build(mid+1, r), 0)

# Función para actualizar el árbol de segmentos cuando se inserta un nuevo valor.
# Se actualiza el valor de cada nodo para representar la cantidad de elementos en el rango presentes.
# Es decir, si el nodo representa el rango [2, 4] y en el arreglo estan presentes los elementos 2 y 4,
# el valor del nodo será 2. Si solo está presenta 2, el valor del nodo será 1.
# Tiempo de ejecución: O(log N), ya que en el peor caso se debera alcanzar el nivel más bajo del árbol
def update(node, l, r, idx):
    if l == r:
        return Node(val=node.val+1)
    mid = (l + r) // 2
    if idx <= mid:
        return Node(update(node.left, l, mid, idx), node.right, node.val+1)
    else:
        return Node(node.left, update(node.right, mid+1, r, idx), node.val+1)


# Función para responder a las consultas. 
# Devuelve el k-ésimo elemento en el subarreglo ordenado A[i..j].
# para obtener el resultado, se realiza una búsqueda binaria en el árbol de segmentos persistente
# para encontrar el k-ésimo elemento en el rango deseado.
# Gracias a la estructura del árbol de segmentos, se puede realizar la búsqueda en O(log N)
# en lugar de ordenar el subarreglo y buscar el k-ésimo elemento, que puede tomar tiempo lineal
# Tiempo de ejecución: O(log N)
def query(node_l, node_r, l, r, k):

    # Cuando el rango es de un solo elemento, se devuelve el valor del nodo
    if l == r:
        return l
    # Se obtiene el punto medio del rango
    mid = (l + r) // 2
    # Si el valor del nodo derecho menos el valor del nodo izquierdo es mayor o igual a k,
    # se realiza la búsqueda en el subarreglo izquierdo ya que el valor buscado se encuentra en ese rango
    if node_r.left.val - node_l.left.val >= k:
        return query(node_l.left, node_r.left, l, mid, k)
    else:
        # Caso contrario, se realiza la búsqueda en el subarreglo derecho
        return query(node_l.right, node_r.right, mid+1, r, k - (node_r.left.val - node_l.left.val))

def seleccion(i, j, k):
    return query(version[i-1], version[j], 1, cant_elems, k)


# Prueba del algoritmo
if __name__ == "__main__" :

    # Se inicializa el arreglo de prueba
    # se crea el arbol de segmentos y se inicializa la version 0
    # posteriormente se crean nuevas versiones con los valores del arreglo
    # Posteriormente se realizan las consultas
    # para realizar cada consulta se llama a la funcion seleccion
    # la cual llama a la funcion query.
    # Como se llama al metodo seleccion un maximo de Q veces,
    # y al metodo update un maximo de N veces, el tiempo de ejecucion es O(N log N + Q log N)
    # es decir, el tiempo de ejecucion es O((N + Q) log N)

    # Arreglo de prueba
    # Se le agrega un 0 al inicio para trabajar con indices basados en 1
    arr = [2, 6, 3, 1, 8, 4, 7, 9, 5]
    cant_elems = len(arr)
    arreglo = [0] + arr

    # Se inicializa el arreglo de nodos que representa todas las versiones del arbol de segmentos
    # Se crearan N+1 versiones, ya que se necesita una version para cada elemento del arreglo
    # ademas de la version inicial 0.
    # Se llama a la función build para construir el árbol de segmentos a partir del arreglo
    # En la primera version todos los nodos tienen valor 0
    version = [None] * (cant_elems+1)
    version[0] = build(1, cant_elems)

    # Se agregan los nodos al arbol de segmentos, actualizando la version en cada iteracion
    for i in range(1, cant_elems+1):
        version[i] = update(version[i-1], 1, cant_elems, arreglo[i])

    
    print(f"Rango de busqueda : 2 - 5, posicion : 3")
    print(f"Subarreglo sin ordenar : {arreglo[2:6]}")
    print(f"Subarreglo ordenado : {sorted(arreglo[2:6])}")
    print(f"Valor esperado: {sorted(arreglo[2:6])[2]}, Valor obtenido: {seleccion(2, 5, 3)}")

    
    print(f"\nRango de busqueda : 3 - 7, posicion : 1")
    print(f"Subarreglo sin ordenar : {arreglo[3:8]}")
    print(f"Subarreglo ordenado : {sorted(arreglo[3:8])}")
    print(f"Valor esperado: {sorted(arreglo[3:8])[0]}, Valor obtenido: {seleccion(3, 7, 1)}")

    print(f"\nRango de busqueda : 1 - 9, posicion : 5")
    print(f"Subarreglo sin ordenar : {arreglo[1:10]}")
    print(f"Subarreglo ordenado : {sorted(arreglo[1:10])}")
    print(f"Valor esperado: {sorted(arreglo[1:10])[4]}, Valor obtenido: {seleccion(1, 9, 5)}")

    print(f"\nRango de busqueda : 4 - 7, posicion : 4")
    print(f"Subarreglo sin ordenar : {arreglo[4:8]}")
    print(f"Subarreglo ordenado : {sorted(arreglo[4:8])}")
    print(f"Valor esperado: {sorted(arreglo[4:8])[3]}, Valor obtenido: {seleccion(4, 7, 4)}")

    
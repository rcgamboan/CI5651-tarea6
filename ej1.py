# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 5. Ejercicio 1

# Clase para el arbol de segmentos
class SegmentTree:
	
    # Constructor de la clase
    # Se crea un arreglo de tamaño 2*n y se inicializa con ceros
    # en este arreglo se almacenaran los valores del arbol
    def __init__(self,cant_elems):
        self.size = cant_elems
        self.tree = [0] * (2*cant_elems)

    # Método para construir el árbol a partir de un arreglo
    # Se copian los elementos del arreglo al árbol
    # Como se recorre el arreglo completo, el tiempo de ejecución es O(N)
    def build(self, A): 
        for i in range(self.size):
            self.tree[self.size + i] = A[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[i<<1], self.tree[i<<1 | 1])

    # Método para actualizar un elemento del árbol
    # Se actualiza el valor en la posición p y se actualizan los nodos padres
    # El tiempo de ejecución es O(log N)
    def update(self, p, value):
        # Se recorre el arbol hasta la posición p
        p += self.size 
        self.tree[p] = value
        i = p
        # Se actualizan los nodos padres
        while i > 1:
            self.tree[i>>1] = min(self.tree[i], self.tree[i^1])
            i >>= 1


# Función para realizar las operaciones de multiswap
def multiswap(A, a, b):  # Tiempo de ejecución: O(N log N)
    
    cant_elems = len(A)  # Tamaño del arreglo

    # Creacion del arból de segmentos
    segTree = SegmentTree(cant_elems)
    segTree.build(A)

    #iter = 0
    j = b
    while a < j and b < len(A):
        segTree.update(a, A[b])  # Actualizamos el valor en la posición a
        segTree.update(b, A[a])  # Actualizamos el valor en la posición b
        a += 1
        b += 1
        #iter += 1
        #print(f"iteracion {iter}; A : {segTree.tree[cant_elems:]}")
    return A  # Devolvemos el arreglo resultante


if __name__ == "__main__" : 

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    print(f"Arreglo resultante: {multiswap(a, 2, 5)}")
    

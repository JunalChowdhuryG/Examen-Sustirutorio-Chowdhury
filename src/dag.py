import graphviz


# funcion que genera earchiv dot
def leer_archivo_dot(ruta_dot):
    # leer archivo .dot a digraph retorna un dag
    try:
        with open(ruta_dot) as f:
            dot_grafo = f.read()
            grafo = graphviz.Source(dot_grafo)
            return grafo
    # error en caso no pueda leer archivo
    except Exception as e:
        print(f"error archivo DOT: {e}")
        return None


# calcula la densidad de un nodo
def calcular_densidad(grafo, nodo):
    # calcula dependencia de un nodo en el grafo
    if grafo is None:
        return None
    try:
        dependencias = []
        for edge in grafo.edges:
            if edge[1] == nodo:
                dependencias.append(edge[0])
        return len(dependencias)
    except Exception as e:
        print(f"error : {e}")
        return None


# dikstra inverso halla camino desde Head hasta un nodo u
def dikstra_inverso(grafo, nodo):
    # calcula camino desde heaad hasta un nodo u
    if grafo is None:
        return None
    try:
        camino = []
        visitados = set()
        pila = [(nodo, [nodo])]
        # apila nodos y recorre el grafo
        while pila:
            actual, ruta = pila.pop()
            if actual not in visitados:
                visitados.add(actual)
                # caundo llegue a head guarda el camino
                if actual == 'HEAD':
                    camino = ruta[::-1]
                    break
                for edge in grafo.edges:
                    if edge[1] == actual:
                        pila.append((edge[0], ruta + [edge[0]]))
        return camino
    except Exception as e:
        print(f"error : {e}")
        return None


# halla los k commits con mayor indegree
# para esto se halla todos los caminos y se ordena por indegree y retorrna los k mayores
def k_commits_mayor_indegree(grafo, k):
    # calcula los k commits con mayor indegree
    if grafo is None:
        return None
    try:
        # creamos diccionario
        indegree = {}
        for edge in grafo.edges:
            if edge[1] not in indegree:
                indegree[edge[1]] = 0
            indegree[edge[1]] += 1
        # ordena por indegree retorna los k mayores
        return sorted(indegree.items(), key=lambda x: x[1], reverse=True)[:k]
    except Exception as e:
        print(f"error : {e}")
        return None

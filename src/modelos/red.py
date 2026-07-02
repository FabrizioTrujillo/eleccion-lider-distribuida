from modelos.nodo import Nodo

class Red:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, id_nodo):
        if id_nodo not in self.nodos:
            self.nodos[id_nodo] = Nodo(id_nodo)

    def conectar(self, id_a, id_b):
        # Conexion bidireccional entre dos nodos
        self.agregar_nodo(id_a)
        self.agregar_nodo(id_b)
        self.nodos[id_a].agregar_vecino(id_b)
        self.nodos[id_b].agregar_vecino(id_a)

    def crear_red_completa(self, cantidad_nodos):
        # Cada nodo conocido por todos (necesario para Bully clasico)
        ids = list(range(1, cantidad_nodos + 1))
        for id_nodo in ids:
            self.agregar_nodo(id_nodo)
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                self.conectar(ids[i], ids[j])

    def desactivar_nodo(self, id_nodo):
        if id_nodo in self.nodos:
            self.nodos[id_nodo].activo = False

    def nodos_activos(self):
        activos = []
        for id_nodo in self.nodos:
            if self.nodos[id_nodo].activo:
                activos.append(id_nodo)
        return activos
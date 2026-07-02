class Nodo:
    def __init__(self, id_nodo, vecinos=None):
        self.id = id_nodo
        self.vecinos = vecinos if vecinos is not None else []
        self.activo = True
        self.es_lider = False
        self.lider_actual = None

    def agregar_vecino(self, id_vecino):
        if id_vecino not in self.vecinos:
            self.vecinos.append(id_vecino)

    def __str__(self):
        estado = "activo" if self.activo else "caido"
        return "Nodo " + str(self.id) + " (" + estado + ")"
from utilidades.contador_mensajes import ContadorMensajes

class Bully:
    def __init__(self, red):
        self.red = red
        self.contador = ContadorMensajes()

    def iniciar_eleccion(self, id_iniciador):
        print("Nodo " + str(id_iniciador) + " inicia la eleccion")
        self.contador.nuevo_paso()

        # Buscar vecinos activos con id mayor
        candidatos_mayores = []
        for id_vecino in self.red.nodos[id_iniciador].vecinos:
            nodo_vecino = self.red.nodos[id_vecino]
            if nodo_vecino.activo and id_vecino > id_iniciador:
                candidatos_mayores.append(id_vecino)
                self.contador.registrar_mensaje(id_iniciador, id_vecino, "ELECCION")

        if len(candidatos_mayores) == 0:
            # No hay nadie mayor activo: este nodo se declara lider
            return self._declarar_lider(id_iniciador)
        else:
            # Simulamos que el nodo mayor entre los candidatos responde
            # y continua la eleccion desde ahi
            siguiente = max(candidatos_mayores)
            self.contador.registrar_mensaje(siguiente, id_iniciador, "OK")
            return self.iniciar_eleccion(siguiente)

    def _declarar_lider(self, id_lider):
        self.red.nodos[id_lider].es_lider = True
        print("Nodo " + str(id_lider) + " es el nuevo lider")
        self.contador.nuevo_paso()

        for id_nodo in self.red.nodos_activos():
            if id_nodo != id_lider:
                self.red.nodos[id_nodo].lider_actual = id_lider
                self.contador.registrar_mensaje(id_lider, id_nodo, "COORDINADOR")

        return id_lider
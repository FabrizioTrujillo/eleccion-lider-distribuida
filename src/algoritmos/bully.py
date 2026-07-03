from utilidades.contador_mensajes import ContadorMensajes

class Bully:
    def __init__(self, red):
        self.red = red
        self.contador = ContadorMensajes()

    def iniciar_eleccion(self, id_iniciador, nodo_que_falla=None):
        print("Nodo " + str(id_iniciador) + " inicia la eleccion")
        self.contador.nuevo_paso()

        vecinos_mayores = []
        for id_vecino in self.red.nodos[id_iniciador].vecinos:
            nodo_vecino = self.red.nodos[id_vecino]
            if nodo_vecino.activo and id_vecino > id_iniciador:
                vecinos_mayores.append(id_vecino)

        vecinos_mayores.sort(reverse=True)

        candidatos_validos = []
        for id_vecino in vecinos_mayores:
            self.contador.registrar_mensaje(id_iniciador, id_vecino, "ELECCION")

            if id_vecino == nodo_que_falla:
                print("Nodo " + str(id_vecino) + " recibe el mensaje y falla antes de responder")
                self.red.desactivar_nodo(id_vecino)
                continue

            candidatos_validos.append(id_vecino)

        if len(candidatos_validos) == 0:
            return self._declarar_lider(id_iniciador)
        else:
            siguiente = max(candidatos_validos)
            self.contador.registrar_mensaje(siguiente, id_iniciador, "OK")
            return self.iniciar_eleccion(siguiente, nodo_que_falla)

    def _declarar_lider(self, id_lider):
        self.red.nodos[id_lider].es_lider = True
        print("Nodo " + str(id_lider) + " es el nuevo lider")
        self.contador.nuevo_paso()

        for id_nodo in self.red.nodos_activos():
            if id_nodo != id_lider:
                self.red.nodos[id_nodo].lider_actual = id_lider
                self.contador.registrar_mensaje(id_lider, id_nodo, "COORDINADOR")

        return id_lider
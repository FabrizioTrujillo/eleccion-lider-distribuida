from utilidades.contador_mensajes import ContadorMensajes

class Anillo:
    def __init__(self, red, orden):
        # orden: lista con el orden logico del anillo, ej. [1,2,3,4,5,6]
        self.red = red
        self.orden = orden
        self.contador = ContadorMensajes()

    def _siguiente_activo(self, id_actual):
        indice = self.orden.index(id_actual)
        n = len(self.orden)
        for i in range(1, n + 1):
            candidato = self.orden[(indice + i) % n]
            if self.red.nodos[candidato].activo:
                return candidato
        return id_actual

    def iniciar_eleccion(self, id_iniciador):
        print("Nodo " + str(id_iniciador) + " inicia la eleccion en anillo")
        actual = id_iniciador
        maximo = id_iniciador
        siguiente = self._siguiente_activo(actual)

        self.contador.nuevo_paso()
        self.contador.registrar_mensaje(actual, siguiente, "ELECCION(" + str(maximo) + ")")

        while siguiente != id_iniciador:
            if siguiente > maximo:
                maximo = siguiente
            actual = siguiente
            siguiente = self._siguiente_activo(actual)
            self.contador.nuevo_paso()
            self.contador.registrar_mensaje(actual, siguiente, "ELECCION(" + str(maximo) + ")")

        return self._declarar_lider(maximo, id_iniciador)

    def _declarar_lider(self, id_lider, id_iniciador):
        self.red.nodos[id_lider].es_lider = True
        print("Nodo " + str(id_lider) + " es el nuevo lider (anillo)")

        actual = id_iniciador
        siguiente = self._siguiente_activo(actual)
        self.contador.nuevo_paso()
        self.red.nodos[siguiente].lider_actual = id_lider
        self.contador.registrar_mensaje(actual, siguiente, "COORDINADOR")

        while siguiente != id_iniciador:
            actual = siguiente
            siguiente = self._siguiente_activo(actual)
            self.contador.nuevo_paso()
            self.red.nodos[siguiente].lider_actual = id_lider
            self.contador.registrar_mensaje(actual, siguiente, "COORDINADOR")

        return id_lider
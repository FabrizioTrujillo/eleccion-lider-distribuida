class ContadorMensajes:
    def __init__(self):
        self.total_mensajes = 0
        self.pasos = 0
        self.historial = []

    def registrar_mensaje(self, origen, destino, tipo):
        self.total_mensajes += 1
        linea = "Paso " + str(self.pasos) + ": " + tipo + " de " + str(origen) + " a " + str(destino)
        self.historial.append(linea)

    def nuevo_paso(self):
        self.pasos += 1

    def resumen(self):
        texto = "Total de mensajes: " + str(self.total_mensajes) + "\n"
        texto += "Total de pasos: " + str(self.pasos)
        return texto
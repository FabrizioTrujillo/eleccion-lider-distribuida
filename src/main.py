from modelos.red import Red
from algoritmos.bully import Bully
from algoritmos.anillo import Anillo

def ejecutar_bully():
    print("=== ALGORITMO BULLY ===")
    cantidad_nodos = 6
    red = Red()
    red.crear_red_completa(cantidad_nodos)
    red.desactivar_nodo(6)

    bully = Bully(red)
    lider = bully.iniciar_eleccion(2)

    print("Lider elegido (Bully): " + str(lider))
    print(bully.contador.resumen())
    return bully.contador.total_mensajes, bully.contador.pasos

def ejecutar_anillo():
    print("\n=== ALGORITMO ANILLO ===")
    cantidad_nodos = 6
    red = Red()
    red.crear_red_completa(cantidad_nodos)
    red.desactivar_nodo(6)

    orden = [1, 2, 3, 4, 5, 6]
    anillo = Anillo(red, orden)
    lider = anillo.iniciar_eleccion(2)

    print("Lider elegido (Anillo): " + str(lider))
    print(anillo.contador.resumen())
    return anillo.contador.total_mensajes, anillo.contador.pasos

def main():
    mensajes_bully, pasos_bully = ejecutar_bully()
    mensajes_anillo, pasos_anillo = ejecutar_anillo()

    print("\n=== COMPARACION ===")
    print("Bully  -> mensajes: " + str(mensajes_bully) + ", pasos: " + str(pasos_bully))
    print("Anillo -> mensajes: " + str(mensajes_anillo) + ", pasos: " + str(pasos_anillo))

if __name__ == "__main__":
    main()
from modelos.red import Red
from algoritmos.bully import Bully

def main():
    cantidad_nodos = 6
    red = Red()
    red.crear_red_completa(cantidad_nodos)

    # Simulamos que el nodo con id mas alto (6) esta caido
    red.desactivar_nodo(6)

    nodo_iniciador = 2
    bully = Bully(red)
    lider = bully.iniciar_eleccion(nodo_iniciador)

    print("\nResultado final: lider elegido = " + str(lider))
    print(bully.contador.resumen())

if __name__ == "__main__":
    main()
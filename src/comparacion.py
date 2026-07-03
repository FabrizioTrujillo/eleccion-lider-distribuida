from modelos.red import Red
from algoritmos.bully import Bully
from algoritmos.anillo import Anillo
import csv

def correr_bully(cantidad_nodos, id_iniciador, id_a_desactivar=None):
    red = Red()
    red.crear_red_completa(cantidad_nodos)
    if id_a_desactivar is not None:
        red.desactivar_nodo(id_a_desactivar)

    bully = Bully(red)
    lider = bully.iniciar_eleccion(id_iniciador)
    return lider, bully.contador.total_mensajes, bully.contador.pasos

def correr_anillo(cantidad_nodos, id_iniciador, id_a_desactivar=None):
    red = Red()
    red.crear_red_completa(cantidad_nodos)
    if id_a_desactivar is not None:
        red.desactivar_nodo(id_a_desactivar)

    orden = list(range(1, cantidad_nodos + 1))
    anillo = Anillo(red, orden)
    lider = anillo.iniciar_eleccion(id_iniciador)
    return lider, anillo.contador.total_mensajes, anillo.contador.pasos

def main():
    tamanios = [5, 10, 15, 20, 30, 50]
    resultados = []

    print("tamanio_red | lider_bully | msj_bully | pasos_bully | lider_anillo | msj_anillo | pasos_anillo")
    print("-" * 100)

    for n in tamanios:
        # Silenciamos los prints internos de cada algoritmo para esta corrida masiva
        import io
        import sys as sistema
        salida_original = sistema.stdout
        sistema.stdout = io.StringIO()

        lider_b, msj_b, pasos_b = correr_bully(n, id_iniciador=1)
        lider_a, msj_a, pasos_a = correr_anillo(n, id_iniciador=1)

        sistema.stdout = salida_original

        fila = {
            "tamanio_red": n,
            "lider_bully": lider_b,
            "mensajes_bully": msj_b,
            "pasos_bully": pasos_b,
            "lider_anillo": lider_a,
            "mensajes_anillo": msj_a,
            "pasos_anillo": pasos_a
        }
        resultados.append(fila)

        print(str(n) + " | " + str(lider_b) + " | " + str(msj_b) + " | " + str(pasos_b) +
              " | " + str(lider_a) + " | " + str(msj_a) + " | " + str(pasos_a))

    import os
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(directorio_script, "..", "data", "resultados.csv")
    ruta_csv = os.path.normpath(ruta_csv)

    with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:
        campos = ["tamanio_red", "lider_bully", "mensajes_bully", "pasos_bully",
                  "lider_anillo", "mensajes_anillo", "pasos_anillo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for fila in resultados:
            escritor.writerow(fila)

    print("\nResultados guardados en " + ruta_csv)

if __name__ == "__main__":
    main()
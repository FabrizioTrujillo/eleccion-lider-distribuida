# eleccion-lider-distribuida

# Simulador de Elección de Líder Distribuida

Proyecto Final - Curso: Análisis de Algoritmos y Estrategias de Programación
Ingeniería de Sistemas Computacionales - UPN
Proyecto N.º 15: Simulador de algoritmos distribuidos para elección de líder

## Descripción

Simulación de dos algoritmos clásicos de elección de líder en sistemas distribuidos:

- **Algoritmo Bully**: el nodo iniciador contacta a sus vecinos de mayor identificador; el nodo con el id más alto activo se declara líder y notifica a todos los demás.
- **Algoritmo de Anillo**: los nodos están organizados en una topología lógica circular; el mensaje de elección circula por el anillo comparando identificadores hasta determinar el líder.

Ambos algoritmos miden cantidad de mensajes intercambiados y pasos de comunicación, permitiendo comparar su eficiencia.

## Requisitos

- Python 3.10 o superior (probado con Python 3.14)
- No requiere librerías externas adicionales a la biblioteca estándar de Python

## Instalación

1. Clonar el repositorio:

git clone <https://github.com/FabrizioTrujillo/eleccion-lider-distribuida>
cd eleccion-lider-distribuida

2. No se requiere instalación de dependencias adicionales.

## Estructura del proyecto

eleccion-lider-distribuida/
├── README.md
├── docs/
│   ├── informe.pdf
│   └── presentacion.pdf
├── src/
│   ├── main.py              # Ejecuta Bully y Anillo con una configuración fija (n=6)
│   ├── comparacion.py        # Ejecuta ambos algoritmos con varios tamaños de red
│   ├── modelos/
│   │   ├── nodo.py           # Clase Nodo
│   │   └── red.py            # Clase Red (grafo de nodos)
│   ├── algoritmos/
│   │   ├── bully.py          # Algoritmo Bully
│   │   └── anillo.py         # Algoritmo de Anillo
│   └── utilidades/
│       └── contador_mensajes.py  # Contador de mensajes y pasos
├── test/
│   └── pruebas_unitarias.py  # 8 pruebas unitarias (4 Bully, 4 Anillo)
├── data/
│   └── resultados.csv        # Resultados de comparacion.py (n=5,10,15,20,30,50)
└── evidencias/
└── capturas/

## Ejecución

### Simulación básica (un caso, n=6 nodos, nodo 6 desactivado)

Desde la carpeta `src`:

cd src
python main.py

Salida esperada (verificada en ejecución real):

=== ALGORITMO BULLY ===
Nodo 2 inicia la eleccion
Nodo 5 inicia la eleccion
Nodo 5 es el nuevo lider
Lider elegido (Bully): 5
Total de mensajes: 8
Total de pasos: 3
=== ALGORITMO ANILLO ===
Nodo 2 inicia la eleccion en anillo
Nodo 5 es el nuevo lider (anillo)
Lider elegido (Anillo): 5
Total de mensajes: 10
Total de pasos: 10
=== COMPARACION ===
Bully  -> mensajes: 8, pasos: 3
Anillo -> mensajes: 10, pasos: 10

### Comparación por tamaños de red

Desde la carpeta `src`:

cd src
python comparacion.py

Este script ejecuta ambos algoritmos con redes de 5, 10, 15, 20, 30 y 50 nodos (sin nodos desactivados) y guarda los resultados en `data/resultados.csv`.

Resultado verificado en ejecución real (n=5 hasta n=50):

| tamaño_red | mensajes_bully | pasos_bully | mensajes_anillo | pasos_anillo |
|---|---|---|---|---|
| 5 | 9 | 3 | 10 | 10 |
| 10 | 19 | 3 | 20 | 20 |
| 15 | 29 | 3 | 30 | 30 |
| 20 | 39 | 3 | 40 | 40 |
| 30 | 59 | 3 | 60 | 60 |
| 50 | 99 | 3 | 100 | 100 |

**Nota sobre complejidad:** en esta implementación específica (red completa, sin nodos desactivados), Bully genera `2n-1` mensajes y Anillo genera `2n` mensajes — ambos con crecimiento lineal O(n) respecto al número de nodos. Esto se debe a que el nodo iniciador contacta directamente al vecino de mayor id en una red completa, a diferencia del algoritmo Bully clásico teórico (García-Molina, 1982), donde cada nodo intermedio puede reiniciar su propia sub-elección, lo cual puede producir hasta O(n²) mensajes en el peor caso. Esta diferencia entre la cota teórica y el comportamiento medido debe explicarse en el informe técnico.

### Pruebas unitarias

Desde la raíz del repositorio:

python -m unittest test.pruebas_unitarias -v

Resultado verificado en ejecución real: 8 pruebas, todas `OK` (4 para Bully, 4 para Anillo).

## Integrantes

ANDERSON JHOMAR SALINAS PATRICIO 
JUAN DAVID TAFUR PALOMINO 
FABRIZIO ANDRE TRUJILLO CORMAN 
GIUSEPPE ALESSANDRO VERDE RODRIGUEZ 
ARIAN FABRIZIO VIZCACHO AMESQUITA


## Docente / Curso
MARCELINO TORRES VILLANUEVA  
Análisis de Algoritmos y Estrategias de Programación - UPN, Ciclo 2026-1





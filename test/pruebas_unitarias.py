import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import unittest
from modelos.red import Red
from algoritmos.bully import Bully

class TestBully(unittest.TestCase):

    def test_lider_es_el_id_mas_alto_activo(self):
        red = Red()
        red.crear_red_completa(6)
        red.desactivar_nodo(6)
        bully = Bully(red)
        lider = bully.iniciar_eleccion(2)
        self.assertEqual(lider, 5)

    def test_nodo_inactivo_no_puede_ganar(self):
        red = Red()
        red.crear_red_completa(4)
        red.desactivar_nodo(4)
        bully = Bully(red)
        lider = bully.iniciar_eleccion(1)
        self.assertEqual(lider, 3)
        self.assertFalse(red.nodos[4].es_lider)

    def test_todos_los_nodos_activos_conocen_al_lider(self):
        red = Red()
        red.crear_red_completa(5)
        bully = Bully(red)
        lider = bully.iniciar_eleccion(1)
        for id_nodo in red.nodos_activos():
            if id_nodo != lider:
                self.assertEqual(red.nodos[id_nodo].lider_actual, lider)

    def test_contador_registra_mensajes(self):
        red = Red()
        red.crear_red_completa(3)
        bully = Bully(red)
        bully.iniciar_eleccion(1)
        self.assertGreater(bully.contador.total_mensajes, 0)
        self.assertGreater(bully.contador.pasos, 0)

from algoritmos.anillo import Anillo

class TestAnillo(unittest.TestCase):

    def test_lider_es_el_id_mas_alto_activo(self):
        red = Red()
        red.crear_red_completa(6)
        red.desactivar_nodo(6)
        anillo = Anillo(red, [1, 2, 3, 4, 5, 6])
        lider = anillo.iniciar_eleccion(2)
        self.assertEqual(lider, 5)

    def test_nodo_inactivo_no_puede_ganar(self):
        red = Red()
        red.crear_red_completa(4)
        red.desactivar_nodo(4)
        anillo = Anillo(red, [1, 2, 3, 4])
        lider = anillo.iniciar_eleccion(1)
        self.assertEqual(lider, 3)
        self.assertFalse(red.nodos[4].es_lider)

    def test_todos_los_nodos_activos_conocen_al_lider(self):
        red = Red()
        red.crear_red_completa(5)
        anillo = Anillo(red, [1, 2, 3, 4, 5])
        lider = anillo.iniciar_eleccion(1)
        for id_nodo in red.nodos_activos():
            if id_nodo != lider:
                self.assertEqual(red.nodos[id_nodo].lider_actual, lider)

    def test_contador_registra_mensajes(self):
        red = Red()
        red.crear_red_completa(3)
        anillo = Anillo(red, [1, 2, 3])
        anillo.iniciar_eleccion(1)
        self.assertGreater(anillo.contador.total_mensajes, 0)
        self.assertGreater(anillo.contador.pasos, 0)
class TestFallosMidElection(unittest.TestCase):

    def test_bully_salta_al_nodo_que_falla(self):
        red = Red()
        red.crear_red_completa(6)
        bully = Bully(red)
        # El nodo 6 (el mayor) falla justo al recibir el mensaje de eleccion
        lider = bully.iniciar_eleccion(1, nodo_que_falla=6)
        self.assertEqual(lider, 5)
        self.assertFalse(red.nodos[6].activo)

    def test_anillo_salta_al_nodo_que_falla(self):
        red = Red()
        red.crear_red_completa(6)
        anillo = Anillo(red, [1, 2, 3, 4, 5, 6])
        # El nodo 4 falla en el segundo paso del recorrido
        lider = anillo.iniciar_eleccion(1, nodo_que_falla=4, paso_de_falla=2)
        self.assertEqual(lider, 6)
        self.assertFalse(red.nodos[4].activo)
class TestCasosLimite(unittest.TestCase):

    def test_red_de_dos_nodos(self):
        red = Red()
        red.crear_red_completa(2)
        bully = Bully(red)
        lider = bully.iniciar_eleccion(1)
        self.assertEqual(lider, 2)

    def test_iniciador_ya_es_el_maximo(self):
        red = Red()
        red.crear_red_completa(5)
        bully = Bully(red)
        lider = bully.iniciar_eleccion(5)
        self.assertEqual(lider, 5)
        self.assertEqual(bully.contador.total_mensajes, 4)

    def test_anillo_iniciador_ya_es_el_maximo(self):
        red = Red()
        red.crear_red_completa(5)
        anillo = Anillo(red, [1, 2, 3, 4, 5])
        lider = anillo.iniciar_eleccion(5)
        self.assertEqual(lider, 5)

if __name__ == "__main__":
    unittest.main()
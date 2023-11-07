from estadisticas import Estadisticas
class Jugador:
    def __init__(
        self, nombre: str, posicion: str, estadisticas: Estadisticas, logros: list[str]
    ):
        self.nombre = nombre
        self.posicion = posicion
        self.estadisticas = Estadisticas
        self.logros = logros

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self, nueva_posicion):
        self._posicion = nueva_posicion

    @property
    def estadisticas(self):
        return self._estadisticas

    @estadisticas.setter
    def estadisticas(self, nuevas_estadisticas):
        self._estadisticas = nuevas_estadisticas

    @property
    def logros(self):
        return self._logros

    @logros.setter
    def logros(self, nuevos_logros):
        self._logros = nuevos_logros

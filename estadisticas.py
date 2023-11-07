import json


class Estadisticas:
    def __init__(self, diccionario: dict):
        self._temporadas = diccionario.get("temporadas")
        self._puntos_totales = diccionario.get("puntos_totales")
        self._promedio_puntos_por_partido = diccionario.get(
            "promedio_puntos_por_partido"
        )
        self._rebotes_totales = diccionario.get("rebotes_totales")
        self._promedio_rebotes_por_partido = diccionario.get(
            "promedio_rebotes_por_partido"
        )
        self._asistencias_totales = diccionario.get("asistencias_totales")
        self._promedio_asistencias_por_partido = diccionario.get(
            "promedio_asistencias_por_partido"
        )
        self._robos_totales = diccionario.get("robos_totales")
        self._bloqueos_totales = diccionario.get("bloqueos_totales")
        self._porcentaje_tiros_de_campo = diccionario.get("porcentaje_tiros_de_campo")
        self._porcentaje_tiros_libres = diccionario.get("porcentaje_tiros_libres")
        self._porcentaje_tiros_triples = diccionario.get("porcentaje_tiros_triples")


      # Getters, Setters y properties
    @property
    def temporadas(self):
        return self._temporadas

    @temporadas.setter
    def temporadas(self, value):
        if isinstance(value, int):
            self._temporadas = value
        else:
            raise ValueError("Ingrese un valor correcto")

    @property
    def puntos_totales(self):
        return self._puntos_totales

    @puntos_totales.setter
    def puntos_totales(self, value):
        if isinstance(value, int):
            self._puntos_totales = value
        else:
            raise ValueError("Ingrese un valor correcto")

    @property
    def promedio_puntos_por_partido(self):
        return self._promedio_puntos_por_partido

    @promedio_puntos_por_partido.setter
    def promedio_puntos_por_partido(self, value):
        if isinstance(value, float):
            self._promedio_puntos_por_partido = value
        else:
            raise ValueError("Ingrese un valor correcto")

    @property
    def rebotes_totales(self):
        return self._rebotes_totales

    @rebotes_totales.setter
    def rebotes_totales(self, value):
        if isinstance(value, int):
            self._rebotes_totales = value
        else:
            raise ValueError("Ingrese un valor correcto")

    @property
    def promedio_rebotes_por_partido(self):
        return self._promedio_rebotes_por_partido

    @promedio_rebotes_por_partido.setter
    def promedio_rebotes_por_partido(self, value):
        if isinstance(value, float):
            self._promedio_rebotes_por_partido = value
        else:
            raise ValueError("Ingrese un valor correcto")

    @property
    def asistencias_totales(self):
        return self._asistencias_totales

    @asistencias_totales.setter
    def asistencias_totales(self, value):
        if isinstance(value, int):
            self._asistencias_totales = value
        else:
            raise ValueError("Ingrese un valor correcto")

    @property
    def promedio_asistencias_por_partido(self):
        return self._promedio_asistencias_por_partido

    @promedio_asistencias_por_partido.setter
    def promedio_asistencias_por_partido(self, value):
        if isinstance(value, float):
            self._promedio_asistencias_por_partido = value
        else:
            raise ValueError("Ingrese un valor correcto")

    @property
    def robos_totales(self):
        return self._robos_totales

    @robos_totales.setter
    def robos_totales(self, value):
        if isinstance(value, int):
            self._robos_totales = value
        else:
            raise ValueError("Ingrese un valor correcto")

    @property
    def bloqueos_totales(self):
        return self._bloqueos_totales

    @bloqueos_totales.setter
    def bloqueos_totales(self, value):
        if isinstance(value, int):
            self._bloqueos_totales = value
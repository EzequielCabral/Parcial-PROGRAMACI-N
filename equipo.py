import json
import re
from estadisticas import Estadisticas
from jugador import Jugador
RUTA_FILES = "C:/Users/Eze_c/OneDrive/Escritorio/Pygame/Parcial"
#Definimos la ruta donde vamos a guardar los archivos


class Equipo:
    def __init__(self):
        self.jugadores = []  #creamos una lista vacía de jugadores.

    def cargar_desde_json(self, dream_team_file):
        with open(dream_team_file, "r") as json_file:
            data = json.load(json_file)  #Cargamos los datos del archivo JSON.
            jugadores_data = data.get('jugadores')  #Obtenemos la lista de datos de los jugadores.

            #Recorremos los datos de cada jugador en la lista.
            for jugador_data in jugadores_data:
                estadisticas_data = jugador_data.get("estadisticas", {})
                nombre = jugador_data["nombre"]
                posicion = jugador_data["posicion"]
                estadisticas = Estadisticas(estadisticas_data)
                logros = jugador_data.get("logros", [])
                #cargamos los datos en los atributos correspondientes
                jugador = Jugador(nombre, posicion, estadisticas, logros)
                self.jugadores.append(jugador)
                #agregamos a la lista el objeto jugador
        
    def mostrar_jugadores(self): # Metodo para mostrar jugadores
        for jugador in self.jugadores:
            print(f"{jugador.nombre} - {jugador.posicion}")

    def ver_estadisticas_del_jugador(self): # Metodo para visualizar estadisticas del jugador seleccionado por su indice
        while True: #entramos en un bucle infinito 
            indice_seleccionado = input("Ingrese el número de índice del jugador que desea ver: ")
            if indice_seleccionado.isdigit(): #validamos que el indice elegido sea numerico
                index = int(indice_seleccionado) # declaramos la variable indice
                if 1 <= index <= len(self.jugadores): # si el indice es mayor o igual a 1 y es mejor o igual al total de jugadores
                    break  # cortamos el bucle infinoto
                else:
                    print('Índice fuera de rango. Ingrese un valor válido.')
            else:
                print('Ingrese un número válido.')
        self.jugador_actual = self.jugadores[index - 1] #el jugador seleccionado es el jugador posicionado en el indice -1
        #estadisticas = self.jugador_actual.estadisticas #esto es poruqe para el usuario no es habitual que listas empiecen en 0
        print(f"Estadísticas de {self.jugador_actual.nombre} ({self.jugador_actual.posicion}):")
        print(f"Temporadas jugadas: {self.jugador_actual.estadisticas.temporadas}")
        print(f"Puntos totales: {self.jugador_actual.estadisticas.puntos_totales}")
        print(f"Promedio de puntos por partido: {self.jugador_actual.estadisticas.promedio_puntos_por_partido}")
        print(f"Rebotes totales: {self.jugador_actual.estadisticas.rebotes_totales}")
        print(f"Promedio de rebotes por partido: {self.jugador_actual.estadisticas.promedio_rebotes_por_partido}")
        print(f"Asistencias totales: {self.jugador_actual.estadisticas.asistencias_totales}")
        print(f"Promedio de asistencias por partido: {self.jugador_actual.estadisticas.promedio_asistencias_por_partido}")
        print(f"Robos totales: {self.jugador_actual.estadisticas.robos_totales}")
        print(f"Bloqueos totales: {self.jugador_actual.estadisticas.bloqueos_totales}")
        print(f"Porcentaje de tiros de campo: {self.jugador_actual.estadisticas.porcentaje_tiros_de_campo}")
        print(f"Porcentaje de tiros libres: {self.jugador_actual.estadisticas.porcentaje_tiros_libres}%")
        print(f"Porcentaje de tiros triples: {self.jugador_actual.estadisticas.porcentaje_tiros_triples}%")
    
    def guardar_estadisticas_jugador_csv(self): # Metodo para guardas las estadisticas del jugador seleccionado anteriormente en un archivo CSV
        if not self.jugador_actual:
            print("Primero debe seleccionar un jugador con la opción anterior")
            return

        estadisticas_jugador = self.jugador_actual.estadisticas  # Obtén las estadísticas del jugador

        datos_jugador = [
            self.jugador_actual.nombre,
            self.jugador_actual.posicion,
            estadisticas_jugador.temporadas,
            estadisticas_jugador.puntos_totales,
            estadisticas_jugador.promedio_puntos_por_partido,
            estadisticas_jugador.rebotes_totales,
            estadisticas_jugador.promedio_rebotes_por_partido,
            estadisticas_jugador.asistencias_totales,
            estadisticas_jugador.promedio_asistencias_por_partido,
            estadisticas_jugador.robos_totales,
            estadisticas_jugador.bloqueos_totales,
            estadisticas_jugador.porcentaje_tiros_de_campo,
            estadisticas_jugador.porcentaje_tiros_libres,
            estadisticas_jugador.porcentaje_tiros_triples
        ]

        nombre_archivo_csv = f"{RUTA_FILES}/Estadisticas_{self.jugador_actual.nombre}.csv"

        try:
            with open(nombre_archivo_csv, 'w', newline='') as file:
                # Escribe el encabezado
                encabezado = ["Nombre", "Posición", "Temporadas", "Puntos Totales", "Promedio Puntos por Partido", "Rebotes Totales", "Promedio Rebotes por Partido", "Asistencias Totales", "Promedio Asistencias por Partido", "Robos Totales", "Bloqueos Totales", "Porcentaje Tiros de Campo", "Porcentaje Tiros Libres", "Porcentaje Tiros Triples"]
                file.write(','.join(encabezado) + '\n')
                #
                # Escribe los datos del jugador
                fila_jugador = [str(dato) for dato in datos_jugador]
                file.write(','.join(fila_jugador) + '\n')

            print(f'Estadísticas de {self.jugador_actual.nombre} guardadas en el archivo CSV.')
        except Exception:
            print('Ocurrió un error al intentar guardar el archivo:', str(e))
    
    def buscar_jugador_por_nombre(self): # Buscamos un jugador por el nombre
        nombre_buscado = input("Ingrese el nombre del jugador que desea buscar: ")
        jugador_encontrado = None

        for jugador in self.jugadores: #recorremos la lista de jugadores
            if re.search(f"^{re.escape(nombre_buscado)}$", jugador.nombre, re.IGNORECASE):  #validamos con regex
                jugador_encontrado = jugador
                break

        if jugador_encontrado: 
            logros = jugador_encontrado.logros #extraemos los logros del objeto jugador
            print(f"Logros de {jugador_encontrado.nombre} ({jugador_encontrado.posicion}):")
            for logro in logros: 
                print(logro)
        else:
            print(f"No se encontró un jugador con el nombre '{nombre_buscado}'.")

    def promedio_puntos_por_partido(self): #metodo para calcular el promedio de puntos por partido
        promedios = []
        for jugador in self.jugadores:
            puntos_totales = jugador.estadisticas.puntos_totales
            temporadas = jugador.estadisticas.temporadas
            temporadas = int(temporadas)
            if temporadas > 0:
                promedio = puntos_totales / temporadas
                promedios.append((jugador.nombre, promedio))
        return promedios

    def mostrar_promedio_puntos_por_partido(self): #metodo para mostrar el promedio de puntos por partido
        promedios = self.promedio_puntos_por_partido()
        promedios.sort(key=lambda x: x[0])
        for nombre, promedio in promedios:
            print(f"{nombre}: {promedio:.2f} puntos por partido")
  
    def buscar_miembros_salon_fama(self): # Buscar jugadores pertenecientes al salon de la fama por nombre
        jugador_buscado = int("Ingrese el jugador que quiere buscar")
        for jugador in self.jugadores:
            if re.search(jugador_buscado, jugador.nombre, re.I):  # re.I para hacer la búsqueda insensible a mayúsculas/minúsculas
                if "miembro del salon de la fama" in jugador.logros:
                    print(f"{jugador.nombre} es miembro del salon de la fama!")
 
    def encontrar_mejor_rebote(self): #metodo para encontrar el jugador con mas rebotes
        mejor_jugador = None
        max_rebotes = 0

        for jugador in self.jugadores:
            rebotes_totales = jugador.estadisticas.rebotes_totales

            if rebotes_totales > max_rebotes:
                max_rebotes = rebotes_totales
                mejor_jugador = jugador
        print (f'el jugador con más rebotes es {mejor_jugador}')

    def ordenar_jugador_por_temporada_quicksort(self, jugadores, inicio, fin):
        if inicio < fin:  #Esta condición es importante para detener la recursión cuando ya no hay elementos para ordenar en la sublista
            # Division
            pivote = self.division(jugadores, inicio, fin)  #Llamamos al metodo division para encontrar el pivote

            # Recursivamente ordenar las dos mitades
            self.ordenar_jugador_por_temporada_quicksort(jugadores, inicio, pivote - 1)  #elementos menor q el pivote
            self.ordenar_jugador_por_temporada_quicksort(jugadores, pivote + 1, fin)  #elemetnos mayores q el pivote

    def division(self, jugadores, inicio, fin):
        pivote = jugadores[fin].estadisticas.temporadas  # Elegimos el pivote como el número de 
        i = inicio - 1                                   # temporadas jugadas del último jugador en la sublista.
        #Esta variable se utilizará para rastrear el índice del último elemento que es menor o igual al pivote
        for j in range(inicio, fin):
            if jugadores[j].estadisticas.temporadas <= pivote:   #Comparamos el número de temporadas jugadas del jugador en la posición j con el pivote.
                i += 1                                           # Si el jugador tiene igual o menos temporadas que el pivote, continuamos.
            # sumanos 1 a i para marcar el nuevo límite entre los elementos menores o iguales al pivote. 
            # Intercambiamos la posición del jugador en i con la posición del jugador en j. 
            # Esto coloca al jugador en la posición j en la parte de elementos menores o iguales al pivote.                                               
                jugadores[i], jugadores[j] = jugadores[j], jugadores[i]

        jugadores[i + 1], jugadores[fin] = jugadores[fin], jugadores[i + 1]
        #intercambiamos el pivote (que se encuentra en la posición fin) con el elemento en i + 1, 
        # lo que coloca al pivote en su posición final en la sublista.
        return i + 1

    def mostrar_jugadores_ordenados(self): #mostrar los jugadores anteriores ordenados
        if not self.jugadores:
            print("No hay jugadores para mostrar.")
            return

        jugadores_ordenados = self.jugadores.copy()
        self.ordenar_jugador_por_temporada_quicksort(jugadores_ordenados, 0, len(jugadores_ordenados) - 1)

        print("Listado de jugadores ordenados por TEMPORADAS JUGADAS (menor a mayor):")
        for jugador in jugadores_ordenados:
            print(f"{jugador.nombre} - Temporadas Jugadas: {jugador.estadisticas.temporadas}")

    def guardar_jugadores_ordenados_csv(self): 
        if not self.jugadores:
            print("No hay jugadores para guardar.")
            return

        jugadores_ordenados = self.jugadores.copy()
        self.ordenar_jugador_por_temporada_quicksort(jugadores_ordenados, 0, len(jugadores_ordenados) - 1)

        for jugador in jugadores_ordenados:
            nombre_archivo_csv = f"{RUTA_FILES}/{jugador.nombre.split()[-1]}.csv"

            try:
                with open(nombre_archivo_csv, 'w', newline='') as file:
                    encabezado = ["Nombre", "Posición", "Temporadas", "Puntos Totales", "Promedio Puntos por Partido", "Rebotes Totales", "Promedio Rebotes por Partido", "Asistencias Totales", "Promedio Asistencias por Partido", "Robos Totales", "Bloqueos Totales", "Porcentaje Tiros de Campo", "Porcentaje Tiros Libres", "Porcentaje Tiros Triples"]
                    file.write(','.join(encabezado) + '\n')

                    datos_jugador = [
                        jugador.nombre,
                        jugador.posicion,
                        jugador.estadisticas.temporadas,
                        jugador.estadisticas.puntos_totales,
                        jugador.estadisticas.promedio_puntos_por_partido,
                        jugador.estadisticas.rebotes_totales,
                        jugador.estadisticas.promedio_rebotes_por_partido,
                        jugador.estadisticas.asistencias_totales,
                        jugador.estadisticas.promedio_asistencias_por_partido,
                        jugador.estadisticas.robos_totales,
                        jugador.estadisticas.bloqueos_totales,
                        jugador.estadisticas.porcentaje_tiros_de_campo,
                        jugador.estadisticas.porcentaje_tiros_libres,
                        jugador.estadisticas.porcentaje_tiros_triples
                    ]

                    fila_jugador = [str(dato) for dato in datos_jugador]
                    file.write(','.join(fila_jugador) + '\n')

                print(f'Listado de jugadores ordenado guardado en el archivo CSV: {nombre_archivo_csv}')
            except Exception:
                print('Ocurrió un error al intentar guardar el archivo:')

    def guardar_jugadores_ordenados_json(self): #metodo para guardar la lista de jugadores ordenados en JSON
        if not self.jugadores:
            print("No hay jugadores para guardar.")
            return

        jugadores_ordenados = self.jugadores.copy()
        self.ordenar_jugador_por_temporada_quicksort(jugadores_ordenados, 0, len(jugadores_ordenados) - 1)

        print("Listado de jugadores ordenados por TEMPORADAS JUGADAS (menor a mayor):")
        for jugador in jugadores_ordenados:
            print(f"{jugador.nombre} - Temporadas Jugadas: {jugador.estadisticas.temporadas}")

        nombre_archivo = input("Ingrese el nombre del archivo JSON para guardar los jugadores ordenados: ")

        if re.match(r'^[a-zA-Z0-9_.-]+$', nombre_archivo):  #Validación por REGEX
            with open(nombre_archivo, 'w') as json_file:
                jugadores_json = [{"nombre": jugador.nombre, "temporadas": jugador.estadisticas.temporadas} for jugador in jugadores_ordenados]
                json.dump(jugadores_json, json_file, indent=4)
                print(f"Jugadores ordenados guardados en el archivo {nombre_archivo}.json")
        else:
            print("Nombre de archivo no válido. Debe contener solo letras, números, guiones bajos (_) y guiones (-).")

    def quicksort_por_robos_y_bloqueos(self, jugadores, inicio, fin):
        if inicio < fin:
            pivote = self.division_por_robos_y_bloqueos(jugadores, inicio, fin)
            self.quicksort_por_robos_y_bloqueos(jugadores, inicio, pivote - 1)
            self.quicksort_por_robos_y_bloqueos(jugadores, pivote + 1, fin)

    def division_por_robos_y_bloqueos(self, jugadores, inicio, fin):
        pivote = jugadores[fin].estadisticas.robos_totales + jugadores[fin].estadisticas.bloqueos_totales
        i = inicio - 1

        for j in range(inicio, fin):
            total_robos_bloqueos_j = jugadores[j].estadisticas.robos_totales + jugadores[j].estadisticas.bloqueos_totales
            if total_robos_bloqueos_j >= pivote:
                i += 1
                jugadores[i], jugadores[j] = jugadores[j], jugadores[i]

        jugadores[i + 1], jugadores[fin] = jugadores[fin], jugadores[i + 1]
        return i + 1

    def mostrar_jugador_ordenados_por_robos_y_bloqueos(self): # Metodo para mostrar jugadores ordenados anteriormente
        if not self.jugadores:
            print("No hay jugadores para ordenar.")
            return

        jugadores_ordenados = self.jugadores.copy()
        self.quicksort_por_robos_y_bloqueos(jugadores_ordenados, 0, len(jugadores_ordenados) - 1)

        print("Listado de jugadores ordenados por Robos + Bloqueos (mayor a menor):")
        for jugador in jugadores_ordenados:
            total_robos_bloqueos = jugador.estadisticas.robos_totales + jugador.estadisticas.bloqueos_totales
            print(f"{jugador.nombre} - Robos + Bloqueos: {total_robos_bloqueos}")

    def listar_jugadores_con_porcentaje(self): #metodo para listar los jugadores segun el porcentaje del total de la suma de robos y bloqueos
        if not self.jugadores:
            print("No hay jugadores para listar.")
            return

        jugadores_ordenados = self.jugadores.copy()
        self.quicksort_por_robos_y_bloqueos(jugadores_ordenados, 0, len(jugadores_ordenados) - 1)

        if not jugadores_ordenados:
            print("No hay jugadores para listar.")
            return

        max_robos_bloqueos = jugadores_ordenados[0].estadisticas.robos_totales + jugadores_ordenados[0].estadisticas.bloqueos_totales

        print("Listado de jugadores ordenados por Robos + Bloqueos (mayor a menor) y porcentaje:")
        for jugador in jugadores_ordenados:
            total_robos_bloqueos = jugador.estadisticas.robos_totales + jugador.estadisticas.bloqueos_totales
            porcentaje = (total_robos_bloqueos / max_robos_bloqueos) * 100
            print(f"{jugador.nombre} - Robos + Bloqueos: {total_robos_bloqueos}, Porcentaje: {porcentaje:.2f}%")

    def listar_jugadores_con_porcentaje_filtrado(self): #
        if not self.jugadores:
            print("No hay jugadores para listar.")
            return

        jugadores_ordenados = self.jugadores.copy()
        self.quicksort_por_robos_y_bloqueos(jugadores_ordenados, 0, len(jugadores_ordenados) - 1)

        if not jugadores_ordenados:
            print("No hay jugadores para listar.")
            return

        max_robos_bloqueos = jugadores_ordenados[0].estadisticas.robos_totales + jugadores_ordenados[0].estadisticas.bloqueos_totales
        cantidad_jugadores = int(input("Ingrese la cantidad de jugadores a mostrar: "))

        if cantidad_jugadores > len(jugadores_ordenados):
            cantidad_jugadores = len(jugadores_ordenados)

        print(f"Listado de los primeros {cantidad_jugadores} jugadores ordenados por Robos + Bloqueos (mayor a menor) y porcentaje:")
        for i in range(cantidad_jugadores):
            jugador = jugadores_ordenados[i]
            total_robos_bloqueos = jugador.estadisticas.robos_totales + jugador.estadisticas.bloqueos_totales
            porcentaje = (total_robos_bloqueos / max_robos_bloqueos) * 100
            print(f"{i + 1}. {jugador.nombre} - Robos + Bloqueos: {total_robos_bloqueos}, Porcentaje: {porcentaje:.2f}%")





    


   
 


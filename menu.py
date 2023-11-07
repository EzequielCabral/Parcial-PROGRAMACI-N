from equipo import Equipo

equipo = Equipo()

equipo.cargar_desde_json("C:/Users/Eze_c/OneDrive/Escritorio/Pygame/Parcial/dream_team.json")


def menu():
    opcion_elegida = input("Ingrese la opción deseada")
    opcion_elegida = int(opcion_elegida)
    if opcion_elegida == 1:
        equipo.mostrar_jugadores()
    elif opcion_elegida == 2:
        equipo.ver_estadisticas_del_jugador()
    elif opcion_elegida == 3:
        equipo.guardar_estadisticas_jugador_csv()
        equipo.__crear_formato_csv()
    elif opcion_elegida == 4:
        equipo.buscar_jugador_por_nombre()
    elif opcion_elegida == 5:
        equipo.promedio_puntos_por_partido()
        equipo.mostrar_promedio_puntos_por_partido()
    elif opcion_elegida == 6:
        equipo.buscar_miembros_salon_fama()
    elif opcion_elegida == 7:
        equipo.encontrar_mejor_rebote()
    elif opcion_elegida == 8:
        equipo.ordenar_jugadores_por_temporadas_jugada_orden_descendente()
    else:
        print ("Error, ingrese un numero valido (Enteros del 1 al 7)")
        return
menu()
         
       
        

        
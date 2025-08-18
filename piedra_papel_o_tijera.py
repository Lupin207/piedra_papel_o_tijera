import random

ultimo_resumen = None
ultimas_estadisticas = None

def mostrar_reglas():
    print("\n=== REGLAS DEL JUEGO ===")
    print("1. Cada jugador debe elegir entre Piedra, Papel o Tijera.")
    print("2. Piedra gana a Tijera, Tijera gana a Papel, Papel gana a Piedra.")
    print("3. En modo 1 jugador: juegas solo, pero igual se registra tu elección.")
    print("4. En modo contra la computadora: compites contra la máquina.")
    print("5. En modo multijugador: dos jugadores compiten entre sí.")
    print("6. Se pueden definir un número de partidas o jugar libremente hasta salir.\n")

def jugar_una_partida(eleccion_j1, eleccion_j2, jugador1, jugador2):
    if eleccion_j1 == eleccion_j2:
        return f"{jugador1} empató - {jugador2} empató", "empate"
    elif (eleccion_j1 == "PIEDRA" and eleccion_j2 == "TIJERA") or \
         (eleccion_j1 == "TIJERA" and eleccion_j2 == "PAPEL") or \
         (eleccion_j1 == "PAPEL" and eleccion_j2 == "PIEDRA"):
        return f"{jugador1} ganó - {jugador2} perdió", "j1"
    else:
        return f"{jugador1} perdió - {jugador2} ganó", "j2"

def pedir_eleccion(nombre):
    while True:
        eleccion = input(f"{nombre}, elige Piedra, Papel o Tijera: ").upper()
        if eleccion in ["PIEDRA", "PAPEL", "TIJERA"]:
            return eleccion
        else:
            print("Opción inválida. Intenta de nuevo.")

def modo_juego(tipo):
    global ultimo_resumen, ultimas_estadisticas

    if tipo == "1":
        jugador1 = input("Ingrese el nombre del jugador: ")
        jugador2 = "Sistema"
    elif tipo == "2":
        jugador1 = input("Ingrese el nombre del jugador 1: ")
        jugador2 = "Computadora"
    else:
        jugador1 = input("Ingrese el nombre del jugador 1: ")
        jugador2 = input("Ingrese el nombre del jugador 2: ")

    resumen = []
    estadisticas = {jugador1: {"gano": 0, "perdio": 0, "empato": 0},
                    jugador2: {"gano": 0, "perdio": 0, "empato": 0}}

    definir = input("¿Desea definir un número de partidas? (si/no): ").lower()
    if definir == "si":
        n = int(input("Ingrese el número de partidas: "))
        jugar_partidas(n, tipo, jugador1, jugador2, resumen, estadisticas)
    else:
        seguir = "si"
        while seguir == "si":
            jugar_partidas(1, tipo, jugador1, jugador2, resumen, estadisticas)
            seguir = input("¿Desea jugar otra partida? (si/no): ").lower()

    ultimo_resumen = resumen
    ultimas_estadisticas = estadisticas

    mostrar_resultados(resumen, estadisticas)

def jugar_partidas(num, tipo, jugador1, jugador2, resumen, estadisticas):
    for i in range(num):
        if tipo == "1":  
            eleccion_j1 = pedir_eleccion(jugador1)
            eleccion_j2 = "N/A"
        elif tipo == "2": 
            eleccion_j1 = pedir_eleccion(jugador1)
            eleccion_j2 = random.choice(["PIEDRA", "PAPEL", "TIJERA"])
        else:  
            eleccion_j1 = pedir_eleccion(jugador1)
            eleccion_j2 = pedir_eleccion(jugador2)

        resultado, ganador = jugar_una_partida(eleccion_j1, eleccion_j2, jugador1, jugador2)
        resumen.append(f"Partida {len(resumen)+1}: {resultado}")

        if ganador == "j1":
            estadisticas[jugador1]["gano"] += 1
            estadisticas[jugador2]["perdio"] += 1
        elif ganador == "j2":
            estadisticas[jugador1]["perdio"] += 1
            estadisticas[jugador2]["gano"] += 1
        else:
            estadisticas[jugador1]["empato"] += 1
            estadisticas[jugador2]["empato"] += 1

def mostrar_resultados(resumen, estadisticas):
    print("\n=== RESUMEN DE PARTIDAS ===")
    print(f"Número de partidas realizadas: {len(resumen)}")
    for r in resumen:
        print(r)
    print("\n=== ESTADÍSTICAS ===")
    for jugador, datos in estadisticas.items():
        print(f"{jugador}: ganó {datos['gano']} partidas, perdió {datos['perdio']} partidas, empató {datos['empato']} partidas")
    print()

def ver_estadisticas():
    global ultimo_resumen, ultimas_estadisticas
    if ultimo_resumen and ultimas_estadisticas:
        mostrar_resultados(ultimo_resumen, ultimas_estadisticas)
    else:
        print("\nNo hay estadísticas recientes.\n")

def menu_juego():
    while True:
        print("\n=== MENÚ DE OPCIONES PARA JUGAR ===")
        print("1. Un solo jugador")
        print("2. Contra la computadora")
        print("3. Multijugador (2 jugadores)")
        print("4. Ver estadísticas del último set de partidas")
        print("5. Regresar al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion in ["1", "2", "3"]:
            modo_juego(opcion)
        elif opcion == "4":
            ver_estadisticas()
        elif opcion == "5":
            break
        else:
            print("Opción inválida, intente nuevamente.")

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Jugar")
        print("2. Reglas del juego")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_juego()
        elif opcion == "2":
            mostrar_reglas()
        elif opcion == "3":
            print("Gracias por jugar :D. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida, intente nuevamente.")


menu_principal()

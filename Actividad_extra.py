equipos = {}

while True:
    print("---MENU---")
    print("1. Agregar equipo")
    print("2. Ingresar resultados")
    print("3. Mostrar tabla")
    print("4. Eliminar equipo")
    print("5. Salir")

    opcion = input("Elija una opcion:")

    if opcion == "1":
        nombre = input("Nombre del equipo: ")
        if nombre in equipos:
            print("Ese equipo ya existe")
        else:
            equipos[nombre] = 0 
            print("Equipo agregado")

    elif opcion == "2":
        local = input("Equipo local: ")
        visitante = input("Equipo visitante: ")
        marcador = input("Marcador (ej: 4-2):")

        if  local not in equipos or visitante  not in equipos:
            print("Alguno de los equipos no existe")
            continue
        
        if "-" not in marcador:
            print("Formato invalido")
            continue
        
        partes = marcador.split("-")

        if len(partes) != 2:
            print("Formato invalido")
            continue
        
        if not partes[0].isdigit() or not partes[1].isdigit():
            print("Formato invalido")
            continue
        
        goles_local = int(partes[0])
        goles_visitante = int(partes[1])

        if goles_local > goles_visitante:
            equipos[local] += 3
        elif goles_local < goles_visitante:
            equipos[visitante] += 3
        else:
            equipos[local] += 1
            equipos[visitante] += 1
        
        print("Resultado cargado")


    elif opcion == "3":
        print("TABLA DE POSICIONES:")
        tabla = sorted(equipos.items(), key=lambda x: x[1], reverse=True)

        for equipo, puntos in tabla:
            print(equipo, "-",puntos, "puntos")

    elif opcion == "4":
        nombre = input("Equipo a eliminar:")

        if nombre in equipos:
            del equipos[nombre]
            print("Equipo eliminado")
        else:
            print("Ese equipo no existe")
    
    elif opcion == "5":
        print("Saliendo del programa")
        break
    else:
        print("Opcion invalida")


            
    



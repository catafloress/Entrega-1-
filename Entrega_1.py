import random
categorias = {"programacion": ["python", "variable", "funcion", "bucle",]
, "basico": ["programa","cadena","entero","lista"]}

palabras_usadas = []

while True: 
    print("Categorías disponibles:")
    for cat in categorias:
        print("-", cat)

    categoria = input("Elegí una categoría: ")

    if categoria not in categorias:
        print("Categoría no válida\n")
        continue

    palabras_disponibles = []
    for word in categorias[categoria]:
        if word not in palabras_usadas:
            palabras_disponibles.append(word)

    if len(palabras_disponibles) == 0:
        print("Ya usaste todas las palabras de esta categoría")
        break

    palabra = random.choice(palabras_disponibles)
    palabras_usadas.append(word)

    guessed = []
    attempts = 6
    puntaje = 0

    print("¡Bienvenido al Ahorcado!")
    print()

    while attempts > 0:

# Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
# Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no valida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1 
            print ("Incorrecto")
    
    if attempts == 0:
        print("Perdiste. La palabra era: ", word)
        puntaje = 0

    print("Puntaje: ", puntaje)

    seguir = input("Queres jugar otra ronda? (s/n):")
    if seguir != "s":
        break
    

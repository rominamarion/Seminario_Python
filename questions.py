import random

words = ["python","programa","variable","funcion","bucle","cadena","entero","lista"]
words1 = ["tomate","salsa","pescado","tenedor","leche"]
words2 = ["colores","acuarelas","pinturas"]
diccionario = {"programación":words,"cocina":words1,"manualidades":words2}

print("¡Bienvenido al Ahorcado!")
print()

seguir = True

key = input("Elegir categoría: programación, cocina o manualidades ---> ")
pos = 0
nueva_lista = random.sample(diccionario.get(key),len(diccionario.get(key)))
while (seguir):  
    try:
        word = nueva_lista[pos]
        pos = pos + 1
        guessed = []
        attempts = 6
        score = 0
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
                score = 6 + score
                print("¡Ganaste!")
                print(f"Puntaje: {score}")
                break

            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")

            letter = input("Ingresá una letra: ")
            if len(letter) > 1 or not letter.isalpha():
                print()
                print("Entrada no válida")
            else:
                if letter in guessed:
                    print("Ya usaste esa letra.")
                elif letter in word:
                    guessed.append(letter)
                    print("¡Bien! Esa letra está en la palabra.")
                else:
                    guessed.append(letter)
                    attempts -= 1
                    score -= 1
                    print("Esa letra no está en la palabra.")

            print()
        else:
            print(f"¡Perdiste! La palabra era: {word}")
            print("Puntaje: 0")
        print()
        continuar = int(input("¿Desea continuar jugando? 1.Si  2.No ---> "))
        seguir = True if continuar == 1 else False
    except IndexError:
        print("No hay más palabras :(...")
        seguir = False #tambien podria ir un break?
else:
    print("Hasta luego :)...")
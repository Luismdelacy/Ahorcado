# Libreria
import random
# Variables
palabras = ["PYTHON","JAVA","PERL","GO","RUBY","JAVASCRIPT","PHP","FORTRAN","SWIFT","SQL","HTML","RUST"]
intentos = 10
letra = []
Continuar = True

# Funciones
def Menu ():
    print("""
-----------------------------------------
___________ Menu del juego ______________
0. -------- Instruciones ----------------
1. -------- Comenzar el juego -----------
2. -------- Finalizar el juego ----------
_________________________________________
____________ Luis María _________________
""")

def Random(palabras):
  return random.choice(palabras)

def Victoria():
    print("Enhorabuena has ganado 👏👏👏👏")
    

# Menú del Juego
while Continuar:

    Menu()
    opcion = input("Elige una opción: ")

    # Jugar
    if opcion == "1":
        print("Iniciando Ahorcado...")
        print("Bienvenido")

        palabraSecreta = Random(palabras)# Palabra aleatoria y ocultarla
        for letras in palabraSecreta:
            letra.append("_")
        print(" ".join(letra))

        while intentos >=0:
            letra_input = input("Escoge una letra: ")

            # Letra no adivinada
            if letra_input not in palabraSecreta:
                fallo = True
                Continuar = True
                intentos -= 1
                print("Has fallado, te quedan " + str(intentos) + " intentos")

            elif "_" not in letra:
                Victoria()
                Menu()

            # Letra adivinada
            else:
                Continuar = True
                print("Enhorabuena, has acertado!!!!!!")
                for x in range(len(palabraSecreta)):
                    if letra_input == palabraSecreta[x]:
                        letra[x] = letra_input
                print(" ".join(letra))

            if "_" not in letra:
                intentos = -1
                Victoria()
                    
        # Intentos
        if intentos <= 0:
            Continuar = False
            print("La palabra era: " + palabraSecreta )
            letra = []
            intentos = 10

    # Cerrar el juego
    elif opcion == "2":
        print("Se está cerrando el juego...")
        print("Gracias por jugar, hasta pronto.")
        Continuar = False

    # Instrucciones
    elif opcion == "0":
        print("""
    - Objetivos:
    Desarrollar el juego “Ahorcado” mediante el lenguaje de programación Python, utilizando las herramientas de control y estructuras vistas en clase.
    - Características:
    El programa cuenta con un banco de posibles palabras, que se ejecutarán aleatoriamente. Temática: Lenguajes de programación.
    El programa pide una letra al usuario.
    El programa comprueba la existencia de la letra en la palabra.
    Tienes 10 vidas por palabra, se restará una por cada fallo.
    El programa muentra la palabra con guiones en vez de las letras, cuando estás no hayan sido adivinadas. 
    Para salir pulsa 99.
        """)
        opcion = input("Elige una opción: ")

    elif opcion == "99":
        Menu()

    # Control
    else:
        print("Elige una opcion valida :(")
        print("Valores numéricos validos, (0 1 2 99)")

    # Empezar?
    Continuar = bool(input("¿Continuar? Pulsa cualquier letra para continuar o por el conrario pulsa Enter para finalizar: ")) # Escribe cualquier palabra para continuar con el programa.
    
    # @luismdelacy
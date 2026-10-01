 1. 
nombre = input(" Por favor digite su nombre")
apellido = input("Ahora,digite su apellido")
edad = int(input("Su edad "))
direccion = input("Su direccion ")
numero = int(input(" Su numero de telefono "))
genero = input("Su genero")
print(nombre)
print(apellido)
print(edad)
print(direccion)
print(numero)
print(genero)

2.
print("Ingrese los valores para efectuar la suma")
num_1 = int(input("Ingrese el primer valor "))
num_2 = int(input("Ingrese el segundo valor "))
resultado = num_1 + num_2
print(resultado)

print("Ingrese los valores para efectuar la resta")
num_3 = int(input("Ingrese el primer valor "))
num_4 = int(input("Ingrese el segundo valor "))
resultado_resta = num_3 - num_4
print(resultado_resta)

print("Ingrese los valores para efectuar la multiplicacion")
num_5 = int(input("Ingrese el primer valor "))
num_6 = int(input("Ingrese el segundo valor "))
resultado_multi = num_5 * num_6
print(resultado_multi)

print("Ingrese los valores para efectuar la division")
num_7 = int(input("Ingrese el primer valor "))
num_8 = int(input("Ingrese el segundo valor "))
if num_8 != 0:
    res_div = num_7 / num_8
    print(res_div)
else:
    print("Error: No se puede dividir entre cero.\n")

print("Ingrese los valores para efectuar la potencia")
num_9 = int(input("Ingrese el valor de la base "))
num_10 = int(input("Ingrese el valor del exponente "))
resultado_poten = num_9 ** num_10
print(resultado_poten)
import math
num_raiz = int(input("Ingrese el número para calcular su raíz cuadrada: "))
if num_raiz >= 0:
    res_raiz = math.sqrt(num_raiz)
    print(f"Resultado: La raíz cuadrada de {num_raiz} es = {res_raiz}\n")
else:
    print("Error: No se puede calcular la raíz cuadrada de un número negativo en números reales.\n")
    
total = int(input("Ingrese la cantidad total: "))
porcentaje = float(input("Ingrese el porcentaje a calcular: "))
res_porcentaje = (total * porcentaje) / 100
print(f"Resultado: El {porcentaje}% de {total} es = {res_porcentaje}\n")

3.
num_1 = int(input("Ingrese el valor num1 "))
num_2 = int(input("Ingrese el valor num2 "))
num_3 = int(input("Ingrese el valor num3 "))

media = (num_1 + num_2 + num_3) / 3

print(f"La media aritmética es: {media}")

4.
altura = float(input("Ingrese su altura "))
peso = float(input("Ingrese su peso "))
imc = round (peso / (altura**2))
print("Su indice de masa corporal ", imc)

5.
tem = float(input("Ingresa la temperatura en grados Fahrenheit "))
tem_C = round((tem - 32) / 1.8, 3 )       
print("La temperatura en grados Celsius es", tem_C)

6.
tem = float(input("Ingresa la temperatura en grados Fahrenheit "))
tem_k = round((tem - 32) / 1.8 + 273.15 , 3 )       
print("La temperatura en grados Kelvin es: " ,tem_k)

7.
tem = float(input("Ingresa la temperatura en grados Kelvin "))
tem_C = round(tem - 273.15 , 3 )       
print("La temperatura en grados Celsius es: " ,tem_C)

8.
segundos = int(input("Ingresa la cantidad de segundos "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_f = segundos % 60
print( " La cantidad de horas es",horas, "de minutos: ",minutos," y segundos:", segundos_f)

9.
a = int(input("Ingresa el valor del lado a del triangulo rectangulo " ))
b = int(input("Ingresa el valor del lado b del triangulo rectangulo " ))
c = int(input("Ingresa el valor del lado c (hipotenusa) del triangulo rectangulo " ))
perimetro = ( a + b + c)
area = (a * b //2)
 print("El valor de lado a ingresado:",a," valor de b:",b," valor de c: ",c)
print(" El area del triangulo es ",area," y su perimetro es",perimetro)

10.
import math
radio = float(input("Ingresa el radio del círculo: "))
perimetro = 2 * math.pi * radio
area = math.pi * (radio ** 2)
print(f"Radio ingresado: {radio}")
print(f"Perímetro del círculo: {round(perimetro, 2)}")
print(f"Área del círculo: {round(area, 2)}")

PARTE 2 EJERCICIOS IF ELSE 
1.
salario_minimo = 1300000
empleados = []
cant = int(input("Cuantas personas deseas registrar? "))
for i in range(cant):
    nombre = input("Ingrese su nombre completo: " )
    T_I = int(input("Ingrese su numero de documento: "))
    sueldo = float(input("Sueldo mensual ($): "))

    empleados.append({ "nombre_apellido": nombre,
                   "documento": T_I,
                   "sueldo": sueldo})
for personas in empleados:
    supera_minimo = "NO gana superior al salario mínimo."

    if personas ["sueldo"] > salario_minimo:
        supera_minimo = "SÍ gana superior al salario mínimo."

    print(f"\nEmpleado: {personas['nombre_apellido']}")
    print(f"Documento: {personas['documento']}")
    print(f"Sueldo: ${personas['sueldo']:}")
    print(f"Estado: {supera_minimo}")
2.
a = float(input("Ingrese el valor de a de la ecuacion: "))
b = float(input("Ingrese el valor de b de la ecuacion: "))
c = float(input("Ingrese el valor de c de la ecuacion: "))
import math
if a==0:
    print("La ecuacion no es de segundo grado debido a el valor del coeficiente")
else:
    discriminante = (b**2)-(4*a*c)
    print("El discriminante",discriminante)

if discriminante>0:
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print("Existen dos raíces reales distintas.")
    print(f"x1 = {round(x1, 4)}")
    print(f"x2 = {round(x2, 4)}")
elif discriminante == 0:
        x = -b / (2 * a)
        
        print("\nResultado: Existen dos raíces reales iguales.")
        print(f"x1 = x2 = {round(x, 4)}")
else:
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(-discriminante) / (2 * a)
        
        print("\nResultado: Existen dos raíces complejas conjugadas.")
        print(f"x1 = {round(parte_real, 4)} + {round(parte_imaginaria, 4)}i")
        print(f"x2 = {round(parte_real, 4)} - {round(parte_imaginaria, 4)}i")
3.
letra = str(input("Ingrese una letra: "))
if len(letra)!= 1:
 print("Error: No se puede procesar el dato. Debes ingresar solo un carácter.")
else:
 letra1 = letra.lower()
    
if letra in "aeiou":
    print("es vocal")
else:
    print("No es una vocal")

4.
import math
while True:
    print("\n================ MENÚ CALCULADORA ================")
    print("1. Operaciones aritméticas básicas (+, -, *, /, //, %, **)")
    print("2. Comparar si un número es par o impar")
    print("3. Calcular porcentaje")
    print("4. Razones trigonométricas (sen, cos, tan)")
    print("5. Salir")
    print("==================================================")
    
    opcion = input("Selecciona una opción (1-5): ")

    # OPCIÓN 1: Operaciones Aritméticas
    if opcion == "1":
        print("\n--- Operaciones Aritméticas ---")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operador = input("Ingresa la operación (+, -, *, /, //, %, **): ")

        if operador == "+":
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif operador == "-":
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif operador == "*":
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif operador == "/":
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
        elif operador == "//":
            if num2 != 0:
                print(f"Resultado: {num1} // {num2} = {num1 // num2}")
            else:
                print("Error: No se puede dividir entre cero.")
        elif operador == "%":
            if num2 != 0:
                print(f"Resultado: {num1} % {num2} = {num1 % num2}")
            else:
                print("Error: No se puede dividir entre cero.")
        elif operador == "**":
            print(f"Resultado: {num1} ** {num2} = {num1 ** num2}")
        else:
            print("Operador aritmético no válido.")

    # OPCIÓN 2: Par o Impar
    elif opcion == "2":
        print("\n--- Evaluar Par o Impar ---")
        numero = int(input("Ingresa un número entero: "))
        
        if numero % 2 == 0:
            print(f"El número {numero} es PAR.")
        else:
            print(f"El número {numero} es IMPAR.")

    # OPCIÓN 3: Porcentajes
    elif opcion == "3":
        print("\n--- Cálculo de Porcentaje ---")
        cantidad = float(input("Ingresa la cantidad base: "))
        porcentaje = float(input("Ingresa el porcentaje a extraer (%): "))
        
        resultado = (cantidad * porcentaje) / 100
        print(f"El {porcentaje}% de {cantidad} es: {resultado}")

    # OPCIÓN 4: Razones Trigonométricas
    elif opcion == "4":
        print("\n--- Razones Trigonométricas ---")
        angulo_grados = float(input("Ingresa el ángulo en grados: "))
        # Se convierte de grados a radianes porque la librería math trabaja en radianes
        angulo_rad = math.radians(angulo_grados)
        
        print("\nSelecciona la función:")
        print("a. Seno")
        print("b. Coseno")
        print("c. Tangente")
        sub_opcion = input("Opción (a-c): ").lower()

        if sub_opcion == "a":
            print(f"sen({angulo_grados}°) = {round(math.sin(angulo_rad), 4)}")
        elif sub_opcion == "b":
            print(f"cos({angulo_grados}°) = {round(math.cos(angulo_rad), 4)}")
        elif sub_opcion == "c":
            # La tangente no existe para 90°, 270°, etc.
            if (angulo_grados - 90) % 180 == 0:
                print("Error: La tangente no está definida para este ángulo.")
            else:
                print(f"tan({angulo_grados}°) = {round(math.tan(angulo_rad), 4)}")
        else:
            print("Opción trigonométrica no válida.")

    # OPCIÓN 5: Salir
    elif opcion == "5":
        print("\n¡Gracias por usar la calculadora! Saliendo del programa...")
        break

    # Opción no válida en el menú principal
    else:
        print("\nOpción no válida. Por favor, selecciona un número entre 1 y 5.")
5.
print("Bienvenido al sistema de conversion de unidades ")
factores_a_metros = {
    "1": 1.0,        # Metros
    "2": 1000.0,     # Kilómetros
    "3": 0.01,       # Centímetros
    "4": 1609.344,   # Millas
    "5": 0.9144,     # Yardas
    "6": 0.3048,     # Pies (12 pulgadas * 0.0254)
    "7": 0.0254      # Pulgadas
}
nombres_unidades = {
    "1": "metros",
    "2": "kilómetros",
    "3": "centímetros",
    "4": "millas",
    "5": "yardas",
    "6": "pies",
    "7": "pulgadas"
}
def mostrar_menu():
    print(" UNIDADES DISPONIBLES ")
    print("1. Metros (m)")
    print("2. Kilómetros (km)")
    print("3. Centímetros (cm)")
    print("4. Millas")
    print("5. Yardas")
    print("6. Pies")
    print("7. Pulgadas")

print(" CONVERTIDOR DE UNIDADES DE LONGITUD ")
mostrar_menu()
origen = input("Selecciona la unidad en que vas a INGRESAR la medida (1-7): ")
destino = input("Selecciona la unidad en que deseas VISUALIZAR el resultado (1-7): ")
if origen in factores_a_metros and destino in factores_a_metros:
    valor = float(input(f"\nIngresa la cantidad en {nombres_unidades[origen]}: "))
    
    valor_en_metros = valor * factores_a_metros[origen]

    resultado = valor_en_metros / factores_a_metros[destino]
    
    print(f"{valor} {nombres_unidades[origen]} equivalen a {round(resultado, 4)} {nombres_unidades[destino]}.")

else:
    print("\n[Error]: Seleccionaste una opción de unidad no válida.")
6.

print("Bienvenido al sistema de votaciones")
opcion = int(input("Las opciones son:\n 1. Candidato A\n 2.Candidato B\n 3. Candidato C\n 4.Voto en blanco\n"))
if opcion == 1:
    print("Usted ha votado por el candidato A")

elif opcion ==2:
    print("Usted ha votado por el candidato B")
    
elif opcion == 3:
     print("Usted ha votado por el candidato C")

elif opcion ==4:
     print("Usted ha votado en blanco")
     
else:
    print("Opcion erronea")

7.
cant = int(input("Que cantidad de estudiantes desea registrar? "))
nombres = []
for i in range(cant):
    nombre = input("Ingrese el nombre del estudiante \n")
    nombres.append(nombre)
busqueda = input("Que nombre desea buscar \n")
encontrado = False
for nombre in nombres:
    if nombre.lower() == busqueda.lower():
        encontrado = True
        break

if encontrado:
    print("El estudiante",busqueda,"si esta en la lista")
else:
    print("El estudiante",busqueda,"no esta en la lista")
    
8.
negativos = 0
positivos = 0
conteo_positivos = 0

print("Ingresa 5 numeros enteros\n")
for i in range(5):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    if numero < 0:
        negativos += numero
    elif numero > 0:
        positivos += numero
        conteo_positivos += 1
print(f"Sumatoria de los números negativos: {negativos}")
if conteo_positivos > 0:
    promedio_positivos = positivos / conteo_positivos
    print(f"Promedio de los números positivos: {round(promedio_positivos, 2)}")
else:
    print("Promedio de los números positivos: No se ingresaron números positivos (división por cero evitada).")

9.

numero_anterior = int(input("Ingresa un número entero: "))
while True:
    numero_actual = int(input(f"Ingresa un número mayor que {numero_anterior}: "))
    if numero_actual <= numero_anterior:
        print(f"\n¡El número {numero_actual} no es mayor que {numero_anterior}! Fin del programa.")
        break
    numero_anterior = numero_actual

10.
import random

def obtener_opcion(nombre_jugador):
    """Solicita y valida la jugada de un participante."""
    opciones = {"1": "Piedra", "2": "Papel", "3": "Tijera"}
    while True:
        print(f"\nTurno de {nombre_jugador}:")
        print("1. Piedra\n2. Papel\n3. Tijera")
        eleccion = input("Seleccione una opción (1-3): ").strip()
        if eleccion in opciones:
            return opciones[eleccion]
        print(" Opción inválida. Intente de nuevo.")

def determinar_ganador(jugada1, jugada2):
    """
    Compara las dos jugadas.
    Retorna 0 si es empate, 1 si gana el Jugador 1, y 2 si gana el Jugador 2.
    """
    if jugada1 == jugada2:
        return 0
    
    reglas = {
        "Piedra": "Tijera",
        "Papel": "Piedra",
        "Tijera": "Papel"
    }
    
    return 1 if reglas[jugada1] == jugada2 else 2

def jugar():
    print("=" * 40)
    print("   JUEGO DE PIEDRA, PAPEL O TIJERA")
    print("=" * 40)
    
    print("\nModos de juego:")
    print("1. Contra la Computadora (PC)")
    print("2. Multijugador (2 Jugadores)")
    
    while True:
        modo = input("Seleccione el modo (1 o 2): ").strip()
        if modo in ["1", "2"]:
            break
        print(" Modo inválido. Ingrese 1 o 2.")

  
    id_j1 = input("\nIngrese el ID o Nombre del Jugador 1: ").strip() or "Jugador 1"
    
    if modo == "1":
        id_j2 = "Computadora (PC)"
    else:
        id_j2 = input("Ingrese el ID o Nombre del Jugador 2: ").strip() or "Jugador 2"

    puntos_j1 = 0
    puntos_j2 = 0
    ronda = 1
    jugando = True
    while jugando:
        print(f"\n--- RONDA {ronda} ---")
       
        jugada_j1 = obtener_opcion(id_j1)
        
        if modo == "1":
            jugada_j2 = random.choice(["Piedra", "Papel", "Tijera"])
            print(f"\n{id_j2} eligió: {jugada_j2}")
        else:
            jugada_j2 = obtener_opcion(id_j2)
        resultado = determinar_ganador(jugada_j1, jugada_j2)
        
        print(f"\nResumen de la ronda:")
        print(f" • {id_j1}: {jugada_j1}")
        print(f" • {id_j2}: {jugada_j2}")
        
        if resultado == 0:
            print("Resultado: ¡Empate! Nadie suma puntos.")
        elif resultado == 1:
            print(f"Resultado: ¡Punto para {id_j1}!")
            puntos_j1 += 1
        else:
            print(f"Resultado: ¡Punto para {id_j2}!")
            puntos_j2 += 1

        print(f"Marcador actual -> {id_j1}: {puntos_j1} | {id_j2}: {puntos_j2}")
        
        
        while True:
            respuesta = input("\n¿Desea jugar otra ronda? (s/n): ").strip().lower()
            if respuesta in ["s", "n"]:
                if respuesta == "n":
                    jugando = False
                break
            print(" Respuesta no válida. Ingrese 's' para sí o 'n' para no.")
        
        ronda += 1

    
    print("\n" + "=" * 40)
    print("          RESULTADOS FINALES")
    print("=" * 40)
    print(f"Puntaje {id_j1}: {puntos_j1}")
    print(f"Puntaje {id_j2}: {puntos_j2}")
    
    if puntos_j1 > puntos_j2:
        print(f"\n ¡EL GANADOR ES {id_j1.upper()}!")
    elif puntos_j2 > puntos_j1:
        print(f"\n ¡EL GANADOR ES {id_j2.upper()}!")
    else:
        print("\n ¡LA PARTIDA TERMINÓ EN EMPATE TOTAL!")

if __name__ == "__main__":
    jugar()
12.
def categorizar_nota(nota):
    """Retorna la categoría correspondiente según el valor numérico de la nota."""
    if nota >= 4.5:
        return "Excelente"
    elif nota >= 4.0:
        return "Bueno"
    elif nota >= 3.0:
        return "Aceptable"
    elif nota >= 2.0:
        return "Insuficiente"
    else:
        return "Deficiente"

def solicitar_cantidad():
    """Solicita y valida la cantidad N de estudiantes."""
    while True:
            n = int(input("Ingrese la cantidad de estudiantes a registrar (N): "))
            if n > 0:
                return n
            print("Ingrese un número entero mayor que 0.")
            print(" Entrada no válida. Debe ingresar un número entero.")

def solicitar_nota(nombre):
    """Solicita y valida la nota de un estudiante (entre 0.0 y 5.0)."""
    while True
            nota = float(input(f"Ingrese la nota de {nombre} (0.0 a 5.0): "))
            if 0.0 <= nota <= 5.0:
                return nota
            print("La nota debe estar en el rango de 0.0 a 5.0.")
            print(" Entrada no válida. Ingrese un número decimal/entero.")

def main():
    print("=" * 50)
    print("   SISTEMA DE CATEGORIZACIÓN DE NOTAS")
    print("=" * 50 + "\n")

    # Contenedor para agrupar estudiantes por categoría
    categorias = {
        "Excelente": [],
        "Bueno": [],
        "Aceptable": [],
        "Insuficiente": [],
        "Deficiente": []
    }

    n_estudiantes = solicitar_cantidad()

    # Captura de datos
    for i in range(1, n_estudiantes + 1):
        print(f"\n--- Estudiante {i} de {n_estudiantes} ---")
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        while not nombre:
            nombre = input("El nombre no puede estar vacío. Reintente: ").strip()

        nota = solicitar_nota(nombre)
        cat = categorizar_nota(nota)
        
        # Se guarda el nombre en el contenedor según su categoría
        categorias[cat].append((nombre, nota))

    # Presentación de resultados
    print("\n" + "=" * 50)
    print("        CLASIFICACIÓN FINAL DE ESTUDIANTES")
    print("=" * 50)

    for cat, estudiantes in categorias.items():
        print(f"\n Categoría: {cat} ({len(estudiantes)} estudiante(s))")
        print("-" * 40)
        
        if estudiantes:
            for nombre, nota in estudiantes:
                print(f"  {nombre} - Nota: {nota:.1f}")
        else:
            print("   (Sin estudiantes en esta categoría)")

if __name__ == "__main__":
    main()
PARTE 3 EJERCICIOS FUNCIONES
1.
def area_perimetro_rectangulo(base, altura):
    perimetro = 2 * (base + altura)
    area = base * altura
    return perimetro, area
2.
import math

def area_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    area = math.pi * (radio ** 2)
    return perimetro, area
3.
def hallar_mayor_menor(a, b):
    if a > b:
        return a, b
    else:
        return b, a
4.
def inversa(cadena):
    return cadena[::-1]
print(inversa("universidad industrial de santander"))

5.
import math


def suma(numeros):
    return sum(numeros)
def resta(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado -= n
    return resultado
def multiplicacion(numeros):
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado
def division(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            return "Error: División por cero"
        resultado /= n
    return resultado
def potencia(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado **= n
    return resultado
def porcentaje(base, porcentaje_val):
    return (base * porcentaje_val) / 100
def raices(numeros):
    # Calcula la raíz n-ésima sucesiva: número^(1/índice)
    resultado = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            return "Error: Índice de raíz cero"
        if resultado < 0 and n % 2 == 0:
            return "Error: Raíz par de un número negativo"
        resultado = resultado ** (1 / n)
    return resultado
def pedir_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        num = float(input(f" Ingrese el número {i + 1}: "))
        numeros.append(num)
    return numeros
def menu():
    while True:
        print("\n=== MENÚ DE OPERACIONES ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Porcentaje")
        print("7. Raíces")
        print("8. Salir")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "8":
            print("¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4", "5", "7"]:
            n = int(input("¿Cuántos números/operaciones desea procesar?: "))
            if n <= 0:
                print("Debe ingresar al menos un número.")
                continue

            nums = pedir_numeros(n)

            if opcion == "1":
                print(f"Resultado de la suma: {suma(nums)}")
            elif opcion == "2":
                print(f"Resultado de la resta: {resta(nums)}")
            elif opcion == "3":
                print(f"Resultado de la multiplicación: {multiplicacion(nums)}")
            elif opcion == "4":
                print(f"Resultado de la división: {division(nums)}")
            elif opcion == "5":
                print(f"Resultado de la potencia: {potencia(nums)}")
            elif opcion == "7":
                print(f"Resultado de la raíz: {raices(nums)}")

        elif opcion == "6":
            base = float(input("Ingrese el número base: "))
            pct = float(
                input("Ingrese el porcentaje a calcular (ejemplo: 15 para 15%): ")
            )
            print(f"El {pct}% de {base} es: {porcentaje(base, pct)}")

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

6.
def relacion(a, b):
    if a > b:
        return True
    elif a < b:
        return False
    else:
        return "Empate"


# Ejemplo de uso
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

print(relacion(a, b))

7.
def Separar(lista):
    lista.sort()

    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares


# Ejemplo de uso
numeros = [15, 4, 23, 8, 42, 11, 0, 7, 18]
lista_pares, lista_impares = Separar(numeros)

print("Pares ordenados:", lista_pares)
print("Impares ordenados:", lista_impares)






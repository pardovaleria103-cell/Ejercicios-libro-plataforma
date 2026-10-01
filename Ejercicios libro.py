#EJERCICIOS CAP 2

1.
nombre = "Ana"
edad = 22
print(f"Me llamo {nombre} y tengo {edad} años.")

2.
base = 10.0
altura = 5.0
area = (base * altura) / 2
print(f"El área del triángulo con base {base} y altura {altura} es {area}.")

3.
numero_entero = 25
numero_decimal = 18.5
es_estudiante = True
nombre = "Carlos"
print(type(numero_entero))
print(type(numero_decimal))
print(type(es_estudiante))
print(type(nombre))

4.
numero = int(input("Ingresa un número: "))
resultado = numero % 2 == 0
print(resultado)

5.
a = 4
b = 2.5
c = "3"

# a) a + b
resultado_a = a + b
print("a) Resultado:", resultado_a)
print("Tipo:", type(resultado_a))

# b) a * int(c)
resultado_b = a * int(c)
print("b) Resultado:", resultado_b)
print("Tipo:", type(resultado_b))

# c) str(a) + c
resultado_c = str(a) + c
print("c) Resultado:", resultado_c)
print("Tipo:", type(resultado_c))

6.
edad = 17
ciudadano = False
puede_votar = (edad >= 18) and ciudadano
print(puede_votar)

7.
texto = "Hola Mundo."
texto_mayusculas = texto.upper()
print("a)", texto_mayusculas)
texto_minusculas = texto.lower()
print("b)", texto_minusculas)
texto_reemplazado = texto.replace("Mundo", "Universo")
print("c)", texto_reemplazado)

8
aprobo_introductorio = input("¿Aprobó el curso introductorio? (sí/no): ").lower() == "sí"
promedio = float(input("Ingrese su promedio: "))
puede_inscribirse = aprobo_introductorio and (promedio >= 3.5)
# Mostrar el resultado (True o False)
print(puede_inscribirse)

9.
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
print(f"Hola {nombre}, tienes {edad} años.")

10.
print( int("Hola"))
 #Genera un error debido a que int() está diseñada para convertir cadenas de texto que representan números enteros.

11.
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))  # Convertimos la entrada a entero (int)
edad_en_10 = edad + 10

print(f"{nombre}, en 10 años tendrás {edad_en_10} años.")

12.
dinero_usuario = float(input("¿De cuánto dinero dispones? "))
precio = 1199999.99
print(dinero_usuario >= precio)

#EJERCICIOS LIBRO CAP 3


1. ##frutas = { "Manzana","Kiwi","Piña" }
##frutas.add("Mango")
##frutas.remove("Manzana")
##print(frutas)

2.
##numeros = [3, 7, 2, 9, 4]
##numeros.sort()
##numeros.append(5)
##numeros.remove(7)
##print(numeros)
3.
##datos_personales = ("Valeria", 19, "Vélez")
##print(datos_personales[0])  
##print(datos_personales[1])
##print(datos_personales[2])
4.
 #datos_personales = ("Valeria", 19, "Velez")
 #datos_personales [1] = 23
 #Las tuplas no se pueden modificar es por ello que al intentar cambiar el valor de la edad que está en la posición 1 me sale error.
5.
##A = {1, 2, 3, 4}
##B = {3, 4, 5, 6}
##print ( A | B )
##print ( A & B )
##print ( A - B )
6.
pelicula = {
    "titulo": "Inception",
    "director": "Christopher Nolan",
    "año": 2010}
print("Título:", pelicula["titulo"])
print("Director:", pelicula["director"])
print("Año:", pelicula["año"])
pelicula["genero"] = "Ciencia ficción"
pelicula["año"] = 2011
pelicula.pop("director")
print("\nDiccionario final:")
print(pelicula)
7.
notas = {'Ana': 4.5, "Luis": 3.7, "Pedro": 4.2}
for nombre, nota in notas.items():
    print(f"{nombre} tiene una nota de {nota}.")
8.
estudiantes = [
    {"nombre": "Ana", "edad": 19},
    {"nombre": "Luis", "edad": 21},
    {"nombre": "Pedro", "edad": 20}]
edad_segundo_estudiante = estudiantes[1]["edad"]

print(f"La edad del segundo estudiante es: {edad_segundo_estudiante}")


 #EJERCICIOS CAP 4
1.
numero = int(input("Digite un numero entero"))
if numero > 0:
	    print("El número es positivo.")
elif numero < 0:
	    print("El número es negativo.")
else:
	    print("El número es cero.")
2.
edad = int(input("Ingrese su edad"))
if edad < 12:
    print("Eres un niño.")
elif edad <= 17:
    print("Eres un adolescente.")
elif edad <= 59:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
3.
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operador = input("Ingresa un operador (+, -, *, /): ")
if operador == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: El operador ingresado no es válido.")
4.
CLAVE_CORRECTA = "python123"
intento = input("Ingresa la contraseña: ")
while intento != CLAVE_CORRECTA:
    print("Contraseña incorrecta. Inténtalo de nuevo.\n")
    intento = input("Ingresa la contraseña: ")
print("¡Acceso concedido!")

5.
contador = 1
while contador <= 10:
    print(contador)
    contador += 1  
6.
suma_total = 0.0
while True:
    entrada = input ("Ingresa un número (o escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":
        break
    
    # Conversión e incremento de la suma
    suma_total += float(entrada)
print(f"\nLa suma total es: {suma_total}")

7.
for i in range(1, 11):
    cuadrado = i ** 2
    print(f"El cuadrado de {i} es: {cuadrado}")

8.
for numero in range(0, 21, 2):
    print(numero)
9.
nombres = ["Ana", "Carlos", "Sofía", "Mateo"]
for nombre in nombres:
    print(f"¡Hola, {nombre}! Espero que tengas un excelente día.")

10.
texto = "Aprender a programar con Python es muy divertido y útil"
contador = 0

for caracter in texto:
    if caracter == "a":
        contador += 1

print(f"La letra 'a' aparece {contador} veces.")

11.
 numeros = [10, 45, 8, -3, 22, 15]

for numero in numeros:
    if numero < 0:
        print(f"Se encontró un número negativo: {numero}. Deteniendo el ciclo.")
        break
    print(f"Número procesado: {numero}")

12.
saldo = 500

print(f"Saldo inicial: ${saldo}")

while saldo > 0:
    monto = float(input("\nIngresa el monto a retirar (o 0 para salir): "))

    if monto == 0:
        print("\nOperación cancelada por el usuario.")
        break

    if monto < 0:
        print("Monto no válido. Ingresa una cantidad mayor a 0.")
        continue

    if monto > saldo:
        print(f"Saldo insuficiente. Intentaste retirar ${monto}, pero tu saldo es de ${saldo}.")
        break

    saldo -= monto
    print(f"Retiro exitoso. Saldo actualizado: ${saldo}")

print(f"\nGracias por usar el cajero automático. Saldo final: ${saldo}")

#EJERCICIOS CAP 5
1.
def saludar():
    print("¡Hola, bienvenido al curso de Python!")
saludar()

2.
def es_par(numero):
    return numero % 2 == 0
print(es_par(4))    # True
print(es_par(7))    # False
print(es_par(0))    # True
print(es_par(15))   # False
print(es_par(20))   # True

3.
# Definición de la función
def area_triangulo(base, altura):
    return (base * altura) / 2

# Uso de la función desde print()
print("El área del triángulo es:", area_triangulo(10, 5))

4.
# Definición de la función
def saludo_personalizado(nombre, mensaje="¡Que tengas un buen día!"):
    print(f"Hola, {nombre}. {mensaje}")

# Prueba usando ambos argumentos
saludo_personalizado("Valeria", "Bienvenida al curso de Python.")

# Prueba usando solo el nombre
saludo_personalizado("Pedro")

5.
contador = 0

def incrementar_contador():
    global contador 
    contador += 1
    print("Se utilizó la palabra clave 'global' porque estamos modificando una variable definida fuera de la función.")
    print("Valor actual del contador:", contador)

# Llamada a la función
incrementar_contador()
incrementar_contador()

6.
def sumar_todo(*args):
    return sum(args)
print("Suma de 3 números:", sumar_todo(5, 10, 15))

print("Suma de 5 números:", sumar_todo(1, 2, 3, 4, 5))

print("Suma de 7 números:", sumar_todo(10, 20, 30, 40, 50, 60, 70))

7.
def imprimir_clave_valor(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
imprimir_clave_valor(
    nombre="Valeria",
    edad=19,
    carrera="Ingeniería Electrónica",
    ciudad="Bucaramanga"
)

8.
def mostrar_reporte(nombre, edad, ciudad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
mostrar_reporte("Valeria", 19, "Bucaramanga")

9.
def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
print("Números primos entre 1 y 50:")

for numero in range(1, 51):
    if es_primo(numero):
        print(numero)

10.
def leer_numeros():
    entrada = input("Ingrese una lista de números separados por comas: ")
    lista = [int(num) for num in entrada.split(",")]
    return lista
def calcular_estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio
def mostrar_resultado(minimo, maximo, promedio):
    print("\n--- Resultados ---")
    print("Valor mínimo:", minimo)
    print("Valor máximo:", maximo)
    print("Promedio:", promedio)
numeros = leer_numeros()
minimo, maximo, promedio = calcular_estadisticas(numeros)
mostrar_resultado(minimo, maximo, promedio)

#EJERCICIOS CAP 6

1.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeros_cinco = numeros[:5]
indice_2_al_7 = numeros[2:8]
lista_invertida = numeros[::-1]

print("Primeros cinco:", primeros_cinco)
print("Índices 2 al 7:", indice_2_al_7)
print("Lista invertida:", lista_invertida)

2.
original = [10, 20, 30]
copia_asignacion = original
copia_copy = original.copy()
copia_slicing = original[:]

print("Original:", original)
print("Copia por asignación:", copia_asignacion)
print("Copia con .copy():", copia_copy)
print("Copia con slicing:", copia_slicing)

3.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
valor = matriz[1][2]
print("Valor:", valor)
fila = matriz[1][:]
print("Segunda fila:", fila)

4.
colores = ['rojo', 'verde', 'azul']

for indice, color in enumerate(colores):
    print(f"{indice}: {color}")
5.
nombres = ['Ana', 'Luis', 'Sofía']
edades = [22, 30, 27]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")

6.
cuadrados = [x**2 for x in range(1, 11)]
pares = [x for x in range(1, 21) if x % 2 == 0]
multiplos_tres = [x for x in range(12, 12 + 10 * 3, 3)]

7.
nombres = ["Ana", "Alexander", "Luis", "Beatriz", "Leo", "Sofía", "Max"]
nombres_largos = [nombre for nombre in nombres if len(nombre) > 4]

print(nombres_largos)

8.
productos = ["Pan", "Leche", "Huevos"]
precios = [1500, 3200, 5200]
productos_con_precio = [f"{prod}: ${precio}" for prod, precio in zip(productos, precios)]

productos_costosos = [f"{prod}: ${precio}" for prod, precio in zip(productos, precios) if precio > 3000]

print("Todos los productos:", productos_con_precio)
print("Productos mayores a $3000:", productos_costosos)

#EJERCICIOS CAP 7

1.
numeros = [1, 2, 3]

# PROBLEMA 1 (SyntaxError): Tenía un espacio dentro de la función "pr int", lo cual no es válido. Se corrigió a "print".
# PROBLEMA 2 (IndexError): Se intentaba acceder a "numeros[5]", pero los índices válidos son solo 0, 1 y 2.
# CORRECCIÓN: Se cambia el índice a uno existente (por ejemplo, el índice 2 para obtener el valor 3).

print(numeros[2])

2.
try:
    entrada = input("Ingrese un número entero: ")
    numero = int(entrada)
    print(f"Número ingresado con éxito: {numero}")

except ValueError:
    print("Entrada inválida: debe ser un número entero")

3.
try:
    entrada = input("Ingrese un número entero: "
    numero = int(entrada)
    print(f"Número ingresado con éxito: {numero}")

except ValueError:
    print("Entrada inválida: debe ser un número entero")

except Exception as e:
    print(f"Ocurrió un error inesperado no contemplado: {e}")

4.
def dividir_numeros(a, b):
    try:
        # Intentamos realizar la división
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
        return None

res1 = dividir_numeros(10, 2)
print("Resultado:", res1)  

print("-" * 30)
res2 = dividir_numeros(10, 0)
print("Resultado:", res2) 

5.
def obtener_edad():
    try:
        edad = int(input("Por favor, ingrese su edad: "))
        if 0 <= edad <= 120:
            print(f"Edad válida registrada: {edad} años.")
            return edad
        else:
            print("Advertencia: La edad debe estar entre 0 y 120 años.")
            return None

    except ValueError:
        print("Advertencia: Debe ingresar un número entero válido.")
        return None
obtener_edad()

6.
try:
    entrada = input("Ingrese un número entero: ")
    numero = int(entrada)
except ValueError:
    print("Error: La entrada ingresada no es un número entero válido.")
else:
    print("Conversión exitosa")
    print(f"El número procesado es: {numero}")
finally:
    print("Fin del programa")

7.
def calcular_promedio(lista):
    # La instrucción assert evalúa si la lista no está vacía (len > 0)
    # Si la condición es False, lanza un AssertionError con el mensaje especificado
    assert len(lista) > 0, "La lista no puede estar vacía"
    
    return sum(lista) / len(lista)


#  Ejemplos de uso 

# Caso 1: Lista con datos
numeros = [10, 20, 30, 40]
print("El promedio es:", calcular_promedio(numeros))

# Caso 2: Lista vacía (Descomentar para ver cómo assert detiene el programa)
lista_vacia = []
print(calcular_promedio(lista_vacia))

8.
def validar_producto(producto):
    claves_requeridas = ["nombre", "precio", "cantidad"]
    faltantes = []

    # Verificamos cada clave requerida en el diccionario
    for clave in claves_requeridas:
        if clave not in producto:
            faltantes.append(clave)

    # Evaluamos si hubo claves faltantes
    if faltantes:
        for clave in faltantes:
            print(f"Error: Falta la clave '{clave}' en los datos del producto.")
    else:
        print("El producto contiene todas las claves requeridas.")

# --- Ejemplos de uso ---

# Caso 1: Producto incompleto (falta 'cantidad')
producto1 = {
    "nombre": "Teclado Mecánico",
    "precio": 150000
}

print("--- Validando producto 1 ---")
validar_producto(producto1)

print("\n--- Validando producto 2 ---")
# Caso 2: Producto completo
producto2 = {
    "nombre": "Mouse Gamer",
    "precio": 80000,
    "cantidad": 15
}
validar_producto(producto2)

9.
def ingresar_nota():
    while True:
        try:
            # Solicitamos la entrada y la convertimos a número flotante
            entrada = input("Ingrese una nota (entre 0.0 y 5.0): ")
            nota = float(entrada)
            
            # Verificamos que esté dentro del rango válido
            if 0.0 <= nota <= 5.0:
                return nota
            else:
                print(" Error: La nota debe estar entre 0.0 y 5.0. Intente de nuevo.\n")
                
        except ValueError:
            # Captura si el usuario ingresó texto o caracteres no numéricos
            print(" Error: Debe ingresar un valor numérico válido (ejemplo: 4.5). Intente de nuevo.\n")

# --- Ejemplo de uso ---
nota_final = ingresar_nota()
print(f"\n Nota registrada con éxito: {nota_final}")

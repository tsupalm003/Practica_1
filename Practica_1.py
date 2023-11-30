print("-------------------------Practica 1-----------------------")
print("--------------------Datos tipo numerico-------------------")
# Numeros Enteros (int)
print("-------------------------int------------------------------")
entero_1 = 20
print("entero_1:", entero_1)
tipo_numero_1 = type(entero_1)
print("tipo_numero_1:", tipo_numero_1)

# Numeros Flotantes (float)
print("-------------------------float----------------------------")
float_1 , float_2 , float_3 , = 0.348 , 10.5 , 1.5e2 
print("float_1:" , float_1)
print("float_2:" , float_2)
print("float_3:" , float_3)
tipo_float_1 = type(float_1)
print("tipo_float_1:" , tipo_float_1)

# Numeros Complejos (complex)
print("------------------------complex---------------------------")
complejo_1 = 2.1 + 7.8j
print("complejo_1:" , complejo_1)
tipo_complejo_1 = type(complejo_1)
print("tipo_complejo_1," , tipo_complejo_1)
print("complejo_1.imag:" , complejo_1.imag)
print("complejo_1.real:" , complejo_1.real)
abs_complejo_1 = abs(complejo_1)
print("abs_complejo_1:" , abs_complejo_1)

print("--------------------Datos tipo booleano-------------------")

# Datos tipo booleano (bool)
bool_1 = False
print("bool_1:" , bool_1)
bool_2 = False
print("bool_2:" , bool_2)
bool_3 = 0
print("bool_3:" , bool_3)
bool_4 = '""'
print("bool_4:" , bool_4)
bool_5 = None
print("bool_5:" , bool_5)
bool_6 = []
print("bool_6:" , bool_6)
bool_7 = ()
print("bool_7:" , bool_7)
bool_8 = {}
print("bool_8:" , bool_8)
bool_9 = ['','']
print ("bool_9:" , bool_9)
print("bool_2 == bool_1:" , bool_2 == bool_1)
print("bool_3 == bool_1:" , bool_3 == bool_1)
print("bool_4 == bool_1:" , bool_4 == bool_1)
print("bool_5 == bool_1:" , bool_5 == bool_1)
print("bool_6 == bool_1:" , bool_6 == bool_1)
print("bool_7 == bool_1:" , bool_7 == bool_1)
print("bool_8 == bool_1:" , bool_8 == bool_1)
print("bool_9 == bool_1:" , bool_9 == bool_1)

print("----------------------------------------------------------------------")

bool_10 = True
int_1 = int(bool_1)
int_2 = int(bool_10)
print("int_1:" , int_1)
print("int_2:" , int_2)

print("----------------------------------------------------------------------")

tipo_bool_10 = type(bool_10)
print("tipo_bool_10:" , tipo_bool_10)
str_1 = str(bool_10)
print("str_1:" , str_1)
tipo_str_1 = type(str(str_1))
print("tipo_str_1:" , tipo_str_1)
tipo_bool_1 = type(bool_1)
print("tipo_bool_1:" , tipo_bool_1)
str_2 = str(bool_1)
print("str_2:" , str_2)
tipo_str_2 = type(str(str_2))
print("tipo_str_2:" , tipo_str_2)

print("----------------------------Datos tipo arreglo--------------------------")
print("----------------------------------list----------------------------------")

# Listas (list)
factura = ['pan' , 'huevos' , 100 , 1234]
print("factura:" , factura)

print("------------------------------------------------------------------------")
print("factura[0]:" , factura[0])
print("factura[3]:" , factura[3])

print("------------------------------------------------------------------------")

numero_de_elementos = len(factura)
print("numero_de_elementos:" , numero_de_elementos)
numero_de_elementos_menos_1 = len(factura)-1
print("numero_de_elementos_menos_1:" , numero_de_elementos_menos_1)
print("factura[-1]:" , factura[-1])
print("factura[-len(factura)]:" , factura[-len(factura)])
factura = ['pan' , "carne" , 'huevos' , 100 , 1234]
print("factura[1]:" , factura[1])
print("factura:" , factura)

print("-----------------------------------------------------------------------")

versiones_plone = [2.5 , 3.6 , 4 , 5]
print("versiones_plone:" , versiones_plone)
versiones_plone.append(6)
print("versiones_plone:" , versiones_plone)

print("-----------------------------------------------------------------------")

versiones_plone = [2.1 , 2.5 , 3.6 , 4 , 5 , 5 , 6]
print("versiones_plone.count(6):" , versiones_plone.count(6))
print("versiones_plone.count(5):" , versiones_plone.count(5))

print("-----------------------------------------------------------------------")

versiones_plone = [2.1 , 2.5 , 3.6]
print("versiones_plone:" , versiones_plone)
versiones_plone.extend([4])
print("versiones_plone:" , versiones_plone)

print("-----------------------------------------------------------------------")

versiones_plone = [2.1 , 2.5 , 3.6 , 4 , 5 , 6 , 4]
print("versiones_plone:" , versiones_plone)
print("versiones_plone.index(4):" , versiones_plone.index(4))

print("-----------------------------------------------------------------------")

versiones_plone = [2.1 , 2.5 , 3.6 , 4 , 5 , 6]
print("versiones_plone:" , versiones_plone)
versiones_plone.insert(2 , 3.7)
print("versiones_plone:" , versiones_plone)

print("-----------------------------------------------------------------------")

versiones_plone = [4 , 2.5 , 5 , 3.6 , 2.1 , 6]
print("versiones_plone:" , versiones_plone)
versiones_plone.sort()
print("versiones_plone:" , versiones_plone)

print("-----------------------------Datos tipo string-------------------------")
# string (str)
print("'Hola Mundo'")
hla_mmd = "'Hola Mundo'"
print("hla_mmd =" , hla_mmd)

print("-----------------------------------------------------------------------")

a , b = "uno" , "dos"
print("a + b =" , a + b)

print("-----------------------------------------------------------------------")

c = "tres"
print("c * 3:" , c * 3)

print("-----------------------------------------------------------------------")

tipo_calculo = "raiz cuadrada de dos"
valor = 2**0.5
print("el resultado de {} es {}".format(tipo_calculo , valor))


print("----------------------------Primer Ejercicio---------------------------")

print("Este programa solicita al usuario tres numeros enteros y da como resultado una lista con los valores ordenados")

# Tres numeros ingresado por el usuario (Los datos ingresa en forma de str)

input_1 = input("Ingrese el primer numero entero: ")
input_2 = input("Ingrese el segundo numero entero: ")
input_3 = input("Ingrese el tercer numero entero: ")

# Cambiar los datos a tipo int

numero_entero_1 = int(input_1)
numero_entero_2 = int(input_2)
numero_entero_3 = int(input_3)

# Crear una lista con los numeros ingresados

Numeros_ingresados = [numero_entero_1 , numero_entero_2 , numero_entero_3]
print("Numeros ingresados: " , Numeros_ingresados)

# Ordenar la lista de numeros

Numeros_ingresados.sort()

print("Lista con los numeros ordenados: " , Numeros_ingresados)

print("--------------------------Segundo Ejercicio--------------------------")

print("Este programa solicita al usuario una cadena de caracteres en mayuscula e imprime una lista con cada palabra en minuscula")

# Solicita al usuario una cadena de caracteres en mayuscula

input_1 = input("Ingresa una cadena de caracteres en mayuscula: ")
 
 # Convertir la cadena de caracteres en una lista
 
Lista_de_palabras = input_1.split()
print("Lista de palabras en mayuscula: " , Lista_de_palabras)

# Convertir la lista de palabras en minuscula

Lista_palabras_minuscula = [palabra.lower() for palabra in Lista_de_palabras]
print("Lista de palabras en minuscula: " , Lista_palabras_minuscula)
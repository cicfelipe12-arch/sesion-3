# tipos de datos primitivos:

# edad = 18 # entero (int)
# altura = 1.80 # float (flotante)
# nombre = "andres" #  string (caracteres, lectras  o simbolos) --- cadena
# es_mayor = True # booleano (2 valores true o false)

# condicional ...

# es una expresion que califica el estado de una proposicion y ejecuta una rama del codigo dependiendo del estado boolenao de esa proposicion.

# clasificar el estado de un pedido segun su codigo:
# 1: "recibido"
# 2: "preparado"
# 3: "despacahdo"
# otro: "desconocido"

# if condicion: 
#    # ejecuta el codigo que pongamos aca
# else:
#    # lo que pasa si es falso

# if condicion matizada:  
#   # ejecuta si es verdadero
# elif condicion 2: 
#   # ejecuta si esta condicion es verdadera
# else:
#   # ejecuta si ninguna condicion se cumple

# como le fue a un alumno segun sus notas:

nota = float(input("como te fue en el examen: "))

if nota >= 4.0:
    print("gané")
else:
    print("perdí la nota")

n = float(input("ingrese una nota dictaminar el rango: "))

if n < 0 or n > 5:
    print("dato invalido")
else:
    if n >= 4.6:
        print("sobresaliente")
    else:
        if n >= 4:
            print("alto") 
        elif n >=3 :
            print("basico")
        else:
            print("bajo")      

#Saludo Simple
def saludo(nombre:str):
    return f"¡Hola, {nombre}!"

#Suma de dos numeros
def sumar(num1:float,num2:float)->float:
    return num1 + num2

#Area de un triangulo
def calcular_area_triangulo(base:float,altura:float)->float:
    area=(base*altura)/2
    return area

#Calculadora de descuento
def calcular_precio_final(precio:float,descuento:float=0.10,impuesto:float=0.16)->float:
    totalDescuento=precio*descuento
    precioDescuento=precio-totalDescuento
    totalImpuesto=precioDescuento*impuesto
    precioFinal=precioDescuento+totalImpuesto
    return precioFinal

#Suma de una lista de numeros
def sumar_lista(lista:list)->float:
    res=0
    for i in range(len(lista)):
        valor=lista[i]
        res+=valor
    return res

#Funcion con valores predeterminados
def producto(producto:str,cantidad:int=1,precio:float=10):
    precioTotal=cantidad*precio
    return f"{cantidad} {producto} cuestan {precioTotal:.2f} pesos."

#Numeros pares e impares
def numeros_pares_e_impares(lista:list):
    pares=[]
    impares=[]
    for i in range(len(lista)):
        valor=lista[i]
        if valor %2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
    return pares,impares

#Multiplicacion con *args
def multiplicar_todos(*nums:float)->float:
    res=1
    if not nums:
        return res
    else:
        for num in nums:
            res*=num
        return res

#Informacion de una persona con **kwargs
def informacion_personal(**info)->dict:
    informacion={}
    for llave,dato in info.items():
        informacion[llave]=dato
    return informacion

#Calculadora flexible
def calculadora_flexible(num1:float,num2:float,operacion:str="Suma"):
    match operacion:
        case "Suma":
            suma=num1 + num2
            return suma
        case "Resta":
            resta=num1 - num2
            return resta
        case "Multiplicación":
            multi=num1 * num2
            return multi
        case "División":
            if num2 == 0:
                return "Expresión indefinida"
            else:
                divi=num1/num2
                return divi
        case _:
            return "Operación no válida"
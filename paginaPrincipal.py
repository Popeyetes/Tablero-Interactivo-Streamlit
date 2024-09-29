import streamlit as st
import pandas as pd
import funciones as fn

st.header("Tablero interactivo")
opciones=["Menú principal","Saludo simple","Suma de dos numeros","Área de un triángulo","Calculadora de descuento","Suma de una lista","Valores predeterminados","Pares e impares","Multiplicación","Información personal","Calculadora flexible"]
opcion=st.sidebar.selectbox("Menú de opciones",opciones)

match opcion:
    case "Menú principal":
        st.title("Página principal")
        st.write("Esta es una aplicación interactiva en la que tiene 10 opciónes para poder realizar distintas actividades.")

        st.markdown("### Saludo simple")
        st.markdown("- **Esta opción realiza un saludo simple, solo tienes que ingresar tu nombre y listo.**")

        st.markdown("### Suma de dos números")
        st.markdown("- **En esta actividad ingresaras dos números para obetener el resultado de su suma.**")

        st.markdown("### Área de un triangulo")
        st.markdown("- **En esta actividad podrás obtener el área de un triangulo ingresando su base y altura.**")

        st.markdown("### Calculadora de descuento")
        st.markdown("- **En esta actividad podrás obtener un precio aplicando un descuento y un impuesto (incluye un impuesto y un descuento por defecto).**")

        st.markdown("### Suma de una lista")
        st.markdown("- **En esta actividad ingresaras valores a una lista, el resultado será la suma de los valores que se ingresaron.**")

        st.markdown("### Valores predeterminados")
        st.markdown("- **Esta actividad realiza una simulación de una compra, en la que ingresas un producto, la cantidad que deseas comprar y su precio (incluye un precio y una cantidad por defecto).**")

        st.markdown("### Pares e impares")
        st.markdown("- **En esta actividad ingresaras numeros enteros y los almacenaras al calculo, el resultado será una lista de los numeros pares e impares que ingresaste.**")

        st.markdown("### Multiplicación")
        st.markdown("- **Para esta actividad deberás ingresar valores (valor1,valor2,valor3,...) y enviar a calcular, el resultado final será una multiplicaión de todos los valores ingresados.**")

        st.markdown("### Información personal")
        st.markdown("- **En esta actividad ingresaras información de cualquier tipo y esta la imprimirá de forma ordenada.**")

        st.markdown("### Calculadora flexible")
        st.markdown("- **Esta actividad es una calculadora para dos números en las que podrás realizar 4 operaciones (Suma, Resta, Multiplicación, División).**")

        st.write("¡Adelante, disfruta de las actividades!")
        
    case "Saludo simple":
        st.title("Saludo simple")
        nombre=st.text_input("Ingrese su nombre")
        if st.button ("¡Saludar!"):
            saludo=fn.saludo(nombre)
            st.write(saludo)

    case "Suma de dos numeros":
        st.title("Suma de dos números")
        num1=st.number_input("Ingrese el primer valor",format="%.2f")
        num2=st.number_input("Ingrese el segundo valor",format="%.2f")
        if st.button ("Sumar"):
            res=fn.sumar(num1,num2)
            st.write(f"Suma: {num1:.2f} + {num2:.2f} = {res:.2f}")

    case "Área de un triángulo":
        st.title("Área de un triangulo")
        base=st.number_input("Ingrese la Base",format="%.2f")
        altura=st.number_input("Ingrese la Altura",format="%.2f")
        if st.button ("Calcular área"):
            area=fn.calcular_area_triangulo(base,altura)
            st.write(f"El area del triangulo con base {base:.2f} y altura {altura:.2f} es: {area:.2f}")

    case "Calculadora de descuento":
        st.title("Calculadora de descuento")
        precio=st.number_input("Precio del producto",format="%.2f")
        descuento=st.number_input("Descuento (opcional)",format="%.2f")
        impuesto=st.number_input("Impuesto (opcional)",format="%.2f")
        if st.button("Calcular"):
            if descuento and impuesto:
                total=fn.calcular_precio_final(precio,descuento,impuesto)
                st.write(f"El total de {precio:.2f} con descuento de {descuento:.2f} y un impuesto de {impuesto:.2f} es: {total:2f}")
            else:
                total=fn.calcular_precio_final(precio)
                st.write(f"El total de {precio:.2f} con descuento de 0.10 y un impuesto de 0.16 es: {total:2f}")

    case "Suma de una lista":
        st.title("Suma de una lista")
        if 'mi_lista' not in st.session_state:
            st.session_state.mi_lista = []
        valor=st.number_input("Ingrese un número",format="%.2f")
        if st.button("Agregar valor"):
            st.session_state.mi_lista.append(valor)
            st.write(f"{valor} agregado a la operación.")
        if st.button("Sumar"):
            sumlist=fn.sumar_lista(st.session_state.mi_lista)
            st.write(f"Suma de la lista: {sumlist:.2f}")
        if st.button("Ingresar valores nuevos"):
            st.session_state.mi_lista=[]

    case "Valores predeterminados":
        st.title("Valores predeterminados")
        prod=st.text_input("Nombre del producto")
        cantidad=st.number_input("Cantidad",min_value=0,step=1)
        precio=st.number_input("Precio",format="%.2f")
        if st.button("Realizar compra"):
            if cantidad and precio:
                producto=fn.producto(prod,cantidad,precio)
                st.write(producto)
            else:
                producto=fn.producto(prod)
                st.write(producto)

    case "Pares e impares":
        st.title("Pares e impares")
        if 'mi_lista' not in st.session_state:
            st.session_state.mi_lista = []
        valor=st.number_input("Ingrese un número",min_value=0,step=1)
        if st.button("Agregar valor"):
            if valor in st.session_state.mi_lista:
                st.write(f"{valor} ya fue agregado anteriormente.")
            else:
                st.session_state.mi_lista.append(valor)
                st.write(f"{valor} agregado a la lista.")
        if st.button("Comprobar"):
            par,impar=fn.numeros_pares_e_impares(st.session_state.mi_lista)
            st.write(f"Numeros pares: {par}")
            st.write(f"Numeros impares: {impar}")
        if st.button("Ingresar valores nuevos"):
            st.session_state.mi_lista=[]

    case "Multiplicación":
        st.title("Multiplicación")
        valores=st.text_input("Ingrese sus valores separados por comas \" , \"")
        if st.button("Calcular"):
            if valores:
                try:
                    list_valores=[float(valor) for valor in valores.split(",")]
                    res=fn.multiplicar_todos(*list_valores)
                    st.write(f"El resultado es: {res}")
                except ValueError:
                    st.warning("Ingrese números válidos.")
            else:
                res=fn.multiplicar_todos()
                st.write(f"Resultado: {res}")

    case "Información personal":
        st.title("Información personal")
        info=st.text_input("Ingrese su información (\"Dato1:Valor1, Dato2:Valor2, ...\")")
        if st.button("Imprimir información en tabla"):
            if info:
                try:
                    par_valores=[par.split(":") for par in info.split(", ")]
                    diccionario={clave: valor for clave, valor in par_valores}
                    informacion=fn.informacion_personal(**diccionario)
                    df = pd.DataFrame([informacion])
                    st.dataframe(df.transpose())
                except ValueError:
                    st.warning("Ingrese correctamente su información")
            else:
                st.write("No ingreso valores.")
        if st.button("Imprimir información en texto"):
            if info:
                try:
                    par_valores=[par.split(":") for par in info.split(", ")]
                    diccionario={clave: valor for clave, valor in par_valores}
                    informacion=fn.informacion_personal(**diccionario)
                    for llave, valor in informacion.items():
                        st.write(f"{llave}: {valor}")
                except ValueError:
                    st.warning("Ingrese correctamente su información")
            else:
                st.write("No ingreso valores.")

    case "Calculadora flexible":
        st.title("Calculadora flexible")
        num1=st.number_input("Número 1",format="%.2f")
        num2=st.number_input("Número 2",format="%.2f")
        operacion=st.selectbox("Operación a realizar",["Suma","Resta","Multiplicación","División"])
        if st.button("Calcular"):
            resultado=fn.calculadora_flexible(num1,num2,operacion)
            if resultado is str:
                st.write(resultado)
            else:
                st.write(f"El resultado es: {resultado:.2f}")
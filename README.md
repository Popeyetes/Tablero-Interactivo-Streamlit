# Objetivo
Este proyecto consiste en un tablero interactivo desarrollado con Streamlit. Su propósito es permitir al usuario realizar diversas actividades, para las cuales deberá tomar decisiones entre las opciones que ofrece la aplicación.

La aplicación comienza en una página principal donde se proporciona una explicación breve de cada uno de los apartados y su uso. Además, cuenta con una caja de selección que permite navegar entre las diferentes páginas y explorar las distintas secciones.


# Código
El programa dispone de un archivo denominado funciones.py, en el cual se encuentran implementadas las diversas tareas necesarias para el funcionamiento del sistema. Esta estructura permite que la sección principal no se vea sobrecargada con múltiples acciones, limitándose casi exclusivamente a la interacción con el usuario.

El archivo funciones.py contiene diez funciones específicas, cada una correspondiente a un apartado del programa. La responsabilidad de estas funciones es desarrollar las soluciones a los problemas planteados y devolver los resultados a la página principal.

Además, el programa incorpora el framework Pandas, utilizado principalmente para manejar estructuras de datos tipo DataFrame. Esto facilita una visualización más cómoda y eficiente de la información.


# Explicación del código
 Las interacciones con el usuario se realizan mediante los modulos button(),text_input(), number_input() y selectbox(); con ellos se podrá recibir información de las opciones tomadas en la aplicación y realizarlas dentro del programa, al recibir información se manejan variables y se usan como parametros que seran usados para usar las funciones que se encuentran en funciones.py, el valor que retorna se almacena y se muestra en la aplicación.

 En algunas de las actividades es necesario convertir una variable a otro tipo de valor, esto para cumplir con los parametros necesarios y no provocar un error.Por ejemplo, para el apartado Multiplicación pasamos los elementos ingresados a una lista, este tipo de valor es uno que puede cumplir como argumento para la función.

 En el archivo funciones.py, se declaran diez funciones, estas funciones son desarrollos cortos y precisos.
 ## saludo()
 - Esta función recibe un parametro y devuelve un string con parametro ingresado.
## sumar()
- Esta función recibe dos parametros, realiza una suma y devuelve el resultado.
## calcular_area_triangulo()
- Esta función recibe dos parametros, hace el calculo con la formula (base*altura)/2 para obtener el area y devuelve el resultado.
## calcular_precio_final()
- Esta función recibe tres parametros, con los que se calcula un precio aplicando un descuento y un producto, en caso que no se reciba un descuento y un impuesto, el calculo se hará con valores predeterminados.
## sumar_lista()
- Esta función recibe como parametro una lista, los valores de esa lista se suman con ayuda de un ciclo y devuelve su resultado.
## producto()
- Esta función recibe tres parametros, se realiza un calculo de un producto con el precio y la cantidad solicitada; devuelve un string con los parametros recibidos y el calculo hecho, en caso de no recibir un precio y una cantidad se usaran parametros predeterminados.
## numeros_pares_e_impares()
- Esta función recibe como parametro una lista y retorna dos con los mismos valores separados respecto a si es par o impar.
## multiplicar_todos()
- Esta función recibe como parametro un *args y mediante un ciclo se multiplican los valores y devuelve el resultado.
## informacion_personal()
- Esta función recibe un **kwargs, mediante un ciclo añade los valores a un diccionario ordenado y lo devuelve.
## calculadora_flexible()
- Esta función recibe tres parametros, dos serán los valores que se calcularan y otro será la operación con la que se calculará el resultado; devuelve el resultado respecto a la operación elegida, si no se recibe una operación se usa el parametro predeterminado.

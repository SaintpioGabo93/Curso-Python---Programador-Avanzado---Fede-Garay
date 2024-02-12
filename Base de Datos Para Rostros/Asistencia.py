import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime


# ---------------- Cargar imagenes que nos van a servir de control -------------------- #
# Se creará un loop para recorrer y cargar todas las fotos

ruta = 'Empleados' # Este es el nombre del archido en la dirección donde está este proyecto
mis_imagenes = [] # Esta lista se queda vacía, y se crea de forma dinámica cada que se ejecuta el programa
nombres_empleados = []

lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual) # Iniciará con la lista vacía de nombre empleados, e irá agregando las fotos
    nombres_empleados.append(os.path.splitext(nombre)[0]) # Esto convierte a los nombres de las fotos en una lista

print(nombres_empleados)

# --------------------------------- Codificación de Imagenes -------------------------- #

# Se creará una función para codificar todas las imagenes de la lista creada

def codificador(imagenes):

    # crear una lista nueva
    lista_codificada = []

    # pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)

    # devolver lista codificada
    return lista_codificada

# ------ Función para registrar los ingresos ------- #
# En esta función se puede codificar que se guarde la foto que se tomó, que se enlace a una base de datos, etc.

def registro_ingresoPersonal(persona):

    f = open('registro_dePersonas.csv','r+') # Abrimos dentro de la misma carpeta el archiro registro_dePersonas
    lista_datos = f.readlines() # esta función nos sirve pare leer todas las líneas de nuestro archivo
    nombres_registro = [] # Esta lista guardará a las personas que quedarán registradas
    for linea in lista_datos: #
        ingreso = linea.split(',') # Con este métodos, separamos cada que se encuentre una coma
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        hora_actual = datetime.now()
        string_hora_actual = hora_actual.strftime('%H:%M:%S')

        f.writelines(f'\n{persona}, {string_hora_actual}')



lista_empleados_codificada = codificador(mis_imagenes)

# print(len(lista_empleados_codificada))

# ------------------------- Tomar Imagen de una Camara Web --------------------------- #

captura_WebCam = cv2.VideoCapture(0, cv2.CAP_DSHOW) # El cero es un ID, y el siguiente argumento es para mostrar la captura de la web cam

# --------------------------- Leer imagen de la camara ------------------------------ #

# Esta función arroja dos valores, primero el de si ha podido realizar la caputra, y después la imagen propiamente dicha
exito, imagen = captura_WebCam.read()

if not exito:
    print("No se pudo tomar la captura")

else:
    # --- Reconocerdor de cara en la captura ---- #
    cara_capturaWC_localizada = fr.face_locations(imagen) # El argumento es la variable imagen obtenida de captura.read()

    # --- Codificar cara capturada --- #

    cara_capturada_codificada = fr.face_encodings(imagen,cara_capturaWC_localizada)


    # ---- Buscamos coincidencia ---- #

    for caraCodificada, caraUbicada in zip(cara_capturada_codificada,cara_capturaWC_localizada):

        # Aqui se comparan las imagenes de la lista de empleados con la cara capturada y codificada de la Camara Web
        coincidencias = fr.compare_faces(lista_empleados_codificada, caraCodificada)
        distancias = fr.face_distance(lista_empleados_codificada,caraCodificada)

        print(distancias)


        # -------- Buscamos el argumento de menor valor que es la coincidencia y la guardamos en una variable ---- #
        indice_de_coincidencias = numpy.argmin(distancias)

        # ------ Mostrar Indice de Coincidencias -------------- #

        if distancias[indice_de_coincidencias] > 0.6:
            print("No coincide con ninguno de nuestros empleados")

        else:
            # ----- Buscar el nombre del Empleado ----- #

            nombre = nombres_empleados[indice_de_coincidencias]
            y1, x2, y2, x1 = caraUbicada # Aquí se guardan las los cuadros generados por cara_capturaWC_localizada
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (100, 200, 30), 2) # Codificamos el rectangulo que rodará a la cara
            cv2.rectangle(imagen,(x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED) # En este rectángulo, se colocará el nombre de la persona encontrada
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

            # ----- Llamamos a la función de registro de
            registro_ingresoPersonal(nombre)

            # ----- Mostrar Imagen obtenida ------- #

            cv2.imshow('Imagen Cámara Web', imagen)

            # ----- Mantener ventana abierta ------ #

            cv2.waitKey(0)

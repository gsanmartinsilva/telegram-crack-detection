# Piloto de Detección de Grietas usando Telegram

Hola! 
Este repositorio alberga un mini-proyecto que desarrollé para un workshop del [Diploma en Big Data Analytics en Confiabilidad y Mantenimiento](http://ingenieria.uchile.cl/cursos/150259/diploma-en-big-data-analytics-en-confiabilidad-y-mantenimiento) del departamento de Ingeniería Civil Mecánica de la Universidad de Chile. 

## Introducción
Una empresa de inspeccion y reparación de estructuras cuenta con un dataset de imagenes de grietas en concreto que estan correctamente etiquetadas de forma binaria según:

* Clase 0: No existen grietas que requieran reparación.
* Clase 1: Sí existen grietas que requieran reparación.

Con este dataset se entrena un algoritmo in-house usando redes neuronales convolucionales que obtiene muy buenos resultados en accuracy, recall, f-score, etc. El objetivo de este algoritmo detector de grietas es desplegarlo en terreno, para dos posibles usos:


1. Para que un inspector técnico pueda apoyarse de una herramienta digital para evaluar las estructuras que vea en terreno.
2. Para que un dron equipado con una camara pueda usarse para inspeccionar estructuras complejas, como puentes o techos internos, dónde usualmente se requeriria personal especializado en maniobras de altura, permisos, equipo cómo gruas alzahombres, etc.

Existen muchas maneras de hacer el deployment de esta solución, por ejemplo se podría alojar el algoritmo en un servidor online (AWS, Google Cloud, etc) y enviar fotos sacadas en terreno. Sin embargo es muy común querer hacer primero un piloto rápido y barato de la solución, para ver como se comporta en terreno y cómo los operadores se adaptan al uso de la nueva tecnología antes de invertir tiempo y dinero en un deployment "tradicional".



Mi propuesta es usar el API de telegram (servicio de mensajería instantánea similar a WhatsApp) para programar en python un bot para realizar las siguientes etapas:


1. El operador o dron saca una foto con un smartphone o camará integrada de la zona a inspeccionar.
2. Esa foto es enviada a través de telegram, usando de forma gratuita toda la encriptación y seguridad dispuesta por la aplicación, hacia el computador o servidor in-house.
3. El computador procesa la imagen para detectar la presencia de grietas severas. Esto elimina la necesidad de un computador o sistema de procesamiento en terreno.
4. Mediante la API de telegram el resultado es enviado al operador de forma instantanea, recibiendo el analisis en un formato human-friendly segundos despues del query inicial.

Esta implementación cuenta con varias ventajas que listo a continuación.

Ventajas:
* La comunicación es simple: solo requiera un celular con camara decente conectado a internet.
* No es necesario levantar servidores, páginas web o nada similar. Esto lo hace ideal para proyectos piloto en terreno.
* El operador solamente debe saber como enviar mensajes a través de telegram, que es exactamente igual a mandarle una foto a un familiar por whatsapp.
* En terminos de costo monetario, es sumamente barato: solo requiere contar con un celular en terreno.


Obviamente, esta implementación se puede usar para muchas más cosas. A traves de telegram se pueden enviar muchas más cosas que imagenes, y también se pueden recibir reportes mucho más complejos que una clasificación binaria. Con el uso de esta API se pueden levantar pilotos de complejidad muy alta en poco tiempo a costo _casi_ cero. Pienso que es una herramienta ideal para muchas empresas y situaciones.

## Organización del repositorio

Este repositorio cuenta con muy poquitos archivos, pues es un ejemplo sencillo de implementar.

La estructura del repositorio es:
```
telegram-crack-detection
│   cnn.ipynb
│   README.md
│   telegram_bot.py
├───data
│   ├───test_data        
│   └───training_data
│   
└───models
    │   model_cnn.h5

```



* Dentro de la carpeta `data` están las imagenes de entrenamiento y testeo para entrenar el algoritmo.
* En el archivo `cnn.ipynb` se realiza en entrenamiento y testeo de la red convolucional para detectar las grietas. Tanto la red como el entrenamiento y el guardado posterior de los pesos se realiza con TensorFlow.
* El archivo `telegram_bot.py` contiene todo lo necesario para poder crear y correr el bot de telegram. También en este archivo se carga y usa el modelo entrenado en `cnn.ipynb` para el procesamiento de nuevas fotografías tomadas en terreno.



## ¿Cómo usar el bot?

Para poder usar este proyecto piloto, primero es necesario crear el bot. Para ello pueden referirse a este [tutorial](https://core.telegram.org/bots). El proceso de creación arrojará el token o identificador del bot, que es necesario incluir en la variable ``token`` del archivo ``telegram_bot.py`` para que el archivo sepa comunicarse con el bot respectivo. Luego, es cosa de acceder al bot desde telegram en nuestro smartphone y enviarle texto o imagenes para activar las funciones respectivas.



## Librerías

Todas las librerías usadas en este proyecto estan contenidas en el archivo requirements.yml, apto para replicar el environment en conda.















"""
Codigo de un bot muy simple que recibe una imagen, la procesa con un clasificador
y devuelve la respuesta como un text message en telegram.

Nota: Este codigo esta fuertemente inspirado en los ejemplos de la API: https://python-telegram-bot.readthedocs.io/en/stable/
Uso:
- Correr este archivo en una terminal
- Para terminar, cortar la terminal con CTRL+C
"""

# Importar librerias de telegram para la comunicacion y tensorflow para el procesamiento
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot
import logging
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img






# Ejecutar un Logging para ver posibles errores
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)




# Definir la función que va a cargar el modelo, procesar la imagen y devolver un string 
# identificando la clase correspondiente.

def predict(file_name):    
    # cargar la imagen desde la memoria del computador o servidor
    img = img_to_array(load_img(file_name, target_size = (60,60),
                                  color_mode = 'grayscale'), dtype='float32')
    # cambiar el tamaño de la imagen para coincidir con la entrada de la red
    img = np.reshape(img, (1,60,60,1))
    # cargar el modelo
    loaded_model = keras.models.load_model('models/model_cnn.h5')
    # procesar la imagen
    pred = loaded_model.predict(img)
    # como es una clasificación binaria, el output de la red es una sigmoide.
    # por ende, si es >0.5 es clase 1, si es <0.5 es clase 0.
    if pred>0.5:
        return 'Es una grieta!'
    else:
        return 'No es una grieta!'


"""
Los handlers son funciones que sirven para poder procesar diferentes inputs desde telegram.
Este ejemplo tiene dos, uno que procesa texto y otro que procesa imagenes.
- El de texto se llama echo, y esta diseñado para probar si el bot esta operativo. Simplemente devuelve un string
identico al que se le envie (de ahí el nombre)
- El de imagenes se llama image_handler y lo que hace es recibir la imagen, guardarla en la memoria y posteriormente llamar
a la funcion predict().
"""
 


def image_handler(update,context):
    file = context.bot.getFile(update.message.photo[-1].file_id)
    file.download('image.jpg')
    update.message.reply_text(predict('image.jpg'))

def echo(update, context):
    """Echo the user message."""
    print('received')
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


    
    
# token o codigo identificador del bot
token = '670402980:AAFyYWKQeVlrX9dA7Q7bgF7DJneUJtkkm0w'
    
def main():
    """
    Funcion que crea el bot.

    """
    
    # Crear el bot y el metodo que crea respuestas
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Añadir los handlers con los codigos o tipos de mensajes respectivos.
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.photo, image_handler))
    dp.add_error_handler(error)
    
    # Prender el bot y dejarlo en idle esperando la llegada de imagenes
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
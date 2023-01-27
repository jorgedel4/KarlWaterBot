import pywhatkit as pwk
from time import sleep

while (True):
    try:
        pwk.sendwhats_image("+522228097257", # Numero destino
            "brett.jpg", # ubicacion de imagen
            "Toma awa y no procrastines :3", # caption
            tab_close=True) # cerrar ventana despues de mensaje
    except Exception as e:
        print(f"Error {e}")

    # Repite cada hora (argumento en segundos)
    sleep(3600)
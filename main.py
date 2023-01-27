import pywhatkit as pwk
from time import sleep

while (True):
    try:
        pwk.sendwhats_image("+522228097257", 
            "brett.jpg",
            "Toma awa y no procrastines :3",
            tab_close=True)
    except Exception as e:
        print(f"Error {e}")

    sleep(3600)
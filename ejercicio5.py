import hashlib
from hmac import digest_size
def encriptar(mensaje):
    mensaje=hashlib.sha256()
    mensaje.update=input("Introduce un mensaje: ")
    mensaje.digest_size(8)
    mensaje.digest(digest_size)
    print(hashlib.sha256(mensaje.update).digest(8))
rango_encriptar=range(ord(' '), ord('}'))
rango_desencriptar=range(chr(32),chr(125))
def crear_tablaencriptacion(tamaño):
    tabla1= [None] * tamaño
    return tabla1
def crear_tabaldesencriptacion(tamaño):
    tabla2= [None] * tamaño
    return tabla2
tabla1=crear_tablaencriptacion(rango_encriptar)
tabla2=crear_tabaldesencriptacion(rango_desencriptar)

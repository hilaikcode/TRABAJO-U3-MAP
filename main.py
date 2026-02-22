#PROCEDIMIENTOS

#PROCEDIMIENTO PEDIR CREDENCIALES

usuarios = []

def pedir_credenciales():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    return usuario, contraseña

#PROCEDIMIENTO VERIFICAR CREDENCIALES
def verificar_credenciales(usuario, contraseña):
    for usuario in usuarios:
        if usuario["nombre"] == usuario and usuario["contraseña"] == contraseña:
            return True
    else:
        return False
    
#PRCEDIMIENTO INGRESAR LIBROS
def ingresar_libros():
    titulo = input("Ingrese el título del libro: ")
    año = input("Ingrese el año de publicación del libro: ")
    libro = {"titulo": titulo, "año": año}
    return libro

#PROCEDIMIENTO VERIFICAR LIBROS EN EL INVENTARIO
def verificar_libros(libro, inventario):
    for item in inventario:
        if item["titulo"] == libro["titulo"] and item["año"] == libro["año"]:
            return True
    else:
        return False
    
#FLUJO PRINCIPAL PROCESO
def main():
    usuario, contraseña = pedir_credenciales()
    if verificar_credenciales(usuario, contraseña):
        print("Credenciales válidas.")
        libro = ingresar_libros()
        inventario = [] 
        if verificar_libros(libro, inventario):
            print("El libro se encuentra disponible, está ubicado en: [ubicación del libro].")
        else:
            print("El libro no se encuentra disponible para prestramo.")



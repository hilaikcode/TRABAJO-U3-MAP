#DATOS PARA PODER AUTOMATIZAR EL PROCESO
usuarios = [
    {"nombre": "juan", "contraseña": "1234"},
    {"nombre": "ana", "contraseña": "abcd"}
]

inventario = [
    {"titulo": "La dama de las camelias", "año": "1848"},
    {"titulo": "Cumbres borroscosas", "año": "1847"}
]


# PROCEDIMIENTOS

def verificar_credenciales(nombre_usuario, contraseña):
    for user in usuarios:
        if user["nombre"] == nombre_usuario and user["contraseña"] == contraseña:
            return True
    return False


def verificar_libros(libro):
    for item in inventario:
        if item["titulo"] == libro["titulo"] and item["año"] == libro["año"]:
            return True
    return False


# FLUJO PRINCIPAL (AUTOMÁTICO)

def main():

    # Simulación automática
    usuario = "juan"
    contraseña = "1234"

    if verificar_credenciales(usuario, contraseña):
        print("Credenciales válidas.")

        libro = {"titulo": "Python Basico", "año": "2020"}

        if verificar_libros(libro):
            print("Libro disponible.")
        else:
            raise Exception("Libro no disponible")
    else:
        raise Exception("Credenciales inválidas")


if __name__ == "__main__":
    main()
    



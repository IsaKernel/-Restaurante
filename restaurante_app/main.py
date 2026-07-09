
# main.py
# Punto de arranque del sistema de "Kasabe SCSM".
# Los objetos se crean a partir de datos ingresados
# por el usuario mediante input().
 
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante
 
 
# ----------------------------------------------------------
# Muestra el menú principal del sistema.
# ----------------------------------------------------------
def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE GESTIÓN KASABE SCSM")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")
    print("========================================")
 
 
# ----------------------------------------------------------
# Solicita los datos de un producto al usuario y lo registra.
# Args:
#     restaurante: Objeto de la clase Restaurante.
# ----------------------------------------------------------
def registrar_producto(restaurante) -> None:
    print("\n=== REGISTRAR PRODUCTO ===")
    try:
        nombre = input("Nombre: ")
        categoria = input("Categoría (Ej: Platillo, Bebida): ")
        precio = float(input("Precio: "))
        disponible_input = input("¿Disponible? (s/n): ").strip().lower()
        disponible = disponible_input == "s"
 
        # Creación del objeto a partir de los datos ingresados
        producto = Producto(nombre, categoria, precio, disponible)
        restaurante.registrar_producto(producto)
 
    except ValueError as e:
        print(f"\nError: {e}")
 
 
# ----------------------------------------------------------
# Solicita los datos de un cliente al usuario y lo registra.
# Args:
#     restaurante: Objeto de la clase Restaurante.
# ----------------------------------------------------------
def registrar_cliente(restaurante) -> None:
    print("\n=== REGISTRAR CLIENTE ===")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    celular = input("Celular: ")
 
    # Creación del objeto con @dataclass a partir de los datos ingresados
    cliente = Cliente(nombre, correo, celular)
    restaurante.registrar_cliente(cliente)
 
 
# ----------------------------------------------------------
# Solicita el nombre de un producto y lo busca en el sistema.
# Args:
#     restaurante: Objeto de la clase Restaurante.
# ----------------------------------------------------------
def buscar_producto(restaurante) -> None:
    print("\n=== BUSCAR PRODUCTO ===")
    nombre = input("Nombre del producto: ")
    restaurante.buscar_producto(nombre)
 
 
# ----------------------------------------------------------
# Solicita el nombre de un cliente y lo busca en el sistema.
# Args:
#     restaurante: Objeto de la clase Restaurante.
# ----------------------------------------------------------
def buscar_cliente(restaurante) -> None:
    print("\n=== BUSCAR CLIENTE ===")
    nombre = input("Nombre del cliente: ")
    restaurante.buscar_cliente(nombre)
 
 
# ----------------------------------------------------------
# Punto de entrada del sistema.
# ----------------------------------------------------------
def main() -> None:
    restaurante = Restaurante()
 
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
 
        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            restaurante.listar_productos()
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            restaurante.listar_clientes()
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            print("\nGracias por utilizar el sistema Kasabe SCSM.")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")
 
 
if __name__ == "__main__":
    main()
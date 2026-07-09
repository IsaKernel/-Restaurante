# servicios/restaurante.py
# Clase Restaurante encargada de administrar las listas
# de productos y clientes del sistema.
 
class Restaurante:
 
  
    # Constructor de la clase Restaurante.
    # Inicializa las listas vacías de productos y clientes.
   
    def __init__(self):
        # Listas para almacenar múltiples objetos
        self.__productos = []
        self.__clientes = []
 
    
    # Registra un producto en la lista del sistema.
    # Args:
    #     producto: Objeto de tipo Producto.
    
    def registrar_producto(self, producto) -> None:
        self.__productos.append(producto)
        print(f"\nProducto '{producto.nombre}' registrado correctamente.")
 
    
    # Lista todos los productos registrados en el sistema.
    
    def listar_productos(self) -> None:
        if not self.__productos:
            print("\nNo hay productos registrados.")
            return
        print(f"\n{'='*40}")
        print("  PRODUCTOS REGISTRADOS")
        print(f"{'='*40}")
        for i, producto in enumerate(self.__productos, 1):
            print(f"\n  [{i}]")
            producto.mostrar_informacion()
 
    
    # Busca un producto por nombre en la lista.
    # Args: nombre (str): Nombre del producto a buscar.
   
    def buscar_producto(self, nombre: str) -> None:
        encontrado = False
        for producto in self.__productos:
            if producto.nombre.lower() == nombre.lower():
                print(f"\n{'='*40}")
                print("  PRODUCTO ENCONTRADO")
                print(f"{'='*40}")
                producto.mostrar_informacion()
                encontrado = True
                break
        if not encontrado:
            print(f"\nProducto '{nombre}' no encontrado.")
 
    
    # Registra un cliente en la lista del sistema.
    # Args:cliente: Objeto de tipo Cliente.
  
    def registrar_cliente(self, cliente) -> None:
        self.__clientes.append(cliente)
        print(f"\nCliente '{cliente.nombre}' registrado correctamente.")
 
    # ----------------------------------------------------------
    # Lista todos los clientes registrados en el sistema.
    # ----------------------------------------------------------
    def listar_clientes(self) -> None:
        if not self.__clientes:
            print("\nNo hay clientes registrados.")
            return
        print(f"\n{'='*40}")
        print("  CLIENTES REGISTRADOS")
        print(f"{'='*40}")
        for i, cliente in enumerate(self.__clientes, 1):
            print(f"\n  [{i}]")
            cliente.mostrar_informacion()
 
    # ----------------------------------------------------------
    # Busca un cliente por nombre en la lista.
    # Args: nombre (str): Nombre del cliente a buscar.
    # ----------------------------------------------------------
    def buscar_cliente(self, nombre: str) -> None:
        encontrado = False
        for cliente in self.__clientes:
            if cliente.nombre.lower() == nombre.lower():
                print(f"\n{'='*40}")
                print("  CLIENTE ENCONTRADO")
                print(f"{'='*40}")
                cliente.mostrar_informacion()
                encontrado = True
                break
        if not encontrado:
            print(f"\nCliente '{nombre}' no encontrado.")
 
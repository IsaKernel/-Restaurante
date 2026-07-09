# modelos/producto.py
# Clase Producto implementada con constructor tradicional,
# decoradores @property y @setter con validaciones.
 
class Producto:

    # Constructor de la clase Producto.
    # Inicializa los atributos mediante los setters para
    # aplicar las validaciones desde el inicio.
    
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible
 
    # Property y setter para el atributo nombre.
    # Valida que el nombre no esté vacío.
  
    @property
    def nombre(self) -> str:
        return self.__nombre
 
    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self.__nombre = valor.strip()
 
    
    # Property y setter para el atributo categoria.
    # Valida que la categoría no esté vacía.
 
    @property
    def categoria(self) -> str:
        return self.__categoria
 
    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self.__categoria = valor.strip()
 
   
    # Property y setter para el atributo precio.
    # Valida que el precio sea mayor a cero.
   
    @property
    def precio(self) -> float:
        return self.__precio
 
    @precio.setter
    def precio(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self.__precio = valor
 
  
    # Property y setter para el atributo disponible.
    
    @property
    def disponible(self) -> bool:
        return self.__disponible
 
    @disponible.setter
    def disponible(self, valor: bool) -> None:
        self.__disponible = valor
 
    
    # Muestra la información completa del producto en consola.
    def mostrar_informacion(self) -> None:
        print(f"  Nombre     : {self.__nombre}")
        print(f"  Categoría  : {self.__categoria}")
        print(f"  Precio     : ${self.__precio:.2f}")
        print(f"  Disponible : {'Sí' if self.__disponible else 'No'}")
 
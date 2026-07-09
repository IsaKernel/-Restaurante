# modelos/cliente.py
# Clase Cliente implementada con el decorador @dataclass.
# Los atributos se definen de forma declarativa y el
# constructor se genera automáticamente.
 
from dataclasses import dataclass

# Clase Cliente
# Representa a un cliente registrado en el restaurante.
# Se utiliza @dataclass para generar el constructor
# y la representación del objeto automáticamente.

@dataclass
class Cliente:
    nombre: str
    correo: str
    celular: str
 
    # ----------------------------------------------------------
    # Muestra la información completa del cliente en consola.
    # ----------------------------------------------------------
    def mostrar_informacion(self) -> None:
        print(f"  Nombre  : {self.nombre}")
        print(f"  Correo  : {self.correo}")
        print(f"  Celular : {self.celular}")
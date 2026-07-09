# 🍽️ Kasabe SCSM — Sistema de Gestión de Restaurante

> **Estudiante:** Cueva Ochoa Sabrina Isabel
> **Materia:** Programación Orientada a Objetos
> **Semana:** 7 — Constructores, Decoradores y menú interactivo.

---

## 📋 Descripción del sistema

**Kasabe SCSM** es un sistema interactivo de gestión de restaurante desarrollado en Python. Permite registrar, listar y buscar productos y clientes desde un menú de consola, creando objetos a partir de datos ingresados por el usuario en tiempo de ejecución.

El sistema aplica constructores tradicionales, decoradores `@property` y `@setter` para controlar el acceso a los atributos de `Producto`, y el decorador `@dataclass` para simplificar la definición de la clase `Cliente`.

---

## 🗂️ Estructura del proyecto
```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
``` 


| Archivo | Ubicación | Responsabilidad |
|---|---|---|
| `__init__.py` | `modelos/` y `servicios/` | Identifica las carpetas como paquetes de Python |
| `producto.py` | `modelos/` | Clase `Producto` con constructor, `@property` y `@setter` |
| `cliente.py` | `modelos/` | Clase `Cliente` implementada con `@dataclass` |
| `restaurante.py` | `servicios/` | Administra listas de productos y clientes |
| `main.py` | raíz | Menú interactivo y punto de arranque del programa |

---

## 🔧 Constructor en la clase Producto

La clase `Producto` utiliza el constructor tradicional `__init__()`. Al momento de crear un objeto, los valores ingresados por el usuario pasan directamente a los setters, donde son validados antes de almacenarse.

```python
def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool):
    self.nombre = nombre        # pasa por @nombre.setter
    self.categoria = categoria  # pasa por @categoria.setter
    self.precio = precio        # pasa por @precio.setter
    self.disponible = disponible
```

---

## 🎛️ Uso de @property y @setter

Los atributos de `Producto` están protegidos mediante `@property` y `@setter`. Esto garantiza que ningún valor inválido pueda almacenarse en el objeto.

| Atributo | Validación aplicada |
|---|---|
| `nombre` | No puede estar vacío |
| `categoria` | No puede estar vacía |
| `precio` | Debe ser mayor a cero |
| `disponible` | Acepta cualquier valor `bool` |

```python
@precio.setter
def precio(self, valor: float) -> None:
    if valor <= 0:
        raise ValueError("El precio debe ser mayor a cero.")
    self.__precio = valor
```

---

## 🃏 Uso de @dataclass en la clase Cliente

La clase `Cliente` utiliza el decorador `@dataclass`, que genera automáticamente el constructor y la representación del objeto sin necesidad de definir `__init__()` manualmente.

```python
@dataclass
class Cliente:
    nombre: str
    correo: str
    celular: str
```

| Atributo | Tipo | Descripción |
|---|---|---|
| `nombre` | `str` | Nombre completo del cliente |
| `correo` | `str` | Correo electrónico del cliente |
| `celular` | `str` | Número de celular del cliente |

---

## 🖥️ Menú interactivo

El sistema se controla desde un menú en consola que se mantiene activo hasta que el usuario seleccione la opción de salir.

```
========================================
        SISTEMA DE GESTIÓN KASABE SCSM
========================================
1. Registrar producto
2. Listar productos
3. Buscar producto
----------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
----------------------------------------
7. Salir
========================================
```

### Flujo de ejecución
input() del usuario
↓
constructor del modelo
↓
creación del objeto
↓
registro en la clase Restaurante
↓
listado o búsqueda del registro

---

## ▶️ Cómo ejecutar el programa

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

---

## 💡 Reflexión

Trabajar con objetos creados a partir de datos ingresados por el usuario es un punto de diferencia importante respecto a semanas anteriores, donde los objetos se definían directamente en el código. Esa forma de trabajar es útil para aprender, pero no llega a reflejar cómo funciona un sistema real.

Respecto a esta semana, cuando el objeto se construye desde `input()`, el programa ya no sabe de antemano qué información recibirá. Eso obliga a pensar con más cuidado en las validaciones: qué pasa si el usuario deja el nombre vacío, qué pasa si ingresa un precio negativo. Los `@setter` resolvieron ese problema de forma elegante, porque la validación ocurre en el momento exacto en que se asigna el valor, no después.
El decorador `@dataclass` en `Cliente` demostró que no siempre hace falta escribir todo manualmente. Cuando una clase solo necesita almacenar datos sin lógica significativamente compleja,`@dataclass` genera el constructor automáticamente y el código queda más limpio y directo.
En conjunto, estas herramientas enseñaron que construir bien un objeto desde el inicio — validando sus datos, controlando su acceso y eligiendo la forma correcta de definirlo — es tan importante como hacer que el programa funcione.
Y en sí, considero que un programa que solo funciona con datos quemados no es como tal un sistema, es sino una "demostración". La entrada del usuario es lo que convierte el código en una herramienta que alguien más puede usar.Por lo que el programa cobra vida. Cada ejecución puede registrar productos diferentes, clientes diferentes, precios diferentes y el sistema va a responder a la realidad en lugar de repetir siempre lo mismo.
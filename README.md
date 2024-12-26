# ZincWriter Backend

Este es un backend desarrollado con **FastAPI** para procesar archivos de texto, convertirlos en datos estructurados y generar código **MiniZinc**. El proyecto se utiliza para cargar archivos con información sobre productos, materiales y demandas, y luego generar un modelo de optimización en MiniZinc para resolver problemas relacionados con la asignación de recursos y la maximización de beneficios.

## Características

- **Cargar archivos**: La API permite cargar archivos `.txt` que contienen datos relacionados con productos, materiales y restricciones.
- **Generación de código MiniZinc**: El backend procesa los datos y genera código MiniZinc basado en las restricciones y los valores proporcionados en el archivo cargado.
- **Soporte para múltiples productos y materiales**: El backend maneja una cantidad variable de productos y materiales definidos en el archivo de entrada.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- **Python 3.8+**
- **pip** (gestor de paquetes de Python)
- **FastAPI**: https://fastapi.tiangolo.com/#installation
- **Uvicorn** (servidor ASGI para ejecutar FastAPI)

## Instalación

### Paso 1: Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone git@github.com:Kahyberth/zinc-writer-backend.git
```

### Paso 2: Crear un entorno virtual (opcional, pero recomendado)
Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto. Si no tienes un entorno virtual, crea uno con:
```
python -m venv venv
```


Activa el entorno virtual:
- En windows:``.\venv\Scripts\activate``
- En macOS/Linux:``source venv/bin/activate``


### Paso 3: Instala directamente lo necesario si aún no lo tienes:
```
pip install fastapi uvicorn
```

### Paso 4: Inicia el servidor
```
fastapi dev main.py
```

### Si quieres revisar los endpoints como funcionan, Ingresa a la siguiente ruta:
```
http://127.0.0.1:8000/docs
```






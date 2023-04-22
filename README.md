# ProyectoDeGrado

# API Clasificación de residuos

API Que realiza las predicciones del modelo de visión por computador entrenado sobre la tecnología YOLO-V5

## Requerimientos
 - Python 3
 - Docker 20.10.12

---
## Tabla de Contenido

- [Descripción](#descripción)
- [Arquitectura](#arquitectura)
- [Construido con](#construido-con)
- [Entorno de desarrollo](#desarrollo)
- [Despliegue con Docker](#Docker)
- [Documentación técnica](#Url-a-Login)
- [Endpoints API](#Endpoints-API)
- [Autores](#autores)
- [Licencia](#licencia)

---

## Descripción

El repositorio de ***API Clasificación de residuos*** tiene como objetivo proveer las funcionalidades de detección de objetos de acuerdo al modelo previamente entrenado sobre la tecnología YOLO V5.

## Arquitectura
En este enlace se encuentra la Arquitectura de componentes definida para la Solución: [Análisis de Arquitectura ](https://www.google.com)
 

## Construido con 

El código de encuentra implementado con Python 3 y FastAPI las librerías usadas se encuentran en :  

- requirements.txt

## Entorno de desarrollo
1. Instale Python 3 o superior. 
2. Clone este repositorio.
3. Instale y active el manejador de ambientes con [venv](https://docs.python.org/3/library/venv.html).
4. Instale las dependencias con PIP
    ```sh
    pip install -r requirements.txt
    ```
5. Ejecute el servidor para iniciar la aplicación.
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8001
    ```
6. Abra http://localhost:8001/ para visualizar la interface del API

---

## Despliegue con Docker 

### Construcción de la imágen
```sh
  docker build -t clasificacion-residuos-api:latest .
```
### Ejecución del contenedor
```sh
  docker run -p 8000:8000 clasificacion-residuos-api:latest 
```

---

## Documentación técnica
- [Docs](localhost:8000/docs/)

---

## Endpoints API

- **DEV**
	- API: #TODO

- **STAGE**
	- API: 

- **PROD**
	- API: 


---
## Autores

El equipo involucrado en la implementación de estos componentes se detalla a continuación:

 - Equipo técnico: 
	 - Miguel Angel Mora Miranda <miamoram@udistrital.edu.co>
   - Jesid Alberto Escobar <Jaescobarp@udistrital.edu.co>

---

## Licencia

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
- Copyright 2023 ©
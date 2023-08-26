## Instalación (install)


### Paso 1. Crear entorno virtual

```
virtualenv venv
```

### Paso 2. Activar entorno virtual

**En MS Windows**

```
venv\Scripts\activate.ps1
```

**En GNU Linux/Mac OS**

```
source venv/bin/activate
```

**Para desactivar el entorno virtual**
```
deactivate
```

**Para eliminar entorno virtual**
```
rm -rf venv
```

### Paso 3. Instalar dependencias

```
pip install -r requirements/dev.txt
```

Para fijar o guardar un listado de los paquetes necesario de desarrollo:

```
pip freeze > requirements/dev.txt
```
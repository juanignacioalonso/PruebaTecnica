# Usa la imagen oficial de Python como imagen base
FROM python:3.9

# Establece la variable de entorno para evitar la compilación en modo no interactivo
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app/

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Expone el puerto en el que se ejecuta la aplicación Django
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
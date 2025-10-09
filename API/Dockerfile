# Imagen base de Python
FROM python:3.11-slim

# Evita archivos .pyc y activa logs en consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para scikit-learn y numpy
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código y el modelo
COPY app ./app

# Exponer el puerto donde correrá la API
EXPOSE 8000

# Comando que ejecuta la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

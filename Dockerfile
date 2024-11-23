FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Sistem bağımlılıklarını yükle
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıklarını kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Prometheus için geçici dizin oluştur
RUN mkdir -p /tmp && chmod 777 /tmp

# Uygulama kodunu kopyala
COPY . .

# Port ayarı
EXPOSE 8000

# Çalıştırma komutu
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
# Geliştirme Ortamı Kurulumu

## Gereksinimler
- Docker ve Docker Compose
- Python 3.9+
- Git

## Yerel Geliştirme Ortamı Kurulumu

1. Projeyi klonlayın:
bash
git clone https://github.com/your-username/location-tracking.git
cd location-tracking
2. Docker container'larını başlatın:
bash
docker-compose -f docker/docker-compose.yml up --build
3. Veritabanı migrasyonlarını uygulayın:
bash
docker-compose -f docker/docker-compose.yml exec web python manage.py migrate

## API Dokümantasyonu
- Swagger UI: http://localhost:8000/api/swagger/
- ReDoc: http://localhost:8000/api/redoc/

## Metrikler
- Prometheus metrikleri: http://localhost:8000/metrics/

## Servisler
- Django (Web): http://localhost:8000
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- Celery Worker
- Celery Beat
- Grafana: http://localhost:3000

# Yapılandırma Rehberi

## Ortam Değişkenleri
env
Django
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=example.com,www.example.com
Database
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=db
DB_PORT=5432
Redis
REDIS_URL=redis://redis:6379/0
Celery
CELERY_BROKER_URL=redis://redis:6379/0

## Güvenlik Ayarları
- HTTPS zorunluluğu
- CORS yapılandırması
- Rate limiting

## Performans Optimizasyonu
- Cache ayarları
- Static dosya sunumu
- Database optimizasyonu

## Monitoring
- Prometheus metrikleri
- Grafana dashboardları
- Log yönetimi

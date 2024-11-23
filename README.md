# Location Tracking API

Location Tracking API, kullanıcıların konum bilgilerini takip etmek ve yönetmek için geliştirilmiş bir REST API projesidir.

## Özellikler

- Kullanıcı konumlarını kaydetme ve takip etme
- Gerçek zamanlı konum güncellemeleri
- Geçmiş konum verilerini sorgulama
- Prometheus ile metrik toplama
- Grafana ile metrik görselleştirme
- Celery ile asenkron görev yönetimi

## Teknolojiler

- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Docker & Docker Compose
- Prometheus
- Grafana

## Hızlı Başlangıç

1. Projeyi klonlayın:
bash
git clone https://github.com/ogunkirikci/location-tracking.git
cd location-tracking
2. Docker container'larını başlatın:
bash
docker-compose -f docker/docker-compose.yml up --build

3. API'ye erişin:
- API: http://localhost:8000/api/v1/
- Swagger: http://localhost:8000/api/swagger/
- Metrics: http://localhost:8000/metrics/
- Grafana: http://localhost:3000

## Dokümantasyon

Detaylı dokümantasyon için [docs](docs/) klasörüne bakın:

- [Kurulum Rehberi](docs/development/setup.md)
- [Katkıda Bulunma](docs/development/contributing.md)
- [Deployment](docs/deployment/installation.md)
- [Yapılandırma](docs/deployment/configuration.md)

## API Endpoints

- `POST /api/v1/token/` - JWT token alma
- `POST /api/v1/token/refresh/` - JWT token yenileme
- `GET /api/v1/locations/` - Konum listesi
- `POST /api/v1/locations/` - Yeni konum ekleme
- `GET /api/v1/locations/{id}/` - Konum detayı

## Monitoring

- Prometheus metrikleri: http://localhost:8000/metrics/
- Grafana dashboards: http://localhost:3000

## Lisans

Bu proje [MIT](LICENSE) lisansı altında lisanslanmıştır.

## İletişim

- Geliştirici: [Ogün Kırıkçı](mailto:ognkrkci@gmail.com)
- Proje: [GitHub Repository](https://github.com/ogunkirikci/location-tracking)
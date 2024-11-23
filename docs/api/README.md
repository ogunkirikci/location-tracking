# Location Tracking API

Location Tracking API, gerçek zamanlı konum takibi için geliştirilmiş bir REST API servisidir.

## 🚀 Özellikler

- Gerçek zamanlı konum takibi
- JWT tabanlı kimlik doğrulama
- REST API endpoints
- Prometheus metrik toplama
- Grafana ile görselleştirme
- Docker ile containerization

## 🛠 Teknolojiler

- Python 3.9
- Django 4.2.7
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Prometheus & Grafana
- JWT Authentication

## 🏃‍♂️ Hızlı Başlangıç

1. Repoyu klonlayın:
bash
git clone https://github.com/ogunkirikci/location-tracking.git
cd location-tracking

2. Docker ile servisleri başlatın:
bash
docker-compose up --build

3. Migrations'ı uygulayın:
bash
docker-compose exec web python manage.py migrate

4. Superuser oluşturun:
bash
docker-compose exec web python manage.py createsuperuser

## 📚 API Endpoints

### Authentication
POST /api/v1/token/
POST /api/v1/token/refresh/
### Locations
GET /api/v1/locations/
POST /api/v1/locations/
GET /api/v1/locations/{id}/
PUT /api/v1/locations/{id}/
DELETE /api/v1/locations/{id}/


## 📊 Monitoring

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## 🔧 Development

Detaylı geliştirme kılavuzu için [Development Guide](docs/development/README.md) dökümanına bakın.

## 📦 Deployment

Production ortamına deploy etmek için [Deployment Guide](docs/deployment/README.md) dökümanını takip edin.

## 📝 API Documentation

Detaylı API dökümanı için [API Documentation](docs/api/README.md) sayfasını ziyaret edin.

## 🧪 Testing

Testleri çalıştırmak için:

docker-compose -f docker/docker-compose.yml exec web python manage.py test

## 📈 Metrics

Metrikler `/metrics` endpoint'inden Prometheus formatında sunulmaktadır:

- HTTP request sayıları
- Response süreleri
- Hata oranları
- Sistem metrikleri

## 🔐 Security

- JWT tabanlı kimlik doğrulama
- CORS koruması
- Rate limiting
- Input validation

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Bu proje MIT lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📞 Contact

Project Link: [https://github.com/ogunkirikci/location-tracking](https://github.com/ogunkirikci/location-tracking)

# Location Tracking Documentation

## Development
- [Setup Guide](development/setup.md)
- [Contributing Guide](development/contributing.md)

## Deployment
- [Installation Guide](deployment/installation.md)
- [Configuration Guide](deployment/configuration.md)

## Quick Links
- API Documentation: http://localhost:8000/api/swagger/
- Metrics: http://localhost:8000/metrics/
- Grafana: http://localhost:3000
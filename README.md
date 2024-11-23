# Location Tracking API

Location Tracking API is a REST API project developed to track and manage user location information.

## Features

- Save and track user locations
- Real-time location updates
- Query historical location data
- Collect metrics with Prometheus
- Visualize metrics with Grafana
- Manage asynchronous tasks with Celery

## Technologies

- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Docker & Docker Compose
- Prometheus
- Grafana

## Quick Start

1. Clone the project:
bash
git clone https://github.com/ogunkirikci/location-tracking.git
cd location-tracking
2. Start Docker containers:
bash
docker-compose -f docker/docker-compose.yml up --build

3. Access the API:
- API: http://localhost:8000/api/v1/
- Swagger: http://localhost:8000/api/swagger/
- Metrics: http://localhost:8000/metrics/
- Grafana: http://localhost:3000

## Documentation

For detailed documentation, please refer to the [docs](docs/) folder:

- [Setup Guide](docs/development/setup.md)

## API Endpoints

- `POST /api/v1/token/` - Get JWT token
- `POST /api/v1/token/refresh/` - JWT token refresh
- `GET /api/v1/locations/` - Location list
- `POST /api/v1/locations/` - Add new location
- `GET /api/v1/locations/{id}/` - Location detail

## Monitoring

- Prometheus metrics: http://localhost:8000/metrics/
- Grafana dashboards: http://localhost:3000


## Contact

- Developer: [Ogün Kırıkçı](mailto:ognkrkci@gmail.com)
- Project: [GitHub Repository](https://github.com/ogunkirikci/location-tracking)

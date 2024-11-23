#!/bin/bash

# Pull latest images
docker-compose -f docker/docker-compose.prod.yml pull

# Restart services
docker-compose -f docker/docker-compose.prod.yml up -d

# Run migrations
docker-compose -f docker/docker-compose.prod.yml exec -T web python manage.py migrate

# Collect static files
docker-compose -f docker/docker-compose.prod.yml exec -T web python manage.py collectstatic --noinput

# Clear cache
docker-compose -f docker/docker-compose.prod.yml exec -T web python manage.py clear_cache

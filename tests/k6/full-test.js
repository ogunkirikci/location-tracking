// tests/k6/full-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 },  // 0 -> 10 kullanıcı
    { duration: '1m', target: 10 },   // 10 kullanıcıda sabit
    { duration: '20s', target: 0 },   // 10 -> 0 kullanıcı
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // isteklerin %95'i 500ms'den hızlı olmalı
    http_req_failed: ['rate<0.01'],   // %1'den az hata kabul edilebilir
  },
};

export default function () {
  // Metrics endpoint testi
  const metricsRes = http.get('http://localhost:8000/metrics/');
  check(metricsRes, {
    'metrics status is 200': (r) => r.status === 200,
    'metrics response time OK': (r) => r.timings.duration < 200,
  });

  // API endpoints testi
  const apiRes = http.get('http://localhost:8000/api/v1/locations/');
  check(apiRes, {
    'api status is 401': (r) => r.status === 401, // Auth olmadığı için 401 bekliyoruz
  });

  // Swagger docs testi
  const docsRes = http.get('http://localhost:8000/api/swagger/');
  check(docsRes, {
    'swagger status is 200': (r) => r.status === 200,
  });

  sleep(1);
}
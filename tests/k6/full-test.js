// tests/k6/full-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 },  // 0 -> 10 users
    { duration: '1m', target: 10 },   // 10 users at a constant rate
    { duration: '20s', target: 0 },   // 10 -> 0 users
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests should be less than 500ms
    http_req_failed: ['rate<0.01'],   // Acceptable failure rate is less than 1%
  },
};

export default function () {
  // Metrics endpoint test
  const metricsRes = http.get('http://localhost:8000/metrics/');
  check(metricsRes, {
    'metrics status is 200': (r) => r.status === 200,
    'metrics response time OK': (r) => r.timings.duration < 200,
  });

  // API endpoints test
  const apiRes = http.get('http://localhost:8000/api/v1/locations/');
  check(apiRes, {
    'api status is 401': (r) => r.status === 401, // We expect 401 because we are not authenticated
  });

  // Swagger docs test
  const docsRes = http.get('http://localhost:8000/api/swagger/');
  check(docsRes, {
    'swagger status is 200': (r) => r.status === 200,
  });

  sleep(1);
}

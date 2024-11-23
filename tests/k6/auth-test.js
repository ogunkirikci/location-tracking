// tests/k6/auth-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '30s',
};

const BASE_URL = 'http://web:8000';

// Test senaryosu
export default function () {
  // Metrics endpoint'ini test et
  const metricsRes = http.get(`${BASE_URL}/metrics/`);
  check(metricsRes, {
    'metrics status is 200': (r) => r.status === 200,
  });

  // Token al
  const loginRes = http.post(`${BASE_URL}/api/v1/token/`, JSON.stringify({
    username: 'admin',
    password: 'admin'
  }), {
    headers: { 'Content-Type': 'application/json' }
  });

  check(loginRes, {
    'login status is 200': (r) => r.status === 200,
  });

  if (loginRes.status === 200) {
    const token = loginRes.json('access');
    const params = {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    };

    // Locations endpoint'ini test et
    const locationsRes = http.get(`${BASE_URL}/api/v1/locations/`, params);
    check(locationsRes, {
      'locations status is 200': (r) => r.status === 200,
    });
  }

  sleep(1);
}
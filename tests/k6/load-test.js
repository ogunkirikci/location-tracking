import http from 'k6/http';
import { check, sleep } from 'k6';

const BASE_URL = 'http://web:8000';
let authToken = '';

export const options = {
  stages: [
    { duration: '30s', target: 20 },
    { duration: '1m', target: 20 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export function setup() {
  const loginRes = http.post(`${BASE_URL}/api/v1/token/`, {
    username: 'admin',
    password: 'admin'
  });
  
  return { token: loginRes.json('access') };
}

export default function(data) {
  const params = {
    headers: {
      'Authorization': `Bearer ${data.token}`,
      'Content-Type': 'application/json',
    },
  };

  const getRes = http.get(`${BASE_URL}/api/v1/locations/`, params);
  check(getRes, {
    'get status is 200': (r) => r.status === 200,
  });

  const payload = JSON.stringify({
    latitude: 41.0082 + (Math.random() - 0.5),
    longitude: 28.9784 + (Math.random() - 0.5),
    timestamp: new Date().toISOString()
  });

  const postRes = http.post(`${BASE_URL}/api/v1/locations/`, payload, params);
  check(postRes, {
    'post status is 201': (r) => r.status === 201,
  });

  sleep(1);
}
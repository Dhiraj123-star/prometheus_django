# Django Monitoring with Prometheus & Grafana

A simple Django application integrated with Prometheus for metrics collection and Grafana for real-time monitoring dashboards.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install django django-prometheus requests
```

### 2. Run Django
```bash
python manage.py runserver 0.0.0.0:8000
```

### 3. Start Monitoring Stack
```bash
docker-compose up -d
```

### 4. Access Applications
- **Django App**: http://localhost:8000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)

## 📊 Available Endpoints

- `/` - Home view with basic metrics
- `/user/profile/` - User profile simulation
- `/search/?q=python` - Search API with variable response times
- `/compute/` - CPU intensive operations
- `/upload/` - File upload simulation
- `/analytics/` - Analytics dashboard data
- `/health/` - Health check endpoint
- `/metrics` - Prometheus metrics endpoint

## 🎯 Generate Test Traffic

```bash
python traffic_generator.py
```

Choose from:
1. Test all endpoints once
2. Generate continuous traffic (5 minutes)
3. Generate burst traffic (100 requests)
4. Generate error scenarios

## 📈 Key Metrics Available

### Automatic Django Metrics
- `django_http_requests_total_by_method_total` - Request count by HTTP method
- `django_http_requests_latency_seconds_by_view_method` - Response time by view
- `django_http_responses_total_by_status_total` - Response count by status code

### Custom Business Metrics
- `custom_requests_total` - Custom request counter with view labels
- `custom_response_time_seconds` - Custom response time tracking
- `active_users_count` - Simulated active user count
- `api_errors_total` - API error counter with error types

## 🛠️ Configuration Files

### `docker-compose.yml`
- Prometheus container on port 9090
- Grafana container on port 3000
- Uses `network_mode: host` for local development

### `prometheus.yml`
- Scrapes Django metrics from `localhost:8000/metrics`
- 15-second global scrape interval
- 5-second scrape interval for Django

### Django Settings
- `django_prometheus` added to `INSTALLED_APPS`
- Prometheus middleware configured (Before/After)
- SQLite database with prometheus wrapper

## 📊 Setting Up Grafana

1. **Add Prometheus Data Source**:
   - URL: `http://prometheus:9090`

2. **Create Dashboard Panels**:
   - Request Rate: `rate(custom_requests_total[1m])`
   - Response Time: `custom_response_time_seconds`
   - Error Rate: `api_errors_total`
   - Active Users: `active_users_count`

## 🔧 Development Features

- **Error Simulation**: `/search/?q=error` triggers search errors
- **Variable Processing Time**: Different endpoints have different response times
- **Status Code Variety**: Mix of 200, 400, and 500 responses
- **Custom Labels**: Track metrics by view name, method, and error type

## 📝 Files Overview

- `manage.py` - Django management script
- `db.sqlite3` - SQLite database
- `docker-compose.yml` - Container orchestration
- `prometheus.yml` - Prometheus configuration
- `traffic_generator.py` - Load testing script
- `monitoring_app/views.py` - Custom view functions with metrics
- `monitoring_app/urls.py` - URL routing configuration

This setup provides a complete monitoring solution for understanding Django application performance and behavior in real-time.

# Django Monitoring with Prometheus & Grafana

A simple Django application integrated with Prometheus for metrics collection and Grafana for real-time monitoring dashboards.
Includes **CI/CD with GitHub Actions** for building and publishing Docker images to Docker Hub.

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install django django-prometheus requests
```

### 2. Run Django

```bash
python promethesus_demo/manage.py runserver 0.0.0.0:8000
```

### 3. Start Monitoring Stack

```bash
docker-compose up -d
```

### 4. Access Applications

* **Django App**: [http://localhost:8000](http://localhost:8000)
* **Prometheus**: [http://localhost:9090](http://localhost:9090)
* **Grafana**: [http://localhost:3000](http://localhost:3000) (admin/admin)

---

## 📊 Available Endpoints

* `/` - Home view with basic metrics
* `/user/profile/` - User profile simulation
* `/search/?q=python` - Search API with variable response times
* `/compute/` - CPU intensive operations
* `/upload/` - File upload simulation
* `/analytics/` - Analytics dashboard data
* `/health/` - Health check endpoint
* `/metrics` - Prometheus metrics endpoint

---

## 🎯 Generate Test Traffic

```bash
python traffic_generator.py
```

Options:

1. Test all endpoints once
2. Generate continuous traffic (5 minutes)
3. Generate burst traffic (100 requests)
4. Generate error scenarios

---

## 📈 Key Metrics Available

### Automatic Django Metrics

* `django_http_requests_total_by_method_total`
* `django_http_requests_latency_seconds_by_view_method`
* `django_http_responses_total_by_status_total`

### Custom Business Metrics

* `custom_requests_total`
* `custom_response_time_seconds`
* `active_users_count`
* `api_errors_total`

---

## 🛠️ Configuration Files

### `docker-compose.yml`

* **Django container** on port 8000
* **Prometheus container** on port 9090
* **Grafana container** on port 3000
* Uses `network_mode: host` for local development

### `prometheus.yml`

* Scrapes Django metrics from `localhost:8000/metrics`
* 15-second global scrape interval
* 5-second scrape interval for Django

### Django Settings

* `django_prometheus` in `INSTALLED_APPS`
* Prometheus middleware configured (Before/After)
* SQLite database wrapped with Prometheus

---

## 📊 Setting Up Grafana

1. **Add Prometheus Data Source**:

   * URL: `http://prometheus:9090`

2. **Create Dashboard Panels**:

   * Request Rate → `rate(custom_requests_total[1m])`
   * Response Time → `custom_response_time_seconds`
   * Error Rate → `api_errors_total`
   * Active Users → `active_users_count`

---

## 🔧 Development Features

* Error simulation → `/search/?q=error`
* Variable response times across endpoints
* Mix of 200, 400, 500 responses
* Custom labels for tracking by view, method, error type

---

## ⚙️ CI/CD with GitHub Actions

This project includes a **CI/CD pipeline** to build and publish the Django Docker image to Docker Hub (`dhiraj918106`).

### Workflow Highlights

* Triggers on pushes to `main` branch
* Logs in to Docker Hub using secrets
* Builds Docker image from `Dockerfile`
* Pushes image as `dhiraj918106/django-app:latest`

### Setup Steps

1. Create a **Docker Hub Access Token**
2. Add the following secrets in GitHub repo → `Settings → Secrets and variables → Actions`:

   * `DOCKERHUB_USERNAME` → your Docker Hub username
   * `DOCKERHUB_TOKEN` → access token
3. GitHub Actions will run automatically on every push to `main`

---

✅ This setup gives you:

* A running Django + Prometheus + Grafana monitoring stack
* Real-time dashboards in Grafana
* Automated Docker builds & publishing via GitHub Actions

---

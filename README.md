# 🚀 FastAPI Feature Exploration

Welcome! This repository is a deep dive into the **FastAPI** web framework, featuring practical examples and best practices for building robust, high-performance APIs.

---

## 🌟 Features Covered

- **Request validation** with Pydantic
- **Dependency injection** for modular code
- **Middleware** for request/response processing
- **Async route handling** for concurrency
- **Authentication & Authorization** (OAuth2, JWT)
- **Background tasks** for non-blocking ops
- **WebSockets** for real-time features
- **CORS** for secure cross-origin requests
- **API versioning**
- **External service integration** (DBs, APIs)
- **Custom exception handling**

You’ll also learn to **run locally**, **containerize with Docker**, and **deploy on Kubernetes**.

---

## 🧪 Local Development

1. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Start the server:**
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

4. **API Docs:**
    - [Swagger UI](http://localhost:8000/docs)
    - [ReDoc](http://localhost:8000/redoc)

---

## 🐳 Docker

1. **Build image:**
    ```bash
    docker build -t fastapi-app .
    ```

2. **Run container:**
    ```bash
    docker run -d -p 8000:8000 fastapi-app
    ```

3. **Browse:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ☸️ Kubernetes

1. **Create deployment and service:**  
   Save as `k8s/deployment.yaml`:
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: fastapi-deployment
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: fastapi
      template:
        metadata:
          labels:
            app: fastapi
        spec:
          containers:
            - name: fastapi
              image: fastapi-app:latest
              ports:
                - containerPort: 8000
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: fastapi-service
    spec:
      selector:
        app: fastapi
      ports:
        - protocol: TCP
          port: 80
          targetPort: 8000
      type: LoadBalancer
    ```

2. **Deploy:**
    ```bash
    kubectl apply -f k8s/deployment.yaml
    ```

3. **Access:**
    - Minikube: `minikube service fastapi-service`
    - Or use your cloud provider’s external IP.

---

## 📊 Observability: Logging & Metrics

### ELK Stack (Elasticsearch, Logstash, Kibana)

- **JSON logs** for easy parsing
- **Log shipping** via Filebeat/Fluentd
- **Centralized search** with Elasticsearch
- **Visualization** in Kibana

**Sample Docker Compose:**
```yaml
services:
  fastapi:
    image: fastapi-app:latest
    logging:
      driver: "json-file"
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.12.0
    environment:
      - discovery.type=single-node
    ports:
      - "9200:9200"
  logstash:
    image: docker.elastic.co/logstash/logstash:8.12.0
    ports:
      - "5044:5044"
  kibana:
    image: docker.elastic.co/kibana/kibana:8.12.0
    ports:
      - "5601:5601"
```

### Grafana & Prometheus

- **Metrics** via [prometheus_fastapi_instrumentator](https://github.com/trallard/prometheus-fastapi-instrumentator)
- **Prometheus** scrapes `/metrics`
- **Grafana** dashboards for API performance

**Sample Docker Compose:**
```yaml
services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"
  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
```

**Prometheus Scrape Config:**
```yaml
scrape_configs:
  - job_name: 'fastapi'
    static_configs:
      - targets: ['fastapi:8000']
```

> See the `monitoring/` directory for ready-to-use configs and dashboards.

---

## 🔁 CI/CD with GitHub Actions *(Coming Soon)*

Automated workflow for:

- Linting & formatting
- Test execution
- Docker image build & push
- Kubernetes deployment

---

## 🧪 Pytest Integration *(Coming Soon)*

- **Test files:** in `tests/`, named `test_*.py`
- **Run tests:**
    ```bash
    pytest
    ```
- **Coverage:**
    ```bash
    pytest --cov=app
    ```

Pytest will be part of the CI/CD workflow.

---

**Questions or requests?**  
Let me know if you want to see the actual `.github/workflows/deploy.yml` or Helm chart templates included.


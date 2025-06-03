# fastapi_explore Kubernetes Deployment

This repository contains Kubernetes manifests and a `.env` file setup for deploying the `fastapi_explore` FastAPI application.

---

## Project Structure

.
├── .env
└── k8s/
├── configmap.yaml
├── deployment.yaml
├── ingress.yaml
├── namespace.yaml
├── pvc.yaml
├── secret.yaml
└── service.yaml


---

## Local Development

Create a `.env` file in the project root to store environment variables for local development:

```dotenv
DATABASE_URL=postgres://user:password@hostname:5432/dbname
SECRET_KEY=supersecretkey123
DEBUG=True
API_KEY=someapikeyvalue

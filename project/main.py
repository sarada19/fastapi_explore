import pkgutil
import importlib
from fastapi import FastAPI
from project import apps

app = FastAPI()

for _, module_name, _ in pkgutil.iter_modules(apps.__path__):
    module = importlib.import_module(f"project.apps.{module_name}")
    if hasattr(module, "router"):
        app.include_router(module.router)
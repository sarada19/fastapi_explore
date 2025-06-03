import pkgutil
import importlib
import project.app
from fastapi import FastAPI

app = FastAPI()

for _, module_name, _ in pkgutil.iter_modules(project.app.__path__):
    module = importlib.import_module(f"project.app.{module_name}")
    if hasattr(module, "router"):
        app.include_router(module.router)
import pkgutil
import importlib
from fastapi import FastAPI
from project import app as app_pkg
from project.imports.logging_conf import logger

# Create FastAPI app
app = FastAPI()

# Dynamically include routers from project/app modules
for _, module_name, _ in pkgutil.iter_modules(app_pkg.__path__):
    try:
        module = importlib.import_module(f"project.app.{module_name}")
        if hasattr(module, "router"):
            app.include_router(module.router)
            logger.info("Router are loaded successfully")
        else:
            logger.debug("No router found")
    except Exception as e:
        logger.error(f"Failed to import module: {str(e)}")

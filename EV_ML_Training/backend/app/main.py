from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import sys

from app.config.settings import settings
from app.ml.model_manager import ModelManager
from app.api.routes import health_routes, prediction_routes
from app.middleware.request_logging import RequestLoggingMiddleware
from app.middleware.error_handler import register_exception_handlers
from app.utils.logging_config import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up application and loading models...")
    model_manager = ModelManager()
    try:
        model_manager.load_models()
        app.state.model_manager = model_manager
    except Exception as e:
        logger.error(f"Failed to load models during startup: {e}")
        # We don't want to sys.exit(1) because the requirement says 
        # "Fail clearly during startup or mark the application as not ready."
        # If we exit, tests might fail if they expect the app to start up.
        # We will just mark it as not ready (is_loaded = False)
        app.state.model_manager = model_manager
        
    yield
    # Shutdown
    logger.info("Shutting down application...")
    app.state.model_manager = None

app = FastAPI(
    title=settings.APP_NAME,
    description="Stateless ML inference backend for EV Battery Health Prediction.",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Middlewares
app.add_middleware(RequestLoggingMiddleware)

# Exception Handlers
register_exception_handlers(app)

# Routes
app.include_router(health_routes.router)
app.include_router(prediction_routes.router)

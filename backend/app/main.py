import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.services.prediction_service import prediction_service
from app.core.config import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up – loading ML model...")
    try:
        prediction_service.load()
        logger.info("ML model loaded successfully.")
    except FileNotFoundError as e:
        logger.warning("Model not found: %s", e)
        logger.warning("API will start but predictions will fail until model is trained.")
    yield
    logger.info("Shutting down.")


app = FastAPI(
    title="Crop Disease Detection API",
    description=(
        "Upload a leaf image to detect plant diseases using a MobileNetV2 "
        "transfer-learning model trained on PlantVillage dataset."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")


@app.get("/", tags=["Health"])
async def root():
    return {
        "service": "Crop Disease Detection API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/v1/health",
    }

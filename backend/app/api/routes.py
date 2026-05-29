import logging
from fastapi import APIRouter, File, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse

from app.services.prediction_service import prediction_service, ModelNotLoadedError, InvalidImageError
from app.services.remedy_service import get_disease_info
from app.core.config import settings
from app.models.schemas import PredictionResponse, HealthResponse

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    return HealthResponse(
        status="ok",
        model_loaded=prediction_service.is_loaded,
        message="Model ready for predictions." if prediction_service.is_loaded else "Model not loaded.",
    )


@router.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict_disease(file: UploadFile = File(...)):
    if not prediction_service.is_loaded:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model is not loaded. Please run training first.",
        )

    if file.content_type not in settings.ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsupported file type '{file.content_type}'. Upload a JPEG, PNG, or WebP image.",
        )

    image_bytes = await file.read()

    max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    if len(image_bytes) > max_bytes:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File size exceeds {settings.MAX_UPLOAD_SIZE_MB} MB limit.",
        )

    try:
        result = prediction_service.predict(image_bytes)
    except InvalidImageError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except ModelNotLoadedError as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e))
    except Exception as e:
        logger.exception("Unexpected error during prediction")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Prediction failed.")

    disease_info = get_disease_info(result["class_name"])

    return PredictionResponse(
        success=True,
        class_name=result["class_name"],
        display_name=disease_info["display_name"],
        plant=disease_info["plant"],
        disease=disease_info["disease"],
        confidence=result["confidence"],
        confidence_pct=result["confidence_pct"],
        description=disease_info["description"],
        symptoms=disease_info["symptoms"],
        causes=disease_info["causes"],
        remedies=disease_info["remedies"],
        prevention=disease_info["prevention"],
        severity=disease_info["severity"],
        top5_predictions=result["top5_predictions"],
        filename=file.filename,
    )

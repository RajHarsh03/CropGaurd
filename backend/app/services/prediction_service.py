import json
import logging
import numpy as np
from pathlib import Path
from typing import Optional

import tensorflow as tf
from PIL import Image, UnidentifiedImageError
import io

logger = logging.getLogger(__name__)

MODEL_PATH   = Path(__file__).parent.parent.parent / "trained_model" / "crop_disease_model.keras"
CLASSES_PATH = Path(__file__).parent.parent.parent / "trained_model" / "class_names.json"

IMG_SIZE = 224


class ModelNotLoadedError(RuntimeError):
    pass


class InvalidImageError(ValueError):
    pass


class PredictionService:
    def __init__(self):
        self._model: Optional[tf.keras.Model] = None
        self._class_names: Optional[list[str]] = None

    def load(self) -> None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model file not found at {MODEL_PATH}. "
                "Please run `python ml/train.py` first."
            )
        if not CLASSES_PATH.exists():
            raise FileNotFoundError(
                f"Class names file not found at {CLASSES_PATH}."
            )

        logger.info("Loading model from %s", MODEL_PATH)
        self._model = tf.keras.models.load_model(str(MODEL_PATH))

        with open(CLASSES_PATH) as f:
            self._class_names = json.load(f)

        logger.info("Model loaded. Classes: %s", self._class_names)

    @property
    def is_loaded(self) -> bool:
        return self._model is not None and self._class_names is not None

    def _preprocess(self, image_bytes: bytes) -> np.ndarray:
        try:
            img = Image.open(io.BytesIO(image_bytes))
        except UnidentifiedImageError:
            raise InvalidImageError("Uploaded file is not a valid image.")

        if img.mode != "RGB":
            img = img.convert("RGB")

        img = img.resize((IMG_SIZE, IMG_SIZE), Image.LANCZOS)
        arr = np.array(img, dtype=np.float32) / 255.0
        return np.expand_dims(arr, axis=0)

    def predict(self, image_bytes: bytes) -> dict:
        if not self.is_loaded:
            raise ModelNotLoadedError("Model has not been loaded yet.")

        tensor = self._preprocess(image_bytes)
        preds = self._model.predict(tensor, verbose=0)[0]

        top_idx = int(np.argmax(preds))
        confidence = float(preds[top_idx])

        top5_indices = np.argsort(preds)[::-1][:5]
        top5 = [
            {
                "class_name": self._class_names[i],
                "confidence": float(preds[i]),
                "confidence_pct": round(float(preds[i]) * 100, 2),
            }
            for i in top5_indices
        ]

        return {
            "class_name": self._class_names[top_idx],
            "confidence": confidence,
            "confidence_pct": round(confidence * 100, 2),
            "top5_predictions": top5,
        }


prediction_service = PredictionService()

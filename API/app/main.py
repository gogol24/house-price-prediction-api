# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import joblib
from pathlib import Path
import numpy as np


MODEL_PATH = Path(__file__).parent / "Model_1.joblib"

app = FastAPI(title="API MVP", version="1.0.0")

# ---- Esquema de entrada ----
class Features(BaseModel):
    x: list[float]  # 5 números

    @field_validator("x")
    @classmethod
    def validate_length(cls, v):
        if len(v) != 5:
            raise ValueError("Debes enviar exactamente 5 valores en 'x'.")
        return v

# ---- Cargar el modelo al iniciar ----
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"No pude cargar el modelo en {MODEL_PATH}: {e}")

# ---- Endpoint de salud opcional ----
@app.get("/health")
def health():
    return {"status": "ok"}

# ---- Endpoint de predicción ----
@app.post("/predict")
def predict(feats: Features):
    try:
        arr = np.array(feats.x, dtype=float).reshape(1, -1)  # (1, 5)
        y_pred = model.predict(arr)
        # Convierte a tipos nativos de Python para JSON
        pred_val = float(y_pred[0])
        return {"prediction": pred_val}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al predecir: {e}")

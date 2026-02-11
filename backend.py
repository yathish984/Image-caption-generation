# backend.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional
from io import BytesIO
from PIL import Image
import threading
from transformers import pipeline


app = FastAPI(title="Image Caption Generator")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lazy-loading model
_captioner = None
_captioner_lock = threading.Lock()


def get_captioner():
    """Load captioning model only once (faster startup)."""
    global _captioner
    if _captioner is None:
        with _captioner_lock:
            if _captioner is None:
                print("Loading image-to-text model (this may take time)...")
                _captioner = pipeline(
                    "image-to-text",
                    model="nlpconnect/vit-gpt2-image-captioning"
                )
                print("Model loaded.")
    return _captioner


class CaptionResponse(BaseModel):
    caption: str
    raw: Optional[Dict] = None


@app.post("/caption", response_model=CaptionResponse)
async def caption_image(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        image = Image.open(BytesIO(contents)).convert("RGB")
    except:
        raise HTTPException(400, "Invalid image file")

    captioner = get_captioner()
    results = captioner(image)

    raw = results[0]
    caption_text = (
        raw.get("generated_text")
        or raw.get("caption")
        or str(raw)
    )

    return {"caption": caption_text, "raw": raw}


@app.get("/")
async def root():
    return {"status": "running"}

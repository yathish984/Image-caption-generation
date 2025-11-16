# backend.py
class CaptionResponse(BaseModel):
caption: str
raw: Optional[Dict] = None




@app.post("/caption", response_model=CaptionResponse)
async def caption_image(file: UploadFile = File(...)):
contents = await file.read()
try:
image = Image.open(BytesIO(contents)).convert("RGB")
except Exception:
raise HTTPException(status_code=400, detail="Invalid image file")


try:
captioner = get_captioner()
results = captioner(image)


raw = None
caption_text = None
if isinstance(results, list) and len(results) > 0:
raw = results[0]
caption_text = (
raw.get("generated_text")
or raw.get("caption")
or raw.get("text")
or raw.get("output_text")
)
elif isinstance(results, dict):
raw = results
caption_text = (
results.get("generated_text")
or results.get("caption")
or results.get("text")
)


if not caption_text:
caption_text = str(raw or results)


return {"caption": caption_text, "raw": raw}
except Exception as e:
traceback.print_exc()
raise HTTPException(status_code=500, detail=f"Failed to generate caption: {e}")




@app.get("/")
async def root():
return {"status": "running"}

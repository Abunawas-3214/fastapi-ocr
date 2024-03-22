from fastapi import FastAPI, File, UploadFile
import shutil
import pytesseract

app = FastAPI()

@app.post("/ocr")
def ocri(images: UploadFile = File(...)):
    filePath = 'txtFile'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    with open(filePath, 'w+b') as buffer:
        shutil.copyfileobj(images.file, buffer)
    return pytesseract.image_to_string(filePath, lang='eng')
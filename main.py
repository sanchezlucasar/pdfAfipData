from fastapi import FastAPI, UploadFile, File
from typing import List
from procesApi import extract_invoice_data

app = FastAPI()

@app.post("/process_pdf/")
async def process_invoices(files: List[UploadFile] = File(...)):
    items = []

    for file in files:
        try:
            resultado = extract_invoice_data(file.file)
            items.append({
               "item": resultado
            })
        except Exception as e:
            return {"error": str(e)}

    return items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

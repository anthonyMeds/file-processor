from fastapi import APIRouter, UploadFile, File

from domain.file_processor import FileProcessor

router = APIRouter()

@router.post("/file/create_file")
async def create_file():
    return FileProcessor().create_file()

@router.post('/file/upload_file')
async def upload_file(file: UploadFile = File(...)):
    return await file.read()

@router.post('/file/add_data')
async def add_data(conta: str, agencia: str, texto: str, valor: float):
    data = {"conta": conta, "agencia": agencia, "texto": texto, "valor": valor}

    return

@router.post("/file/delete_data")
async def delete_data():
    return {"message": "Dado deletado com sucesso"}
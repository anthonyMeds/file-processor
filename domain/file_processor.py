import csv
import os

from fastapi import HTTPException, UploadFile, status


class FileProcessor:

    def __init__(self):
        self.file_path = 'data/seu_file.csv'
        self.directory = 'data'

    def create_file(self):
        if not os.path.exists(self.directory):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['conta', 'agencia', 'texto', 'valor'])
                return {"mensagem": f"Arquivo {self.file_path} criado com sucesso."}
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="Arquivo existente")

    async def upload_file(self, file: UploadFile):

        if file.filename.endswith('.csv'):
            try:
                # Decodifica o arquivo para string
                contents = await file.read()
                decoded_file = contents.decode('utf-8').splitlines()

                # Cria o CSV reader a partir do conteúdo decodificado
                csv_reader = csv.DictReader(decoded_file)

                for row in csv_reader:
                    print(row)

                return {"mensagem": f"Arquivo {file.filename} processado com sucesso",
                        "data_read": decoded_file}
            except KeyError as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Erro: coluna {str(e)} não encontrada no CSV"
                )
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Falha ao processar o arquivo CSV: {str(e)}"
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Apenas arquivos CSV são aceitos"
            )

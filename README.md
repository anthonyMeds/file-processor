

    Upload de arquivos: Suporte para o envio de múltiplos tipos de arquivos.
    Manipulação de arquivos: Processamento e gestão de arquivos enviados.
    API RESTful: Exposição de endpoints para interação com o serviço de forma programática.

Tecnologias Utilizadas

    Python: Linguagem de programação utilizada para o desenvolvimento do serviço.
    FastAPI: Framework web utilizado para construir a API do serviço.
    Uvicorn: Servidor ASGI usado para rodar a aplicação FastAPI.
    Pydantic: Utilizado para a validação dos dados das requisições.

Pré-requisitos
    Python 3.x
    Pip para instalação de dependências


## Instalação

Clone o repositório:

Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows

## Instale as dependências:

pip install -r requirements.txt

----


## Como Usar

Inicie o servidor:

uvicorn main:app --reload

    Acesse a documentação swagger da API em http://127.0.0.1:8000/docs. 
    http://localhost:8000/docs - Windows

    Use os endpoints disponíveis para fazer upload e manipular arquivos.

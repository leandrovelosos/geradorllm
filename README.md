# Gerador de codigo baseado em LLM local

LLM hospedada localmente para gerar, executar e validar trechos de código JavaScript com base em prompts.

## Requisitos

- Python 3.8+
- Node.js
- Ollama instalado: https://ollama.com
- Modelo baixado: mistral


## Instalação

1. Instalação do modelo: 
   
```bash
ollama run mistral
```

2. Clone o repositório:
   
```bash
git clone https://github.com/leandrovelosos/geradorllmolama.git
```
3. Crie o ambiente python e instale as dependencias:
   
```bash
python -m venv venv
.\venv\Scripts\activate
pip install requests
```
4. Ative o ambiente virtual:
```bash
   .\venv\Scripts\activate
```   
5. Selecione seu prompt na pasta prompts e execute o arquivo main.py

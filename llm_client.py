# imprta a biblioteca requests para fazer requisições HTTP
import requests

#envia um prompt para um modelo llm local e recebe um codigo gerado
def gerar_codigo(prompt, modelo="mistral", host="http://localhost:11434"):

    #url onde e enviada a requisicao post
    url = f"{host}/api/generate"

    #dados da requisicao 
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.2,
        "num_predict": 100
    }

    try:
        #manada a requisicao para a api com json 
        response = requests.post(url, json=payload)
        response.raise_for_status()

        resposta_texto = response.json().get("response", "")

        #limpeza para remover o que nao e desejado como markdown ```js ou ```javascript
        codigo_limpo = extrair_codigo(resposta_texto)
        return codigo_limpo

    except requests.exceptions.RequestException as e:
        print(f"Erro ao se comunicar com a LLM: {e}")
        return ""

#remove as marcacoes de bloco do codigo markdown e outras
def extrair_codigo(resposta):

    linhas = resposta.strip().splitlines()


    if linhas and linhas[0].startswith("```"):
        linhas = linhas[1:]
    if linhas and linhas[-1].startswith("```"):
        linhas = linhas[:-1]
    #junta as linhas restantes em uma string e remove os espacos
    return "\n".join(linhas).strip()



if __name__ == "__main__":
    prompt = "Escreva uma função JavaScript que imprime 'Hello, World!' no console."
    codigo = gerar_codigo(prompt)
    print("Código JS gerado:\n")
    print(codigo)

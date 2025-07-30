import requests

def gerar_codigo(prompt, modelo="mistral", host="http://localhost:11434"):

    url = f"{host}/api/generate"
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.2,
        "num_predict": 100
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        resposta_texto = response.json().get("response", "")

        # Limpeza básica: remove markdown ```js ou ```javascript
        codigo_limpo = extrair_codigo(resposta_texto)
        return codigo_limpo

    except requests.exceptions.RequestException as e:
        print(f"Erro ao se comunicar com a LLM: {e}")
        return ""


def extrair_codigo(resposta):

    linhas = resposta.strip().splitlines()


    if linhas and linhas[0].startswith("```"):
        linhas = linhas[1:]
    if linhas and linhas[-1].startswith("```"):
        linhas = linhas[:-1]

    return "\n".join(linhas).strip()



if __name__ == "__main__":
    prompt = "Escreva uma função JavaScript que imprime 'Hello, World!' no console."
    codigo = gerar_codigo(prompt)
    print("Código JS gerado:\n")
    print(codigo)

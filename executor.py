import subprocess
from pathlib import Path

def salvar_codigo(codigo: str, caminho_arquivo: str = "generated_code/code.js"):
   
    Path(caminho_arquivo).parent.mkdir(parents=True, exist_ok=True)
    Path(caminho_arquivo).write_text(codigo)
    print(f"Código salvo em: {caminho_arquivo}")


def executar_js(caminho_arquivo: str = "generated_code/code.js"):

    try:
        resultado = subprocess.run(
            ["node", caminho_arquivo],
            capture_output=True,
            text=True,
            timeout=5
        )
        return resultado.stdout.strip(), resultado.stderr.strip()

    except subprocess.TimeoutExpired:
        return "", "Erro: Execução excedeu o tempo limite."
    except FileNotFoundError:
        return "", "Erro: Node.js não encontrado. Verifique a instalação."



if __name__ == "__main__":
    codigo_teste = """
    function hello() {
        console.log("Hello, World!");
    }
    hello();
    """
    salvar_codigo(codigo_teste)
    saida, erro = executar_js()

    if erro:
        print("Erro:\n", erro)
    else:
        print("Saída:\n", saida)

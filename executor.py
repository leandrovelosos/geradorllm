#importaçoes 
import subprocess #executa comandos no s.o
from pathlib import Path #path para manipulacao de arquivos e diretorios de forma simples

def salvar_codigo(codigo: str, caminho_arquivo: str = "generated_code/code.js"):
    #cria os diretorios
    Path(caminho_arquivo).parent.mkdir(parents=True, exist_ok=True)
    #escrve o codigon no arquivo
    Path(caminho_arquivo).write_text(codigo)
    #mostra onde o codigo foi salvo
    print(f"Código salvo em: {caminho_arquivo}")


def executar_js(caminho_arquivo: str = "generated_code/code.js"):
    #roda o arquivo js usando node
    try:
        resultado = subprocess.run(
            ["node", caminho_arquivo], #executa o node
            capture_output=True, #captura a saida padrao e erro
            text=True, #retorna a saida como string
            timeout=5 #timeout de execucao de 5 segundos
        )
        #retorna a saida e o erro 
        return resultado.stdout.strip(), resultado.stderr.strip()

    except subprocess.TimeoutExpired:
        return "", "Erro: Execução excedeu o tempo limite."
    #se o nodejs nao estiver instalado retorna esta mensagem
    except FileNotFoundError:
        return "", "Erro: Node.js não encontrado. Verifique a instalação."


#exemplo de codigo js para ser salvo

if __name__ == "__main__":
    codigo_teste = """
    function hello() {
        console.log("Hello, World!");
    }
    hello();
    """
    #salva o codigo no arquivo criado
    salvar_codigo(codigo_teste)
    #executa o arquivo js e captura a saida
    saida, erro = executar_js()

    #verifica se existe erro e mostra no console
    if erro:
        print("Erro:\n", erro)
    else:
        print("Saída:\n", saida)

from llm_client import gerar_codigo
from executor import salvar_codigo, executar_js
from validator import validar_saida, exibir_resultado
import re

#prompt pode ser escrito direto na variavel ou usar algum existente na pasta prompts
PROMPT_PATH = "prompts/hello_world.txt"

with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    prompt_text = f.read()

#vai verificar o tipo de saida 
prompt_lower = prompt_text.lower()

#verifica se o prompt envolve booleanos
if any(word in prompt_lower for word in ["true", "false", "boolean", "bool"]):
    SAIDA_ESPERADA = bool
#verifica se o prompt envolve números
elif re.search(r"-?\d+", prompt_text):
    SAIDA_ESPERADA = int
elif "hello, world!" in prompt_lower:
    SAIDA_ESPERADA = "Hello, World!"
else:
    SAIDA_ESPERADA = int


def main():
    print("Enviando prompt para a LLM...")
    codigo = gerar_codigo(prompt_text)

    if not codigo:
        print("Nenhum código foi gerado. Encerrando.")
        return

    print("\n Código gerado:\n" + "-" * 40)
    print(codigo)
    print("-" * 40)

    salvar_codigo(codigo)

    print("\n Executando o código...")
    saida, erro = executar_js()

    if erro:
        print("Erro durante a execução:\n", erro)
    else:
        print("Código executado com sucesso!\n")
        exibir_resultado(SAIDA_ESPERADA, saida)


if __name__ == "__main__":
    main()

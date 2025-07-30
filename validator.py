import re

def validar_saida(saida_esperada, saida_obtida: str) -> bool:
    saida_obtida = saida_obtida.strip().lower()

    if saida_esperada == int:
        # Verifica se há pelo menos um número na saída
        return re.search(r"-?\d+", saida_obtida) is not None

    elif saida_esperada == bool:
        # Verifica se a saída é 'true' ou 'false' (pode ser múltiplas linhas)
        linhas = [linha.strip() for linha in saida_obtida.splitlines()]
        return len(linhas) > 0 and all(linha in ("true", "false") for linha in linhas)
    
    elif isinstance(saida_esperada, str):
        return saida_obtida == saida_esperada.lower().strip()
    
    else:
        return False


def exibir_resultado(saida_esperada, saida_obtida: str):
    print("Saída esperada:", repr(saida_esperada))
    print("Saída obtida:", repr(saida_obtida.strip()))

    if validar_saida(saida_esperada, saida_obtida):
        print("Resultado: Código válido!")
    else:
        print("Resultado: Código não produziu a saída esperada.")

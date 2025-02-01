from operations.soma import soma

def multiplicacao(a, b):
    """Retorna a multiplicação de dois números usando soma."""
    if b == 0 or a == 0:
        return 0
    if b < 0:
        return -multiplicacao(a, -b)
    return soma(a, multiplicacao(a, b - 1))

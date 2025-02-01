def fatorial(n):
    """Calcula o fatorial de um número n usando soma e subtração."""
    if n == 0 or n == 1:
        return 1  # 0! = 1! = 1

    # Multiplicação recursiva para calcular o fatorial
    def multiplicacao(a, b):
        if b == 0:
            return 0
        if b < 0:
            return -multiplicacao(a, -b)
        return a + multiplicacao(a, b - 1)

    return multiplicacao(n, fatorial(n - 1))

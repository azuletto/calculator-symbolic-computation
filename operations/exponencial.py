def exponencial(base, expoente):
    """Calcula base^expoente usando apenas soma e subtração."""
    if expoente == 0:
        return 1  # Qualquer número elevado a 0 é 1
    if expoente == 1:
        return base  # Qualquer número elevado a 1 é ele mesmo

    # Multiplicação da base por ela mesma (base * base^(expoente-1))
    def multiplicacao(a, b):
        if b == 0:
            return 0
        if b < 0:
            return -multiplicacao(a, -b)
        return a + multiplicacao(a, b - 1)

    return multiplicacao(base, exponencial(base, expoente - 1))

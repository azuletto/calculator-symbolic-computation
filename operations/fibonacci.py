def fibonacci(n, memo={}):
    """Calcula o n-ésimo número da sequência de Fibonacci usando hash para memoização."""
    if n in memo:  # Retorna o valor memoizado se já calculado
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Soma recursiva com memoização
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

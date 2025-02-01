from tkinter import messagebox
from operations.soma import soma
from operations.subtracao import subtracao

def divisao(a, b):
    """Retorna a parte inteira e o resto da divisão de dois números."""
    if b == 0:
        messagebox.showerror("A resposta da Vida, Universo e tudo que há de mais é 42", "A divisão por zero pode causar o colapso do universo!")
        return None, None
    if a < 0 and b > 0:
        quociente, resto = divisao(-a, b)
        return -quociente, -resto if resto != 0 else resto
    if a > 0 and b < 0:
        quociente, resto = divisao(a, -b)
        return -quociente, resto
    if a < 0 and b < 0:
        quociente, resto = divisao(-a, -b)
        return quociente, resto
    if a < b:
        return 0, a
    quociente, resto = divisao(subtracao(a, b), b)
    return soma(1, quociente), resto

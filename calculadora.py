import tkinter as tk
from operations.soma import soma
from operations.subtracao import subtracao
from operations.multiplicacao import multiplicacao
from operations.divisao import divisao
from operations.exponencial import exponencial
from operations.fatorial import fatorial
from operations.fibonacci import fibonacci

def handle_operation(operation):

    try:
        num1 = float(entry_num1.get())
        if operation in {fatorial, fibonacci}:  # Operações que utilizam um único número
            result = operation(int(num1))
        else:
            num2 = float(entry_num2.get())
            result = operation(num1, int(num2))  # Inteiro para o expoente em exponencial
        result_display.config(state="normal")
        result_display.delete(1.0, "end")
        result_display.insert("end", f"{result}")
        result_display.config(state="disabled")
    except ValueError:
        result_display.config(state="normal")
        result_display.delete(1.0, "end")
        result_display.insert("end", "Insira números válidos.")
        result_display.config(state="disabled")
        
# Configuração da janela
root = tk.Tk()
root.title("Calculadora Elegante")
root.geometry("700x400")
root.configure(bg="#1e1e2e")

# Configuração de estilo
font_title = ("Arial", 18, "bold")
font_label = ("Arial", 12)
font_button = ("Arial", 12, "bold")
font_result = ("Arial", 14)


# Entrada para números
frame_inputs = tk.Frame(root, bg="#1e1e2e")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Número 1:", font=font_label, bg="#1e1e2e", fg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(frame_inputs, font=font_label, width=15)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Número 2:", font=font_label, bg="#1e1e2e", fg="#ffffff").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(frame_inputs, font=font_label, width=15)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Botões das operações
frame_buttons = tk.Frame(root, bg="#1e1e2e")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Soma", font=font_button, bg="#4CAF50", fg="#ffffff",
          command=lambda: handle_operation(soma)).grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame_buttons, text="Subtração", font=font_button, bg="#f44336", fg="#ffffff",
          command=lambda: handle_operation(subtracao)).grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_buttons, text="Multiplicação", font=font_button, bg="#2196F3", fg="#ffffff",
          command=lambda: handle_operation(multiplicacao)).grid(row=0, column=2, padx=10, pady=10)
tk.Button(frame_buttons, text="Divisão", font=font_button, bg="#FF9800", fg="#ffffff",
          command=lambda: handle_operation(divisao)).grid(row=0, column=3, padx=10, pady=10)
tk.Button(frame_buttons, text="Expoente", font=font_button, bg="#9C27B0", fg="#ffffff",
          command=lambda: handle_operation(exponencial)).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
tk.Button(frame_buttons, text="Fatorial", font=font_button, bg="#673AB7", fg="#ffffff",
          command=lambda: handle_operation(fatorial)).grid(row=1, column=1, columnspan=2, padx=10, pady=10)
tk.Button(frame_buttons, text="Fibonacci", font=font_button, bg="#E4727B", fg="#ffffff",
          command=lambda: handle_operation(fibonacci)).grid(row=1, column=2, columnspan=2, padx=10, pady=10)



# Exibição do resultado
tk.Label(root, text="Resultado:", font=font_label, bg="#1e1e2e", fg="#ffffff").pack(pady=10)
#mostre o resultado centralizado
result_display = tk.Text(root, height=1, width=20, font=font_result, bg="#ffffff", fg="#000000", state="disabled")

result_display.pack(pady=10)
result_display.insert("end", "Digite os números e escolha a operação.")
result_display.config(state="disabled")

# Loop principal
root.mainloop()

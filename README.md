# Calculator Symbolic Computation

A recursive calculator implemented in Python that performs mathematical operations using only **addition (+) and subtraction (-)**. This project is part of a Numerical Calculation assignment and supports basic arithmetic, exponentiation, factorial, and Fibonacci sequence calculation.

## 📌 Features

✅ Addition, Subtraction, Multiplication, and Division (Integer-based)  
✅ Exponentiation using recursion  
✅ Factorial computation  
✅ Fibonacci sequence with memoization optimization  
✅ Graphical User Interface (GUI) with Tkinter  

## 🛠️ Installation

Ensure you have Python installed (>= 3.8). Clone this repository and install dependencies:

```sh
# Clone the repository
git clone https://github.com/azuletto/calculator-symbolic-computation.git
cd calculator-symbolic-computation

# Run the application
python calculadora.py
```

## 📚 How It Works

### 🔢 Arithmetic Operations (Recursive)
- **Addition & Subtraction**: Directly implemented.
- **Multiplication**: Uses repeated addition.
- **Division**: Uses repeated subtraction, returning both quotient and remainder.
- **Exponentiation**: Uses recursive multiplication.
- **Factorial**: Uses recursive multiplication.
- **Fibonacci**: Uses recursion with memoization for efficiency.

### 🏗️ Project Structure

```
calculator-symbolic-computation/
│── operations/
│   ├── soma.py        # Addition
│   ├── subtracao.py   # Subtraction
│   ├── multiplicacao.py # Multiplication using recursion
│   ├── divisao.py     # Integer division using subtraction
│   ├── exponencial.py # Exponentiation using recursive multiplication
│   ├── fatorial.py    # Factorial using recursion
│   ├── fibonacci.py   # Fibonacci with memoization
│── calculadora.py      # GUI implementation with Tkinter
│── README.md          # Documentation
```

## 🖥️ Running the GUI

To run the graphical interface, execute:

```sh
python calculadora.py
```

### 📌 GUI Features
- User-friendly interface with input fields and buttons for each operation.
- Displays results dynamically in a text box.
- Prevents division by zero with error handling.

## 📜 License

This project is licensed under the MIT License. Feel free to contribute or modify.

---

**Author:** [azuletto](https://github.com/azuletto)

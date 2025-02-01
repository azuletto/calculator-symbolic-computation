# 📊 Calculator Symbolic Computation

A recursive calculator that performs mathematical operations **using only addition (+) and subtraction (-)**. This project explores **numerical computation principles**, recursion, and algorithmic efficiency.

---

## 🔍 Overview

This calculator supports basic and advanced arithmetic operations, ensuring that **all calculations are derived exclusively from addition and subtraction**. The project serves as an exercise in recursion, numerical decomposition, and **computational thinking**.

### 📌 Supported Operations:
| Operation       | Implementation Method |
|----------------|----------------------|
| **Addition (+)**  | Direct summation |
| **Subtraction (-)** | Direct subtraction |
| **Multiplication (×)** | Repeated addition |
| **Division (÷)** | Repeated subtraction (quotient & remainder) |
| **Exponentiation (xʸ)** | Recursive multiplication |
| **Factorial (n!)** | Recursive multiplication |
| **Fibonacci (Fₙ)** | Recursive sequence with memoization |

---

## 📖 Methodology & Examples

### ➕ Addition  
**Formula:** `a + b`  
Implemented directly with Python's `+` operator.  

**Example:**  
```
soma(4, 3) → 4 + 3 = 7
```

### ➖ Subtraction  
**Formula:** `a - b`  
Implemented directly with Python's `-` operator.  

**Example:**  
```
subtracao(9, 5) → 9 - 5 = 4
```

### ✖ Multiplication  
**Formula:** `a × b = a + a + ... + a (b times)`  
Implemented recursively using repeated addition.  

**Example:**  
```
multiplicacao(3, 4) → 3 + 3 + 3 + 3 = 12
```

### ➗ Division  
**Formula:** `a ÷ b = how many times b fits in a`  
Implemented by recursively subtracting `b` from `a` until `a < b`.  

**Example:**  
```
divisao(10, 3) → (Quotient: 3, Remainder: 1)
```

### 📈 Exponentiation  
**Formula:** `xʸ = x × x × ... × x (y times)`  
Implemented recursively using multiplication.  

**Example:**  
```
exponencial(2, 3) → 2 × 2 × 2 = 8
```

### 🧮 Factorial  
**Formula:** `n! = n × (n-1) × (n-2) ... × 1`  
Implemented recursively using multiplication.  

**Example:**  
```
fatorial(5) → 5 × 4 × 3 × 2 × 1 = 120
```

### 🔢 Fibonacci Sequence  
**Formula:** `Fₙ = Fₙ₋₁ + Fₙ₋₂`  
Optimized with memoization for efficiency.  

**Example:**  
```
fibonacci(6) → 8 (Sequence: 0, 1, 1, 2, 3, 5, 8)
```

---

## 🚀 Installation & Usage

1. Clone the repository:
```sh
git clone https://github.com/azuletto/calculator-symbolic-computation.git
cd calculator-symbolic-computation
```

2. Run the graphical interface (GUI):
```sh
python calculadora.py
```

---

## 🎨 GUI Overview

The calculator features a **Tkinter-based graphical interface**, allowing users to perform operations interactively.  

✅ **Intuitive UI with input fields and buttons**  
✅ **Error handling (e.g., division by zero warnings)**  
✅ **Live result display**  

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

**Author:** [azuletto](https://github.com/azuletto) 🚀

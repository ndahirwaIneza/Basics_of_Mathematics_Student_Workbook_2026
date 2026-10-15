# Exercise 1

**Problem:** Write the system
$$\begin{cases}2x-y+z=4,\\x+3y-2z=1,\\3x+y+z=7.\end{cases}$$
in the form $Ax=b$.
Identify the coefficient matrix, the vector of unknowns, and the right-hand side vector. Explain how each row of the matrix corresponds to one equation.

---

## Relevant theorem / definition

A linear system of $m$ equations in $n$ unknowns can be represented compactly as a single matrix equation:
$$
A\mathbf{x} = \mathbf{b}
$$
where $A \in \mathbb{R}^{m \times n}$ is the coefficient matrix, $\mathbf{x} \in \mathbb{R}^n$ is the column vector of unknowns, and $\mathbf{b} \in \mathbb{R}^m$ is the right-hand side vector.

---

## Solution

The given system of linear equations is:
$$
\begin{cases}
2x - y + z = 4 \\
x + 3y - 2z = 1 \\
3x + y + z = 7
\end{cases}
$$

1. Matrix form $Ax = b$:
   $$
   \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}
   $$

2. Identification of components:
   - Coefficient matrix $A$:
     $$
     A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix}
     $$
   - Vector of unknowns $\mathbf{x}$:
     $$
     \mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}
     $$
   - Right-hand side vector $\mathbf{b}$:
     $$
     \mathbf{b} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}
     $$

3. Explanation of row-equation correspondence:
   By the definition of matrix multiplication, the $i$-th entry of the product $A\mathbf{x}$ is computed by taking the dot product of the $i$-th row of $A$ with the vector of unknowns $\mathbf{x}$:
   - Row 1: $\begin{pmatrix} 2 & -1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 2x - y + z = 4$ (Equation 1)
   - Row 2: $\begin{pmatrix} 1 & 3 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = x + 3y - 2z = 1$ (Equation 2)
   - Row 3: $\begin{pmatrix} 3 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 3x + y + z = 7$ (Equation 3)
   Thus, row $i$ contains precisely the ordered coefficients of the variables in the $i$-th equation, and setting its dot product with $\mathbf{x}$ equal to the $i$-th entry of $\mathbf{b}$ reproduces the $i$-th equation.

---

## Result

$$
A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix}, \qquad \mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}, \qquad \mathbf{b} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}
$$

$$
\begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the matrix-vector product $A\mathbf{x}$:
$$
A\mathbf{x} = \begin{pmatrix} 2x + (-1)y + 1z \\ 1x + 3y + (-2)z \\ 3x + 1y + 1z \end{pmatrix} = \begin{pmatrix} 2x - y + z \\ x + 3y - 2z \\ 3x + y + z \end{pmatrix}
$$
Equating this to $\mathbf{b} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}$ yields the three original equations.

**Pass 2 — Numerical check:** Substitute test point $(x, y, z) = (1, 1, 3)$:
$A \begin{pmatrix} 1 \\ 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 2(1)-1+3 \\ 1+3(1)-2(3) \\ 3(1)+1+3 \end{pmatrix} = \begin{pmatrix} 4 \\ -2 \\ 7 \end{pmatrix}$. Rows 1 and 3 match entries $b_1 = 4, b_3 = 7$.

**Pass 3 — Consistency check:** Dimension check: $A$ is $3 \times 3$, $\mathbf{x}$ is $3 \times 1$, $\mathbf{b}$ is $3 \times 1$. The dimensions $(3 \times 3)(3 \times 1) = 3 \times 1$ are compatible.

---

## Exam tip

Ensure variables are aligned in identical order ($x, y, z$) in every equation before writing down the coefficient matrix to avoid placing coefficients into the wrong columns.


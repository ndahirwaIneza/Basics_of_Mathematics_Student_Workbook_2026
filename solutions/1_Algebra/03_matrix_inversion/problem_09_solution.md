# Exercise 9

**Problem:** Given
$$A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}3&1\\2&4\end{pmatrix}.$$
Solve the equation $AX=B$ for $X$. Before calculating, decide on which side of the equation $A^{-1}$ must be used. Then check the result by computing $AX$.

---

## Relevant theorem / definition

For an invertible matrix $A$, to isolate $X$ in the equation $AX = B$, multiply both sides from the left by $A^{-1}$:
$$
A^{-1}(AX) = A^{-1}B \implies (A^{-1}A)X = A^{-1}B \implies IX = A^{-1}B \implies X = A^{-1}B
$$
Because matrix multiplication is non-commutative, multiplying from the right would give $AXA^{-1} = BA^{-1}$, which does not isolate $X$.

---

## Solution

The given matrices are:
$$
A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}
$$

1. Deciding which side to multiply by $A^{-1}$:
   In the expression $AX$, the matrix $A$ appears to the left of the unknown matrix $X$. Therefore, to eliminate $A$ using the property $A^{-1}A = I$, we must multiply the equation from the left by $A^{-1}$:
   $$
   X = A^{-1}B
   $$

2. Compute $A^{-1}$:
   Since $\det(A) = 1(1) - 2(0) = 1 \neq 0$, $A$ is invertible:
   $$
   A^{-1} = \frac{1}{1} \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}
   $$

3. Calculate $X = A^{-1}B$:
   $$
   \begin{align}
   X &= \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} \\
   &= \begin{pmatrix} 1(3) + (-2)(2) & 1(1) + (-2)(4) \\ 0(3) + 1(2) & 0(1) + 1(4) \end{pmatrix} \\
   &= \begin{pmatrix} 3 - 4 & 1 - 8 \\ 0 + 2 & 0 + 4 \end{pmatrix} \\
   &= \begin{pmatrix} -1 & -7 \\ 2 & 4 \end{pmatrix}
   \end{align}
   $$

4. Check by computing $AX$:
   $$
   \begin{align}
   AX &= \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -1 & -7 \\ 2 & 4 \end{pmatrix} \\
   &= \begin{pmatrix} 1(-1) + 2(2) & 1(-7) + 2(4) \\ 0(-1) + 1(2) & 0(-7) + 1(4) \end{pmatrix} \\
   &= \begin{pmatrix} -1 + 4 & -7 + 8 \\ 0 + 2 & 0 + 4 \end{pmatrix} \\
   &= \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} = B
   \end{align}
   $$
   The product $AX$ equals $B$, confirming the solution.

---

## Result

$$
X = \begin{pmatrix} -1 & -7 \\ 2 & 4 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Check row by row:
Row 2 of $AX$ is $0 \cdot \text{row}_1(X) + 1 \cdot \text{row}_2(X) = \text{row}_2(X)$. Since row 2 of $B$ is $\begin{pmatrix} 2 & 4 \end{pmatrix}$, row 2 of $X$ must be $\begin{pmatrix} 2 & 4 \end{pmatrix}$.
Row 1 of $AX$ is $\text{row}_1(X) + 2 \cdot \text{row}_2(X) = \begin{pmatrix} 3 & 1 \end{pmatrix} \implies \text{row}_1(X) = \begin{pmatrix} 3 & 1 \end{pmatrix} - 2\begin{pmatrix} 2 & 4 \end{pmatrix} = \begin{pmatrix} -1 & -7 \end{pmatrix}$.
Both rows match.

**Pass 2 — Numerical check:** Determinants: $\det(A) = 1$, $\det(B) = 3(4) - 1(2) = 10$.
$\det(X) = (-1)(4) - (-7)(2) = -4 + 14 = 10$.
Matches $\det(X) = \frac{\det B}{\det A} = \frac{10}{1} = 10$.

**Pass 3 — Consistency check:** If we had incorrectly multiplied on the right ($B A^{-1}$):
$$
B A^{-1} = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}\begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 3 & -5 \\ 2 & 0 \end{pmatrix}
$$
Then $A(B A^{-1}) = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 3 & -5 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 7 & -5 \\ 2 & 0 \end{pmatrix} \neq B$, proving right-multiplication fails.

---

## Exam tip

For $AX = B$, solve $X = A^{-1}B$ (left multiplication); for $XA = B$, solve $X = B A^{-1}$ (right multiplication).


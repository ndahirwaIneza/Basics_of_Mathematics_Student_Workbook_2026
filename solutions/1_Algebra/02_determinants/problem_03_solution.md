# Exercise 3

**Problem:** For
$$A=\begin{pmatrix}1&2&0\\0&3&1\\2&1&1\end{pmatrix}$$
compute $\det A$. Then form a matrix $B$ by swapping the first and second rows of $A$.

First predict $\det B$ using a determinant property, and then verify your prediction by calculation.

---

## Relevant theorem / definition

Interchanging any two rows (or two columns) of an $n \times n$ matrix reverses the sign of its determinant:
$$
\det(B) = -\det(A)
$$

---

## Solution

1. Computation of $\det A$:
   Expand along Row 1:
   $$
   \begin{align}
   \det A &= 1 \cdot \begin{vmatrix} 3 & 1 \\ 1 & 1 \end{vmatrix} - 2 \cdot \begin{vmatrix} 0 & 1 \\ 2 & 1 \end{vmatrix} + 0 \cdot \begin{vmatrix} 0 & 3 \\ 2 & 1 \end{vmatrix} \\
   &= 1(3 \cdot 1 - 1 \cdot 1) - 2(0 \cdot 1 - 1 \cdot 2) + 0 \\
   &= 1(3 - 1) - 2(0 - 2) \\
   &= 2 - (-4) = 2 + 4 = 6
   \end{align}
   $$

2. Prediction for $\det B$:
   Matrix $B$ is obtained from $A$ by swapping Row 1 and Row 2 ($R_1 \leftrightarrow R_2$). By the row interchange property:
   $$
   \det B = -\det A = -6
   $$

3. Verification by direct calculation:
   The matrix $B$ is:
   $$
   B = \begin{pmatrix} 0 & 3 & 1 \\ 1 & 2 & 0 \\ 2 & 1 & 1 \end{pmatrix}
   $$
   Expand along Row 1:
   $$
   \begin{align}
   \det B &= 0 \cdot \begin{vmatrix} 2 & 0 \\ 1 & 1 \end{vmatrix} - 3 \cdot \begin{vmatrix} 1 & 0 \\ 2 & 1 \end{vmatrix} + 1 \cdot \begin{vmatrix} 1 & 2 \\ 2 & 1 \end{vmatrix} \\
   &= 0 - 3(1 \cdot 1 - 0 \cdot 2) + 1(1 \cdot 1 - 2 \cdot 2) \\
   &= -3(1 - 0) + 1(1 - 4) \\
   &= -3 - 3 = -6
   \end{align}
   $$

The calculated value $\det B = -6$ confirms the theoretical prediction.

---

## Result

$$
\det A = 6
$$

$$
\det B = -\det A = -6
$$

---

## Verification

**Pass 1 — Algebraic check:** Row swap represents left multiplication by elementary permutation matrix $P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$. Since $\det(P) = -1$, $\det(B) = \det(PA) = \det(P)\det(A) = (-1)(6) = -6$.

**Pass 2 — Numerical check:** Sarrus' rule for $B$: $(0 \cdot 2 \cdot 1 + 3 \cdot 0 \cdot 2 + 1 \cdot 1 \cdot 1) - (1 \cdot 2 \cdot 2 + 0 \cdot 0 \cdot 1 + 3 \cdot 1 \cdot 1) = (0 + 0 + 1) - (4 + 0 + 3) = 1 - 7 = -6$.

**Pass 3 — Consistency check:** Since $A$ and $B$ have identical rows in different positions, their row spaces are identical and both are non-singular with $|\det A| = |\det B| = 6$.

---

## Exam tip

Each single row swap multiplies the determinant by $-1$; an even number of row swaps preserves the determinant's sign.


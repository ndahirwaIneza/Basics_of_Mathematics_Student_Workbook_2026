# Exercise 3

**Problem:** For
$$A=\begin{pmatrix}2&4\\1&2\end{pmatrix}$$
explain in two ways why $A^{-1}$ does not exist: using the determinant and using dependence between the rows.

---

## Relevant theorem / definition

For a square matrix $A \in \mathbb{R}^{n \times n}$, the following statements are equivalent (Invertible Matrix Theorem):
1. $A$ is invertible ($A^{-1}$ exists).
2. $\det(A) \neq 0$.
3. The rows (and columns) of $A$ are linearly independent ($\text{rank}(A) = n$).

---

## Solution

The given matrix is:
$$
A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}
$$

1. Explanation using the determinant:
   Calculate the determinant of $A$:
   $$
   \det(A) = 2(2) - 4(1) = 4 - 4 = 0
   $$
   By the Invertible Matrix Theorem, a square matrix is invertible if and only if its determinant is non-zero. If an inverse $A^{-1}$ existed, the product rule would require $\det(A) \det(A^{-1}) = \det(I) = 1$, which would imply $0 \cdot \det(A^{-1}) = 1$, an impossible contradiction. Therefore, because $\det(A) = 0$, $A^{-1}$ does not exist.

2. Explanation using dependence between the rows:
   Let the rows of $A$ be:
   $$
   R_1 = \begin{pmatrix} 2 & 4 \end{pmatrix}, \qquad R_2 = \begin{pmatrix} 1 & 2 \end{pmatrix}
   $$
   Comparing the two rows:
   $$
   R_1 = 2 \cdot R_2
   $$
   Row 1 is a non-trivial scalar multiple of Row 2, which means the rows are linearly dependent. Linear dependence among the rows reduces the row rank of $A$ to $\text{rank}(A) = 1$, which is strictly less than the dimension $n = 2$. As a linear transformation, $A$ collapses the 2D plane onto the 1D line $y = \frac{1}{2}x$. This collapse destroys information (all vectors along the line $x_1 + 2x_2 = 0$ map to the zero vector $\mathbf{0}$), making the mapping non-injective. Because the transformation cannot be uniquely reversed, no inverse matrix $A^{-1}$ exists.

---

## Result

$$
\det(A) = 0 \implies A^{-1} \text{ does not exist}
$$

$$
R_1 = 2R_2 \implies \text{rows are linearly dependent} \implies \text{rank}(A) = 1 < 2 \implies A^{-1} \text{ does not exist}
$$

---

## Verification

**Pass 1 — Algebraic check:** Null space check: solve $A\mathbf{x} = \mathbf{0}$:
$$
\begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies x_1 + 2x_2 = 0 \implies \mathbf{x} = t \begin{pmatrix} -2 \\ 1 \end{pmatrix}
$$
The non-trivial kernel vector $\begin{pmatrix} -2 \\ 1 \end{pmatrix} \neq \mathbf{0}$ maps to $\mathbf{0}$, algebraically proving non-invertibility.

**Pass 2 — Numerical check:** Attempt to apply the $2 \times 2$ formula: $A^{-1} = \frac{1}{0}\begin{pmatrix} 2 & -4 \\ -1 & 2 \end{pmatrix}$, which requires division by zero and is undefined.

**Pass 3 — Consistency check:** Gaussian elimination gives:
$$
\left[\begin{array}{cc} 2 & 4 \\ 1 & 2 \end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - \frac{1}{2}R_1} \left[\begin{array}{cc} 2 & 4 \\ 0 & 0 \end{array}\right]
$$
The echelon form contains an entire row of zeros, confirming rank 1 and lack of invertibility.

---

## Exam tip

A zero determinant and linearly dependent rows are two sides of the same coin: both immediately signal that the matrix has no inverse.


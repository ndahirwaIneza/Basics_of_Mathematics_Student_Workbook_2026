# Exercise 1

**Problem:** For
$$A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad B=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$$
check, without using a formula, whether $B=A^{-1}$. Compute $AB$ and $BA$ and relate the result to the definition of the inverse.

---

## Relevant theorem / definition

Let $A$ be a square matrix of size $n \times n$. A matrix $B$ is the inverse of $A$ (denoted $A^{-1}$) if and only if:
$$
AB = BA = I_n
$$
where $I_n$ is the $n \times n$ identity matrix.

---

## Solution

1. Computation of $AB$:
   $$
   AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(-1) & 2(-1) + 1(2) \\ 1(1) + 1(-1) & 1(-1) + 1(2) \end{pmatrix} = \begin{pmatrix} 2-1 & -2+2 \\ 1-1 & -1+2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
   $$

2. Computation of $BA$:
   $$
   BA = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1(2) + (-1)(1) & 1(1) + (-1)(1) \\ -1(2) + 2(1) & -1(1) + 2(1) \end{pmatrix} = \begin{pmatrix} 2-1 & 1-1 \\ -2+2 & -1+2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
   $$

3. Relation to the definition:
   Because both products $AB$ and $BA$ result in the identity matrix $I$, the matrix $B$ fulfills the fundamental two-sided definition of the matrix inverse.
   Therefore, $B = A^{-1}$.

---

## Result

$$
AB = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I, \qquad BA = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \implies B = A^{-1}
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute determinants: $\det(A) = 2(1) - 1(1) = 1$. By the inverse determinant rule, $\det(A^{-1}) = \frac{1}{\det A} = 1$. Computing $\det(B) = 1(2) - (-1)(-1) = 2 - 1 = 1$. The identity $\det(A)\det(B) = 1 \cdot 1 = 1 = \det(I)$ is verified.

**Pass 2 — Numerical check:** Plug in the $2 \times 2$ inverse formula: $A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{1}\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = B$.

**Pass 3 — Consistency check:** Since $A$ is symmetric ($A = A^T$), its inverse must also be symmetric: $B^T = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}^T = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = B$.

---

## Exam tip

To verify whether a proposed matrix is the inverse, simply multiply it with the original matrix; if the product is the identity matrix $I$, it is the inverse.


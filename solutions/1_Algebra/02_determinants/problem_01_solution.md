# Exercise 1

**Problem:** Compute
$$\det\begin{pmatrix}3&-2\\5&4\end{pmatrix},\qquad \det\begin{pmatrix}1&7\\2&14\end{pmatrix}.$$
Which matrix is invertible? Justify your answer.

---

## Relevant theorem / definition

For a $2 \times 2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, its determinant is:
$$
\det(M) = ad - bc
$$
A square matrix is invertible if and only if $\det(M) \neq 0$.

---

## Solution

1. First matrix:
   Let $A = \begin{pmatrix} 3 & -2 \\ 5 & 4 \end{pmatrix}$.
   $$
   \det(A) = 3(4) - (-2)(5) = 12 - (-10) = 12 + 10 = 22
   $$

2. Second matrix:
   Let $B = \begin{pmatrix} 1 & 7 \\ 2 & 14 \end{pmatrix}$.
   $$
   \det(B) = 1(14) - 7(2) = 14 - 14 = 0
   $$

3. Invertibility:
   - For matrix $A$, $\det(A) = 22 \neq 0$, so $A$ is invertible.
   - For matrix $B$, $\det(B) = 0$, so $B$ is not invertible (singular).

---

## Result

$$
\det\begin{pmatrix} 3 & -2 \\ 5 & 4 \end{pmatrix} = 22 \neq 0 \implies \text{invertible}
$$

$$
\det\begin{pmatrix} 1 & 7 \\ 2 & 14 \end{pmatrix} = 0 \implies \text{not invertible}
$$

---

## Verification

**Pass 1 — Algebraic check:** Row dependence check for $B$: the second row is $2 \times$ the first row: $(2, 14) = 2(1, 7)$. Linearly dependent rows algebraically guarantee $\det(B) = 0$.

**Pass 2 — Numerical check:** Compute inverse formula for $A$:
$$
A^{-1} = \frac{1}{22} \begin{pmatrix} 4 & 2 \\ -5 & 3 \end{pmatrix} \implies A A^{-1} = \frac{1}{22} \begin{pmatrix} 3(4)+(-2)(-5) & 3(2)+(-2)(3) \\ 5(4)+4(-5) & 5(2)+4(3) \end{pmatrix} = \frac{1}{22} \begin{pmatrix} 22 & 0 \\ 0 & 22 \end{pmatrix} = I
$$

**Pass 3 — Consistency check:** For $B$, row operations give $R_2 \leftarrow R_2 - 2R_1 \implies \begin{pmatrix} 1 & 7 \\ 0 & 0 \end{pmatrix}$, which has a zero row, confirming rank is 1 and $\det = 0$.

---

## Exam tip

A matrix is invertible if and only if its determinant is non-zero; check for proportional rows first for an immediate answer.


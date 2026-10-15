# Exercise 10

**Problem:** Without carrying out a full determinant calculation, explain why
$$\det\begin{pmatrix}1&2&3\\2&4&6\\0&1&5\end{pmatrix}=0.$$
Identify a specific dependence between the rows and connect it with noninvertibility of the matrix.

---

## Relevant theorem / definition

If a square matrix has linearly dependent rows (or columns) — in particular, if one row is a scalar multiple of another — its determinant is zero:
$$
R_i = c R_j \implies \det(A) = 0
$$
A matrix with $\det(A) = 0$ is singular and has no inverse.

---

## Solution

Let the rows of the matrix $A$ be:
$$
R_1 = \begin{pmatrix} 1 & 2 & 3 \end{pmatrix}, \qquad R_2 = \begin{pmatrix} 2 & 4 & 6 \end{pmatrix}, \qquad R_3 = \begin{pmatrix} 0 & 1 & 5 \end{pmatrix}
$$

1. Identification of row dependence:
   Comparing $R_1$ and $R_2$:
   $$
   R_2 = 2 \cdot R_1
   $$
   since $(2, 4, 6) = 2(1, 2, 3)$. The second row is an exact scalar multiple of the first row.

2. Determinant value:
   Performing the row operation $R_2 \leftarrow R_2 - 2R_1$, which does not change the determinant, produces a row consisting entirely of zeros:
   $$
   \begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 1 & 5 \end{pmatrix}
   $$
   Expanding along the zero row yields:
   $$
   \det(A) = 0
   $$

3. Connection with non-invertibility:
   Because the rows are linearly dependent:
   - The row rank of the matrix is at most 2, which is strictly less than the dimension $n = 3$.
   - By the Invertible Matrix Theorem, an $n \times n$ matrix is invertible if and only if $\text{rank}(A) = n$, which is equivalent to $\det(A) \neq 0$.
   - Since $\text{rank}(A) < 3$ and $\det(A) = 0$, the matrix maps $\mathbb{R}^3$ into a proper subspace (at most a 2D plane). It is not surjective, not injective, and therefore possesses no inverse matrix $A^{-1}$.

---

## Result

$$
R_2 = 2R_1 \implies \det\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 5 \end{pmatrix} = 0 \implies \text{not invertible}
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute Sarrus expansion to confirm:
$$
\begin{align}
\det(A) &= [1(4)(5) + 2(6)(0) + 3(2)(1)] - [3(4)(0) + 1(6)(1) + 2(2)(5)] \\
&= [20 + 0 + 6] - [0 + 6 + 20] \\
&= 26 - 26 = 0
\end{align}
$$
Algebraically confirms $\det(A) = 0$.

**Pass 2 — Numerical check:** Let $\mathbf{x} = \begin{pmatrix} 2 \\ -1 \\ 0 \end{pmatrix} \neq \mathbf{0}$. Check $A\mathbf{x}$:
$$
A\mathbf{x} = \begin{pmatrix} 1(2)+2(-1)+0 \\ 2(2)+4(-1)+0 \\ 0(2)+1(-1)+5(0) \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}
$$
To find an exact kernel vector, solve $Ax = 0$: $x_1 + 2x_2 + 3x_3 = 0$ and $x_2 + 5x_3 = 0$. For $x_3 = 1 \implies x_2 = -5 \implies x_1 = 7$.
Then $A \begin{pmatrix} 7 \\ -5 \\ 1 \end{pmatrix} = \begin{pmatrix} 7-10+3 \\ 14-20+6 \\ 0-5+5 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$.
The existence of a non-zero null space vector confirms non-invertibility.

**Pass 3 — Consistency check:** Proportional rows always imply that the volume spanned by the row vectors has zero 3D thickness (it is flattened into a 2D plane), so volume $= |\det(A)| = 0$.

---

## Exam tip

Always scan for proportional rows or columns before calculating a determinant; finding one immediately yields $\det = 0$ and non-invertibility.


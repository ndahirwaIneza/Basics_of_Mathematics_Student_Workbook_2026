# Exercise 8

**Problem:** For
$$A=\begin{pmatrix}1&2&-1\\2&4&1\\-1&1&3\end{pmatrix}$$
perform, in order:
1. $R_2\leftarrow R_2-2R_1$,
2. $R_3\leftarrow R_3+R_1$,
3. interchange $R_2$ and $R_3$.

Write the matrix after each step. Then, for each of the three operations, state an operation that reverses it.

---

## Relevant theorem / definition

The three elementary row operations on a matrix are:
1. Row addition/replacement: $R_i \leftarrow R_i + c R_j$ ($i \neq j$), reversed by $R_i \leftarrow R_i - c R_j$.
2. Row scaling: $R_i \leftarrow c R_i$ ($c \neq 0$), reversed by $R_i \leftarrow \frac{1}{c} R_i$.
3. Row interchange: $R_i \leftrightarrow R_j$, reversed by $R_i \leftrightarrow R_j$.

---

## Solution

The starting matrix is:
$$
A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & 1 \\ -1 & 1 & 3 \end{pmatrix}
$$

Step 1: Perform $R_2 \leftarrow R_2 - 2R_1$:
$$
R_2 - 2R_1 = \begin{pmatrix} 2 - 2(1) & 4 - 2(2) & 1 - 2(-1) \end{pmatrix} = \begin{pmatrix} 0 & 0 & 3 \end{pmatrix}
$$
The matrix becomes:
$$
A_1 = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ -1 & 1 & 3 \end{pmatrix}
$$
The reverse operation is:
$$
R_2 \leftarrow R_2 + 2R_1
$$

Step 2: Perform $R_3 \leftarrow R_3 + R_1$:
$$
R_3 + R_1 = \begin{pmatrix} -1 + 1 & 1 + 2 & 3 + (-1) \end{pmatrix} = \begin{pmatrix} 0 & 3 & 2 \end{pmatrix}
$$
The matrix becomes:
$$
A_2 = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 3 & 2 \end{pmatrix}
$$
The reverse operation is:
$$
R_3 \leftarrow R_3 - R_1
$$

Step 3: Interchange $R_2$ and $R_3$ ($R_2 \leftrightarrow R_3$):
The matrix becomes:
$$
A_3 = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix}
$$
The reverse operation is:
$$
R_2 \leftrightarrow R_3
$$

---

## Result

$$
A_1 = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ -1 & 1 & 3 \end{pmatrix}, \quad \text{reverse: } R_2 \leftarrow R_2 + 2R_1
$$

$$
A_2 = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 3 & 2 \end{pmatrix}, \quad \text{reverse: } R_3 \leftarrow R_3 - R_1
$$

$$
A_3 = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix}, \quad \text{reverse: } R_2 \leftrightarrow R_3
$$

---

## Verification

**Pass 1 — Algebraic check:** Apply the reverse operations in reverse order to $A_3$:
Swap $R_2 \leftrightarrow R_3$ recovers $A_2$; $R_3 \leftarrow R_3 - R_1$ recovers $A_1$; $R_2 \leftarrow R_2 + 2R_1$ recovers $A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & 1 \\ -1 & 1 & 3 \end{pmatrix}$.

**Pass 2 — Numerical check:** The final matrix $A_3$ is in upper triangular form. Its determinant is the product of diagonal entries: $1 \cdot 3 \cdot 3 = 9$. Because a row swap flips the sign of the determinant, $\det(A) = -9$. Expanding original $A$ along row 1: $1(12-1) - 2(6 - (-1)) + (-1)(2 - (-4)) = 11 - 14 - 6 = -9$. Both match.

**Pass 3 — Consistency check:** Step 1 affects only row 2; step 2 affects only row 3; step 3 exchanges rows 2 and 3. Row 1 remains $\begin{pmatrix} 1 & 2 & -1 \end{pmatrix}$ throughout.

---

## Exam tip

Elementary row operations preserve the row space and invertibility of a matrix, which forms the basis of Gaussian elimination.


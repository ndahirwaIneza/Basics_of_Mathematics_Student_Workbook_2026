# Exercise 11

**Problem:** Compute
$$\det\begin{pmatrix}1&2&3\\1&3&4\\1&4&6\end{pmatrix}$$
by first performing row operations that create as many zeros as possible. State which operations do not change the determinant.

---

## Relevant theorem / definition

Elementary row replacement operations of the form $R_i \leftarrow R_i + c R_j$ ($i \neq j$) preserve the determinant:
$$
\det(E_{ij}(c) A) = \det(A)
$$
Creating zeros in a column using these operations transforms the matrix into triangular form without altering the determinant's value.

---

## Solution

The initial matrix is:
$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 4 \\ 1 & 4 & 6 \end{pmatrix}
$$

Step 1: Create zeros in the first column below entry $a_{11} = 1$:
- Apply $R_2 \leftarrow R_2 - R_1$:
  $$
  R_2 - R_1 = \begin{pmatrix} 1 - 1 & 3 - 2 & 4 - 3 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 1 \end{pmatrix}
  $$
- Apply $R_3 \leftarrow R_3 - R_1$:
  $$
  R_3 - R_1 = \begin{pmatrix} 1 - 1 & 4 - 2 & 6 - 3 \end{pmatrix} = \begin{pmatrix} 0 & 2 & 3 \end{pmatrix}
  $$
Both of these operations are row additions of the form $R_i \leftarrow R_i - R_j$, which do not change the determinant.
The matrix becomes:
$$
A_1 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 2 & 3 \end{pmatrix}, \qquad \det A = \det A_1
$$

Step 2: Create a zero in the second column below entry $(2,2) = 1$:
- Apply $R_3 \leftarrow R_3 - 2R_2$:
  $$
  R_3 - 2R_2 = \begin{pmatrix} 0 - 2(0) & 2 - 2(1) & 3 - 2(1) \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 \end{pmatrix}
  $$
This operation is also a row addition, so it does not change the determinant.
The matrix becomes:
$$
A_2 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det A = \det A_2
$$

Step 3: Evaluate the determinant of the resulting upper triangular matrix:
$$
\det A = 1 \cdot 1 \cdot 1 = 1
$$

Operations that do not change the determinant:
All operations used ($R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - R_1$, and $R_3 \leftarrow R_3 - 2R_2$) are row replacement operations ($R_i \leftarrow R_i + c R_j$), none of which change the determinant.

---

## Result

$$
\det\begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 4 \\ 1 & 4 & 6 \end{pmatrix} = 1
$$

---

## Verification

**Pass 1 — Algebraic check:** Direct Sarrus calculation:
$$
\begin{align}
\det A &= [1(3)(6) + 2(4)(1) + 3(1)(4)] - [3(3)(1) + 1(4)(4) + 2(1)(6)] \\
&= [18 + 8 + 12] - [9 + 16 + 12] \\
&= 38 - 37 = 1
\end{align}
$$
Matches the elimination result.

**Pass 2 — Numerical check:** Column operations check: $C_2 \leftarrow C_2 - 2C_1$ and $C_3 \leftarrow C_3 - 3C_1$ give $\begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 3 \end{pmatrix}$.
Then $C_3 \leftarrow C_3 - C_2$ gives $\begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 2 & 1 \end{pmatrix}$, a lower triangular matrix with diagonal product $1 \cdot 1 \cdot 1 = 1$.

**Pass 3 — Consistency check:** The matrix entries are consecutive in row differences: $\Delta R_1 = R_2 - R_1 = (0, 1, 1)$ and $\Delta R_2 = R_3 - R_2 = (0, 1, 2)$. The second difference is $(0, 0, 1)$, giving an echelon matrix with determinant 1.

---

## Exam tip

Using $R_i \leftarrow R_i + c R_j$ to eliminate entries column-by-column into upper triangular form is the fastest, least error-prone method for calculating determinants.


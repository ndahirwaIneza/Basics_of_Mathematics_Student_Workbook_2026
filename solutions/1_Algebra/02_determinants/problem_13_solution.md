# Exercise 13

**Problem:** Compute the determinant
$$A=\begin{pmatrix}1&2&3\\2&5&7\\1&0&2\end{pmatrix}$$
using elimination. Record the effect of every row operation used on the value of the determinant.

---

## Relevant theorem / definition

Gaussian elimination transforms a matrix into upper triangular form using elementary row operations:
- Row replacement $R_i \leftarrow R_i + c R_j$: preserves determinant value ($\times 1$).
- Row swap $R_i \leftrightarrow R_j$: reverses sign ($\times (-1)$).
- Row scaling $R_i \leftarrow c R_i$: scales determinant ($\times c$).
For an upper triangular matrix, the determinant is the product of its diagonal elements.

---

## Solution

The initial matrix is:
$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \\ 1 & 0 & 2 \end{pmatrix}
$$

Step 1: Eliminate entry $a_{21} = 2$ using pivot $a_{11} = 1$:
Apply $R_2 \leftarrow R_2 - 2R_1$:
$$
R_2 - 2R_1 = \begin{pmatrix} 2 - 2(1) & 5 - 2(2) & 7 - 2(3) \end{pmatrix} = \begin{pmatrix} 0 & 1 & 1 \end{pmatrix}
$$
Effect on determinant: row addition does not change the determinant ($\det A = \det A_1$).
The matrix is now:
$$
A_1 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 1 & 0 & 2 \end{pmatrix}
$$

Step 2: Eliminate entry $a_{31} = 1$ using pivot $a_{11} = 1$:
Apply $R_3 \leftarrow R_3 - R_1$:
$$
R_3 - R_1 = \begin{pmatrix} 1 - 1 & 0 - 2 & 2 - 3 \end{pmatrix} = \begin{pmatrix} 0 & -2 & -1 \end{pmatrix}
$$
Effect on determinant: row addition does not change the determinant ($\det A = \det A_2$).
The matrix is now:
$$
A_2 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & -2 & -1 \end{pmatrix}
$$

Step 3: Eliminate entry $a_{32} = -2$ using pivot $a_{22} = 1$:
Apply $R_3 \leftarrow R_3 + 2R_2$:
$$
R_3 + 2R_2 = \begin{pmatrix} 0 + 2(0) & -2 + 2(1) & -1 + 2(1) \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 \end{pmatrix}
$$
Effect on determinant: row addition does not change the determinant ($\det A = \det A_3$).
The matrix is now in upper triangular form:
$$
A_3 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}
$$

Step 4: Compute the determinant from the triangular form:
$$
\det A = \det A_3 = 1 \cdot 1 \cdot 1 = 1
$$

Summary of effects:
All three operations were row replacements ($R_i \leftarrow R_i + c R_j$), so each had an effect factor of $1$. No row interchanges or row scalings were required.

---

## Result

$$
\det\begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \\ 1 & 0 & 2 \end{pmatrix} = 1
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute $\det A$ using Sarrus' rule on the original matrix:
$$
\begin{align}
\det A &= [1(5)(2) + 2(7)(1) + 3(2)(0)] - [3(5)(1) + 1(7)(0) + 2(2)(2)] \\
&= [10 + 14 + 0] - [15 + 0 + 8] \\
&= 24 - 23 = 1
\end{align}
$$
Matches the value obtained through elimination.

**Pass 2 — Numerical check:** Expanding along row 3:
$$
1 \cdot \begin{vmatrix} 2 & 3 \\ 5 & 7 \end{vmatrix} - 0 + 2 \cdot \begin{vmatrix} 1 & 2 \\ 2 & 5 \end{vmatrix} = 1(14 - 15) + 2(5 - 4) = -1 + 2(1) = 1
$$

**Pass 3 — Consistency check:** Since all pivots are 1, the matrix has full rank 3 and unit determinant, meaning it preserves oriented volume.

---

## Exam tip

When using elimination to find determinants, track any row swaps (factor $-1$) or row scalings (factor $1/c$); pure row additions preserve the determinant exactly.


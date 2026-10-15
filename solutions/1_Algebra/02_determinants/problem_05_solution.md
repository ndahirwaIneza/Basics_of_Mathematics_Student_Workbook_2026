# Exercise 5

**Problem:** For
$$A=\begin{pmatrix}1&2&3\\2&1&0\\-1&4&2\end{pmatrix}$$
find $\det A$ by simplifying the matrix with row operations. At each step, indicate whether and how the determinant changes.

---

## Relevant theorem / definition

Elementary row operations affect determinants as follows:
1. $R_i \leftarrow R_i + c R_j$ ($i \neq j$): does not change the determinant ($\det$ multiplied by 1).
2. $R_i \leftrightarrow R_j$: reverses the sign of the determinant ($\det$ multiplied by $-1$).
3. $R_i \leftarrow c R_i$: scales the determinant by $c$ ($\det$ multiplied by $c$).

---

## Solution

The initial matrix is:
$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 0 \\ -1 & 4 & 2 \end{pmatrix}
$$

Step 1: Perform $R_2 \leftarrow R_2 - 2R_1$.
Effect on determinant: adding a multiple of one row to another preserves the determinant ($\det$ is unchanged).
$$
R_2 - 2R_1 = \begin{pmatrix} 2 - 2(1) & 1 - 2(2) & 0 - 2(3) \end{pmatrix} = \begin{pmatrix} 0 & -3 & -6 \end{pmatrix}
$$
The matrix becomes:
$$
A_1 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ -1 & 4 & 2 \end{pmatrix}, \qquad \det A = \det A_1
$$

Step 2: Perform $R_3 \leftarrow R_3 + R_1$.
Effect on determinant: adding a multiple of one row to another preserves the determinant ($\det$ is unchanged).
$$
R_3 + R_1 = \begin{pmatrix} -1 + 1 & 4 + 2 & 2 + 3 \end{pmatrix} = \begin{pmatrix} 0 & 6 & 5 \end{pmatrix}
$$
The matrix becomes:
$$
A_2 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 0 & 6 & 5 \end{pmatrix}, \qquad \det A = \det A_2
$$

Step 3: Perform $R_3 \leftarrow R_3 + 2R_2$.
Effect on determinant: adding a multiple of one row to another preserves the determinant ($\det$ is unchanged).
$$
R_3 + 2R_2 = \begin{pmatrix} 0 + 2(0) & 6 + 2(-3) & 5 + 2(-6) \end{pmatrix} = \begin{pmatrix} 0 & 0 & -7 \end{pmatrix}
$$
The matrix becomes:
$$
A_3 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 0 & 0 & -7 \end{pmatrix}, \qquad \det A = \det A_3
$$

Since $A_3$ is in upper triangular form, its determinant is the product of its diagonal entries:
$$
\det A = \det A_3 = 1 \cdot (-3) \cdot (-7) = 21
$$

---

## Result

$$
\det A = 21
$$

---

## Verification

**Pass 1 — Algebraic check:** Direct Sarrus calculation on the original matrix $A$:
$$
\begin{align}
\det A &= [1(1)(2) + 2(0)(-1) + 3(2)(4)] - [3(1)(-1) + 1(0)(4) + 2(2)(2)] \\
&= [2 + 0 + 24] - [-3 + 0 + 8] \\
&= 26 - 5 = 21
\end{align}
$$
Matches the result obtained via row reduction.

**Pass 2 — Numerical check:** Factor $-3$ out of row 2: $\det A = -3 \begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 6 & 5 \end{vmatrix} = -3 [1(1 \cdot 5 - 2 \cdot 6)] = -3(5 - 12) = -3(-7) = 21$.

**Pass 3 — Consistency check:** Since only row addition operations ($R_i \leftarrow R_i + c R_j$) were used, no sign flips or scale factor adjustments occurred, ensuring $\det A = \det A_3$.

---

## Exam tip

Using row operations of the type $R_i \leftarrow R_i + c R_j$ to eliminate entries below the diagonal never changes the determinant, reducing the computation to multiplying diagonal entries.


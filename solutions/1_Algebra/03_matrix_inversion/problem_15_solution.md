# Exercise 15

**Problem:** For
$$A=\begin{pmatrix}2&1\\1&3\end{pmatrix},\qquad b=\begin{pmatrix}7\\8\end{pmatrix}$$
solve $Ax=b$ in two ways:

1. using $A^{-1}b$,
2. using Gaussian elimination.

Compare both solutions, the number of essential steps, and state which method was simpler in this example.

---

## Relevant theorem / definition

A linear system $Ax = b$ with non-singular $A$ can be solved by:
1. Matrix inversion: $x = A^{-1}b$, where $A^{-1}$ is computed first.
2. Gaussian elimination: $[A \mid b] \xrightarrow{\text{row operations}} [U \mid c]$, followed by back-substitution.

---

## Solution

The system is:
$$
A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}, \qquad b = \begin{pmatrix} 7 \\ 8 \end{pmatrix}
$$

1. Method 1 — Inversion ($x = A^{-1}b$):
   Step 1: Compute $\det(A) = 2(3) - 1(1) = 6 - 1 = 5 \neq 0$.
   Step 2: Find $A^{-1}$ using the $2 \times 2$ formula:
   $$
   A^{-1} = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}
   $$
   Step 3: Multiply $A^{-1}$ by $b$:
   $$
   x = A^{-1}b = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 7 \\ 8 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 3(7) + (-1)(8) \\ -1(7) + 2(8) \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 21 - 8 \\ -7 + 16 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 13 \\ 9 \end{pmatrix} = \begin{pmatrix} \frac{13}{5} \\ \frac{9}{5} \end{pmatrix}
   $$

2. Method 2 — Gaussian elimination:
   Step 1: Set up the augmented matrix $[A \mid b]$:
   $$
   \left[\begin{array}{cc|c} 2 & 1 & 7 \\ 1 & 3 & 8 \end{array}\right]
   $$
   Step 2: Swap rows ($R_1 \leftrightarrow R_2$) to obtain pivot 1:
   $$
   \left[\begin{array}{cc|c} 1 & 3 & 8 \\ 2 & 1 & 7 \end{array}\right]
   $$
   Step 3: Eliminate position $(2,1)$ via $R_2 \leftarrow R_2 - 2R_1$:
   $$
   R_2 - 2R_1 = \left[\begin{array}{cc|c} 2 - 2(1) & 1 - 2(3) & 7 - 2(8) \end{array}\right] = \left[\begin{array}{cc|c} 0 & -5 & -9 \end{array}\right]
   $$
   The upper triangular echelon form is:
   $$
   \left[\begin{array}{cc|c} 1 & 3 & 8 \\ 0 & -5 & -9 \end{array}\right]
   $$
   Step 4: Back-substitution:
   From row 2: $-5 x_2 = -9 \implies x_2 = \frac{9}{5}$.
   From row 1: $x_1 + 3x_2 = 8 \implies x_1 = 8 - 3\left(\frac{9}{5}\right) = \frac{40 - 27}{5} = \frac{13}{5}$.
   Thus:
   $$
   x = \begin{pmatrix} \frac{13}{5} \\ \frac{9}{5} \end{pmatrix}
   $$

3. Comparison:
   - Both methods produce the exact same solution vector $x = \begin{pmatrix} 13/5 \\ 9/5 \end{pmatrix}$.
   - Essential stages:
     - Method 1 computes the determinant, constructs the inverse, and then performs a matrix-vector multiplication.
     - Method 2 performs one row swap, one elimination step, and back-substitution. A complete scalar-operation comparison would also count the augmented-entry update, back-substitution, and divisions, so the stage comparison is more meaningful here than the incomplete counts of individual arithmetic operations.
   - Which was simpler:
     For this single system, Gaussian elimination was simpler because it directly solves for the unknowns without constructing the four entries of the inverse matrix. For multiple right-hand sides with the same matrix $A$, an existing inverse can be reused, but an LU factorization or elimination factors can also be reused, so inversion is not automatically superior.

---

## Result

$$
x = \begin{pmatrix} \frac{13}{5} \\ \frac{9}{5} \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute $x$ into original equation 1:
$$
2\left(\frac{13}{5}\right) + 1\left(\frac{9}{5}\right) = \frac{26 + 9}{5} = \frac{35}{5} = 7 = b_1
$$
Substitute $x$ into original equation 2:
$$
1\left(\frac{13}{5}\right) + 3\left(\frac{9}{5}\right) = \frac{13 + 27}{5} = \frac{40}{5} = 8 = b_2
$$
Both equations are satisfied.

**Pass 2 — Numerical check:** Check using Cramer's rule:
$$
x_1 = \frac{\begin{vmatrix} 7 & 1 \\ 8 & 3 \end{vmatrix}}{5} = \frac{21 - 8}{5} = \frac{13}{5}, \qquad x_2 = \frac{\begin{vmatrix} 2 & 7 \\ 1 & 8 \end{vmatrix}}{5} = \frac{16 - 7}{5} = \frac{9}{5}
$$
Matches both previous methods.

**Pass 3 — Consistency check:** The coefficient matrix $A$ is symmetric positive definite because its leading principal minors satisfy $2>0$ and $\det A=5>0$. This guarantees a unique solution; positive definiteness alone does not guarantee that the system is well-conditioned.

---

## Exam tip

For a single system of equations, Gaussian elimination avoids the extra work of explicitly forming the inverse. For several right-hand sides, reuse an existing inverse or reuse LU/elimination factors; inversion is not automatically the best choice.

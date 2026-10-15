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
   - Operation count / steps:
     - Method 1 requires 3 distinct conceptual stages: calculating the determinant, constructing the $2 \times 2$ inverse matrix, and computing a matrix-vector dot product (involving 4 multiplications and 2 additions).
     - Method 2 requires only 1 row swap, 1 row elimination step, and 1 back-substitution step (involving 2 multiplications and 1 subtraction).
   - Which was simpler:
     For this single system, Gaussian elimination was simpler and faster because it directly solves for the unknowns without constructing the four entries of the inverse matrix. However, if multiple systems $Ax = b_i$ needed to be solved for various right-hand sides with the same matrix $A$, Method 1 would be superior since $A^{-1}$ would only need to be computed once.

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

**Pass 3 — Consistency check:** The coefficient matrix $A$ is symmetric positive definite ($2 > 0$ and $\det A = 5 > 0$), guaranteeing a unique, well-conditioned solution.

---

## Exam tip

For a single system of equations, Gaussian elimination is faster than inverting the matrix; only invert $A$ if you must solve $Ax = b$ for several different vectors $b$.


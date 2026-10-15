# Exercise 2

**Problem:** Solve using Gaussian elimination:
$$\begin{cases}x+y+z=6,\\2x-y+z=3,\\x+2y-z=2.\end{cases}$$
After solving, substitute the result into all equations and check consistency.

---

## Relevant theorem / definition

Gaussian elimination transforms the augmented matrix $[A \mid \mathbf{b}]$ of a linear system into row echelon form through elementary row operations, followed by back-substitution to find the unique solution vector $\mathbf{x}$.

---

## Solution

The system is:
$$
\begin{cases}
x + y + z = 6 \\
2x - y + z = 3 \\
x + 2y - z = 2
\end{cases}
$$

Step 1: Set up the augmented matrix:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
2 & -1 & 1 & 3 \\
1 & 2 & -1 & 2
\end{array}\right]
$$

Step 2: Eliminate $x$ from rows 2 and 3 using pivot in row 1:
- Apply $R_2 \leftarrow R_2 - 2R_1$:
  $$
  R_2 - 2R_1 = \left[\begin{array}{ccc|c} 2 - 2(1) & -1 - 2(1) & 1 - 2(1) & 3 - 2(6) \end{array}\right] = \left[\begin{array}{ccc|c} 0 & -3 & -1 & -9 \end{array}\right]
  $$
- Apply $R_3 \leftarrow R_3 - R_1$:
  $$
  R_3 - R_1 = \left[\begin{array}{ccc|c} 1 - 1 & 2 - 1 & -1 - 1 & 2 - 6 \end{array}\right] = \left[\begin{array}{ccc|c} 0 & 1 & -2 & -4 \end{array}\right]
  $$
The matrix becomes:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & -3 & -1 & -9 \\
0 & 1 & -2 & -4
\end{array}\right]
$$

Step 3: Swap rows 2 and 3 to obtain pivot $+1$:
Apply $R_2 \leftrightarrow R_3$:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & -3 & -1 & -9
\end{array}\right]
$$

Step 4: Eliminate $y$ from row 3 using pivot in row 2:
Apply $R_3 \leftarrow R_3 + 3R_2$:
$$
R_3 + 3R_2 = \left[\begin{array}{ccc|c} 0 + 3(0) & -3 + 3(1) & -1 + 3(-2) & -9 + 3(-4) \end{array}\right] = \left[\begin{array}{ccc|c} 0 & 0 & -7 & -21 \end{array}\right]
$$
The matrix is now in row echelon form:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & 0 & -7 & -21
\end{array}\right]
$$

Step 5: Back-substitution:
- From Row 3:
  $$
  -7z = -21 \implies z = \frac{-21}{-7} = 3
  $$
- From Row 2:
  $$
  y - 2z = -4 \implies y - 2(3) = -4 \implies y - 6 = -4 \implies y = 2
  $$
- From Row 1:
  $$
  x + y + z = 6 \implies x + 2 + 3 = 6 \implies x + 5 = 6 \implies x = 1
  $$

The unique solution is $(x, y, z) = (1, 2, 3)$.

Substitution check into all original equations:
1. Equation 1: $x + y + z = 1 + 2 + 3 = 6$ (holds)
2. Equation 2: $2x - y + z = 2(1) - 2 + 3 = 2 - 2 + 3 = 3$ (holds)
3. Equation 3: $x + 2y - z = 1 + 2(2) - 3 = 1 + 4 - 3 = 2$ (holds)
All three equations are satisfied.

---

## Result

$$
\mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Solve via Cramer's rule:
$\det(A) = 1(1 - (-2)) - 1(-2 - 1) + 1(4 - (-1)) = 3 + 3 + 5$ ... let's check:
$\det(A) = 1(1 - (-2)) - 1(-2 - 1) + 1(4 - (-1))$ wait, row 1 is $(1, 1, 1)$, row 2 is $(2, -1, 1)$, row 3 is $(1, 2, -1)$.
$\det(A) = 1(1 - 2) - 1(-2 - 1) + 1(4 - (-1)) = -1 + 3 + 5 = 7 \neq 0$.
Product of pivots after one swap: $(-1) \cdot [1 \cdot 1 \cdot (-7)] = 7$. Matches.

**Pass 2 — Numerical check:**
$\det(A_x) = \begin{vmatrix} 6 & 1 & 1 \\ 3 & -1 & 1 \\ 2 & 2 & -1 \end{vmatrix} = 6(1-2) - 1(-3-2) + 1(6 - (-2)) = -6 + 5 + 8 = 7 \implies x = 7/7 = 1$.
$\det(A_y) = \begin{vmatrix} 1 & 6 & 1 \\ 2 & 3 & 1 \\ 1 & 2 & -1 \end{vmatrix} = 1(-3-2) - 6(-2-1) + 1(4-3) = -5 + 18 + 1 = 14 \implies y = 14/7 = 2$.
$\det(A_z) = \begin{vmatrix} 1 & 1 & 6 \\ 2 & -1 & 3 \\ 1 & 2 & 2 \end{vmatrix} = 1(-2-6) - 1(4-3) + 6(4 - (-1)) = -8 - 1 + 30 = 21 \implies z = 21/7 = 3$.

**Pass 3 — Consistency check:** Since $\text{rank}(A) = \text{rank}([A \mid \mathbf{b}]) = 3$, by Rouché–Capelli the system has a unique solution.

---

## Exam tip

Swapping rows to obtain a pivot of $+1$ (as done in $R_2 \leftrightarrow R_3$) eliminates fractions and minimizes arithmetic errors during elimination.


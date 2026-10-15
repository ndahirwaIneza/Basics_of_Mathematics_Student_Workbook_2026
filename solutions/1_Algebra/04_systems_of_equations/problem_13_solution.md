# Exercise 13

**Problem:** Consider the system
$$x_1+x_2=10,\qquad x_2+x_3=8,\qquad x_1-x_3=2.$$
Solve it and check whether all three equations are independently necessary to describe the solution set. If one follows from the others, show this by calculation.

---

## Relevant theorem / definition

An equation in a linear system is redundant (not independently necessary) if it can be written as a linear combination of the other equations:
$$
E_k = \sum_{j \neq k} c_j E_j
$$
In Gaussian elimination, redundant equations reduce to a row of zeros $[0 \; 0 \cdots 0 \mid 0]$, indicating that $\text{rank}(A) < m$.

---

## Solution

The system of equations is:
$$
\begin{cases}
x_1 + x_2 = 10 \\
x_2 + x_3 = 8 \\
x_1 - x_3 = 2
\end{cases}
$$

1. Set up the augmented matrix:
   $$
   \left[\begin{array}{ccc|c}
   1 & 1 & 0 & 10 \\
   0 & 1 & 1 & 8 \\
   1 & 0 & -1 & 2
   \end{array}\right]
   $$

2. Perform row elimination:
   - Eliminate $x_1$ from row 3 using row 1 via $R_3 \leftarrow R_3 - R_1$:
     $$
     R_3 - R_1 = \left[\begin{array}{ccc|c} 1 - 1 & 0 - 1 & -1 - 0 & 2 - 10 \end{array}\right] = \left[\begin{array}{ccc|c} 0 & -1 & -1 & -8 \end{array}\right]
     $$
   - Eliminate $x_2$ from row 3 using row 2 via $R_3 \leftarrow R_3 + R_2$:
     $$
     R_3 + R_2 = \left[\begin{array}{ccc|c} 0 + 0 & -1 + 1 & -1 + 1 & -8 + 8 \end{array}\right] = \left[\begin{array}{ccc|c} 0 & 0 & 0 & 0 \end{array}\right]
     $$
   The resulting row echelon form is:
   $$
   \left[\begin{array}{ccc|c}
   1 & 1 & 0 & 10 \\
   0 & 1 & 1 & 8 \\
   0 & 0 & 0 & 0
   \end{array}\right]
   $$

3. Are all three equations independently necessary?
   No, they are not. The third row reduces to all zeros, which proves that the third equation is linearly dependent on the first two.
   Explicit calculation showing how Equation 3 follows from Equations 1 and 2:
   Subtract Equation 2 from Equation 1:
   $$
   (x_1 + x_2) - (x_2 + x_3) = 10 - 8 \implies x_1 - x_3 = 2
   $$
   The left-hand side simplifies to $x_1 - x_3$, and the right-hand side simplifies to 2, which is precisely Equation 3.
   Therefore, Equation 3 contains no new information and is redundant.

4. Parametric solution of the system:
   Since $\text{rank}(A) = 2$ and $n = 3$, there are $3 - 2 = 1$ free variable.
   Column 3 has no pivot, so set $x_3 = t \in \mathbb{R}$.
   - From Row 2:
     $$
     x_2 + x_3 = 8 \implies x_2 = 8 - t
     $$
   - From Row 1:
     $$
     x_1 + x_2 = 10 \implies x_1 + (8 - t) = 10 \implies x_1 = 2 + t
     $$
   The parametric solution is:
   $$
   \mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 2 + t \\ 8 - t \\ t \end{pmatrix} = \begin{pmatrix} 2 \\ 8 \\ 0 \end{pmatrix} + t \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}
   $$

---

## Result

$$
\text{The equations are not independently necessary; Equation 3 is redundant:}
$$

$$
\text{Equation 3} = \text{Equation 1} - \text{Equation 2}: \quad (x_1 + x_2) - (x_2 + x_3) = 10 - 8 \iff x_1 - x_3 = 2
$$

$$
\mathbf{x} = \begin{pmatrix} 2 + t \\ 8 - t \\ t \end{pmatrix} = \begin{pmatrix} 2 \\ 8 \\ 0 \end{pmatrix} + t \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute $(2+t, 8-t, t)$ into the three equations:
- $x_1 + x_2 = (2 + t) + (8 - t) = 10$ (holds).
- $x_2 + x_3 = (8 - t) + t = 8$ (holds).
- $x_1 - x_3 = (2 + t) - t = 2$ (holds).
All three equations hold for every real value of $t$.

**Pass 2 — Numerical check:** For $t = 0$: $(x_1, x_2, x_3) = (2, 8, 0)$.
$2 + 8 = 10$, $8 + 0 = 8$, $2 - 0 = 2$.
For $t = 3$: $(x_1, x_2, x_3) = (5, 5, 3)$.
$5 + 5 = 10$, $5 + 3 = 8$, $5 - 3 = 2$.

**Pass 3 — Consistency check:** Determinant of coefficient matrix:
$$
\det(A) = 1(-1 - 0) - 1(0 - 1) + 0 = -1 + 1 = 0
$$
A zero determinant algebraically confirms the linear dependence of the rows.

---

## Exam tip

If an equation can be produced by adding or subtracting the remaining equations, it is redundant and does not reduce the dimension of the solution space.


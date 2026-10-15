# Exercise 4

**Problem:** Solve
$$\begin{cases}x+y+z=2,\\2x+2y+2z=4,\\x-y+z=0.\end{cases}$$
Give the solution in parametric form, identify a free variable, and for one chosen parameter value check that the resulting point really satisfies the system.

---

## Relevant theorem / definition

When Gaussian elimination produces $\text{rank}(A) = \text{rank}([A \mid b]) = r < n$ (where $n$ is the number of unknowns), the system is consistent with $n - r$ free variables, yielding infinitely many solutions expressed in parametric form:
$$
\mathbf{x} = \mathbf{x}_0 + t_1 \mathbf{v}_1 + \cdots + t_{n-r} \mathbf{v}_{n-r}, \quad t_i \in \mathbb{R}
$$

---

## Solution

The system is:
$$
\begin{cases}
x + y + z = 2 \\
2x + 2y + 2z = 4 \\
x - y + z = 0
\end{cases}
$$

Step 1: Set up the augmented matrix:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 2 \\
2 & 2 & 2 & 4 \\
1 & -1 & 1 & 0
\end{array}\right]
$$

Step 2: Eliminate the first column below entry $(1,1)$:
- Apply $R_2 \leftarrow R_2 - 2R_1$:
  $$
  R_2 - 2R_1 = \left[\begin{array}{ccc|c} 0 & 0 & 0 & 0 \end{array}\right]
  $$
- Apply $R_3 \leftarrow R_3 - R_1$:
  $$
  R_3 - R_1 = \left[\begin{array}{ccc|c} 1 - 1 & -1 - 1 & 1 - 1 & 0 - 2 \end{array}\right] = \left[\begin{array}{ccc|c} 0 & -2 & 0 & -2 \end{array}\right]
  $$
The matrix becomes:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 2 \\
0 & 0 & 0 & 0 \\
0 & -2 & 0 & -2
\end{array}\right]
$$

Step 3: Swap row 2 and row 3 to place non-zero rows first:
Apply $R_2 \leftrightarrow R_3$:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 2 \\
0 & -2 & 0 & -2 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

Step 4: Scale row 2 by $-\frac{1}{2}$:
Apply $R_2 \leftarrow -\frac{1}{2} R_2$:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 2 \\
0 & 1 & 0 & 1 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

Step 5: Identify leading and free variables:
- Column 1 has a pivot: $x$ is a leading (basic) variable.
- Column 2 has a pivot: $y$ is a leading (basic) variable.
- Column 3 has no pivot: $z$ is the free variable.

Set $z = t$, where $t \in \mathbb{R}$ is an arbitrary parameter.

Step 6: Express leading variables in terms of the parameter $t$:
- From row 2:
  $$
  y = 1
  $$
- From row 1:
  $$
  x + y + z = 2 \implies x + 1 + t = 2 \implies x = 1 - t
  $$

Parametric form of the solution:
$$
\mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 - t \\ 1 \\ t \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}
$$

Step 7: Check for one chosen parameter value:
Choose parameter value $t = 2$:
$$
\mathbf{x} = \begin{pmatrix} 1 - 2 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix}
$$
Substitute into the original system:
1. $x + y + z = -1 + 1 + 2 = 2$ (holds)
2. $2x + 2y + 2z = 2(-1) + 2(1) + 2(2) = -2 + 2 + 4 = 4$ (holds)
3. $x - y + z = -1 - 1 + 2 = 0$ (holds)
All three original equations are satisfied.

---

## Result

$$
\text{Free variable: } z = t \in \mathbb{R}
$$

$$
\mathbf{x} = \begin{pmatrix} 1 - t \\ 1 \\ t \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}
$$

$$
\text{For } t = 2: \quad (x, y, z) = (-1, 1, 2) \text{ satisfies all equations}
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute general parametric form into the system:
- $x + y + z = (1 - t) + 1 + t = 2$ (identically 2 for all $t$).
- $2x + 2y + 2z = 2(1 - t) + 2(1) + 2(t) = 2 - 2t + 2 + 2t = 4$ (identically 4 for all $t$).
- $x - y + z = (1 - t) - 1 + t = 0$ (identically 0 for all $t$).
All three equations hold algebraically for every $t \in \mathbb{R}$.

**Pass 2 — Numerical check:** Check $t = 0$: $\mathbf{x} = (1, 1, 0)$.
$1 + 1 + 0 = 2$, $2(1) + 2(1) + 0 = 4$, $1 - 1 + 0 = 0$. Holds.

**Pass 3 — Consistency check:** Since $\text{rank}(A) = \text{rank}([A \mid b]) = 2 < 3$, the solution set is a 1-dimensional line in $\mathbb{R}^3$, matching the 1-parameter family.

---

## Exam tip

Columns without leading pivots in row echelon form correspond directly to free variables; assign them parameter names ($t, s$) to write the solution set.


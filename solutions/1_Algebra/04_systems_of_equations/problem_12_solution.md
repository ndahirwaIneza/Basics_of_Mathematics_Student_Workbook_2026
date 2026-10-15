# Exercise 12

**Problem:** Solve
$$\begin{cases}x+2y-z=0,\\2x+4y-2z=0,\\x-y+2z=0.\end{cases}$$
Give all solutions in parametric form and explain why $(0,0,0)$ always satisfies a homogeneous system.

---

## Relevant theorem / definition

A homogeneous system of linear equations has the form $A\mathbf{x} = \mathbf{0}$.
1. The zero vector $\mathbf{x} = \mathbf{0}$ is always a solution (the trivial solution).
2. Non-trivial solutions exist if and only if $\text{rank}(A) < n$, in which case the solution space is the null space $\text{null}(A)$, a subspace of dimension $n - \text{rank}(A)$.

---

## Solution

The homogeneous system is:
$$
\begin{cases}
x + 2y - z = 0 \\
2x + 4y - 2z = 0 \\
x - y + 2z = 0
\end{cases}
$$

1. Set up the augmented matrix:
   $$
   \left[\begin{array}{ccc|c}
   1 & 2 & -1 & 0 \\
   2 & 4 & -2 & 0 \\
   1 & -1 & 2 & 0
   \end{array}\right]
   $$

2. Perform row operations to eliminate $x$:
   - Apply $R_2 \leftarrow R_2 - 2R_1$:
     $$
     R_2 - 2R_1 = \left[\begin{array}{ccc|c} 2 - 2(1) & 4 - 2(2) & -2 - 2(-1) & 0 \end{array}\right] = \left[\begin{array}{ccc|c} 0 & 0 & 0 & 0 \end{array}\right]
     $$
   - Apply $R_3 \leftarrow R_3 - R_1$:
     $$
     R_3 - R_1 = \left[\begin{array}{ccc|c} 1 - 1 & -1 - 2 & 2 - (-1) & 0 \end{array}\right] = \left[\begin{array}{ccc|c} 0 & -3 & 3 & 0 \end{array}\right]
     $$
   The matrix becomes:
   $$
   \left[\begin{array}{ccc|c}
   1 & 2 & -1 & 0 \\
   0 & 0 & 0 & 0 \\
   0 & -3 & 3 & 0
   \end{array}\right]
   $$

3. Swap row 2 and row 3, then scale row 2:
   Apply $R_2 \leftrightarrow R_3$:
   $$
   \left[\begin{array}{ccc|c}
   1 & 2 & -1 & 0 \\
   0 & -3 & 3 & 0 \\
   0 & 0 & 0 & 0
   \end{array}\right]
   $$
   Apply $R_2 \leftarrow -\frac{1}{3} R_2$:
   $$
   \left[\begin{array}{ccc|c}
   1 & 2 & -1 & 0 \\
   0 & 1 & -1 & 0 \\
   0 & 0 & 0 & 0
   \end{array}\right]
   $$

4. Identify leading and free variables:
   - Pivots are in Column 1 ($x$) and Column 2 ($y$).
   - Column 3 has no pivot: $z$ is the free variable.
   Set $z = t \in \mathbb{R}$.

5. Back-substitution:
   - From Row 2:
     $$
     y - z = 0 \implies y - t = 0 \implies y = t
     $$
   - From Row 1:
     $$
     x + 2y - z = 0 \implies x + 2(t) - t = 0 \implies x + t = 0 \implies x = -t
     $$

6. Parametric solution:
   $$
   \mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} -t \\ t \\ t \end{pmatrix} = t \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}
   $$

7. Why $(0, 0, 0)$ always satisfies a homogeneous system:
   In any linear equation $a_{i1} x_1 + a_{i2} x_2 + \cdots + a_{in} x_n = 0$, substituting $x_1 = 0, x_2 = 0, \ldots, x_n = 0$ gives:
   $$
   a_{i1}(0) + a_{i2}(0) + \cdots + a_{in}(0) = 0 + 0 + \cdots + 0 = 0
   $$
   In matrix notation, $A \mathbf{0} = \mathbf{0}$ for every linear map $A$, because scaling by scalar 0 always maps any vector to the zero vector: $A(0 \cdot \mathbf{v}) = 0 \cdot A\mathbf{v} = \mathbf{0}$. Therefore, the zero vector $\mathbf{0} = (0, 0, 0)$ is guaranteed to be a solution to any homogeneous system.

---

## Result

$$
\mathbf{x} = t \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}
$$

$$
(0, 0, 0) \text{ always satisfies } A\mathbf{x} = \mathbf{0} \text{ because } A\mathbf{0} = \mathbf{0} \text{ by linearity}
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute $\mathbf{x} = (-t, t, t)$ into the original equations:
- $x + 2y - z = -t + 2t - t = 0$ (holds).
- $2x + 4y - 2z = 2(-t) + 4t - 2t = -2t + 4t - 2t = 0$ (holds).
- $x - y + 2z = -t - t + 2t = 0$ (holds).
All three equations hold for all $t$.

**Pass 2 — Numerical check:** For $t = 1$, test point is $(-1, 1, 1)$:
$-1 + 2(1) - 1 = 0$, $2(-1) + 4(1) - 2(1) = 0$, $-1 - 1 + 2(1) = 0$.
For $t = 0$, test point is $(0, 0, 0)$, which is the trivial solution.

**Pass 3 — Consistency check:** Since $\text{rank}(A) = 2$ and $n = 3$, the null space has dimension $3 - 2 = 1$, which is a line through the origin spanned by $\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$.

---

## Exam tip

A homogeneous system is never inconsistent; it always has at least the trivial solution $\mathbf{0}$, and has non-trivial solutions if and only if $\text{rank}(A) < n$.


# Exercise 8

**Problem:** Solve by elimination the two systems
$$\begin{cases}2x+y=5,\\x-y=1,\end{cases}$$
$$\begin{cases}2x+y=1,\\x-y=4.\end{cases}$$
Compare the successive elimination steps. Which part of the calculation is the same in both cases, and why?

---

## Relevant theorem / definition

The elementary row operations in Gaussian elimination are determined exclusively by the coefficient matrix $A$. When solving multiple systems $A\mathbf{x} = \mathbf{b}_1$ and $A\mathbf{x} = \mathbf{b}_2$ sharing the same matrix $A$, they can be solved simultaneously using a multi-column augmented matrix $[A \mid \mathbf{b}_1 \quad \mathbf{b}_2]$.

---

## Solution

Both systems share the same coefficient matrix:
$$
A = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}
$$
The right-hand side vectors are:
$$
\mathbf{b}_1 = \begin{pmatrix} 5 \\ 1 \end{pmatrix}, \qquad \mathbf{b}_2 = \begin{pmatrix} 1 \\ 4 \end{pmatrix}
$$

Form the simultaneous augmented matrix:
$$
[A \mid \mathbf{b}_1 \quad \mathbf{b}_2] = \left[\begin{array}{cc|cc}
2 & 1 & 5 & 1 \\
1 & -1 & 1 & 4
\end{array}\right]
$$

Step 1: Swap rows 1 and 2 to obtain pivot 1:
Apply $R_1 \leftrightarrow R_2$:
$$
\left[\begin{array}{cc|cc}
1 & -1 & 1 & 4 \\
2 & 1 & 5 & 1
\end{array}\right]
$$

Step 2: Eliminate entry $(2,1)$ via $R_2 \leftarrow R_2 - 2R_1$:
- Left block: $(2 - 2(1), 1 - 2(-1)) = (0, 3)$
- First right column: $5 - 2(1) = 3$
- Second right column: $1 - 2(4) = -7$
The matrix becomes:
$$
\left[\begin{array}{cc|cc}
1 & -1 & 1 & 4 \\
0 & 3 & 3 & -7
\end{array}\right]
$$

Step 3: Solve System 1 (using first right-hand column $\begin{pmatrix} 1 \\ 3 \end{pmatrix}$):
- From row 2:
  $$
  3y = 3 \implies y = 1
  $$
- From row 1:
  $$
  x - y = 1 \implies x - 1 = 1 \implies x = 2
  $$
Solution to System 1: $(x, y) = (2, 1)$.

Step 4: Solve System 2 (using second right-hand column $\begin{pmatrix} 4 \\ -7 \end{pmatrix}$):
- From row 2:
  $$
  3y = -7 \implies y = -\frac{7}{3}
  $$
- From row 1:
  $$
  x - y = 4 \implies x - \left(-\frac{7}{3}\right) = 4 \implies x + \frac{7}{3} = \frac{12}{3} \implies x = \frac{5}{3}
  $$
Solution to System 2: $(x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)$.

Comparison of elimination steps:
- Which part is the same:
  The sequence of row operations (first swapping $R_1 \leftrightarrow R_2$, then subtracting $2R_1$ from $R_2$) and the resulting coefficient matrix $\begin{pmatrix} 1 & -1 \\ 0 & 3 \end{pmatrix}$ are identical in both cases.
- Why:
  Row operations are chosen entirely to create pivots and eliminate entries in the coefficient matrix $A$. The right-hand side vectors undergo the exact same arithmetic transformations passively, without influencing which operations or multipliers are selected.

---

## Result

$$
\text{System 1: } \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}
$$

$$
\text{System 2: } \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \frac{5}{3} \\ -\frac{7}{3} \end{pmatrix}
$$

$$
\text{The coefficient reduction } [A \to U] \text{ is identical because operations depend solely on } A
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute into System 1:
$2(2) + 1 = 5$ (holds), $2 - 1 = 1$ (holds).
Substitute into System 2:
$2(5/3) + (-7/3) = 10/3 - 7/3 = 3/3 = 1$ (holds), $5/3 - (-7/3) = 12/3 = 4$ (holds).

**Pass 2 — Numerical check:** Solve via inverse:
$\det A = 2(-1) - 1(1) = -3 \implies A^{-1} = -\frac{1}{3}\begin{pmatrix} -1 & -1 \\ -1 & 2 \end{pmatrix} = \frac{1}{3}\begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}$.
- $\mathbf{x}_1 = \frac{1}{3}\begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} 5 \\ 1 \end{pmatrix} = \frac{1}{3}\begin{pmatrix} 6 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
- $\mathbf{x}_2 = \frac{1}{3}\begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} 1 \\ 4 \end{pmatrix} = \frac{1}{3}\begin{pmatrix} 5 \\ -7 \end{pmatrix} = \begin{pmatrix} 5/3 \\ -7/3 \end{pmatrix}$.

**Pass 3 — Consistency check:** Both systems have unique solutions because $\det(A) = -3 \neq 0$.

---

## Exam tip

When solving multiple systems with the same coefficient matrix, concatenate their right-hand sides into a single augmented matrix $[A \mid \mathbf{b}_1 \quad \mathbf{b}_2 \cdots]$ to eliminate $A$ once.


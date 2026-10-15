# Exercise 11

**Problem:** Analyze the number of solutions depending on $t$:
$$\begin{cases}x+y+z=1,\\x+ty+z=2,\\x+y+tz=3.\end{cases}$$
Use elimination and separately analyze the parameter values for which a standard calculation step ceases to be valid.

---

## Relevant theorem / definition

In Gaussian elimination with a parameter, whenever dividing by an expression involving the parameter (such as $t - 1$), that expression must be non-zero. The values making the pivot zero must be isolated and evaluated separately to determine whether the system is consistent (infinitely many solutions) or inconsistent (no solution).

---

## Solution

The parameterized system is:
$$
\begin{cases}
x + y + z = 1 \\
x + ty + z = 2 \\
x + y + tz = 3
\end{cases}
$$

Step 1: Set up the augmented matrix:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
1 & t & 1 & 2 \\
1 & 1 & t & 3
\end{array}\right]
$$

Step 2: Eliminate $x$ from rows 2 and 3 using row 1:
- Apply $R_2 \leftarrow R_2 - R_1$:
  $$
  R_2 - R_1 = \left[\begin{array}{ccc|c} 1 - 1 & t - 1 & 1 - 1 & 2 - 1 \end{array}\right] = \left[\begin{array}{ccc|c} 0 & t - 1 & 0 & 1 \end{array}\right]
  $$
- Apply $R_3 \leftarrow R_3 - R_1$:
  $$
  R_3 - R_1 = \left[\begin{array}{ccc|c} 1 - 1 & 1 - 1 & t - 1 & 3 - 1 \end{array}\right] = \left[\begin{array}{ccc|c} 0 & 0 & t - 1 & 2 \end{array}\right]
  $$
The matrix in row echelon form is:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
0 & t - 1 & 0 & 1 \\
0 & 0 & t - 1 & 2
\end{array}\right]
$$

Step 3: Analyze the critical parameter value where the pivot vanishes ($t - 1 = 0 \implies t = 1$):
When $t = 1$, the augmented matrix becomes:
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 2
\end{array}\right]
$$
Row 2 represents $0x + 0y + 0z = 1 \implies 0 = 1$, and Row 3 represents $0 = 2$.
Both are impossible contradictions.
Here $\text{rank}(A) = 1$, but $\text{rank}([A \mid b]) = 2$.
Therefore, for $t = 1$, the system has **no solution** (inconsistent).

Step 4: Analyze $t \neq 1$:
When $t \neq 1$, $t - 1 \neq 0$, so both diagonal pivots are non-zero.
Dividing by $t - 1$ is valid:
- From Row 3:
  $$
  (t - 1)z = 2 \implies z = \frac{2}{t - 1}
  $$
- From Row 2:
  $$
  (t - 1)y = 1 \implies y = \frac{1}{t - 1}
  $$
- From Row 1:
  $$
  x = 1 - y - z = 1 - \frac{1}{t - 1} - \frac{2}{t - 1} = 1 - \frac{3}{t - 1} = \frac{(t - 1) - 3}{t - 1} = \frac{t - 4}{t - 1}
  $$
Because all three pivots are non-zero, $\text{rank}(A) = \text{rank}([A \mid b]) = 3$.
Therefore, for every $t \neq 1$, the system has **exactly one unique solution**:
$$
\mathbf{x} = \begin{pmatrix} \frac{t - 4}{t - 1} \\ \frac{1}{t - 1} \\ \frac{2}{t - 1} \end{pmatrix}
$$

Conclusion on solution types:
- Exactly one solution: for all $t \in \mathbb{R} \setminus \{1\}$.
- No solution: for $t = 1$.
- Infinitely many solutions: does not occur for any value of $t$.

---

## Result

$$
t \neq 1 \implies \text{exactly one unique solution: } \mathbf{x} = \begin{pmatrix} \frac{t - 4}{t - 1} \\ \frac{1}{t - 1} \\ \frac{2}{t - 1} \end{pmatrix}
$$

$$
t = 1 \implies \text{no solution (inconsistent)}
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute the solution for $t \neq 1$ into all three equations:
- $x + y + z = \frac{t-4 + 1 + 2}{t-1} = \frac{t-1}{t-1} = 1$ (holds).
- $x + ty + z = \frac{t-4 + t(1) + 2}{t-1} = \frac{2t - 2}{t-1} = \frac{2(t-1)}{t-1} = 2$ (holds).
- $x + y + tz = \frac{t-4 + 1 + t(2)}{t-1} = \frac{3t - 3}{t-1} = \frac{3(t-1)}{t-1} = 3$ (holds).

**Pass 2 — Numerical check:** Plug in $t = 2$:
$z = \frac{2}{1} = 2, \quad y = \frac{1}{1} = 1, \quad x = \frac{2-4}{1} = -2$.
Check: $-2 + 1 + 2 = 1$ (holds), $-2 + 2(1) + 2 = 2$ (holds), $-2 + 1 + 2(2) = 3$ (holds).

**Pass 3 — Consistency check:** Determinant of the coefficient matrix:
$$
\det(A) = 1 \cdot (t - 1) \cdot (t - 1) = (t - 1)^2
$$
The matrix is singular if and only if $\det(A) = 0 \iff t = 1$, perfectly matching our pivot condition.

---

## Exam tip

Row operations like $R_2 - R_1$ that isolate $(t-1)$ in distinct columns immediately decouple the variables and avoid complicated polynomial division.


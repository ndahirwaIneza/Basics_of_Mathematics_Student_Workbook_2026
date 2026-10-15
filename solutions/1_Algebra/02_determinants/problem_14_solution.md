# Exercise 14

**Problem:** Consider the system $Ax=b$, where
$$A=\begin{pmatrix}1&2\\k&4\end{pmatrix}.$$
For which values of $k$ does the system have exactly one solution for every $b$? For the remaining value, give an example of a right-hand side $b$ for which the system has infinitely many solutions, and an example for which it has no solution.

---

## Relevant theorem / definition

For a square linear system $Ax = b$ with coefficient matrix $A \in \mathbb{R}^{n \times n}$:
1. Unique solution for every $b \iff \det(A) \neq 0$.
2. When $\det(A) = 0$, by the Rouché–Capelli theorem:
   - Infinitely many solutions if $\text{rank}(A) = \text{rank}([A \mid b])$.
   - No solution if $\text{rank}(A) < \text{rank}([A \mid b])$.

---

## Solution

1. Determinant of the coefficient matrix:
   $$
   \det A = 1(4) - 2(k) = 4 - 2k
   $$

2. Condition for exactly one solution for every $b$:
   The system has a unique solution for every right-hand side vector $b$ if and only if $A$ is invertible:
   $$
   \det A \neq 0 \iff 4 - 2k \neq 0 \iff 2k \neq 4 \iff k \neq 2
   $$

3. Analysis of the remaining value $k = 2$:
   When $k = 2$, the matrix is:
   $$
   A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}
   $$
   Notice that Row 2 is $2 \times \text{Row 1}$. The system $Ax = b$ corresponds to equations:
   $$
   \begin{cases} x_1 + 2x_2 = b_1 \\ 2x_1 + 4x_2 = b_2 \end{cases}
   $$

4. Example with infinitely many solutions:
   Choose $b = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, so that $b_2 = 2 b_1$.
   The system is:
   $$
   \begin{cases} x_1 + 2x_2 = 1 \\ 2x_1 + 4x_2 = 2 \end{cases}
   $$
   Applying $R_2 \leftarrow R_2 - 2R_1$ gives the augmented matrix:
   $$
   \left[\begin{array}{cc|c} 1 & 2 & 1 \\ 0 & 0 & 0 \end{array}\right]
   $$
   Here $\text{rank}(A) = \text{rank}([A \mid b]) = 1 < 2$. The equation reduces to $x_1 = 1 - 2x_2$. Setting $x_2 = t$ (free parameter) gives infinitely many solutions:
   $$
   \mathbf{x} = \begin{pmatrix} 1 - 2t \\ t \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -2 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}
   $$

5. Example with no solution:
   Choose $b = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$, so that $b_2 \neq 2 b_1$.
   The system is:
   $$
   \begin{cases} x_1 + 2x_2 = 1 \\ 2x_1 + 4x_2 = 3 \end{cases}
   $$
   Applying $R_2 \leftarrow R_2 - 2R_1$ gives the augmented matrix:
   $$
   \left[\begin{array}{cc|c} 1 & 2 & 1 \\ 0 & 0 & 1 \end{array}\right]
   $$
   Row 2 states $0x_1 + 0x_2 = 1$, which is an impossible contradiction ($0 = 1$). Here $\text{rank}(A) = 1 < 2 = \text{rank}([A \mid b])$, so no solution exists.

---

## Result

$$
\text{Unique solution for every } b \iff k \neq 2
$$

$$
\text{For } k = 2: \quad b = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \implies \text{infinitely many solutions}, \qquad b = \begin{pmatrix} 1 \\ 3 \end{pmatrix} \implies \text{no solution}
$$

---

## Verification

**Pass 1 — Algebraic check:** At $k = 2$, the left-hand side of equation 2 is $2(x_1 + 2x_2)$. Since equation 1 sets $x_1 + 2x_2 = b_1$, the left side evaluates to $2b_1$. Consistency requires $2b_1 = b_2$. When $b = (1, 2)^T$, $2(1) = 2$ holds (consistent). When $b = (1, 3)^T$, $2(1) \neq 3$ fails (contradiction).

**Pass 2 — Numerical check:** For $k = 3 \neq 2$: $\det A = 4 - 2(3) = -2 \neq 0$. The unique solution for $b = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$ is $x = A^{-1}b = -\frac{1}{2}\begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 3 \end{pmatrix} = -\frac{1}{2}\begin{pmatrix} -2 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$. Check: $1 + 2(0) = 1$ and $3(1) + 4(0) = 3$.

**Pass 3 — Consistency check:** For any $2 \times 2$ system, the solution space has dimension $2 - \text{rank}(A)$. At $k = 2$, $\text{rank}(A) = 1$, so the solution space is either empty or a 1-dimensional line.

---

## Exam tip

For $Ax = b$, $\det(A) \neq 0$ guarantees existence and uniqueness; when $\det(A) = 0$, check whether the right-hand side vector satisfies the same linear dependence as the rows of $A$.


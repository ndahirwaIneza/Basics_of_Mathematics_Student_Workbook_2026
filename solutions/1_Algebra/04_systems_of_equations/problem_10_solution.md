# Exercise 10

**Problem:** Find a polynomial $p(x)=ax^2+bx+c$ whose graph passes through $(0,1)$, $(1,3)$, and $(2,9)$. Reduce the problem to a system of equations and check the result by substituting all three points.

---

## Relevant theorem / definition

Polynomial interpolation: for $n+1$ distinct points $(x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)$, there exists a unique polynomial $p(x)$ of degree at most $n$ satisfying $p(x_i) = y_i$. The condition leads to a linear system with a Vandermonde coefficient matrix, which is always invertible when the points $x_i$ are distinct.

---

## Solution

The polynomial is:
$$
p(x) = ax^2 + bx + c
$$

Step 1: Set up the linear equations by evaluating $p(x)$ at each point:
- At point $(0, 1)$:
  $$
  p(0) = a(0)^2 + b(0) + c = 1 \implies c = 1
  $$
- At point $(1, 3)$:
  $$
  p(1) = a(1)^2 + b(1) + c = 3 \implies a + b + c = 3
  $$
- At point $(2, 9)$:
  $$
  p(2) = a(2)^2 + b(2) + c = 9 \implies 4a + 2b + c = 9
  $$

Step 2: Write the system in matrix form:
$$
\begin{pmatrix}
0 & 0 & 1 \\
1 & 1 & 1 \\
4 & 2 & 1
\end{pmatrix}
\begin{pmatrix} a \\ b \\ c \end{pmatrix} =
\begin{pmatrix} 1 \\ 3 \\ 9 \end{pmatrix}
$$

Step 3: Solve the system:
Since $c = 1$ from the first equation, substitute $c = 1$ into equations 2 and 3:
$$
\begin{cases}
a + b + 1 = 3 \implies a + b = 2 \\
4a + 2b + 1 = 9 \implies 4a + 2b = 8 \implies 2a + b = 4
\end{cases}
$$
Subtract the first simplified equation from the second:
$$
(2a + b) - (a + b) = 4 - 2 \implies a = 2
$$
Substitute $a = 2$ back to find $b$:
$$
a + b = 2 \implies 2 + b = 2 \implies b = 0
$$

The coefficients are:
$$
a = 2, \qquad b = 0, \qquad c = 1
$$
The resulting polynomial is:
$$
p(x) = 2x^2 + 1
$$

Step 4: Check by substituting all three points into $p(x)$:
1. Point $(0, 1)$:
   $$
   p(0) = 2(0)^2 + 1 = 0 + 1 = 1 \quad \checkmark
   $$
2. Point $(1, 3)$:
   $$
   p(1) = 2(1)^2 + 1 = 2(1) + 1 = 3 \quad \checkmark
   $$
3. Point $(2, 9)$:
   $$
   p(2) = 2(2)^2 + 1 = 2(4) + 1 = 8 + 1 = 9 \quad \checkmark
   $$
All three points lie on the graph of the polynomial.

---

## Result

$$
a = 2, \quad b = 0, \quad c = 1
$$

$$
p(x) = 2x^2 + 1
$$

---

## Verification

**Pass 1 — Algebraic check:** Lagrange interpolation formula:
$$
\begin{align}
p(x) &= 1 \cdot \frac{(x-1)(x-2)}{(0-1)(0-2)} + 3 \cdot \frac{(x-0)(x-2)}{(1-0)(1-2)} + 9 \cdot \frac{(x-0)(x-1)}{(2-0)(2-1)} \\
&= \frac{1}{2}(x^2 - 3x + 2) - 3(x^2 - 2x) + \frac{9}{2}(x^2 - x) \\
&= \left(\frac{1}{2} - 3 + \frac{9}{2}\right)x^2 + \left(-\frac{3}{2} + 6 - \frac{9}{2}\right)x + 1 \\
&= 2x^2 + 0x + 1 = 2x^2 + 1
\end{align}
$$
Lagrange interpolation confirms the exact same polynomial.

**Pass 2 — Numerical check:** Vandermonde determinant for nodes $x = (0, 1, 2)$:
$$
\det(V) = (x_2 - x_1)(x_3 - x_1)(x_3 - x_2) = (1 - 0)(2 - 0)(2 - 1) = 1 \cdot 2 \cdot 1 = 2 \neq 0
$$
Because the determinant is non-zero, the solution is unique.

**Pass 3 — Consistency check:** Since $p(x)$ is an even function ($b = 0$), $p(-1) = p(1) = 3$ and $p(-2) = p(2) = 9$, which is consistent with the symmetry about the $y$-axis.

---

## Exam tip

Evaluating the polynomial at $x = 0$ directly reveals the constant term $c$, simplifying the remaining problem to a $2 \times 2$ system in $a$ and $b$.


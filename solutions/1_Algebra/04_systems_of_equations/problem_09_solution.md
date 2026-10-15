# Exercise 9

**Problem:** Find numbers $x,y$ satisfying
$$x+y=10,\qquad 2x+5y=32.$$
Solve the system and explain geometrically why the solution is unique.

---

## Relevant theorem / definition

A system of two linear equations in two unknowns represents two lines in the Cartesian plane $\mathbb{R}^2$.
1. If the lines have different slopes, they intersect at exactly one point (unique solution).
2. If they have the same slope and different intercepts, they are distinct parallel lines (no solution).
3. If they have the same slope and identical intercepts, they coincide (infinitely many solutions).

---

## Solution

The system of equations is:
$$
\begin{cases}
x + y = 10 \\
2x + 5y = 32
\end{cases}
$$

1. Solving the system using elimination:
   Set up the augmented matrix:
   $$
   \left[\begin{array}{cc|c}
   1 & 1 & 10 \\
   2 & 5 & 32
   \end{array}\right]
   $$
   Eliminate $x$ from Row 2 by applying $R_2 \leftarrow R_2 - 2R_1$:
   $$
   R_2 - 2R_1 = \left[\begin{array}{cc|c} 2 - 2(1) & 5 - 2(1) & 32 - 2(10) \end{array}\right] = \left[\begin{array}{cc|c} 0 & 3 & 12 \end{array}\right]
   $$
   The resulting system is:
   $$
   \left[\begin{array}{cc|c}
   1 & 1 & 10 \\
   0 & 3 & 12
   \end{array}\right]
   $$
   Back-substitution:
   - From Row 2:
     $$
     3y = 12 \implies y = 4
     $$
   - From Row 1:
     $$
     x + y = 10 \implies x + 4 = 10 \implies x = 6
     $$
   The solution is $(x, y) = (6, 4)$.

2. Geometric explanation of uniqueness:
   Convert each linear equation into slope-intercept form ($y = mx + c$):
   - First line ($L_1$):
     $$
     x + y = 10 \implies y = -x + 10
     $$
     The slope of $L_1$ is $m_1 = -1$, and its $y$-intercept is $(0, 10)$.
   - Second line ($L_2$):
     $$
     2x + 5y = 32 \implies 5y = -2x + 32 \implies y = -\frac{2}{5}x + \frac{32}{5}
     $$
     The slope of $L_2$ is $m_2 = -\frac{2}{5} = -0.4$, and its $y$-intercept is $(0, 6.4)$.
   
   Because $m_1 = -1 \neq -\frac{2}{5} = m_2$, the two slopes are unequal. In two-dimensional Euclidean geometry, any two straight lines with distinct slopes are non-parallel and must intersect at exactly one single point. That unique intersection point is $(6, 4)$.

---

## Result

$$
x = 6, \qquad y = 4
$$

$$
(x, y) = (6, 4)
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute $(6, 4)$ into the original equations:
- Equation 1: $6 + 4 = 10$ (holds).
- Equation 2: $2(6) + 5(4) = 12 + 20 = 32$ (holds).
Both equations are verified.

**Pass 2 — Numerical check:** Determinant of the coefficient matrix:
$$
\det(A) = \det\begin{pmatrix} 1 & 1 \\ 2 & 5 \end{pmatrix} = 1(5) - 1(2) = 5 - 2 = 3 \neq 0
$$
Since $\det(A) \neq 0$, the coefficient matrix is invertible and Cramer's rule confirms uniqueness.

**Pass 3 — Consistency check:** Intersection of lines: at $x = 6$, $y_1 = -6 + 10 = 4$, and $y_2 = -\frac{2}{5}(6) + \frac{32}{5} = \frac{-12 + 32}{5} = \frac{20}{5} = 4$. Both lines pass through $(6, 4)$.

---

## Exam tip

For a $2 \times 2$ system, comparing the slopes of the two lines immediately tells you whether a unique intersection exists ($m_1 \neq m_2$).


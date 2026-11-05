# Exercise 8

**Problem:** Reduce

$$
x^2+y^2+z^2-4x+2y-6z-2=0
$$

to canonical form. Find the center and radius. Give two points on the sphere and check them in the equation.

---

## Relevant theorem / definition

The canonical equation of a sphere in $\mathbb{R}^3$ with center $(x_0, y_0, z_0)$ and radius $R > 0$ is:

$$
(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = R^2
$$

A general second-degree equation with equal quadratic coefficients $x^2 + y^2 + z^2 + Dx + Ey + Fz + G = 0$ is reduced to canonical form by completing the square in each of the three variables independently.

---

## Solution

1. Group the terms by variable:

$$
(x^2 - 4x) + (y^2 + 2y) + (z^2 - 6z) - 2 = 0
$$

2. Complete the square for each variable:

$$
x^2 - 4x = (x - 2)^2 - 4
$$

$$
y^2 + 2y = (y + 1)^2 - 1
$$

$$
z^2 - 6z = (z - 3)^2 - 9
$$

3. Substitute the completed squares into the equation:

$$
\begin{align}
(x - 2)^2 - 4 + (y + 1)^2 - 1 + (z - 3)^2 - 9 - 2 &= 0 \\
(x - 2)^2 + (y + 1)^2 + (z - 3)^2 - 16 &= 0 \\
(x - 2)^2 + (y + 1)^2 + (z - 3)^2 &= 16
\end{align}
$$

4. Identify center and radius:
   - Center: $S = (x_0, y_0, z_0) = (2, -1, 3)$
   - Radius: $R = \sqrt{16} = 4$

5. Select two simple points on the sphere:
   - Shift from the center along the $x$-axis by $+R = 4$:

$$
P_1 = (2 + 4, -1, 3) = (6, -1, 3)
$$

   - Shift from the center along the $y$-axis by $+R = 4$:

$$
P_2 = (2, -1 + 4, 3) = (2, 3, 3)
$$

6. Check $P_1(6, -1, 3)$ in both forms:
   - Canonical form:

$$
(6 - 2)^2 + (-1 + 1)^2 + (3 - 3)^2 = 4^2 + 0^2 + 0^2 = 16
$$

   - Original general form:

$$
\begin{align}
6^2 + (-1)^2 + 3^2 - 4(6) + 2(-1) - 6(3) - 2 &= 36 + 1 + 9 - 24 - 2 - 18 - 2 \\
&= 46 - 46 = 0
\end{align}
$$

7. Check $P_2(2, 3, 3)$ in both forms:
   - Canonical form:

$$
(2 - 2)^2 + (3 + 1)^2 + (3 - 3)^2 = 0^2 + 4^2 + 0^2 = 16
$$

   - Original general form:

$$
\begin{align}
2^2 + 3^2 + 3^2 - 4(2) + 2(3) - 6(3) - 2 &= 4 + 9 + 9 - 8 + 6 - 18 - 2 \\
&= 28 - 28 = 0
\end{align}
$$

---

## Result

$$
(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16
$$

$$
\text{Center: } (2, -1, 3), \qquad \text{Radius: } R = 4
$$

$$
\text{Points on the sphere: } P_1(6, -1, 3) \quad \text{and} \quad P_2(2, 3, 3)
$$

---

## Verification

**Pass 1 — Algebraic check:** Expand the canonical equation back into general form:

$$
\begin{align}
(x^2 - 4x + 4) + (y^2 + 2y + 1) + (z^2 - 6z + 9) &= 16 \\
x^2 + y^2 + z^2 - 4x + 2y - 6z + 14 - 16 &= 0 \\
x^2 + y^2 + z^2 - 4x + 2y - 6z - 2 &= 0
\end{align}
$$

The expansion matches the original polynomial identically.

**Pass 2 — Numerical check:** Test the point $P_3(2, -1, 7)$ (shifted by $+R$ along the $z$-axis):

$$
2^2 + (-1)^2 + 7^2 - 4(2) + 2(-1) - 6(7) - 2 = 4 + 1 + 49 - 8 - 2 - 42 - 2 = 54 - 54 = 0
$$

**Pass 3 — Consistency check:** Use the radius invariant formula $R^2 = x_0^2 + y_0^2 + z_0^2 - G$:

$$
R^2 = 2^2 + (-1)^2 + 3^2 - (-2) = 4 + 1 + 9 + 2 = 16 \implies R = 4
$$

This directly confirms the arithmetic.

---

## Exam tip

The center coordinates are obtained instantly by halving the coefficients of the linear terms and reversing their signs: $x_0 = -(-4)/2 = 2$, $y_0 = -(2)/2 = -1$, and $z_0 = -(-6)/2 = 3$.

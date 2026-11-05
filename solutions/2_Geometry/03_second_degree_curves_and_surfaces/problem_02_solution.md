# Exercise 2

**Problem:** Reduce

$$
x^2+y^2-6x+4y-3=0
$$

to canonical form. Find the center and radius, then substitute two simple points from the circle into both forms of the equation.

---

## Relevant theorem / definition

The canonical equation of a circle in $\mathbb{R}^2$ with center $(x_0, y_0)$ and radius $R > 0$ is:

$$
(x - x_0)^2 + (y - y_0)^2 = R^2
$$

Any quadratic equation of the form $x^2 + y^2 + Dx + Ey + F = 0$ can be reduced to this form by completing the square in both variables.

---

## Solution

1. Group the quadratic and linear terms by variable:

$$
(x^2 - 6x) + (y^2 + 4y) - 3 = 0
$$

2. Complete the square for the $x$-terms:

$$
x^2 - 6x = (x - 3)^2 - 3^2 = (x - 3)^2 - 9
$$

3. Complete the square for the $y$-terms:

$$
y^2 + 4y = (y + 2)^2 - 2^2 = (y + 2)^2 - 4
$$

4. Substitute these expressions back into the equation:

$$
\begin{align}
(x - 3)^2 - 9 + (y + 2)^2 - 4 - 3 &= 0 \\
(x - 3)^2 + (y + 2)^2 - 16 &= 0 \\
(x - 3)^2 + (y + 2)^2 &= 16
\end{align}
$$

5. Extract the geometric parameters:
   - Center: $(x_0, y_0) = (3, -2)$
   - Radius: $R = \sqrt{16} = 4$

6. Choose two simple points on the circle:
   - Let $y = -2$: $(x - 3)^2 + 0 = 16 \implies x - 3 = 4 \implies x = 7$. Point $P_1 = (7, -2)$.
   - Let $x = 3$: $0 + (y + 2)^2 = 16 \implies y + 2 = 4 \implies y = 2$. Point $P_2 = (3, 2)$.

7. Substitute $P_1 = (7, -2)$ into both forms:
   - Canonical form:

$$
(7 - 3)^2 + (-2 + 2)^2 = 4^2 + 0^2 = 16
$$

   - General form:

$$
7^2 + (-2)^2 - 6(7) + 4(-2) - 3 = 49 + 4 - 42 - 8 - 3 = 53 - 53 = 0
$$

8. Substitute $P_2 = (3, 2)$ into both forms:
   - Canonical form:

$$
(3 - 3)^2 + (2 + 2)^2 = 0^2 + 4^2 = 16
$$

   - General form:

$$
3^2 + 2^2 - 6(3) + 4(2) - 3 = 9 + 4 - 18 + 8 - 3 = 21 - 21 = 0
$$

---

## Result

$$
(x - 3)^2 + (y + 2)^2 = 16
$$

$$
\text{Center: } (3, -2), \qquad \text{Radius: } R = 4
$$

$$
\text{Test points: } P_1(7, -2) \text{ and } P_2(3, 2) \text{ satisfy both forms}
$$

---

## Verification

**Pass 1 — Algebraic check:** Expand the canonical equation $(x - 3)^2 + (y + 2)^2 = 16$: $(x^2 - 6x + 9) + (y^2 + 4y + 4) = 16 \iff x^2 + y^2 - 6x + 4y + 13 - 16 = 0 \iff x^2 + y^2 - 6x + 4y - 3 = 0$, exactly matching the original equation.

**Pass 2 — Numerical check:** Test the opposite extremities: $P_3 = (3 - 4, -2) = (-1, -2)$ gives $(-1)^2 + (-2)^2 - 6(-1) + 4(-2) - 3 = 1 + 4 + 6 - 8 - 3 = 0$. $P_4 = (3, -2 - 4) = (3, -6)$ gives $3^2 + (-6)^2 - 6(3) + 4(-6) - 3 = 9 + 36 - 18 - 24 - 3 = 0$.

**Pass 3 — Consistency check:** The formula $R^2 = x_0^2 + y_0^2 - F$ gives $R^2 = 3^2 + (-2)^2 - (-3) = 9 + 4 + 3 = 16$, which confirms $R = 4$.

---

## Exam tip

When completing the square, remember that the constant to add to the right-hand side is $(D/2)^2 + (E/2)^2 - F$; keeping signs straight on $F$ avoids erroneous imaginary radii.

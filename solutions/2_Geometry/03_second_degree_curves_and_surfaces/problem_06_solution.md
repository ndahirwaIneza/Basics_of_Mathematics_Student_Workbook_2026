# Exercise 6

**Problem:** Reduce

$$
4x^2+9y^2-16x+18y-11=0
$$

to canonical form. Give the center and semiaxis lengths. Check that substituting the coordinates of the center into the left-hand side gives a value consistent with the form you obtained.

---

## Relevant theorem / definition

The canonical equation of an ellipse with center $(x_0, y_0)$ and axes parallel to the coordinate axes is:

$$
\frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1
$$

where $a > 0$ and $b > 0$ are the horizontal and vertical semiaxis lengths. The center $(x_0, y_0)$ corresponds to the critical point of the quadratic polynomial $F(x, y) = Ax^2 + Cy^2 + Dx + Ey + F$.

---

## Solution

1. Group the terms by variable and factor out the leading coefficients:

$$
4(x^2 - 4x) + 9(y^2 + 2y) - 11 = 0
$$

2. Complete the square inside each parenthesis:
   - For $x$: $x^2 - 4x = (x - 2)^2 - 4$
   - For $y$: $y^2 + 2y = (y + 1)^2 - 1$

3. Substitute the completed squares back into the equation:

$$
\begin{align}
4\left[(x - 2)^2 - 4\right] + 9\left[(y + 1)^2 - 1\right] - 11 &= 0 \\
4(x - 2)^2 - 16 + 9(y + 1)^2 - 9 - 11 &= 0 \\
4(x - 2)^2 + 9(y + 1)^2 - 36 &= 0 \\
4(x - 2)^2 + 9(y + 1)^2 &= 36
\end{align}
$$

4. Divide both sides by $36$:

$$
\frac{4(x - 2)^2}{36} + \frac{9(y + 1)^2}{36} = 1 \implies \frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1
$$

5. Extract the geometric features:
   - Center: $(x_0, y_0) = (2, -1)$
   - Semiaxis along $x$: $a = \sqrt{9} = 3$
   - Semiaxis along $y$: $b = \sqrt{4} = 2$

6. Consistency check at the center:
   Evaluate the left-hand side polynomial $F(x, y) = 4x^2 + 9y^2 - 16x + 18y - 11$ at $(2, -1)$:

$$
\begin{align}
F(2, -1) &= 4(2)^2 + 9(-1)^2 - 16(2) + 18(-1) - 11 \\
&= 4(4) + 9(1) - 32 - 18 - 11 \\
&= 16 + 9 - 32 - 18 - 11 \\
&= 25 - 61 = -36
\end{align}
$$

   In terms of completed squares, $F(x,y) = 4(x-2)^2 + 9(y+1)^2 - 36$. When evaluated at the center $(2,-1)$, both quadratic terms vanish identically ($0 + 0 - 36 = -36$). Setting $F(x,y) = 0$ is therefore equivalent to $4(x-2)^2 + 9(y+1)^2 = 36$, perfectly matching the obtained value.

---

## Result

$$
\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1
$$

$$
\text{Center: } (2, -1), \qquad \text{Semiaxis lengths: } a = 3, \quad b = 2
$$

$$
F(2, -1) = -36 \iff 4(x-2)^2 + 9(y+1)^2 = 36
$$

---

## Verification

**Pass 1 — Algebraic check:** Expand the canonical form $\frac{(x-2)^2}{9} + \frac{(y+1)^2}{4} = 1$:

$$
4(x^2 - 4x + 4) + 9(y^2 + 2y + 1) = 36 \iff 4x^2 - 16x + 16 + 9y^2 + 18y + 9 - 36 = 0 \iff 4x^2 + 9y^2 - 16x + 18y - 11 = 0
$$

**Pass 2 — Numerical check:** Test the vertex $P(5, -1)$ (shifted by $a=3$ along $x$):

$$
F(5, -1) = 4(25) + 9(1) - 16(5) + 18(-1) - 11 = 100 + 9 - 80 - 18 - 11 = 109 - 109 = 0
$$

Test the vertex $Q(2, 1)$ (shifted by $b=2$ along $y$):

$$
F(2, 1) = 4(4) + 9(1) - 16(2) + 18(1) - 11 = 16 + 9 - 32 + 18 - 11 = 43 - 43 = 0
$$

**Pass 3 — Consistency check:** The partial derivatives $\frac{\partial F}{\partial x} = 8x - 16 = 0 \implies x = 2$ and $\frac{\partial F}{\partial y} = 18y + 18 = 0 \implies y = -1$ independently yield the center $(2, -1)$.

---

## Exam tip

Before completing the square, always factor the leading coefficient completely outside each grouping: $4(x^2 - 4x)$ prevents mistakenly writing $(4x - 8)^2$.

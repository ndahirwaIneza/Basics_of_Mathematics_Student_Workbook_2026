# Exercise 10

**Problem:** For
$$f(x)=x^2-3x+1$$
find the equation of the tangent line at the point with $x=2$. Give the point of tangency, the value $f'(2)$, the equation of the line, and verify that the point lies on the obtained tangent line.

---

## Relevant theorem / definition

The tangent line to the graph of a differentiable function $y = f(x)$ at the point $(x_0, y_0) = (x_0, f(x_0))$ has slope $m = f'(x_0)$. The point-slope equation of the tangent line is:
$$
y - y_0 = f'(x_0)(x - x_0) \iff y = f'(x_0)(x - x_0) + f(x_0)
$$

---

## Solution

1. Find the point of tangency:
   Given $x_0 = 2$, evaluate $f(2)$:
   $$
   y_0 = f(2) = 2^2 - 3(2) + 1 = 4 - 6 + 1 = -1.
   $$
   The point of tangency is $P(2, -1)$.

2. Compute $f'(x)$ and $f'(2)$:
   Differentiate $f(x)$ using the power rule:
   $$
   f'(x) = 2x - 3.
   $$
   Evaluate at $x = 2$:
   $$
   f'(2) = 2(2) - 3 = 4 - 3 = 1.
   $$
   The slope of the tangent line is $m = 1$.

3. Write the equation of the tangent line:
   Substitute $x_0 = 2$, $y_0 = -1$, and $m = 1$ into the point-slope form:
   \begin{align}
   y - (-1) &= 1(x - 2) \\
   y + 1 &= x - 2 \\
   y &= x - 3.
   \end{align}

4. Verify that the point of tangency lies on the obtained tangent line:
   Substitute $x = 2$ into the line equation $y = x - 3$:
   $$
   y = 2 - 3 = -1.
   $$
   The resulting value matches $y_0 = f(2) = -1$. Hence, the point $P(2, -1)$ lies on the tangent line.

---

## Result

$$
\text{Point of tangency: } P(2, -1)
$$

$$
f'(2) = 1
$$

$$
\text{Tangent line equation: } y = x - 3
$$

$$
\text{Point verification: } y(2) = 2 - 3 = -1 = f(2) \quad (\text{point lies on line})
$$

---

## Verification

**Pass 1 — Algebraic check:** Solve for the intersection of the parabola $y = x^2 - 3x + 1$ and the tangent line $y = x - 3$:
$$
x^2 - 3x + 1 = x - 3 \iff x^2 - 4x + 4 = 0 \iff (x - 2)^2 = 0
$$
The equation has a single root $x = 2$ with multiplicity 2 (a double root). In algebraic geometry, a line intersects a quadratic curve with multiplicity 2 if and only if it is tangent to the curve at that point.

**Pass 2 — Numerical check:** Check the vertical difference between the curve and the tangent line near $x = 2$:
At $x = 2.1$:
$f(2.1) = (2.1)^2 - 3(2.1) + 1 = 4.41 - 6.30 + 1 = -0.89$.
Tangent line at $x = 2.1$:
$y(2.1) = 2.1 - 3 = -0.90$.
The difference is $f(2.1) - y(2.1) = -0.89 - (-0.90) = 0.01 = (2.1 - 2)^2$, exactly matching the Taylor remainder $\frac{f''(2)}{2}(x-2)^2 = \frac{2}{2}(0.1)^2 = 0.01$.

**Pass 3 — Consistency check:** The parabola $f(x) = x^2 - 3x + 1$ has its vertex at $x_v = -\frac{b}{2a} = \frac{3}{2} = 1.5$. For $x > 1.5$, the parabola is increasing, which requires the tangent slope to be positive. At $x = 2 > 1.5$, $m = 1 > 0$, consistent with the geometry.

---

## Exam tip

Find both coordinates of the point $(x_0, f(x_0))$ first before substituting into $y - y_0 = m(x - x_0)$ to prevent sign errors in the constant term.

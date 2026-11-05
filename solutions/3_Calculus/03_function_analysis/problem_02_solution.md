# Exercise 2

**Problem:** For $f(x)=x^2-4x+1$, find the minimum using the derivative. Compare the result with the vertex form and explain why both approaches lead to the same point.

---

## Relevant theorem / definition

1. First derivative condition for extrema: If a differentiable function $f$ attains a local extremum at $c$, then $f'(c) = 0$. For a convex quadratic function ($a > 0$), the unique critical point is the global minimum.
2. Vertex form of a quadratic: Any quadratic $f(x) = ax^2 + bx + c$ can be written in vertex form:

$$
   f(x) = a(x - p)^2 + q
$$

   where $p = -\frac{b}{2a}$ and $q = f(p) = -\frac{\Delta}{4a}$. When $a > 0$, the square $(x - p)^2 \ge 0$ is minimized when $x = p$, giving the minimum value $q$.

---

## Solution

1. Finding the minimum using the derivative:
   Compute the first derivative of $f(x) = x^2 - 4x + 1$:

$$
   f'(x) = 2x - 4
$$

   Set the derivative to zero to find the critical point:

$$
   2x - 4 = 0 \implies 2x = 4 \implies x = 2
$$

   Compute the second derivative:

$$
   f''(x) = 2 > 0
$$

   Because $f''(x) > 0$ for all $x \in \mathbb{R}$, $f$ is strictly convex everywhere, and $x = 2$ corresponds to a global minimum.
   Compute the function value at $x = 2$:

$$
   f(2) = 2^2 - 4(2) + 1 = 4 - 8 + 1 = -3
$$

   The minimum point is $(2, -3)$, with minimum value $-3$.

2. Finding the vertex form by completing the square:
   Group the quadratic and linear terms:

$$
   \begin{align}
   f(x) &= (x^2 - 4x) + 1 \\
   &= (x^2 - 4x + 4) - 4 + 1 \\
   &= (x - 2)^2 - 3
   \end{align}
$$

   In standard vertex form $a(x - p)^2 + q$, we have $a = 1$, $p = 2$, and $q = -3$.
   Since $(x - 2)^2 \ge 0$ for all $x \in \mathbb{R}$, with equality if and only if $x = 2$:

$$
   f(x) = (x - 2)^2 - 3 \ge 0 - 3 = -3
$$

   The minimum occurs at $x = 2$ and equals $-3$, giving the vertex $(2, -3)$.

3. Comparison and explanation of equivalence:
   Both methods identify the exact same point $(2, -3)$.
   - Geometrical connection:
     The graph of $f(x) = a(x - p)^2 + q$ is an upward-opening parabola with vertical axis of symmetry $x = p$. At the vertex, the tangent line is completely horizontal (slope zero).
   - Analytical connection:
     Differentiating the general vertex form with respect to $x$ yields:

$$
     \frac{d}{dx}\left[a(x - p)^2 + q\right] = 2a(x - p)
$$

     Setting the derivative equal to zero gives:

$$
     2a(x - p) = 0 \implies x = p
$$

     Since $a \neq 0$, the algebraic condition minimizing the squared distance $(x - p)^2 = 0$ is identical to the calculus condition of a horizontal tangent $f'(x) = 0$.

---

## Result

$$
\text{Minimum point: } (2, -3), \qquad \text{Minimum value: } f(2) = -3
$$

$$
\text{Vertex form: } f(x) = (x - 2)^2 - 3
$$

---

## Verification

**Pass 1 — Algebraic check:** Use the standard vertex formula $p = -\frac{b}{2a}$: for $a = 1, b = -4, c = 1$, we have $p = -\frac{-4}{2(1)} = 2$, and $q = c - \frac{b^2}{4a} = 1 - \frac{16}{4} = -3$. Both match $x = 2, y = -3$.

**Pass 2 — Numerical check:** Test points symmetrically placed around $x = 2$: $f(1) = 1^2 - 4(1) + 1 = -2 > -3$, and $f(3) = 3^2 - 4(3) + 1 = -2 > -3$. The symmetry $f(2 - h) = f(2 + h) = h^2 - 3 > -3$ holds for any $h \neq 0$.

**Pass 3 — Consistency check:** The discriminant is $\Delta = b^2 - 4ac = (-4)^2 - 4(1)(1) = 12 > 0$. Two real roots exist at $x = \frac{4 \pm \sqrt{12}}{2} = 2 \pm \sqrt{3}$. The midpoint of the roots is $\frac{(2 - \sqrt{3}) + (2 + \sqrt{3})}{2} = 2$, which coincides with the critical point $x = 2$.

---

## Exam tip

For any quadratic $ax^2 + bx + c$, setting the derivative $2ax + b = 0$ provides the fastest derivation of the vertex formula $x = -\frac{b}{2a}$.

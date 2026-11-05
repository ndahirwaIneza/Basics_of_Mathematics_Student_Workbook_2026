# Exercise 6

**Problem:** Compute the average value of the function

$$
f(x)=x^2
$$

on the interval $[0,3]$.

Find a point $c\in[0,3]$ for which $f(c)$ is equal to this average value, and interpret the result geometrically.

---

## Relevant theorem / definition

The average value (mean value) of an integrable function $f$ on an interval $[a, b]$ is defined by:

$$
f_{\text{avg}} = \frac{1}{b - a} \int_a^b f(x)\,dx
$$

By the Mean Value Theorem for Integrals, if $f$ is continuous on $[a, b]$, there exists at least one point $c \in [a, b]$ such that:

$$
f(c) = f_{\text{avg}} \iff \int_a^b f(x)\,dx = f(c)(b - a)
$$

---

## Solution

1. Average value of $f(x) = x^2$ on $[0, 3]$:
   Apply the average value formula with $a = 0$ and $b = 3$:

   $$
   \begin{align}
   f_{\text{avg}} &= \frac{1}{3 - 0} \int_0^3 x^2\,dx \\
   &= \frac{1}{3} \left[ \frac{x^3}{3} \right]_0^3 \\
   &= \frac{1}{3} \left( \frac{3^3}{3} - 0 \right) \\
   &= \frac{1}{3} \cdot 9 \\
   &= 3
   \end{align}
   $$

2. Determination of the point $c \in [0, 3]$:
   Set $f(c) = f_{\text{avg}}$:

   $$
   c^2 = 3
   $$

   Solving for $c$:

   $$
   c = \pm\sqrt{3}
   $$

   Because the interval is $[0, 3]$, we retain only the positive solution:

   $$
   c = \sqrt{3} \approx 1.732 \in [0, 3]
   $$

3. Geometric interpretation:
   The total area under the parabola $y = x^2$ from $x = 0$ to $x = 3$ is:

   $$
   \int_0^3 x^2\,dx = 9
   $$

   A rectangle constructed on the same base interval $[0, 3]$ with constant height equal to the average value $f_{\text{avg}} = 3$ has area:

   $$
   \text{Area}_{\text{rect}} = \text{base} \times \text{height} = (3 - 0) \times 3 = 9
   $$

   Thus, the area under the parabolic curve equals the area of this rectangle.
   The point $c = \sqrt{3}$ is the coordinate at which the curve $y = x^2$ intersects the top horizontal boundary of this rectangle ($y = 3$). The "excess" area where the parabola rises above the horizontal level $y = 3$ (on $[\sqrt{3}, 3]$) exactly equals the "deficit" area below the level $y = 3$ (on $[0, \sqrt{3}]$).

---

## Result

$$
f_{\text{avg}} = 3
$$

$$
c = \sqrt{3} \approx 1.732
$$

$$
\int_0^3 x^2\,dx = f(c) \cdot (3 - 0) = 3 \times 3 = 9
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the deficit and excess areas directly:
- Deficit area on $[0, \sqrt{3}]$:

$$
\int_0^{\sqrt{3}} (3 - x^2)\,dx = \left[ 3x - \frac{x^3}{3} \right]_0^{\sqrt{3}} = 3\sqrt{3} - \frac{3\sqrt{3}}{3} = 2\sqrt{3}
$$

- Excess area on $[\sqrt{3}, 3]$:

$$
\int_{\sqrt{3}}^3 (x^2 - 3)\,dx = \left[ \frac{x^3}{3} - 3x \right]_{\sqrt{3}}^3 = (9 - 9) - \left(\sqrt{3} - 3\sqrt{3}\right) = 2\sqrt{3}
$$

The deficit and excess areas are identical, confirming $c = \sqrt{3}$.

**Pass 2 — Numerical check:** The function values at endpoints are $f(0) = 0$ and $f(3) = 9$. For a convex function ($f''(x) = 2 > 0$), the average value must be strictly less than the arithmetic average of endpoints:

$$
f_{\text{avg}} = 3 < \frac{f(0) + f(3)}{2} = \frac{0 + 9}{2} = 4.5
$$

This matches convexity theory.

**Pass 3 — Consistency check:** Since $f$ is strictly increasing on $[0, 3]$ from 0 to 9, the Intermediate Value Theorem guarantees a unique $c \in (0, 3)$ where $f(c) = 3$. That value is $\sqrt{3} \approx 1.732$, which lies inside $(0, 3)$.

---

## Exam tip

Do not forget the factor $\frac{1}{b - a}$ in front of the integral; the average value represents the average height, not the total area.

# Exercise 4

**Problem:** Find the area of the region bounded by the graphs

$$
y=x
$$

and

$$
y=x^2.
$$

First find the intersection points and justify which function is greater on the relevant interval.

---

## Relevant theorem / definition

The area of a planar region bounded above by $y = f(x)$ and below by $y = g(x)$ on an interval $[a, b]$, where $f(x) \ge g(x)$, is given by the definite integral:

$$
A = \int_a^b \left(f(x) - g(x)\right)\,dx
$$

---

## Solution

1. Intersection points:
   Set the two equations equal to find the points of intersection:

   $$
   x^2 = x
   $$

   Rearrange into standard polynomial form:

   $$
   x^2 - x = 0 \implies x(x - 1) = 0
   $$

   This yields two solutions:

   $$
   x_1 = 0, \qquad x_2 = 1
   $$

   Substituting into $y = x$ gives the intersection points:

   $$
   (0, 0) \quad \text{and} \quad (1, 1)
   $$

2. Ordering of functions on $(0, 1)$:
   Examine the sign of the difference $d(x) = x - x^2$ on the open interval $(0, 1)$:

   $$
   d(x) = x(1 - x)
   $$

   For every $x \in (0, 1)$, both factors are strictly positive: $x > 0$ and $1 - x > 0$. Therefore:

   $$
   x - x^2 > 0 \implies x > x^2 \quad \text{for all } x \in (0, 1)
   $$

   Thus, the upper boundary curve is $f(x) = x$ and the lower boundary curve is $g(x) = x^2$.

3. Area computation:
   Set up and evaluate the definite integral from $x = 0$ to $x = 1$:

   $$
   \begin{align}
   A &= \int_0^1 \left(x - x^2\right)\,dx \\
   &= \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1 \\
   &= \left(\frac{1}{2} - \frac{1}{3}\right) - (0 - 0) \\
   &= \frac{1}{6}
   \end{align}
   $$

---

## Result

$$
\text{Intersection points: } (0, 0), \quad (1, 1)
$$

$$
x > x^2 \quad \text{on } (0, 1)
$$

$$
A = \frac{1}{6}
$$

---

## Verification

**Pass 1 — Algebraic check:** Integrating with respect to $y$: the curves are $x = y$ and $x = \sqrt{y}$ for $y \in [0, 1]$. Since $\sqrt{y} \ge y$, the horizontal strip integral is:

$$
A = \int_0^1 \left(\sqrt{y} - y\right)\,dy = \left[ \frac{2}{3}y^{3/2} - \frac{y^2}{2} \right]_0^1 = \frac{2}{3} - \frac{1}{2} = \frac{1}{6}
$$

Integrating along $y$ yields the identical area.

**Pass 2 — Numerical check:** The region lies entirely inside the unit square $[0, 1] \times [0, 1]$, which has area 1. The lower triangle under $y = x$ has area $\frac{1}{2}$, and the parabolic area under $y = x^2$ is $\int_0^1 x^2\,dx = \frac{1}{3}$. Subtracting the parabolic area from the triangle area gives $\frac{1}{2} - \frac{1}{3} = \frac{1}{6} \approx 0.1667$.

**Pass 3 — Consistency check:** At the midpoint $x = 0.5$, the vertical height is $0.5 - 0.25 = 0.25$. A midpoint Riemann approximation with 1 subinterval gives $1 \times 0.25 = 0.25$; a trapezoidal/Simpson comparison confirms $\frac{1}{6}$ is strictly between 0 and 0.25, consistent with a concave upper boundary $d(x)$.

---

## Exam tip

Always evaluate a test point such as $x = \frac{1}{2}$ into $f(x) - g(x)$ before setting up the integral to ensure the integrand is non-negative and the area will be positive.

# Exercise 2

**Problem:** A rectangle has perimeter $40$.

1. Write its area as a function of the length of one side.
2. Determine the domain of this function resulting from the geometry of the problem.
3. Find the dimensions that give the maximum area.
4. Justify that the point found actually gives a maximum.

---

## Relevant theorem / definition

For a rectangle with side lengths $x$ and $y$, perimeter is $P = 2x + 2y$ and area is $A = xy$. A differentiable function $A(x)$ on an open interval has an interior local extremum only at critical points where $A'(x) = 0$. By the second derivative test, if $A'(x_0) = 0$ and $A''(x_0) < 0$, then $x_0$ is a local maximum; if $A''(x) < 0$ on the entire domain, $x_0$ is the unique global maximum.

---

## Solution

1. Area as a function of one side length:
   Let $x$ denote the length of one side and $y$ denote the length of the adjacent side.
   The perimeter constraint gives:

   $$
   2x + 2y = 40 \implies x + y = 20 \implies y = 20 - x
   $$

   Substitute $y$ into the area formula:

   $$
   A(x) = x(20 - x) = 20x - x^2
   $$

2. Geometric domain:
   Both side lengths must be strictly positive:

   $$
   x > 0 \quad \text{and} \quad y = 20 - x > 0 \implies x < 20
   $$

   Therefore, the domain of $A$ is:

   $$
   D_A = (0, 20)
   $$

3. Dimensions maximizing area:
   Compute the first derivative of $A(x)$:

   $$
   A'(x) = \frac{d}{dx}\left(20x - x^2\right) = 20 - 2x
   $$

   Set the derivative to zero:

   $$
   20 - 2x = 0 \implies 2x = 20 \implies x = 10
   $$

   Substitute $x = 10$ into $y = 20 - x$:

   $$
   y = 20 - 10 = 10
   $$

   The optimal dimensions are $10 \times 10$, forming a square of area:

   $$
   A(10) = 10 \cdot 10 = 100
   $$

4. Justification of the maximum:
   Compute the second derivative:

   $$
   A''(x) = \frac{d}{dx}(20 - 2x) = -2
   $$

   Because $A''(x) = -2 < 0$ for all $x \in (0, 20)$, the function $A(x)$ is strictly concave on its entire domain. Consequently, the unique critical point $x = 10$ is the unique global maximum.
   Alternatively, completing the square confirms:

   $$
   A(x) = -(x - 10)^2 + 100 \le 100
   $$

   with equality holding if and only if $x = 10$.

---

## Result

$$
A(x) = 20x - x^2
$$

$$
D_A = (0, 20)
$$

$$
x = 10, \quad y = 10, \quad A_{\max} = 100
$$

---

## Verification

**Pass 1 — Algebraic check:** By the arithmetic mean-geometric mean inequality (AM-GM):

$$
\sqrt{xy} \le \frac{x+y}{2} = \frac{20}{2} = 10 \implies xy \le 100
$$

Equality holds if and only if $x = y = 10$, confirming both the dimensions and the maximal value algebraically without calculus.

**Pass 2 — Numerical check:** Evaluate $A(x)$ near $x = 10$: $A(9) = 9 \cdot 11 = 99$, $A(10) = 100$, $A(11) = 11 \cdot 9 = 99$. Both adjacent integer points yield smaller areas.

**Pass 3 — Consistency check:** As $x \to 0^+$ or $x \to 20^-$, the rectangle collapses to a line segment and $A(x) \to 0$. Since $A(x) > 0$ on $(0, 20)$ and continuous, a global maximum must exist in $(0, 20)$, and it matches $A(10) = 100$.

---

## Exam tip

Among all rectangles with a fixed perimeter, the square always encloses the maximum area.

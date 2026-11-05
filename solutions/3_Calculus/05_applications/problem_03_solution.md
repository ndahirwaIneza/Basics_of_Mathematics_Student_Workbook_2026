# Exercise 3

**Problem:** From a $30\text{ cm}\times40\text{ cm}$ sheet, squares of side length $x$ are cut from the corners and the edges are folded up to form an open box.

Write the volume as a function of $x$, determine the physically meaningful domain, and find the value of $x$ for which the volume is greatest.

---

## Relevant theorem / definition

The volume of a rectangular prism with base dimensions $a, b$ and height $h$ is $V = abh$. A continuous function on a closed interval $[a, b]$ achieves its maximum either at critical points where $V'(x) = 0$ or at the endpoints. If $V''(x) < 0$ at a unique critical point in an open interval where $V(x) > 0$ and boundary limits vanish, that critical point is the unique global maximum.

---

## Solution

1. Volume as a function of $x$:
   Cutting out a square of side $x$ from each corner leaves a base of width $30 - 2x$ and length $40 - 2x$.
   Folding the flaps upward gives a box of height $x$.
   The volume function is:

   $$
   V(x) = x(30 - 2x)(40 - 2x)
   $$

   Expand the expression:

   $$
   V(x) = x(1200 - 140x + 4x^2) = 4x^3 - 140x^2 + 1200x
   $$

2. Physically meaningful domain:
   All geometric dimensions of the box must be strictly positive:

   $$
   x > 0, \qquad 30 - 2x > 0 \implies x < 15, \qquad 40 - 2x > 0 \implies x < 20
   $$

   The restrictive upper bound is $x < 15$. Thus, the physically meaningful domain is:

   $$
   D_V = (0, 15)
   $$

3. Value of $x$ maximizing volume:
   Compute the first derivative of $V(x)$:

   $$
   V'(x) = 12x^2 - 280x + 1200
   $$

   Set $V'(x) = 0$ and divide by 4:

   $$
   3x^2 - 70x + 300 = 0
   $$

   Solve the quadratic equation using the discriminant:

   $$
   \Delta = (-70)^2 - 4(3)(300) = 4900 - 3600 = 1300
   $$

   $$
   \sqrt{\Delta} = \sqrt{1300} = 10\sqrt{13}
   $$

   The solutions are:

   $$
   x = \frac{70 \pm 10\sqrt{13}}{6} = \frac{35 \pm 5\sqrt{13}}{3}
   $$

   Evaluating the two roots:

   $$
   x_1 = \frac{35 - 5\sqrt{13}}{3} \approx 5.66\text{ cm}
   $$

   $$
   x_2 = \frac{35 + 5\sqrt{13}}{3} \approx 17.68\text{ cm}
   $$

   Only $x_1$ lies within the domain $(0, 15)$; the root $x_2 > 15$ is geometrically impossible because the side of length $30\text{ cm}$ cannot support two cuts exceeding $15\text{ cm}$ each.

4. Second derivative check:
   Compute $V''(x)$:

   $$
   V''(x) = 24x - 280
   $$

   Evaluate at $x_1$:

   $$
   V''(x_1) = 24\left(\frac{35 - 5\sqrt{13}}{3}\right) - 280 = 8(35 - 5\sqrt{13}) - 280 = -40\sqrt{13} < 0
   $$

   Because $V''(x_1) < 0$ and $V(x) \to 0$ as $x \to 0^+$ and $x \to 15^-$, the point $x_1$ is the unique global maximum on $(0, 15)$.

---

## Result

$$
V(x) = 4x^3 - 140x^2 + 1200x\quad [\text{cm}^3]
$$

$$
D_V = (0, 15)\quad [\text{cm}]
$$

$$
x = \frac{35 - 5\sqrt{13}}{3}\approx 5.66\text{ cm}
$$

---

## Verification

**Pass 1 — Algebraic check:** The derivative factorizes as $V'(x) = 4(3x^2 - 70x + 300) = 12\left(x - \frac{35 - 5\sqrt{13}}{3}\right)\left(x - \frac{35 + 5\sqrt{13}}{3}\right)$. For $x \in \left(0, \frac{35 - 5\sqrt{13}}{3}\right)$, $V'(x) > 0$ (increasing volume). For $x \in \left(\frac{35 - 5\sqrt{13}}{3}, 15\right)$, $V'(x) < 0$ (decreasing volume). This confirms a unique local and global peak.

**Pass 2 — Numerical check:** Plug in $x = 5$, $x = 5.657$, and $x = 6$:
- $V(5) = 5(20)(30) = 3000\text{ cm}^3$
- $V(5.6574) \approx 5.6574(18.6852)(28.6852) \approx 3032.30\text{ cm}^3$
- $V(6) = 6(18)(28) = 3024\text{ cm}^3$
The value at $5.657$ exceeds both neighboring integer points.

**Pass 3 — Consistency check:** At the physical boundaries $x = 0$ (no flaps folded up) and $x = 15$ (sheet cut entirely in half along the shorter dimension), the volume is 0. The internal maximum is strictly positive, satisfying physical boundary conditions.

---

## Exam tip

The domain is constrained by the shorter side of the sheet: cutting squares of side $x$ from both corners requires $2x < \min(\text{width}, \text{length})$.

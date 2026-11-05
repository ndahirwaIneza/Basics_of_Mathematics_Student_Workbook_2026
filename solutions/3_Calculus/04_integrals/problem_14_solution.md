# Exercise 14

**Problem:** Let

$$
f(x)=\begin{cases}x+1,&-1\le x<1,\\2,&1\le x\le3.\end{cases}
$$

Sketch the graph, decide where to split the integral, compute

$$
\int_{-1}^{3}f(x)\,dx
$$

and verify the result geometrically.

---

## Relevant theorem / definition

The interval additivity property of the definite integral states that if $f$ is integrable on $[a, b]$ and $c \in (a, b)$, then:

$$
\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx
$$

The area of a right triangle with base $b$ and height $h$ is:

$$
\text{Area}_{\text{triangle}} = \frac{1}{2} b h
$$

The area of a rectangle with width $w$ and height $h$ is:

$$
\text{Area}_{\text{rectangle}} = w h
$$

---

## Solution

1. Graph description:
   - On the interval $[-1, 1)$, $f(x) = x + 1$. This is a line segment with slope $1$, starting on the $x$-axis at $(-1, 0)$ and rising to $(1, 2)$ (with open endpoint $(1,2)$).
   - On the interval $[1, 3]$, $f(x) = 2$. This is a horizontal line segment of constant height $2$, starting at $(1, 2)$ and ending at $(3, 2)$.
   At the junction point $x = 1$, $\lim_{x \to 1^-} f(x) = 1 + 1 = 2$ and $f(1) = 2$. Therefore, the two pieces meet continuously at $(1, 2)$, forming a continuous, piecewise linear curve.

2. Deciding where to split the integral:
   Because the formula defining $f(x)$ changes at $x = 1$, the integral over $[-1, 3]$ must be split at $c = 1$:

$$
   \int_{-1}^3 f(x)\,dx = \int_{-1}^1 (x+1)\,dx + \int_1^3 2\,dx
$$

3. Computing the integrals:
   Evaluate the first sub-integral on $[-1, 1]$:

$$
   \begin{align}
   \int_{-1}^1 (x+1)\,dx &= \left[ \frac{x^2}{2} + x \right]_{-1}^1 \\
   &= \left(\frac{1^2}{2} + 1\right) - \left(\frac{(-1)^2}{2} + (-1)\right) \\
   &= \left(\frac{1}{2} + 1\right) - \left(\frac{1}{2} - 1\right) \\
   &= \frac{3}{2} - \left(-\frac{1}{2}\right) \\
   &= \frac{3}{2} + \frac{1}{2} \\
   &= 2
   \end{align}
$$

   Evaluate the second sub-integral on $[1, 3]$:

$$
   \int_1^3 2\,dx = \left[ 2x \right]_1^3 = 2(3) - 2(1) = 6 - 2 = 4
$$

   Summing the two contributions:

$$
   \int_{-1}^3 f(x)\,dx = 2 + 4 = 6
$$

4. Geometric verification:
   The region under the curve on $[-1, 3]$ decomposes into two standard geometric polygons:
   - Over $[-1, 1]$: A right-angled triangle with base along the $x$-axis from $x = -1$ to $x = 1$ of length $b = 1 - (-1) = 2$, and vertical height $h = f(1) = 2$:

$$
     \text{Area}_{\text{triangle}} = \frac{1}{2} \cdot 2 \cdot 2 = 2
$$

   - Over $[1, 3]$: A rectangle with horizontal base along $[1, 3]$ of length $w = 3 - 1 = 2$, and constant vertical height $h = 2$:

$$
     \text{Area}_{\text{rectangle}} = 2 \cdot 2 = 4
$$

   Total geometric area:

$$
   \text{Total Area} = 2 + 4 = 6
$$

   The geometric area equals the analytic integral value.

---

## Result

$$
\int_{-1}^{3}f(x)\,dx = 6
$$

---

## Verification

**Pass 1 — Algebraic check:** By linearity on $[-1, 1]$, $\int_{-1}^1 (x+1)\,dx = \int_{-1}^1 x\,dx + \int_{-1}^1 1\,dx$. The first integral is $0$ because $x$ is odd on the symmetric interval $[-1, 1]$, and the second is $1 \cdot (1 - (-1)) = 2$. Adding $\int_1^3 2\,dx = 2(3 - 1) = 4$ yields $2 + 4 = 6$.

**Pass 2 — Numerical check:** Over the entire domain $[-1, 3]$ of width $4$, the function satisfies $0 \le f(x) \le 2$. The total area must lie between $0 \cdot 4 = 0$ and $2 \cdot 4 = 8$. The computed value $6$ lies within $(0, 8)$.

**Pass 3 — Consistency check:** The region can alternatively be viewed as a trapezoid on $[-1, 1]$ (with parallel vertical sides $0$ and $2$, width $2$, area $\frac{0+2}{2} \cdot 2 = 2$) joined to a square on $[1, 3]$ of side $2$ (area $2^2 = 4$). Their sum $2 + 4 = 6$ confirms consistency.

---

## Exam tip

For piecewise functions, split the integral at each boundary point where the algebraic formula changes, and check continuity at the junction to avoid missing vertical jumps.

# Exercise 12

**Problem:** Compare

$$
\int_{-2}^{2}x\,dx
$$

and

$$
\int_{-2}^{2}|x|\,dx.
$$

Before calculating, predict the results from symmetry and a sketch, then carry out the calculation and explain the difference.

---

## Relevant theorem / definition

For an integral over a symmetric interval $[-a, a]$:
- If $f$ is an odd function ($f(-x) = -f(x)$ for all $x$):

$$
\int_{-a}^a f(x)\,dx = 0
$$

- If $f$ is an even function ($f(-x) = f(x)$ for all $x$):

$$
\int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx
$$

The absolute value function is defined piecewise by:

$$
|x| = \begin{cases} -x, & x < 0 \\ x, & x \ge 0 \end{cases}
$$

---

## Solution

1. Predicting from symmetry and sketch:
   - For $f(x) = x$: The function is odd because $f(-x) = -x = -f(x)$. Its graph is a straight line through the origin with 180-degree rotational symmetry about $(0,0)$. On $[-2, 0]$, the graph forms a triangle below the $x$-axis of base $2$ and height $2$, contributing signed area $-2$. On $[0, 2]$, the graph forms a congruent triangle above the $x$-axis, contributing signed area $+2$. The two signed regions are equal in magnitude and opposite in sign, so they cancel completely. Prediction: $\int_{-2}^2 x\,dx = 0$.
   - For $g(x) = |x|$: The function is even because $g(-x) = |-x| = |x| = g(x)$. Its graph is a V-shape symmetric across the $y$-axis. Both triangular regions lie entirely on or above the $x$-axis, so their contributions add together without cancellation. Prediction: $\int_{-2}^2 |x|\,dx = 2 \int_0^2 x\,dx = 2 \cdot 2 = 4$.

2. Calculating $\int_{-2}^2 x\,dx$:

$$
   \int_{-2}^2 x\,dx = \left[ \frac{x^2}{2} \right]_{-2}^2 = \frac{2^2}{2} - \frac{(-2)^2}{2} = \frac{4}{2} - \frac{4}{2} = 2 - 2 = 0
$$

3. Calculating $\int_{-2}^2 |x|\,dx$:
   Split the integral at $x = 0$ where $|x|$ changes its algebraic rule:

$$
   \begin{align}
   \int_{-2}^2 |x|\,dx &= \int_{-2}^0 (-x)\,dx + \int_0^2 x\,dx \\
   &= \left[ -\frac{x^2}{2} \right]_{-2}^0 + \left[ \frac{x^2}{2} \right]_0^2 \\
   &= \left(0 - \left(-\frac{(-2)^2}{2}\right)\right) + \left(\frac{2^2}{2} - 0\right) \\
   &= \left(0 - (-2)\right) + (2 - 0) \\
   &= 2 + 2 \\
   &= 4
   \end{align}
$$

4. Explaining the difference:
   The definite integral computes net signed area. For $f(x) = x$, negative accumulation on the left side of the origin cancels the positive accumulation on the right side. Taking the absolute value $|x|$ reflects the negative branch across the $x$-axis, transforming negative signed values into positive ones. Consequently, the definite integral of $|x|$ measures the total geometric area enclosed by $y = x$ and the $x$-axis on $[-2, 2]$.

---

## Result

$$
\int_{-2}^{2}x\,dx = 0
$$

$$
\int_{-2}^{2}|x|\,dx = 4
$$

---

## Verification

**Pass 1 — Algebraic check:** By the substitution $x = -u$, $dx = -du$:

$$
\int_{-2}^2 x\,dx = \int_2^{-2} (-u)(-du) = -\int_{-2}^2 u\,du \implies 2\int_{-2}^2 x\,dx = 0 \implies \int_{-2}^2 x\,dx = 0
$$

For $|x|$: $|-u| = |u|$, so $\int_{-2}^2 |x|\,dx = 2\int_0^2 x\,dx = 2\left[\frac{x^2}{2}\right]_0^2 = 2(2) = 4$.

**Pass 2 — Numerical check:** Each triangular half has base $b = 2$ and height $h = 2$, with Euclidean area $\frac{1}{2}bh = \frac{1}{2}(2)(2) = 2$. Signed sum: $-2 + 2 = 0$; sum of absolute values: $2 + 2 = 4$.

**Pass 3 — Consistency check:** Since $|x| \ge x$ everywhere and $|x| > x$ for $x \in [-2, 0)$, monotonicity of the integral requires $\int_{-2}^2 |x|\,dx > \int_{-2}^2 x\,dx$, which holds strictly ($4 > 0$).

---

## Exam tip

Always check for parity on symmetric intervals $[-a, a]$: if the integrand is odd, the integral is immediately $0$, while if it is even, simplify to $2\int_0^a f(x)\,dx$.

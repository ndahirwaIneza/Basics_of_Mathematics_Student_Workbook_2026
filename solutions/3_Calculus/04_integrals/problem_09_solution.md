# Exercise 9

**Problem:** Compute

$$
\int_{-1}^{2}x\,dx.
$$

Then separately compute the areas of the parts of the graph below and above the $x$-axis and explain the difference between the definite integral and geometric area.

---

## Relevant theorem / definition

The Fundamental Theorem of Calculus states that if $f$ is continuous on $[a, b]$ and $F$ is an antiderivative of $f$, then:

$$
\int_a^b f(x)\,dx = F(b) - F(a) = \left[ F(x) \right]_a^b
$$

The definite integral computes the signed area between the curve and the $x$-axis:

$$
\int_a^b f(x)\,dx = A_{\text{above}} - A_{\text{below}}
$$

whereas total geometric area is given by the integral of the absolute value:

$$
\text{Area} = \int_a^b |f(x)|\,dx = A_{\text{above}} + A_{\text{below}}
$$

---

## Solution

1. Computing the definite integral directly:
   An antiderivative of $f(x) = x$ is $F(x) = \frac{x^2}{2}$.

$$
   \int_{-1}^{2} x\,dx = \left[ \frac{x^2}{2} \right]_{-1}^2 = \frac{2^2}{2} - \frac{(-1)^2}{2} = \frac{4}{2} - \frac{1}{2} = \frac{3}{2}
$$

2. Computing the area of the region below the $x$-axis:
   The function $f(x) = x$ crosses the $x$-axis at $x = 0$.
   On the interval $[-1, 0]$, $f(x) \le 0$. The region below the $x$-axis is a right-angled triangle with base on $[-1, 0]$ of length $1$ and height $|f(-1)| = |-1| = 1$:

$$
   A_{\text{below}} = \int_{-1}^0 (-x)\,dx = \left[ -\frac{x^2}{2} \right]_{-1}^0 = 0 - \left(-\frac{(-1)^2}{2}\right) = \frac{1}{2}
$$

3. Computing the area of the region above the $x$-axis:
   On the interval $[0, 2]$, $f(x) \ge 0$. The region above the $x$-axis is a right-angled triangle with base on $[0, 2]$ of length $2$ and height $f(2) = 2$:

$$
   A_{\text{above}} = \int_0^2 x\,dx = \left[ \frac{x^2}{2} \right]_0^2 = \frac{2^2}{2} - 0 = 2
$$

4. Explaining the difference between the definite integral and geometric area:
   - The definite integral accumulates values with algebraic signs. Regions where $f(x) < 0$ contribute negatively, canceling positive accumulation:

$$
     \int_{-1}^2 x\,dx = A_{\text{above}} - A_{\text{below}} = 2 - \frac{1}{2} = \frac{3}{2}
$$

   - Total geometric area measures physical surface size, which is strictly non-negative and additive:

$$
     \text{Area} = A_{\text{above}} + A_{\text{below}} = 2 + \frac{1}{2} = \frac{5}{2}
$$

   Therefore, the definite integral yields $\frac{3}{2}$ due to partial cancellation, whereas the total geometric area is $\frac{5}{2}$.

---

## Result

$$
\int_{-1}^{2}x\,dx = \frac{3}{2}
$$

$$
A_{\text{below}} = \frac{1}{2}, \quad A_{\text{above}} = 2, \quad \text{Total Geometric Area} = \frac{5}{2}
$$

---

## Verification

**Pass 1 — Algebraic check:** Net signed combination: $A_{\text{above}} - A_{\text{below}} = 2 - \frac{1}{2} = \frac{3}{2}$, which matches the direct Newton-Leibniz calculation $\left[\frac{x^2}{2}\right]_{-1}^2 = 2 - \frac{1}{2} = \frac{3}{2}$.

**Pass 2 — Numerical check:** Geometric triangle area formula $\frac{1}{2} \cdot \text{base} \cdot \text{height}$: for $[-1, 0]$, $\frac{1}{2}(1)(1) = \frac{1}{2}$; for $[0, 2]$, $\frac{1}{2}(2)(2) = 2$. Signed sum: $-1/2 + 2 = 3/2$.

**Pass 3 — Consistency check:** The interval above the axis has length $2$ and maximum height $2$, which is strictly greater than the subinterval below the axis (length $1$, maximum depth $1$). Hence the positive area must dominate, guaranteeing a positive value for the definite integral.

---

## Exam tip

Distinguish between "definite integral" (signed sum, allows negative values and cancellations) and "area between curve and axis" (must integrate $|f(x)|$, always non-negative).

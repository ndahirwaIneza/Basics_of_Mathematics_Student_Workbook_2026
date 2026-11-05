# Exercise 10

**Problem:** Before carrying out the exact calculation, estimate the possible range of values of the integral

$$
\int_0^2(x^2+1)\,dx,
$$

using

$$
1\le x^2+1\le5
$$

on $[0,2]$. Only then compute the integral exactly, compare the result with the earlier estimate, and explain what type of computational error such a check can detect.

---

## Relevant theorem / definition

The boundedness (comparison) property of the definite integral states that if $m \le f(x) \le M$ for all $x \in [a, b]$, then:

$$
m(b - a) \le \int_a^b f(x)\,dx \le M(b - a)
$$

The Fundamental Theorem of Calculus states:

$$
\int_a^b f(x)\,dx = F(b) - F(a)
$$

where $F'(x) = f(x)$.

---

## Solution

1. Estimating the range of values:
   On the interval $[0, 2]$, the function $f(x) = x^2 + 1$ is strictly increasing.
   At $x = 0$, $f(0) = 0^2 + 1 = 1$ (the minimum value $m$).
   At $x = 2$, $f(2) = 2^2 + 1 = 5$ (the maximum value $M$).
   The length of the interval of integration is $b - a = 2 - 0 = 2$.
   Applying the comparison property:

$$
   1 \cdot (2 - 0) \le \int_0^2 (x^2+1)\,dx \le 5 \cdot (2 - 0)
$$

$$
   2 \le \int_0^2 (x^2+1)\,dx \le 10
$$

2. Computing the exact value:
   Find an antiderivative of $x^2 + 1$:

$$
   F(x) = \frac{x^3}{3} + x
$$

   Apply the Fundamental Theorem of Calculus:

$$
   \begin{align}
   \int_0^2 (x^2+1)\,dx &= \left[ \frac{x^3}{3} + x \right]_0^2 \\
   &= \left(\frac{2^3}{3} + 2\right) - \left(\frac{0^3}{3} + 0\right) \\
   &= \frac{8}{3} + 2 \\
   &= \frac{14}{3}
   \end{align}
$$

3. Comparing the exact result with the estimate:
   In decimal form, $\frac{14}{3} \approx 4.67$.
   Because $2 \le \frac{14}{3} \le 10$ (specifically, $\frac{6}{3} \le \frac{14}{3} \le \frac{30}{3}$), the exact value lies strictly within the predicted bounds.

4. Types of computational errors this check can detect:
   - Sign errors: if lower and upper limits are subtracted in reverse, yielding a negative value (e.g., $-14/3$), this contradicts the lower bound $2 > 0$ for a positive integrand.
   - Power integration slips: forgetting to divide by the new exponent when integrating $x^2$ gives $x^3 + x$, yielding $8 + 2 = 10$, which hits the extreme theoretical upper bound (impossible for a strictly increasing, non-constant function).
   - Order-of-magnitude mistakes: multiplying instead of plugging in limits, or incorrect fractional arithmetic yielding a value outside $[2, 10]$.

---

## Result

$$
\text{Estimate: } 2 \le \int_0^2(x^2+1)\,dx \le 10
$$

$$
\text{Exact value: } \int_0^2(x^2+1)\,dx = \frac{14}{3}
$$

---

## Verification

**Pass 1 — Algebraic check:** Approximating with the trapezoidal rule $T_1 = \frac{2-0}{2}[f(0) + f(2)] = 1 \cdot (1 + 5) = 6$. For a convex function ($f''(x) = 2 > 0$), the trapezoidal rule is an upper bound: $14/3 \approx 4.67 < 6$. Approximating with the midpoint rule $M_1 = (2-0)f(1) = 2(1^2+1) = 4$. For a convex function, midpoint is a lower bound: $4 < 14/3$. Thus $4 < 14/3 < 6$.

**Pass 2 — Numerical check:** Simpson's rule with $n=2$ (subintervals $[0,1]$ and $[1,2]$) gives:

$$
S_2 = \frac{2-0}{6}\left[f(0) + 4f(1) + f(2)\right] = \frac{1}{3}\left[1 + 4(2) + 5\right] = \frac{1}{3}(14) = \frac{14}{3}
$$

Simpson's rule is exact for polynomials of degree up to 3, confirming $\frac{14}{3}$ identically.

**Pass 3 — Consistency check:** The average value of the function over $[0, 2]$ is $\frac{1}{2-0} \cdot \frac{14}{3} = \frac{7}{3} \approx 2.33$, which lies strictly between the minimum $1$ and maximum $5$.

---

## Exam tip

Before completing a definite integral of a positive function, establish quick bounds $(b-a)m \le I \le (b-a)M$ to catch sign and arithmetic errors instantly.

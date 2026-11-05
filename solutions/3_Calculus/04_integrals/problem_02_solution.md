# Exercise 2

**Problem:** Compute

$$
\int\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)\,dx.
$$

First rewrite the terms as powers, determine the domain of the original expression, and verify the result by differentiation.

---

## Relevant theorem / definition

The power rule of integration states that for any real constant $\alpha \neq -1$:

$$
\int x^\alpha\,dx = \frac{x^{\alpha+1}}{\alpha+1} + C
$$

Integration is linear:

$$
\int \left(a f(x) + b g(x)\right)\,dx = a \int f(x)\,dx + b \int g(x)\,dx
$$

---

## Solution

1. Determining the domain of the original expression:
   - The term $2\sqrt{x}$ requires $x \ge 0$.
   - The term $\frac{3}{x^2}$ requires $x \neq 0$.
   - The term $x^{1/3}$ is defined for all $x \in \mathbb{R}$ (or $x \ge 0$ under general power definitions).
   The intersection of these conditions defines the domain of the integrand:

$$
   D = (0, \infty)
$$

2. Rewriting terms as powers:

$$
   f(x) = 2x^{1/2} + 3x^{-2} - x^{1/3}
$$

3. Integrating term by term:
   For the first term:

$$
   \int 2x^{1/2}\,dx = 2 \cdot \frac{x^{1/2+1}}{\frac{1}{2}+1} = 2 \cdot \frac{x^{3/2}}{\frac{3}{2}} = \frac{4}{3}x^{3/2}
$$

   For the second term:

$$
   \int 3x^{-2}\,dx = 3 \cdot \frac{x^{-2+1}}{-2+1} = 3 \cdot \frac{x^{-1}}{-1} = -3x^{-1} = -\frac{3}{x}
$$

   For the third term:

$$
   \int -x^{1/3}\,dx = -\frac{x^{1/3+1}}{\frac{1}{3}+1} = -\frac{x^{4/3}}{\frac{4}{3}} = -\frac{3}{4}x^{4/3}
$$

   Combining the terms and adding the constant of integration $C$:

$$
   F(x) = \frac{4}{3}x^{3/2} - \frac{3}{x} - \frac{3}{4}x^{4/3} + C
$$

4. Verification by differentiation:

$$
   \begin{align}
   \frac{d}{dx}\left(\frac{4}{3}x^{3/2} - 3x^{-1} - \frac{3}{4}x^{4/3} + C\right) &= \frac{4}{3}\left(\frac{3}{2}x^{1/2}\right) - 3\left(-1x^{-2}\right) - \frac{3}{4}\left(\frac{4}{3}x^{1/3}\right) + 0 \\
   &= 2x^{1/2} + 3x^{-2} - x^{1/3} \\
   &= 2\sqrt{x} + \frac{3}{x^2} - x^{1/3}
   \end{align}
$$

---

## Result

$$
\int\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)\,dx = \frac{4}{3}x^{3/2} - \frac{3}{x} - \frac{3}{4}x^{4/3} + C, \quad x \in (0, \infty)
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiating the power terms directly recovers each original exponent: $\frac{3}{2}-1 = \frac{1}{2}$, $-1-1 = -2$, and $\frac{4}{3}-1 = \frac{1}{3}$, with coefficients matching $2$, $3$, and $-1$.

**Pass 2 — Numerical check:** At $x = 1$, the integrand evaluates to $f(1) = 2\sqrt{1} + \frac{3}{1^2} - 1^{1/3} = 2 + 3 - 1 = 4$. Differentiating $F(x)$ at $x = 1$: $F'(1) = \frac{4}{3} \cdot \frac{3}{2}(1)^{1/2} - 3(-1)(1)^{-2} - \frac{3}{4} \cdot \frac{4}{3}(1)^{1/3} = 2 + 3 - 1 = 4$, which matches $f(1)$.

**Pass 3 — Consistency check:** As $x \to 0^+$, the term $3/x^2 \to \infty$ dominates the integrand, and its antiderivative $-3/x \to -\infty$ dominates $F(x)$, which is consistent with the behavior of non-integrable poles at the origin.

---

## Exam tip

Convert radical and reciprocal expressions into fractional and negative exponents before integrating, and verify that the domain excludes $x = 0$.

# Exercise 1

**Problem:** For

$$
f(x)=3x^2-4x+5
$$

find one antiderivative $F(x)$. Write the entire family of antiderivatives, verify the result by differentiation, and explain the meaning of the constant $C$.

---

## Relevant theorem / definition

An antiderivative of a continuous function $f(x)$ on an interval $I$ is any differentiable function $F(x)$ such that $F'(x) = f(x)$ for all $x \in I$. By the mean value theorem, if $F(x)$ is one antiderivative, the general antiderivative (indefinite integral) is:

$$
\int f(x)\,dx = F(x) + C, \quad C \in \mathbb{R}
$$

The power rule of integration states:

$$
\int x^n\,dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)
$$

---

## Solution

1. Finding one antiderivative $F(x)$:
   Apply the power rule and linearity term by term:

$$
   \int 3x^2\,dx = 3 \cdot \frac{x^3}{3} = x^3
$$

$$
   \int (-4x)\,dx = -4 \cdot \frac{x^2}{2} = -2x^2
$$

$$
   \int 5\,dx = 5x
$$

   Setting the arbitrary constant to zero gives one specific antiderivative:

$$
   F(x) = x^3 - 2x^2 + 5x
$$

2. Entire family of antiderivatives:
   Adding an arbitrary real constant $C$:

$$
   \int (3x^2 - 4x + 5)\,dx = x^3 - 2x^2 + 5x + C, \quad C \in \mathbb{R}
$$

3. Verification by differentiation:
   Differentiating the family with respect to $x$:

$$
   \begin{align}
   \frac{d}{dx}\left(x^3 - 2x^2 + 5x + C\right) &= \frac{d}{dx}(x^3) - 2\frac{d}{dx}(x^2) + 5\frac{d}{dx}(x) + \frac{d}{dx}(C) \\
   &= 3x^2 - 2(2x) + 5(1) + 0 \\
   &= 3x^2 - 4x + 5 \\
   &= f(x)
   \end{align}
$$

4. Meaning of the constant $C$:
   The derivative of any constant is zero, so adding $C$ does not change the slope of the tangent at any point $x$. Geometrically, the constant $C$ corresponds to a vertical translation of the integral curve $y = F(x)$ along the $y$-axis. The entire family represents an infinite set of vertically parallel curves filling the plane, where specifying an initial condition $(x_0, y_0)$ selects a unique curve from the family.

---

## Result

$$
F(x) = x^3 - 2x^2 + 5x
$$

$$
\int (3x^2 - 4x + 5)\,dx = x^3 - 2x^2 + 5x + C, \quad C \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiating term by term: $\frac{d}{dx}(x^3) = 3x^2$, $\frac{d}{dx}(-2x^2) = -4x$, $\frac{d}{dx}(5x) = 5$, and $\frac{d}{dx}(C) = 0$. Summing these terms yields $3x^2 - 4x + 5 = f(x)$.

**Pass 2 — Numerical check:** At $x = 2$, $f(2) = 3(2^2) - 4(2) + 5 = 12 - 8 + 5 = 9$. Using $F(x) = x^3 - 2x^2 + 5x$, the symmetric difference quotient with $h = 0.001$ gives:

$$
\frac{F(2.001) - F(1.999)}{0.002} = \frac{10.009001 - 9.991001}{0.002} = \frac{0.018}{0.002} = 9.000
$$

which matches $f(2) = 9$.

**Pass 3 — Consistency check:** The integrand $f(x)$ is a polynomial of degree 2. Its antiderivatives must be polynomials of degree $2 + 1 = 3$ with leading coefficient $3 / 3 = 1$. The expression $x^3 - 2x^2 + 5x + C$ matches this degree and leading coefficient.

---

## Exam tip

Always include $+ C$ when writing indefinite integrals, as an indefinite integral represents an entire infinite family of functions, not a single curve.

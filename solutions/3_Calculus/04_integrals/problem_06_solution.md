# Exercise 6

**Problem:** Compute

$$
\int\frac{2x}{x^2+5}\,dx.
$$

Identify the denominator as a candidate for substitution, compare the numerator with its derivative, and explain the source of the logarithm in the result.

---

## Relevant theorem / definition

The logarithmic integration rule states:

$$
\int \frac{g'(x)}{g(x)}\,dx = \ln|g(x)| + C
$$

which arises from the substitution $u = g(x)$, $du = g'(x)\,dx$, and the fundamental integral:

$$
\int \frac{1}{u}\,du = \ln|u| + C \quad (u \neq 0)
$$

---

## Solution

1. Identifying the candidate for substitution and comparing with the numerator:
   Choose the denominator as the candidate:

$$
   u = g(x) = x^2 + 5
$$

   The derivative of $u$ with respect to $x$ is:

$$
   \frac{du}{dx} = 2x \implies du = 2x\,dx
$$

   Comparing with the numerator: the numerator of the integrand is exactly $2x$. Thus the entire numerator combined with the differential $dx$ equals $du$.

2. Substituting and integrating:

$$
   \int \frac{2x}{x^2+5}\,dx = \int \frac{1}{u}\,du = \ln|u| + C
$$

3. Back-substituting $u = x^2 + 5$:

$$
   \ln|x^2 + 5| + C
$$

   Because $x^2 \ge 0$ for all real $x$, $x^2 + 5 \ge 5 > 0$, so $|x^2 + 5| = x^2 + 5$. The expression simplifies to:

$$
   \ln(x^2 + 5) + C
$$

4. Explaining the source of the logarithm:
   The power rule $\int u^n\,du = \frac{u^{n+1}}{n+1}$ applies to all real exponents except $n = -1$, where division by zero would occur. In this integrand, after substitution the exponent of $u$ in the denominator is exactly $-1$, that is, $u^{-1} = \frac{1}{u}$. Because $\frac{d}{du}(\ln|u|) = \frac{1}{u}$ on each interval avoiding $0$ (and a derivative does not determine a single unique antiderivative without an initial condition), an antiderivative is $\ln|u|$; the whole family is $\ln|u| + C$ on each interval avoiding $0$. Thus, whenever an integrand exhibits the structure $\frac{g'(x)}{g(x)}$, the result is fundamentally logarithmic.

---

## Result

$$
\int\frac{2x}{x^2+5}\,dx = \ln(x^2+5) + C, \quad C \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiating $\ln(x^2+5)$ by the chain rule: $\frac{d}{dx}\ln(x^2+5) = \frac{1}{x^2+5} \cdot \frac{d}{dx}(x^2+5) = \frac{2x}{x^2+5}$, matching the integrand.

**Pass 2 — Numerical check:** At $x = 2$, $f(2) = \frac{2(2)}{2^2+5} = \frac{4}{9} \approx 0.4444$. Evaluating the derivative of $F(x) = \ln(x^2+5)$ at $x = 2$: $F'(2) = \frac{2(2)}{2^2+5} = \frac{4}{9}$, which matches $f(2)$.

**Pass 3 — Consistency check:** For large $x$, the integrand behaves asymptotically as $\frac{2x}{x^2} = \frac{2}{x}$, whose integral is $2\ln x = \ln(x^2)$. Expanding the antiderivative for large $x$ gives $\ln(x^2+5) = \ln\left[x^2\left(1 + \frac{5}{x^2}\right)\right] = 2\ln x + \ln\left(1 + \frac{5}{x^2}\right)$, which approaches $2\ln x$ as $x \to \infty$.

---

## Exam tip

Whenever a rational integrand has a numerator that is the derivative of the denominator, write down $\ln|\text{denominator}| + C$ immediately.

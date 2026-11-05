# Exercise 5

**Problem:** Compute

$$
\int xe^{x^2}\,dx.
$$

First compare the structure with Problem 4 and explain what is common despite the different appearance of the function.

---

## Relevant theorem / definition

Integration by substitution:
If $u = g(x)$ is differentiable and $f$ is continuous, then:

$$
\int f(g(x)) g'(x)\,dx = \int f(u)\,du
$$

The standard exponential antiderivative is:

$$
\int e^u\,du = e^u + C
$$

---

## Solution

1. Structural comparison with Problem 4:
   In Problem 4, the integrand had the structure $g'(x) [g(x)]^4$, where $g(x) = x^2+1$ and $g'(x) = 2x$. The outer function was a 4th power $f(u) = u^4$.
   In this problem, the integrand is $x e^{x^2}$, which has the structure $\frac{1}{2} g'(x) e^{g(x)}$, where $g(x) = x^2$ and $g'(x) = 2x$. The outer function is the exponential $f(u) = e^u$.
   What is common:
   - In both cases, a composite function has a quadratic expression ($x^2$ or $x^2+1$) in its inner argument.
   - In both cases, the outer multiplicative factor contains the linear term $x$, which is proportional to the derivative of the quadratic inner function: $\frac{d}{dx}(x^2) = 2x$.
   - Consequently, both integrals reduce directly to elementary standard forms through a quadratic substitution. The specific type of outer function (polynomial power vs. exponential) changes the anti-differentiation rule, but the core substitution mechanism is identical.

2. Carrying out the substitution:
   Let $u = x^2$.
   Differentiating both sides:

$$
   du = 2x\,dx \implies x\,dx = \frac{1}{2}\,du
$$

3. Integrating with respect to $u$:

$$
   \int xe^{x^2}\,dx = \int e^u \left(\frac{1}{2}\,du\right) = \frac{1}{2}\int e^u\,du = \frac{1}{2}e^u + C
$$

4. Back-substituting $u = x^2$:

$$
   \frac{1}{2}e^{x^2} + C
$$

5. Verification by differentiation:
   Apply the chain rule:

$$
   \frac{d}{dx}\left(\frac{1}{2}e^{x^2} + C\right) = \frac{1}{2}e^{x^2} \cdot \frac{d}{dx}(x^2) + 0 = \frac{1}{2}e^{x^2}(2x) = xe^{x^2}
$$

---

## Result

$$
\int xe^{x^2}\,dx = \frac{1}{2}e^{x^2} + C, \quad C \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiating $\frac{1}{2}e^{x^2}$ via the chain rule produces $\frac{1}{2} \cdot e^{x^2} \cdot 2x = xe^{x^2}$, which is identical to the integrand.

**Pass 2 — Numerical check:** At $x = 1$, $f(1) = 1 \cdot e^{1^2} = e \approx 2.71828$. Evaluating the derivative of $F(x) = \frac{1}{2}e^{x^2}$ at $x = 1$ using $h = 0.001$:

$$
\frac{F(1.001) - F(0.999)}{0.002} = \frac{\frac{1}{2}e^{1.002001} - \frac{1}{2}e^{0.998001}}{0.002} \approx \frac{1.36186 - 1.35642}{0.002} \approx 2.72 \approx e
$$

**Pass 3 — Consistency check:** The function $f(x) = xe^{x^2}$ is odd: $f(-x) = (-x)e^{(-x)^2} = -xe^{x^2} = -f(x)$. Its antiderivative $F(x) = \frac{1}{2}e^{x^2}$ is even: $F(-x) = \frac{1}{2}e^{(-x)^2} = \frac{1}{2}e^{x^2} = F(x)$, consistent with general symmetry properties of integrals.

---

## Exam tip

When an exponential term has a non-linear argument $g(x)$, look for $g'(x)$ as an outside factor; missing constant coefficients can be factored out.

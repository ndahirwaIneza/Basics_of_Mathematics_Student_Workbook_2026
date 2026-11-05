# Exercise 4

**Problem:** Compute

$$
\int 2x(x^2+1)^4\,dx.
$$

Before calculating, identify a candidate for the new variable $u$ and show that its derivative appears in the integral. Finally, verify the result by differentiation.

---

## Relevant theorem / definition

Integration by substitution (the chain rule in reverse):
If $u = g(x)$ is a differentiable function whose range is an interval $I$, and $f$ is continuous on $I$, then:

$$
\int f(g(x)) g'(x)\,dx = \int f(u)\,du
$$

The power rule of integration states:

$$
\int u^n\,du = \frac{u^{n+1}}{n+1} + C \quad (n \neq -1)
$$

---

## Solution

1. Identifying the candidate for substitution:
   Consider the inner function of the composite factor $(x^2+1)^4$:

$$
   u = g(x) = x^2 + 1
$$

   Its derivative with respect to $x$ is:

$$
   \frac{du}{dx} = 2x \implies du = 2x\,dx
$$

   The factor $2x\,dx$ appears directly in the integrand multiplying the composite term $(x^2+1)^4$.

2. Carrying out the substitution:
   Substitute $u = x^2 + 1$ and $du = 2x\,dx$:

$$
   \int 2x(x^2+1)^4\,dx = \int u^4\,du
$$

3. Integrating with respect to $u$:

$$
   \int u^4\,du = \frac{u^5}{5} + C = \frac{1}{5}u^5 + C
$$

4. Back-substituting $u = x^2 + 1$:

$$
   \frac{1}{5}(x^2+1)^5 + C
$$

5. Verification by differentiation:
   Apply the chain rule to the antiderivative:

$$
   \begin{align}
   \frac{d}{dx}\left(\frac{1}{5}(x^2+1)^5 + C\right) &= \frac{1}{5} \cdot 5(x^2+1)^{5-1} \cdot \frac{d}{dx}(x^2+1) + 0 \\
   &= (x^2+1)^4 \cdot (2x) \\
   &= 2x(x^2+1)^4
   \end{align}
$$

---

## Result

$$
\int 2x(x^2+1)^4\,dx = \frac{1}{5}(x^2+1)^5 + C, \quad C \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Expanding $(x^2+1)^5$ by the binomial theorem gives $x^{10} + 5x^8 + 10x^6 + 10x^4 + 5x^2 + 1$. Multiplying by $\frac{1}{5}$ gives $\frac{1}{5}x^{10} + x^8 + 2x^6 + 2x^4 + x^2 + \frac{1}{5}$. Differentiating this polynomial term by term yields $2x^9 + 8x^7 + 12x^5 + 8x^3 + 2x = 2x(x^8 + 4x^6 + 6x^4 + 4x^2 + 1) = 2x(x^2+1)^4$.

**Pass 2 — Numerical check:** At $x = 1$, the integrand evaluates to $f(1) = 2(1)(1^2+1)^4 = 2(16) = 32$. Evaluating $F(x) = \frac{1}{5}(x^2+1)^5$ around $x = 1$ with step $h = 0.001$:

$$
\frac{F(1.001) - F(0.999)}{0.002} = \frac{\frac{1}{5}(2.002001)^5 - \frac{1}{5}(1.998001)^5}{0.002} \approx \frac{6.432064 - 6.368064}{0.002} = 32.000
$$

which matches $f(1) = 32$.

**Pass 3 — Consistency check:** The integrand is an odd function because $f(-x) = 2(-x)((-x)^2+1)^4 = -2x(x^2+1)^4 = -f(x)$. The antiderivative $F(x) = \frac{1}{5}(x^2+1)^5$ is an even function because $F(-x) = \frac{1}{5}((-x)^2+1)^5 = F(x)$, consistent with the property that an antiderivative of an odd function is even.

---

## Exam tip

Before expanding high-degree powers in a product, always check whether the other factor is a scalar multiple of the derivative of the base.

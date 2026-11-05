# Exercise 7

**Problem:** Compute

$$
\int xe^x\,dx.
$$

First write the product differentiation rule and, on that basis, explain the meaning of the integration-by-parts formula. Verify the result by differentiation.

---

## Relevant theorem / definition

The product rule for differentiating two differentiable functions $u(x)$ and $v(x)$ is:

$$
\frac{d}{dx}\left[u(x)v(x)\right] = u'(x)v(x) + u(x)v'(x)
$$

Integrating both sides with respect to $x$ yields:

$$
u(x)v(x) = \int u'(x)v(x)\,dx + \int u(x)v'(x)\,dx
$$

Rearranging gives the integration-by-parts formula:

$$
\int u\,dv = uv - \int v\,du
$$

where $dv = v'(x)\,dx$ and $du = u'(x)\,dx$.

---

## Solution

1. Meaning of the integration-by-parts formula:
   The product rule shows that the derivative of a product is composed of two terms. Integration by parts reorganizes this identity to solve for one of the product integrals, allowing an integral of the form $\int u\,dv$ to be exchanged for a new integral $\int v\,du$. The method succeeds when differentiating $u$ simplifies it (e.g., reducing the degree of a polynomial), while $dv$ can be readily integrated without increasing complexity.

2. Choosing factors:
   Set:

$$
   u = x \implies du = dx
$$

$$
   dv = e^x\,dx \implies v = \int e^x\,dx = e^x
$$

   Differentiating $x$ lowers its degree from 1 to 0, eliminating the variable $x$ in the subsequent integral.

3. Applying integration by parts:

$$
   \begin{align}
   \int xe^x\,dx &= uv - \int v\,du \\
   &= x e^x - \int e^x\,dx \\
   &= x e^x - e^x + C \\
   &= (x-1)e^x + C
   \end{align}
$$

4. Verification by differentiation:
   Apply the product rule:

$$
   \begin{align}
   \frac{d}{dx}\left[(x-1)e^x + C\right] &= \frac{d}{dx}(x-1) \cdot e^x + (x-1)\frac{d}{dx}(e^x) + 0 \\
   &= 1 \cdot e^x + (x-1)e^x \\
   &= e^x + xe^x - e^x \\
   &= xe^x
   \end{align}
$$

---

## Result

$$
\int xe^x\,dx = (x-1)e^x + C, \quad C \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiating $(x-1)e^x$ by the product rule gives $(x-1)'e^x + (x-1)(e^x)' = e^x + (x-1)e^x = xe^x$, matching the integrand.

**Pass 2 — Numerical check:** At $x = 2$, $f(2) = 2e^2 \approx 14.7781$. The antiderivative is $F(x) = (x-1)e^x$. Evaluating $F'(2)$ directly: $F'(2) = 1 \cdot e^2 + (2-1)e^2 = 2e^2 \approx 14.7781$, matching $f(2)$.

**Pass 3 — Consistency check:** At $x = 1$, $F(1) = (1-1)e^1 = 0$, while $f(1) = 1 \cdot e^1 = e$. The tangent line to $y = F(x)$ at $x = 1$ has slope $e$, which equals $f(1)$.

---

## Exam tip

For integrals of the form $\int P(x)e^{ax}\,dx$, choose $u = P(x)$ so that differentiation repeatedly lowers the polynomial degree until it becomes a constant.

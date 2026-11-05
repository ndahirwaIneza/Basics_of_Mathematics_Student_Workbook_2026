# Exercise 3

**Problem:** For
$$f(x)=(x^2+1)e^x$$
compute the derivative. Then compare the correct result with the incorrect idea
$$f'(x)\stackrel{?}{=}(2x)e^x$$
and explain which term is missing.

---

## Relevant theorem / definition

The product rule for differentiating the product of two differentiable functions $u(x)$ and $v(x)$ states:
$$
\frac{d}{dx}[u(x)v(x)] = u'(x)v(x) + u(x)v'(x)
$$
The derivative of an exponential function with the natural base is $\frac{d}{dx}(e^x) = e^x$.

---

## Solution

1. Identify factors:
   Let $u(x) = x^2 + 1$ and $v(x) = e^x$.
   Compute individual derivatives:
   $$
   u'(x) = 2x, \quad v'(x) = e^x.
   $$

2. Apply the product rule:
   \begin{align}
   f'(x) &= u'(x)v(x) + u(x)v'(x) \\
   &= (2x)e^x + (x^2+1)e^x.
   \end{align}

3. Simplify by factoring out $e^x$:
   \begin{align}
   f'(x) &= (x^2 + 2x + 1)e^x \\
   &= (x+1)^2 e^x.
   \end{align}

4. Comparison with the incorrect formula $f'(x) \stackrel{?}{=} (2x)e^x$:
   The incorrect proposal differentiates only the first factor $u(x) = x^2+1$ to get $2x$, while keeping $v(x) = e^x$ untouched, effectively asserting that $(uv)' = u'v$.
   The missing term in this incorrect expression is:
   $$
   u(x)v'(x) = (x^2+1)e^x.
   $$
   This missing term accounts for the rate of change induced by the second factor $e^x$ changing over time while holding the first factor $x^2+1$ constant.

---

## Result

$$
f'(x) = (x^2 + 2x + 1)e^x = (x+1)^2 e^x
$$

$$
\text{Missing term in } (2x)e^x: \quad u(x)v'(x) = (x^2+1)e^x
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the derivative using logarithmic differentiation:
$$
\ln f(x) = \ln(x^2+1) + x
$$
Differentiating both sides:
$$
\frac{f'(x)}{f(x)} = \frac{2x}{x^2+1} + 1 = \frac{x^2+2x+1}{x^2+1}
$$
Multiplying by $f(x) = (x^2+1)e^x$:
$$
f'(x) = (x^2+2x+1)e^x = (x+1)^2 e^x
$$
This independently confirms the product rule derivation.

**Pass 2 — Numerical check:** Evaluate at $x = 0$:
$$
f(0) = (0^2+1)e^0 = 1, \quad f'(0) = (0+1)^2 e^0 = 1
$$
The incorrect idea gives $(2 \cdot 0)e^0 = 0 \neq 1$.
Compute the forward difference quotient at $x = 0$ with $h = 0.001$:
$f(0.001) = (1.000001)e^{0.001} \approx 1.000001 \times 1.0010005 = 1.0010015$.
$$
\frac{f(0.001) - f(0)}{0.001} = \frac{1.0010015 - 1}{0.001} \approx 1.001 \approx 1 = f'(0)
$$

**Pass 3 — Consistency check:** Since $(x+1)^2 \ge 0$ and $e^x > 0$ for all $x \in \mathbb{R}$, we have $f'(x) \ge 0$ everywhere, with a single stationary point at $x = -1$. Because $f(x) > 0$ for all $x$, $f(x) \to 0$ as $x \to -\infty$, and $f(x) \to \infty$ as $x \to \infty$, the function must be monotonically non-decreasing, matching $f'(x) \ge 0$.

---

## Exam tip

The derivative of a product is never the product of the derivatives; both factors must take turns being differentiated in the sum $u'v + uv'$.

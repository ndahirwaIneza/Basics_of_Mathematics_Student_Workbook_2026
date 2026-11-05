# Exercise 12

**Problem:** For
$$f(x)=(x^2+1)^3e^x$$
compute the derivative. Before calculating, write down a plan: which rule applies to the whole expression and which rule applies to one of its factors. Finally, organize the result by factoring out common factors.

---

## Relevant theorem / definition

The product rule states that $(uv)' = u'v + uv'$. The chain rule for a power of a function states that $\frac{d}{dx}[w(x)^n] = n[w(x)]^{n-1}w'(x)$. The derivative of the exponential function with base $e$ is $\frac{d}{dx}(e^x) = e^x$.

---

## Solution

1. Plan before calculation:
   - **Whole expression:** The function $f(x)$ is the product of two factors, $u(x) = (x^2+1)^3$ and $v(x) = e^x$. Therefore, the primary rule governing the whole expression is the **product rule**:
     $$
     f'(x) = u'(x)v(x) + u(x)v'(x).
     $$
   - **Factor $u(x) = (x^2+1)^3$:** This factor is a composite function with outer function $g(w) = w^3$ and inner function $w(x) = x^2 + 1$. Therefore, the **chain rule** applies to differentiate this factor:
     $$
     u'(x) = 3(x^2 + 1)^2 \cdot \frac{d}{dx}(x^2 + 1) = 3(x^2 + 1)^2 (2x) = 6x(x^2 + 1)^2.
     $$
   - **Factor $v(x) = e^x$:** Differentiating this factor uses the standard exponential derivative $v'(x) = e^x$.

2. Compute the derivative:
   Substitute $u(x)$, $u'(x)$, $v(x)$, and $v'(x)$ into the product rule:
   \begin{align}
   f'(x) &= u'(x)v(x) + u(x)v'(x) \\
   &= [6x(x^2 + 1)^2] e^x + [(x^2 + 1)^3] e^x.
   \end{align}

3. Organize by factoring out common factors:
   Both terms share the common factor $(x^2 + 1)^2$ and $e^x$:
   \begin{align}
   f'(x) &= (x^2 + 1)^2 e^x \left[ 6x + (x^2 + 1) \right] \\
   &= (x^2 + 1)^2 (x^2 + 6x + 1) e^x.
   \end{align}

---

## Result

$$
\text{Plan: Product rule for the whole expression; chain rule for the factor } (x^2+1)^3
$$

$$
f'(x) = (x^2 + 1)^2 (x^2 + 6x + 1) e^x
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the derivative by logarithmic differentiation:
$$
\ln f(x) = 3\ln(x^2 + 1) + x
$$
Differentiating both sides with respect to $x$:
$$
\frac{f'(x)}{f(x)} = 3 \cdot \frac{2x}{x^2 + 1} + 1 = \frac{6x + (x^2 + 1)}{x^2 + 1} = \frac{x^2 + 6x + 1}{x^2 + 1}
$$
Multiplying both sides by $f(x) = (x^2 + 1)^3 e^x$:
$$
f'(x) = (x^2 + 1)^3 e^x \cdot \frac{x^2 + 6x + 1}{x^2 + 1} = (x^2 + 1)^2 (x^2 + 6x + 1) e^x
$$
This independently confirms the result.

**Pass 2 — Numerical check:** Evaluate at $x = 0$:
$$
f(0) = (0^2 + 1)^3 e^0 = 1, \quad f'(0) = (0 + 1)^2 (0 + 0 + 1) e^0 = 1
$$
Compute forward difference quotient with $h = 0.001$:
$f(0.001) = ((0.001)^2 + 1)^3 e^{0.001} \approx (1 + 3 \times 10^{-6})(1.0010005) \approx 1.0010035$.
$$
\frac{f(0.001) - f(0)}{0.001} = \frac{1.0010035 - 1}{0.001} \approx 1.0035 \approx 1 = f'(0)
$$

**Pass 3 — Consistency check:** Since $(x^2+1)^2 > 0$ and $e^x > 0$ for all real $x$, the zeros of $f'(x)$ are determined solely by the quadratic term $x^2 + 6x + 1 = 0$. The roots are $x = \frac{-6 \pm \sqrt{36 - 4}}{2} = -3 \pm 2\sqrt{2}$. Since $\sqrt{2} \approx 1.414$, the roots are approximately $-0.172$ and $-5.828$. Between these roots, the quadratic is negative, so $f'(x) < 0$; for $x > -3 + 2\sqrt{2}$, $f'(x) > 0$. At $x = 0 > -3+2\sqrt{2}$, $f'(0) = 1 > 0$, consistent with the sign structure.

---

## Exam tip

Do not expand powers like $(x^2+1)^3$ before differentiating; factor out the lowest common power $(x^2+1)^2$ directly from both terms instead.

# Exercise 5

**Problem:** For
$$f(x)=(3x^2-2x+1)^5$$
identify the inner and outer functions, compute their derivatives, and combine the result according to the chain rule. Explain the origin of the additional factor.

---

## Relevant theorem / definition

The chain rule states that if $y = g(u)$ is differentiable at $u = u(x)$ and $u(x)$ is differentiable at $x$, then the composite function $f(x) = (g \circ u)(x) = g(u(x))$ is differentiable at $x$, and its derivative is:
$$
f'(x) = g'(u(x)) \cdot u'(x) = \frac{dg}{du} \cdot \frac{du}{dx}
$$

---

## Solution

1. Identify inner and outer functions:
   - Inner function: $u(x) = 3x^2 - 2x + 1$
   - Outer function: $g(u) = u^5$, so that $f(x) = g(u(x))$

2. Compute individual derivatives:
   - Derivative of outer function with respect to $u$:
     $$
     g'(u) = \frac{dg}{du} = 5u^4
     $$
   - Derivative of inner function with respect to $x$:
     $$
     u'(x) = \frac{du}{dx} = \frac{d}{dx}(3x^2 - 2x + 1) = 6x - 2
     $$

3. Combine using the chain rule:
   \begin{align}
   f'(x) &= g'(u(x)) \cdot u'(x) \\
   &= 5(3x^2 - 2x + 1)^4 \cdot (6x - 2) \\
   &= 10(3x - 1)(3x^2 - 2x + 1)^4.
   \end{align}

4. Explain the origin of the additional factor:
   The outer function $g(u) = u^5$ scales changes in its argument by $g'(u) = 5u^4$. However, the argument $u$ is not the independent variable $x$; it is itself a function of $x$. A small change $\Delta x$ causes an intermediate change $\Delta u \approx u'(x)\Delta x = (6x - 2)\Delta x$. In turn, this change $\Delta u$ propagates through the outer power function to yield $\Delta f \approx g'(u)\Delta u \approx 5u^4 \cdot (6x - 2)\Delta x$. The additional factor $(6x - 2)$ is therefore $u'(x)$, representing the internal rate of change of the inner layer.

---

## Result

$$
u(x) = 3x^2 - 2x + 1, \quad g(u) = u^5
$$

$$
g'(u) = 5u^4, \quad u'(x) = 6x - 2
$$

$$
f'(x) = 5(3x^2 - 2x + 1)^4(6x - 2) = 10(3x - 1)(3x^2 - 2x + 1)^4
$$

---

## Verification

**Pass 1 — Algebraic check:** Consider the quadratic expression $u(x) = 3x^2 - 2x + 1$. Its discriminant is $\Delta = (-2)^2 - 4(3)(1) = 4 - 12 = -8 < 0$, meaning $u(x) > 0$ for all real $x$. Since $u(x) > 0$, the factor $(3x^2 - 2x + 1)^4$ is strictly positive for all $x$. Thus $f'(x) = 0$ if and only if $6x - 2 = 0 \iff x = \frac{1}{3}$. This matches the location of the vertex and minimum of $u(x)$ at $x = -\frac{-2}{2(3)} = \frac{1}{3}$.

**Pass 2 — Numerical check:** Evaluate at $x = 0$:
$$
u(0) = 1, \quad f(0) = 1^5 = 1
$$
$$
f'(0) = 5(1)^4(6(0) - 2) = 5(1)(-2) = -10
$$
Compute forward difference quotient with $h = 0.001$:
$u(0.001) = 3(0.001)^2 - 2(0.001) + 1 = 0.000003 - 0.002 + 1 = 0.998003$.
$f(0.001) = (0.998003)^5 \approx 0.9900598$.
$$
\frac{f(0.001) - f(0)}{0.001} = \frac{0.9900598 - 1}{0.001} \approx -9.940 \approx -10 = f'(0)
$$

**Pass 3 — Consistency check:** For a power of 2, expanding $((3x^2-2x+1)^2)'$ yields $2(3x^2-2x+1)(6x-2) = (6x-2)(6x^2-4x+2)$, which equals the term-by-term derivative of $9x^4 - 12x^3 + 10x^2 - 4x + 1 \implies 36x^3 - 36x^2 + 20x - 4$. The chain rule scales identically to the 5th power.

---

## Exam tip

Enclose the inner derivative in parentheses when writing the product, writing $\cdot (6x - 2)$ to avoid mistakenly treating the subtraction as an external operation.

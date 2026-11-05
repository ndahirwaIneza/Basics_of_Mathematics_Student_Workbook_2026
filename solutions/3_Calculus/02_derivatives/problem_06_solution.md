# Exercise 6

**Problem:** For
$$f(x)=x\sin x+\cos x$$
compute the derivative and simplify the result. Then compute $f'(0)$ and interpret the direction of the tangent line at that point.

---

## Relevant theorem / definition

The product rule states that $(uv)' = u'v + uv'$. The standard trigonometric derivatives are:
$$
\frac{d}{dx}(\sin x) = \cos x, \quad \frac{d}{dx}(\cos x) = -\sin x
$$
A tangent line with slope $m = f'(x_0) = 0$ is horizontal (parallel to the $x$-axis).

---

## Solution

1. Differentiate using the sum rule and product rule:
   Apply the product rule to the first term $x\sin x$, where $u(x) = x$ and $v(x) = \sin x$:
   $$
   \frac{d}{dx}(x\sin x) = (1)\sin x + x(\cos x) = \sin x + x\cos x.
   $$
   Differentiate the second term:
   $$
   \frac{d}{dx}(\cos x) = -\sin x.
   $$

2. Combine and simplify:
   \begin{align}
   f'(x) &= (\sin x + x\cos x) + (-\sin x) \\
   &= \sin x + x\cos x - \sin x \\
   &= x\cos x.
   \end{align}

3. Compute $f'(0)$:
   $$
   f'(0) = 0 \cdot \cos(0) = 0 \cdot 1 = 0.
   $$

4. Interpret the direction of the tangent line:
   The slope of the tangent line at $x = 0$ is $m = f'(0) = 0$. A slope of zero indicates that the tangent line is horizontal (parallel to the $x$-axis). The point of tangency is $(0, f(0)) = (0, 0\sin 0 + \cos 0) = (0, 1)$, and the equation of the tangent line is:
   $$
   y = 1.
   $$

---

## Result

$$
f'(x) = x\cos x
$$

$$
f'(0) = 0
$$

$$
\text{Interpretation: The tangent line at } (0, 1) \text{ is horizontal (slope } m = 0\text{) with equation } y = 1.
$$

---

## Verification

**Pass 1 — Algebraic check:** Integrate $f'(x) = x\cos x$ using integration by parts:
Let $u = x$ and $dv = \cos x\,dx$, so $du = dx$ and $v = \sin x$:
$$
\int x\cos x\,dx = x\sin x - \int \sin x\,dx = x\sin x - (-\cos x) + C = x\sin x + \cos x + C
$$
Setting $C = 0$ returns the original function $f(x)$.

**Pass 2 — Numerical check:** Compute the symmetric difference quotient at $x = 0$ with $h = 0.01$:
$f(0.01) = 0.01\sin(0.01) + \cos(0.01) \approx 0.01(0.0099998) + 0.9999500 = 0.0001000 + 0.9999500 = 1.0000500$.
$f(-0.01) = (-0.01)\sin(-0.01) + \cos(-0.01) = 0.01\sin(0.01) + \cos(0.01) \approx 1.0000500$.
$$
\frac{f(0.01) - f(-0.01)}{2(0.01)} = \frac{1.0000500 - 1.0000500}{0.02} = 0.000 = f'(0)
$$

**Pass 3 — Consistency check:** The function $f(x)$ is even:
$$
f(-x) = (-x)\sin(-x) + \cos(-x) = (-x)(-\sin x) + \cos x = x\sin x + \cos x = f(x).
$$
The derivative of any differentiable even function is necessarily odd:
$$
f'(-x) = (-x)\cos(-x) = -x\cos x = -f'(x).
$$
Any continuous odd function defined at $0$ must satisfy $f'(0) = 0$, confirming the zero slope.

---

## Exam tip

Cancel opposing terms like $\sin x - \sin x$ immediately; product rule problems in trigonometry frequently produce compact cancellations.

# Exercise 7

**Problem:** For
$$f(x)=\sin(x^2+1)$$
compute the derivative. Explicitly identify the outer function, the inner function, and the derivative of the inner function. Finally, determine the sign of $f'(0)$.

---

## Relevant theorem / definition

The chain rule states that if $f(x) = g(u(x))$, then:
$$
f'(x) = g'(u(x)) \cdot u'(x)
$$
The derivative of the sine function is $\frac{d}{du}(\sin u) = \cos u$. A derivative value of zero is neutral in sign (neither strictly positive nor strictly negative).

---

## Solution

1. Identify components of the composition:
   - Outer function: $g(u) = \sin u$
   - Inner function: $u(x) = x^2 + 1$

2. Compute individual derivatives:
   - Derivative of the outer function with respect to $u$:
     $$
     g'(u) = \frac{dg}{du} = \cos u
     $$
   - Derivative of the inner function with respect to $x$:
     $$
     u'(x) = \frac{du}{dx} = \frac{d}{dx}(x^2 + 1) = 2x
     $$

3. Combine according to the chain rule:
   \begin{align}
   f'(x) &= g'(u(x)) \cdot u'(x) \\
   &= \cos(x^2 + 1) \cdot 2x \\
   &= 2x \cos(x^2 + 1).
   \end{align}

4. Compute $f'(0)$ and determine its sign:
   $$
   f'(0) = 2(0) \cos(0^2 + 1) = 0 \cdot \cos(1) = 0.
   $$
   The value $f'(0) = 0$ is zero. It is neither positive nor negative; geometrically, the tangent line to the graph at $(0, \sin(1))$ is horizontal.

---

## Result

$$
\text{Outer function: } g(u) = \sin u, \quad \text{Inner function: } u(x) = x^2 + 1
$$

$$
u'(x) = 2x
$$

$$
f'(x) = 2x \cos(x^2 + 1)
$$

$$
f'(0) = 0 \quad (\text{zero: neither positive nor negative})
$$

---

## Verification

**Pass 1 — Algebraic check:** The function $f(x) = \sin(x^2+1)$ is an even function:
$$
f(-x) = \sin((-x)^2 + 1) = \sin(x^2 + 1) = f(x).
$$
Its derivative is:
$$
f'(-x) = 2(-x)\cos((-x)^2 + 1) = -2x\cos(x^2 + 1) = -f'(x).
$$
Because $f'(x)$ is an odd function defined everywhere on $\mathbb{R}$, evaluating at $x = 0$ gives $f'(0) = -f'(0) \implies 2f'(0) = 0 \implies f'(0) = 0$.

**Pass 2 — Numerical check:** Evaluate symmetric difference quotient at $x = 0$ with $h = 0.01$:
$f(0.01) = \sin((0.01)^2 + 1) = \sin(1.0001) \approx 0.8415250$.
$f(-0.01) = \sin((-0.01)^2 + 1) = \sin(1.0001) \approx 0.8415250$.
$$
\frac{f(0.01) - f(-0.01)}{2(0.01)} = \frac{0.8415250 - 0.8415250}{0.02} = 0.000 = f'(0)
$$

**Pass 3 — Consistency check:** For small $x > 0$ such that $x^2 + 1 < \frac{\pi}{2} \approx 1.5708$ (which holds for $0 < x < \sqrt{\pi/2 - 1} \approx 0.755$), the term $\cos(x^2+1) > 0$. Since $2x > 0$, the product $f'(x) = 2x\cos(x^2+1) > 0$. For small $x < 0$, $2x < 0$ and $\cos(x^2+1) > 0$, so $f'(x) < 0$. The derivative changes sign from negative to positive across $x = 0$, confirming a local minimum at $(0, \sin(1))$ where $f'(0) = 0$.

---

## Exam tip

Do not differentiate the angle inside the cosine; the chain rule yields $\cos(x^2+1) \cdot 2x$, not $\cos(2x)$.

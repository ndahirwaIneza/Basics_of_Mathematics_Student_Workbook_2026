# Exercise 4

**Problem:** For
$$f(x)=\frac{x^2+1}{x-1}$$
determine the domain, compute the derivative, simplify the result, and explain why the restriction $x\neq1$ remains important.

---

## Relevant theorem / definition

The quotient rule for two differentiable functions $u(x)$ and $v(x)$ with $v(x) \neq 0$ states:
$$
\frac{d}{dx}\left[\frac{u(x)}{v(x)}\right] = \frac{u'(x)v(x) - u(x)v'(x)}{[v(x)]^2}
$$
The domain of a rational function consists of all real numbers where the denominator is non-zero. Differentiability requires that the function be defined and continuous on a neighborhood around the point.

---

## Solution

1. Determine the domain:
   The denominator cannot equal zero:
   $$
   x - 1 \neq 0 \implies x \neq 1.
   $$
   Therefore:
   $$
   D_f = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, \infty).
   $$

2. Compute the derivative using the quotient rule:
   Let $u(x) = x^2 + 1$ and $v(x) = x - 1$.
   Differentiate the components:
   $$
   u'(x) = 2x, \quad v'(x) = 1.
   $$
   Apply the quotient rule formula:
   \begin{align}
   f'(x) &= \frac{u'(x)v(x) - u(x)v'(x)}{[v(x)]^2} \\
   &= \frac{(2x)(x - 1) - (x^2 + 1)(1)}{(x - 1)^2}.
   \end{align}

3. Simplify the numerator:
   \begin{align}
   f'(x) &= \frac{2x^2 - 2x - x^2 - 1}{(x - 1)^2} \\
   &= \frac{x^2 - 2x - 1}{(x - 1)^2}.
   \end{align}
   Alternatively, expressing using the completed square in the numerator:
   $$
   x^2 - 2x - 1 = (x - 1)^2 - 2 \implies f'(x) = 1 - \frac{2}{(x - 1)^2}.
   $$

4. Explain why the restriction $x \neq 1$ remains important:
   At $x = 1$, the function $f(x)$ is not defined because division by zero has no meaning in the real numbers; geometrically, the curve has a vertical asymptote at $x = 1$. A function cannot have a derivative (a rate of change or tangent line) at a point where the function itself does not exist. The derivative formula also has $(x-1)^2$ in its denominator, so $D_{f'} = \mathbb{R} \setminus \{1\}$. Retaining $x \neq 1$ prevents erroneous substitution into $f'$ and enforces the mathematical principle that the domain of a derivative can never exceed the domain of the parent function.

---

## Result

$$
D_f = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, \infty)
$$

$$
f'(x) = \frac{x^2 - 2x - 1}{(x - 1)^2} = 1 - \frac{2}{(x - 1)^2}
$$

$$
D_{f'} = \mathbb{R} \setminus \{1\}
$$

---

## Verification

**Pass 1 — Algebraic check:** Rewrite $f(x)$ via polynomial division before differentiating:
$$
f(x) = \frac{(x^2 - 1) + 2}{x - 1} = \frac{(x - 1)(x + 1) + 2}{x - 1} = x + 1 + 2(x - 1)^{-1}
$$
Differentiating directly using the power rule and chain rule:
$$
f'(x) = 1 + 0 + 2(-1)(x - 1)^{-2}(1) = 1 - \frac{2}{(x - 1)^2} = \frac{(x - 1)^2 - 2}{(x - 1)^2} = \frac{x^2 - 2x - 1}{(x - 1)^2}
$$
This matches the quotient rule result identically.

**Pass 2 — Numerical check:** Evaluate at $x = 3$:
$$
f(3) = \frac{3^2 + 1}{3 - 1} = \frac{10}{2} = 5, \quad f'(3) = 1 - \frac{2}{(3 - 1)^2} = 1 - \frac{2}{4} = 0.5
$$
Evaluate forward difference quotient with $h = 0.001$:
$f(3.001) = \frac{(3.001)^2 + 1}{3.001 - 1} = \frac{9.006001 + 1}{2.001} = \frac{10.006001}{2.001} \approx 5.00050025$.
$$
\frac{f(3.001) - f(3)}{0.001} = \frac{5.00050025 - 5}{0.001} \approx 0.50025 \approx 0.5 = f'(3)
$$

**Pass 3 — Consistency check:** As $x \to \pm\infty$, the term $\frac{2}{(x-1)^2} \to 0$, so $f'(x) \to 1$. This is consistent with the oblique asymptote $y = x + 1$, which has slope $m = 1$.

---

## Exam tip

Distribute the negative sign across all terms of the second product $-u(x)v'(x)$ inside the quotient rule numerator to avoid a common sign error.

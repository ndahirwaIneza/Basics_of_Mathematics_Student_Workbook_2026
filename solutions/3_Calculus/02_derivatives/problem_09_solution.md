# Exercise 9

**Problem:** For
$$f(x)=\ln(x^2+1)$$
compute the derivative. Then determine the sign of $f'(x)$ for $x<0$, $x=0$, and $x>0$, and describe qualitatively how the function behaves around zero.

---

## Relevant theorem / definition

For a differentiable function $u(x) > 0$, the chain rule gives:
$$
\frac{d}{dx}[\ln(u(x))] = \frac{u'(x)}{u(x)}
$$
If $f'(x) < 0$ on an interval, $f$ is strictly decreasing on that interval; if $f'(x) > 0$, $f$ is strictly increasing. If $f'(x_0) = 0$ and $f'$ switches from negative to positive at $x_0$, $f$ has a local minimum at $x_0$.

---

## Solution

1. Compute the derivative:
   The argument $u(x) = x^2 + 1$ satisfies $x^2 + 1 \ge 1 > 0$ for all $x \in \mathbb{R}$, so the natural logarithm is defined on all of $\mathbb{R}$.
   The derivative of the inner function is:
   $$
   u'(x) = \frac{d}{dx}(x^2 + 1) = 2x.
   $$
   Applying the logarithmic chain rule:
   $$
   f'(x) = \frac{u'(x)}{u(x)} = \frac{2x}{x^2 + 1}.
   $$

2. Determine the sign of $f'(x)$:
   Because $x^2 + 1 > 0$ for all real $x$, the sign of the quotient is identical to the sign of the numerator $2x$:
   - For $x < 0$: $2x < 0$, so $f'(x) < 0$.
   - For $x = 0$: $2(0) = 0$, so $f'(0) = 0$.
   - For $x > 0$: $2x > 0$, so $f'(x) > 0$.

3. Describe qualitative behavior around zero:
   - For $x < 0$, $f'(x) < 0$, so the function is strictly decreasing as $x$ approaches zero from the left.
   - At $x = 0$, $f'(0) = 0$, meaning the tangent line to the graph at $(0, f(0)) = (0, \ln 1) = (0, 0)$ is horizontal.
   - For $x > 0$, $f'(x) > 0$, so the function is strictly increasing as $x$ moves away from zero to the right.
   - By the first derivative test, $f$ attains a strict global minimum at $(0, 0)$. In the immediate neighborhood of $x = 0$, the graph forms a smooth symmetric basin (parabolic valley) opening upward, tangent to the $x$-axis.

---

## Result

$$
f'(x) = \frac{2x}{x^2 + 1}
$$

$$
\text{Signs: } f'(x) < 0 \text{ for } x < 0, \quad f'(0) = 0, \quad f'(x) > 0 \text{ for } x > 0
$$

$$
\text{Qualitative behavior: Strictly decreasing on } (-\infty, 0), \text{ horizontal tangent and strict global minimum at } (0,0), \text{ strictly increasing on } (0, \infty).
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the second derivative using the quotient rule:
$$
f''(x) = \frac{2(x^2 + 1) - 2x(2x)}{(x^2 + 1)^2} = \frac{2x^2 + 2 - 4x^2}{(x^2 + 1)^2} = \frac{2(1 - x^2)}{(x^2 + 1)^2}
$$
At $x = 0$:
$$
f''(0) = \frac{2(1 - 0)}{(0 + 1)^2} = 2 > 0
$$
Since $f'(0) = 0$ and $f''(0) = 2 > 0$, the second derivative test independently confirms a strict local minimum at $x = 0$.

**Pass 2 — Numerical check:** Evaluate at $x = 1$:
$$
f(1) = \ln(2) \approx 0.693147, \quad f'(1) = \frac{2(1)}{1^2 + 1} = 1
$$
Evaluate forward difference quotient with $h = 0.001$:
$f(1.001) = \ln((1.001)^2 + 1) = \ln(2.002001) \approx 0.694147$.
$$
\frac{f(1.001) - f(1)}{0.001} = \frac{0.694147 - 0.693147}{0.001} = \frac{0.001000}{0.001} = 1.000 = f'(1)
$$

**Pass 3 — Consistency check:** Since $x^2 \ge 0$, $x^2 + 1 \ge 1$, which implies $f(x) = \ln(x^2+1) \ge \ln(1) = 0$ for all real $x$. The minimum value is 0, which occurs precisely when $x = 0$. This confirms algebraically that $(0,0)$ is the global minimum.

---

## Exam tip

For any expression of the form $\ln(g(x))$, write $\frac{g'(x)}{g(x)}$ in one direct step without writing an intermediate reciprocal.

# Exercise 2

**Problem:** For
$$f(x)=2\sqrt{x}-\frac{3}{x^2}+x^{3/2}$$
1. rewrite the function using powers,
2. determine the domain,
3. compute the derivative,
4. compare the domain of the function with the domain of its derivative.

---

## Relevant theorem / definition

Radicals and fractions rewrite as powers via $\sqrt[m]{x^k} = x^{k/m}$ and $\frac{1}{x^k} = x^{-k}$. The power rule gives:
$$
\frac{d}{dx}(x^p) = p x^{p-1} \quad (p \in \mathbb{R})
$$
The domain $D_f$ of a function is the set of all real numbers for which each term is defined. A function is differentiable only at interior points of its domain where the derivative limit exists.

---

## Solution

1. Rewrite using powers:
   Using $\sqrt{x} = x^{1/2}$ and $\frac{1}{x^2} = x^{-2}$:
   $$
   f(x) = 2x^{1/2} - 3x^{-2} + x^{3/2}.
   $$

2. Determine the domain of $f$:
   - The terms $2\sqrt{x} = 2x^{1/2}$ and $x^{3/2}$ require $x \ge 0$.
   - The term $-\frac{3}{x^2} = -3x^{-2}$ requires a non-zero denominator: $x \neq 0$.
   Intersecting these conditions:
   $$
   D_f = [0, \infty) \cap (\mathbb{R} \setminus \{0\}) = (0, \infty).
   $$

3. Compute the derivative:
   Differentiate term-by-term using the power rule:
   \begin{align}
   f'(x) &= 2\left(\frac{1}{2}x^{1/2 - 1}\right) - 3\left(-2x^{-2 - 1}\right) + \frac{3}{2}x^{3/2 - 1} \\
   &= x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2} \\
   &= \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}.
   \end{align}

4. Compare the domains of $f$ and $f'$:
   In $f'(x) = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}$:
   - $\frac{1}{\sqrt{x}}$ requires $x > 0$.
   - $\frac{6}{x^3}$ requires $x \neq 0$.
   - $\frac{3}{2}\sqrt{x}$ requires $x \ge 0$.
   Intersecting these conditions gives:
   $$
   D_{f'} = (0, \infty).
   $$
   Comparing with $D_f = (0, \infty)$, we have $D_f = D_{f'}$. While the derivative of $\sqrt{x}$ alone typically loses the endpoint $x = 0$ because its derivative $\frac{1}{2\sqrt{x}}$ diverges at zero, here $x = 0$ was already excluded from the domain of $f$ due to the singular term $-\frac{3}{x^2}$. Consequently, the two domains coincide.

---

## Result

$$
f(x) = 2x^{1/2} - 3x^{-2} + x^{3/2}
$$

$$
D_f = (0, \infty)
$$

$$
f'(x) = x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2} = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}
$$

$$
D_{f'} = (0, \infty) = D_f
$$

---

## Verification

**Pass 1 — Algebraic check:** Integrate $f'(x) = x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2}$:
$$
\int \left(x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2}\right) dx = \frac{x^{1/2}}{1/2} + 6\frac{x^{-2}}{-2} + \frac{3}{2}\frac{x^{3/2}}{3/2} + C = 2x^{1/2} - 3x^{-2} + x^{3/2} + C
$$
This recovers $f(x)$ identically.

**Pass 2 — Numerical check:** At $x = 1$:
$$
f(1) = 2(1) - 3(1) + 1 = 0, \quad f'(1) = 1 + 6 + 1.5 = 8.5
$$
With $h = 0.001$:
$f(1.001) = 2\sqrt{1.001} - 3(1.001)^{-2} + (1.001)^{1.5} \approx 2(1.00049988) - 3(0.99800499) + 1.00150037 = 0.00848512$.
The forward difference quotient is:
$$
\frac{f(1.001) - f(1)}{0.001} = \frac{0.00848512}{0.001} \approx 8.485 \approx 8.5 = f'(1)
$$

**Pass 3 — Consistency check:** For any $x > 0$, every term in $f'(x) = x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2}$ is strictly positive because positive bases raised to any real power remain positive. Thus $f'(x) > 0$ on $(0, \infty)$, confirming that $f(x)$ is strictly increasing on its entire domain.

---

## Exam tip

When differentiating negative exponents, subtract 1 correctly: $-2 - 1 = -3$, not $-1$.

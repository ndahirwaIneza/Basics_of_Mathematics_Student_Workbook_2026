# Exercise 9

**Problem:** Analyze the asymptotes of

$$
f(x)=\frac{x^2+1}{x-1}.
$$

Perform polynomial division and explain why the remainder term vanishes for large $|x|$.

---

## Relevant theorem / definition

1. Vertical asymptote: The line $x = x_0$ is a vertical asymptote of $f$ if at least one of the one-sided limits $\lim_{x \to x_0^\pm} f(x)$ is $\pm\infty$.
2. Oblique (slant) asymptote: The straight line $y = mx + b$ is an oblique asymptote of $f(x)$ as $x \to \infty$ (or $x \to -\infty$) if and only if:

$$
   \lim_{x \to \pm\infty} [f(x) - (mx + b)] = 0
$$

   Equivalently, the parameters can be calculated via limits:

$$
   m = \lim_{x \to \pm\infty} \frac{f(x)}{x}, \qquad b = \lim_{x \to \pm\infty} [f(x) - mx]
$$

3. Polynomial decomposition: If rational function $f(x) = \frac{P(x)}{Q(x)}$ has $\deg(P) = \deg(Q) + 1$, polynomial long division gives $f(x) = mx + b + \frac{R(x)}{Q(x)}$, where $\deg(R) < \deg(Q)$.

---

## Solution

1. Domain:
   The denominator vanishes when $x - 1 = 0 \implies x = 1$.
   Thus, the domain is:

$$
   D = (-\infty, 1) \cup (1, \infty)
$$

2. Vertical asymptote:
   Evaluate the one-sided limits at $x = 1$:

$$
   \lim_{x \to 1^-} \frac{x^2 + 1}{x - 1} = \left[\frac{1^2 + 1}{0^-}\right] = \left[\frac{2}{0^-}\right] = -\infty
$$

$$
   \lim_{x \to 1^+} \frac{x^2 + 1}{x - 1} = \left[\frac{1^2 + 1}{0^+}\right] = \left[\frac{2}{0^+}\right] = +\infty
$$

   Since both one-sided limits are infinite, the vertical line $x = 1$ is a two-sided vertical asymptote.

3. Polynomial division:
   Divide the numerator $x^2 + 1$ by the denominator $x - 1$:

$$
   \begin{align}
   x^2 + 1 &= (x^2 - x) + (x + 1) \\
   &= x(x - 1) + (x - 1) + 2 \\
   &= (x + 1)(x - 1) + 2
   \end{align}
$$

   Dividing both sides by $x - 1$ produces the decomposition:

$$
   f(x) = \frac{x^2 + 1}{x - 1} = x + 1 + \frac{2}{x - 1}
$$

   Here, the polynomial quotient is the linear expression $q(x) = x + 1$, and the remainder is the constant $r(x) = 2$.

4. Oblique asymptote identification:
   Consider the linear candidate $y = x + 1$.
   Compute the difference between $f(x)$ and $y = x + 1$:

$$
   f(x) - (x + 1) = \left(x + 1 + \frac{2}{x - 1}\right) - (x + 1) = \frac{2}{x - 1}
$$

   Evaluate the limit of this difference as $x \to \infty$ and $x \to -\infty$:

$$
   \lim_{x \to \infty} [f(x) - (x + 1)] = \lim_{x \to \infty} \frac{2}{x - 1} = 0
$$

$$
   \lim_{x \to -\infty} [f(x) - (x + 1)] = \lim_{x \to -\infty} \frac{2}{x - 1} = 0
$$

   Because the difference approaches zero at both infinities, the line:

$$
   y = x + 1
$$

   is an oblique asymptote of $f(x)$ both as $x \to \infty$ and as $x \to -\infty$.
   Since the degree of the numerator exceeds the degree of the denominator, no horizontal asymptotes exist ($\lim_{x \to \pm\infty} f(x) = \pm\infty$).

5. Explanation of why the remainder term vanishes for large $|x|$:
   In the decomposed form $f(x) = (x + 1) + \frac{2}{x - 1}$, the remainder term is $\frac{2}{x - 1}$.
   - Degree disparity: The remainder polynomial has degree $0$ (constant value 2), whereas the divisor has degree $1$ ($x - 1$).
   - Limiting behavior: As $|x|$ becomes arbitrarily large ($|x| \to \infty$), the denominator $|x - 1|$ grows without bound towards $\infty$, while the numerator remains fixed at $2$. Therefore, the quotient $\frac{2}{x - 1}$ approaches 0:

$$
     \lim_{|x| \to \infty} \left|\frac{2}{x - 1}\right| = \left[\frac{2}{\infty}\right] = 0
$$

   - Geometric meaning: The vertical distance between the curve $y = f(x)$ and the line $y = x + 1$ is precisely $\left|\frac{2}{x - 1}\right|$. As $|x|$ increases, this gap shrinks to zero, meaning the graph of $f(x)$ becomes indistinguishable from the straight line $y = x + 1$.
   - Relative position:
     For $x > 1$, $\frac{2}{x - 1} > 0$, so the curve approaches the oblique asymptote from above ($f(x) > x + 1$).
     For $x < 1$, $\frac{2}{x - 1} < 0$, so the curve approaches the oblique asymptote from below ($f(x) < x + 1$).

---

## Result

$$
\text{Vertical asymptote: } x = 1
$$

$$
\text{Oblique asymptote: } y = x + 1 \quad (\text{as } x \to \infty \text{ and } x \to -\infty)
$$

$$
\text{Decomposition: } f(x) = x + 1 + \frac{2}{x - 1}
$$

---

## Verification

**Pass 1 — Algebraic check:** Verify the oblique asymptote using the general limit formulas:

$$
m = \lim_{x \to \pm\infty} \frac{f(x)}{x} = \lim_{x \to \pm\infty} \frac{x^2 + 1}{x^2 - x} = \lim_{x \to \pm\infty} \frac{1 + \frac{1}{x^2}}{1 - \frac{1}{x}} = 1
$$

$$
b = \lim_{x \to \pm\infty} [f(x) - 1 \cdot x] = \lim_{x \to \pm\infty} \left(\frac{x^2 + 1 - x(x - 1)}{x - 1}\right) = \lim_{x \to \pm\infty} \frac{x + 1}{x - 1} = 1
$$

This independently reproduces the line $y = x + 1$.

**Pass 2 — Numerical check:** Evaluate $f(x)$ and the asymptote $y = x + 1$ for large values of $x$:
- For $x = 101$: $f(101) = \frac{101^2 + 1}{100} = \frac{10202}{100} = 102.02$, while $y(101) = 101 + 1 = 102$. The error is $0.02 = \frac{2}{100}$.
- For $x = -99$: $f(-99) = \frac{(-99)^2 + 1}{-100} = \frac{9802}{-100} = -98.02$, while $y(-99) = -99 + 1 = -98$. The error is $-0.02 = \frac{2}{-100}$.

**Pass 3 — Consistency check:** Check whether $f(x)$ ever intersects its oblique asymptote:

$$
f(x) = x + 1 \iff x + 1 + \frac{2}{x - 1} = x + 1 \iff \frac{2}{x - 1} = 0
$$

Since $\frac{2}{x - 1} = 0$ has no real solution, the graph never crosses the oblique asymptote, which is fully consistent with the non-vanishing constant remainder.

---

## Exam tip

Whenever the degree of the numerator is exactly 1 higher than the degree of the denominator, use polynomial division immediately to find both the oblique asymptote and the position of the curve relative to it.

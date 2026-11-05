# Exercise 4

**Problem:** Analyze

$$
f(x)=\frac1{x^2-1}.
$$

Determine the domain, asymptotes, sign, and monotonicity on the intervals of the domain. Explain why each interval must be analyzed separately.

---

## Relevant theorem / definition

1. Domain of a rational expression: The set of all real numbers where the denominator is non-zero.
2. Sign of a rational function: Determined by the signs of its factors across its zeros and poles.
3. Monotonicity theorem: A differentiable function with $f'(x) > 0$ (respectively $f'(x) < 0$) on an interval $I$ is strictly increasing (respectively strictly decreasing) on $I$. This theorem applies to connected intervals only.
4. Vertical and horizontal asymptotes: Limits of the form $x \to x_0^\pm$ yielding $\pm\infty$ establish vertical asymptotes; limits of the form $x \to \pm\infty$ yielding a finite value $L$ establish the horizontal asymptote $y = L$.

---

## Solution

1. Domain:
   The denominator must not vanish:

$$
   x^2 - 1 \neq 0 \iff (x - 1)(x + 1) \neq 0 \iff x \neq -1 \quad \text{and} \quad x \neq 1
$$

   Hence, the domain consists of three disconnected open intervals:

$$
   D = (-\infty, -1) \cup (-1, 1) \cup (1, \infty)
$$

   Note that $f(-x) = \frac{1}{(-x)^2 - 1} = \frac{1}{x^2 - 1} = f(x)$, so $f$ is an even function (symmetric about the $y$-axis).

2. Asymptotes:
   - Vertical asymptotes:
     Evaluate one-sided limits at the boundary points $x = -1$ and $x = 1$:

$$
     \lim_{x \to -1^-} \frac{1}{x^2 - 1} = \left[\frac{1}{0^+}\right] = +\infty, \qquad \lim_{x \to -1^+} \frac{1}{x^2 - 1} = \left[\frac{1}{0^-}\right] = -\infty
$$

$$
     \lim_{x \to 1^-} \frac{1}{x^2 - 1} = \left[\frac{1}{0^-}\right] = -\infty, \qquad \lim_{x \to 1^+} \frac{1}{x^2 - 1} = \left[\frac{1}{0^+}\right] = +\infty
$$

     Thus, the lines $x = -1$ and $x = 1$ are vertical asymptotes.
   - Horizontal asymptote:

$$
     \lim_{x \to \pm\infty} \frac{1}{x^2 - 1} = 0
$$

     Thus, the line $y = 0$ ($x$-axis) is a horizontal asymptote as $x \to -\infty$ and $x \to +\infty$.

3. Sign of the function:
   The numerator is always $1 > 0$. The sign of $f(x)$ is determined solely by $x^2 - 1$:
   - On $(-\infty, -1)$: $x^2 > 1 \implies x^2 - 1 > 0 \implies f(x) > 0$.
   - On $(-1, 1)$: $x^2 < 1 \implies x^2 - 1 < 0 \implies f(x) < 0$.
   - On $(1, \infty)$: $x^2 > 1 \implies x^2 - 1 > 0 \implies f(x) > 0$.
   There are no zeros because the numerator is never zero. The $y$-intercept is $f(0) = \frac{1}{0 - 1} = -1$.

4. First derivative and monotonicity:
   Differentiate using the chain rule:

$$
   f'(x) = \frac{d}{dx}\left[(x^2 - 1)^{-1}\right] = -(x^2 - 1)^{-2} \cdot 2x = -\frac{2x}{(x^2 - 1)^2}
$$

   For all $x \in D$, the denominator $(x^2 - 1)^2 > 0$. The sign of $f'(x)$ is determined solely by the numerator $-2x$:
   - On $(-\infty, -1)$: $x < 0 \implies -2x > 0 \implies f'(x) > 0$. The function is strictly increasing.
   - On $(-1, 0)$: $x < 0 \implies -2x > 0 \implies f'(x) > 0$. The function is strictly increasing.
   - At $x = 0$: $f'(0) = 0$. Since $f'$ changes from $+$ to $-$, $f$ has a local maximum at $x = 0$ with value $f(0) = -1$.
   - On $(0, 1)$: $x > 0 \implies -2x < 0 \implies f'(x) < 0$. The function is strictly decreasing.
   - On $(1, \infty)$: $x > 0 \implies -2x < 0 \implies f'(x) < 0$. The function is strictly decreasing.

   Monotonicity and sign summary table:

   | Interval / Point | $(-\infty, -1)$ | $x = -1$ | $(-1, 0)$ | $x = 0$ | $(0, 1)$ | $x = 1$ | $(1, \infty)$ |
   |:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
   | $f(x)$ | $+$ | Undef. | $-$ | $-1$ | $-$ | Undef. | $+$ |
   | $f'(x)$ | $+$ | Undef. | $+$ | $0$ | $-$ | Undef. | $-$ |
   | Shape | $\nearrow$ to $+\infty$ | Asymptote | $\nearrow$ from $-\infty$ | Local Max | $\searrow$ to $-\infty$ | Asymptote | $\searrow$ to $0^+$ |

5. Why each interval must be analyzed separately:
   The domain $D$ is the union of three pairwise disjoint open intervals separated by the points of discontinuity $x = -1$ and $x = 1$. The Mean Value Theorem, which establishes that a positive derivative implies an increasing function, requires the function to be continuous on a single connected interval $[a, b]$. Across points of discontinuity, this continuity breaks down.
   For example, taking $x_1 = 0.5 \in (0, 1)$ and $x_2 = 2 \in (1, \infty)$, we have $x_1 < x_2$, yet:

$$
   f(0.5) = -\frac{4}{3} \approx -1.33 < f(2) = \frac{1}{3} \approx 0.33
$$

   Even though $f'(x) < 0$ on both $(0, 1)$ and $(1, \infty)$, the function value jumps across the vertical asymptote. Therefore, assertions about monotonicity, boundedness, or extrema are valid only within each connected component of the domain individually.

---

## Result

$$
\text{Domain: } D = (-\infty, -1) \cup (-1, 1) \cup (1, \infty)
$$

$$
\text{Asymptotes: Vertical } x = -1 \text{ and } x = 1; \quad \text{Horizontal } y = 0
$$

$$
\text{Sign: } f(x) > 0 \text{ on } (-\infty, -1) \cup (1, \infty); \quad f(x) < 0 \text{ on } (-1, 1)
$$

$$
\text{Monotonicity: Strictly increasing on } (-\infty, -1) \text{ and on } (-1, 0];
$$

$$
\text{Strictly decreasing on } [0, 1) \text{ and on } (1, \infty)
$$

$$
\text{Local extremum: Local maximum at } (0, -1)
$$

---

## Verification

**Pass 1 — Algebraic check:** Symmetry verification: $f(-x) = \frac{1}{(-x)^2 - 1} = f(x)$ shows that $f$ is even, which algebraically guarantees that if $f$ is increasing on $(-\infty, -1)$, it must be decreasing on $(1, \infty)$, and if it increases on $(-1, 0)$, it must decrease on $(0, 1)$. This matches the derivative results identically.

**Pass 2 — Numerical check:** Evaluate test points: $f(-2) = \frac{1}{3} > 0$; $f(-0.5) = -\frac{4}{3} < 0$; $f(0) = -1$; $f(0.5) = -\frac{4}{3} < 0$; $f(2) = \frac{1}{3} > 0$. For monotonicity on $(-1, 0]$, $f(-0.5) = -1.33 < f(0) = -1$, confirming that $f$ increases towards 0.

**Pass 3 — Consistency check:** Second derivative check at the critical point:

$$
f''(x) = \frac{-2(x^2 - 1)^2 - (-2x) \cdot 2(x^2 - 1)(2x)}{(x^2 - 1)^4} = \frac{-2(x^2 - 1) + 8x^2}{(x^2 - 1)^3} = \frac{6x^2 + 2}{(x^2 - 1)^3}
$$

At $x = 0$, $f''(0) = \frac{2}{(-1)^3} = -2 < 0$, which confirms by the second derivative test that $(0, -1)$ is a strict local maximum.

---

## Exam tip

Monotonicity properties never bridge across vertical asymptotes; always state increasing/decreasing behavior on separate individual intervals.

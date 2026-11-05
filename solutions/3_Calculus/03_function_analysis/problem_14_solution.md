# Exercise 14

**Problem:** It is known that

$$
f'(x)=(x-1)(x+2).
$$

Determine the monotonicity and the locations of the extrema, and sketch a possible qualitative shape of the function. Then, for

$$
g(x)=\frac{x^3}{3}+\frac{x^2}{2}-2x
$$

verify that $g'(x)=(x-1)(x+2)$, and compare the specific graph with the earlier qualitative sketch.

---

## Relevant theorem / definition

1. First derivative test for monotonicity and extrema:
   - $f'(x) > 0$ on an interval implies $f$ is strictly increasing.
   - $f'(x) < 0$ on an interval implies $f$ is strictly decreasing.
   - A critical point where $f'$ changes sign from positive to negative is a local maximum; from negative to positive is a local minimum.
2. Indefinite integration / antiderivatives: If two differentiable functions have the same derivative ($f'(x) = g'(x)$) on an interval, they differ by an additive constant: $f(x) = g(x) + C$. The derivative determines the shape and horizontal locations of extrema, while $C$ determines the vertical translation.

---

## Solution

1. Monotonicity and extrema from $f'(x) = (x - 1)(x + 2)$:
   The zeros of $f'(x)$ are:

$$
   (x - 1)(x + 2) = 0 \implies x_1 = -2, \quad x_2 = 1
$$

   Expanding gives the quadratic $f'(x) = x^2 + x - 2$, which has a positive leading coefficient ($a = 1 > 0$). Thus, the parabola opens upward:
   - For $x \in (-\infty, -2)$: both factors $(x - 1) < 0$ and $(x + 2) < 0$, so $f'(x) > 0$. The function $f$ is strictly increasing.
   - For $x \in (-2, 1)$: $(x - 1) < 0$ and $(x + 2) > 0$, so $f'(x) < 0$. The function $f$ is strictly decreasing.
   - For $x \in (1, \infty)$: $(x - 1) > 0$ and $(x + 2) > 0$, so $f'(x) > 0$. The function $f$ is strictly increasing.

   Extrema:
   - At $x = -2$: $f'$ changes sign from $+$ to $-$. Therefore, $f$ has a local maximum at $x = -2$.
   - At $x = 1$: $f'$ changes sign from $-$ to $+$. Therefore, $f$ has a local minimum at $x = 1$.

2. Qualitative sketch of $f(x)$:
   Because $f'(x)$ is a quadratic with positive leading coefficient, any antiderivative $f(x)$ is a cubic polynomial with a positive leading coefficient.
   ```text
              y
              |          * (-2, f(-2)) [Local Max]
              |         / \
              |        /   \
   -----------+-------/-----*------------------> x
             /|      /       \     * (1, f(1)) [Local Min]
            / |     /         \___/ \
           /  |    /                 \
              |   /                   \
   ```
   Qualitative features:
   - Ascends from $-\infty$ as $x \to -\infty$.
   - Reaches a peak (local maximum) at $x = -2$ with a horizontal tangent.
   - Descends between $x = -2$ and $x = 1$, passing an inflection point at the midpoint $x = \frac{-2 + 1}{2} = -0.5$.
   - Reaches a trough (local minimum) at $x = 1$ with a horizontal tangent.
   - Ascends towards $+\infty$ as $x \to +\infty$.
   - The absolute vertical position is indeterminate: adding any constant $C$ shifts the entire graph vertically without altering slopes, critical points, or extrema locations.

3. Verification for $g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x$:
   Differentiate $g(x)$ term by term using the power rule:

$$
   \begin{align}
   g'(x) &= \frac{d}{dx}\left(\frac{x^3}{3}\right) + \frac{d}{dx}\left(\frac{x^2}{2}\right) - \frac{d}{dx}(2x) \\
   &= \frac{3x^2}{3} + \frac{2x}{2} - 2 \\
   &= x^2 + x - 2
   \end{align}
$$

   Factor the quadratic:

$$
   x^2 + x - 2 = (x - 1)(x + 2)
$$

   Therefore, $g'(x) = (x - 1)(x + 2) = f'(x)$, confirming that $g(x)$ is indeed a specific antiderivative of $f'(x)$ with integration constant $C = 0$.

4. Comparison of the specific graph of $g$ with the qualitative sketch:
   Evaluating $g(x)$ at landmark points fixes the specific vertical placement:
   - Value at the local maximum ($x = -2$):

$$
     g(-2) = \frac{(-2)^3}{3} + \frac{(-2)^2}{2} - 2(-2) = -\frac{8}{3} + 2 + 4 = -\frac{8}{3} + 6 = \frac{10}{3} \approx 3.333
$$

     Local maximum point: $\left(-2, \frac{10}{3}\right)$.
   - Value at the local minimum ($x = 1$):

$$
     g(1) = \frac{1^3}{3} + \frac{1^2}{2} - 2(1) = \frac{1}{3} + \frac{1}{2} - 2 = \frac{5}{6} - \frac{12}{6} = -\frac{7}{6} \approx -1.167
$$

     Local minimum point: $\left(1, -\frac{7}{6}\right)$.
   - $y$-intercept and origin crossing:

$$
     g(0) = 0
$$

     The graph passes directly through the origin $(0, 0)$ on its downward descent from the maximum to the minimum, with instantaneous slope $g'(0) = -2$.
   - Inflection point:

$$
     g''(x) = 2x + 1 = 0 \implies x = -\frac{1}{2}
$$

$$
     g\left(-\frac{1}{2}\right) = \frac{-1/8}{3} + \frac{1/4}{2} - 2\left(-\frac{1}{2}\right) = -\frac{1}{24} + \frac{1}{8} + 1 = \frac{13}{12} \approx 1.083
$$

   Comparison summary:
   The specific graph of $g$ perfectly realizes the qualitative sketch:
   - Monotonicity and critical locations are identical ($x = -2$ and $x = 1$).
   - The qualitative sketch allowed the curve to float vertically; the specific equation $g(x)$ pins the local maximum at height $+10/3$ (strictly above the $x$-axis) and the local minimum at height $-7/6$ (strictly below the $x$-axis).
   - Because $g(-2) > 0$ and $g(1) < 0$, the intermediate value theorem guarantees that the descending branch must cross the $x$-axis, which occurs precisely at $x = 0$.

---

## Result

$$
\text{Monotonicity: Strictly increasing on } (-\infty, -2] \text{ and on } [1, \infty)
$$

$$
\text{Strictly decreasing on } [-2, 1]
$$

$$
\text{Local maximum at } x = -2, \qquad \text{Local minimum at } x = 1
$$

$$
\text{Verification: } g'(x) = x^2 + x - 2 = (x - 1)(x + 2)
$$

$$
\text{Specific extrema of } g: \text{Max at } \left(-2, \frac{10}{3}\right), \quad \text{Min at } \left(1, -\frac{7}{6}\right)
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the second derivative of $g$: $g''(x) = 2x + 1$.
- At $x = -2$: $g''(-2) = 2(-2) + 1 = -3 < 0 \implies$ confirms strict local maximum.
- At $x = 1$: $g''(1) = 2(1) + 1 = +3 > 0 \implies$ confirms strict local minimum.

**Pass 2 — Numerical check:** Verify the change in function value using the Fundamental Theorem of Calculus:

$$
g(1) - g(-2) = \int_{-2}^1 (x^2 + x - 2)\,dx = \left[\frac{x^3}{3} + \frac{x^2}{2} - 2x\right]_{-2}^1 = -\frac{7}{6} - \frac{10}{3} = -\frac{27}{6} = -\frac{9}{2} = -4.5
$$

Direct subtraction of computed values: $-\frac{7}{6} - \frac{20}{6} = -\frac{27}{6} = -4.5$. The net decrease matches the integral of the derivative.

**Pass 3 — Consistency check:** Since $g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x$ has a local maximum at $10/3 > 0$ and a local minimum at $-7/6 < 0$, the curve must cross the $x$-axis 3 times (3 real roots). Factoring $g(x) = \frac{x}{6}(2x^2 + 3x - 12)$, the quadratic has discriminant $\Delta = 9 - 4(2)(-12) = 105 > 0$, confirming three distinct real roots ($x \approx -3.31, 0, 1.81$), fully consistent with the extrema lying on opposite sides of the $x$-axis.

---

## Exam tip

The derivative provides the complete horizontal geometry (extrema and monotonicity), while integration constants control vertical translation.

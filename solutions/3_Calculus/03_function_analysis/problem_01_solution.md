# Exercise 1

**Problem:** Analyze the monotonicity and extrema of

$$
f(x)=x^3-3x^2+2.
$$

Sketch the graph based on the results and mark the critical points.

---

## Relevant theorem / definition

Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$.
1. If $f'(x) > 0$ for all $x \in (a, b)$, then $f$ is strictly increasing on $[a, b]$.
2. If $f'(x) < 0$ for all $x \in (a, b)$, then $f$ is strictly decreasing on $[a, b]$.
3. First derivative test: If $f'(c) = 0$ (or $f'(c)$ does not exist) and $f'$ changes sign from positive to negative at $c$, then $f$ has a local maximum at $c$; if $f'$ changes sign from negative to positive, then $f$ has a local minimum at $c$.

---

## Solution

1. Domain:
   The function is a polynomial, so its domain is:

$$
   D = \mathbb{R}
$$

2. First derivative:
   Differentiate $f(x)$ term by term:

$$
   f'(x) = \frac{d}{dx}(x^3 - 3x^2 + 2) = 3x^2 - 6x = 3x(x - 2)
$$

3. Critical points:
   Set $f'(x) = 0$:

$$
   3x(x - 2) = 0 \implies x_1 = 0, \quad x_2 = 2
$$

4. Sign of the first derivative and intervals of monotonicity:
   The critical points divide the real line into three intervals: $(-\infty, 0)$, $(0, 2)$, and $(2, \infty)$.
   - For $x \in (-\infty, 0)$: $x < 0$ and $x - 2 < 0 \implies f'(x) = 3(-)(-) > 0$. The function is strictly increasing.
   - For $x \in (0, 2)$: $x > 0$ and $x - 2 < 0 \implies f'(x) = 3(+)(-) < 0$. The function is strictly decreasing.
   - For $x \in (2, \infty)$: $x > 0$ and $x - 2 > 0 \implies f'(x) = 3(+)(+) > 0$. The function is strictly increasing.

   Monotonicity table:

   | Interval / Point | $(-\infty, 0)$ | $x = 0$ | $(0, 2)$ | $x = 2$ | $(2, \infty)$ |
   |:---|:---:|:---:|:---:|:---:|:---:|
   | $f'(x)$ | $+$ | $0$ | $-$ | $0$ | $+$ |
   | $f(x)$ | $\nearrow$ | Local max ($2$) | $\searrow$ | Local min ($-2$) | $\nearrow$ |

5. Local extrema:
   - At $x = 0$: $f'(x)$ changes sign from $+$ to $-$. Thus, $f$ has a local maximum:

$$
     f(0) = 0^3 - 3(0)^2 + 2 = 2
$$

     Local maximum point: $(0, 2)$.
   - At $x = 2$: $f'(x)$ changes sign from $-$ to $+$. Thus, $f$ has a local minimum:

$$
     f(2) = 2^3 - 3(2)^2 + 2 = 8 - 12 + 2 = -2
$$

     Local minimum point: $(2, -2)$.

6. Inflection point and limits at infinity:
   The second derivative is:

$$
   f''(x) = 6x - 6 = 6(x - 1)
$$

   Setting $f''(x) = 0$ gives $x = 1$, with $f(1) = 1 - 3 + 2 = 0$.
   The curve is concave down on $(-\infty, 1)$ and concave up on $(1, \infty)$.
   The limits at infinity are:

$$
   \lim_{x \to -\infty} f(x) = -\infty, \qquad \lim_{x \to \infty} f(x) = +\infty
$$

7. Graph sketch:
   ```text
              y
              ^
              |       (0, 2) [Local Max]
              |      *---*
              |     /     \
              |    /       \
              |   /         \
   -----------+--/-----------*------------*--------> x
             /|             (1, 0)       / \
            / |                         /   \
           /  |                        /     * (2, -2) [Local Min]
              |                       *-------*
              |
   ```
   Qualitative features:
   - Rises from $-\infty$ through root $x = 1 - \sqrt{3} \approx -0.73$.
   - Reaches local maximum at $(0, 2)$ with horizontal tangent.
   - Decreases through the inflection point $(1, 0)$ where curvature switches from concave down to concave up.
   - Reaches local minimum at $(2, -2)$ with horizontal tangent.
   - Increases through root $x = 1 + \sqrt{3} \approx 2.73$ towards $+\infty$.

---

## Result

$$
\text{Strictly increasing on } (-\infty, 0] \text{ and on } [2, \infty)
$$

$$
\text{Strictly decreasing on } [0, 2]
$$

$$
\text{Local maximum at } (0, 2), \qquad \text{Local minimum at } (2, -2)
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the second derivative at the critical points: $f''(0) = 6(0) - 6 = -6 < 0$ confirms a strict local maximum at $x = 0$; $f''(2) = 6(2) - 6 = +6 > 0$ confirms a strict local minimum at $x = 2$.

**Pass 2 — Numerical check:** Evaluate test points between and around critical values: $f(-1) = (-1)^3 - 3(-1)^2 + 2 = -2 < f(0) = 2$; $f(1) = 1 - 3 + 2 = 0$, which lies strictly between $f(0) = 2$ and $f(2) = -2$; $f(3) = 27 - 27 + 2 = 2 > f(2) = -2$.

**Pass 3 — Consistency check:** Since $f$ is a cubic polynomial with positive leading coefficient $a = 1 > 0$, the end behavior must satisfy $f(x) \to -\infty$ as $x \to -\infty$ and $f(x) \to +\infty$ as $x \to +\infty$. A cubic with two distinct critical points must have its local maximum to the left of its local minimum, matching $x_{\max} = 0 < x_{\min} = 2$.

---

## Exam tip

State monotonicity on closed intervals $[a, b]$ where the function is continuous, but determine the sign of $f'(x)$ on open intervals $(a, b)$.

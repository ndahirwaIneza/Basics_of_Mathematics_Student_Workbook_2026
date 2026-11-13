# Exercise 10

**Problem:** Perform a complete analysis of

$$
f(x)=\frac{x}{x^2+1}.
$$

Include the domain, symmetry, zeros, limits, monotonicity, extrema, and convexity. Finally, produce a sketch based only on this information.

---

## Relevant theorem / definition

1. Odd function symmetry: $f(-x) = -f(x)$ for all $x \in D$ indicates rotational point symmetry of order 2 about the origin $(0, 0)$.
2. Quotient rule:

$$
   \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}
$$

3. Extremum conditions: Critical points where $f'(x) = 0$ mark local extrema when $f'$ changes sign.
4. Inflection points and concavity: Points where $f''(x)$ changes sign are inflection points. $f''(x) > 0$ implies convex (concave up); $f''(x) < 0$ implies concave (concave down).

---

## Solution

1. Domain:
   The denominator satisfies $x^2 + 1 \ge 1 > 0$ for all real $x$. There are no values where the denominator is zero.

$$
   D = \mathbb{R}
$$

2. Symmetry:
   Evaluate $f(-x)$:

$$
   f(-x) = \frac{-x}{(-x)^2 + 1} = -\frac{x}{x^2 + 1} = -f(x)
$$

   Therefore, $f$ is an odd function. Its graph is point-symmetric with respect to the origin $(0, 0)$.

3. Zeros and sign:
   Set $f(x) = 0$:

$$
   \frac{x}{x^2 + 1} = 0 \iff x = 0
$$

   The origin $(0, 0)$ is the unique $x$-intercept and $y$-intercept.
   Because $x^2 + 1 > 0$ for all $x$:
   - $f(x) < 0$ for $x \in (-\infty, 0)$
   - $f(x) > 0$ for $x \in (0, \infty)$

4. Limits and asymptotes:
   Evaluate limits as $x \to \pm\infty$:

$$
   \lim_{x \to \pm\infty} \frac{x}{x^2 + 1} = \lim_{x \to \pm\infty} \frac{\frac{1}{x}}{1 + \frac{1}{x^2}} = \frac{0}{1} = 0
$$

   Therefore, the line $y = 0$ ($x$-axis) is a horizontal asymptote as $x \to \infty$ and as $x \to -\infty$.
   There are no vertical asymptotes since the domain is all of $\mathbb{R}$.

5. First derivative, monotonicity, and extrema:
   Differentiate using the quotient rule:

$$
   f'(x) = \frac{1 \cdot (x^2 + 1) - x(2x)}{(x^2 + 1)^2} = \frac{1 - x^2}{(x^2 + 1)^2} = \frac{(1 - x)(1 + x)}{(x^2 + 1)^2}
$$

   Set $f'(x) = 0$:

$$
   1 - x^2 = 0 \iff x = -1 \quad \text{or} \quad x = 1
$$

   Since the denominator $(x^2 + 1)^2 > 0$ everywhere, the sign of $f'(x)$ is given by $1 - x^2$:
   - For $x \in (-\infty, -1)$: $1 - x^2 < 0 \implies f'(x) < 0$. The function is strictly decreasing.
   - For $x \in (-1, 1)$: $1 - x^2 > 0 \implies f'(x) > 0$. The function is strictly increasing.
   - For $x \in (1, \infty)$: $1 - x^2 < 0 \implies f'(x) < 0$. The function is strictly decreasing.

   Extrema:
   - At $x = -1$: $f'$ changes from $-$ to $+$, so $f$ attains a local (and global) minimum:

$$
     f(-1) = \frac{-1}{(-1)^2 + 1} = -\frac{1}{2}
$$

     Minimum point: $\left(-1, -\frac{1}{2}\right)$.
   - At $x = 1$: $f'$ changes from $+$ to $-$, so $f$ attains a local (and global) maximum:

$$
     f(1) = \frac{1}{1^2 + 1} = \frac{1}{2}
$$

     Maximum point: $\left(1, \frac{1}{2}\right)$.

6. Second derivative, convexity, and inflection points:
   Differentiate $f'(x) = \frac{1 - x^2}{(x^2 + 1)^2}$:

$$
   \begin{align}
   f''(x) &= \frac{-2x(x^2 + 1)^2 - (1 - x^2) \cdot 2(x^2 + 1)(2x)}{(x^2 + 1)^4} \\
   &= \frac{-2x(x^2 + 1) - 4x(1 - x^2)}{(x^2 + 1)^3} \\
   &= \frac{-2x^3 - 2x - 4x + 4x^3}{(x^2 + 1)^3} \\
   &= \frac{2x^3 - 6x}{(x^2 + 1)^3} = \frac{2x(x^2 - 3)}{(x^2 + 1)^3}
   \end{align}
$$

   Set $f''(x) = 0$:

$$
   2x(x^2 - 3) = 0 \iff x_1 = -\sqrt{3}, \quad x_2 = 0, \quad x_3 = \sqrt{3}
$$

   Sign of $f''(x)$:
   - On $(-\infty, -\sqrt{3})$: $x < 0$ and $x^2 - 3 > 0 \implies f''(x) < 0$ (strictly concave / concave down).
   - On $(-\sqrt{3}, 0)$: $x < 0$ and $x^2 - 3 < 0 \implies f''(x) > 0$ (strictly convex / concave up).
   - On $(0, \sqrt{3})$: $x > 0$ and $x^2 - 3 < 0 \implies f''(x) < 0$ (strictly concave / concave down).
   - On $(\sqrt{3}, \infty)$: $x > 0$ and $x^2 - 3 > 0 \implies f''(x) > 0$ (strictly convex / concave up).

   All three points are inflection points because $f''$ changes sign across each:

$$
   f(-\sqrt{3}) = \frac{-\sqrt{3}}{3 + 1} = -\frac{\sqrt{3}}{4} \approx -0.433
$$

$$
   f(0) = 0
$$

$$
   f(\sqrt{3}) = \frac{\sqrt{3}}{3 + 1} = \frac{\sqrt{3}}{4} \approx 0.433
$$

   Inflection points: $\left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right)$, $(0, 0)$, and $\left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)$.

7. Complete summary table:

   | $x$ | $(-\infty, -\sqrt{3})$ | $-\sqrt{3}$ | $(-\sqrt{3}, -1)$ | $-1$ | $(-1, 0)$ | $0$ | $(0, 1)$ | $1$ | $(1, \sqrt{3})$ | $\sqrt{3}$ | $(\sqrt{3}, \infty)$ |
   |:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
   | $f'(x)$ | $-$ | $-$ | $-$ | $0$ | $+$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ |
   | $f''(x)$ | $-$ | $0$ | $+$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ | $0$ | $+$ |
   | $f(x)$ | $\searrow$, conc. | Infl. | $\searrow$, conv. | Min $\left(-\frac{1}{2}\right)$ | $\nearrow$, conv. | Infl. ($0$) | $\nearrow$, conc. | Max $\left(\frac{1}{2}\right)$ | $\searrow$, conc. | Infl. | $\searrow$, conv. |

8. Graph sketch:
   ```text
                                         y
                                         ^          (1, 1/2) [Global Max]
                                         |            .--*--.
                                         |         .-'       '-.
                                         |       .'             '.  I3 (sqrt(3), sqrt(3)/4)
                                         |     .'                 *---.___  (stays > 0)
                                         |   .'
       ----------------------------------*-----------------------------------> x  (y = 0)
       (stays < 0) ''---._             .'|  (0, 0) [Infl / Only Zero]
                          *          .'  |
                       I1  '-.    .-'    |
                              '--*       |
                             (-1, -1/2)  |
                            [Global Min] |
   ```
   Qualitative features:
   - Starts near $y = 0$ as $x \to -\infty$, decreases through inflection point $I_1 = (-\sqrt{3}, -\sqrt{3}/4)$.
   - Reaches global minimum at $(-1, -1/2)$ with horizontal tangent.
   - Increases through the origin $(0, 0)$, which is both a zero and an inflection point (slope $f'(0) = 1$).
   - Reaches global maximum at $(1, 1/2)$ with horizontal tangent.
   - Decreases through inflection point $I_3 = (\sqrt{3}, \sqrt{3}/4)$, where it switches to concave up and flattens asymptotically towards $y = 0$ as $x \to \infty$.

---

## Result

$$
\text{Domain: } D = \mathbb{R}, \qquad \text{Symmetry: Odd function (origin symmetric)}
$$

$$
\text{Zero / Intercept: } (0, 0), \qquad \text{Asymptote: Horizontal } y = 0
$$

$$
\text{Monotonicity: Strictly decreasing on } (-\infty, -1] \text{ and on } [1, \infty); \quad \text{Strictly increasing on } [-1, 1]
$$

$$
\text{Extrema: Global minimum at } \left(-1, -\frac{1}{2}\right), \quad \text{Global maximum at } \left(1, \frac{1}{2}\right)
$$

$$
\text{Inflection points: } \left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right), \quad (0, 0), \quad \left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)
$$

---

## Verification

**Pass 1 — Algebraic check:** The inequality $(x \mp 1)^2 \ge 0 \implies x^2 \mp 2x + 1 \ge 0 \implies x^2 + 1 \ge \pm 2x$. Dividing by $2(x^2 + 1) > 0$ yields $-\frac{1}{2} \le \frac{x}{x^2 + 1} \le \frac{1}{2}$ for all $x \in \mathbb{R}$, with equalities attained precisely at $x = -1$ and $x = 1$. This algebraically proves the global bounds.

**Pass 2 — Numerical check:** Compute values across the domain:
$f(-2) = -2/5 = -0.4 > -0.5$;
$f(-1) = -0.5$;
$f(-0.5) = -0.4$;
$f(0) = 0$;
$f(0.5) = 0.4$;
$f(1) = 0.5$;
$f(2) = 0.4 < 0.5$;
$f(10) = 10/101 \approx 0.099$.
The numerical trend matches all monotonicity intervals.

**Pass 3 — Consistency check:** At the origin, $f'(0) = \frac{1 - 0}{(0 + 1)^2} = 1$. The tangent line at the inflection point $(0, 0)$ is $y = x$. Since $f''(x) > 0$ on $(-\sqrt{3}, 0)$, the curve lies above its tangent for $x \in (-\sqrt{3}, 0)$ (i.e. $\frac{x}{x^2+1} > x$ for negative $x$), and since $f''(x) < 0$ on $(0, \sqrt{3})$, the curve lies below its tangent for positive $x$ (i.e. $\frac{x}{x^2+1} < x$), exactly consistent with concavity.

---

## Exam tip

Exploiting odd or even symmetry immediately halves the computational workload for monotonicity and concavity.

# Exercise 8

**Problem:** For

$$
f(x)=x^4-4x^2
$$

find the local extrema, intervals of convexity and concavity, and inflection points. Sketch the graph and mark all the identified features on it.

---

## Relevant theorem / definition

1. First derivative test for extrema: A critical point $c$ where $f'$ changes sign from negative to positive is a local minimum; from positive to negative is a local maximum.
2. Convexity and concavity:
   - If $f''(x) > 0$ on an interval $I$, then $f$ is strictly convex (concave up) on $I$.
   - If $f''(x) < 0$ on an interval $I$, then $f$ is strictly concave (concave down) on $I$.
3. Inflection point: A point $(x_0, f(x_0))$ on the graph where $f$ is continuous, has a tangent line, and $f''(x)$ changes sign across $x_0$.

---

## Solution

1. Domain and symmetry:
   The function is a polynomial, so $D = \mathbb{R}$.
   Furthermore:

$$
   f(-x) = (-x)^4 - 4(-x)^2 = x^4 - 4x^2 = f(x)
$$

   The function is even, meaning its graph is symmetric with respect to the $y$-axis.
   The roots of $f(x) = 0$ are:

$$
   x^2(x^2 - 4) = 0 \implies x = 0 \quad (\text{double root}), \quad x = -2, \quad x = 2
$$

2. First derivative and local extrema:
   Differentiate $f(x)$:

$$
   f'(x) = 4x^3 - 8x = 4x(x^2 - 2) = 4x(x - \sqrt{2})(x + \sqrt{2})
$$

   Setting $f'(x) = 0$ yields three critical points:

$$
   x_1 = -\sqrt{2}, \qquad x_2 = 0, \qquad x_3 = \sqrt{2}
$$

   Sign of $f'(x)$:
   - For $x \in (-\infty, -\sqrt{2})$: $f'(x) < 0 \implies f$ is strictly decreasing.
   - For $x \in (-\sqrt{2}, 0)$: $f'(x) > 0 \implies f$ is strictly increasing.
   - For $x \in (0, \sqrt{2})$: $f'(x) < 0 \implies f$ is strictly decreasing.
   - For $x \in (\sqrt{2}, \infty)$: $f'(x) > 0 \implies f$ is strictly increasing.

   Extrema values:
   - At $x = -\sqrt{2}$: $f'(x)$ switches from $-$ to $+$, yielding a local minimum:

$$
     f(-\sqrt{2}) = (-\sqrt{2})^4 - 4(-\sqrt{2})^2 = 4 - 8 = -4
$$

     Local minimum point: $(-\sqrt{2}, -4)$.
   - At $x = 0$: $f'(x)$ switches from $+$ to $-$, yielding a local maximum:

$$
     f(0) = 0^4 - 4(0)^2 = 0
$$

     Local maximum point: $(0, 0)$.
   - At $x = \sqrt{2}$: $f'(x)$ switches from $-$ to $+$, yielding a local minimum:

$$
     f(\sqrt{2}) = (\sqrt{2})^4 - 4(\sqrt{2})^2 = 4 - 8 = -4
$$

     Local minimum point: $(\sqrt{2}, -4)$.

3. Second derivative, convexity, and inflection points:
   Differentiate $f'(x)$:

$$
   f''(x) = \frac{d}{dx}(4x^3 - 8x) = 12x^2 - 8 = 4(3x^2 - 2) = 12\left(x^2 - \frac{2}{3}\right)
$$

   Set $f''(x) = 0$:

$$
   x^2 = \frac{2}{3} \implies x = \pm\sqrt{\frac{2}{3}} = \pm\frac{\sqrt{6}}{3} \approx \pm 0.8165
$$

   Sign of $f''(x)$:
   - On $\left(-\infty, -\sqrt{\frac{2}{3}}\right)$: $x^2 > \frac{2}{3} \implies f''(x) > 0$ (strictly convex / concave up).
   - On $\left(-\sqrt{\frac{2}{3}}, \sqrt{\frac{2}{3}}\right)$: $x^2 < \frac{2}{3} \implies f''(x) < 0$ (strictly concave / concave down).
   - On $\left(\sqrt{\frac{2}{3}}, \infty\right)$: $x^2 > \frac{2}{3} \implies f''(x) > 0$ (strictly convex / concave up).

   Because $f''(x)$ changes sign at $x = -\sqrt{\frac{2}{3}}$ and at $x = \sqrt{\frac{2}{3}}$, both are inflection points.
   Evaluate $f$ at the inflection points:

$$
   f\left(\pm\sqrt{\frac{2}{3}}\right) = \left(\frac{2}{3}\right)^2 - 4\left(\frac{2}{3}\right) = \frac{4}{9} - \frac{8}{3} = -\frac{20}{9} \approx -2.222
$$

   The inflection points are:

$$
   I_1 = \left(-\sqrt{\frac{2}{3}}, -\frac{20}{9}\right), \qquad I_2 = \left(\sqrt{\frac{2}{3}}, -\frac{20}{9}\right)
$$

4. Summary table:

   | $x$ | $(-\infty, -\sqrt{2})$ | $-\sqrt{2}$ | $\left(-\sqrt{2}, -\sqrt{\frac{2}{3}}\right)$ | $-\sqrt{\frac{2}{3}}$ | $\left(-\sqrt{\frac{2}{3}}, 0\right)$ | $0$ | $\left(0, \sqrt{\frac{2}{3}}\right)$ | $\sqrt{\frac{2}{3}}$ | $\left(\sqrt{\frac{2}{3}}, \sqrt{2}\right)$ | $\sqrt{2}$ | $(\sqrt{2}, \infty)$ |
   |:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
   | $f'(x)$ | $-$ | $0$ | $+$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ | $0$ | $+$ |
   | $f''(x)$ | $+$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ | $0$ | $+$ | $+$ | $+$ |
   | Shape | $\searrow$, conv. | Min ($-4$) | $\nearrow$, conv. | Infl. | $\nearrow$, conc. | Max ($0$) | $\searrow$, conc. | Infl. | $\searrow$, conv. | Min ($-4$) | $\nearrow$, conv. |

5. Graph sketch:
   ```text
              y
       \      |      /
        \     |     /
   ------*----+----*------> x
     (-2, 0)  |  (2, 0)
          \ (0, 0) [Local Max]
           \  *  /
            \/ \/
        I1 *     * I2  [Inflection points y = -20/9]
          /       \
         *         *
    (-sqrt(2),-4) (sqrt(2),-4)
    [Local Min]   [Local Min]
   ```
   Qualitative features:
   - Classic symmetric "W-shape".
   - Approaches $+\infty$ as $x \to \pm\infty$.
   - Crosses the $x$-axis at $(-2, 0)$ and $(2, 0)$, touching the origin $(0, 0)$ as a tangent local peak.
   - Sinks to two equal absolute minima of height $-4$ at $x = \pm\sqrt{2} \approx \pm 1.414$.
   - Transitions curvature at the inflection points $x = \pm\sqrt{2/3} \approx \pm 0.816$ with height $-20/9 \approx -2.22$.

---

## Result

$$
\text{Local minima: } (-\sqrt{2}, -4) \text{ and } (\sqrt{2}, -4) \quad (\text{global minima})
$$

$$
\text{Local maximum: } (0, 0)
$$

$$
\text{Strictly convex (concave up) on } \left(-\infty, -\sqrt{\frac{2}{3}}\right] \text{ and on } \left[\sqrt{\frac{2}{3}}, \infty\right)
$$

$$
\text{Strictly concave (concave down) on } \left[-\sqrt{\frac{2}{3}}, \sqrt{\frac{2}{3}}\right]
$$

$$
\text{Inflection points: } \left(-\sqrt{\frac{2}{3}}, -\frac{20}{9}\right) \text{ and } \left(\sqrt{\frac{2}{3}}, -\frac{20}{9}\right)
$$

---

## Verification

**Pass 1 — Algebraic check:** At the local maximum $x = 0$, $f''(0) = -8 < 0$, confirming strict concavity and a local maximum. At the local minima $x = \pm\sqrt{2}$, $f''(\pm\sqrt{2}) = 12(2) - 8 = 16 > 0$, confirming strict convexity and local minima.

**Pass 2 — Numerical check:** Inflection point slope check: $f'\left(\sqrt{2/3}\right) = 4(2/3)^{1/2}(2/3 - 2) = 4\sqrt{6}/3 \cdot (-4/3) = -\frac{16\sqrt{6}}{9} \approx -4.35$. At this point the downward slope is steepest before leveling out to zero at $x = \sqrt{2}$.

**Pass 3 — Consistency check:** Since $f(x) = (x^2 - 2)^2 - 4$, the minimum of $(x^2 - 2)^2$ is $0$ (achieved when $x^2 = 2 \implies x = \pm\sqrt{2}$), which algebraically proves that the global minimum value is exactly $0 - 4 = -4$.

---

## Exam tip

A zero of the second derivative is an inflection point only if $f''(x)$ actually changes sign across that point.

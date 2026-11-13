# Exercise 3

**Problem:** Analyze the domain, zeros, asymptotes, and monotonicity of

$$
f(x)=\frac{x+1}{x-2}.
$$

Finally, sketch a graph consistent with all the information obtained.

---

## Relevant theorem / definition

1. Domain of a rational function: $P(x)/Q(x)$ is defined for all $x \in \mathbb{R}$ such that $Q(x) \neq 0$.
2. Vertical asymptote: The line $x = x_0$ is a vertical asymptote if at least one of the one-sided limits $\lim_{x \to x_0^\pm} f(x)$ is $+\infty$ or $-\infty$.
3. Horizontal asymptote: The line $y = L$ is a horizontal asymptote if $\lim_{x \to \infty} f(x) = L$ or $\lim_{x \to -\infty} f(x) = L$.
4. Quotient rule:

$$
   \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}
$$

---

## Solution

1. Domain:
   The denominator cannot be zero:

$$
   x - 2 \neq 0 \implies x \neq 2
$$

   Thus, the domain is:

$$
   D = (-\infty, 2) \cup (2, \infty)
$$

2. Zeros and intercepts:
   Set $f(x) = 0$:

$$
   \frac{x+1}{x-2} = 0 \implies x + 1 = 0 \implies x = -1
$$

   The $x$-intercept is $(-1, 0)$.
   The $y$-intercept is obtained by setting $x = 0$:

$$
   f(0) = \frac{0 + 1}{0 - 2} = -\frac{1}{2}
$$

   The $y$-intercept is $(0, -1/2)$.

3. Asymptotes:
   - Vertical asymptote:
     Evaluate one-sided limits at the point of exclusion $x = 2$:

$$
     \lim_{x \to 2^-} \frac{x+1}{x-2} = \left[\frac{3}{0^-}\right] = -\infty
$$

$$
     \lim_{x \to 2^+} \frac{x+1}{x-2} = \left[\frac{3}{0^+}\right] = +\infty
$$

     Therefore, the line $x = 2$ is a two-sided vertical asymptote.
   - Horizontal asymptote:
     Evaluate the limits at infinity:

$$
     \lim_{x \to \pm\infty} \frac{x+1}{x-2} = \lim_{x \to \pm\infty} \frac{1 + \frac{1}{x}}{1 - \frac{2}{x}} = \frac{1 + 0}{1 - 0} = 1
$$

     Therefore, the line $y = 1$ is a horizontal asymptote as $x \to \infty$ and $x \to -\infty$.
   - Oblique asymptotes: None, because the degree of the numerator equals the degree of the denominator.

4. Derivative and monotonicity:
   Apply the quotient rule:

$$
   f'(x) = \frac{1 \cdot (x - 2) - (x + 1) \cdot 1}{(x - 2)^2} = \frac{x - 2 - x - 1}{(x - 2)^2} = \frac{-3}{(x - 2)^2}
$$

   For all $x \in D$, $(x - 2)^2 > 0$ and the numerator is $-3 < 0$.
   Hence:

$$
   f'(x) < 0 \quad \text{for all } x \in (-\infty, 2) \cup (2, \infty)
$$

   The function has no critical points and no local extrema.
   It is strictly decreasing on $(-\infty, 2)$ and strictly decreasing on $(2, \infty)$.

5. Curvature and second derivative:

$$
   f''(x) = \frac{d}{dx}\left[-3(x - 2)^{-2}\right] = 6(x - 2)^{-3} = \frac{6}{(x - 2)^3}
$$

   - For $x \in (-\infty, 2)$: $(x - 2)^3 < 0 \implies f''(x) < 0$ (strictly concave).
   - For $x \in (2, \infty)$: $(x - 2)^3 > 0 \implies f''(x) > 0$ (strictly convex).

6. Graph sketch:
   ```text
                                   y              : x = 2
                                   ^              : | (+inf)
                                   |              : |
                                   |              : \
                                   |              :  '-.____   (stays above y = 1)
       y = 1  - - - - - - - - - - -+ - - - - - - -: - - - - - - - - - - -
        ''--.._  (below y = 1)     |              :
               ''--.._             |              :
       ---------------*------------+--------------:----------------------> x
                 (-1, 0) ''--.._   |              :
                                ''-* (0, -1/2)    :
                                   |'.            :
                                   |  \           :
                                   |   |          :
                                   |   v          :
                                   | (-inf)       :
   ```
   Qualitative features:
   - Left branch ($x < 2$): Starts near $y = 1$ from below as $x \to -\infty$, decreases through $(-1, 0)$ and $(0, -1/2)$, remains concave down, and plunges towards $-\infty$ along the vertical asymptote $x = 2$.
   - Right branch ($x > 2$): Plunges from $+\infty$ along $x = 2$, decreases while maintaining upward convexity, and flattens out towards the horizontal asymptote $y = 1$ from above as $x \to +\infty$.

---

## Result

$$
\text{Domain: } D = (-\infty, 2) \cup (2, \infty)
$$

$$
\text{Zeros: } x = -1 \quad (\text{point } (-1, 0)); \quad y\text{-intercept: } \left(0, -\frac{1}{2}\right)
$$

$$
\text{Asymptotes: } \text{Vertical } x = 2, \quad \text{Horizontal } y = 1
$$

$$
\text{Monotonicity: Strictly decreasing on } (-\infty, 2) \text{ and on } (2, \infty)
$$

---

## Verification

**Pass 1 — Algebraic check:** Rewrite $f(x)$ as a shifted hyperbola: $f(x) = \frac{x - 2 + 3}{x - 2} = 1 + \frac{3}{x - 2}$. The horizontal asymptote is directly $y = 1$, the vertical asymptote is $x = 2$, and the derivative is $\frac{d}{dx}\left[1 + 3(x-2)^{-1}\right] = -3(x-2)^{-2}$, confirming both asymptotes and negative slope algebraically.

**Pass 2 — Numerical check:** Compute values on either side of the vertical asymptote: $f(1.9) = \frac{2.9}{-0.1} = -29$ (consistent with $-\infty$ as $x \to 2^-$); $f(2.1) = \frac{3.1}{0.1} = 31$ (consistent with $+\infty$ as $x \to 2^+$). Also $f(102) = \frac{103}{100} = 1.03 \approx 1$.

**Pass 3 — Consistency check:** Check whether $f(x)$ ever crosses its horizontal asymptote: set $1 + \frac{3}{x - 2} = 1 \implies \frac{3}{x - 2} = 0$, which has no real solution. Thus the curve never intersects $y = 1$, consistent with being entirely below $y = 1$ on $(-\infty, 2)$ and entirely above $y = 1$ on $(2, \infty)$.

---

## Exam tip

Never write that a rational function is decreasing on the union $(-\infty, 2) \cup (2, \infty)$, because a value to the right of the asymptote (e.g. $f(3) = 4$) is greater than a value to the left (e.g. $f(1) = -2$).

# Exercise 5

**Problem:** For

$$
\frac{x^2}{16}-\frac{y^2}{9}=1,
$$

find the intercepts with the $x$-axis, the asymptotes, and make a sketch. Explain why the asymptotes describe the behavior of the curve far from the center.

---

## Relevant theorem / definition

The canonical equation of a hyperbola centered at the origin with transverse axis on the $x$-axis is:

$$
\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1
$$

- Vertices ($x$-intercepts): $(\pm a, 0)$.
- Asymptotes: lines given by replacing the constant $1$ with $0$:

$$
\frac{x^2}{a^2} - \frac{y^2}{b^2} = 0 \implies y = \pm \frac{b}{a}x
$$

---

## Solution

1. Find the intercepts with the $x$-axis:
   Set $y = 0$:

$$
\frac{x^2}{16} - 0 = 1 \implies x^2 = 16 \implies x = \pm 4
$$

   The intercepts (vertices) are $(-4, 0)$ and $(4, 0)$.
   (Setting $x = 0$ gives $-\frac{y^2}{9} = 1 \implies y^2 = -9$, which has no real solutions; hence there are no $y$-intercepts).

2. Determine the asymptotes:
   Set the quadratic form equal to 0:

$$
\frac{x^2}{16} - \frac{y^2}{9} = 0 \implies \frac{y^2}{9} = \frac{x^2}{16} \implies y = \pm \frac{3}{4}x
$$

   The two asymptotes are $y = \frac{3}{4}x$ and $y = -\frac{3}{4}x$.

3. Explain the asymptotic behavior far from the center:
   Solve for $y$ in the upper branch for $x \ge 4$:

$$
y = \frac{3}{4}\sqrt{x^2 - 16}
$$

   Compare this with the asymptote $y_{\text{asymp}} = \frac{3}{4}x$ by rationalizing their difference:

$$
\begin{align}
y_{\text{asymp}} - y &= \frac{3}{4}\left(x - \sqrt{x^2 - 16}\right) \\
&= \frac{3}{4} \cdot \frac{(x - \sqrt{x^2 - 16})(x + \sqrt{x^2 - 16})}{x + \sqrt{x^2 - 16}} \\
&= \frac{3}{4} \cdot \frac{x^2 - (x^2 - 16)}{x + \sqrt{x^2 - 16}} \\
&= \frac{12}{x + \sqrt{x^2 - 16}}
\end{align}
$$

   As $x \to \infty$, the denominator $x + \sqrt{x^2 - 16} \to \infty$, and therefore:

$$
\lim_{x \to \infty} (y_{\text{asymp}} - y) = 0
$$

   Far from the center ($|x| \gg 4$), the constant $1$ in $\frac{x^2}{16} - \frac{y^2}{9} = 1$ is negligible compared to the large quantities $\frac{x^2}{16} \gg 1$. Hence, the curve equation asymptotically coincides with the cone of lines $\frac{x^2}{16} - \frac{y^2}{9} = 0$.

4. Sketch of the hyperbola:

```text
               y
         \     ^     /    asymptote y = (3/4)x
          \    |    /
     branch\   |   / branch
       (    \  |  /    )
  -----+-----+---+-+---+----+-----> x
     (-4,0)   \|/    (4,0)
              /|\
       (    /  |  \    )
     branch/   |   \ branch
          /    |    \
         /     |     \    asymptote y = -(3/4)x
```

---

## Result

$$
x\text{-intercepts: } (-4, 0) \quad \text{and} \quad (4, 0)
$$

$$
\text{Asymptotes: } y = \frac{3}{4}x \quad \text{and} \quad y = -\frac{3}{4}x
$$

$$
\lim_{|x| \to \infty} \left|y_{\text{hyperbola}}(x) - y_{\text{asymptote}}(x)\right| = 0
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the focal distance $c = \sqrt{a^2 + b^2} = \sqrt{16 + 9} = \sqrt{25} = 5$. The foci are $(\pm 5, 0)$. For a hyperbola, the absolute difference of distances to the foci from any point $P$ must equal $2a = 8$. For vertex $P(4,0)$: $|d(P, F_1) - d(P, F_2)| = |(4 - (-5)) - (5 - 4)| = |9 - 1| = 8$.

**Pass 2 — Numerical check:** At $x = 20$, the asymptote gives $y_{\text{asymp}} = \frac{3}{4}(20) = 15$. The hyperbola gives $y = \frac{3}{4}\sqrt{400 - 16} = \frac{3}{4}\sqrt{384} \approx 14.6969$. The vertical difference is $\frac{12}{20 + \sqrt{384}} \approx \frac{12}{39.596} \approx 0.303$, exactly matching $15 - 14.6969$.

**Pass 3 — Consistency check:** The domain of the hyperbola is $|x| \ge 4$, leaving an empty band $(-4, 4)$ where no real points exist. The asymptotes pass through the origin $(0,0)$ and the corners of the fundamental rectangle $[-4,4] \times [-3,3]$, which verifies their slopes $\pm \frac{b}{a} = \pm \frac{3}{4}$.

---

## Exam tip

To find the asymptotes of any canonical hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$, replace the right-hand constant $1$ with $0$ and factor into linear terms $(y - \frac{b}{a}x)(y + \frac{b}{a}x) = 0$.

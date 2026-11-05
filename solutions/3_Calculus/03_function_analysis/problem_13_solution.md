# Exercise 13

**Problem:** Perform a complete analysis of

$$
f(x)=\frac{\ln x}{x},\qquad x>0.
$$

Find the maximum and the behavior at the ends of the domain. Explain which information is necessary for a correct sketch.

---

## Relevant theorem / definition

1. Quotient rule:

$$
   \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}
$$

2. Derivative of natural logarithm: $\frac{d}{dx}(\ln x) = \frac{1}{x}$ for $x > 0$.
3. L'Hôpital's rule: For limits of the form $\left[\frac{\infty}{\infty}\right]$, $\lim_{x \to \infty} \frac{f(x)}{g(x)} = \lim_{x \to \infty} \frac{f'(x)}{g'(x)}$ under the standard differentiability hypotheses.
4. Second derivative and concavity: The point where $f''(x)$ changes sign marks an inflection point where the graph transitions between concave down and concave up.

---

## Solution

1. Domain:
   The problem specifies the domain:

$$
   D = (0, \infty)
$$

2. Zeros and sign:
   Set $f(x) = 0$:

$$
   \frac{\ln x}{x} = 0 \iff \ln x = 0 \iff x = 1
$$

   The point $(1, 0)$ is the unique $x$-intercept.
   Because the denominator $x > 0$ on the entire domain:
   - For $x \in (0, 1)$: $\ln x < 0 \implies f(x) < 0$.
   - For $x \in (1, \infty)$: $\ln x > 0 \implies f(x) > 0$.
   There is no $y$-intercept because $x = 0$ is outside the domain.

3. First derivative and critical points:
   Apply the quotient rule:

$$
   f'(x) = \frac{\frac{1}{x} \cdot x - (\ln x) \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}
$$

   Set $f'(x) = 0$:

$$
   1 - \ln x = 0 \iff \ln x = 1 \iff x = e \approx 2.7183
$$

   Because $x^2 > 0$ for all $x \in D$, the sign of $f'(x)$ is determined solely by $1 - \ln x$:
   - For $x \in (0, e)$: $\ln x < 1 \implies f'(x) > 0$. The function is strictly increasing on $(0, e]$.
   - At $x = e$: $f'(e) = 0$.
   - For $x \in (e, \infty)$: $\ln x > 1 \implies f'(x) < 0$. The function is strictly decreasing on $[e, \infty)$.

4. Maximum:
   Since $f'(x)$ transitions from positive to negative at $x = e$, the function attains a strict local and global maximum at $x = e$:

$$
   f(e) = \frac{\ln e}{e} = \frac{1}{e} \approx 0.3679
$$

   The maximum point is $\left(e, \frac{1}{e}\right)$.

5. Behavior at the ends of the domain:
   - At the left boundary ($x \to 0^+$):

$$
     \lim_{x \to 0^+} \frac{\ln x}{x} = \lim_{x \to 0^+} (\ln x) \cdot \frac{1}{x} = (-\infty) \cdot (+\infty) = -\infty
$$

     Thus, the line $x = 0$ (the positive $y$-axis) is a vertical asymptote approached downwards towards $-\infty$.
   - At the right boundary ($x \to \infty$):
     Evaluate the indeterminate form $\left[\frac{\infty}{\infty}\right]$ via L'Hôpital's rule:

$$
     \lim_{x \to \infty} \frac{\ln x}{x} \stackrel{\text{H}}{=} \lim_{x \to \infty} \frac{\frac{1}{x}}{1} = \lim_{x \to \infty} \frac{1}{x} = 0
$$

     Thus, the line $y = 0$ ($x$-axis) is a horizontal asymptote as $x \to \infty$, approached from above since $f(x) > 0$ for all $x > 1$.

6. Second derivative, convexity, and inflection points:
   Differentiate $f'(x) = \frac{1 - \ln x}{x^2}$:

$$
   \begin{align}
   f''(x) &= \frac{\left(-\frac{1}{x}\right) x^2 - (1 - \ln x)(2x)}{x^4} \\
   &= \frac{-x - 2x + 2x\ln x}{x^4} \\
   &= \frac{-3x + 2x\ln x}{x^4} = \frac{2\ln x - 3}{x^3}
   \end{align}
$$

   Set $f''(x) = 0$:

$$
   2\ln x - 3 = 0 \iff \ln x = \frac{3}{2} \iff x = e^{3/2} = e\sqrt{e} \approx 4.4817
$$

   Sign of $f''(x)$:
   - For $x \in (0, e^{3/2})$: $\ln x < 3/2 \implies f''(x) < 0$ (strictly concave / concave down).
   - For $x \in (e^{3/2}, \infty)$: $\ln x > 3/2 \implies f''(x) > 0$ (strictly convex / concave up).
   The inflection point occurs at $x = e^{3/2}$:

$$
   f(e^{3/2}) = \frac{\frac{3}{2}}{e^{3/2}} = \frac{3}{2e\sqrt{e}} \approx 0.3347
$$

7. Information necessary for a correct sketch:
   A geometrically accurate sketch requires five essential elements:
   - Domain restriction $x > 0$: The entire curve lies strictly in the right half-plane ($x > 0$).
   - Vertical asymptote $x = 0$: The curve plunges to $-\infty$ along the $y$-axis as $x \to 0^+$.
   - Zero crossing $(1, 0)$: The curve crosses the $x$-axis from negative to positive at $(1, 0)$ with slope $f'(1) = 1$.
   - Global maximum $\left(e, \frac{1}{e}\right)$: The peak of the graph where the tangent line is horizontal.
   - Horizontal asymptote $y = 0$ and inflection point $\left(e^{3/2}, \frac{3}{2e^{3/2}}\right)$: After the maximum, the curve decreases. To approach $y = 0$ asymptotically from above without intersecting the $x$-axis or turning back up, the graph must change curvature from concave down to concave up at $x = e^{3/2}$.

---

## Result

$$
\text{Domain: } D = (0, \infty)
$$

$$
\text{Global maximum: } \left(e, \frac{1}{e}\right)
$$

$$
\text{Left boundary: } \lim_{x \to 0^+} f(x) = -\infty \quad (\text{vertical asymptote } x = 0)
$$

$$
\text{Right boundary: } \lim_{x \to \infty} f(x) = 0 \quad (\text{horizontal asymptote } y = 0 \text{ from above})
$$

$$
\text{Zero: } (1, 0), \qquad \text{Inflection point: } \left(e^{3/2}, \frac{3}{2e^{3/2}}\right)
$$

---

## Verification

**Pass 1 — Algebraic check:** Verify the second derivative at the critical point $x = e$:

$$
f''(e) = \frac{2\ln e - 3}{e^3} = \frac{2(1) - 3}{e^3} = -\frac{1}{e^3} < 0
$$

Since $f''(e) < 0$, the second derivative test confirms a strict local maximum at $x = e$.

**Pass 2 — Numerical check:** Compare function values across key landmarks:
- $f(0.1) = \frac{\ln(0.1)}{0.1} \approx \frac{-2.3026}{0.1} = -23.026$ (steep dive near 0).
- $f(1) = 0$.
- $f(2) = \frac{\ln 2}{2} \approx \frac{0.6931}{2} = 0.3466$.
- $f(e) = \frac{1}{e} \approx 0.3679$ (maximum).
- $f(3) = \frac{\ln 3}{3} \approx \frac{1.0986}{3} = 0.3662 < f(e)$.
- $f(e^{3/2}) \approx 0.3347$.
- $f(10) = \frac{\ln 10}{10} \approx \frac{2.3026}{10} = 0.2303$.
The values strictly increase on $(0, e]$ and strictly decrease on $[e, \infty)$.

**Pass 3 — Consistency check:** Since $f(e) > f(\pi)$, we have $\frac{\ln e}{e} > \frac{\ln \pi}{\pi}$, which implies $\pi \ln e > e \ln \pi \iff \ln(e^\pi) > \ln(\pi^e) \iff e^\pi > \pi^e$. This classical inequality is a direct consequence of $x = e$ being the unique global maximum of $f(x)$.

---

## Exam tip

The limit $\lim_{x \to \infty}\frac{\ln x}{x} = 0$ is a standard fundamental limit demonstrating that any power of $x$ grows faster than the logarithm.

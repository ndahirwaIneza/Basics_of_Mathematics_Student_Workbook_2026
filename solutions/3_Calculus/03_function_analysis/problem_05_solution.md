# Exercise 5

**Problem:** Analyze the monotonicity and extrema of

$$
f(x)=xe^{-x}.
$$

Also examine the behavior as $x\to\infty$ and explain how the limit affects the shape of the graph on the right-hand side.

---

## Relevant theorem / definition

1. Product rule:

$$
   (uv)' = u'v + uv'
$$

2. Derivative of exponential:

$$
   \frac{d}{dx}\left(e^{-x}\right) = -e^{-x}
$$

3. First derivative test for extrema: A critical point $c$ where $f'$ changes sign from positive to negative is a local maximum.
4. L'Hôpital's rule: For limits of indeterminate form $\left[\frac{\infty}{\infty}\right]$, if $f$ and $g$ are differentiable and $g'(x) \neq 0$, then $\lim \frac{f(x)}{g(x)} = \lim \frac{f'(x)}{g'(x)}$.

---

## Solution

1. Domain:
   Both $x$ and $e^{-x}$ are defined on all of $\mathbb{R}$, so the domain is:

$$
   D = \mathbb{R}
$$

2. First derivative and critical points:
   Differentiate using the product rule:

$$
   f'(x) = \frac{d}{dx}(x) \cdot e^{-x} + x \cdot \frac{d}{dx}\left(e^{-x}\right) = 1 \cdot e^{-x} + x(-e^{-x}) = (1 - x)e^{-x}
$$

   Because the exponential function satisfies $e^{-x} > 0$ for all $x \in \mathbb{R}$, we set $f'(x) = 0$:

$$
   (1 - x)e^{-x} = 0 \iff 1 - x = 0 \iff x = 1
$$

   There is exactly one critical point at $x = 1$.

3. Monotonicity and extrema:
   The sign of $f'(x)$ is governed entirely by the linear factor $(1 - x)$:
   - For $x \in (-\infty, 1)$: $1 - x > 0 \implies f'(x) > 0$. The function is strictly increasing on $(-\infty, 1]$.
   - At $x = 1$: $f'(1) = 0$.
   - For $x \in (1, \infty)$: $1 - x < 0 \implies f'(x) < 0$. The function is strictly decreasing on $[1, \infty)$.

   Since $f'(x)$ transitions from positive to negative at $x = 1$, the function attains a strict local (and global) maximum at $x = 1$:

$$
   f(1) = 1 \cdot e^{-1} = \frac{1}{e} \approx 0.3679
$$

   The maximum point is $\left(1, \frac{1}{e}\right)$.

4. Behavior as $x \to \infty$ and $x \to -\infty$:
   - As $x \to \infty$:
     Rewrite $xe^{-x}$ in quotient form to evaluate the indeterminate form $\left[\frac{\infty}{\infty}\right]$:

$$
     \lim_{x \to \infty} xe^{-x} = \lim_{x \to \infty} \frac{x}{e^x} \stackrel{\text{H}}{=} \lim_{x \to \infty} \frac{\frac{d}{dx}(x)}{\frac{d}{dx}(e^x)} = \lim_{x \to \infty} \frac{1}{e^x} = 0
$$

     Thus, the line $y = 0$ is a horizontal asymptote as $x \to \infty$.
   - As $x \to -\infty$:

$$
     \lim_{x \to -\infty} xe^{-x} = (-\infty) \cdot e^{+\infty} = -\infty
$$

5. How the limit affects the shape of the graph on the right-hand side:
   For all $x > 0$, both $x > 0$ and $e^{-x} > 0$, so $f(x) > 0$.
   After reaching its peak value of $\frac{1}{e}$ at $x = 1$, the graph decreases monotonically towards $0$. Because $f(x) > 0$ for all $x > 0$ and $\lim_{x \to \infty} f(x) = 0$, the curve must approach the $x$-axis from above without ever crossing it.
   Near the peak $x = 1$, the curve is concave down (curving toward the $x$-axis). To level off and approach the horizontal asymptote $y = 0$ tangentially, the curve must switch from concave down to concave up.
   Computing the second derivative verifies this transition:

$$
   f''(x) = \frac{d}{dx}\left[(1 - x)e^{-x}\right] = -1 \cdot e^{-x} + (1 - x)(-e^{-x}) = (x - 2)e^{-x}
$$

   Setting $f''(x) = 0$ gives the inflection point at $x = 2$, with value $f(2) = 2e^{-2} = \frac{2}{e^2} \approx 0.2707$.
   - For $x \in (1, 2)$: The curve decreases while concave down ($f''(x) < 0$).
   - At $x = 2$: Inflection point where curvature changes.
   - For $x \in (2, \infty)$: The curve decreases while concave up ($f''(x) > 0$), flattening out into a gentle asymptotic tail that hugs the positive $x$-axis.

---

## Result

$$
\text{Strictly increasing on } (-\infty, 1], \qquad \text{Strictly decreasing on } [1, \infty)
$$

$$
\text{Global maximum at } \left(1, \frac{1}{e}\right)
$$

$$
\lim_{x \to \infty} xe^{-x} = 0 \quad (\text{horizontal asymptote } y = 0 \text{ approached from above})
$$

---

## Verification

**Pass 1 — Algebraic check:** Second derivative test at the critical point $x = 1$: $f''(1) = (1 - 2)e^{-1} = -e^{-1} < 0$, which algebraically confirms a strict local maximum at $x = 1$.

**Pass 2 — Numerical check:** Evaluate test points: $f(0) = 0 \cdot 1 = 0$; $f(1) = e^{-1} \approx 0.3679$; $f(2) = 2e^{-2} \approx 0.2707 < f(1)$; $f(5) = 5e^{-5} \approx 0.0337$; $f(10) = 10e^{-10} \approx 0.00045$. The values strictly decrease towards 0 for $x > 1$.

**Pass 3 — Consistency check:** The explicit derivative sign change already proved ($f'(x) > 0$ on $(-\infty, 1)$ and $f'(x) < 0$ on $(1, \infty)$) establishes that $x = 1$ is the unique global maximum. Independently, on any closed bounded interval $[0, b]$ with $b > 1$ chosen large enough that $f(b) < f(1)$ (for instance $[0, 10]$, where $f(0) = 0$ and $f(10) = 10e^{-10} < e^{-1}$), continuity of $f$ on $[0, b]$ guarantees by the Extreme Value Theorem an interior global maximum $c \in (0, b)$ where differentiability forces $f'(c) = 0$, consistent with the unique critical point $x = 1$.

---

## Exam tip

Remember that $e^{-x}$ is never zero or negative; when solving $f'(x) = 0$, you can divide by $e^{-x}$ immediately.

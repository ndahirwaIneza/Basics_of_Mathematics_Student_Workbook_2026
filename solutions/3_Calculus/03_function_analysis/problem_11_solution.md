# Exercise 11

**Problem:** For

$$
f_a(x)=x^3-3ax
$$

depending on $a$, determine the number of critical points and their character. Separate the parameter cases and justify why the structure of the graph changes.

---

## Relevant theorem / definition

1. Critical point: A point $c$ in the domain of $f$ where $f'(c) = 0$ or $f'(c)$ does not exist.
2. First derivative test:
   - If $f'$ changes sign from positive to negative at $c$, $c$ is a local maximum.
   - If $f'$ changes sign from negative to positive at $c$, $c$ is a local minimum.
   - If $f'$ does not change sign at $c$, $c$ is not an extremum (e.g. a stationary inflection point).
3. Bifurcation: A qualitative change in the topological structure or number of critical points of a family of functions as a parameter passes through a critical value.

---

## Solution

1. Domain and first derivative:
   For any parameter $a \in \mathbb{R}$, $f_a(x)$ is a polynomial with domain $D = \mathbb{R}$.
   Compute the first derivative:

$$
   f_a'(x) = \frac{d}{dx}(x^3 - 3ax) = 3x^2 - 3a = 3(x^2 - a)
$$

2. Critical points equation:
   Set $f_a'(x) = 0$:

$$
   3(x^2 - a) = 0 \iff x^2 = a
$$

   The existence and number of real solutions depend directly on the sign of $a$.

3. Separation of parameter cases:

   **Case 1: $a < 0$**
   - Equation: $x^2 = a < 0$ has no real solutions because $x^2 \ge 0$ for all real $x$.
   - Number of critical points: $0$.
   - Sign of $f_a'(x)$: Since $x^2 \ge 0$ and $-a > 0$, we have $x^2 - a > 0$ for all $x \in \mathbb{R}$. Thus $f_a'(x) > 0$ everywhere.
   - Monotonicity and extrema: $f_a(x)$ is strictly increasing on $(-\infty, \infty)$.
   - There are $0$ local extrema.

   **Case 2: $a = 0$**
   - Equation: $x^2 = 0 \implies x = 0$.
   - Number of critical points: $1$ (at $x = 0$).
   - Function: $f_0(x) = x^3$, with derivative $f_0'(x) = 3x^2$.
   - Sign of $f_0'(x)$: For all $x \neq 0$, $3x^2 > 0$. The derivative is zero at $x = 0$ but does not change sign (it is positive on both sides).
   - Monotonicity and extrema: $f_0(x)$ is strictly increasing on $(-\infty, \infty)$.
   - The critical point $(0, 0)$ is a horizontal/stationary inflection point, not a local extremum.
   - There are $0$ local extrema.

   **Case 3: $a > 0$**
   - Equation: $x^2 = a$ has two distinct real solutions:

$$
     x_1 = -\sqrt{a}, \qquad x_2 = \sqrt{a}
$$

   - Number of critical points: $2$.
   - Sign of $f_a'(x) = 3(x + \sqrt{a})(x - \sqrt{a})$:
     - On $(-\infty, -\sqrt{a})$: $f_a'(x) > 0 \implies f_a$ is strictly increasing.
     - On $(-\sqrt{a}, \sqrt{a})$: $f_a'(x) < 0 \implies f_a$ is strictly decreasing.
     - On $(\sqrt{a}, \infty)$: $f_a'(x) > 0 \implies f_a$ is strictly increasing.
   - Character of extrema:
     - At $x_1 = -\sqrt{a}$: $f_a'$ changes from $+$ to $-$. Local maximum at $x_1 = -\sqrt{a}$ with value:

$$
       f_a(-\sqrt{a}) = (-\sqrt{a})^3 - 3a(-\sqrt{a}) = -a\sqrt{a} + 3a\sqrt{a} = 2a\sqrt{a} = 2a^{3/2}
$$

     - At $x_2 = \sqrt{a}$: $f_a'$ changes from $-$ to $+$. Local minimum at $x_2 = \sqrt{a}$ with value:

$$
       f_a(\sqrt{a}) = (\sqrt{a})^3 - 3a(\sqrt{a}) = a\sqrt{a} - 3a\sqrt{a} = -2a\sqrt{a} = -2a^{3/2}
$$

   - There are $2$ local extrema (one local maximum and one local minimum).

4. Justification of why the structure of the graph changes:
   The derivative $f_a'(x) = 3x^2 - 3a$ is a vertical parabola with vertex at $(0, -3a)$.
   - For $a < 0$, the parabola is shifted upward ($y$-intercept $-3a > 0$). The graph of $f_a'$ lies entirely above the $x$-axis. Since the slope is always strictly positive, the graph of $f_a(x)$ rises monotonically across all $\mathbb{R}$ without turning.
   - At $a = 0$, the parabola's vertex touches the $x$-axis at $(0, 0)$. This marks the transition (bifurcation point). The tangent becomes horizontal at a single point, but the graph continues climbing immediately after.
   - For $a > 0$, the parabola dips below the $x$-axis by $3a$, intersecting it at two symmetric roots $x = \pm\sqrt{a}$. This creates an open interval $(-\sqrt{a}, \sqrt{a})$ where the derivative is negative. A region of negative slope is inserted between two regions of positive slope, forcing the graph to form a crest (local maximum) and a trough (local minimum).

---

## Result

$$
\begin{cases}
a < 0: & 0 \text{ critical points, } 0 \text{ local extrema (strictly increasing on } \mathbb{R}) \\
a = 0: & 1 \text{ critical point at } x = 0 \text{ (stationary inflection point, no local extrema)} \\
a > 0: & 2 \text{ critical points: local max at } (-\sqrt{a}, 2a^{3/2}), \text{ local min at } (\sqrt{a}, -2a^{3/2})
\end{cases}
$$

---

## Verification

**Pass 1 — Algebraic check:** Second derivative test for $a > 0$:

$$
f_a''(x) = 6x
$$

- At $x = -\sqrt{a}$: $f_a''(-\sqrt{a}) = -6\sqrt{a} < 0 \implies$ strict local maximum.
- At $x = \sqrt{a}$: $f_a''(\sqrt{a}) = 6\sqrt{a} > 0 \implies$ strict local minimum.
- At $a = 0$: $f_0''(0) = 0$ and $f_0'''(0) = 6 \neq 0$, confirming an inflection point at the horizontal tangent.

**Pass 2 — Numerical check:** Concrete parameter values:
- For $a = -1$: $f_{-1}(x) = x^3 + 3x \implies f_{-1}'(x) = 3x^2 + 3 \ge 3 > 0$ everywhere, verifying no critical points.
- For $a = 1$: $f_1(x) = x^3 - 3x \implies f_1'(x) = 3(x^2 - 1) = 0 \implies x = \pm 1$. Maximum value $f_1(-1) = 2 = 2(1)^{3/2}$, minimum value $f_1(1) = -2 = -2(1)^{3/2}$, exactly matching the formula.

**Pass 3 — Consistency check:** Check odd symmetry: $f_a(-x) = (-x)^3 - 3a(-x) = -(x^3 - 3ax) = -f_a(x)$. Since $f_a$ is odd for all $a$, any extremum at $x_0$ must have an opposite counterpart at $-x_0$ with value $-f(x_0)$. The results $(-\sqrt{a}, 2a^{3/2})$ and $(\sqrt{a}, -2a^{3/2})$ obey this symmetry perfectly.

---

## Exam tip

A critical point where $f'(x) = 0$ is an extremum only if $f'(x)$ changes sign; if $f'(x)$ has a double zero, it is an inflection point, not an extremum.

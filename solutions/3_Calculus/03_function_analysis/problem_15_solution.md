# Exercise 15

**Problem:** For the function

$$
f(x)=x^3-3x
$$

the derivative was correctly computed as

$$
f'(x)=3(x-1)(x+1).
$$

However, a student wrote the following conclusion:

> The derivative is positive between its zeros and negative outside them. Therefore, the function is decreasing on $(-\infty,-1)\cup(1,\infty)$, increasing on $(-1,1)$, has a local minimum at $x=-1$, and a local maximum at $x=1$.

1. Without differentiating again, explain why merely identifying the zeros of the derivative does not justify the stated sign chart, and find the error in the student's reasoning.
2. Construct the correct sign chart for $f'(x)$.
3. Give the correct intervals of monotonicity and the character of the extrema.
4. In each of the three intervals, choose one simple test point and show that the sign of the derivative confirms your classification.

---

## Relevant theorem / definition

1. Sign of a quadratic function: For $q(x) = a(x - x_1)(x - x_2)$ with $x_1 < x_2$:
   - If the leading coefficient satisfies $a > 0$, the parabola opens upward: $q(x) < 0$ between the roots ($x \in (x_1, x_2)$) and $q(x) > 0$ outside the roots ($x \in (-\infty, x_1) \cup (x_2, \infty)$).
   - If $a < 0$, the signs are inverted.
2. First derivative test for extrema: A critical point $c$ where $f'$ transitions from positive to negative is a local maximum; where $f'$ transitions from negative to positive is a local minimum.
3. Monotonicity on subsets vs. derivative sign: Monotonicity can be defined on any ordered subset $S \subseteq D$ by comparing all pairs $x_1 < x_2$ in $S$. However, having $f'(x) > 0$ (or $f'(x) < 0$) on separate intervals does not establish monotonicity across their union; each connected interval must be checked or stated separately.

---

## Solution

1. Error diagnosis in the student's reasoning:
   - Zeros only indicate boundaries: Finding the zeros of $f'(x)$ ($x = \pm 1$) merely partitions the real line into three open intervals: $(-\infty, -1)$, $(-1, 1)$, and $(1, \infty)$. It provides no information on whether the values in those intervals are positive or negative without analyzing the leading coefficient or evaluating test points.
   - Reversed quadratic sign rule: The derivative is:

$$
     f'(x) = 3(x - 1)(x + 1) = 3x^2 - 3
$$

     This is a quadratic polynomial with a positive leading coefficient ($a = 3 > 0$). An upward-opening parabola dips below the horizontal axis between its roots and rises above the axis outside them. The student asserted the exact opposite ("positive between its zeros and negative outside them"), confusing an upward-opening parabola with a downward-opening one.
   - Cascading errors: Because the signs were flipped across all three intervals, every conclusion drawn was reversed:
     - Regions of growth were labeled as decreasing, and the region of decrease was labeled as increasing.
     - The sign change at $x = -1$ was thought to be negative-to-positive (claiming a minimum), whereas the true change is positive-to-negative (a maximum).
     - The sign change at $x = 1$ was thought to be positive-to-negative (claiming a maximum), whereas the true change is negative-to-positive (a minimum).
   - Set union error: Stating that $f$ is decreasing (or increasing) on $(-\infty, -1) \cup (1, \infty)$ conflates derivative signs on separate intervals with monotonicity on their union. While monotonicity can be defined on any ordered subset by comparing all pairs of points, derivative signs on separate intervals do not establish monotonicity across their union—for example, $f(-1.1) = 1.969 > f(1.1) = -1.969$, so $f$ is not increasing on $(-\infty, -1) \cup (1, \infty)$ even though $f'(x) > 0$ on both intervals. Keeping the two intervals separate is therefore appropriate.

2. Correct sign chart for $f'(x)$:
   The factor $3$ is always positive. Analyzing the signs of $(x - 1)$ and $(x + 1)$:
   - For $x \in (-\infty, -1)$: $(x - 1) < 0$ and $(x + 1) < 0 \implies f'(x) = 3(-)(-) > 0$.
   - At $x = -1$: $f'(-1) = 0$.
   - For $x \in (-1, 1)$: $(x - 1) < 0$ and $(x + 1) > 0 \implies f'(x) = 3(-)(+) < 0$.
   - At $x = 1$: $f'(1) = 0$.
   - For $x \in (1, \infty)$: $(x - 1) > 0$ and $(x + 1) > 0 \implies f'(x) = 3(+)(+) > 0$.

   Sign table:

   | Interval / Point | $(-\infty, -1)$ | $x = -1$ | $(-1, 1)$ | $x = 1$ | $(1, \infty)$ |
   |:---|:---:|:---:|:---:|:---:|:---:|
   | Factor $(x + 1)$ | $-$ | $0$ | $+$ | $+$ | $+$ |
   | Factor $(x - 1)$ | $-$ | $-$ | $-$ | $0$ | $+$ |
   | $f'(x) = 3(x-1)(x+1)$ | $+$ | $0$ | $-$ | $0$ | $+$ |

3. Correct intervals of monotonicity and character of extrema:
   - Monotonicity:
     - $f$ is strictly increasing on $(-\infty, -1]$ and on $[1, \infty)$.
     - $f$ is strictly decreasing on $[-1, 1]$.
   - Local extrema:
     - At $x = -1$: $f'(x)$ transitions from $+$ to $-$. Therefore, $f$ has a local maximum at $x = -1$:

$$
       f(-1) = (-1)^3 - 3(-1) = -1 + 3 = 2
$$

       Local maximum point: $(-1, 2)$.
     - At $x = 1$: $f'(x)$ transitions from $-$ to $+$. Therefore, $f$ has a local minimum at $x = 1$:

$$
       f(1) = 1^3 - 3(1) = 1 - 3 = -2
$$

       Local minimum point: $(1, -2)$.

4. Numerical confirmation with test points:
   - For the interval $(-\infty, -1)$, choose test point $x = -2$:

$$
     f'(-2) = 3(-2 - 1)(-2 + 1) = 3(-3)(-1) = +9 > 0
$$

     Confirms that $f'(x) > 0$ and $f$ is strictly increasing on $(-\infty, -1]$.
   - For the interval $(-1, 1)$, choose test point $x = 0$:

$$
     f'(0) = 3(0 - 1)(0 + 1) = 3(-1)(1) = -3 < 0
$$

     Confirms that $f'(x) < 0$ and $f$ is strictly decreasing on $[-1, 1]$.
   - For the interval $(1, \infty)$, choose test point $x = 2$:

$$
     f'(2) = 3(2 - 1)(2 + 1) = 3(1)(3) = +9 > 0
$$

     Confirms that $f'(x) > 0$ and $f$ is strictly increasing on $[1, \infty)$.

---

## Result

$$
\text{Sign chart: } f'(x) > 0 \text{ on } (-\infty, -1) \cup (1, \infty), \qquad f'(x) < 0 \text{ on } (-1, 1)
$$

$$
\text{Monotonicity: Strictly increasing on } (-\infty, -1] \text{ and on } [1, \infty); \quad \text{Strictly decreasing on } [-1, 1]
$$

$$
\text{Extrema: Local maximum at } (-1, 2), \qquad \text{Local minimum at } (1, -2)
$$

$$
\text{Test points: } f'(-2) = +9 > 0, \quad f'(0) = -3 < 0, \quad f'(2) = +9 > 0
$$

---

## Verification

**Pass 1 — Algebraic check:** Second derivative test at the critical points:

$$
f''(x) = \frac{d}{dx}(3x^2 - 3) = 6x
$$

- At $x = -1$: $f''(-1) = 6(-1) = -6 < 0 \implies$ strict local maximum.
- At $x = 1$: $f''(1) = 6(1) = +6 > 0 \implies$ strict local minimum.
This confirms the student's extrema classification was completely inverted.

**Pass 2 — Numerical check:** Compare function values directly:
$f(-2) = (-2)^3 - 3(-2) = -8 + 6 = -2 < f(-1) = 2$ (confirms increasing on $(-\infty, -1]$);
$f(0) = 0$, which satisfies $f(1) = -2 < f(0) = 0 < f(-1) = 2$ (confirms decreasing on $[-1, 1]$);
$f(2) = 2^3 - 3(2) = 8 - 6 = 2 > f(1) = -2$ (confirms increasing on $[1, \infty)$).

**Pass 3 — Consistency check:** Since $f(x) = x^3 - 3x$ has leading coefficient $+1 > 0$, $\lim_{x \to \infty} f(x) = +\infty$. Decreasing throughout the entire tail $(1, \infty)$ would force $f(x) \le f(1) = -2$ for all $x > 1$, which is incompatible with a limit of $+\infty$ (refuting the student's claim on $(1, \infty)$). Note that $\lim_{x \to \infty} f(x) = +\infty$ does not force eventual monotonicity for functions in general; for this cubic, strict increase on $[1, \infty)$ is proved by the derivative sign $f'(x) = 3(x - 1)(x + 1) > 0$ for all $x > 1$.

---

## Exam tip

Always test a simple intermediate value like $x = 0$ to confirm whether a quadratic derivative is positive or negative between its roots.

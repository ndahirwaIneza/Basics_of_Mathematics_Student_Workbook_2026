# Exercise 7

**Problem:** On $[0,2\pi]$, find the intervals of monotonicity and the extrema of

$$
f(x)=\sin x+\cos x.
$$

Include the endpoints of the interval and compare the function values at the critical points and at the endpoints.

---

## Relevant theorem / definition

1. Derivatives of basic trigonometric functions:

$$
   \frac{d}{dx}(\sin x) = \cos x, \qquad \frac{d}{dx}(\cos x) = -\sin x
$$

2. Extreme Value Theorem: A continuous function on a closed bounded interval $[a, b]$ attains both an absolute maximum and an absolute minimum. Candidates for absolute extrema are the interior critical points where $f'(x) = 0$ (or does not exist) and the endpoints $x = a$ and $x = b$.
3. Trigonometric identity:

$$
   \sin x + \cos x = \sqrt{2}\sin\left(x + \frac{\pi}{4}\right)
$$

---

## Solution

1. Domain:
   The problem specifies the closed domain:

$$
   D = [0, 2\pi]
$$

2. First derivative:
   Differentiate $f(x) = \sin x + \cos x$:

$$
   f'(x) = \cos x - \sin x
$$

3. Critical points in $(0, 2\pi)$:
   Set $f'(x) = 0$:

$$
   \cos x - \sin x = 0 \iff \sin x = \cos x
$$

   Since $\cos x \neq 0$ at any solution (if $\cos x = 0$, then $\sin x = \pm 1 \neq 0$), divide by $\cos x$:

$$
   \tan x = 1
$$

   In the interval $(0, 2\pi)$, $\tan x = 1$ has two solutions:

$$
   x_1 = \frac{\pi}{4}, \qquad x_2 = \frac{\pi}{4} + \pi = \frac{5\pi}{4}
$$

4. Monotonicity on $[0, 2\pi]$:
   Determine the sign of $f'(x) = \cos x - \sin x$:
   - On $\left[0, \frac{\pi}{4}\right)$: For $x \in \left[0, \frac{\pi}{4}\right)$, $\cos x > \sin x \implies f'(x) > 0$. The function is strictly increasing on $\left[0, \frac{\pi}{4}\right]$.
   - On $\left(\frac{\pi}{4}, \frac{5\pi}{4}\right)$: For $x \in \left(\frac{\pi}{4}, \frac{5\pi}{4}\right)$, $\sin x > \cos x \implies f'(x) < 0$. The function is strictly decreasing on $\left[\frac{\pi}{4}, \frac{5\pi}{4}\right]$.
   - On $\left(\frac{5\pi}{4}, 2\pi\right]$: For $x \in \left(\frac{5\pi}{4}, 2\pi\right]$, $\cos x > \sin x \implies f'(x) > 0$. The function is strictly increasing on $\left[\frac{5\pi}{4}, 2\pi\right]$.

5. Evaluation and comparison at critical points and endpoints:
   Evaluate $f(x)$ at all four candidate points:
   - Left endpoint $x = 0$:

$$
     f(0) = \sin 0 + \cos 0 = 0 + 1 = 1
$$

   - Critical point $x = \frac{\pi}{4}$:

$$
     f\left(\frac{\pi}{4}\right) = \sin\left(\frac{\pi}{4}\right) + \cos\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2} \approx 1.4142
$$

   - Critical point $x = \frac{5\pi}{4}$:

$$
     f\left(\frac{5\pi}{4}\right) = \sin\left(\frac{5\pi}{4}\right) + \cos\left(\frac{5\pi}{4}\right) = -\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = -\sqrt{2} \approx -1.4142
$$

   - Right endpoint $x = 2\pi$:

$$
     f(2\pi) = \sin(2\pi) + \cos(2\pi) = 0 + 1 = 1
$$

6. Classification of extrema:
   Ordering the values:

$$
   -\sqrt{2} < 1 < \sqrt{2}
$$

   - Global maximum: The greatest value is $\sqrt{2}$, attained at the interior critical point $x = \frac{\pi}{4}$.
   - Global minimum: The least value is $-\sqrt{2}$, attained at the interior critical point $x = \frac{5\pi}{4}$.
   - Endpoint behavior:
     - At $x = 0$, $f$ starts at $1$ and increases into the interval, making $x = 0$ a boundary local minimum.
     - At $x = 2\pi$, $f$ increases up to $1$ from the left, making $x = 2\pi$ a boundary local maximum.
     Neither endpoint produces an absolute extremum because $-\sqrt{2} < 1 < \sqrt{2}$.

---

## Result

$$
\text{Strictly increasing on } \left[0, \frac{\pi}{4}\right] \text{ and on } \left[\frac{5\pi}{4}, 2\pi\right]
$$

$$
\text{Strictly decreasing on } \left[\frac{\pi}{4}, \frac{5\pi}{4}\right]
$$

$$
\text{Global maximum: } f\left(\frac{\pi}{4}\right) = \sqrt{2}, \qquad \text{Global minimum: } f\left(\frac{5\pi}{4}\right) = -\sqrt{2}
$$

$$
\text{Endpoint values: } f(0) = 1, \qquad f(2\pi) = 1
$$

---

## Verification

**Pass 1 — Algebraic check:** Express $f(x)$ using the sine addition formula:

$$
f(x) = \sqrt{2}\left(\frac{1}{\sqrt{2}}\sin x + \frac{1}{\sqrt{2}}\cos x\right) = \sqrt{2}\sin\left(x + \frac{\pi}{4}\right)
$$

Since $-1 \le \sin\left(x + \frac{\pi}{4}\right) \le 1$, the amplitude of $f(x)$ is $\sqrt{2}$, confirming that the absolute maximum is $\sqrt{2}$ (when $x + \frac{\pi}{4} = \frac{\pi}{2} \implies x = \frac{\pi}{4}$) and the absolute minimum is $-\sqrt{2}$ (when $x + \frac{\pi}{4} = \frac{3\pi}{2} \implies x = \frac{5\pi}{4}$).

**Pass 2 — Numerical check:** Second derivative test at critical points:

$$
f''(x) = -\sin x - \cos x = -f(x)
$$

- At $x = \frac{\pi}{4}$: $f''\left(\frac{\pi}{4}\right) = -\sqrt{2} < 0$, confirming a local maximum.
- At $x = \frac{5\pi}{4}$: $f''\left(\frac{5\pi}{4}\right) = -(-\sqrt{2}) = \sqrt{2} > 0$, confirming a local minimum.

**Pass 3 — Consistency check:** Test midpoint values: at $x = \frac{\pi}{2}$, $f\left(\frac{\pi}{2}\right) = 1 + 0 = 1$, which satisfies $-\sqrt{2} < 1 < \sqrt{2}$. At $x = \pi$, $f(\pi) = 0 - 1 = -1$, which also satisfies $-\sqrt{2} < -1 < \sqrt{2}$.

---

## Exam tip

On closed bounded intervals, always compute and list the values at the boundaries $x = a$ and $x = b$ alongside all interior critical points.

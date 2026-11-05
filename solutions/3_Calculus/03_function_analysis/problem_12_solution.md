# Exercise 12

**Problem:** Analyze

$$
f(x)=|x^2-4|.
$$

First sketch $x^2-4$, then explain the effect of the absolute value. Indicate the points where the derivative does not exist and justify the reason geometrically.

---

## Relevant theorem / definition

1. Absolute value definition: For any real expression $u$, $|u| = u$ if $u \ge 0$, and $|u| = -u$ if $u < 0$.
2. Differentiability: A function $f$ is differentiable at $x_0$ if and only if both one-sided derivatives exist and are equal:

$$
   f'_-(x_0) = \lim_{h \to 0^-} \frac{f(x_0 + h) - f(x_0)}{h} = \lim_{h \to 0^+} \frac{f(x_0 + h) - f(x_0)}{h} = f'_+(x_0)
$$

3. Geometric meaning of non-differentiability: If the left-hand and right-hand slopes differ at a point where the function is continuous, the graph forms a sharp corner (angular point), preventing the existence of a unique tangent line.

---

## Solution

1. Sketch and analysis of the base function $g(x) = x^2 - 4$:
   - $g(x)$ is a standard parabola opening upward with vertex at $(0, -4)$ and line of symmetry $x = 0$.
   - Zeros of $g(x)$:

$$
     x^2 - 4 = 0 \iff (x - 2)(x + 2) = 0 \iff x = -2 \quad \text{or} \quad x = 2
$$

   - Sign of $g(x)$:
     $g(x) \ge 0$ on $(-\infty, -2] \cup [2, \infty)$, and $g(x) < 0$ on $(-2, 2)$.

   ASCII sketch of $g(x) = x^2 - 4$:
   ```text
              y
       \      |      /
        \     |     /
   ------*----+----*------> x
     (-2, 0)  |  (2, 0)
          \   |   /
           \  |  /
            \ * /  (0, -4) [Vertex]
             ---
   ```

2. Effect of the absolute value:
   Applying the absolute value to $g(x)$ gives:

$$
   f(x) = |x^2 - 4| = \begin{cases} x^2 - 4, & \text{if } |x| \ge 2 \\ -(x^2 - 4) = 4 - x^2, & \text{if } |x| < 2 \end{cases}
$$

   - For $|x| \ge 2$, $x^2 - 4 \ge 0$, so the graph of $f(x)$ is identical to $g(x)$.
   - For $|x| < 2$, $x^2 - 4 < 0$, so the negative trough of the parabola is reflected vertically across the $x$-axis into the upper half-plane.
   - The original downward vertex $(0, -4)$ is flipped to a positive peak at $(0, 4)$.
   - The roots $x = \pm 2$ become points where the graph meets the $x$-axis and rebounds upward.

   ASCII sketch of $f(x) = |x^2 - 4|$:
   ```text
              y
       \    (0, 4)   /
        \    *---*  /
         \  /     \/
   -------*--------*------> x
       (-2, 0)   (2, 0)
       [Corner]  [Corner]
   ```

3. Points where the derivative does not exist:
   The candidate points of non-differentiability are the zeros $x = 2$ and $x = -2$.
   - At $x = 2$:
     Left-hand derivative (using $f(x) = 4 - x^2$ for $x < 2$):

$$
     f'_-(2) = \lim_{h \to 0^-} \frac{f(2 + h) - f(2)}{h} = \lim_{h \to 0^-} \frac{(4 - (2 + h)^2) - 0}{h} = \lim_{h \to 0^-} \frac{-4h - h^2}{h} = -4
$$

     Right-hand derivative (using $f(x) = x^2 - 4$ for $x > 2$):

$$
     f'_+(2) = \lim_{h \to 0^+} \frac{f(2 + h) - f(2)}{h} = \lim_{h \to 0^+} \frac{((2 + h)^2 - 4) - 0}{h} = \lim_{h \to 0^+} \frac{4h + h^2}{h} = +4
$$

     Since $f'_-(2) = -4 \neq +4 = f'_+(2)$, the derivative $f'(2)$ does not exist.

   - At $x = -2$:
     Left-hand derivative (using $f(x) = x^2 - 4$ for $x < -2$):

$$
     f'_-(-2) = \lim_{h \to 0^-} \frac{((-2 + h)^2 - 4) - 0}{h} = \lim_{h \to 0^-} \frac{-4h + h^2}{h} = -4
$$

     Right-hand derivative (using $f(x) = 4 - x^2$ for $x > -2$):

$$
     f'_+(-2) = \lim_{h \to 0^+} \frac{(4 - (-2 + h)^2) - 0}{h} = \lim_{h \to 0^+} \frac{4h - h^2}{h} = +4
$$

     Since $f'_-(-2) = -4 \neq +4 = f'_+(-2)$, the derivative $f'(-2)$ does not exist.

4. Geometric justification:
   The base parabola $y = x^2 - 4$ crosses the $x$-axis transversely with non-zero slopes: at $x = 2$ with slope $+4$, and at $x = -2$ with slope $-4$.
   The absolute value operator acts as a mirror across the $x$-axis. It negates the slopes on the interior segment $(-2, 2)$ while preserving the slopes on the exterior branches.
   At $x = 2$, the curve arrives from the left with downward slope $-4$ and departs to the right with upward slope $+4$.
   At $x = -2$, the curve arrives from the left with downward slope $-4$ and departs to the right with upward slope $+4$.
   The tangent direction undergoes an abrupt jump rather than a smooth transition. Geometrically, each root is a sharp "V-corner" (corner point) where two distinct half-tangents meet at an angle, so no unique tangent line can be defined.

5. Extrema:
   - Global minima: $x = -2$ and $x = 2$ with value $f(\pm 2) = 0$ (singular critical points).
   - Local maximum: $x = 0$ with value $f(0) = 4$ (stationary critical point where $f'(0) = 0$).

---

## Result

$$
\text{Piecewise form: } f(x) = \begin{cases} x^2 - 4 & \text{for } |x| \ge 2 \\ 4 - x^2 & \text{for } |x| < 2 \end{cases}
$$

$$
\text{Points where } f'(x) \text{ does not exist: } x = -2 \quad \text{and} \quad x = 2
$$

$$
\text{One-sided slopes at } x = 2: f'_-(2) = -4, \quad f'_+(2) = +4
$$

$$
\text{One-sided slopes at } x = -2: f'_-(-2) = -4, \quad f'_+(-2) = +4
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiate piecewise on open intervals:

$$
f'(x) = \begin{cases} 2x, & \text{for } |x| > 2 \\ -2x, & \text{for } |x| < 2 \end{cases}
$$

Evaluating the limits of $f'(x)$ as $x \to 2^-$ gives $\lim_{x \to 2^-} (-2x) = -4$, and as $x \to 2^+$ gives $\lim_{x \to 2^+} (2x) = +4$. Since the one-sided limits of the derivative differ, the derivative cannot exist at the boundary.

**Pass 2 — Numerical check:** Compute difference quotients with $h = \pm 0.001$ at $x = 2$:
- $\frac{f(2.001) - f(2)}{0.001} = \frac{(2.001^2 - 4) - 0}{0.001} = \frac{0.004001}{0.001} = 4.001 \approx +4$.
- $\frac{f(1.999) - f(2)}{-0.001} = \frac{(4 - 1.999^2) - 0}{-0.001} = \frac{0.003999}{-0.001} = -3.999 \approx -4$.
Both numerical values converge to $\pm 4$.

**Pass 3 — Consistency check:** Since $f(x) \ge 0$ for all $x$ and $f(\pm 2) = 0$, $x = \pm 2$ must be global minima. A local minimum of a continuous function on an open interval can occur either where $f'(x) = 0$ or where $f'(x)$ does not exist. Since $f'(x) = \pm 2x \neq 0$ near $\pm 2$, non-differentiability is required for these minima to exist.

---

## Exam tip

Whenever taking the absolute value of a function, non-differentiable corner points occur precisely at the zeros of the function where the original graph intersects the $x$-axis with a non-zero slope.

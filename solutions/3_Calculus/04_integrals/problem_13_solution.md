# Exercise 13

**Problem:** Let

$$
F(x)=\int_0^x(t^2+1)\,dt.
$$

Determine $F(x)$, compute $F'(x)$, and compare the result with the integrand. Explain in your own words why the height of the function describes the local rate of increase of the accumulated area.

---

## Relevant theorem / definition

The Fundamental Theorem of Calculus (Part 1) states that if $f$ is continuous on an interval $[a, b]$, then the accumulation function:

$$
F(x) = \int_a^x f(t)\,dt
$$

is differentiable on $(a, b)$, and its derivative is given by:

$$
F'(x) = \frac{d}{dx}\int_a^x f(t)\,dt = f(x)
$$

---

## Solution

1. Determining $F(x)$:
   Evaluate the definite integral with variable upper bound $x$:

$$
   \begin{align}
   F(x) &= \int_0^x (t^2+1)\,dt \\
   &= \left[ \frac{t^3}{3} + t \right]_0^x \\
   &= \left(\frac{x^3}{3} + x\right) - \left(\frac{0^3}{3} + 0\right) \\
   &= \frac{1}{3}x^3 + x
   \end{align}
$$

2. Computing $F'(x)$:
   Differentiate $F(x)$ with respect to $x$:

$$
   F'(x) = \frac{d}{dx}\left(\frac{1}{3}x^3 + x\right) = \frac{1}{3}(3x^2) + 1 = x^2 + 1
$$

3. Comparing $F'(x)$ with the integrand:
   The original integrand is $f(t) = t^2 + 1$. Evaluated at the upper limit $t = x$, it gives $f(x) = x^2 + 1$.
   Therefore:

$$
   F'(x) = f(x)
$$

   The derivative of the accumulated area function is identically equal to the value of the integrand at the boundary.

4. Explaining why the height describes the rate of increase of area:
   When the upper limit moves from $x$ to $x + \Delta x$, the newly added area under the curve is a thin vertical strip of width $\Delta x$. For small $\Delta x$, the height of this strip is approximately constant and equal to $f(x)$. The area added is therefore:

$$
   \Delta F = F(x + \Delta x) - F(x) \approx f(x) \cdot \Delta x
$$

   Dividing both sides by $\Delta x$:

$$
   \frac{\Delta F}{\Delta x} \approx f(x)
$$

   Taking the limit as $\Delta x \to 0$ gives the instantaneous rate of change of area:

$$
   F'(x) = \lim_{\Delta x \to 0} \frac{F(x + \Delta x) - F(x)}{\Delta x} = f(x)
$$

   Because the area grows by sweeping out thin vertical rectangles, the instantaneous rate of area accumulation per horizontal unit of movement is precisely the height of the curve at that boundary point.

---

## Result

$$
F(x) = \frac{1}{3}x^3 + x
$$

$$
F'(x) = x^2 + 1
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiating $\frac{1}{3}x^3 + x$ gives $x^2 + 1$. Evaluating at $x = 0$ gives $F(0) = \frac{1}{3}(0)^3 + 0 = 0$, which matches the definite integral with identical limits $\int_0^0 (t^2+1)\,dt = 0$.

**Pass 2 — Numerical check:** At $x = 1$, $F(1) = \frac{1}{3}(1) + 1 = \frac{4}{3}$. From the definition: $\int_0^1 (t^2+1)\,dt = \left[\frac{t^3}{3}+t\right]_0^1 = \frac{4}{3}$. Its derivative is $F'(1) = 1^2 + 1 = 2$, matching $f(1) = 1^2 + 1 = 2$.

**Pass 3 — Consistency check:** Since $f(t) = t^2 + 1 \ge 1 > 0$ for all real $t$, the integrand is strictly positive everywhere. Hence the accumulated area $F(x)$ must be strictly increasing on $\mathbb{R}$, which is confirmed by $F'(x) = x^2 + 1 \ge 1 > 0$ for all $x$.

---

## Exam tip

By the Fundamental Theorem of Calculus, $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$; never integrate and then differentiate if only the derivative is asked.

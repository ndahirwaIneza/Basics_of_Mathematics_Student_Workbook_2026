# Exercise 1

**Problem:** The position of a point is described by

$$
s(t)=t^3-6t^2+9t+2,\qquad t\ge0.
$$

1. Determine the velocity and acceleration.
2. Find the times at which the point stops.
3. Determine on which intervals the point moves in the positive direction of the axis and on which intervals it moves in the negative direction.

---

## Relevant theorem / definition

For a position function $s(t)$, velocity is the first time derivative $v(t) = s'(t) = \frac{ds}{dt}$, and acceleration is the second time derivative $a(t) = v'(t) = s''(t) = \frac{d^2s}{dt^2}$. A point is stationary (stops) when $v(t) = 0$. The sign of velocity indicates direction: $v(t) > 0$ corresponds to motion in the positive direction, and $v(t) < 0$ corresponds to motion in the negative direction.

---

## Solution

1. Velocity and acceleration:
   Differentiate $s(t)$ with respect to $t$:

   $$
   v(t) = s'(t) = \frac{d}{dt}\left(t^3 - 6t^2 + 9t + 2\right) = 3t^2 - 12t + 9
   $$

   Differentiate $v(t)$ with respect to $t$:

   $$
   a(t) = v'(t) = \frac{d}{dt}\left(3t^2 - 12t + 9\right) = 6t - 12
   $$

2. Times when the point stops:
   Set $v(t) = 0$:

   $$
   3t^2 - 12t + 9 = 0
   $$

   Factor out the constant 3:

   $$
   3(t^2 - 4t + 3) = 0
   $$

   Factor the quadratic polynomial:

   $$
   3(t - 1)(t - 3) = 0
   $$

   Because $t \ge 0$, both roots are admissible:

   $$
   t = 1, \qquad t = 3
   $$

3. Intervals of motion in positive and negative directions:
   The sign of $v(t) = 3(t - 1)(t - 3)$ on the domain $[0, \infty)$ is partitioned by the roots $t = 1$ and $t = 3$:
   - For $t \in [0, 1)$: both $(t - 1) < 0$ and $(t - 3) < 0$, so $v(t) > 0$. The point moves in the positive direction.
   - For $t \in (1, 3)$: $(t - 1) > 0$ and $(t - 3) < 0$, so $v(t) < 0$. The point moves in the negative direction.
   - For $t \in (3, \infty)$: both $(t - 1) > 0$ and $(t - 3) > 0$, so $v(t) > 0$. The point moves in the positive direction.

---

## Result

$$
v(t) = 3t^2 - 12t + 9, \qquad a(t) = 6t - 12
$$

$$
\text{Stopping times: } t = 1, \quad t = 3
$$

$$
\text{Positive direction: } t \in [0, 1) \cup (3, \infty), \qquad \text{Negative direction: } t \in (1, 3)
$$

---

## Verification

**Pass 1 — Algebraic check:** Integrating velocity over time recovers position up to an integration constant:

$$
\int (3t^2 - 12t + 9)\,dt = t^3 - 6t^2 + 9t + C
$$

Evaluating at $t = 0$ gives $s(0) = 2$, which confirms $C = 2$ and reproduces $s(t)$.

**Pass 2 — Numerical check:** Test sample points in each subinterval: at $t = 0.5$, $v(0.5) = 3(0.25) - 6 + 9 = 3.75 > 0$; at $t = 2$, $v(2) = 12 - 24 + 9 = -3 < 0$; at $t = 4$, $v(4) = 48 - 48 + 9 = 9 > 0$. The signs match the deduced intervals.

**Pass 3 — Consistency check:** At $t = 1$, $s(1) = 1 - 6 + 9 + 2 = 6$. At $t = 3$, $s(3) = 27 - 54 + 27 + 2 = 2$. The point moves forward from $s(0) = 2$ to $s(1) = 6$ ($\Delta s = +4$), reverses from $s(1) = 6$ to $s(3) = 2$ ($\Delta s = -4$), and then moves forward indefinitely ($s(4) = 6$). The turning points occur precisely at $t = 1$ and $t = 3$.

---

## Exam tip

The stopping condition is $v(t) = 0$, not $a(t) = 0$; acceleration can be nonzero when velocity instantaneously vanishes at a turning point.

# Exercise 5

**Problem:** The velocity of a car during the first five seconds is described by the function

$$
v(t)=4t+2\quad [\mathrm{m/s}].
$$

Compute the distance traveled and explain why the integral of velocity gives the change in position.

Then answer what would have to be changed in the reasoning if the velocity also took negative values.

---

## Relevant theorem / definition

By the Fundamental Theorem of Calculus, if $s(t)$ is a position function whose derivative is continuous velocity $v(t) = s'(t)$, the net change in position (displacement) over $[a, b]$ is:

$$
\Delta s = s(b) - s(a) = \int_a^b v(t)\,dt
$$

The total distance traveled over $[a, b]$ is the integral of speed:

$$
d = \int_a^b |v(t)|\,dt
$$

When $v(t) \ge 0$ throughout $[a, b]$, $|v(t)| = v(t)$, and displacement equals total distance.

---

## Solution

1. Computation of distance traveled:
   On the time interval $[0, 5]$, $4t + 2 \ge 2 > 0$, so velocity is strictly positive and the car moves in a single direction without reversing.
   The total distance traveled $s$ equals the definite integral of $v(t)$:

   $$
   \begin{align}
   s &= \int_0^5 (4t + 2)\,dt \\
   &= \left[ 2t^2 + 2t \right]_0^5 \\
   &= \left(2(5)^2 + 2(5)\right) - \left(2(0)^2 + 2(0)\right) \\
   &= 2(25) + 10 \\
   &= 60\text{ m}
   \end{align}
   $$

2. Why the integral of velocity gives change in position:
   Velocity is the instantaneous rate of change of position:

   $$
   v(t) = \frac{ds}{dt}
   $$

   Partitioning the interval $[0, 5]$ into small subintervals of duration $\Delta t_k$, the small displacement during each subinterval is approximately:

   $$
   \Delta s_k \approx v(t_k^*) \Delta t_k
   $$

   Summing all these discrete displacements yields the total approximate change in position:

   $$
   \Delta s \approx \sum_k v(t_k^*) \Delta t_k
   $$

   Taking the limit as $\Delta t_k \to 0$ defines the Riemann integral $\int_0^5 v(t)\,dt$. By the Fundamental Theorem of Calculus:

   $$
   \int_0^5 v(t)\,dt = \int_0^5 s'(t)\,dt = s(5) - s(0) = \Delta s
   $$

   Thus, integration accumulates infinitesimal changes in position over time.

3. Modification when velocity takes negative values:
   If velocity takes negative values, the car reverses direction. The direct integral $\int_a^b v(t)\,dt$ computes net displacement $s(b) - s(a)$, where forward and backward motions cancel each other out.
   To find the actual total distance traveled, one must integrate the absolute value of velocity (speed):

   $$
   d = \int_a^b |v(t)|\,dt
   $$

   Practically, this requires finding all roots of $v(t) = 0$, dividing $[a, b]$ into subintervals of constant sign, and summing the integrals:

   $$
   d = \int_{\text{positive}} v(t)\,dt - \int_{\text{negative}} v(t)\,dt
   $$

---

## Result

$$
s = 60\text{ m}
$$

$$
\Delta s = \int_a^b v(t)\,dt = s(b) - s(a) \quad (\text{accumulation of infinitesimal displacements } v(t)\,dt)
$$

$$
d = \int_a^b |v(t)|\,dt \quad (\text{total distance requires integrating speed } |v(t)|)
$$

---

## Verification

**Pass 1 — Algebraic check:** The velocity function is linear, $v(t) = 4t + 2$, representing motion with constant acceleration $a = 4\text{ m/s}^2$ and initial velocity $v_0 = 2\text{ m/s}$. The kinematic equation gives:

$$
s = v_0 t + \frac{1}{2}at^2 = 2(5) + \frac{1}{2}(4)(5^2) = 10 + 2(25) = 60\text{ m}
$$

This matches the integral result.

**Pass 2 — Numerical check:** Geometrically, the region under $v(t) = 4t + 2$ on $[0, 5]$ is a trapezoid with parallel vertical sides $v(0) = 2$ and $v(5) = 22$, and base $h = 5$. The trapezoid area formula gives:

$$
A_{\text{trap}} = \frac{v(0) + v(5)}{2} \cdot \Delta t = \frac{2 + 22}{2} \cdot 5 = 12 \cdot 5 = 60\text{ m}
$$

**Pass 3 — Consistency check:** The average velocity is $\bar{v} = \frac{v(0) + v(5)}{2} = 12\text{ m/s}$. Distance is $\bar{v} \cdot \Delta t = 12\text{ m/s} \times 5\text{ s} = 60\text{ m}$, with units $[(\text{m/s}) \cdot \text{s}] = [\text{m}]$.

---

## Exam tip

Distinguish between displacement ($\int v\,dt$, which can be negative or zero) and distance traveled ($\int |v|\,dt$, which is always non-negative).

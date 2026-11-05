# Exercise 8

**Problem:** The rate at which requests arrive at a server during the first 5 minutes is described by the function

$$
r(t)=100+20t\quad [\text{requests/min}],\qquad 0\le t\le5.
$$

1. Compute the total number of requests that arrived during this time.
2. Compute the average rate of incoming requests over this interval.
3. Compare the average rate with the values $r(0)$ and $r(5)$.

---

## Relevant theorem / definition

For a time-varying rate function $r(t)$, the total accumulated quantity over $[a, b]$ is given by the definite integral $R = \int_a^b r(t)\,dt$. The average rate of the process over $[a, b]$ is $r_{\text{avg}} = \frac{1}{b - a} \int_a^b r(t)\,dt = \frac{R}{b - a}$. For any affine function $f(t) = mt + q$, the mean value over $[a, b]$ equals the arithmetic mean of the endpoint values: $\frac{f(a) + f(b)}{2}$.

---

## Solution

1. Total number of requests:
   Integrate the arrival rate function $r(t)$ from $t = 0$ to $t = 5$:

   $$
   \begin{align}
   R &= \int_0^5 (100 + 20t)\,dt \\
   &= \left[ 100t + 10t^2 \right]_0^5 \\
   &= \left(100(5) + 10(5)^2\right) - (0) \\
   &= 500 + 250 \\
   &= 750\text{ requests}
   \end{align}
   $$

2. Average rate of incoming requests:
   Divide the total requests accumulated by the total elapsed time:

   $$
   r_{\text{avg}} = \frac{1}{5 - 0} \int_0^5 r(t)\,dt = \frac{750}{5} = 150\text{ requests/min}
   $$

3. Comparison with $r(0)$ and $r(5)$:
   Evaluate the rate function at the endpoints:

   $$
   r(0) = 100 + 20(0) = 100\text{ requests/min}
   $$

   $$
   r(5) = 100 + 20(5) = 200\text{ requests/min}
   $$

   Calculate the arithmetic mean of the two endpoint rates:

   $$
   \frac{r(0) + r(5)}{2} = \frac{100 + 200}{2} = 150\text{ requests/min}
   $$

   The average rate matches the arithmetic mean of the boundary values:

   $$
   r_{\text{avg}} = \frac{r(0) + r(5)}{2} = 150\text{ requests/min}
   $$

   Moreover, because $r(t)$ is linear, $r_{\text{avg}}$ coincides with the rate evaluated at the midpoint $t = 2.5\text{ min}$:

   $$
   r(2.5) = 100 + 20(2.5) = 150\text{ requests/min}
   $$

---

## Result

$$
R = 750\text{ requests}
$$

$$
r_{\text{avg}} = 150\text{ requests/min}
$$

$$
r_{\text{avg}} = \frac{r(0) + r(5)}{2} = 150\text{ requests/min}
$$

---

## Verification

**Pass 1 — Algebraic check:** For a general affine function $r(t) = a + bt$ on $[0, T]$:

$$
\int_0^T (a + bt)\,dt = aT + \frac{bT^2}{2} = T\left(a + \frac{bT}{2}\right)
$$

Dividing by $T$ gives $r_{\text{avg}} = a + \frac{bT}{2}$. Meanwhile, $\frac{r(0) + r(T)}{2} = \frac{a + (a + bT)}{2} = a + \frac{bT}{2}$. The identity holds algebraically for all $a, b, T$.

**Pass 2 — Numerical check:** The area under the rate graph is a trapezoid with height $h = 5\text{ min}$ and parallel sides $b_1 = 100\text{ req/min}$ and $b_2 = 200\text{ req/min}$. Its geometric area is:

$$
\text{Area} = \frac{100 + 200}{2} \times 5 = 150 \times 5 = 750\text{ requests}
$$

**Pass 3 — Consistency check:** The rate is strictly increasing from $100$ to $200$. Therefore, the average rate must lie strictly between the minimum and maximum: $100 < 150 < 200$. Dimensional check: $[\text{requests/min}] \times [\text{min}] = [\text{requests}]$.

---

## Exam tip

For any linear rate function, the integral over an interval is simply the midpoint rate multiplied by the interval length.

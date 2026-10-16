# Exercise 15

**Problem:** Given
$$a=(1,2,1),\qquad b=(2,4,2),\qquad c=(2,0,3).$$
For each pair, compute
$$\frac{u\cdot v}{\|u\|\,\|v\|}.$$
Order the pairs by increasing angle between the vectors. Explain why for $a$ and $b$ the value is $1$ even though the vectors have different lengths.

---

## Relevant theorem / definition

For non-zero vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$, the cosine of the angle $\theta \in [0, \pi]$ between them is defined by
$$
\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}.
$$
Because the cosine function $f(\theta) = \cos\theta$ is strictly decreasing on the interval $[0, \pi]$, larger values of $\cos\theta$ correspond to smaller angles $\theta$. If $\mathbf{v} = k\mathbf{u}$ with $k > 0$, then $\cos\theta = \frac{\mathbf{u} \cdot (k\mathbf{u})}{\|\mathbf{u}\|(k\|\mathbf{u}\|)} = \frac{k\|\mathbf{u}\|^2}{k\|\mathbf{u}\|^2} = 1$, corresponding to $\theta = 0$.

---

## Solution

1. Compute norms of each vector:
   $$
   \|a\| = \sqrt{1^2 + 2^2 + 1^2} = \sqrt{1 + 4 + 1} = \sqrt{6}
   $$
   $$
   \|b\| = \sqrt{2^2 + 4^2 + 2^2} = \sqrt{4 + 16 + 4} = \sqrt{24} = 2\sqrt{6}
   $$
   $$
   \|c\| = \sqrt{2^2 + 0^2 + 3^2} = \sqrt{4 + 0 + 9} = \sqrt{13}
   $$

2. Compute $\cos\theta$ for each pair:
   - Pair $(a, b)$:
     $$
     a \cdot b = (1)(2) + (2)(4) + (1)(2) = 2 + 8 + 2 = 12
     $$
     $$
     \frac{a \cdot b}{\|a\|\|b\|} = \frac{12}{\sqrt{6}\sqrt{24}} = \frac{12}{\sqrt{144}} = \frac{12}{12} = 1
     $$
     Angle: $\theta_{ab} = \arccos(1) = 0^\circ$.

   - Pair $(a, c)$:
     $$
     a \cdot c = (1)(2) + (2)(0) + (1)(3) = 2 + 0 + 3 = 5
     $$
     $$
     \frac{a \cdot c}{\|a\|\|c\|} = \frac{5}{\sqrt{6}\sqrt{13}} = \frac{5}{\sqrt{78}} \approx 0.5661
     $$
     Angle: $\theta_{ac} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ$.

   - Pair $(b, c)$:
     $$
     b \cdot c = (2)(2) + (4)(0) + (2)(3) = 4 + 0 + 6 = 10
     $$
     $$
     \frac{b \cdot c}{\|b\|\|c\|} = \frac{10}{\sqrt{24}\sqrt{13}} = \frac{10}{2\sqrt{6}\sqrt{13}} = \frac{5}{\sqrt{78}} \approx 0.5661
     $$
     Angle: $\theta_{bc} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ$.

3. Order pairs by increasing angle $\theta$:
   Since $0^\circ < 55.52^\circ$, the ascending order by angle is:
   $$
   (a, b) \quad [\theta = 0^\circ] < (a, c) = (b, c) \quad [\theta \approx 55.52^\circ]
   $$

4. Explanation for pair $(a, b)$:
   Notice that $b = 2a$, where the scalar multiple $k = 2 > 0$. The formula for the cosine normalizes both vectors by dividing them by their respective magnitudes, eliminating all influence of length:
   $$
   \frac{a \cdot b}{\|a\|\|b\|} = \left(\frac{a}{\|a\|}\right) \cdot \left(\frac{b}{\|b\|}\right) = \mathbf{e}_a \cdot \mathbf{e}_b
   $$
   Because both $a$ and $b$ point along the identical ray through the origin, their unit vectors are identical: $\mathbf{e}_a = \mathbf{e}_b$. The dot product of any unit vector with itself is 1. Thus, the cosine measures pure directional divergence, completely independent of vector lengths.

---

## Result

$$
\frac{a \cdot b}{\|a\|\|b\|} = 1 \implies \theta_{ab} = 0^\circ
$$

$$
\frac{a \cdot c}{\|a\|\|c\|} = \frac{5}{\sqrt{78}} \implies \theta_{ac} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ
$$

$$
\frac{b \cdot c}{\|b\|\|c\|} = \frac{5}{\sqrt{78}} \implies \theta_{bc} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ
$$

$$
\text{Order by increasing angle: } (a, b) < (a, c) = (b, c)
$$

---

## Verification

**Pass 1 — Algebraic check:** Since $b = 2a$, substituting directly into the angle formula with $c$: $\frac{b \cdot c}{\|b\|\|c\|} = \frac{(2a) \cdot c}{\|2a\|\|c\|} = \frac{2(a \cdot c)}{2\|a\|\|c\|} = \frac{a \cdot c}{\|a\|\|c\|} = \frac{5}{\sqrt{78}}$, confirming algebraic identity for pairs $(a, c)$ and $(b, c)$.

**Pass 2 — Numerical check:** $78 \approx 8.83176$, so $\frac{5}{8.83176} \approx 0.566138$. $\arccos(0.566138) \approx 0.9690 \text{ rad} \approx 55.52^\circ$.

**Pass 3 — Consistency check:** Since $-1 \le \frac{5}{\sqrt{78}} \le 1$, the values lie strictly within the valid domain of the $\arccos$ function.

---

## Exam tip

Because the cosine function decreases as the angle increases from $0^\circ$ to $180^\circ$, the largest cosine value corresponds to the smallest angle.


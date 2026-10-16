# Exercise 5

**Problem:** Given $u=(1,1,0)$ and $v=(1,0,1)$:

1. Use the sign of $u\cdot v$ to predict the type of angle.
2. Compute the angle.
3. Compare the result with the prediction.

---

## Relevant theorem / definition

The angle $\theta \in [0, \pi]$ between two non-zero vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ satisfies
$$
\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}.
$$
Because lengths are strictly positive ($\|\mathbf{u}\|\|\mathbf{v}\| > 0$), the sign of $\cos\theta$ is identical to the sign of $\mathbf{u} \cdot \mathbf{v}$:
- If $\mathbf{u} \cdot \mathbf{v} > 0$, then $\cos\theta > 0$, so $\theta \in [0, \pi/2)$ (acute angle).
- If $\mathbf{u} \cdot \mathbf{v} = 0$, then $\cos\theta = 0$, so $\theta = \pi/2$ (right angle).
- If $\mathbf{u} \cdot \mathbf{v} < 0$, then $\cos\theta < 0$, so $\theta \in (\pi/2, \pi]$ (obtuse angle).

---

## Solution

1. Prediction via the sign of $u \cdot v$:
   $$
   u \cdot v = (1)(1) + (1)(0) + (0)(1) = 1 + 0 + 0 = 1
   $$
   Since $u \cdot v = 1 > 0$, $\cos\theta > 0$, predicting an acute angle ($0^\circ \le \theta < 90^\circ$).

2. Computation of the angle:
   Compute the lengths of $u$ and $v$:
   $$
   \|u\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{1 + 1 + 0} = \sqrt{2}
   $$
   $$
   \|v\| = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{1 + 0 + 1} = \sqrt{2}
   $$
   Compute the cosine of the angle:
   $$
   \cos\theta = \frac{u \cdot v}{\|u\|\|v\|} = \frac{1}{\sqrt{2}\sqrt{2}} = \frac{1}{2}
   $$
   Determine the angle $\theta$:
   $$
   \theta = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3} = 60^\circ
   $$

3. Comparison with prediction:
   The computed angle $\theta = 60^\circ$ lies in the interval $(0^\circ, 90^\circ)$, which is strictly acute, fully validating the qualitative prediction made from the positive dot product.

---

## Result

$$
u \cdot v = 1 > 0 \implies \text{the angle is acute}
$$

$$
\cos\theta = \frac{1}{2} \implies \theta = \frac{\pi}{3} = 60^\circ
$$

---

## Verification

**Pass 1 — Algebraic check:** By the law of cosines, $\|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2\|u\|\|v\|\cos\theta$. Here $u - v = (0, 1, -1)$, so $\|u - v\|^2 = 0^2 + 1^2 + (-1)^2 = 2$. Then $2 = 2 + 2 - 2(2)\cos\theta \implies 2 = 4 - 4\cos\theta \implies 4\cos\theta = 2 \implies \cos\theta = \frac{1}{2}$.

**Pass 2 — Numerical check:** Evaluating $\cos(60^\circ) = 0.5$, which matches $\frac{1}{2}$ exactly.

**Pass 3 — Consistency check:** Cauchy-Schwarz inequality requires $|u \cdot v| \le \|u\|\|v\|$. Here $|1| \le \sqrt{2}\sqrt{2} = 2$, which holds with strict inequality since the vectors are not collinear.

---

## Exam tip

Always compute the dot product first: its sign immediately indicates whether the angle is acute ($>0$), orthogonal ($=0$), or obtuse ($<0$) before calculating any square roots.


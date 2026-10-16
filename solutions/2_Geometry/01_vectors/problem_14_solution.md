# Exercise 14

**Problem:** Given a point $P=(4,1)$ and a line through the origin with direction $v=(1,2)$. Using projection, find the closest point on the line, the distance from $P$ to the line, and verify that the appropriate vector is perpendicular to the direction of the line.

---

## Relevant theorem / definition

For a line $L$ passing through the origin with direction vector $\mathbf{v}$, any point on $L$ is of the form $t\mathbf{v}$ ($t \in \mathbb{R}$). The closest point $Q \in L$ to an arbitrary point $P$ with position vector $\mathbf{p} = \overrightarrow{OP}$ is given by the orthogonal projection of $\mathbf{p}$ onto $\mathbf{v}$:
$$
\mathbf{q} = \operatorname{proj}_{\mathbf{v}} \mathbf{p} = \frac{\mathbf{p} \cdot \mathbf{v}}{\|\mathbf{v}\|^2} \mathbf{v}.
$$
The shortest distance from $P$ to $L$ is the length of the error vector:
$$
d(P, L) = \|\overrightarrow{QP}\| = \|\mathbf{p} - \mathbf{q}\|.
$$
The error vector $\overrightarrow{QP}$ is orthogonal to the direction of the line: $\overrightarrow{QP} \cdot \mathbf{v} = 0$.

---

## Solution

1. Finding the closest point $Q$ on the line:
   The position vector of $P$ is $\mathbf{p} = (4, 1)$.
   Compute the dot product $\mathbf{p} \cdot v$:
   $$
   \mathbf{p} \cdot v = (4)(1) + (1)(2) = 4 + 2 = 6
   $$
   Compute the squared norm $\|v\|^2$:
   $$
   \|v\|^2 = 1^2 + 2^2 = 1 + 4 = 5
   $$
   Compute the projection point $Q$:
   $$
   \mathbf{q} = \frac{\mathbf{p} \cdot v}{\|v\|^2} v = \frac{6}{5}(1, 2) = \left(\frac{6}{5}, \frac{12}{5}\right) = (1.2, 2.4)
   $$

2. Computing the displacement vector $\overrightarrow{QP}$:
   $$
   \overrightarrow{QP} = \mathbf{p} - \mathbf{q} = (4, 1) - \left(\frac{6}{5}, \frac{12}{5}\right) = \left(\frac{20}{5} - \frac{6}{5}, \frac{5}{5} - \frac{12}{5}\right) = \left(\frac{14}{5}, -\frac{7}{5}\right)
   $$

3. Computing the distance from $P$ to the line:
   $$
   d(P, L) = \|\overrightarrow{QP}\| = \sqrt{\left(\frac{14}{5}\right)^2 + \left(-\frac{7}{5}\right)^2} = \sqrt{\frac{196}{25} + \frac{49}{25}} = \sqrt{\frac{245}{25}}
   $$
   Simplify the radical:
   $$
   \sqrt{\frac{245}{25}} = \frac{\sqrt{49 \times 5}}{5} = \frac{7\sqrt{5}}{5}
   $$

4. Verification of perpendicularity:
   Check the dot product $\overrightarrow{QP} \cdot v$:
   $$
   \overrightarrow{QP} \cdot v = \left(\frac{14}{5}\right)(1) + \left(-\frac{7}{5}\right)(2) = \frac{14 - 14}{5} = 0
   $$
   Thus, $\overrightarrow{QP} \perp v$.

---

## Result

$$
Q = \left(\frac{6}{5}, \frac{12}{5}\right) = (1.2, 2.4)
$$

$$
d(P, L) = \frac{7\sqrt{5}}{5}
$$

$$
\overrightarrow{QP} \cdot v = 0 \implies \overrightarrow{QP} \perp v
$$

---

## Verification

**Pass 1 — Algebraic check:** Parameterize the distance squared as a function of $t$: $f(t) = \|(4,1) - t(1,2)\|^2 = (4-t)^2 + (1-2t)^2 = 16 - 8t + t^2 + 1 - 4t + 4t^2 = 5t^2 - 12t + 17$. Differentiating and setting to zero: $f'(t) = 10t - 12 = 0 \implies t = \frac{12}{10} = \frac{6}{5}$, which reproduces $Q = \frac{6}{5}(1, 2)$.

**Pass 2 — Numerical check:** Minimum distance squared: $f\left(\frac{6}{5}\right) = 5\left(\frac{36}{25}\right) - 12\left(\frac{6}{5}\right) + 17 = \frac{36}{5} - \frac{72}{5} + \frac{85}{5} = \frac{49}{5}$. Taking the square root gives $\sqrt{\frac{49}{5}} = \frac{7}{\sqrt{5}} = \frac{7\sqrt{5}}{5}$, exactly matching the projection result.

**Pass 3 — Consistency check:** The Cartesian equation of the line through $(0,0)$ with direction $(1,2)$ is $2x - y = 0$. Using the standard point-line distance formula: $\frac{|2(4) - 1(1)|}{\sqrt{2^2 + (-1)^2}} = \frac{|8 - 1|}{\sqrt{5}} = \frac{7}{\sqrt{5}} = \frac{7\sqrt{5}}{5}$.

---

## Exam tip

The vector perpendicular to the line is $\mathbf{p} - \operatorname{proj}_{\mathbf{v}}\mathbf{p}$; verify orthogonality immediately by checking $(\mathbf{p} - \operatorname{proj}_{\mathbf{v}}\mathbf{p}) \cdot \mathbf{v} = 0$.


# Exercise 13

**Problem:** Find the point on the plane $x+2y+2z=4$ closest to $P=(3,0,0)$. Give the distance and check that the segment joining the two points is perpendicular to the plane.

---

## Relevant theorem / definition

The point of a plane closest to $P$ is the foot of the perpendicular from $P$, that is, the intersection of the plane with the normal line $P + t\mathbf{n}$. The distance is $|t_0|\,\|\mathbf{n}\|$, which agrees with $D = \dfrac{|\mathbf{n} \cdot P - d|}{\|\mathbf{n}\|}$.

---

## Solution

Normal vector: $\mathbf{n} = (1,2,2)$, $\|\mathbf{n}\| = \sqrt{1 + 4 + 4} = 3$.

Normal line through $P$:

$$
(x,y,z) = (3 + t,\ 2t,\ 2t)
$$

Intersection with the plane:

$$
\begin{align}
(3 + t) + 2(2t) + 2(2t) &= 4 \\
3 + 9t &= 4 \\
t_0 &= \frac{1}{9}
\end{align}
$$

Closest point:

$$
Q = \left(3 + \tfrac19,\ \tfrac29,\ \tfrac29\right) = \left(\tfrac{28}{9},\ \tfrac{2}{9},\ \tfrac{2}{9}\right)
$$

Distance:

$$
D = |t_0|\,\|\mathbf{n}\| = \frac19 \cdot 3 = \frac13
$$

Perpendicularity: $\overrightarrow{PQ} = \frac19(1,2,2) = \frac19\mathbf{n}$ is a multiple of the normal vector, so the segment $PQ$ is perpendicular to the plane.

---

## Result

$$
Q = \left(\frac{28}{9},\ \frac{2}{9},\ \frac{2}{9}\right), \qquad D = \frac{1}{3}
$$

---

## Verification

**Pass 1 — Algebraic check:** $Q$ lies on the plane: $\frac{28}{9} + 2 \cdot \frac29 + 2 \cdot \frac29 = \frac{28 + 4 + 4}{9} = 4$.

**Pass 2 — Numerical check:** Distance formula: $D = \frac{|3 + 0 + 0 - 4|}{3} = \frac13$. Also $\|\overrightarrow{PQ}\| = \frac19\sqrt{1 + 4 + 4} = \frac39 = \frac13$.

**Pass 3 — Consistency check:** Two in-plane directions are $(2,-1,0)$ and $(2,0,-1)$ (both satisfy $x + 2y + 2z = 0$). Then $\overrightarrow{PQ} \cdot (2,-1,0) = \frac19(2 - 2 + 0) = 0$ and $\overrightarrow{PQ} \cdot (2,0,-1) = \frac19(2 + 0 - 2) = 0$, so $PQ$ is perpendicular to the whole plane. As a comparison, the plane point $(4,0,0)$ is at distance $1 > \frac13$ from $P$.

---

## Exam tip

The closest point and the distance come from the same $t_0$: the point is $P + t_0\mathbf{n}$, the distance is $|t_0|\,\|\mathbf{n}\|$.


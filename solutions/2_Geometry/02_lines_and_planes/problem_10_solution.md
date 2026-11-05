# Exercise 10

**Problem:** Find the orthogonal projection of $P=(2,1,3)$ onto the plane $x+y+z=3$, and then find the reflection of $P$ across this plane. Check that the midpoint of the segment joining the point and its reflection lies on the plane.

---

## Relevant theorem / definition

The orthogonal projection $P'$ of $P$ onto the plane $\mathbf{n} \cdot \mathbf{x} = d$ is the intersection of the plane with the normal line $P + t\mathbf{n}$. If $P' = P + t_0\mathbf{n}$, the reflection is $P'' = P + 2t_0\mathbf{n}$, so that $P'$ is the midpoint of $PP''$.

---

## Solution

Normal vector: $\mathbf{n} = (1,1,1)$.

Normal line through $P$:

$$
(x,y,z) = (2 + t,\ 1 + t,\ 3 + t)
$$

Intersection with the plane:

$$
\begin{align}
(2 + t) + (1 + t) + (3 + t) &= 3 \\
6 + 3t &= 3 \\
t_0 &= -1
\end{align}
$$

Projection:

$$
P' = P + t_0\mathbf{n} = (2,1,3) - (1,1,1) = (1,0,2)
$$

Reflection:

$$
P'' = P + 2t_0\mathbf{n} = (2,1,3) - 2(1,1,1) = (0,-1,1)
$$

Midpoint check:

$$
M = \frac{P + P''}{2} = \frac{(2,1,3) + (0,-1,1)}{2} = (1,0,2)
$$

$$
1 + 0 + 2 = 3
$$

The midpoint lies on the plane and coincides with the projection $P'$.

---

## Result

$$
P' = (1,0,2), \qquad P'' = (0,-1,1)
$$

---

## Verification

**Pass 1 — Algebraic check:** $\overrightarrow{PP''} = (-2,-2,-2) = -2\mathbf{n}$, so the segment $PP''$ is perpendicular to the plane, and its midpoint lies in the plane; both conditions of a reflection hold.

**Pass 2 — Numerical check:** The distance formula gives $\frac{|2 + 1 + 3 - 3|}{\sqrt{3}} = \frac{3}{\sqrt3} = \sqrt3$, and $\|P - P'\| = \|(1,1,1)\| = \sqrt3$. Also $\|P'' - P'\| = \|(-1,-1,-1)\| = \sqrt3$, so $P$ and $P''$ are equidistant from the plane.

**Pass 3 — Consistency check:** $P$ gives $2 + 1 + 3 = 6 > 3$ and $P''$ gives $0 - 1 + 1 = 0 < 3$, so the two points lie on opposite sides of the plane, as a reflection requires. Reflecting $P''$ once more ($t$ satisfies $0 + 3t = 3$, so $t = 1$, and $P'' + 2\mathbf{n} = (2,1,3)$) returns $P$.

---

## Exam tip

Find $t_0$ once and reuse it: the projection is $P + t_0\mathbf{n}$ and the reflection is $P + 2t_0\mathbf{n}$; do not solve a second problem.


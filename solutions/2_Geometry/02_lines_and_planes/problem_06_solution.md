# Exercise 6

**Problem:** Given

$$
\Pi_1:x+y+z=1,\qquad \Pi_2:x-y=2.
$$

First use the normal vectors to decide whether the planes are parallel. If not, compute the angle between them and explain why the normal vectors alone are enough for this calculation.

---

## Relevant theorem / definition

Two planes are parallel if and only if their normal vectors are proportional. The angle $\varphi \in [0^\circ, 90^\circ]$ between two planes equals the angle between their normal lines:

$$
\cos\varphi = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{\|\mathbf{n}_1\|\,\|\mathbf{n}_2\|}
$$

---

## Solution

Normal vectors (coefficients of $x, y, z$):

$$
\mathbf{n}_1 = (1,1,1), \qquad \mathbf{n}_2 = (1,-1,0)
$$

Parallelism test: if $\mathbf{n}_1 = k\mathbf{n}_2$, the third components would give $1 = 0 \cdot k$, which is impossible. The normals are not proportional, so the planes are not parallel; they intersect in a line.

Angle:

$$
\mathbf{n}_1 \cdot \mathbf{n}_2 = 1 \cdot 1 + 1 \cdot (-1) + 1 \cdot 0 = 0
$$

$$
\cos\varphi = \frac{|0|}{\sqrt{3}\,\sqrt{2}} = 0 \implies \varphi = 90^\circ
$$

The planes are perpendicular.

Why the normals suffice: a plane is determined, up to translation, by its normal direction. Translating a plane does not change angles, and the angle between the planes, measured in a cross-section perpendicular to their line of intersection, equals the angle between lines perpendicular to each plane, that is, the angle between the normals (taken as the acute one, hence the absolute value). The right-hand sides $1$ and $2$ only shift the planes and play no role.

---

## Result

$$
\Pi_1 \not\parallel \Pi_2, \qquad \varphi = 90^\circ \ (\Pi_1 \perp \Pi_2)
$$

---

## Verification

**Pass 1 — Algebraic check:** The direction of the intersection line is $\mathbf{n}_1 \times \mathbf{n}_2 = (1 \cdot 0 - 1 \cdot (-1),\ 1 \cdot 1 - 1 \cdot 0,\ 1 \cdot (-1) - 1 \cdot 1) = (1,1,-2) \neq \mathbf{0}$, confirming that the planes are not parallel.

**Pass 2 — Numerical check:** The vector $\mathbf{n}_2 = (1,-1,0)$ satisfies $\mathbf{n}_1 \cdot \mathbf{n}_2 = 0$, so $\mathbf{n}_2$ lies parallel to $\Pi_1$. A plane containing a direction normal to another plane is perpendicular to it, consistent with $\varphi = 90^\circ$.

**Pass 3 — Consistency check:** Changing the right-hand sides, for example to $x + y + z = 5$ and $x - y = -7$, leaves $\mathbf{n}_1, \mathbf{n}_2$ and hence $\varphi$ unchanged, as the explanation predicts.

---

## Exam tip

Use the absolute value $|\mathbf{n}_1 \cdot \mathbf{n}_2|$ so that the angle between planes is always reported in $[0^\circ, 90^\circ]$.


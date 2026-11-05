# Exercise 7

**Problem:** For

$$
L:(x,y,z)=(1,1,0)+t(1,-1,0),\qquad \Pi:x+y+z=2,
$$

determine whether the line intersects the plane at one point, is parallel to it, or lies in it. Explain the role of the dot product of the direction vector and the normal vector.

---

## Relevant theorem / definition

For a line $\mathbf{p} + t\mathbf{v}$ and a plane $\mathbf{n} \cdot \mathbf{x} = d$:

- $\mathbf{n} \cdot \mathbf{v} \neq 0$: exactly one intersection point;
- $\mathbf{n} \cdot \mathbf{v} = 0$ and $\mathbf{n} \cdot \mathbf{p} \neq d$: parallel, no common points;
- $\mathbf{n} \cdot \mathbf{v} = 0$ and $\mathbf{n} \cdot \mathbf{p} = d$: the line lies in the plane.

---

## Solution

Data:

$$
\mathbf{p} = (1,1,0), \qquad \mathbf{v} = (1,-1,0), \qquad \mathbf{n} = (1,1,1), \qquad d = 2
$$

Step 1 — Direction test:

$$
\mathbf{n} \cdot \mathbf{v} = 1 \cdot 1 + 1 \cdot (-1) + 1 \cdot 0 = 0
$$

The direction is perpendicular to the normal, so the line is parallel to the plane or lies in it.

Step 2 — Point test:

$$
\mathbf{n} \cdot \mathbf{p} = 1 + 1 + 0 = 2 = d
$$

The base point lies in the plane. Combined with Step 1, the whole line lies in $\Pi$.

Direct substitution confirms this for every $t$:

$$
(1 + t) + (1 - t) + 0 = 2 \quad \text{for all } t \in \mathbb{R}
$$

Role of $\mathbf{n} \cdot \mathbf{v}$: substituting the line into the plane gives $\mathbf{n} \cdot \mathbf{p} + t(\mathbf{n} \cdot \mathbf{v}) = d$. The number $\mathbf{n} \cdot \mathbf{v}$ is the rate at which the left-hand side changes as one moves along the line. If it is zero, the line never moves "towards" or "away from" the plane, so it either stays in the plane or stays at a constant positive distance from it.

---

## Result

$$
\mathbf{n} \cdot \mathbf{v} = 0, \quad \mathbf{n} \cdot \mathbf{p} = 2 = d \implies L \subset \Pi
$$

---

## Verification

**Pass 1 — Algebraic check:** The substituted equation reduces to $2 = 2$, an identity in $t$, which is the algebraic signature of a line contained in the plane.

**Pass 2 — Numerical check:** $t = 3$ gives $(4,-2,0)$ with $4 - 2 + 0 = 2$; $t = -5$ gives $(-4,6,0)$ with $-4 + 6 + 0 = 2$. Both points lie in $\Pi$.

**Pass 3 — Consistency check:** The distance from $\mathbf{p}$ to $\Pi$ is $\frac{|1 + 1 + 0 - 2|}{\sqrt{3}} = 0$, and since the line is parallel to the plane, every point of the line has the same distance $0$.

---

## Exam tip

$\mathbf{n} \cdot \mathbf{v} = 0$ alone never decides between "parallel" and "contained"; always test one point of the line as well.


# Exercise 4

**Problem:** Find the equation of the plane through

$$
A=(1,0,0),\quad B=(0,1,0),\quad C=(0,0,1).
$$

First construct two vectors lying in the plane, and then use the cross product. Check the resulting equation on all three points.

---

## Relevant theorem / definition

If $\mathbf{u}$ and $\mathbf{v}$ are non-parallel vectors lying in a plane, then $\mathbf{n} = \mathbf{u} \times \mathbf{v}$ is perpendicular to both and is therefore a normal vector of the plane:

$$
\mathbf{u} \times \mathbf{v} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3
\end{vmatrix}
$$

---

## Solution

Two in-plane vectors:

$$
\mathbf{u} = \overrightarrow{AB} = (-1,1,0), \qquad \mathbf{v} = \overrightarrow{AC} = (-1,0,1)
$$

They are not parallel (the second components $1$ and $0$ rule out a common multiple).

Cross product:

$$
\begin{align}
\mathbf{n} = \mathbf{u} \times \mathbf{v} &=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{vmatrix} \\
&= \mathbf{i}(1 \cdot 1 - 0 \cdot 0) - \mathbf{j}\big((-1) \cdot 1 - 0 \cdot (-1)\big) + \mathbf{k}\big((-1) \cdot 0 - 1 \cdot (-1)\big) \\
&= \mathbf{i}(1) - \mathbf{j}(-1) + \mathbf{k}(1) \\
&= (1,1,1)
\end{align}
$$

Plane through $A = (1,0,0)$ with normal $(1,1,1)$:

$$
\begin{align}
1(x - 1) + 1(y - 0) + 1(z - 0) &= 0 \\
x + y + z &= 1
\end{align}
$$

Check on all three points:

- $A$: $1 + 0 + 0 = 1$
- $B$: $0 + 1 + 0 = 1$
- $C$: $0 + 0 + 1 = 1$

---

## Result

$$
x + y + z = 1
$$

---

## Verification

**Pass 1 — Algebraic check:** $\mathbf{n} \cdot \mathbf{u} = -1 + 1 + 0 = 0$ and $\mathbf{n} \cdot \mathbf{v} = -1 + 0 + 1 = 0$, so $\mathbf{n}$ is perpendicular to both in-plane vectors.

**Pass 2 — Numerical check:** The centroid $G = \frac{A + B + C}{3} = \left(\frac13, \frac13, \frac13\right)$ must lie in the plane: $\frac13 + \frac13 + \frac13 = 1$.

**Pass 3 — Consistency check:** By symmetry, the three points are interchanged by permuting the coordinates, so the plane equation must be symmetric in $x, y, z$; the result $x + y + z = 1$ is. The intercept form $\frac{x}{1} + \frac{y}{1} + \frac{z}{1} = 1$ also matches the intercepts $1, 1, 1$ on the three axes.

---

## Exam tip

Check $\mathbf{n} \cdot \mathbf{u} = \mathbf{n} \cdot \mathbf{v} = 0$ right after computing the cross product; a sign error in the middle ($\mathbf{j}$) term is the most common mistake.


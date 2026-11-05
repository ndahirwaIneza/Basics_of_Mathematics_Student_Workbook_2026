# Exercise 12

**Problem:** Find a parametric equation of the line that is the intersection of

$$
x+y+z=3,\qquad x-y+z=1.
$$

Find its direction vector in two ways: from the system of equations and from the cross product of the normal vectors. Compare the results.

---

## Relevant theorem / definition

Two non-parallel planes meet in a line. Its direction is perpendicular to both normals, so it is parallel to $\mathbf{n}_1 \times \mathbf{n}_2$. Algebraically, the line is the solution set of the $2 \times 3$ system, which has one free variable.

---

## Solution

Method 1 — solving the system.

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 3 \\
1 & -1 & 1 & 1
\end{array}\right]
\xrightarrow{R_2 \leftarrow R_2 - R_1}
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 3 \\
0 & -2 & 0 & -2
\end{array}\right]
$$

From row 2: $-2y = -2$, so $y = 1$.

Column 3 has no pivot, so $z$ is free: set $z = t$. From row 1: $x + 1 + t = 3$, so $x = 2 - t$.

$$
(x,y,z) = (2 - t,\ 1,\ t) = (2,1,0) + t(-1,0,1), \qquad t \in \mathbb{R}
$$

Direction from the system: $\mathbf{d}_1 = (-1,0,1)$.

Method 2 — cross product of the normals.

$$
\mathbf{n}_1 = (1,1,1), \qquad \mathbf{n}_2 = (1,-1,1)
$$

$$
\begin{align}
\mathbf{n}_1 \times \mathbf{n}_2 &=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 1 & 1 \\
1 & -1 & 1
\end{vmatrix} \\
&= \mathbf{i}\big(1 \cdot 1 - 1 \cdot (-1)\big) - \mathbf{j}(1 \cdot 1 - 1 \cdot 1) + \mathbf{k}\big(1 \cdot (-1) - 1 \cdot 1\big) \\
&= (2,0,-2)
\end{align}
$$

Comparison:

$$
(2,0,-2) = -2(-1,0,1)
$$

The two direction vectors are parallel; they differ only by the non-zero factor $-2$, which changes length and orientation but not the line.

---

## Result

$$
(x,y,z) = (2,1,0) + t(-1,0,1), \qquad t \in \mathbb{R}
$$

$$
\mathbf{n}_1 \times \mathbf{n}_2 = (2,0,-2) = -2(-1,0,1)
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute the parametric line into both planes: $(2 - t) + 1 + t = 3$ and $(2 - t) - 1 + t = 1$, identities in $t$.

**Pass 2 — Numerical check:** $t = 2$ gives $(0,1,2)$: $0 + 1 + 2 = 3$ and $0 - 1 + 2 = 1$.

**Pass 3 — Consistency check:** $\mathbf{d}_1 \cdot \mathbf{n}_1 = -1 + 0 + 1 = 0$ and $\mathbf{d}_1 \cdot \mathbf{n}_2 = -1 + 0 + 1 = 0$; the direction lies in both planes, as it must.

---

## Exam tip

Direction vectors are only defined up to a non-zero multiple; $(2,0,-2)$ and $(-1,0,1)$ describe the same line, so do not treat them as different answers.


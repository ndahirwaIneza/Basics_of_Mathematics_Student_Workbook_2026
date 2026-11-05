# Exercise 11

**Problem:** Find the equation of the plane containing

$$
(x,y,z)=(1,0,2)+t(1,1,-1)
$$

and the point $P=(0,2,1)$. Check that both the entire line and the point lie in the plane you obtain.

---

## Relevant theorem / definition

A plane is determined by a point and two linearly independent in-plane directions $\mathbf{u}, \mathbf{v}$; its normal is $\mathbf{n} = \mathbf{u} \times \mathbf{v}$. A line lies in the plane $\mathbf{n} \cdot \mathbf{x} = d$ if and only if its direction satisfies $\mathbf{n} \cdot \mathbf{v} = 0$ and one of its points satisfies the equation.

---

## Solution

Data: $A = (1,0,2)$ is a point of the line, and $\mathbf{u} = (1,1,-1)$ is its direction.

Second in-plane direction (from the line to the point $P$):

$$
\mathbf{v} = \overrightarrow{AP} = (0 - 1,\ 2 - 0,\ 1 - 2) = (-1,2,-1)
$$

Independence: if $\mathbf{v} = k\mathbf{u}$, the first components give $k = -1$, but then the second component would be $-1 \neq 2$. So $\mathbf{u}, \mathbf{v}$ are independent and $P$ is not on the line; the plane is uniquely determined.

Normal vector:

$$
\begin{align}
\mathbf{n} = \mathbf{u} \times \mathbf{v} &=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 1 & -1 \\
-1 & 2 & -1
\end{vmatrix} \\
&= \mathbf{i}\big(1 \cdot (-1) - (-1) \cdot 2\big) - \mathbf{j}\big(1 \cdot (-1) - (-1)(-1)\big) + \mathbf{k}\big(1 \cdot 2 - 1 \cdot (-1)\big) \\
&= \mathbf{i}(1) - \mathbf{j}(-2) + \mathbf{k}(3) \\
&= (1,2,3)
\end{align}
$$

Plane through $A = (1,0,2)$:

$$
\begin{align}
1(x - 1) + 2(y - 0) + 3(z - 2) &= 0 \\
x + 2y + 3z &= 7
\end{align}
$$

Check of the point: $P = (0,2,1)$ gives $0 + 4 + 3 = 7$.

Check of the entire line: substitute $x = 1 + t$, $y = t$, $z = 2 - t$:

$$
(1 + t) + 2t + 3(2 - t) = 1 + t + 2t + 6 - 3t = 7 \quad \text{for all } t \in \mathbb{R}
$$

---

## Result

$$
x + 2y + 3z = 7
$$

---

## Verification

**Pass 1 — Algebraic check:** $\mathbf{n} \cdot \mathbf{u} = 1 + 2 - 3 = 0$ and $\mathbf{n} \cdot \mathbf{v} = -1 + 4 - 3 = 0$, so the normal is perpendicular to both in-plane directions.

**Pass 2 — Numerical check:** The line points at $t = 1$, $(2,1,1)$, and $t = -2$, $(-1,-2,4)$, give $2 + 2 + 3 = 7$ and $-1 - 4 + 12 = 7$.

**Pass 3 — Consistency check:** The substituted line equation reduces to the identity $7 = 7$ (the $t$-terms cancel because $\mathbf{n} \cdot \mathbf{u} = 0$), which is the algebraic signature of a line contained in a plane.

---

## Exam tip

The second direction must come from connecting a point of the line to the extra point; using only the line's direction twice gives a zero cross product.


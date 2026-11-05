# Exercise 3

**Problem:** Find the equation of the plane through $P=(1,-2,3)$ and perpendicular to $n=(2,1,-1)$. Check the result by substituting the point $P$ and explain the role of the normal vector.

---

## Relevant theorem / definition

The plane through $P_0 = (x_0, y_0, z_0)$ with normal vector $\mathbf{n} = (a,b,c)$ is the set of points $X$ such that $\mathbf{n} \cdot (X - P_0) = 0$:

$$
a(x - x_0) + b(y - y_0) + c(z - z_0) = 0
$$

---

## Solution

Substitute $\mathbf{n} = (2,1,-1)$ and $P = (1,-2,3)$:

$$
\begin{align}
2(x - 1) + 1(y + 2) - 1(z - 3) &= 0 \\
2x - 2 + y + 2 - z + 3 &= 0 \\
2x + y - z + 3 &= 0
\end{align}
$$

Check with $P$:

$$
2(1) + (-2) - 3 + 3 = 0
$$

Role of the normal vector: for any point $X$ of the plane, the vector $X - P$ lies in the plane. The condition $\mathbf{n} \cdot (X - P) = 0$ says that every such in-plane vector is perpendicular to $\mathbf{n}$. The normal therefore fixes the orientation (tilt) of the plane, and the point $P$ fixes its position. The coefficients of $x, y, z$ in the general equation are exactly the components of $\mathbf{n}$.

---

## Result

$$
2x + y - z + 3 = 0 \qquad \text{(equivalently } 2x + y - z = -3\text{)}
$$

---

## Verification

**Pass 1 — Algebraic check:** The coefficients of $2x + y - z + 3 = 0$ are $(2,1,-1) = \mathbf{n}$, as required.

**Pass 2 — Numerical check:** Take another point of the plane: $x = 0$, $y = 0$ gives $z = 3$, so $Q = (0,0,3)$. Then $Q - P = (-1,2,0)$ and $\mathbf{n} \cdot (Q - P) = -2 + 2 + 0 = 0$, confirming that an in-plane vector is perpendicular to $\mathbf{n}$.

**Pass 3 — Consistency check:** Moving from $P$ along the normal, the point $P + \mathbf{n} = (3,-1,2)$ gives $2(3) + (-1) - 2 + 3 = 6 \neq 0$; it is off the plane, as it must be, at distance $\frac{6}{\sqrt{6}} = \sqrt{6} = \|\mathbf{n}\|$.

---

## Exam tip

Expand carefully: the most frequent error is a sign slip when the point has negative coordinates, as in $1 \cdot (y - (-2)) = y + 2$.


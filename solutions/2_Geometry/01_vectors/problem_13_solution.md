# Exercise 13

**Problem:** Given
$$A=(0,0,0),\qquad B=(1,2,0),\qquad C=(0,1,1),\qquad D=(2,5,1).$$

1. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
2. Find $n=\overrightarrow{AB}\times\overrightarrow{AC}$.
3. Construct $\overrightarrow{AD}$ and check whether $\overrightarrow{AD}\cdot n=0$.
4. Based on this, decide whether $D$ lies in the plane determined by $A,B,C$, and justify the criterion.

---

## Relevant theorem / definition

In $\mathbb{R}^3$, three non-collinear points $A, B, C$ uniquely determine a plane with normal vector $\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC}$. A point $D$ lies in this plane if and only if the displacement vector $\overrightarrow{AD}$ is orthogonal to $\mathbf{n}$:
$$
\overrightarrow{AD} \cdot \mathbf{n} = 0.
$$
This condition is identical to the vanishing of the scalar triple product:
$$
[\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}] = (\overrightarrow{AB} \times \overrightarrow{AC}) \cdot \overrightarrow{AD} = 0,
$$
which geometrically signifies that the volume of the parallelepiped spanned by the three displacement vectors is zero, meaning all four points are coplanar.

---

## Solution

1. Construction of $\overrightarrow{AB}$ and $\overrightarrow{AC}$:
   $$
   \overrightarrow{AB} = B - A = (1 - 0, 2 - 0, 0 - 0) = (1, 2, 0)
   $$
   $$
   \overrightarrow{AC} = C - A = (0 - 0, 1 - 0, 1 - 0) = (0, 1, 1)
   $$

2. Computation of $n = \overrightarrow{AB} \times \overrightarrow{AC}$:
   $$
   n = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 0 \\ 0 & 1 & 1 \end{vmatrix}
   $$
   Expand along row 1:
   $$
   n = \mathbf{i}(2\cdot 1 - 0\cdot 1) - \mathbf{j}(1\cdot 1 - 0\cdot 0) + \mathbf{k}(1\cdot 1 - 2\cdot 0)
   $$
   $$
   n = 2\mathbf{i} - 1\mathbf{j} + 1\mathbf{k} = (2, -1, 1)
   $$

3. Construction of $\overrightarrow{AD}$ and computation of $\overrightarrow{AD} \cdot n$:
   $$
   \overrightarrow{AD} = D - A = (2 - 0, 5 - 0, 1 - 0) = (2, 5, 1)
   $$
   $$
   \overrightarrow{AD} \cdot n = (2)(2) + (5)(-1) + (1)(1) = 4 - 5 + 1 = 0
   $$

4. Decision and justification of the criterion:
   - **Decision:** Because $\overrightarrow{AD} \cdot n = 0$, point $D$ lies in the plane determined by $A, B, C$.
   - **Justification:** The vector $n$ is perpendicular to every direction within the plane through $A, B, C$. The point $D$ belongs to this plane if and only if the line segment from $A$ to $D$ lies entirely in the plane, which requires its direction vector $\overrightarrow{AD}$ to be perpendicular to $n$. Since $\overrightarrow{AD} \cdot n = 0$, $D$ satisfies this condition.

---

## Result

$$
\overrightarrow{AB} = (1, 2, 0), \qquad \overrightarrow{AC} = (0, 1, 1), \qquad \overrightarrow{AD} = (2, 5, 1)
$$

$$
n = \overrightarrow{AB} \times \overrightarrow{AC} = (2, -1, 1)
$$

$$
\overrightarrow{AD} \cdot n = 0 \implies D \text{ lies in the plane determined by } A, B, C
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the scalar triple product via a single $3 \times 3$ determinant:
$$
\begin{vmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 2 & 5 & 1 \end{vmatrix} = 1(1 - 5) - 2(0 - 2) + 0 = 1(-4) - 2(-2) = -4 + 4 = 0
$$

**Pass 2 — Numerical check:** Express $\overrightarrow{AD}$ as a linear combination of $\overrightarrow{AB}$ and $\overrightarrow{AC}$:
$$
2\overrightarrow{AB} + 1\overrightarrow{AC} = 2(1, 2, 0) + 1(0, 1, 1) = (2, 4, 0) + (0, 1, 1) = (2, 5, 1) = \overrightarrow{AD}
$$
This directly confirms that $\overrightarrow{AD}$ is in the span of $\overrightarrow{AB}$ and $\overrightarrow{AC}$.

**Pass 3 — Consistency check:** Since $A = (0,0,0)$, the plane equation is $2x - y + z = 0$. Plugging in $D = (2, 5, 1)$: $2(2) - 5 + 1 = 4 - 5 + 1 = 0$, confirming $D$ satisfies the Cartesian equation of the plane.

---

## Exam tip

Expressing the coplanarity test as the scalar triple product determinant $\det[\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}] = 0$ is often faster than computing the cross product followed by the dot product.


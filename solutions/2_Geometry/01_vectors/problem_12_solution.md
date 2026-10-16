# Exercise 12

**Problem:** Given $A=(1,0,2)$, $B=(2,1,0)$, and $C=(0,3,1)$. Construct two vectors lying in the plane, find a vector perpendicular to both, and check the perpendicularity using dot products.

---

## Relevant theorem / definition

Given three non-collinear points $A, B, C$ defining a plane in $\mathbb{R}^3$, two directional vectors spanning the plane are given by the displacements $\mathbf{u} = \overrightarrow{AB} = B - A$ and $\mathbf{v} = \overrightarrow{AC} = C - A$. A normal vector $\mathbf{n}$ perpendicular to the plane is orthogonal to every vector lying in that plane and is constructed via the cross product:
$$
\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC}.
$$
Perpendicularity is verified if and only if $\mathbf{n} \cdot \overrightarrow{AB} = 0$ and $\mathbf{n} \cdot \overrightarrow{AC} = 0$.

---

## Solution

1. Construct two vectors lying in the plane:
   $$
   \overrightarrow{AB} = B - A = (2 - 1, 1 - 0, 0 - 2) = (1, 1, -2)
   $$
   $$
   \overrightarrow{AC} = C - A = (0 - 1, 3 - 0, 1 - 2) = (-1, 3, -1)
   $$

2. Find a normal vector $n$ perpendicular to both vectors via the cross product:
   $$
   n = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & -2 \\ -1 & 3 & -1 \end{vmatrix}
   $$
   Expand along row 1:
   $$
   n = \mathbf{i}\begin{vmatrix} 1 & -2 \\ 3 & -1 \end{vmatrix} - \mathbf{j}\begin{vmatrix} 1 & -2 \\ -1 & -1 \end{vmatrix} + \mathbf{k}\begin{vmatrix} 1 & 1 \\ -1 & 3 \end{vmatrix}
   $$
   $$
   n = \mathbf{i}(1(-1) - (-2)(3)) - \mathbf{j}(1(-1) - (-2)(-1)) + \mathbf{k}(1(3) - 1(-1))
   $$
   $$
   n = \mathbf{i}(-1 + 6) - \mathbf{j}(-1 - 2) + \mathbf{k}(3 + 1)
   $$
   $$
   n = 5\mathbf{i} - (-3)\mathbf{j} + 4\mathbf{k} = (5, 3, 4)
   $$

3. Check perpendicularity using dot products:
   - Check against $\overrightarrow{AB}$:
     $$
     n \cdot \overrightarrow{AB} = (5)(1) + (3)(1) + (4)(-2) = 5 + 3 - 8 = 0
     $$
     Thus, $n \perp \overrightarrow{AB}$.
   - Check against $\overrightarrow{AC}$:
     $$
     n \cdot \overrightarrow{AC} = (5)(-1) + (3)(3) + (4)(-1) = -5 + 9 - 4 = 0
     $$
     Thus, $n \perp \overrightarrow{AC}$.

---

## Result

$$
\overrightarrow{AB} = (1, 1, -2), \qquad \overrightarrow{AC} = (-1, 3, -1)
$$

$$
n = \overrightarrow{AB} \times \overrightarrow{AC} = (5, 3, 4)
$$

$$
n \cdot \overrightarrow{AB} = 0, \qquad n \cdot \overrightarrow{AC} = 0
$$

---

## Verification

**Pass 1 — Algebraic check:** Check against the third side vector $\overrightarrow{BC} = C - B = (-2, 2, 1) = \overrightarrow{AC} - \overrightarrow{AB}$:
$$
n \cdot \overrightarrow{BC} = (5)(-2) + (3)(2) + (4)(1) = -10 + 6 + 4 = 0
$$
Since $\overrightarrow{BC}$ also lies in the plane, $n$ is orthogonal to it as well.

**Pass 2 — Numerical check:** Norm calculation: $\|n\| = \sqrt{5^2 + 3^2 + 4^2} = \sqrt{25 + 9 + 16} = \sqrt{50} = 5\sqrt{2}$.

**Pass 3 — Consistency check:** Since $\overrightarrow{AB}$ and $\overrightarrow{AC}$ are not scalar multiples of each other, they span a 2D plane in $\mathbb{R}^3$; therefore their cross product $n = (5, 3, 4) \neq \mathbf{0}$, producing a valid 1D normal line.

---

## Exam tip

Any non-zero scalar multiple of $n$ (such as $(-5, -3, -4)$ or $(10, 6, 8)$) is also a valid normal vector to the plane.


# Exercise 10

**Problem:** The points $A=(0,0,0)$, $B=(2,1,0)$, and $C=(1,3,2)$ form a triangle. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$, compute the area of the parallelogram using the cross product, and then find the area of the triangle. Explain the factor $\frac12$.

---

## Relevant theorem / definition

The area of the parallelogram spanned by two vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^3$ equals the magnitude of their cross product:
$$
S_{\text{parallelogram}} = \|\mathbf{u} \times \mathbf{v}\|.
$$
The area of the triangle formed by vertices $A, B, C$ is half the area of the parallelogram spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$:
$$
S_{\triangle} = \frac{1}{2}\|\overrightarrow{AB} \times \overrightarrow{AC}\|.
$$
The factor $\frac{1}{2}$ arises because a diagonal divides any parallelogram into two congruent triangles of identical area.

---

## Solution

1. Construct vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$:
   $$
   \overrightarrow{AB} = B - A = (2 - 0, 1 - 0, 0 - 0) = (2, 1, 0)
   $$
   $$
   \overrightarrow{AC} = C - A = (1 - 0, 3 - 0, 2 - 0) = (1, 3, 2)
   $$

2. Compute the cross product $\overrightarrow{AB} \times \overrightarrow{AC}$:
   $$
   \overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & 1 & 0 \\ 1 & 3 & 2 \end{vmatrix}
   $$
   Expand along row 1:
   $$
   \overrightarrow{AB} \times \overrightarrow{AC} = \mathbf{i}(1\cdot 2 - 0\cdot 3) - \mathbf{j}(2\cdot 2 - 0\cdot 1) + \mathbf{k}(2\cdot 3 - 1\cdot 1)
   $$
   $$
   \overrightarrow{AB} \times \overrightarrow{AC} = 2\mathbf{i} - 4\mathbf{j} + 5\mathbf{k} = (2, -4, 5)
   $$

3. Area of the parallelogram:
   $$
   S_{\text{parallelogram}} = \|\overrightarrow{AB} \times \overrightarrow{AC}\| = \sqrt{2^2 + (-4)^2 + 5^2} = \sqrt{4 + 16 + 25} = \sqrt{45} = 3\sqrt{5}
   $$

4. Area of the triangle:
   $$
   S_{\triangle} = \frac{1}{2} S_{\text{parallelogram}} = \frac{\sqrt{45}}{2} = \frac{3\sqrt{5}}{2}
   $$

5. Explanation of the factor $\frac{1}{2}$:
   The parallelogram defined by the vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ consists of the union of $\triangle ABC$ and a second congruent triangle $\triangle DCB$ obtained by completing the fourth vertex $D = B + \overrightarrow{AC}$. The diagonal $BC$ bisects the parallelogram into two triangles with identical base and height, meaning the area of $\triangle ABC$ is precisely $\frac{1}{2}$ the area of the entire parallelogram.

---

## Result

$$
\overrightarrow{AB} = (2, 1, 0), \qquad \overrightarrow{AC} = (1, 3, 2)
$$

$$
\overrightarrow{AB} \times \overrightarrow{AC} = (2, -4, 5)
$$

$$
S_{\text{parallelogram}} = 3\sqrt{5} = \sqrt{45}, \qquad S_{\triangle} = \frac{3\sqrt{5}}{2} = \frac{\sqrt{45}}{2}
$$

---

## Verification

**Pass 1 — Algebraic check:** Check perpendicularity: $(2, -4, 5) \cdot (2, 1, 0) = 4 - 4 + 0 = 0$, and $(2, -4, 5) \cdot (1, 3, 2) = 2 - 12 + 10 = 0$. The normal vector is orthogonal to both side vectors.

**Pass 2 — Numerical check:** $3\sqrt{5} \approx 3 \times 2.23607 = 6.7082$, so $S_\triangle \approx 3.3541$. Checking via $\|\overrightarrow{AB}\| = \sqrt{5} \approx 2.236$, $\|\overrightarrow{AC}\| = \sqrt{14} \approx 3.742$, $\cos\theta = \frac{2(1)+1(3)+0(2)}{\sqrt{5}\sqrt{14}} = \frac{5}{\sqrt{70}}$, $\sin\theta = \sqrt{1 - \frac{25}{70}} = \sqrt{\frac{45}{70}}$. Then $S_\triangle = \frac{1}{2}\sqrt{5}\sqrt{14}\sqrt{\frac{45}{70}} = \frac{\sqrt{45}}{2} = \frac{3\sqrt{5}}{2}$.

**Pass 3 — Consistency check:** Since vertices $A, B, C$ are not collinear (cross product is non-zero), the area must be strictly positive: $\frac{3\sqrt{5}}{2} > 0$.

---

## Exam tip

Always simplify radicals in your final answer: $\sqrt{45} = \sqrt{9 \times 5} = 3\sqrt{5}$, and never omit the factor of $\frac{1}{2}$ for triangle area.


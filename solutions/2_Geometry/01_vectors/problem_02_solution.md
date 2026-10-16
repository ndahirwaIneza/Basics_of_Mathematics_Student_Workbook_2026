# Exercise 2

**Problem:** The points are $A=(1,2,3)$ and $B=(4,-2,6)$.

1. Construct $\overrightarrow{AB}$.
2. Compute its length.
3. Compute the distance between the points using the coordinate formula.
4. Explain why both calculations give the same result.

---

## Relevant theorem / definition

Given two points $A = (x_A, y_A, z_A)$ and $B = (x_B, y_B, z_B)$ in $\mathbb{R}^3$, the displacement vector from $A$ to $B$ is
$$
\overrightarrow{AB} = B - A = (x_B - x_A, y_B - y_A, z_B - z_A).
$$
The Euclidean length (norm) of a vector $\mathbf{v} = (v_1, v_2, v_3)$ is $\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}$, and the Euclidean distance formula between points is $d(A, B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$.

---

## Solution

1. Construction of $\overrightarrow{AB}$:
   $$
   \overrightarrow{AB} = (4 - 1, -2 - 2, 6 - 3) = (3, -4, 3)
   $$

2. Length of $\overrightarrow{AB}$:
   $$
   \|\overrightarrow{AB}\| = \sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{9 + 16 + 9} = \sqrt{34}
   $$

3. Distance between $A$ and $B$ via the coordinate formula:
   $$
   d(A, B) = \sqrt{(4 - 1)^2 + (-2 - 2)^2 + (6 - 3)^2} = \sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{9 + 16 + 9} = \sqrt{34}
   $$

4. Reason both calculations coincide:
   The displacement vector $\overrightarrow{AB}$ stores the coordinate differences $\Delta x = x_B - x_A$, $\Delta y = y_B - y_A$, and $\Delta z = z_B - z_A$. By definition, the distance $d(A, B)$ is the Euclidean length of the straight line segment connecting $A$ and $B$, which is precisely the norm of the displacement vector $\overrightarrow{AB}$ derived from the Pythagorean theorem in three dimensions.

---

## Result

$$
\overrightarrow{AB} = (3, -4, 3)
$$

$$
\|\overrightarrow{AB}\| = \sqrt{34}, \qquad d(A, B) = \sqrt{34}
$$

---

## Verification

**Pass 1 — Algebraic check:** Reversing orientation gives $\overrightarrow{BA} = A - B = (-3, 4, -3) = -\overrightarrow{AB}$. The norm satisfies $\|\overrightarrow{BA}\| = \sqrt{(-3)^2 + 4^2 + (-3)^2} = \sqrt{34} = \|\overrightarrow{AB}\|$.

**Pass 2 — Numerical check:** $5^2 = 25 < 34 < 36 = 6^2$, so $5 < \sqrt{34} \approx 5.831 < 6$, which matches the order of magnitude of the coordinate steps $(\Delta x, \Delta y, \Delta z) = (3, -4, 3)$.

**Pass 3 — Consistency check:** Since $A \neq B$, the length must be strictly positive; $\sqrt{34} > 0$ satisfies the positive definiteness axiom of a metric.

---

## Exam tip

Remember that the vector from $A$ to $B$ is always computed as "terminal point minus initial point" ($B - A$), never $A - B$.


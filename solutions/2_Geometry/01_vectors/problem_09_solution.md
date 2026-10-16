# Exercise 9

**Problem:** For $u=(1,2,0)$ and $v=(0,1,3)$ compute $u\times v$. Use dot products to check perpendicularity to both vectors, compute $v\times u$, and compare the results.

---

## Relevant theorem / definition

The cross product (vector product) of two vectors $\mathbf{u} = (u_1, u_2, u_3)$ and $\mathbf{v} = (v_1, v_2, v_3)$ in $\mathbb{R}^3$ is defined via the formal determinant:
$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} = (u_2 v_3 - u_3 v_2)\mathbf{i} - (u_1 v_3 - u_3 v_1)\mathbf{j} + (u_1 v_2 - u_2 v_1)\mathbf{k}.
$$
The resulting vector $\mathbf{u} \times \mathbf{v}$ is perpendicular to both $\mathbf{u}$ and $\mathbf{v}$ ($(\mathbf{u} \times \mathbf{v}) \cdot \mathbf{u} = 0$ and $(\mathbf{u} \times \mathbf{v}) \cdot \mathbf{v} = 0$). The cross product is anticommutative:
$$
\mathbf{v} \times \mathbf{u} = -(\mathbf{u} \times \mathbf{v}).
$$

---

## Solution

1. Computation of $u \times v$:
   $$
   u \times v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 0 \\ 0 & 1 & 3 \end{vmatrix}
   $$
   Expand along the first row:
   $$
   u \times v = \mathbf{i}\begin{vmatrix} 2 & 0 \\ 1 & 3 \end{vmatrix} - \mathbf{j}\begin{vmatrix} 1 & 0 \\ 0 & 3 \end{vmatrix} + \mathbf{k}\begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix}
   $$
   $$
   u \times v = \mathbf{i}(2\cdot 3 - 0\cdot 1) - \mathbf{j}(1\cdot 3 - 0\cdot 0) + \mathbf{k}(1\cdot 1 - 2\cdot 0)
   $$
   $$
   u \times v = 6\mathbf{i} - 3\mathbf{j} + 1\mathbf{k} = (6, -3, 1)
   $$

2. Checking perpendicularity using dot products:
   - Dot product with $u$:
     $$
     (u \times v) \cdot u = (6)(1) + (-3)(2) + (1)(0) = 6 - 6 + 0 = 0
     $$
     Thus, $(u \times v) \perp u$.
   - Dot product with $v$:
     $$
     (u \times v) \cdot v = (6)(0) + (-3)(1) + (1)(3) = 0 - 3 + 3 = 0
     $$
     Thus, $(u \times v) \perp v$.

3. Computation of $v \times u$:
   $$
   v \times u = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 0 & 1 & 3 \\ 1 & 2 & 0 \end{vmatrix}
   $$
   Expand along the first row:
   $$
   v \times u = \mathbf{i}(1\cdot 0 - 3\cdot 2) - \mathbf{j}(0\cdot 0 - 3\cdot 1) + \mathbf{k}(0\cdot 2 - 1\cdot 1)
   $$
   $$
   v \times u = -6\mathbf{i} + 3\mathbf{j} - 1\mathbf{k} = (-6, 3, -1)
   $$

4. Comparison of the results:
   $$
   v \times u = (-6, 3, -1) = -(6, -3, 1) = -(u \times v)
   $$
   The two vectors have identical magnitudes ($\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{v} \times \mathbf{u}\|$) and act along the same perpendicular line, but point in opposite directions, verifying the anticommutativity property of the vector cross product.

---

## Result

$$
u \times v = (6, -3, 1)
$$

$$
(u \times v) \cdot u = 0, \qquad (u \times v) \cdot v = 0
$$

$$
v \times u = (-6, 3, -1) = -(u \times v)
$$

---

## Verification

**Pass 1 — Algebraic check:** By determinant row-swap property, swapping row 2 and row 3 in the determinant negates the determinant: $\det = -\det$, so $v \times u = -(u \times v)$ holds identically.

**Pass 2 — Numerical check:** Compute the norm of both products: $\|u \times v\| = \sqrt{6^2 + (-3)^2 + 1^2} = \sqrt{36 + 9 + 1} = \sqrt{46}$. Likewise, $\|v \times u\| = \sqrt{(-6)^2 + 3^2 + (-1)^2} = \sqrt{36 + 9 + 1} = \sqrt{46}$.

**Pass 3 — Consistency check:** Lagrange's identity states $\|u \times v\|^2 = \|u\|^2 \|v\|^2 - (u \cdot v)^2$. Here $\|u\|^2 = 1^2 + 2^2 + 0^2 = 5$, $\|v\|^2 = 0^2 + 1^2 + 3^2 = 10$, and $u \cdot v = 1(0) + 2(1) + 0(3) = 2$. Then $\|u\|^2\|v\|^2 - (u\cdot v)^2 = 5(10) - 2^2 = 50 - 4 = 46 = (\sqrt{46})^2$.

---

## Exam tip

Do not forget the negative sign on the $\mathbf{j}$-component when expanding the $3 \times 3$ determinant along the first row: $-(u_1 v_3 - u_3 v_1)\mathbf{j}$.


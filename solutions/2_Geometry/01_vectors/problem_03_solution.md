# Exercise 3

**Problem:** For $v=(3,4)$ find a unit vector $e$ with the same direction and orientation. Check that $\|e\|=1$, reconstruct $v$ in the form $v=\|v\|e$, and explain what changes during normalization and what remains unchanged.

---

## Relevant theorem / definition

For any non-zero vector $\mathbf{v} \in \mathbb{R}^n$, its Euclidean length is $\|\mathbf{v}\| = \sqrt{\sum_{i=1}^n v_i^2}$. The normalized (unit) vector in the direction of $\mathbf{v}$ is
$$
\mathbf{e} = \frac{\mathbf{v}}{\|\mathbf{v}\|}.
$$
By linearity of the norm, $\|\mathbf{e}\| = \left\|\frac{1}{\|\mathbf{v}\|} \mathbf{v}\right\| = \frac{1}{\|\mathbf{v}\|} \|\mathbf{v}\| = 1$. The representation $\mathbf{v} = \|\mathbf{v}\|\mathbf{e}$ factors any vector into its magnitude $\|\mathbf{v}\|$ and its direction/orientation $\mathbf{e}$.

---

## Solution

1. Length of vector $v$:
   $$
   \|v\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
   $$

2. Normalization to obtain unit vector $e$:
   $$
   e = \frac{v}{\|v\|} = \frac{1}{5}(3, 4) = \left(\frac{3}{5}, \frac{4}{5}\right) = (0.6, 0.8)
   $$

3. Verification that $\|e\| = 1$:
   $$
   \|e\| = \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2} = \sqrt{\frac{9}{25} + \frac{16}{25}} = \sqrt{\frac{25}{25}} = 1
   $$

4. Reconstruction of $v$:
   $$
   \|v\| e = 5 \cdot \left(\frac{3}{5}, \frac{4}{5}\right) = \left(5 \cdot \frac{3}{5}, 5 \cdot \frac{4}{5}\right) = (3, 4) = v
   $$

5. What changes and what remains unchanged:
   - **What changes:** The length (magnitude) changes from $5$ to $1$.
   - **What remains unchanged:** The direction (the line through the origin containing the vector) and the orientation (the sense along that line) remain invariant, because $e$ is formed by multiplying $v$ by the strictly positive scalar $\frac{1}{5} > 0$.

---

## Result

$$
e = \left(\frac{3}{5}, \frac{4}{5}\right) = (0.6, 0.8)
$$

$$
\|e\| = 1, \qquad \|v\|e = 5 \cdot \left(\frac{3}{5}, \frac{4}{5}\right) = (3, 4) = v
$$

---

## Verification

**Pass 1 — Algebraic check:** For any scalar $c > 0$ and vector $v$, $\left\|\frac{v}{\|v\|}\right\| = \frac{\|v\|}{\|v\|} = 1$. Here $c = \frac{1}{5}$, and $e$ is collinear with $v$ since $e = \frac{1}{5}v$.

**Pass 2 — Numerical check:** $0.6^2 + 0.8^2 = 0.36 + 0.64 = 1.00$, and $\sqrt{1.00} = 1$.

**Pass 3 — Consistency check:** Both components of $v$ are positive ($3 > 0, 4 > 0$), and both components of $e$ remain positive ($0.6 > 0, 0.8 > 0$), confirming orientation preservation.

---

## Exam tip

A unit vector must always have a norm of exactly 1; if your sum of squared components does not equal 1, recheck your common denominator or square root.


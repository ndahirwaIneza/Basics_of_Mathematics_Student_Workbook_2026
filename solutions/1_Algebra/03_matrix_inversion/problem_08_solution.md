# Exercise 8

**Problem:** The matrix
$$S=\begin{pmatrix}2&0\\0&\frac12\end{pmatrix}$$
describes a scaling of the plane. Find $S^{-1}$ and explain geometrically what the inverse transformation does. Check the action of the pair $S,S^{-1}$ on one simple vector.

---

## Relevant theorem / definition

For a diagonal matrix $D = \text{diag}(d_1, d_2, \ldots, d_n)$ with non-zero diagonal entries, its inverse is $D^{-1} = \text{diag}(1/d_1, 1/d_2, \ldots, 1/d_n)$. The inverse transformation geometrically undoes the deformation caused by the original transformation, returning every point to its original position.

---

## Solution

The given scaling matrix is:
$$
S = \begin{pmatrix} 2 & 0 \\ 0 & \frac{1}{2} \end{pmatrix}
$$

1. Find $S^{-1}$:
   Because $S$ is a diagonal matrix, we invert its non-zero diagonal entries:
   $$
   S^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{1/2} \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 2 \end{pmatrix}
   $$

2. Geometric explanation:
   - The matrix $S$ performs a non-uniform scaling: it stretches the plane horizontally along the $x$-axis by a factor of 2, while compressing it vertically along the $y$-axis by a factor of $\frac{1}{2}$ (halving the $y$-coordinate).
   - The inverse matrix $S^{-1}$ performs the exact complementary geometric operation: it compresses the plane horizontally along the $x$-axis by a factor of $\frac{1}{2}$ (halving the $x$-coordinate) and stretches it vertically along the $y$-axis by a factor of 2 (doubling the $y$-coordinate).
   - Composing $S^{-1}$ with $S$ restores any geometric figure or vector to its original shape, orientation, and position.

3. Check on a simple vector:
   Choose the test vector:
   $$
   \mathbf{v} = \begin{pmatrix} 4 \\ 6 \end{pmatrix}
   $$
   Apply transformation $S$:
   $$
   S\mathbf{v} = \begin{pmatrix} 2 & 0 \\ 0 & \frac{1}{2} \end{pmatrix} \begin{pmatrix} 4 \\ 6 \end{pmatrix} = \begin{pmatrix} 2(4) + 0(6) \\ 0(4) + \frac{1}{2}(6) \end{pmatrix} = \begin{pmatrix} 8 \\ 3 \end{pmatrix}
   $$
   Now apply the inverse transformation $S^{-1}$ to the result:
   $$
   S^{-1}(S\mathbf{v}) = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 8 \\ 3 \end{pmatrix} = \begin{pmatrix} \frac{1}{2}(8) + 0(3) \\ 0(8) + 2(3) \end{pmatrix} = \begin{pmatrix} 4 \\ 6 \end{pmatrix} = \mathbf{v}
   $$
   The original vector $\mathbf{v}$ is restored.

---

## Result

$$
S^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 2 \end{pmatrix}
$$

$$
S \begin{pmatrix} 4 \\ 6 \end{pmatrix} = \begin{pmatrix} 8 \\ 3 \end{pmatrix}, \qquad S^{-1} \begin{pmatrix} 8 \\ 3 \end{pmatrix} = \begin{pmatrix} 4 \\ 6 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Verify $S S^{-1} = I$:
$$
S S^{-1} = \begin{pmatrix} 2 & 0 \\ 0 & \frac{1}{2} \end{pmatrix} \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 2\left(\frac{1}{2}\right) & 0 \\ 0 & \frac{1}{2}(2) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

**Pass 2 — Numerical check:** Determinant check: $\det(S) = 2 \cdot \frac{1}{2} - 0 = 1$. The transformation is equiareal (area-preserving). The inverse determinant is $\det(S^{-1}) = \frac{1}{2} \cdot 2 = 1 = \frac{1}{\det S}$.

**Pass 3 — Consistency check:** For an arbitrary vector $\mathbf{x} = \begin{pmatrix} x \\ y \end{pmatrix}$:
$$
S^{-1}(S\mathbf{x}) = S^{-1}\begin{pmatrix} 2x \\ y/2 \end{pmatrix} = \begin{pmatrix} \frac{1}{2}(2x) \\ 2(y/2) \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix}
$$
The identity map is produced for all $(x, y) \in \mathbb{R}^2$.

---

## Exam tip

The inverse of a diagonal matrix is simply obtained by taking the reciprocals of each diagonal entry.


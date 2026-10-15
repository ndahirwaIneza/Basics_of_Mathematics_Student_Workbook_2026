# Exercise 9

**Problem:** The vectors
$$u=\begin{pmatrix}3\\1\end{pmatrix},\qquad v=\begin{pmatrix}1\\4\end{pmatrix}$$
span a parallelogram. Compute its area using a determinant. Then reverse the order of the vectors and explain what changes in the determinant and what does not change in the area.

---

## Relevant theorem / definition

The area of the parallelogram spanned by two column vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^2$ is the absolute value of the determinant of the matrix having these vectors as its columns:
$$
\text{Area} = |\det(\mathbf{u}, \mathbf{v})|
$$
The signed determinant $\det(\mathbf{u}, \mathbf{v})$ indicates the orientation (counterclockwise when positive, clockwise when negative).

---

## Solution

1. Area computation:
   Form the matrix with columns $u$ and $v$:
   $$
   M = \begin{pmatrix} u & v \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 1 & 4 \end{pmatrix}
   $$
   Compute its determinant:
   $$
   \det(M) = 3(4) - 1(1) = 12 - 1 = 11
   $$
   The geometric area of the parallelogram is:
   $$
   \text{Area} = |\det(M)| = |11| = 11
   $$

2. Reversing the order of vectors:
   Form the matrix with columns $v$ and $u$:
   $$
   M' = \begin{pmatrix} v & u \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 4 & 1 \end{pmatrix}
   $$
   Compute its determinant:
   $$
   \det(M') = 1(1) - 3(4) = 1 - 12 = -11
   $$

3. Comparison and explanation:
   - What changes in the determinant: The sign flips from $+11$ to $-11$. Swapping two columns exchanges the roles of the basis vectors, reversing the orientation of the ordered pair from a counterclockwise system $(u, v)$ to a clockwise system $(v, u)$.
   - What does not change in the area: The geometric area of the parallelogram is given by the magnitude $|\det| = |-11| = 11$. Physical area is strictly non-negative and independent of the choice of orientation.

---

## Result

$$
\text{Area} = 11
$$

$$
\det(u, v) = 11, \qquad \det(v, u) = -11
$$

---

## Verification

**Pass 1 — Algebraic check:** Area by 3D cross product: embed vectors in $\mathbb{R}^3$: $\mathbf{u} = (3, 1, 0)$ and $\mathbf{v} = (1, 4, 0)$.
$$
\mathbf{u} \times \mathbf{v} = (0, 0, 3(4) - 1(1)) = (0, 0, 11) \implies \|\mathbf{u} \times \mathbf{v}\| = 11
$$
Algebraically confirms the determinant area formula.

**Pass 2 — Numerical check:** Area by coordinate geometry (box formula): enclose the parallelogram in a rectangle of size $4 \times 5$: Area of enclosing box = $4 \times 5 = 20$.
Subtract corner triangles and excess rectangles: two triangles of base 3, height 1 (area $2 \times \frac{3 \cdot 1}{2} = 3$), two triangles of base 1, height 4 (area $2 \times \frac{1 \cdot 4}{2} = 4$), and two corner rectangles of $0$: $20 - 3 - 4 - 2(1 \cdot 1) = 20 - 7 - 2 = 11$. Matches.

**Pass 3 — Consistency check:** Since $u$ and $v$ are not scalar multiples of each other, they span a non-degenerate 2D parallelogram, guaranteeing positive non-zero area.

---

## Exam tip

Geometric area is always non-negative: $\text{Area} = |\det(u, v)|$; the sign of the determinant indicates the orientation of the vector pair.


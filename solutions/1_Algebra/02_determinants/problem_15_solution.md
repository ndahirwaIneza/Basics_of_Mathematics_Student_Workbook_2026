# Exercise 15

**Problem:** Let $A$ and $B$ be invertible $2\times2$ matrices with
$$\det A=-2,\qquad \det B=3.$$
Without finding the entries of the matrices, compute
$$\det\left(B^{-1}A^TB\right).$$
State the determinant properties you use in order and explain why the factors involving $B$ eventually cancel.

---

## Relevant theorem / definition

For any square matrices $M, N$ and invertible matrix $P$ of the same size:
1. Product property: $\det(MN) = \det(M)\det(N)$.
2. Transpose property: $\det(M^T) = \det(M)$.
3. Inverse property: $\det(P^{-1}) = \frac{1}{\det(P)}$.
4. Similarity invariance: Similar matrices have equal determinants: $\det(P^{-1} M P) = \det(M)$.

---

## Solution

We evaluate $\det(B^{-1}A^TB)$ step by step:

Step 1: Apply the product property of determinants:
$$
\det\left(B^{-1}A^TB\right) = \det\left(B^{-1}\right) \cdot \det\left(A^T\right) \cdot \det(B)
$$

Step 2: Apply the inverse property to the first factor:
Since $B$ is invertible and $\det B = 3$:
$$
\det\left(B^{-1}\right) = \frac{1}{\det(B)} = \frac{1}{3}
$$

Step 3: Apply the transpose property to the second factor:
Since transposition does not change the determinant:
$$
\det\left(A^T\right) = \det(A) = -2
$$

Step 4: Substitute all values into the expression:
$$
\det\left(B^{-1}A^TB\right) = \left(\frac{1}{3}\right) \cdot (-2) \cdot 3
$$

Step 5: Multiply the scalar factors:
$$
\det\left(B^{-1}A^TB\right) = \left(\frac{1}{3} \cdot 3\right) \cdot (-2) = 1 \cdot (-2) = -2
$$

Explanation of why the factors involving $B$ cancel:
The transformation $M \mapsto B^{-1} M B$ represents a similarity transformation (conjugation), corresponding to a change of basis. In the determinant computation, the determinant of $B^{-1}$ is the scalar $\frac{1}{\det B}$, and the determinant of $B$ is the scalar $\det B$. Because scalars in $\mathbb{R}$ commute under ordinary multiplication, we have:
$$
\det\left(B^{-1}\right) \cdot \det(B) = \frac{1}{\det B} \cdot \det B = 1
$$
Geometrically, changing basis changes coordinate axes by an area scaling factor of $\det B$, and the inverse change of basis rescales by $\frac{1}{\det B}$. The net area distortion introduced by the coordinate change is exactly 1, leaving the determinant of the underlying operator ($A^T$, and hence $A$) unchanged.

---

## Result

$$
\det\left(B^{-1}A^TB\right) = -2
$$

---

## Verification

**Pass 1 — Algebraic check:** By similarity invariance: for any invertible $B$ and any square matrix $M$, $\det(B^{-1}MB) = \det(M)$. Setting $M = A^T$ gives $\det(B^{-1}A^TB) = \det(A^T) = \det(A) = -2$.

**Pass 2 — Numerical check:** Concrete realization: let $A = \begin{pmatrix} -2 & 0 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$.
Then $A^T = A = \begin{pmatrix} -2 & 0 \\ 0 & 1 \end{pmatrix}$ and $B^{-1} = \begin{pmatrix} 1/3 & 0 \\ 0 & 1 \end{pmatrix}$.
$$
B^{-1} A^T B = \begin{pmatrix} 1/3 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} -2/3 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 0 \\ 0 & 1 \end{pmatrix}
$$
Its determinant is $(-2)(1) - 0 = -2$, confirming the formula.

**Pass 3 — Consistency check:** Since $\det A \neq 0$ and $\det B \neq 0$, the product matrix is an invertible matrix with non-zero determinant of identical sign to $\det A$.

---

## Exam tip

The determinant is invariant under similarity transformations: $\det(P^{-1}AP) = \det(A)$ for any invertible matrix $P$.


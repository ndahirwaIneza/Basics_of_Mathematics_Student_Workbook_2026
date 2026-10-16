# Exercise 6

**Problem:** For
$$A(t)=\begin{pmatrix}t&1\\2&t\end{pmatrix}$$
find all values of $t$ for which the matrix is not invertible. Explain how your answer is related to the determinant being zero.

---

## Relevant theorem / definition

A square matrix $M$ is singular (not invertible) if and only if its determinant is zero:
$$
M \text{ is not invertible} \iff \det(M) = 0
$$

---

## Solution

1. Compute the determinant of $A(t)$:
   $$
   \det A(t) = t \cdot t - 1 \cdot 2 = t^2 - 2
   $$

2. Set the determinant to zero to find values for non-invertibility:
   $$
   \det A(t) = 0 \iff t^2 - 2 = 0 \iff t^2 = 2 \iff t = \pm\sqrt{2}
   $$

3. Relationship between non-invertibility and $\det A(t) = 0$:
   A matrix $A$ represents a linear transformation $T(\mathbf{x}) = A\mathbf{x}$. The determinant measures the oriented area scaling factor of this transformation.
   - When $\det A(t) = 0$, the transformation collapses 2D space onto a 1D line (or the origin), mapping at least one non-zero vector to zero (a nontrivial kernel).
   - Because dimension is lost, the mapping is not injective and information cannot be recovered; therefore, no two-sided inverse matrix $A^{-1}$ can exist.
   - For $t = \sqrt{2}$, the matrix is $\begin{pmatrix} \sqrt{2} & 1 \\ 2 & \sqrt{2} \end{pmatrix}$, where Row 2 is $\sqrt{2} \times \text{Row 1}$, showing direct linear dependence.
   - For $t = -\sqrt{2}$, Row 2 is $-\sqrt{2} \times \text{Row 1}$, which is also linearly dependent.

---

## Result

$$
t = \sqrt{2} \quad \text{or} \quad t = -\sqrt{2}
$$

---

## Verification

**Pass 1 — Algebraic check:** At $t = \sqrt{2}$, Row 2 is $\begin{pmatrix} 2 & \sqrt{2} \end{pmatrix} = \sqrt{2} \begin{pmatrix} \sqrt{2} & 1 \end{pmatrix} = \sqrt{2} R_1$. Linearly dependent rows algebraically prove non-invertibility.

**Pass 2 — Numerical check:** Plug in $t = 2$: $\det A(2) = 2^2 - 2 = 2 \neq 0$, which is invertible. Plug in $t = \sqrt{2}$: $\det A(\sqrt{2}) = (\sqrt{2})^2 - 2 = 2 - 2 = 0$, confirming singularity.

**Pass 3 — Consistency check:** The characteristic polynomial is
$$
\det(A(t)-\lambda I)=(t-\lambda)^2-2=(\lambda-t)^2-2.
$$
Thus the eigenvalues are $\lambda=t\pm\sqrt{2}$. Zero is an eigenvalue if and only if $t\pm\sqrt{2}=0$, which gives $t=\mp\sqrt{2}$, agreeing with the determinant calculation.

---

## Exam tip

To find where a parameterized matrix fails to be invertible, compute its determinant as a polynomial in the parameter and solve $\det A(t) = 0$.

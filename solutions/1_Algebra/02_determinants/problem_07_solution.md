# Exercise 7

**Problem:** Suppose that for a $3\times3$ matrix, $\det A=-4$. Compute
$$\det(2A),\qquad \det(A^T),\qquad \det(A^2),\qquad \det(-A).$$
Justify each answer using the appropriate property.

---

## Relevant theorem / definition

For an $n \times n$ matrix $A$ and scalar $c \in \mathbb{R}$:
1. Scalar multiplication property: $\det(cA) = c^n \det(A)$.
2. Transpose property: $\det(A^T) = \det(A)$.
3. Power / product property: $\det(A^k) = (\det A)^k$.

---

## Solution

The matrix $A$ is of size $n = 3$, and its determinant is $\det A = -4$.

1. Computation of $\det(2A)$:
   By the scalar multiplication property with $c = 2$ and dimension $n = 3$:
   $$
   \det(2A) = 2^3 \det(A) = 8 \cdot (-4) = -32
   $$
   Justification: Multiplying a matrix by a scalar $c$ multiplies every one of its $n$ rows by $c$. Since the determinant is multilinear with respect to each row, the factor $c$ is factored out $n$ times.

2. Computation of $\det(A^T)$:
   By the transpose property:
   $$
   \det(A^T) = \det(A) = -4
   $$
   Justification: Transposition reflects matrix entries across the main diagonal without altering the set of permutation products in the Leibniz formula for the determinant.

3. Computation of $\det(A^2)$:
   By the multiplicative property of determinants:
   $$
   \det(A^2) = \det(AA) = (\det A)(\det A) = (\det A)^2 = (-4)^2 = 16
   $$
   Justification: The determinant of a product of square matrices equals the product of their individual determinants.

4. Computation of $\det(-A)$:
   Applying the scalar multiplication property with $c = -1$ and $n = 3$:
   $$
   \det(-A) = (-1)^3 \det(A) = -1 \cdot (-4) = 4
   $$
   Justification: Factoring $-1$ out of each of the 3 rows yields $(-1)^3 = -1$.

---

## Result

$$
\det(2A) = -32, \qquad \det(A^T) = -4, \qquad \det(A^2) = 16, \qquad \det(-A) = 4
$$

---

## Verification

**Pass 1 — Algebraic check:** Special case matrix: let $A = \text{diag}(-4, 1, 1)$.
- $2A = \text{diag}(-8, 2, 2) \implies \det(2A) = -8 \cdot 2 \cdot 2 = -32$.
- $A^T = A \implies \det(A^T) = -4$.
- $A^2 = \text{diag}(16, 1, 1) \implies \det(A^2) = 16$.
- $-A = \text{diag}(4, -1, -1) \implies \det(-A) = 4(-1)(-1) = 4$.
All values match.

**Pass 2 — Numerical check:** Parity check on $\det(-A)$: because $n = 3$ is odd, $\det(-A) = -\det(A) = -(-4) = 4$. If $n$ had been even, $\det(-A)$ would equal $\det(A)$.

**Pass 3 — Consistency check:** For any real matrix, $\det(A^2) = (\det A)^2 \ge 0$. Here $\det(A^2) = 16 > 0$, consistent with non-negativity of squares.

---

## Exam tip

The most common exam mistake is writing $\det(cA) = c\det(A)$ instead of $c^n\det(A)$; always raise the scalar to the power equal to the matrix size $n$.


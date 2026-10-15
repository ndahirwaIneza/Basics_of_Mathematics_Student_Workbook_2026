# Exercise 8

**Problem:** Let $A,B$ be square matrices such that $\det A=3$ and $\det B=-5$. Compute $\det(AB)$, $\det(BA)$ and, if it exists, $\det(A^{-1}B)$. Explain why the first two results are equal even though usually $AB\neq BA$.

---

## Relevant theorem / definition

For any square matrices $A, B \in \mathbb{R}^{n \times n}$:
1. Product rule: $\det(AB) = \det(A)\det(B)$.
2. Inverse rule: If $\det(A) \neq 0$, then $A$ is invertible and $\det(A^{-1}) = \frac{1}{\det(A)}$.

---

## Solution

Given:
$$
\det A = 3, \qquad \det B = -5
$$

1. Computation of $\det(AB)$:
   $$
   \det(AB) = \det(A) \cdot \det(B) = 3 \cdot (-5) = -15
   $$

2. Computation of $\det(BA)$:
   $$
   \det(BA) = \det(B) \cdot \det(A) = (-5) \cdot 3 = -15
   $$

3. Computation of $\det(A^{-1}B)$:
   Since $\det A = 3 \neq 0$, $A$ is invertible. Its inverse has determinant:
   $$
   \det(A^{-1}) = \frac{1}{\det A} = \frac{1}{3}
   $$
   Therefore:
   $$
   \det(A^{-1}B) = \det(A^{-1}) \cdot \det(B) = \frac{1}{3} \cdot (-5) = -\frac{5}{3}
   $$

4. Explanation of why $\det(AB) = \det(BA)$ even though $AB \neq BA$:
   Matrix multiplication is non-commutative in the matrix ring ($AB \neq BA$ in general). However, the determinant function maps matrices to real numbers ($\det: \mathbb{R}^{n \times n} \to \mathbb{R}$). In the field of real numbers $\mathbb{R}$, scalar multiplication is commutative. Therefore:
   $$
   \det(AB) = \det(A)\det(B) = \det(B)\det(A) = \det(BA)
   $$
   While the matrices $AB$ and $BA$ represent different linear transformations, they scale oriented $n$-dimensional volumes by the exact same overall factor.

---

## Result

$$
\det(AB) = -15, \qquad \det(BA) = -15, \qquad \det(A^{-1}B) = -\frac{5}{3}
$$

---

## Verification

**Pass 1 — Algebraic check:** Check $A (A^{-1}B) = B$:
$$
\det(A(A^{-1}B)) = \det(A) \det(A^{-1}B) = 3 \cdot \left(-\frac{5}{3}\right) = -5 = \det(B)
$$
Algebraically consistent with the multiplicative property.

**Pass 2 — Numerical check:** Let $A = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} -5 & 0 \\ 0 & 1 \end{pmatrix}$.
Then $AB = BA = \begin{pmatrix} -15 & 0 \\ 0 & 1 \end{pmatrix} \implies \det(AB) = -15$.
$A^{-1}B = \begin{pmatrix} 1/3 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} -5 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} -5/3 & 0 \\ 0 & 1 \end{pmatrix} \implies \det(A^{-1}B) = -5/3$.

**Pass 3 — Consistency check:** Since $\det A \neq 0$ and $\det B \neq 0$, the products $AB, BA$ and $A^{-1}B$ are all invertible matrices with non-zero determinants.

---

## Exam tip

$\det(AB) = \det(BA)$ holds for all square matrices of the same size, even though $AB \neq BA$ in general.


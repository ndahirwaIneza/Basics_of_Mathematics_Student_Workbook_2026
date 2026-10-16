# Exercise 7

**Problem:** Given
$$u=(1,2,3),\qquad v=(2,4,6),\qquad w=(0,1,1).$$
Identify a specific relation between $u$ and $v$, decide whether the three vectors can be linearly independent, and explain why no long calculation is needed.

---

## Relevant theorem / definition

A set of vectors $\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ in a vector space $V$ is linearly dependent if there exist scalars $c_1, \dots, c_k$, not all zero, such that
$$
c_1 \mathbf{v}_1 + \dots + c_k \mathbf{v}_k = \mathbf{0}.
$$
In particular, if any two vectors in the set are collinear (one is a scalar multiple of the other: $\mathbf{v}_j = c \mathbf{v}_i$), the entire set is linearly dependent. Consequently, no larger set containing a linearly dependent subset can be linearly independent.

---

## Solution

1. Identification of the relation between $u$ and $v$:
   Comparing components of $u = (1, 2, 3)$ and $v = (2, 4, 6)$:
   $$
   2 = 2(1), \qquad 4 = 2(2), \qquad 6 = 2(3)
   $$
   Therefore:
   $$
   v = 2u \iff 2u - v = \mathbf{0}
   $$

2. Decision on linear independence of $\{u, v, w\}$:
   The vectors cannot be linearly independent; they are linearly dependent.

3. Explanation why no long calculation is needed:
   A non-trivial linear combination that sums to zero can be written immediately by taking non-zero weights for $u$ and $v$ and zero weight for $w$:
   $$
   2u - 1v + 0w = 2(1, 2, 3) - (2, 4, 6) + 0(0, 1, 1) = (0, 0, 0) = \mathbf{0}
   $$
   Since the coefficients $(c_1, c_2, c_3) = (2, -1, 0)$ are not all zero, the definition of linear dependence is satisfied directly by inspection. No determinant computation or Gaussian elimination is required.

---

## Result

$$
v = 2u \quad (v \text{ is a scalar multiple of } u)
$$

$$
\{u, v, w\} \text{ is linearly dependent}
$$

---

## Verification

**Pass 1 — Algebraic check:** Form the matrix with row vectors $u, v, w$:
$$
\begin{vmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 1 \end{vmatrix}
$$
Row 2 is $2 \times \text{Row 1}$. A determinant with proportional rows is identically 0: $\det = 0$, confirming linear dependence algebraically.

**Pass 2 — Numerical check:** Evaluating the linear combination explicitly:
$$
2(1, 2, 3) - 1(2, 4, 6) + 0(0, 1, 1) = (2 - 2 + 0, 4 - 4 + 0, 6 - 6 + 0) = (0, 0, 0)
$$

**Pass 3 — Consistency check:** Since $u$ and $v$ lie on the same 1D line through the origin, the subspace spanned by $\{u, v, w\}$ has dimension at most 2, which is strictly less than 3, proving linear dependence.

---

## Exam tip

Before applying row operations or setting up a determinant, always inspect vectors for pairs with proportional coordinates ($v = cu$).


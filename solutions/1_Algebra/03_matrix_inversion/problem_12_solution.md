# Exercise 12

**Problem:** It is known that
$$A^{-1}=\begin{pmatrix}2&-1\\-3&2\end{pmatrix}.$$
Without finding $A$, compute $(3A)^{-1}$, $(A^T)^{-1}$, and $(A^2)^{-1}$. Justify each result using the appropriate property.

---

## Relevant theorem / definition

For an invertible matrix $A$ and non-zero scalar $c \in \mathbb{R}$:
1. Scalar multiplication of an inverse: $(cA)^{-1} = \frac{1}{c} A^{-1}$.
2. Transpose of an inverse: $(A^T)^{-1} = (A^{-1})^T$.
3. Power of an inverse: $(A^k)^{-1} = (A^{-1})^k$.

---

## Solution

Given:
$$
A^{-1} = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}
$$

1. Computation of $(3A)^{-1}$:
   Property used: $(cA)^{-1} = \frac{1}{c} A^{-1}$ for any non-zero scalar $c$.
   With $c = 3$:
   $$
   (3A)^{-1} = \frac{1}{3} A^{-1} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix} = \begin{pmatrix} \frac{2}{3} & -\frac{1}{3} \\ -1 & \frac{2}{3} \end{pmatrix}
   $$
   Justification: $(3A)\left(\frac{1}{3}A^{-1}\right) = \left(3 \cdot \frac{1}{3}\right)(A A^{-1}) = 1 \cdot I = I$.

2. Computation of $(A^T)^{-1}$:
   Property used: Inversion and transposition commute: $(A^T)^{-1} = (A^{-1})^T$.
   Transposing $A^{-1}$:
   $$
   (A^T)^{-1} = (A^{-1})^T = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}^T = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}
   $$
   Justification: $A^T (A^{-1})^T = (A^{-1} A)^T = I^T = I$.

3. Computation of $(A^2)^{-1}$:
   Property used: $(A^2)^{-1} = (AA)^{-1} = A^{-1} A^{-1} = (A^{-1})^2$.
   Squaring $A^{-1}$:
   $$
   \begin{align}
   (A^2)^{-1} &= (A^{-1})^2 = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix} \\
   &= \begin{pmatrix} 2(2) + (-1)(-3) & 2(-1) + (-1)(2) \\ -3(2) + 2(-3) & -3(-1) + 2(2) \end{pmatrix} \\
   &= \begin{pmatrix} 4 + 3 & -2 - 2 \\ -6 - 6 & 3 + 4 \end{pmatrix} \\
   &= \begin{pmatrix} 7 & -4 \\ -12 & 7 \end{pmatrix}
   \end{align}
   $$
   Justification: $(A^2)(A^{-1})^2 = A(A A^{-1}) A^{-1} = A I A^{-1} = A A^{-1} = I$.

---

## Result

$$
(3A)^{-1} = \begin{pmatrix} \frac{2}{3} & -\frac{1}{3} \\ -1 & \frac{2}{3} \end{pmatrix}, \qquad (A^T)^{-1} = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}, \qquad (A^2)^{-1} = \begin{pmatrix} 7 & -4 \\ -12 & 7 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Find $A = (A^{-1})^{-1}$ to check consistency:
$\det(A^{-1}) = 2(2) - (-1)(-3) = 4 - 3 = 1$.
$$
A = \frac{1}{1}\begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}
$$
- $3A = \begin{pmatrix} 6 & 3 \\ 9 & 6 \end{pmatrix} \implies (3A)^{-1} = \frac{1}{9}\begin{pmatrix} 6 & -3 \\ -9 & 6 \end{pmatrix} = \begin{pmatrix} 2/3 & -1/3 \\ -1 & 2/3 \end{pmatrix}$.
- $A^T = \begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix} \implies (A^T)^{-1} = \frac{1}{1}\begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}$.
- $A^2 = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 7 & 4 \\ 12 & 7 \end{pmatrix} \implies (A^2)^{-1} = \frac{1}{49-48}\begin{pmatrix} 7 & -4 \\ -12 & 7 \end{pmatrix} = \begin{pmatrix} 7 & -4 \\ -12 & 7 \end{pmatrix}$.
All three match.

**Pass 2 — Numerical check:** Determinant consistency: $\det(A^{-1}) = 1$.
- $\det((3A)^{-1}) = \left(\frac{1}{3}\right)^2 \det(A^{-1}) = \frac{1}{9}$. From matrix: $\left(\frac{2}{3}\right)\left(\frac{2}{3}\right) - \left(-\frac{1}{3}\right)(-1) = \frac{4}{9} - \frac{3}{9} = \frac{1}{9}$.
- $\det((A^2)^{-1}) = 7(7) - (-4)(-12) = 49 - 48 = 1 = (\det A^{-1})^2$.

**Pass 3 — Consistency check:** Since $A^{-1}$ has integer entries with determinant 1 (unimodular), all its powers have integer entries and determinant 1.

---

## Exam tip

Never invert $A^{-1}$ to find $A$ if the problem only asks for inverses of algebraic expressions of $A$; apply inverse algebraic identities directly to $A^{-1}$.


# Exercise 11

**Problem:** For
$$A(t)=\begin{pmatrix}1&t\\t&1\end{pmatrix}$$
find all $t$ for which the matrix is invertible, and then give a formula for $A(t)^{-1}$. Explain what happens to this formula at the excluded values.

---

## Relevant theorem / definition

A square matrix $A$ is invertible if and only if $\det(A) \neq 0$. For a $2 \times 2$ matrix:
$$
A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$
Division by zero at $\det(A) = 0$ corresponds to a singular matrix where the linear transformation collapses dimension.

---

## Solution

The given parameterized matrix is:
$$
A(t) = \begin{pmatrix} 1 & t \\ t & 1 \end{pmatrix}
$$

1. Determine invertibility condition:
   Compute the determinant of $A(t)$:
   $$
   \det A(t) = 1(1) - t(t) = 1 - t^2
   $$
   The matrix is invertible if and only if $\det A(t) \neq 0$:
   $$
   1 - t^2 \neq 0 \iff t^2 \neq 1 \iff t \neq 1 \quad \text{and} \quad t \neq -1
   $$
   Therefore, $A(t)$ is invertible for all $t \in \mathbb{R} \setminus \{-1, 1\}$.

2. Formula for $A(t)^{-1}$:
   Applying the $2 \times 2$ inversion formula:
   $$
   A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix} 1 & -t \\ -t & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{1 - t^2} & -\frac{t}{1 - t^2} \\ -\frac{t}{1 - t^2} & \frac{1}{1 - t^2} \end{pmatrix}
   $$

3. Explanation of what happens at the excluded values:
   - At $t = 1$:
     The matrix becomes $A(1) = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$. Both rows are identical ($R_1 = R_2$). The transformation maps any vector $\begin{pmatrix} x \\ y \end{pmatrix}$ to $(x+y) \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, collapsing the entire 2D plane onto the 1D diagonal line $y = x$.
   - At $t = -1$:
     The matrix becomes $A(-1) = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$. Here $R_2 = -R_1$. The transformation maps any vector to $(x-y) \begin{pmatrix} 1 \\ -1 \end{pmatrix}$, collapsing 2D space onto the line $y = -x$.
   In the formula, substituting $t = \pm 1$ yields a denominator of $1 - (\pm 1)^2 = 0$. Division by zero is undefined, reflecting the geometric fact that once a 2D plane is collapsed onto a 1D line, points that mapped to the same location cannot be uniquely separated, making an inverse mapping mathematically impossible.

---

## Result

$$
A(t) \text{ is invertible for } t \in \mathbb{R} \setminus \{-1, 1\}
$$

$$
A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix} 1 & -t \\ -t & 1 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Multiply $A(t) A(t)^{-1}$:
$$
\begin{align}
A(t) A(t)^{-1} &= \begin{pmatrix} 1 & t \\ t & 1 \end{pmatrix} \cdot \frac{1}{1 - t^2} \begin{pmatrix} 1 & -t \\ -t & 1 \end{pmatrix} \\
&= \frac{1}{1 - t^2} \begin{pmatrix} 1(1) + t(-t) & 1(-t) + t(1) \\ t(1) + 1(-t) & t(-t) + 1(1) \end{pmatrix} \\
&= \frac{1}{1 - t^2} \begin{pmatrix} 1 - t^2 & 0 \\ 0 & 1 - t^2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
\end{align}
$$
The product is the identity matrix for all $t \neq \pm 1$.

**Pass 2 — Numerical check:** Plug in $t = 0$: $A(0) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$. The formula gives $A(0)^{-1} = \frac{1}{1} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$, which is correct. Plug in $t = 2$: $\det = 1 - 4 = -3$, $A(2)^{-1} = -\frac{1}{3} \begin{pmatrix} 1 & -2 \\ -2 & 1 \end{pmatrix}$. Check: $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}\left(-\frac{1}{3}\right)\begin{pmatrix} 1 & -2 \\ -2 & 1 \end{pmatrix} = -\frac{1}{3}\begin{pmatrix} -3 & 0 \\ 0 & -3 \end{pmatrix} = I$.

**Pass 3 — Consistency check:** Eigenvalues of $A(t)$ are $\lambda = 1 \pm t$. The matrix is singular when at least one eigenvalue is zero, which occurs precisely when $1 \pm t = 0 \implies t = \mp 1$.

---

## Exam tip

Factoring the determinant as $\det A(t) = (1-t)(1+t)$ immediately identifies the excluded parameter values and explains why each distinct sign produces a different collapsed subspace.


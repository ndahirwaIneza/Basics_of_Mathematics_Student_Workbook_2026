# Exercise 10

**Problem:** Given
$$D=\begin{pmatrix}2&0&0\\0&-3&0\\0&0&5\end{pmatrix},\qquad E=\begin{pmatrix}2&0&0\\0&0&0\\0&0&5\end{pmatrix}.$$
Without using Gauss–Jordan elimination, decide which matrix is invertible. For the invertible matrix, give the inverse and check the result by multiplication.

---

## Relevant theorem / definition

A diagonal matrix $M = \text{diag}(d_1, d_2, \ldots, d_n)$ has determinant $\det(M) = d_1 d_2 \cdots d_n$.
Therefore:
1. $M$ is invertible if and only if all of its diagonal entries are non-zero: $d_i \neq 0$ for all $i$.
2. When invertible, its inverse is the diagonal matrix of reciprocals:
$$
M^{-1} = \text{diag}\left(\frac{1}{d_1}, \frac{1}{d_2}, \ldots, \frac{1}{d_n}\right)
$$

---

## Solution

1. Decision on invertibility:
   - For matrix $D$:
     The diagonal entries are $d_{11} = 2$, $d_{22} = -3$, and $d_{33} = 5$. Since all diagonal entries are non-zero:
     $$
     \det(D) = 2 \cdot (-3) \cdot 5 = -30 \neq 0
     $$
     Therefore, matrix $D$ is invertible.
   - For matrix $E$:
     The second diagonal entry is $e_{22} = 0$. The second row of $E$ consists entirely of zeros: $\begin{pmatrix} 0 & 0 & 0 \end{pmatrix}$.
     $$
     \det(E) = 2 \cdot 0 \cdot 5 = 0
     $$
     Because $\det(E) = 0$ (or equivalently, because it has a zero row), matrix $E$ is singular and not invertible.

2. Inverse of matrix $D$:
   Reciprocate each diagonal entry:
   $$
   D^{-1} = \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -\frac{1}{3} & 0 \\ 0 & 0 & \frac{1}{5} \end{pmatrix}
   $$

3. Check by multiplication $D D^{-1}$:
   $$
   D D^{-1} = \begin{pmatrix} 2 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 5 \end{pmatrix} \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -\frac{1}{3} & 0 \\ 0 & 0 & \frac{1}{5} \end{pmatrix} = \begin{pmatrix} 2\left(\frac{1}{2}\right) & 0 & 0 \\ 0 & -3\left(-\frac{1}{3}\right) & 0 \\ 0 & 0 & 5\left(\frac{1}{5}\right) \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3
   $$
   The product equals the $3 \times 3$ identity matrix.

---

## Result

$$
D \text{ is invertible}, \qquad E \text{ is not invertible}
$$

$$
D^{-1} = \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -\frac{1}{3} & 0 \\ 0 & 0 & \frac{1}{5} \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Null space check for $E$: $E \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$. The standard basis vector $\mathbf{e}_2 \neq \mathbf{0}$ lies in the null space, algebraically confirming that $E$ cannot be invertible.

**Pass 2 — Numerical check:** Check the reverse product $D^{-1} D$:
$$
\begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -\frac{1}{3} & 0 \\ 0 & 0 & \frac{1}{5} \end{pmatrix} \begin{pmatrix} 2 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 5 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3
$$

**Pass 3 — Consistency check:** Determinant of inverse: $\det(D^{-1}) = \left(\frac{1}{2}\right)\left(-\frac{1}{3}\right)\left(\frac{1}{5}\right) = -\frac{1}{30} = \frac{1}{\det D}$.

---

## Exam tip

A diagonal matrix is invertible if and only if there are no zeros on its main diagonal, and its inverse is found by reciprocating each diagonal entry directly.


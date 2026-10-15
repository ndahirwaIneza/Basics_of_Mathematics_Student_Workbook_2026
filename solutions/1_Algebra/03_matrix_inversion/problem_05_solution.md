# Exercise 5

**Problem:** Use Gauss–Jordan elimination to find the inverse of
$$A=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}.$$
Check the result by multiplication.

---

## Relevant theorem / definition

For an $n \times n$ matrix $A$, if $[A \mid I_n]$ can be row-reduced to $[I_n \mid B]$, then $A$ is invertible and $A^{-1} = B$. Verification requires checking $A A^{-1} = I_n$.

---

## Solution

The initial augmented matrix is:
$$
[A \mid I] = \left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 0 & 1
\end{array}\right]
$$

Step 1: Eliminate entry $(3,1)$ using pivot $(1,1) = 1$:
Apply $R_3 \leftarrow R_3 - R_1$:
$$
\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
0 & -1 & 1 & -1 & 0 & 1
\end{array}\right]
$$

Step 2: Eliminate entry $(3,2)$ using pivot $(2,2) = 1$:
Apply $R_3 \leftarrow R_3 + R_2$:
$$
\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 2 & -1 & 1 & 1
\end{array}\right]
$$

Step 3: Scale Row 3 to create pivot 1 in position $(3,3)$:
Apply $R_3 \leftarrow \frac{1}{2} R_3$:
$$
\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{array}\right]
$$

Step 4: Upward elimination: eliminate entry $(2,3)$ using pivot $(3,3) = 1$:
Apply $R_2 \leftarrow R_2 - R_3$:
$$
\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 - \left(-\frac{1}{2}\right) & 1 - \frac{1}{2} & 0 - \frac{1}{2} \\
0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{array}\right] =
\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{array}\right]
$$

Step 5: Upward elimination: eliminate entry $(1,2)$ using pivot $(2,2) = 1$:
Apply $R_1 \leftarrow R_1 - R_2$:
$$
\left[\begin{array}{ccc|ccc}
1 & 0 & 0 & 1 - \frac{1}{2} & 0 - \frac{1}{2} & 0 - \left(-\frac{1}{2}\right) \\
0 & 1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{array}\right] =
\left[\begin{array}{ccc|ccc}
1 & 0 & 0 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
0 & 1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{array}\right]
$$

The matrix on the right is $A^{-1}$:
$$
A^{-1} = \frac{1}{2} \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{pmatrix}
$$

Check by multiplication $A A^{-1}$:
$$
\begin{align}
A A^{-1} &= \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \cdot \frac{1}{2} \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix} \\
&= \frac{1}{2} \begin{pmatrix} 1(1)+1(1)+0 & 1(-1)+1(1)+0 & 1(1)+1(-1)+0 \\ 0+1(1)+1(-1) & 0+1(1)+1(1) & 0+1(-1)+1(1) \\ 1(1)+0+1(-1) & 1(-1)+0+1(1) & 1(1)+0+1(1) \end{pmatrix} \\
&= \frac{1}{2} \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I
\end{align}
$$

---

## Result

$$
A^{-1} = \frac{1}{2} \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Determinant check: $\det(A) = 1(1-0) - 1(0-1) + 0 = 1 + 1 = 2$. By Jacobi's adjugate formula, $A^{-1} = \frac{1}{\det A} C^T$. The cofactor matrix is $C = \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}$, so $C^T = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}$. Dividing by $\det A = 2$ gives exactly $A^{-1}$.

**Pass 2 — Numerical check:** Check the reverse product $A^{-1} A$:
$$
\frac{1}{2} \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1+0+1 & 1-1+0 & 0-1+1 \\ 1+0-1 & 1+1+0 & 0+1-1 \\ -1+0+1 & -1+1+0 & 0+1+1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix} = I
$$

**Pass 3 — Consistency check:** Matrix $A$ has circulant symmetry, which is preserved in its inverse: each row is a cyclically shifted permutation of the entries.

---

## Exam tip

Keep the common scalar factor $\frac{1}{2}$ outside the matrix during computations to avoid fraction arithmetic until the final step.


# Exercise 2

**Problem:** Find the inverse of
$$A=\begin{pmatrix}3&2\\5&4\end{pmatrix}$$
using the formula for a $2\times2$ matrix. At the end, check the result by computing one product with $A$.

---

## Relevant theorem / definition

For an invertible $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $\det(A) = ad - bc \neq 0$, the inverse matrix is given by:
$$
A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$

---

## Solution

The given matrix is:
$$
A = \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix}
$$

Step 1: Compute the determinant of $A$:
$$
\det(A) = 3(4) - 2(5) = 12 - 10 = 2
$$
Since $\det(A) = 2 \neq 0$, the matrix $A$ is invertible.

Step 2: Apply the $2 \times 2$ inverse formula:
Swap the main diagonal entries ($3$ and $4$), negate the off-diagonal entries ($2$ and $5$), and divide by the determinant ($2$):
$$
A^{-1} = \frac{1}{2} \begin{pmatrix} 4 & -2 \\ -5 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -\frac{5}{2} & \frac{3}{2} \end{pmatrix}
$$

Step 3: Verification by computing the product $A A^{-1}$:
$$
\begin{align}
A A^{-1} &= \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -\frac{5}{2} & \frac{3}{2} \end{pmatrix} \\
&= \begin{pmatrix} 3(2) + 2\left(-\frac{5}{2}\right) & 3(-1) + 2\left(\frac{3}{2}\right) \\ 5(2) + 4\left(-\frac{5}{2}\right) & 5(-1) + 4\left(\frac{3}{2}\right) \end{pmatrix} \\
&= \begin{pmatrix} 6 - 5 & -3 + 3 \\ 10 - 10 & -5 + 6 \end{pmatrix} \\
&= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
\end{align}
$$
The product yields the identity matrix $I$.

---

## Result

$$
A^{-1} = \begin{pmatrix} 2 & -1 \\ -\frac{5}{2} & \frac{3}{2} \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Trace and determinant check: $\det(A^{-1}) = 2\left(\frac{3}{2}\right) - (-1)\left(-\frac{5}{2}\right) = 3 - \frac{5}{2} = \frac{1}{2} = \frac{1}{\det A}$.

**Pass 2 — Numerical check:** Compute the reverse product $A^{-1} A$:
$$
A^{-1} A = \begin{pmatrix} 2 & -1 \\ -\frac{5}{2} & \frac{3}{2} \end{pmatrix} \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix} = \begin{pmatrix} 6 - 5 & 4 - 4 \\ -\frac{15}{2} + \frac{15}{2} & -5 + 6 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

**Pass 3 — Consistency check:** Dimension check: $A$ is $2 \times 2$, so $A^{-1}$ must be $2 \times 2$. All rows and columns have size 2.

---

## Exam tip

In the $2 \times 2$ formula, remember to swap the diagonal entries and change the signs of the off-diagonal entries before dividing by $\det(A)$.


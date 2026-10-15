# Exercise 6

**Problem:** Solve
$$Ax=b,$$
where
$$A=\begin{pmatrix}2&1\\1&3\end{pmatrix},\qquad b=\begin{pmatrix}5\\7\end{pmatrix},$$
using $x=A^{-1}b$. Then substitute the resulting vector back into the equation and check the result.

---

## Relevant theorem / definition

For an invertible square matrix $A$ and vector $b$, the matrix equation $Ax = b$ has a unique solution given by:
$$
x = A^{-1}b
$$
For a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

---

## Solution

The system is:
$$
A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}, \qquad b = \begin{pmatrix} 5 \\ 7 \end{pmatrix}
$$

Step 1: Compute $A^{-1}$:
$$
\det(A) = 2(3) - 1(1) = 6 - 1 = 5 \neq 0
$$
Since $\det(A) \neq 0$, $A$ is invertible. Using the $2 \times 2$ formula:
$$
A^{-1} = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}
$$

Step 2: Compute $x = A^{-1}b$:
$$
x = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 5 \\ 7 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 3(5) + (-1)(7) \\ -1(5) + 2(7) \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 15 - 7 \\ -5 + 14 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 8 \\ 9 \end{pmatrix} = \begin{pmatrix} \frac{8}{5} \\ \frac{9}{5} \end{pmatrix}
$$

Step 3: Check by substituting $x$ back into $Ax$:
$$
Ax = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} \frac{8}{5} \\ \frac{9}{5} \end{pmatrix} = \begin{pmatrix} 2\left(\frac{8}{5}\right) + 1\left(\frac{9}{5}\right) \\ 1\left(\frac{8}{5}\right) + 3\left(\frac{9}{5}\right) \end{pmatrix} = \begin{pmatrix} \frac{16 + 9}{5} \\ \frac{8 + 27}{5} \end{pmatrix} = \begin{pmatrix} \frac{25}{5} \\ \frac{35}{5} \end{pmatrix} = \begin{pmatrix} 5 \\ 7 \end{pmatrix} = b
$$
The solution vector satisfies the equation exactly.

---

## Result

$$
x = \begin{pmatrix} \frac{8}{5} \\ \frac{9}{5} \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Check using Cramer's rule:
$$
x_1 = \frac{\begin{vmatrix} 5 & 1 \\ 7 & 3 \end{vmatrix}}{\det A} = \frac{15 - 7}{5} = \frac{8}{5}, \qquad x_2 = \frac{\begin{vmatrix} 2 & 5 \\ 1 & 7 \end{vmatrix}}{\det A} = \frac{14 - 5}{5} = \frac{9}{5}
$$
Cramer's rule yields the identical vector.

**Pass 2 — Numerical check:** Gaussian elimination check:
Subtract $\frac{1}{2} R_1$ from $R_2$: $3 - \frac{1}{2} = \frac{5}{2}$, and $7 - \frac{5}{2} = \frac{9}{2}$.
Then $\frac{5}{2} x_2 = \frac{9}{2} \implies x_2 = \frac{9}{5}$.
Then $2x_1 + \frac{9}{5} = 5 \implies 2x_1 = \frac{16}{5} \implies x_1 = \frac{8}{5}$.

**Pass 3 — Consistency check:** Dimension check: $A^{-1}$ is $2 \times 2$, $b$ is $2 \times 1$; the product $x$ is a $2 \times 1$ column vector.

---

## Exam tip

Multiplying $Ax = b$ by $A^{-1}$ must be done on the left ($x = A^{-1}b$), never on the right ($b A^{-1}$ is undefined).


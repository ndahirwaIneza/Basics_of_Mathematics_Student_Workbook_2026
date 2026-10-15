# Exercise 4

**Problem:** Without expanding the determinant, compute
$$\det\begin{pmatrix}2&4&1\\0&-3&5\\0&0&7\end{pmatrix}.$$
State the rule for an arbitrary triangular matrix and explain it using this example.

---

## Relevant theorem / definition

The determinant of any upper triangular, lower triangular, or diagonal matrix $T = (t_{ij})_{n \times n}$ equals the product of its main diagonal entries:
$$
\det(T) = \prod_{i=1}^n t_{ii} = t_{11} t_{22} \cdots t_{nn}
$$

---

## Solution

The given matrix is:
$$
T = \begin{pmatrix} 2 & 4 & 1 \\ 0 & -3 & 5 \\ 0 & 0 & 7 \end{pmatrix}
$$

This matrix is upper triangular because all entries strictly below the main diagonal are zero ($t_{21} = 0, t_{31} = 0, t_{32} = 0$).

Application of the rule:
$$
\det(T) = 2 \cdot (-3) \cdot 7 = -42
$$

Explanation using this example:
Perform cofactor expansion along the first column. Since all entries below the first entry are zero:
$$
\det(T) = 2 \cdot \begin{vmatrix} -3 & 5 \\ 0 & 7 \end{vmatrix} - 0 + 0 = 2 \cdot \begin{vmatrix} -3 & 5 \\ 0 & 7 \end{vmatrix}
$$
The remaining $2 \times 2$ submatrix is itself upper triangular. Expanding this submatrix along its first column yields:
$$
\begin{vmatrix} -3 & 5 \\ 0 & 7 \end{vmatrix} = (-3) \cdot 7 - 5 \cdot 0 = (-3) \cdot 7
$$
Multiplying by the first diagonal factor gives:
$$
\det(T) = 2 \cdot [(-3) \cdot 7] = -42
$$
In any triangular matrix of size $n$, this recursive column expansion isolates one diagonal entry at a time, leaving only the product of all diagonal elements.

---

## Result

$$
\det\begin{pmatrix} 2 & 4 & 1 \\ 0 & -3 & 5 \\ 0 & 0 & 7 \end{pmatrix} = -42
$$

---

## Verification

**Pass 1 — Algebraic check:** Trace of the matrix is $2 + (-3) + 7 = 6$. The eigenvalues of any triangular matrix are its diagonal entries: $\lambda_1 = 2, \lambda_2 = -3, \lambda_3 = 7$. By the spectral identity, $\det(T) = \prod \lambda_i = 2(-3)(7) = -42$.

**Pass 2 — Numerical check:** Full Sarrus expansion:
$(2 \cdot (-3) \cdot 7 + 4 \cdot 5 \cdot 0 + 1 \cdot 0 \cdot 0) - (1 \cdot (-3) \cdot 0 + 4 \cdot 0 \cdot 7 + 2 \cdot 5 \cdot 0) = -42 - 0 = -42$.

**Pass 3 — Consistency check:** Since all diagonal entries are non-zero ($2 \neq 0, -3 \neq 0, 7 \neq 0$), the matrix is non-singular and its determinant is non-zero.

---

## Exam tip

Whenever a matrix is triangular, compute its determinant immediately by multiplying the diagonal entries without writing any cofactor expansions.


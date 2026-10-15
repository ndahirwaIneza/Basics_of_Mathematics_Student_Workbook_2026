# Exercise 12

**Problem:** For
$$A(t)=\begin{pmatrix}1&2&3\\2&4&t\\0&1&1\end{pmatrix}$$
find the values of $t$ for which the matrix is not invertible.

Before computing the determinant, perform the operation
$$R_2\leftarrow R_2-2R_1$$
and use the resulting structure. At the end, explain what special thing happens to the rows for the value of the parameter you found.

---

## Relevant theorem / definition

A matrix $A(t)$ is not invertible if and only if $\det A(t) = 0$. Row replacement operations of the form $R_2 \leftarrow R_2 - 2R_1$ preserve the value of the determinant:
$$
\det(A(t)) = \det(A_{\text{reduced}}(t))
$$

---

## Solution

The initial matrix is:
$$
A(t) = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & t \\ 0 & 1 & 1 \end{pmatrix}
$$

1. Perform the operation $R_2 \leftarrow R_2 - 2R_1$:
   $$
   R_2 - 2R_1 = \begin{pmatrix} 2 - 2(1) & 4 - 2(2) & t - 2(3) \end{pmatrix} = \begin{pmatrix} 0 & 0 & t-6 \end{pmatrix}
   $$
   The resulting matrix is:
   $$
   \tilde{A}(t) = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & t-6 \\ 0 & 1 & 1 \end{pmatrix}
   $$
   Since this is a row replacement operation, $\det A(t) = \det \tilde{A}(t)$.

2. Compute the determinant using the resulting structure:
   Notice that the second row has zeros in the first two columns. Expand along Row 2:
   $$
   \det A(t) = \det \tilde{A}(t) = (-1)^{2+3} (t-6) \cdot \begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix} = -(t-6)(1 \cdot 1 - 2 \cdot 0) = -(t-6) = 6 - t
   $$

3. Find values of $t$ for which $A(t)$ is not invertible:
   $$
   \det A(t) = 0 \iff 6 - t = 0 \iff t = 6
   $$

4. Explanation of what happens to the rows when $t = 6$:
   When $t = 6$, the second row of the original matrix is:
   $$
   R_2 = \begin{pmatrix} 2 & 4 & 6 \end{pmatrix} = 2 \begin{pmatrix} 1 & 2 & 3 \end{pmatrix} = 2 R_1
   $$
   Row 2 is an exact scalar multiple of Row 1. Consequently, after the row operation $R_2 \leftarrow R_2 - 2R_1$, the entire second row becomes a zero row: $\begin{pmatrix} 0 & 0 & 0 \end{pmatrix}$. This creates immediate linear dependence between the rows, reducing the rank from 3 to 2 and causing the determinant to vanish.

---

## Result

$$
t = 6
$$

$$
\det A(t) = 6 - t
$$

---

## Verification

**Pass 1 — Algebraic check:** Direct Sarrus expansion on original $A(t)$:
$$
\begin{align}
\det A(t) &= [1(4)(1) + 2(t)(0) + 3(2)(1)] - [3(4)(0) + 1(t)(1) + 2(2)(1)] \\
&= [4 + 0 + 6] - [0 + t + 4] \\
&= 10 - (t + 4) = 6 - t
\end{align}
$$
Algebraically confirms $\det A(t) = 6 - t$.

**Pass 2 — Numerical check:** Plug in $t = 0$: $\det A(0) = 6 - 0 = 6$. By Sarrus with $t = 0$: $[4 + 0 + 6] - [0 + 0 + 4] = 10 - 4 = 6$. Plug in $t = 6$: $\det A(6) = 6 - 6 = 0$.

**Pass 3 — Consistency check:** Swapping rows 2 and 3 of $\tilde{A}(t)$ gives $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & t-6 \end{pmatrix}$, an upper triangular matrix with determinant $1 \cdot 1 \cdot (t-6) = t-6$. Since one row swap introduces a factor of $-1$, $\det A(t) = -(t-6) = 6-t$.

---

## Exam tip

Eliminating with row operations before expanding simplifies parameter problems by concentrating the parameter into a single entry with zeros around it.


# Exercise 2

**Problem:** For
$$A=\begin{pmatrix}1&2&-1\\0&3&4\\2&1&5\end{pmatrix}$$
compute $\det A$ using Sarrus' rule. Then perform one simple check using a chosen property of the determinant.

---

## Relevant theorem / definition

Sarrus' rule for a $3 \times 3$ matrix evaluates the determinant as the sum of three downward diagonal products minus three upward diagonal products:
$$
\det(A) = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}
$$

---

## Solution

Given:
$$
A = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 4 \\ 2 & 1 & 5 \end{pmatrix}
$$

Computation using Sarrus' rule:
- Positive diagonals:
  $$
  1 \cdot 3 \cdot 5 = 15
  $$
  $$
  2 \cdot 4 \cdot 2 = 16
  $$
  $$
  (-1) \cdot 0 \cdot 1 = 0
  $$
  Sum of positive terms: $15 + 16 + 0 = 31$.

- Negative diagonals:
  $$
  (-1) \cdot 3 \cdot 2 = -6
  $$
  $$
  1 \cdot 4 \cdot 1 = 4
  $$
  $$
  2 \cdot 0 \cdot 5 = 0
  $$
  Sum of negative terms: $(-6) + 4 + 0 = -2$.

Combining terms:
$$
\det A = 31 - (-2) = 31 + 2 = 33
$$

Check using cofactor expansion along Column 1 (which contains a zero):
$$
\begin{align}
\det A &= 1 \cdot \begin{vmatrix} 3 & 4 \\ 1 & 5 \end{vmatrix} - 0 \cdot \begin{vmatrix} 2 & -1 \\ 1 & 5 \end{vmatrix} + 2 \cdot \begin{vmatrix} 2 & -1 \\ 3 & 4 \end{vmatrix} \\
&= 1(3 \cdot 5 - 4 \cdot 1) + 2(2 \cdot 4 - (-1) \cdot 3) \\
&= 1(15 - 4) + 2(8 + 3) \\
&= 11 + 2(11) = 11 + 22 = 33
\end{align}
$$

Both methods give $\det A = 33$.

---

## Result

$$
\det A = 33
$$

---

## Verification

**Pass 1 — Algebraic check:** Row reduction check: $R_3 \leftarrow R_3 - 2R_1$ gives third row $(0, -3, 7)$. Adding $R_2$ to $R_3$ gives $(0, 0, 11)$. The resulting triangular matrix has diagonal entries $1, 3, 11$, with product $1 \cdot 3 \cdot 11 = 33$.

**Pass 2 — Numerical check:** Expanding along row 2: $-0 + 3(1 \cdot 5 - (-1) \cdot 2) - 4(1 \cdot 1 - 2 \cdot 2) = 3(5 + 2) - 4(1 - 4) = 3(7) - 4(-3) = 21 + 12 = 33$.

**Pass 3 — Consistency check:** The determinant is an integer because all matrix entries are integers; sign and parity are consistent across all three evaluation paths.

---

## Exam tip

Sarrus' rule only applies to $3 \times 3$ matrices — never attempt to use it on $4 \times 4$ or larger matrices.


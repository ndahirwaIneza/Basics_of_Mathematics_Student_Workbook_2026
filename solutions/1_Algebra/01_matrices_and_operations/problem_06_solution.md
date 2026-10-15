# Exercise 6

**Problem:** For
$$A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix},\qquad B=\begin{pmatrix}1&0\\2&1\\-1&3\end{pmatrix}$$
compute $A^T$, $B^T$, and $AB$. Then verify in this example that
$$(AB)^T=B^TA^T.$$

---

## Relevant theorem / definition

The transpose of $M \in \mathbb{R}^{m \times n}$ is $M^T \in \mathbb{R}^{n \times m}$ defined by $(M^T)_{ij} = M_{ji}$. For compatible matrices $A$ and $B$, transposition reverses the order of factors:
$$
(AB)^T = B^T A^T
$$

---

## Solution

Computation of $A^T$:
Matrix $A$ has size $2 \times 3$, so $A^T$ has size $3 \times 2$:
$$
A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}
$$

Computation of $B^T$:
Matrix $B$ has size $3 \times 2$, so $B^T$ has size $2 \times 3$:
$$
B^T = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{pmatrix}
$$

Computation of $AB$:
Dimension check: $(2 \times 3) \times (3 \times 2) = 2 \times 2$:
$$
\begin{align}
AB &= \begin{pmatrix} 1(1) + 2(2) + 3(-1) & 1(0) + 2(1) + 3(3) \\ 4(1) + 5(2) + 6(-1) & 4(0) + 5(1) + 6(3) \end{pmatrix} \\
&= \begin{pmatrix} 1 + 4 - 3 & 0 + 2 + 9 \\ 4 + 10 - 6 & 0 + 5 + 18 \end{pmatrix} \\
&= \begin{pmatrix} 2 & 11 \\ 8 & 23 \end{pmatrix}
\end{align}
$$

Transpose of $AB$:
$$
(AB)^T = \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix}
$$

Computation of $B^T A^T$:
Dimension check: $(2 \times 3) \times (3 \times 2) = 2 \times 2$:
$$
\begin{align}
B^T A^T &= \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix} \\
&= \begin{pmatrix} 1(1) + 2(2) + (-1)(3) & 1(4) + 2(5) + (-1)(6) \\ 0(1) + 1(2) + 3(3) & 0(4) + 1(5) + 3(6) \end{pmatrix} \\
&= \begin{pmatrix} 1 + 4 - 3 & 4 + 10 - 6 \\ 0 + 2 + 9 & 0 + 5 + 18 \end{pmatrix} \\
&= \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix}
\end{align}
$$

Comparing the two matrices:
$$
(AB)^T = \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix} = B^T A^T
$$

The identity $(AB)^T = B^T A^T$ is confirmed.

---

## Result

$$
A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}, \qquad B^T = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{pmatrix}, \qquad AB = \begin{pmatrix} 2 & 11 \\ 8 & 23 \end{pmatrix}
$$

$$
(AB)^T = B^T A^T = \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** $((AB)^T)_{ij} = (AB)_{ji} = \sum_k A_{jk} B_{ki} = \sum_k (B^T)_{ik} (A^T)_{kj} = (B^T A^T)_{ij}$. The entrywise derivation holds for all $i, j$.

**Pass 2 — Numerical check:** Entry $(1,2)$ of $(AB)^T$ is entry $(2,1)$ of $AB$, which is 8. In $B^T A^T$, entry $(1,2)$ is the product of row 1 of $B^T$ and column 2 of $A^T$: $1(4) + 2(5) - 1(6) = 4 + 10 - 6 = 8$. They match.

**Pass 3 — Consistency check:** Dimension check: $A^T B^T$ would be $(3 \times 2)(2 \times 3) = 3 \times 3$, which does not equal the $2 \times 2$ size of $(AB)^T$. This reinforces why factors must reverse order: $B^T A^T$ is $2 \times 2$.

---

## Exam tip

Remember the order reversal in transpose: $(AB)^T = B^T A^T$, not $A^T B^T$.


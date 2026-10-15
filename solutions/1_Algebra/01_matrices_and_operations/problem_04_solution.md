# Exercise 4

**Problem:** For
$$A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}2&0\\3&1\end{pmatrix}$$
compute $AB$ and $BA$. Is $AB=BA$? Use this example to explain what noncommutativity of matrix multiplication means.

---

## Relevant theorem / definition

For $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$, the entry $(AB)_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$. In general, matrix multiplication is not commutative: $AB \neq BA$, even when both matrices are square and of the same size.

---

## Solution

Dimension check: Both $A$ and $B$ are $2 \times 2$, so both $AB$ and $BA$ are defined and are of size $2 \times 2$.

Computation of $AB$:
$$
AB = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 3 & 1 \end{pmatrix} = \begin{pmatrix} 1(2) + 2(3) & 1(0) + 2(1) \\ 0(2) + 1(3) & 0(0) + 1(1) \end{pmatrix} = \begin{pmatrix} 2+6 & 0+2 \\ 0+3 & 0+1 \end{pmatrix} = \begin{pmatrix} 8 & 2 \\ 3 & 1 \end{pmatrix}
$$

Computation of $BA$:
$$
BA = \begin{pmatrix} 2 & 0 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2(1) + 0(0) & 2(2) + 0(1) \\ 3(1) + 1(0) & 3(2) + 1(1) \end{pmatrix} = \begin{pmatrix} 2+0 & 4+0 \\ 3+0 & 6+1 \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 3 & 7 \end{pmatrix}
$$

Comparison:
$$
AB = \begin{pmatrix} 8 & 2 \\ 3 & 1 \end{pmatrix} \neq \begin{pmatrix} 2 & 4 \\ 3 & 7 \end{pmatrix} = BA
$$

Meaning of noncommutativity:
Noncommutativity means that the order of matrix factors matters. Applying the linear transformation $B$ first and then $A$ (represented by $AB$) does not yield the same transformation as applying $A$ first and then $B$ (represented by $BA$).

---

## Result

$$
AB = \begin{pmatrix} 8 & 2 \\ 3 & 1 \end{pmatrix}, \qquad BA = \begin{pmatrix} 2 & 4 \\ 3 & 7 \end{pmatrix}, \qquad AB \neq BA
$$

---

## Verification

**Pass 1 — Algebraic check:** Trace check: $\text{tr}(AB) = 8 + 1 = 9$; $\text{tr}(BA) = 2 + 7 = 9$. The identity $\text{tr}(AB) = \text{tr}(BA)$ holds.

**Pass 2 — Numerical check:** Determinant check: $\det(A) = 1(1) - 2(0) = 1$, $\det(B) = 2(1) - 0(3) = 2$. Then $\det(AB) = 8(1) - 2(3) = 2$, and $\det(BA) = 2(7) - 4(3) = 14 - 12 = 2$. Both match $\det(A)\det(B) = 2$.

**Pass 3 — Consistency check:** Entry $(1,1)$ of $AB$ is $1 \cdot 2 + 2 \cdot 3 = 8$, while entry $(1,1)$ of $BA$ is $2 \cdot 1 + 0 \cdot 0 = 2$, confirming that the products differ.

---

## Exam tip

Never assume $AB = BA$; when factoring matrix equations, never change factor order.


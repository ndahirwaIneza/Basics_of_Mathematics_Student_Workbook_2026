# Exercise 2

**Problem:** For
$$A=\begin{pmatrix}1&2\\-1&3\end{pmatrix},\qquad B=\begin{pmatrix}4&-2\\0&5\end{pmatrix}$$
compute
$$A+B,\qquad A-B,\qquad 3A-2B.$$
Explain why matrix addition is possible only for matrices of the same size.

---

## Relevant theorem / definition

For matrices $A, B \in \mathbb{R}^{m \times n}$ and scalars $c, d \in \mathbb{R}$, the linear combination $cA + dB$ is defined entrywise:
$$
(cA + dB)_{ij} = c a_{ij} + d b_{ij}
$$
for all $1 \le i \le m$ and $1 \le j \le n$.

---

## Solution

The matrices $A$ and $B$ are both of size $2 \times 2$.

Computation of $A+B$:
$$
A+B = \begin{pmatrix} 1+4 & 2+(-2) \\ -1+0 & 3+5 \end{pmatrix} = \begin{pmatrix} 5 & 0 \\ -1 & 8 \end{pmatrix}
$$

Computation of $A-B$:
$$
A-B = \begin{pmatrix} 1-4 & 2-(-2) \\ -1-0 & 3-5 \end{pmatrix} = \begin{pmatrix} -3 & 4 \\ -1 & -2 \end{pmatrix}
$$

Computation of $3A-2B$:
$$
3A = 3\begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 3 & 6 \\ -3 & 9 \end{pmatrix}
$$
$$
2B = 2\begin{pmatrix} 4 & -2 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 8 & -4 \\ 0 & 10 \end{pmatrix}
$$
$$
3A - 2B = \begin{pmatrix} 3-8 & 6-(-4) \\ -3-0 & 9-10 \end{pmatrix} = \begin{pmatrix} -5 & 10 \\ -3 & -1 \end{pmatrix}
$$

Explanation:
Matrix addition is defined componentwise by adding corresponding entries at index $(i,j)$. If two matrices have different dimensions, at least one entry in one matrix does not correspond to any entry in the other matrix, making the operation undefined.

---

## Result

$$
A+B = \begin{pmatrix} 5 & 0 \\ -1 & 8 \end{pmatrix}, \qquad A-B = \begin{pmatrix} -3 & 4 \\ -1 & -2 \end{pmatrix}, \qquad 3A-2B = \begin{pmatrix} -5 & 10 \\ -3 & -1 \end{pmatrix}
$$

---

<!-- ## Verification

**Pass 1 — Algebraic check:** Check $(A+B) + (A-B) = 2A$:
$$
\begin{pmatrix} 5 & 0 \\ -1 & 8 \end{pmatrix} + \begin{pmatrix} -3 & 4 \\ -1 & -2 \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ -2 & 6 \end{pmatrix} = 2\begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix} = 2A
$$

**Pass 2 — Numerical check:** Check the $(1,2)$ entry for $3A-2B$: $3(2) - 2(-2) = 6 + 4 = 10$, which matches entry $(1,2)$ of the result.

**Pass 3 — Consistency check:** Both inputs are $2 \times 2$; all resulting matrices are $2 \times 2$.

---

## Exam tip

Watch double negatives during entrywise subtraction, such as $2 - (-2) = 4$ and $6 - (-4) = 10$. -->


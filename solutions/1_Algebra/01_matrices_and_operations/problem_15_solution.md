# Exercise 15

**Problem:** Given
$$A=\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix},\quad B=\begin{pmatrix}1&0\\2&1\\-1&3\end{pmatrix},\quad C=\begin{pmatrix}2&1\\0&-1\end{pmatrix}.$$
Compute $(AB)C$ and $A(BC)$. Compare the results and the number of intermediate operations. Explain what associativity of matrix multiplication means in this example.

---

## Relevant theorem / definition

Matrix multiplication is associative: for any matrices $A, B, C$ with compatible sizes $(m \times n)$, $(n \times p)$, and $(p \times q)$,
$$
(AB)C = A(BC)
$$
While the final product is identical, the computational cost (number of scalar multiplications) depends on the order of evaluation: multiplying $(m \times n)$ by $(n \times p)$ takes $mnp$ multiplications.

---

## Solution

The matrix sizes are:
$A$ is $2 \times 3$, $B$ is $3 \times 2$, $C$ is $2 \times 2$.

Path 1: Evaluate $(AB)C$:
First compute $AB$ (size $(2 \times 3) \times (3 \times 2) = 2 \times 2$):
$$
\begin{align}
AB &= \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix} \\
&= \begin{pmatrix} 1(1) + 2(2) + 0(-1) & 1(0) + 2(1) + 0(3) \\ 0(1) + 1(2) + 1(-1) & 0(0) + 1(1) + 1(3) \end{pmatrix} \\
&= \begin{pmatrix} 1 + 4 + 0 & 0 + 2 + 0 \\ 0 + 2 - 1 & 0 + 1 + 3 \end{pmatrix} \\
&= \begin{pmatrix} 5 & 2 \\ 1 & 4 \end{pmatrix}
\end{align}
$$
Now compute $(AB)C$ (size $(2 \times 2) \times (2 \times 2) = 2 \times 2$):
$$
\begin{align}
(AB)C &= \begin{pmatrix} 5 & 2 \\ 1 & 4 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & -1 \end{pmatrix} \\
&= \begin{pmatrix} 5(2) + 2(0) & 5(1) + 2(-1) \\ 1(2) + 4(0) & 1(1) + 4(-1) \end{pmatrix} \\
&= \begin{pmatrix} 10 + 0 & 5 - 2 \\ 2 + 0 & 1 - 4 \end{pmatrix} \\
&= \begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix}
\end{align}
$$

Path 2: Evaluate $A(BC)$:
First compute $BC$ (size $(3 \times 2) \times (2 \times 2) = 3 \times 2$):
$$
\begin{align}
BC &= \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & -1 \end{pmatrix} \\
&= \begin{pmatrix} 1(2) + 0(0) & 1(1) + 0(-1) \\ 2(2) + 1(0) & 2(1) + 1(-1) \\ -1(2) + 3(0) & -1(1) + 3(-1) \end{pmatrix} \\
&= \begin{pmatrix} 2 & 1 \\ 4 & 1 \\ -2 & -4 \end{pmatrix}
\end{align}
$$
Now compute $A(BC)$ (size $(2 \times 3) \times (3 \times 2) = 2 \times 2$):
$$
\begin{align}
A(BC) &= \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 4 & 1 \\ -2 & -4 \end{pmatrix} \\
&= \begin{pmatrix} 1(2) + 2(4) + 0(-2) & 1(1) + 2(1) + 0(-4) \\ 0(2) + 1(4) + 1(-2) & 0(1) + 1(1) + 1(-4) \end{pmatrix} \\
&= \begin{pmatrix} 2 + 8 + 0 & 1 + 2 + 0 \\ 0 + 4 - 2 & 0 + 1 - 4 \end{pmatrix} \\
&= \begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix}
\end{align}
$$

Comparison of results:
$$
(AB)C = \begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix} = A(BC)
$$

Comparison of intermediate operations (scalar multiplications):
- In $(AB)C$:
  Computing $AB$ takes $2 \times 3 \times 2 = 12$ multiplications.
  Computing $(AB)C$ takes $2 \times 2 \times 2 = 8$ multiplications.
  Total: $12 + 8 = 20$ scalar multiplications.
- In $A(BC)$:
  Computing $BC$ takes $3 \times 2 \times 2 = 12$ multiplications.
  Computing $A(BC)$ takes $2 \times 3 \times 2 = 12$ multiplications.
  Total: $12 + 12 = 24$ scalar multiplications.

Explanation of associativity:
Associativity means that the grouping (parenthesization) of matrices in a product chain does not alter the resulting transformation or matrix entries. However, because intermediate matrices have different dimensions ($2 \times 2$ vs $3 \times 2$), evaluating $(AB)C$ requires fewer total arithmetic operations than $A(BC)$.

---

## Result

$$
(AB)C = A(BC) = \begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix}
$$

$$
\text{Operations: } (AB)C \text{ requires } 20 \text{ multiplications}, \quad A(BC) \text{ requires } 24 \text{ multiplications}
$$

---

## Verification

**Pass 1 — Algebraic check:** Trace check: $\text{tr}((AB)C) = 10 + (-3) = 7$. In $A(BC)$, the diagonal entries are 10 and $-3$, giving sum 7.

**Pass 2 — Numerical check:** Determinant of the result: $\det\begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix} = 10(-3) - 3(2) = -30 - 6 = -36$. Note $\det(AB) = 5(4) - 2(1) = 18$ and $\det(C) = 2(-1) - 1(0) = -2$. Then $\det((AB)C) = \det(AB)\det(C) = 18(-2) = -36$, which confirms the calculation.

**Pass 3 — Consistency check:** The dimensions of $A, B, C$ are $2 \times 3$, $3 \times 2$, and $2 \times 2$. Both parenthesizations collapse to outer dimensions $2 \times 2$.

---

## Exam tip

Matrix multiplication is associative ($(AB)C = A(BC)$) but NOT commutative ($AB \neq BA$); choosing the right parenthesization is the core idea of the matrix chain multiplication optimization problem.


# Exercise 7

**Problem:** For
$$A=\begin{pmatrix}2&1\\0&2\end{pmatrix}$$
compute
$$AI,\qquad IA,\qquad A+0,\qquad A^2,\qquad A^3.$$
Explain the roles of the matrices $I$ and $0$, and describe the pattern you observe in successive powers of $A$.

---

## Relevant theorem / definition

The identity matrix $I$ satisfies $AI = IA = A$ for any square matrix $A$, acting as the multiplicative identity. The zero matrix $0$ satisfies $A + 0 = A$, acting as the additive identity. Matrix powers are defined by $A^1 = A$ and $A^{k+1} = A^k A$.

---

## Solution

The identity and zero matrices of size $2 \times 2$ are:
$$
I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad 0 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}
$$

Multiplication by the identity matrix:
$$
AI = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2(1)+1(0) & 2(0)+1(1) \\ 0(1)+2(0) & 0(0)+2(1) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = A
$$
$$
IA = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1(2)+0(0) & 1(1)+0(2) \\ 0(2)+1(0) & 0(1)+1(2) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = A
$$

Addition with the zero matrix:
$$
A + 0 = \begin{pmatrix} 2+0 & 1+0 \\ 0+0 & 2+0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = A
$$

Computation of $A^2$:
$$
A^2 = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 2(2)+1(0) & 2(1)+1(2) \\ 0(2)+2(0) & 0(1)+2(2) \end{pmatrix} = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix}
$$

Computation of $A^3$:
$$
A^3 = A^2 A = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 4(2)+4(0) & 4(1)+4(2) \\ 0(2)+4(0) & 0(1)+4(2) \end{pmatrix} = \begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix}
$$

Roles of $I$ and $0$:
The matrix $I$ is the neutral element for matrix multiplication, meaning multiplication by $I$ from the left or right leaves any matrix unchanged. The matrix $0$ is the neutral element for matrix addition, meaning adding $0$ leaves any matrix unchanged.

Pattern observed in powers of $A$:
Decompose $A = 2I + N$ where $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. Note that $N^2 = 0$.
By the binomial theorem (since $2I$ and $N$ commute):
$$
A^n = (2I + N)^n = (2I)^n + n(2I)^{n-1}N = 2^n I + n 2^{n-1} N = \begin{pmatrix} 2^n & n 2^{n-1} \\ 0 & 2^n \end{pmatrix}
$$
- For $n=1$: $\begin{pmatrix} 2^1 & 1 \cdot 2^0 \\ 0 & 2^1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.
- For $n=2$: $\begin{pmatrix} 2^2 & 2 \cdot 2^1 \\ 0 & 2^2 \end{pmatrix} = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix}$.
- For $n=3$: $\begin{pmatrix} 2^3 & 3 \cdot 2^2 \\ 0 & 2^3 \end{pmatrix} = \begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix}$.
The main diagonal entries are always $2^n$, the bottom-left entry is always $0$, and the top-right entry is $n 2^{n-1}$.

---

## Result

$$
AI = IA = A+0 = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}, \qquad A^2 = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix}, \qquad A^3 = \begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix}
$$

$$
A^n = \begin{pmatrix} 2^n & n 2^{n-1} \\ 0 & 2^n \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Trace and determinant check for $A^2$: $\det(A) = 4 \implies \det(A^2) = 16$. From $A^2 = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix}$, $\det(A^2) = 4(4) - 0 = 16$, which confirms the calculation.

**Pass 2 — Numerical check:** For $n=3$, formula gives $\det(A^3) = \det(A)^3 = 4^3 = 64$. From matrix $A^3$, $8 \cdot 8 - 0 = 64$. The top-right entry for $n=3$ is $3 \cdot 2^2 = 12$, matching computed $A^3$.

**Pass 3 — Consistency check:** For an upper triangular matrix, any power remains upper triangular with diagonal entries equal to the powers of the corresponding diagonal entries: $2^1, 2^2, 2^3$.

---

## Exam tip

Matrices of the form $\lambda I + N$ with $N^2 = 0$ (Jordan blocks) can be raised to power $n$ directly using the two-term binomial expansion.


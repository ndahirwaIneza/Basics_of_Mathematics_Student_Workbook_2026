# Exercise 12

**Problem:** Let
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix}.$$
Compute $A^2$, $A^3$, and $A^4$, and use them to formulate a conjecture for $A^n$. Then do not stop after checking one more case: assume the formula is true for $n$, multiply by $A$, and explain why you obtain exactly the formula for $n+1$.

---

## Relevant theorem / definition

Mathematical induction: to prove a statement $P(n)$ holds for all integers $n \ge 1$, prove:
1. Base case: $P(1)$ is true.
2. Inductive step: assuming $P(n)$ is true (the induction hypothesis), prove that $P(n+1)$ must also be true.

---

## Solution

1. Computation of initial powers:
   $$
   A^2 = A A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(1)+1(0) & 1(1)+1(1) \\ 0(1)+1(0) & 0(1)+1(1) \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}
   $$
   $$
   A^3 = A^2 A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(1)+2(0) & 1(1)+2(1) \\ 0(1)+1(0) & 0(1)+1(1) \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}
   $$
   $$
   A^4 = A^3 A = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(1)+3(0) & 1(1)+3(1) \\ 0(1)+1(0) & 0(1)+1(1) \end{pmatrix} = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}
   $$

2. Conjecture:
   For every integer $n \ge 1$:
   $$
   A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}
   $$

3. Inductive proof:
   - Base case: For $n = 1$, $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = A^1$, which is true.
   - Inductive step: Assume the formula holds for $n$, that is, $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$.
   Compute $A^{n+1} = A^n A$:
   $$
   \begin{align}
   A^{n+1} &= \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \\
   &= \begin{pmatrix} 1(1) + n(0) & 1(1) + n(1) \\ 0(1) + 1(0) & 0(1) + 1(1) \end{pmatrix} \\
   &= \begin{pmatrix} 1 & n+1 \\ 0 & 1 \end{pmatrix}
   \end{align}
   $$
   The product gives $1$ on the main diagonal, $0$ in position $(2,1)$, and $1 + n = n+1$ in position $(1,2)$. This matches the statement for $n+1$, completing the proof by induction for all $n \ge 1$.

---

## Result

$$
A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \qquad A^3 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}, \qquad A^4 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}
$$

$$
A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix} \quad \text{for all } n \ge 1
$$

---

## Verification

**Pass 1 — Algebraic check:** Decompose $A = I + N$ with $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. Note $N^2 = 0$. Since $I$ and $N$ commute, $A^n = (I + N)^n = I^n + n I^{n-1} N + \binom{n}{2} N^2 + \cdots = I + nN = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$.

**Pass 2 — Numerical check:** For $n = 5$: $A^5 = A^4 A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 5 \\ 0 & 1 \end{pmatrix}$, which matches the formula with $n = 5$.

**Pass 3 — Consistency check:** Determinant check: $\det(A) = 1$, so $\det(A^n) = (\det A)^n = 1^n = 1$. The formula gives $\det\begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix} = 1(1) - 0(n) = 1$ for all $n$.

---

## Exam tip

A shear matrix $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ raised to power $n$ simply multiplies the shear factor by $n$, giving $\begin{pmatrix} 1 & nk \\ 0 & 1 \end{pmatrix}$.


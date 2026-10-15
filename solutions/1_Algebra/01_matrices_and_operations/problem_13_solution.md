# Exercise 13

**Problem:** Let
$$F=\begin{pmatrix}1&1\\1&0\end{pmatrix}.$$
Compute $F^2$, $F^3$, $F^4$, and $F^5$. Compare the numbers obtained with the sequence
$$0,1,1,2,3,5,8,\ldots$$
and describe the relationship you observe. Then compute
$$F\begin{pmatrix}a\\b\end{pmatrix}$$
and explain how this multiplication performs one recurrence step: it creates the sum of two consecutive terms and keeps one of them for the next step.

---

## Relevant theorem / definition

The Fibonacci sequence is defined by $f_0 = 0, f_1 = 1$ and $f_{k+1} = f_k + f_{k-1}$ for $k \ge 1$. A linear recurrence of order 2 can be encoded in matrix form as:
$$
\begin{pmatrix} f_{k+1} \\ f_k \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} f_k \\ f_{k-1} \end{pmatrix}
$$

---

## Solution

1. Computation of powers of $F$:
   $$
   F^2 = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1(1)+1(1) & 1(1)+1(0) \\ 1(1)+0(1) & 1(1)+0(0) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}
   $$
   $$
   F^3 = F^2 F = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2(1)+1(1) & 2(1)+1(0) \\ 1(1)+1(1) & 1(1)+1(0) \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix}
   $$
   $$
   F^4 = F^3 F = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 3(1)+2(1) & 3(1)+2(0) \\ 2(1)+1(1) & 2(1)+1(0) \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}
   $$
   $$
   F^5 = F^4 F = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 5(1)+3(1) & 5(1)+3(0) \\ 3(1)+2(1) & 3(1)+2(0) \end{pmatrix} = \begin{pmatrix} 8 & 5 \\ 5 & 3 \end{pmatrix}
   $$

2. Comparison with the Fibonacci sequence:
   The sequence is $f_0=0, f_1=1, f_2=1, f_3=2, f_4=3, f_5=5, f_6=8, \ldots$
   Comparing the entries of $F^n$:
   - $F^1 = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} f_2 & f_1 \\ f_1 & f_0 \end{pmatrix}$
   - $F^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} f_3 & f_2 \\ f_2 & f_1 \end{pmatrix}$
   - $F^3 = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} f_4 & f_3 \\ f_3 & f_2 \end{pmatrix}$
   - $F^4 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} f_5 & f_4 \\ f_4 & f_3 \end{pmatrix}$
   - $F^5 = \begin{pmatrix} 8 & 5 \\ 5 & 3 \end{pmatrix} = \begin{pmatrix} f_6 & f_5 \\ f_5 & f_4 \end{pmatrix}$
   In general, $F^n = \begin{pmatrix} f_{n+1} & f_n \\ f_n & f_{n-1} \end{pmatrix}$.

3. Multiplication by an arbitrary vector:
   $$
   F \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} 1(a) + 1(b) \\ 1(a) + 0(b) \end{pmatrix} = \begin{pmatrix} a+b \\ a \end{pmatrix}
   $$
   Explanation:
   The first row computes $a+b$, generating the next term of the recurrence from the two preceding terms. The second row computes $a$, shifting the current term into the role of the older term for the subsequent step.

---

## Result

$$
F^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \quad F^3 = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix}, \quad F^4 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}, \quad F^5 = \begin{pmatrix} 8 & 5 \\ 5 & 3 \end{pmatrix}
$$

$$
F^n = \begin{pmatrix} f_{n+1} & f_n \\ f_n & f_{n-1} \end{pmatrix}, \qquad F \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} a+b \\ a \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Cassini's identity check: $\det(F) = 1(0) - 1(1) = -1$. Therefore $\det(F^n) = (\det F)^n = (-1)^n$. From the formula, $\det(F^n) = f_{n+1} f_{n-1} - f_n^2 = (-1)^n$. For $n=4$: $f_5 f_3 - f_4^2 = 5(2) - 3^2 = 10 - 9 = 1 = (-1)^4$. For $n=5$: $f_6 f_4 - f_5^2 = 8(3) - 5^2 = 24 - 25 = -1 = (-1)^5$.

**Pass 2 — Numerical check:** Testing the vector action with $a=f_5=5$ and $b=f_4=3$:
$$
F \begin{pmatrix} 5 \\ 3 \end{pmatrix} = \begin{pmatrix} 5+3 \\ 5 \end{pmatrix} = \begin{pmatrix} 8 \\ 5 \end{pmatrix} = \begin{pmatrix} f_6 \\ f_5 \end{pmatrix}
$$

**Pass 3 — Consistency check:** The matrix $F$ is symmetric, so all its powers $F^n$ must be symmetric: the $(1,2)$ entry equals the $(2,1)$ entry for every power computed ($1=1, 2=2, 3=3, 5=5$).

---

## Exam tip

The matrix formulation of a recurrence allows calculating the $n$-th term in $O(\log n)$ matrix multiplications via repeated squaring.


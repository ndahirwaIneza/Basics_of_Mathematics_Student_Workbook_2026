# Exercise 11

**Problem:** Given
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}a&b\\c&d\end{pmatrix}.$$
Find the conditions on $a,b,c,d$ under which $AB=BA$. Describe the general form of all such matrices $B$.

---

## Relevant theorem / definition

Two square matrices $A$ and $B$ commute if and only if their commutator $[A, B] = AB - BA = 0$, meaning $AB = BA$. The set of all matrices that commute with a given matrix $A$ forms a subspace known as the centralizer of $A$.

---

## Solution

Compute the product $AB$:
$$
AB = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 1(a) + 1(c) & 1(b) + 1(d) \\ 0(a) + 1(c) & 0(b) + 1(d) \end{pmatrix} = \begin{pmatrix} a+c & b+d \\ c & d \end{pmatrix}
$$

Compute the product $BA$:
$$
BA = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a(1) + b(0) & a(1) + b(1) \\ c(1) + d(0) & c(1) + d(1) \end{pmatrix} = \begin{pmatrix} a & a+b \\ c & c+d \end{pmatrix}
$$

Equate $AB = BA$ entry by entry:
$$
\begin{align}
(1,1): \quad a+c &= a \implies c = 0 \\
(1,2): \quad b+d &= a+b \implies d = a \\
(2,1): \quad c &= c \quad (\text{identically true}) \\
(2,2): \quad d &= c+d \implies c = 0
\end{align}
$$

Both $(1,1)$ and $(2,2)$ yield $c = 0$, while $(1,2)$ yields $d = a$. The parameter $b$ is unconstrained.

Thus, the necessary and sufficient conditions are:
$$
c = 0 \quad \text{and} \quad d = a, \quad \text{with } a, b \in \mathbb{R} \text{ arbitrary}
$$

General form of all commuting matrices $B$:
$$
B = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix} = a \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + b \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = a I + b (A - I)
$$

---

## Result

$$
c = 0, \qquad d = a
$$

$$
B = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}, \qquad a, b \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Check $AB - BA$ using the general form $B = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$:
$$
AB = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} a & b \\ 0 & a \end{pmatrix} = \begin{pmatrix} a & b+a \\ 0 & a \end{pmatrix}
$$
$$
BA = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a & a+b \\ 0 & a \end{pmatrix}
$$
Since $b+a = a+b$, $AB = BA$ identically for all $a, b \in \mathbb{R}$.

**Pass 2 — Numerical check:** Choose $a = 3, b = 5$:
$$
A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 3 & 5 \\ 0 & 3 \end{pmatrix}
$$
$$
AB = \begin{pmatrix} 3 & 8 \\ 0 & 3 \end{pmatrix}, \qquad BA = \begin{pmatrix} 3 & 8 \\ 0 & 3 \end{pmatrix}
$$
The products match.

**Pass 3 — Consistency check:** For any polynomial $p(x) = c_0 + c_1 x$, the matrix $p(A) = c_0 I + c_1 A$ always commutes with $A$. Here $B = (a-b)I + bA$, which is a degree $\le 1$ polynomial in $A$, matching the dimension of the centralizer of a non-derogatory $2 \times 2$ matrix.

---

## Exam tip

Matrices that commute with a Jordan block must be upper triangular with equal diagonal entries, expressing $B$ as a polynomial in $A$.


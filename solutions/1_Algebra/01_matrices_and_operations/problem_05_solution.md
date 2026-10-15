# Exercise 5

**Problem:** Let
$$A=\begin{pmatrix}2&-1\\1&3\end{pmatrix},\qquad x=\begin{pmatrix}4\\2\end{pmatrix}.$$
Compute $Ax$. Then express $Ax$ as a linear combination of the columns of $A$, with coefficients coming from the vector $x$.

---

## Relevant theorem / definition

For $A = \begin{pmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{pmatrix} \in \mathbb{R}^{m \times n}$ and $x = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} \in \mathbb{R}^n$, the matrix-vector product $Ax$ is the linear combination of the columns of $A$ weighted by the components of $x$:
$$
Ax = \sum_{j=1}^n x_j \mathbf{a}_j = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \cdots + x_n \mathbf{a}_n
$$

---

## Solution

Dimension check: $A$ is $2 \times 2$ and $x$ is $2 \times 1$. The product is defined and has size $2 \times 1$.

Direct computation by row-column dot products:
$$
Ax = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 2 \end{pmatrix} = \begin{pmatrix} 2(4) + (-1)(2) \\ 1(4) + 3(2) \end{pmatrix} = \begin{pmatrix} 8 - 2 \\ 4 + 6 \end{pmatrix} = \begin{pmatrix} 6 \\ 10 \end{pmatrix}
$$

Expression as a linear combination of the columns of $A$:
The columns of $A$ are:
$$
\mathbf{a}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \qquad \mathbf{a}_2 = \begin{pmatrix} -1 \\ 3 \end{pmatrix}
$$
The components of $x$ are $x_1 = 4$ and $x_2 = 2$.
Forming the linear combination:
$$
x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 = 4 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 2 \begin{pmatrix} -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 8 \\ 4 \end{pmatrix} + \begin{pmatrix} -2 \\ 6 \end{pmatrix} = \begin{pmatrix} 8 - 2 \\ 4 + 6 \end{pmatrix} = \begin{pmatrix} 6 \\ 10 \end{pmatrix}
$$

Both approaches yield the same vector.

---

## Result

$$
Ax = \begin{pmatrix} 6 \\ 10 \end{pmatrix} = 4 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 2 \begin{pmatrix} -1 \\ 3 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** By linearity: $A(x_1 \mathbf{e}_1 + x_2 \mathbf{e}_2) = x_1 A\mathbf{e}_1 + x_2 A\mathbf{e}_2$. Since $A\mathbf{e}_1 = \mathbf{a}_1$ and $A\mathbf{e}_2 = \mathbf{a}_2$, the column combination identity is algebraically guaranteed.

**Pass 2 — Numerical check:** Compute row 1: $4(2) + 2(-1) = 8 - 2 = 6$. Compute row 2: $4(1) + 2(3) = 4 + 6 = 10$. Both match the entries of the result vector.

**Pass 3 — Consistency check:** Dimension check: $(2 \times 2) \times (2 \times 1) = 2 \times 1$. The output is a 2-dimensional column vector.

---

## Exam tip

Viewing $Ax$ as a linear combination of the columns of $A$ is the fundamental concept behind column spaces, span, and solving linear systems.


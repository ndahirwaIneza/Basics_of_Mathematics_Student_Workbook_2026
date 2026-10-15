# Exercise 3

**Problem:** The matrix sizes are
$$A_{2\times3},\qquad B_{3\times4},\qquad C_{4\times2},\qquad D_{2\times2}.$$
For the products
$$AB,\ BA,\ BC,\ CB,\ AC,\ CA,\ AD,\ DA$$
determine whether they are defined. If so, state the size of the result. Justify each decision using the dimension compatibility condition.

---

## Relevant theorem / definition

The matrix product $MN$ of matrices $M_{m \times n}$ and $N_{p \times q}$ is defined if and only if the number of columns in $M$ equals the number of rows in $N$ ($n = p$). When defined, the resulting matrix has size $m \times q$.

---

## Solution

1. $AB$: Matrix $A$ is $2 \times 3$ and $B$ is $3 \times 4$. The inner dimensions match ($3 = 3$). The product is defined and has size $2 \times 4$.

2. $BA$: Matrix $B$ is $3 \times 4$ and $A$ is $2 \times 3$. The inner dimensions do not match ($4 \neq 2$). The product is undefined.

3. $BC$: Matrix $B$ is $3 \times 4$ and $C$ is $4 \times 2$. The inner dimensions match ($4 = 4$). The product is defined and has size $3 \times 2$.

4. $CB$: Matrix $C$ is $4 \times 2$ and $B$ is $3 \times 4$. The inner dimensions do not match ($2 \neq 3$). The product is undefined.

5. $AC$: Matrix $A$ is $2 \times 3$ and $C$ is $4 \times 2$. The inner dimensions do not match ($3 \neq 4$). The product is undefined.

6. $CA$: Matrix $C$ is $4 \times 2$ and $A$ is $2 \times 3$. The inner dimensions match ($2 = 2$). The product is defined and has size $4 \times 3$.

7. $AD$: Matrix $A$ is $2 \times 3$ and $D$ is $2 \times 2$. The inner dimensions do not match ($3 \neq 2$). The product is undefined.

8. $DA$: Matrix $D$ is $2 \times 2$ and $A$ is $2 \times 3$. The inner dimensions match ($2 = 2$). The product is defined and has size $2 \times 3$.

---

## Result

$$
\begin{align}
AB &: \text{defined, size } 2 \times 4 \\
BA &: \text{undefined} \\
BC &: \text{defined, size } 3 \times 2 \\
CB &: \text{undefined} \\
AC &: \text{undefined} \\
CA &: \text{defined, size } 4 \times 3 \\
AD &: \text{undefined} \\
DA &: \text{defined, size } 2 \times 3
\end{align}
$$

---

## Verification

**Pass 1 — Algebraic check:** Dimension rule check: $(m \times k)(k \times p) = m \times p$. Four products have inner dimensions matching: $AB$ ($3=3$), $BC$ ($4=4$), $CA$ ($2=2$), and $DA$ ($2=2$).

**Pass 2 — Numerical check:** Testing $D_{2\times2} A_{2\times3}$: Row 1 of $D$ has 2 elements; each column of $A$ has 2 elements. The dot product of a 2-vector and a 2-vector is well-defined, yielding a row of 3 elements. Two rows give size $2 \times 3$.

**Pass 3 — Consistency check:** For non-square matrices, if $MN$ is defined, $NM$ is not necessarily defined. Here, $AB$ is defined ($2 \times 4$), but $BA$ is undefined because $4 \neq 2$.

---

## Exam tip

Write dimensions as $(m \times \mathbf{n})(\mathbf{n} \times p) = m \times p$ and circle the inner pair first before calculating anything.


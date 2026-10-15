# Exercise 1

**Problem:** Given
$$A=\begin{pmatrix}2&-1&3\\0&4&5\end{pmatrix},\qquad B=\begin{pmatrix}1&0\\-2&3\\4&1\end{pmatrix}.$$

1. State the sizes of matrices $A$ and $B$.
2. Read off the entries $a_{12}$, $a_{23}$, $b_{21}$, and $b_{32}$.
3. Write the second row of $A$ and the first column of $B$ as vectors.

---

## Relevant theorem / definition

A matrix with $m$ rows and $n$ columns has size $m \times n$. The entry at the intersection of row $i$ and column $j$ is denoted by $a_{ij}$. The $i$-th row is an $n$-dimensional row vector, and the $j$-th column is an $m$-dimensional column vector.

---

## Solution

1. Matrix sizes:
   Matrix $A$ has 2 rows and 3 columns, so its size is $2 \times 3$.
   Matrix $B$ has 3 rows and 2 columns, so its size is $3 \times 2$.

2. Matrix entries:
   The entry $a_{12}$ is in row 1, column 2 of $A$:
   $$
   a_{12} = -1
   $$
   The entry $a_{23}$ is in row 2, column 3 of $A$:
   $$
   a_{23} = 5
   $$
   The entry $b_{21}$ is in row 2, column 1 of $B$:
   $$
   b_{21} = -2
   $$
   The entry $b_{32}$ is in row 3, column 2 of $B$:
   $$
   b_{32} = 1
   $$

3. Row and column vectors:
   The second row of $A$ is:
   $$
   \mathbf{r}_2(A) = \begin{pmatrix} 0 & 4 & 5 \end{pmatrix}
   $$
   The first column of $B$ is:
   $$
   \mathbf{c}_1(B) = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}
   $$

---

## Result

$$
\text{size}(A) = 2 \times 3, \quad \text{size}(B) = 3 \times 2
$$

$$
a_{12} = -1, \quad a_{23} = 5, \quad b_{21} = -2, \quad b_{32} = 1
$$

$$
\mathbf{r}_2(A) = \begin{pmatrix} 0 & 4 & 5 \end{pmatrix}, \quad \mathbf{c}_1(B) = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** The total number of entries in $A$ is $2 \cdot 3 = 6$, and in $B$ is $3 \cdot 2 = 6$, matching the number of explicitly listed values in each array.

**Pass 2 — Numerical check:** Re-locating entries by coordinate pairs: $A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix} = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 4 & 5 \end{pmatrix}$ confirms $a_{12}=-1$ and $a_{23}=5$. Similarly for $B$, $b_{21}=-2$ and $b_{32}=1$.

**Pass 3 — Consistency check:** The vector $\mathbf{r}_2(A)$ has length 3, matching the column count of $A$. The vector $\mathbf{c}_1(B)$ has length 3, matching the row count of $B$.

---

## Exam tip

Always read indices as $(row, column)$ — row comes first, column comes second.


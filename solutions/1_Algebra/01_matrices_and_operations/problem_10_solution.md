# Exercise 10

**Problem:** Given
$$A=\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix},\qquad B=\begin{pmatrix}1&2\\-1&0\\3&1\end{pmatrix}.$$
Denote the columns of $B$ by $b_1,b_2$.

1. Compute $Ab_1$ and $Ab_2$.
2. Compute the matrix $AB$.
3. Compare the results and explain why the columns of $AB$ are exactly the vectors $Ab_1$ and $Ab_2$.

---

## Relevant theorem / definition

For any matrix $A$ and matrix $B = \begin{pmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \cdots & \mathbf{b}_p \end{pmatrix}$, the columns of the product matrix $AB$ are the products of $A$ with each column of $B$:
$$
AB = \begin{pmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & \cdots & A\mathbf{b}_p \end{pmatrix}
$$

---

## Solution

The columns of $B$ are:
$$
b_1 = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}, \qquad b_2 = \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}
$$

1. Computation of $Ab_1$ and $Ab_2$:
   $$
   Ab_1 = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 1(1) + 2(-1) + 0(3) \\ 0(1) + 1(-1) + 1(3) \end{pmatrix} = \begin{pmatrix} 1 - 2 + 0 \\ 0 - 1 + 3 \end{pmatrix} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}
   $$
   $$
   Ab_2 = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1(2) + 2(0) + 0(1) \\ 0(2) + 1(0) + 1(1) \end{pmatrix} = \begin{pmatrix} 2 + 0 + 0 \\ 0 + 0 + 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}
   $$

2. Computation of $AB$:
   Dimension check: $(2 \times 3) \times (3 \times 2) = 2 \times 2$:
   $$
   \begin{align}
   AB &= \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ -1 & 0 \\ 3 & 1 \end{pmatrix} \\
   &= \begin{pmatrix} 1(1)+2(-1)+0(3) & 1(2)+2(0)+0(1) \\ 0(1)+1(-1)+1(3) & 0(2)+1(0)+1(1) \end{pmatrix} \\
   &= \begin{pmatrix} -1 & 2 \\ 2 & 1 \end{pmatrix}
   \end{align}
   $$

3. Comparison and explanation:
   Comparing the columns of $AB$ with the computed vectors:
   - First column of $AB$ is $\begin{pmatrix} -1 \\ 2 \end{pmatrix} = Ab_1$.
   - Second column of $AB$ is $\begin{pmatrix} 2 \\ 1 \end{pmatrix} = Ab_2$.
   
   Explanation: By definition of matrix multiplication, entry $(AB)_{ij} = \sum_k a_{ik} b_{kj}$. For a fixed column $j$, the entire $j$-th column of $AB$ has entries $\sum_k a_{ik} (b_j)_k$, which is the definition of the matrix-vector product $A b_j$. Hence, $AB$ acts as a simultaneous collection of individual matrix-vector multiplications on each column of $B$.

---

## Result

$$
Ab_1 = \begin{pmatrix} -1 \\ 2 \end{pmatrix}, \qquad Ab_2 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}
$$

$$
AB = \begin{pmatrix} -1 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} Ab_1 & Ab_2 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** By block multiplication: $A \begin{pmatrix} b_1 & b_2 \end{pmatrix} = \begin{pmatrix} A b_1 & A b_2 \end{pmatrix}$. This block identity holds for any partitioned matrix.

**Pass 2 — Numerical check:** Trace of $AB$ is $(-1) + 1 = 0$. Row 1 of $A$ dotted with col 1 of $B$: $1(1) + 2(-1) + 0 = -1$. Row 2 of $A$ dotted with col 2 of $B$: $0(2) + 1(0) + 1(1) = 1$. Trace is $(-1) + 1 = 0$, fully consistent.

**Pass 3 — Consistency check:** Matrix $A$ has 2 rows and $B$ has 2 columns. The product $AB$ must have size $2 \times 2$. Each column $Ab_j$ is a 2-vector, producing two columns of height 2.

---

## Exam tip

The column perspective of matrix multiplication, $AB = \begin{pmatrix} Ab_1 & Ab_2 & \cdots \end{pmatrix}$, allows computing matrix products one column at a time.


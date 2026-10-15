# Exercise 7

**Problem:** Do not solve all of the following systems completely. For each situation, choose the method that best uses its structure and justify your choice:

1. one system with a triangular coefficient matrix
   $$\begin{cases}2x-y=3,\\4y=8;\end{cases}$$
2. three systems $Ax=b_i$ with the same invertible matrix $A$, when $A^{-1}$ is already known;
3. one $3\times3$ system for which the inverse matrix is not given and the goal is only to find one solution vector.

For case 1, carry out the chosen method completely. For cases 2 and 3, describe the plan and indicate which part of the computation would be reusable or unnecessary. Do not judge a method by its name alone — refer to the number of right-hand sides and the structure of the matrix.

---

## Relevant theorem / definition

The computational efficiency of solving $Ax = b$ depends on structure and repetition:
1. Triangular systems require only back-substitution ($O(n^2)$), bypassing elimination entirely.
2. Multiple right-hand sides ($k$ systems) with precomputed $A^{-1}$ require only $k$ matrix-vector multiplications ($k \cdot O(n^2)$), completely reusing $A^{-1}$.
3. Single general $n \times n$ system without precomputed $A^{-1}$ is solved via Gaussian elimination with back-substitution ($\frac{2}{3}n^3$ operations), which is three times faster than computing $A^{-1}$ ($\sim 2n^3$ operations).

---

## Solution

### Case 1: Triangular system
$$\begin{cases} 2x - y = 3 \\ 4y = 8 \end{cases}$$

- Chosen method: **Direct back-substitution**.
- Justification: The coefficient matrix $\begin{pmatrix} 2 & -1 \\ 0 & 4 \end{pmatrix}$ is already in upper triangular form. Gaussian elimination would do nothing, and computing the inverse would introduce unnecessary steps.
- Complete execution:
  - From equation 2:
    $$
    4y = 8 \implies y = \frac{8}{4} = 2
    $$
  - Substitute $y = 2$ into equation 1:
    $$
    2x - 2 = 3 \implies 2x = 5 \implies x = \frac{5}{2}
    $$
  - Result: $(x, y) = \left(\frac{5}{2}, 2\right)$.

---

### Case 2: Three systems $Ax = b_i$ with known $A^{-1}$

- Chosen method: **Matrix-vector multiplication: $\mathbf{x}_i = A^{-1} \mathbf{b}_i$ for $i \in \{1, 2, 3\}$**.
- Justification: Because $A^{-1}$ is already computed, each solution vector is obtained by multiplying $A^{-1}$ by $\mathbf{b}_i$.
- Plan and reusability:
  - The known matrix $A^{-1}$ is reused three times without recomputation.
  - Each solve requires only one matrix-vector dot product ($n^2$ operations per system).
  - Unnecessary work: Running Gaussian elimination three times on $[A \mid b_1]$, $[A \mid b_2]$, and $[A \mid b_3]$ would redundantly perform identical row operations on $A$ three times, wasting computation.

---

### Case 3: One $3 \times 3$ system without known $A^{-1}$

- Chosen method: **Gaussian elimination with back-substitution on the augmented matrix $[A \mid \mathbf{b}]$**.
- Justification: We only need to solve for a single vector $\mathbf{b}$, and $A^{-1}$ is not given.
- Plan and computational economy:
  - Plan: Transform $[A \mid \mathbf{b}]$ to upper triangular echelon form $[U \mid \mathbf{c}]$ using row operations, then solve for unknowns via back-substitution.
  - Unnecessary work: Inverting $A$ by solving $[A \mid I_3]$ requires finding all 9 entries of $A^{-1}$ (equivalent to solving 3 systems with unit basis vectors $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$). Computing $A^{-1}$ takes $\sim 2n^3$ operations, whereas Gaussian elimination on $[A \mid \mathbf{b}]$ takes only $\sim \frac{2}{3}n^3$ operations. Since there is only one right-hand side, constructing $A^{-1}$ is completely redundant.

---

## Result

$$
\text{Case 1: Direct back-substitution } \implies (x, y) = \left(\frac{5}{2}, 2\right)
$$

$$
\text{Case 2: Matrix-vector multiplication } \mathbf{x}_i = A^{-1}\mathbf{b}_i \implies A^{-1} \text{ is fully reused 3 times}
$$

$$
\text{Case 3: Gaussian elimination on } [A \mid \mathbf{b}] \implies \text{avoids unnecessary } O(n^3) \text{ inversion overhead}
$$

---

## Verification

**Pass 1 — Algebraic check:** Check Case 1 substitution: $2(5/2) - 2 = 5 - 2 = 3$, and $4(2) = 8$. Both equations hold.

**Pass 2 — Numerical check:** For $n = 3$:
- Operation count for Gaussian elimination: $\frac{2}{3}(27) + \frac{1}{2}(9) \approx 22$ operations.
- Operation count for matrix inversion + multiplication: $2(27) + 2(9) = 72$ operations.
Gaussian elimination is over 3 times faster for a single $3 \times 3$ system.

**Pass 3 — Consistency check:** For Case 2, if $k$ systems are solved: inversion takes $2n^3 + k n^2$, while $k$ eliminations take $k(\frac{2}{3}n^3)$. For large $k$, matrix-vector multiplication is asymptotically superior.

---

## Exam tip

Choose methods based on problem structure: triangular matrices $\to$ back-substitution; single system $\to$ Gaussian elimination; many systems with same $A \to$ inverse or LU decomposition.


# Exercise 6

**Problem:** Analyze, depending on the parameter $a$, the system
$$\begin{cases}x+y=2,\\ax+ay=4.\end{cases}$$

Among the three possibilities — exactly one solution, infinitely many solutions, no solution — determine which actually occur and for which values of $a$. If one type cannot occur, explain why.

---

## Relevant theorem / definition

For a linear system $Ax = b$:
1. A unique solution exists if and only if $\text{rank}(A) = \text{rank}([A \mid b]) = n$ (which for a square system requires $\det(A) \neq 0$).
2. Infinitely many solutions exist if $\text{rank}(A) = \text{rank}([A \mid b]) < n$.
3. No solution exists if $\text{rank}(A) < \text{rank}([A \mid b])$.

---

## Solution

The system is:
$$
\begin{cases}
x + y = 2 \\
ax + ay = 4
\end{cases}
$$

1. Set up the augmented matrix:
   $$
   \left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   a & a & 4
   \end{array}\right]
   $$

2. Perform row elimination:
   Apply $R_2 \leftarrow R_2 - a R_1$:
   $$
   R_2 - a R_1 = \left[\begin{array}{cc|c} a - a(1) & a - a(1) & 4 - a(2) \end{array}\right] = \left[\begin{array}{cc|c} 0 & 0 & 4 - 2a \end{array}\right]
   $$
   The echelon form is:
   $$
   \left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   0 & 0 & 4 - 2a
   \end{array}\right]
   $$

3. Case analysis on parameter $a$:
   - Case 1: $4 - 2a = 0 \implies 2a = 4 \implies a = 2$.
     The second row becomes:
     $$
     \left[\begin{array}{cc|c} 0 & 0 & 0 \end{array}\right]
     $$
     Here $\text{rank}(A) = \text{rank}([A \mid b]) = 1 < 2$. The system is consistent with $2 - 1 = 1$ free variable.
     Equation 2 becomes $2x + 2y = 4$, which is identical to equation 1 ($x + y = 2$).
     Thus, for $a = 2$, there are **infinitely many solutions**:
     $$
     \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2 - t \\ t \end{pmatrix}, \quad t \in \mathbb{R}
     $$

   - Case 2: $4 - 2a \neq 0 \implies a \neq 2$.
     The second row is $\left[\begin{array}{cc|c} 0 & 0 & 4 - 2a \end{array}\right]$ with $4 - 2a \neq 0$.
     This represents the equation:
     $$
     0x + 0y = 4 - 2a \neq 0 \iff 0 = 4 - 2a
     $$
     which is an impossible contradiction.
     Here $\text{rank}(A) = 1 < 2 = \text{rank}([A \mid b])$.
     Thus, for all $a \neq 2$, there is **no solution** (the system is inconsistent).

4. Explanation of why "exactly one solution" cannot occur:
   The determinant of the coefficient matrix $A = \begin{pmatrix} 1 & 1 \\ a & a \end{pmatrix}$ is:
   $$
   \det(A) = 1(a) - 1(a) = 0
   $$
   Because $\det(A) = 0$ for every real value of $a$, the matrix $A$ is singular for all $a \in \mathbb{R}$. The rows $\begin{pmatrix} 1 & 1 \end{pmatrix}$ and $\begin{pmatrix} a & a \end{pmatrix}$ are always linearly dependent ($R_2 = a R_1$), which bounds the rank of $A$ to $\text{rank}(A) \le 1 < 2$. Because the rank of the coefficient matrix never reaches the number of unknowns ($n = 2$), the system cannot have a unique solution for any value of $a$.

---

## Result

$$
a = 2 \implies \text{infinitely many solutions}
$$

$$
a \neq 2 \implies \text{no solution}
$$

$$
\text{"Exactly one solution" never occurs because } \det(A) = 0 \text{ for all } a \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** At $a = 0$: system is $x + y = 2$ and $0x + 0y = 4 \implies 0 = 4$, no solution. Consistent with $a \neq 2$.

**Pass 2 — Numerical check:** At $a = 2$: choose $x = 1, y = 1$: $1 + 1 = 2$ and $2(1) + 2(1) = 4$, consistent. Choose $x = 0, y = 2$: $0 + 2 = 2$ and $2(0) + 2(2) = 4$, consistent.

**Pass 3 — Consistency check:** For any $a$, the lines $x + y = 2$ and $a(x + y) = 4$ are parallel because both have normal vector $(1, 1)$. When $a = 2$, they are coincident; when $a \neq 2$, they are distinct parallel lines. Distinct parallel lines never intersect, and coincident lines intersect everywhere.

---

## Exam tip

Do not assume that all three theoretical outcomes must occur; check whether $\det(A)$ is identically zero for all values of the parameter first.


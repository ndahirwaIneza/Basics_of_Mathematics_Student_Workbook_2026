# Exercise 14

**Problem:** Compare the systems
$$\begin{cases}x+y=2,\\2x-y=1,\\3x=3\end{cases}$$
and
$$\begin{cases}x+y=2,\\2x-y=1,\\3x=3.1.\end{cases}$$
Check the consistency of each system and explain why a small change in one number can change the type of the system.

---

## Relevant theorem / definition

An overdetermined linear system ($m > n$, more equations than unknowns) is consistent if and only if all hyperplanes intersect at a common set of points, meaning $\text{rank}(A) = \text{rank}([A \mid b])$. If even a single equation shifts parallel to itself by an epsilon perturbation $\epsilon \neq 0$, the common intersection can vanish, turning a consistent system into an inconsistent one ($\text{rank}([A \mid b]) > \text{rank}(A)$).

---

## Solution

### 1. Analysis of the first system
$$
\begin{cases}
x + y = 2 \\
2x - y = 1 \\
3x = 3
\end{cases}
$$

Set up the augmented matrix:
$$
\left[\begin{array}{cc|c}
1 & 1 & 2 \\
2 & -1 & 1 \\
3 & 0 & 3
\end{array}\right]
$$
Perform row operations:
- $R_2 \leftarrow R_2 - 2R_1$: row 2 becomes $\begin{pmatrix} 0 & -3 & -3 \end{pmatrix}$.
- $R_3 \leftarrow R_3 - 3R_1$: row 3 becomes $\begin{pmatrix} 0 & -3 & -3 \end{pmatrix}$.
The matrix is:
$$
\left[\begin{array}{cc|c}
1 & 1 & 2 \\
0 & -3 & -3 \\
0 & -3 & -3
\end{array}\right]
$$
- $R_3 \leftarrow R_3 - R_2$: row 3 becomes $\begin{pmatrix} 0 & 0 & 0 \end{pmatrix}$.
The row echelon form is:
$$
\left[\begin{array}{cc|c}
1 & 1 & 2 \\
0 & -3 & -3 \\
0 & 0 & 0
\end{array}\right]
$$
Here $\text{rank}(A) = 2$ and $\text{rank}([A \mid b]) = 2$.
Since $\text{rank}(A) = \text{rank}([A \mid b]) = n = 2$, the system is **consistent** and has a **unique solution**:
- From row 2: $-3y = -3 \implies y = 1$.
- From row 1: $x + 1 = 2 \implies x = 1$.
The unique solution is $(x, y) = (1, 1)$.

---

### 2. Analysis of the second system
$$
\begin{cases}
x + y = 2 \\
2x - y = 1 \\
3x = 3.1
\end{cases}
$$

Set up the augmented matrix:
$$
\left[\begin{array}{cc|c}
1 & 1 & 2 \\
2 & -1 & 1 \\
3 & 0 & 3.1
\end{array}\right]
$$
Perform the same row operations:
- $R_2 \leftarrow R_2 - 2R_1$: row 2 becomes $\begin{pmatrix} 0 & -3 & -3 \end{pmatrix}$.
- $R_3 \leftarrow R_3 - 3R_1$: row 3 becomes $\begin{pmatrix} 0 & -3 & 3.1 - 6 \end{pmatrix} = \begin{pmatrix} 0 & -3 & -2.9 \end{pmatrix}$.
The matrix is:
$$
\left[\begin{array}{cc|c}
1 & 1 & 2 \\
0 & -3 & -3 \\
0 & -3 & -2.9
\end{array}\right]
$$
- $R_3 \leftarrow R_3 - R_2$: row 3 becomes:
  $$
  \begin{pmatrix} 0 & 0 & -2.9 - (-3) \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0.1 \end{pmatrix}
  $$
The row echelon form is:
$$
\left[\begin{array}{cc|c}
1 & 1 & 2 \\
0 & -3 & -3 \\
0 & 0 & 0.1
\end{array}\right]
$$
Row 3 represents the equation $0x + 0y = 0.1 \implies 0 = 0.1$, which is an impossible contradiction.
Here $\text{rank}(A) = 2 < 3 = \text{rank}([A \mid b])$.
Therefore, the second system is **inconsistent** (has **no solution**).

---

### 3. Explanation of why a small change alters the system type
Geometrically, each equation represents a straight line in the 2D plane:
- The first two equations $x + y = 2$ and $2x - y = 1$ intersect at the unique point $(1, 1)$.
- In the first system, the third line is $3x = 3 \implies x = 1$. This vertical line passes directly through the point $(1, 1)$. All three lines are concurrent (they meet at one common point), making the system consistent.
- In the second system, the third line is shifted by a small perturbation of $+0.1$ to $x = \frac{3.1}{3} \approx 1.0333$. Because the line is shifted horizontally, it no longer passes through $(1, 1)$. The three lines now form a small non-degenerate triangle whose pairwise intersections are three distinct points. Because there is no single point common to all three lines simultaneously, the system abruptly transitions from having a unique solution to having no solution.

---

## Result

$$
\text{System 1 is consistent with unique solution: } (x, y) = (1, 1)
$$

$$
\text{System 2 is inconsistent (no solution): } 0x + 0y = 0.1 \iff 0 = 0.1 \quad (\text{contradiction})
$$

---

## Verification

**Pass 1 — Algebraic check:** From the first two equations of System 2, $x = 1$ and $y = 1$. Substituting into the third equation gives $3(1) = 3 \neq 3.1$, algebraically proving inconsistency.

**Pass 2 — Numerical check:** For System 1: $1 + 1 = 2$, $2(1) - 1 = 1$, $3(1) = 3$. All three hold.

**Pass 3 — Consistency check:** For an overdetermined $3 \times 2$ system, consistency requires $\mathbf{b}$ to lie in the 2D column space $\text{col}(A) \subset \mathbb{R}^3$. For System 1, $\mathbf{b}_1 = \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} = 1 \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + 1 \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} \in \text{col}(A)$. For System 2, $\mathbf{b}_2 = \mathbf{b}_1 + \begin{pmatrix} 0 \\ 0 \\ 0.1 \end{pmatrix} \notin \text{col}(A)$.

---

## Exam tip

In overdetermined systems (more equations than unknowns), the system is consistent only if the additional equations pass exactly through the intersection of the primary equations; any deviation destroys consistency.


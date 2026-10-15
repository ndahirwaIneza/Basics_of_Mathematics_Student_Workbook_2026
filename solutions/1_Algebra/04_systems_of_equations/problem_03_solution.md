# Exercise 3

**Problem:** Solve or show that the system is inconsistent:
$$\begin{cases}x+2y=3,\\2x+4y=7.\end{cases}$$
Show how the contradiction appears in the matrix after elimination and interpret it in terms of equations.

---

## Relevant theorem / definition

Rouché–Capelli Theorem: A system of linear equations $Ax = b$ is consistent if and only if the rank of the coefficient matrix equals the rank of the augmented matrix:
$$
\text{rank}(A) = \text{rank}([A \mid b])
$$
If $\text{rank}(A) < \text{rank}([A \mid b])$, the row echelon form contains a row of the form $\left[\begin{array}{cc|c} 0 & 0 & c \end{array}\right]$ with $c \neq 0$, which represents the impossible contradiction $0 = c$, meaning the system has no solution.

---

## Solution

The given system is:
$$
\begin{cases}
x + 2y = 3 \\
2x + 4y = 7
\end{cases}
$$

1. Set up the augmented matrix:
   $$
   \left[\begin{array}{cc|c}
   1 & 2 & 3 \\
   2 & 4 & 7
   \end{array}\right]
   $$

2. Perform elimination to eliminate $x$ from Row 2:
   Apply $R_2 \leftarrow R_2 - 2R_1$:
   $$
   R_2 - 2R_1 = \left[\begin{array}{cc|c} 2 - 2(1) & 4 - 2(2) & 7 - 2(3) \end{array}\right] = \left[\begin{array}{cc|c} 0 & 0 & 1 \end{array}\right]
   $$
   The augmented matrix in row echelon form is:
   $$
   \left[\begin{array}{cc|c}
   1 & 2 & 3 \\
   0 & 0 & 1
   \end{array}\right]
   $$

3. Appearance of the contradiction in the matrix:
   The second row of the augmented matrix consists of zeros in the coefficient columns and a non-zero value ($1$) in the right-hand side column.

4. Interpretation in terms of equations:
   Translating the second row back into an algebraic equation:
   $$
   0 \cdot x + 0 \cdot y = 1 \implies 0 = 1
   $$
   Because $0 = 1$ is false for all real values of $x$ and $y$, no pair $(x, y)$ can satisfy both equations simultaneously.
   Geometrically, the two equations describe two straight lines in the plane:
   - Line 1: $y = -\frac{1}{2}x + \frac{3}{2}$
   - Line 2: $y = -\frac{2}{4}x + \frac{7}{4} = -\frac{1}{2}x + \frac{7}{4}$
   Both lines have the same slope ($m = -\frac{1}{2}$) but different $y$-intercepts ($\frac{3}{2} \neq \frac{7}{4}$). They are distinct parallel lines that never intersect.
   Therefore, the system is inconsistent (no solution).

---

## Result

$$
\text{No solution (inconsistent system)}
$$

$$
\left[\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 1 \end{array}\right] \implies 0x + 0y = 1 \iff 0 = 1 \quad (\text{contradiction})
$$

---

## Verification

**Pass 1 — Algebraic check:** Compare left-hand sides: $2x + 4y = 2(x + 2y)$. Substituting the first equation ($x + 2y = 3$) into the left-hand side of the second equation gives $2(3) = 6$. The second equation asserts $2x + 4y = 7$. Thus $6 = 7$, an algebraic impossibility.

**Pass 2 — Numerical check:** Determinant of coefficient matrix: $\det(A) = 1(4) - 2(2) = 0$. Since $\det(A) = 0$, the system either has infinitely many solutions or no solution. Because $7 \neq 2(3)$, the right-hand side does not lie in the column space of $A$, proving no solution.

**Pass 3 — Consistency check:** The rank of the coefficient matrix is $\text{rank}(A) = 1$, whereas the rank of the augmented matrix is $\text{rank}([A \mid b]) = 2$. Since $1 < 2$, Rouché–Capelli confirms inconsistency.

---

## Exam tip

A row of zeros followed by a non-zero right-hand side, $\left[\begin{array}{cc|c} 0 & 0 & c \end{array}\right]$ with $c \neq 0$, immediately proves the system has no solution.


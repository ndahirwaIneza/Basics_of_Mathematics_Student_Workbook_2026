# Exercise 15

**Problem:** For each of the following systems, perform only as much elimination as necessary to recognize its type:

1. $\begin{cases}x+y=2,\\x-y=0,\end{cases}$
2. $\begin{cases}x+y=2,\\2x+2y=4,\end{cases}$
3. $\begin{cases}x+y=2,\\2x+2y=5.\end{cases}$

For each, justify the classification: one solution, infinitely many solutions, or no solution.

---

## Relevant theorem / definition

Rouché–Capelli Classification for an $m \times n$ system:
1. Exactly one solution: $\text{rank}(A) = \text{rank}([A \mid b]) = n$.
2. Infinitely many solutions: $\text{rank}(A) = \text{rank}([A \mid b]) < n$.
3. No solution: $\text{rank}(A) < \text{rank}([A \mid b])$.

---

## Solution

### 1. System 1
$$
\begin{cases}
x + y = 2 \\
x - y = 0
\end{cases}
$$
Set up the augmented matrix and perform one elimination step ($R_2 \leftarrow R_2 - R_1$):
$$
\left[\begin{array}{cc|c} 1 & 1 & 2 \\ 1 & -1 & 0 \end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - R_1} \left[\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & -2 & -2 \end{array}\right]
$$
- Justification:
  There are two pivots (in column 1 and column 2).
  Therefore, $\text{rank}(A) = \text{rank}([A \mid b]) = 2 = n$.
  With full rank and no free variables, the system has **exactly one solution** (unique solution: $y = 1, x = 1$).

---

### 2. System 2
$$
\begin{cases}
x + y = 2 \\
2x + 2y = 4
\end{cases}
$$
Set up the augmented matrix and perform one elimination step ($R_2 \leftarrow R_2 - 2R_1$):
$$
\left[\begin{array}{cc|c} 1 & 1 & 2 \\ 2 & 2 & 4 \end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - 2R_1} \left[\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & 0 & 0 \end{array}\right]
$$
- Justification:
  The second row vanishes entirely into zeros.
  Therefore, $\text{rank}(A) = \text{rank}([A \mid b]) = 1 < n = 2$.
  The system is consistent with $2 - 1 = 1$ free variable ($y = t$), meaning the equations represent the same line and the system has **infinitely many solutions** ($(x, y) = (2 - t, t)$).

---

### 3. System 3
$$
\begin{cases}
x + y = 2 \\
2x + 2y = 5
\end{cases}
$$
Set up the augmented matrix and perform one elimination step ($R_2 \leftarrow R_2 - 2R_1$):
$$
\left[\begin{array}{cc|c} 1 & 1 & 2 \\ 2 & 2 & 5 \end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - 2R_1} \left[\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & 0 & 1 \end{array}\right]
$$
- Justification:
  Row 2 gives the contradictory statement $0x + 0y = 1 \implies 0 = 1$.
  Therefore, $\text{rank}(A) = 1 < 2 = \text{rank}([A \mid b])$.
  Because the augmented matrix has higher rank than the coefficient matrix, the equations represent distinct parallel lines that never intersect, so the system has **no solution**.

---

## Result

$$
\text{System 1: Exactly one solution} \quad (\text{rank}(A) = \text{rank}([A \mid b]) = 2)
$$

$$
\text{System 2: Infinitely many solutions} \quad (\text{rank}(A) = \text{rank}([A \mid b]) = 1 < 2)
$$

$$
\text{System 3: No solution} \quad (\text{rank}(A) = 1 < 2 = \text{rank}([A \mid b]))
$$

---

## Verification

**Pass 1 — Algebraic check:**
- System 1: $x + y = 2$ and $x - y = 0 \implies x = y \implies 2x = 2 \implies x = 1, y = 1$ (unique).
- System 2: Row 2 is $2 \times$ Row 1: $2(x + y) = 2(2) = 4$, redundant equation (infinitely many).
- System 3: Row 2 is $2(x + y) = 2(2) = 4 \neq 5$, contradiction $4 = 5$ (no solution).

**Pass 2 — Numerical check:**
- For System 1: $\det(A) = 1(-1) - 1(1) = -2 \neq 0 \implies$ unique solution.
- For System 2 & 3: $\det(A) = 1(2) - 1(2) = 0 \implies$ cannot have a unique solution; consistency depends on $b_2 = 2b_1$. For System 2, $4 = 2(2)$ (consistent); for System 3, $5 \neq 2(2)$ (inconsistent).

**Pass 3 — Consistency check:** The three systems cover the complete, mutually exclusive trichotomy of linear systems in $\mathbb{R}^2$: intersecting lines, coincident lines, and parallel lines.

---

## Exam tip

A single row elimination step $R_2 - c R_1$ instantly reveals the system type: two pivots $\to$ unique; zero row $\to$ infinitely many; contradiction row $[0 \; 0 \mid c]$ with $c \neq 0 \to$ no solution.


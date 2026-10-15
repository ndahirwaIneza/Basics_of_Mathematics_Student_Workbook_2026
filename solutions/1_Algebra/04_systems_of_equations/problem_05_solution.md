# Exercise 5

**Problem:** For the augmented matrix
$$\left[\begin{array}{ccc|c}1&2&-1&3\\0&1&2&1\\0&0&0&0\end{array}\right]$$
determine the number of solutions and write them in parametric form. Explain how you know how many variables may be chosen freely.

---

## Relevant theorem / definition

For a consistent system with augmented matrix in row echelon form, let $n$ be the number of unknowns and $r = \text{rank}(A)$ be the number of non-zero rows (pivots). The number of free variables is:
$$
k = n - r = n - \text{rank}(A)
$$
If $k > 0$, the system has infinitely many solutions parameterized by $k$ free variables.

---

## Solution

The given augmented matrix is:
$$
\left[\begin{array}{ccc|c}
1 & 2 & -1 & 3 \\
0 & 1 & 2 & 1 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

1. Determine the number of solutions:
   - The matrix is already in row echelon form.
   - The number of unknowns is $n = 3$ (corresponding to $x_1, x_2, x_3$).
   - The leading non-zero entries (pivots) are in row 1, column 1 (value $1$) and row 2, column 2 (value $1$).
   - The rank of the coefficient matrix is $r = 2$, and the rank of the augmented matrix is also $2$.
   - Since $\text{rank}(A) = \text{rank}([A \mid b]) = 2 < 3$, the system is consistent and has:
     $$
     \text{infinitely many solutions}
     $$

2. Determining the number of free variables:
   A variable is basic (leading) if its column contains a pivot, and free if its column does not contain a pivot.
   - Column 1 contains a pivot $\implies x_1$ is a basic variable.
   - Column 2 contains a pivot $\implies x_2$ is a basic variable.
   - Column 3 contains no pivot $\implies x_3$ is a free variable.
   The number of free variables is $n - r = 3 - 2 = 1$. Exactly 1 variable ($x_3$) may be chosen freely.

3. Parametric form of the solution:
   Set the free variable to a parameter: $x_3 = t \in \mathbb{R}$.
   - From Row 2:
     $$
     x_2 + 2x_3 = 1 \implies x_2 + 2t = 1 \implies x_2 = 1 - 2t
     $$
   - From Row 1:
     $$
     x_1 + 2x_2 - x_3 = 3
     $$
     Substitute the expressions for $x_2$ and $x_3$:
     $$
     x_1 + 2(1 - 2t) - t = 3 \implies x_1 + 2 - 4t - t = 3 \implies x_1 + 2 - 5t = 3 \implies x_1 = 1 + 5t
     $$

Vector parametric form:
$$
\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 + 5t \\ 1 - 2t \\ t \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} 5 \\ -2 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}
$$

---

## Result

$$
\text{Infinitely many solutions}
$$

$$
\text{Free variables: } 3 - 2 = 1 \text{ free variable } (x_3)
$$

$$
\mathbf{x} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} 5 \\ -2 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute the parametric solution into equation 1:
$$
x_1 + 2x_2 - x_3 = (1 + 5t) + 2(1 - 2t) - t = 1 + 5t + 2 - 4t - t = 3
$$
Substitute into equation 2:
$$
x_2 + 2x_3 = (1 - 2t) + 2t = 1
$$
Both equations are identically satisfied for all $t \in \mathbb{R}$.

**Pass 2 — Numerical check:** Plug in $t = 1$: $\mathbf{x} = (6, -1, 1)^T$.
$x_1 + 2x_2 - x_3 = 6 + 2(-1) - 1 = 6 - 2 - 1 = 3$.
$x_2 + 2x_3 = -1 + 2(1) = 1$.
Both equations hold.

**Pass 3 — Consistency check:** The direction vector $\mathbf{v} = (5, -2, 1)^T$ satisfies $A\mathbf{v} = \mathbf{0}$:
$\begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} 5 \\ -2 \\ 1 \end{pmatrix} = \begin{pmatrix} 5 - 4 - 1 \\ 0 - 2 + 2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$, confirming $\mathbf{v}$ spans the 1D null space.

---

## Exam tip

The number of free variables always equals the total number of columns minus the number of pivot columns in echelon form: $\text{free} = n - \text{rank}$.


# Presentation Notes — 04_systems_of_equations

## Topic summary

Systems of linear equations can be written compactly as $A\mathbf{x} = \mathbf{b}$ and solved systematically via Gaussian elimination on the augmented matrix $[A \mid \mathbf{b}]$. According to the Rouché–Capelli theorem, the structure of the row echelon form classifies every linear system into exactly one of three mutually exclusive outcomes: a unique solution when rank equals the number of variables, infinitely many solutions parameterized by free variables when rank is less than the number of variables, or no solution when a contradictory row $[0 \; \dots \; 0 \mid c]$ with $c \neq 0$ appears. Structuring solution methods consciously avoids unnecessary inverse computations and highlights redundant constraints.

---

## Exercise 1 — verbal script

**Key idea:** Translating a system of linear equations into the matrix-vector equation $Ax = b$.

**What to say:**
We convert the three given equations into the matrix form $Ax = b$. The coefficient matrix $A$ collects the coefficients of $x, y, z$ as rows: row 1 is $(2, -1, 1)$, row 2 is $(1, 3, -2)$, and row 3 is $(3, 1, 1)$. The vector of unknowns $\mathbf{x}$ is the column vector $(x, y, z)^T$, and the right-hand side vector $\mathbf{b}$ is $(4, 1, 7)^T$. Each row of $A$ corresponds to one equation because taking the dot product of row $i$ with $\mathbf{x}$ evaluates $\sum a_{ij} x_j$, which reconstructs the left-hand side of equation $i$. Setting this dot product equal to $b_i$ reproduces the equation exactly.

**Show on screen:** The matrix equation $\begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}$ with row-to-equation mappings.

**If asked to go deeper:** The mapping $\mathbf{x} \mapsto A\mathbf{x}$ defines a linear transformation from $\mathbb{R}^3$ to $\mathbb{R}^3$, where solving the system is equivalent to finding the pre-image of $\mathbf{b}$.

---

## Exercise 2 — verbal script

**Key idea:** Systematic Gaussian elimination to echelon form and back-substitution.

**What to say:**
We set up the augmented matrix and eliminate the first column by subtracting $2R_1$ from $R_2$ and $R_1$ from $R_3$. To keep calculations clean without fractions, we swap row 2 and row 3, giving a pivot of 1 in position $(2,2)$. We then eliminate position $(3,2)$ by adding $3R_2$ to $R_3$, which produces an upper triangular echelon form with $-7z = -21$. Dividing gives $z = 3$. We back-substitute into row 2 to obtain $y = 2$, and into row 1 to obtain $x = 1$. Finally, substituting $(1, 2, 3)$ into all three original equations confirms consistency.

**Show on screen:** The echelon form $\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & -2 & -4 \\ 0 & 0 & -7 & -21 \end{array}\right]$ and the back-substitution steps.

**If asked to go deeper:** Pivoting by swapping rows when a convenient integer pivot is available is an elementary form of partial pivoting, which prevents floating-point instability in numerical solvers.

---

## Exercise 3 — verbal script

**Key idea:** Recognizing inconsistency through an impossible row $[0 \; 0 \mid c]$.

**What to say:**
We write the augmented matrix and eliminate $x$ from the second row by subtracting $2R_1$ from $R_2$. The left-hand coefficients completely vanish to $(0, 0)$, while the right-hand side becomes $7 - 2(3) = 1$. Row 2 now states $0x + 0y = 1$, which is the impossible statement $0 = 1$. Geometrically, both equations describe lines with slope $-\frac{1}{2}$, but their distinct $y$-intercepts make them parallel lines that never meet. Because $\text{rank}(A) = 1 < 2 = \text{rank}([A \mid b])$, the system is inconsistent and has no solution.

**Show on screen:** The contradiction row $\left[\begin{array}{cc|c} 0 & 0 & 1 \end{array}\right]$ and the parallel lines geometry.

**If asked to go deeper:** In terms of vector spaces, the vector $\mathbf{b} = (3, 7)^T$ does not lie in the column space of $A$, which is the 1D line spanned by $(1, 2)^T$.

---

## Exercise 4 — verbal script

**Key idea:** Expressing infinitely many solutions in parametric form using free variables.

**What to say:**
During elimination, subtracting $2R_1$ from $R_2$ produces an entire row of zeros, and subtracting $R_1$ from $R_3$ yields $(0, -2, 0 \mid -2)$. Reordering rows gives leading pivots in columns 1 and 2, which correspond to variables $x$ and $y$. Because column 3 has no pivot, variable $z$ is free. Setting $z = t$, row 2 gives $y = 1$, and row 1 gives $x = 1 - t$. In parametric vector form, the solution is $(1, 1, 0)^T + t(-1, 0, 1)^T$. Testing with $t = 2$ gives the point $(-1, 1, 2)$, which satisfies all three original equations.

**Show on screen:** The vector parametric equation $\mathbf{x} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}$ and the test check for $t = 2$.

**If asked to go deeper:** The vector $(1, 1, 0)^T$ is a particular solution $\mathbf{x}_p$, while $(-1, 0, 1)^T$ spans the 1-dimensional null space $\text{null}(A)$ of the homogeneous problem.

---

## Exercise 5 — verbal script

**Key idea:** Reading ranks and the number of free variables directly from row echelon form.

**What to say:**
Inspecting the augmented matrix, it is already in row echelon form. The coefficient matrix has 2 non-zero rows, so its rank is 2. The augmented matrix also has rank 2, and since they match, the system is consistent. The number of unknowns is 3. By the dimension formula, the number of free variables equals the number of unknowns minus the rank, giving $3 - 2 = 1$ free variable. Columns 1 and 2 contain pivots, so $x_1$ and $x_2$ are basic, while column 3 has no pivot, making $x_3$ the free variable. Setting $x_3 = t$, back-substitution yields $x_2 = 1 - 2t$ and $x_1 = 1 + 5t$.

**Show on screen:** The pivot entries circled in columns 1 and 2, and the resulting parametric line equation.

**If asked to go deeper:** The solution space represents the intersection of two non-parallel planes in $\mathbb{R}^3$, which is always a 1-dimensional line.

---

## Exercise 6 — verbal script

**Key idea:** Parameter analysis and explaining why a unique solution can never occur.

**What to say:**
We apply $R_2 \leftarrow R_2 - a R_1$, which transforms row 2 into $(0, 0 \mid 4 - 2a)$. If $4 - 2a = 0$, meaning $a = 2$, row 2 becomes all zeros, the equations become identical, and we have infinitely many solutions. If $a \neq 2$, row 2 represents $0 = 4 - 2a \neq 0$, creating a contradiction, so there is no solution. Crucially, "exactly one solution" can never occur for any value of $a$. This is because the determinant of the coefficient matrix is $1(a) - 1(a) = 0$ for all $a$, meaning the rows of $A$ are always proportional and the rank can never reach 2.

**Show on screen:** The row $(0, 0 \mid 4 - 2a)$, highlighting the case $a = 2$ versus $a \neq 2$, and the identity $\det(A) = 0$.

**If asked to go deeper:** For every $a$, the normal vectors of both equations are parallel, meaning the two lines are either parallel and distinct or identical, never intersecting at a single point.

---

## Exercise 7 — verbal script

**Key idea:** Deliberate method selection based on matrix structure and repetition count.

**What to say:**
In case 1, the matrix is already upper triangular, so we use direct back-substitution: $4y = 8$ immediately gives $y = 2$, and substituting gives $x = \frac{5}{2}$, avoiding all elimination. In case 2, we have three systems with the same matrix and $A^{-1}$ is already known. We use matrix-vector multiplication $x_i = A^{-1} b_i$, reusing $A^{-1}$ three times and avoiding redundant eliminations. In case 3, we have a single $3 \times 3$ system without $A^{-1}$. We use Gaussian elimination on $[A \mid \mathbf{b}]$ because finding $A^{-1}$ requires solving for three columns ($\sim 2n^3$ operations), which is three times more work than eliminating one vector ($\sim \frac{2}{3}n^3$).

**Show on screen:** The three cases summarized with their chosen methods and computational operation counts.

**If asked to go deeper:** In industrial software, linear solvers automatically inspect sparsity and structure to switch between direct elimination, Cholesky, and iterative solvers.

---

## Exercise 8 — verbal script

**Key idea:** Structural invariance of Gaussian elimination across different right-hand sides.

**What to say:**
We solve both systems simultaneously by appending both right-hand vectors to the coefficient matrix. The row operations—swapping rows 1 and 2, then subtracting $2R_1$ from $R_2$—are identical for both systems. The left-hand block transforms into the exact same upper triangular matrix $\begin{pmatrix} 1 & -1 \\ 0 & 3 \end{pmatrix}$. This occurs because row operations depend strictly on eliminating coefficients in $A$. The right-hand sides simply undergo the corresponding arithmetic without influencing the operations. Back-substitution yields $(2, 1)$ for the first system and $\left(\frac{5}{3}, -\frac{7}{3}\right)$ for the second.

**Show on screen:** The simultaneous augmented matrix $\left[\begin{array}{cc|cc} 2 & 1 & 5 & 1 \\ 1 & -1 & 1 & 4 \end{array}\right]$ and the reduced form.

**If asked to go deeper:** This invariance of row operations is the foundation of the $LU$ decomposition, where the elimination steps are stored in a lower triangular matrix $L$ and applied to any new vector $\mathbf{b}$ in $O(n^2)$ time.

---

## Exercise 9 — verbal script

**Key idea:** Uniqueness of solution interpreted as the intersection of non-parallel lines.

**What to say:**
We solve the system by subtracting $2R_1$ from $R_2$, which gives $3y = 12$, so $y = 4$. Back-substitution into the first equation yields $x = 6$. Geometrically, the two equations define lines in the plane: the first has slope $-1$, while the second has slope $-\frac{2}{5}$. Because the two slopes are different, the lines are not parallel. In the plane, any two non-parallel lines must intersect at exactly one point, which geometrically proves why the solution $(6, 4)$ is unique.

**Show on screen:** The elimination steps leading to $(6, 4)$ and the two lines with slopes $-1$ and $-\frac{2}{5}$.

**If asked to go deeper:** In algebraic terms, the slopes differ if and only if the determinant of the coefficient matrix is non-zero ($\det = 5 - 2 = 3 \neq 0$).

---

## Exercise 10 — verbal script

**Key idea:** Reducing quadratic polynomial interpolation to a linear system of equations.

**What to say:**
We determine a quadratic polynomial $p(x) = ax^2 + bx + c$ passing through three points. Substituting $x = 0$ immediately reveals $c = 1$. Substituting $x = 1$ gives $a + b + 1 = 3$, so $a + b = 2$. Substituting $x = 2$ gives $4a + 2b + 1 = 9$, which simplifies to $2a + b = 4$. Subtracting the two equations gives $a = 2$, and back-substituting gives $b = 0$. The polynomial is $p(x) = 2x^2 + 1$. Checking by substitution, $p(0) = 1, p(1) = 3$, and $p(2) = 9$, confirming all three points lie on the parabola.

**Show on screen:** The system of equations for $a, b, c$ and the verification check on points $(0, 1), (1, 3), (2, 9)$.

**If asked to go deeper:** The coefficient matrix of a polynomial interpolation problem is a Vandermonde matrix, which is always non-singular as long as the interpolation nodes $x_i$ are distinct.

---

## Exercise 11 — verbal script

**Key idea:** Parametric pivot analysis and identifying invalid division points.

**What to say:**
We eliminate $x$ by subtracting $R_1$ from both $R_2$ and $R_3$. This yields rows $(0, t-1, 0 \mid 1)$ and $(0, 0, t-1 \mid 2)$. We observe that $t - 1$ appears on the diagonal pivots. If $t = 1$, row 2 becomes $0 = 1$ and row 3 becomes $0 = 2$, creating contradictions, so there is no solution. If $t \neq 1$, both pivots are non-zero, allowing us to divide by $t - 1$. Back-substitution yields the unique solution $z = \frac{2}{t-1}, y = \frac{1}{t-1}$, and $x = \frac{t-4}{t-1}$. In this system, infinitely many solutions never occurs for any $t$.

**Show on screen:** The echelon matrix with diagonal entries $t-1$ and the case analysis $t = 1$ vs $t \neq 1$.

**If asked to go deeper:** The determinant of the coefficient matrix is $(t-1)^2$, confirming that $t = 1$ is the only singular point.

---

## Exercise 12 — verbal script

**Key idea:** Homogeneous systems, existence of non-trivial solutions, and the trivial solution.

**What to say:**
In this homogeneous system, elimination produces an entire row of zeros, reducing the system to rank 2 with 3 variables. Variable $z$ is free. Setting $z = t$, row 2 gives $y = t$, and row 1 gives $x = -t$, yielding the parametric line $\mathbf{x} = t(-1, 1, 1)^T$. The point $(0, 0, 0)$ always satisfies any homogeneous system because multiplying any coefficient by zero yields zero, meaning $A \mathbf{0} = \mathbf{0}$ holds identically by linearity.

**Show on screen:** The parametric vector $t \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$ and the statement $A\mathbf{0} = \mathbf{0}$.

**If asked to go deeper:** The set of all solutions to a homogeneous system forms a true vector subspace (the kernel or null space), which is closed under vector addition and scalar multiplication.

---

## Exercise 13 — verbal script

**Key idea:** Detecting redundant equations via row elimination and linear combination.

**What to say:**
We perform Gaussian elimination on the system. When we subtract row 1 from row 3 and then add row 2, the third row vanishes completely into zeros. This proves that the third equation is redundant and adds no independent constraints. By direct calculation, subtracting equation 2 from equation 1 gives $(x_1 + x_2) - (x_2 + x_3) = 10 - 8$, which simplifies to $x_1 - x_3 = 2$, reproducing equation 3. Setting $x_3 = t$ gives infinitely many solutions along the line $(2+t, 8-t, t)^T$.

**Show on screen:** The row of zeros in echelon form and the explicit identity $\text{Eq } 3 = \text{Eq } 1 - \text{Eq } 2$.

**If asked to go deeper:** In a geometric context, three equations represent three planes; here, they intersect along a common 1D line rather than at a single point.

---

## Exercise 14 — verbal script

**Key idea:** Sensitivity of overdetermined systems to small perturbations in the right-hand side.

**What to say:**
In the first system, solving the first two equations gives $x = 1, y = 1$, which satisfies the third equation $3(1) = 3$, yielding a unique solution. In the second system, a slight perturbation changes the third equation to $3x = 3.1$. The third line shifts horizontally and no longer passes through $(1, 1)$, creating the contradiction $0 = 0.1$. Geometrically, the first system has three concurrent lines meeting at a single point. Shifting one line turns the concurrence into a small triangle with three pairwise intersections but no common intersection, causing the system to abruptly become inconsistent.

**Show on screen:** The echelon contradiction row $\left[\begin{array}{cc|c} 0 & 0 & 0.1 \end{array}\right]$ and the geometric diagram of 3 concurrent lines versus a triangle.

**If asked to go deeper:** In experimental data fitting, overdetermined systems are almost always inconsistent due to measurement noise, requiring least-squares approximation rather than exact solution.

---

## Exercise 15 — verbal script

**Key idea:** Minimal-step classification into the three fundamental Rouché–Capelli cases.

**What to say:**
We classify three systems using a single elimination step on each. In system 1, subtracting row 1 from row 2 gives a second pivot of $-2$; with rank 2 equal to the number of variables, it has exactly one solution. In system 2, subtracting $2R_1$ from $R_2$ makes the second row vanish into all zeros; with rank 1 less than 2, the lines coincide, giving infinitely many solutions. In system 3, subtracting $2R_1$ from $R_2$ produces $(0, 0 \mid 1)$, which means $0 = 1$; with $\text{rank}(A) < \text{rank}([A \mid b])$, the lines are parallel and distinct, giving no solution.

**Show on screen:** The three echelon matrices side by side, highlighting two pivots, a zero row, and a contradiction row.

**If asked to go deeper:** These three cases correspond algebraically to whether the column space projection has a unique pre-image, a positive-dimensional fiber, or does not contain the target vector.


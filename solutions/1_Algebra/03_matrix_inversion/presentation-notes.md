# Presentation Notes — 03_matrix_inversion

## Topic summary

The inverse of a square matrix $A$ is the unique matrix $A^{-1}$ satisfying $A A^{-1} = A^{-1} A = I$, existing if and only if $\det(A) \neq 0$. Inverses can be computed explicitly for $2 \times 2$ matrices via the adjugate formula and generally via Gauss–Jordan reduction on the augmented matrix $[A \mid I] \to [I \mid A^{-1}]$. Inversion inverts composite maps in reverse order, $(AB)^{-1} = B^{-1} A^{-1}$, and allows solving linear matrix equations $AX = B$ by left multiplication. Geometrically, $A^{-1}$ reverses the distortion produced by $A$, restoring coordinates to their initial configurations.

---

## Exercise 1 — verbal script

**Key idea:** Defining property of the matrix inverse through two-sided multiplication.

**What to say:**
We test whether $B$ is the inverse of $A$ directly from first principles without using formulas. We compute the matrix product $AB$, taking rows of $A$ against columns of $B$, which simplifies entry by entry to the identity matrix $I$. We then compute $BA$, taking rows of $B$ against columns of $A$, which also simplifies entry by entry to $I$. Because both $AB = I$ and $BA = I$, matrix $B$ satisfies the complete two-sided algebraic definition of an inverse matrix. Therefore, $B$ is indeed the inverse of $A$.

**Show on screen:** The calculations $AB = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and $BA = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.

**If asked to go deeper:** For finite-dimensional square matrices, the one-sided condition $AB = I$ automatically implies $BA = I$, although verifying both is best practice from the definition.

---

## Exercise 2 — verbal script

**Key idea:** Explicit $2 \times 2$ matrix inverse formula and multiplication check.

**What to say:**
To invert a $2 \times 2$ matrix, we first compute its determinant: $3 \times 4 - 2 \times 5 = 2$. Because the determinant is non-zero, the inverse exists. We apply the standard formula: swap the main diagonal entries 3 and 4, negate the off-diagonal entries 2 and 5, and divide the entire matrix by the determinant 2. This gives the inverse matrix with entries $2, -1, -\frac{5}{2}$, and $\frac{3}{2}$. Finally, multiplying $A$ by this inverse gives the identity matrix $I$, confirming our calculation.

**Show on screen:** The $2 \times 2$ formula structure $\frac{1}{2}\begin{pmatrix} 4 & -2 \\ -5 & 3 \end{pmatrix}$ and the product verification $A A^{-1} = I$.

**If asked to go deeper:** The swapped and negated matrix is the classical adjugate matrix $\text{adj}(A)$, which satisfies $A \cdot \text{adj}(A) = \det(A) I$ in all dimensions.

---

## Exercise 3 — verbal script

**Key idea:** Non-invertibility diagnosed by zero determinant and row linear dependence.

**What to say:**
We show why $A^{-1}$ does not exist from two perspectives. First, computing the determinant gives $2 \times 2 - 4 \times 1 = 0$. Since invertibility requires $\det(A) \det(A^{-1}) = 1$, a matrix with determinant zero cannot have an inverse. Second, observing the rows, row 1 is $(2, 4)$, which is exactly twice row 2, which is $(1, 2)$. This linear dependence means the matrix has rank 1 rather than full rank 2. As a linear map, it collapses the entire plane onto a single line, destroying information that cannot be reconstructed by any inverse.

**Show on screen:** The determinant calculation $\det = 0$ alongside the relation $R_1 = 2 R_2$.

**If asked to go deeper:** By the Rank-Nullity Theorem, rank 1 implies a 1-dimensional null space spanned by $(-2, 1)^T$, which makes the transformation non-injective.

---

## Exercise 4 — verbal script

**Key idea:** Gauss–Jordan elimination algorithm on augmented matrix $[A \mid I]$.

**What to say:**
We set up the augmented matrix $[A \mid I]$ with $A$ on the left and the $2 \times 2$ identity matrix on the right. First, we eliminate entry $(2,1)$ by subtracting $3R_1$ from $R_2$, producing $(0, -1 \mid -3, 1)$. Second, we scale row 2 by $-1$ to create a leading pivot of 1. Third, we eliminate upwards by subtracting $2R_2$ from $R_1$, leaving the identity matrix on the left. The matrix appearing on the right is $A^{-1}$, with rows $(-5, 2)$ and $(3, -1)$. This works because the elementary row operations that transform $A$ into $I$ represent multiplying by $A^{-1}$, so applying them to $I$ produces $A^{-1} I = A^{-1}$.

**Show on screen:** The three augmented matrix stages and the resulting inverse $\begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix}$.

**If asked to go deeper:** Gauss–Jordan elimination is algebraically equivalent to computing the LU decomposition and solving $n$ systems of equations with standard basis unit vectors as right-hand sides.

---

## Exercise 5 — verbal script

**Key idea:** Gauss–Jordan inversion of a $3 \times 3$ matrix with fraction management.

**What to say:**
We place $A$ alongside the $3 \times 3$ identity matrix. We eliminate the first column by subtracting $R_1$ from $R_3$, then eliminate the second column by adding $R_2$ to $R_3$. This yields an entry of 2 in position $(3,3)$, which we scale to 1 by dividing row 3 by 2. In the upward pass, we eliminate entry $(2,3)$ by subtracting $R_3$ from $R_2$, and eliminate entry $(1,2)$ by subtracting $R_2$ from $R_1$. The identity matrix is now on the left, and factoring out $\frac{1}{2}$ from the right-hand block reveals the inverse matrix. We verify the result by multiplying $A A^{-1}$, which produces the $3 \times 3$ identity matrix.

**Show on screen:** The reduced augmented matrix with factor $\frac{1}{2}$ factored out and the verification product $A A^{-1} = I$.

**If asked to go deeper:** Matrix $A$ is a permutation-like circulant matrix, meaning its inverse must also exhibit circulant symmetry across all rows.

---

## Exercise 6 — verbal script

**Key idea:** Solving a linear system by left-multiplying by the matrix inverse.

**What to say:**
To solve $Ax = b$, we express the solution as $x = A^{-1}b$. We compute $\det(A) = 2 \times 3 - 1 \times 1 = 5$, and use the $2 \times 2$ formula to find $A^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$. Multiplying this inverse matrix by the vector $b = (5, 7)^T$ gives $\frac{1}{5}$ times $(8, 9)^T$, so $x = \left(\frac{8}{5}, \frac{9}{5}\right)^T$. To verify, we substitute $x$ back into the original equations: $2(8/5) + 1(9/5) = 25/5 = 5$, and $1(8/5) + 3(9/5) = 35/5 = 7$. Both original equations are satisfied.

**Show on screen:** The matrix-vector multiplication $A^{-1}b$ and the substitution check into $Ax = b$.

**If asked to go deeper:** The inverse method is computationally ideal when the same system matrix $A$ must be evaluated against thousands of different load vectors $b$, such as in structural engineering.

---

## Exercise 7 — verbal script

**Key idea:** Inverse of a product as the product of inverses in reversed order.

**What to say:**
We compute $(AB)^{-1}$ in two ways. Multiplying $A$ by $B$ gives the upper triangular matrix with rows $(2, 3)$ and $(0, 3)$, whose inverse evaluates to rows $\left(\frac{1}{2}, -\frac{1}{2}\right)$ and $\left(0, \frac{1}{3}\right)$. Alternatively, we invert $B$ and $A$ individually and multiply them in reverse order as $B^{-1}A^{-1}$, obtaining the exact same matrix. The reversed order is required because when transforming by $AB$, $B$ acts first and $A$ acts second. To undo this composition, the last operation ($A$) must be undone first by $A^{-1}$, and only then can $B$ be undone by $B^{-1}$.

**Show on screen:** The side-by-side computation of $(AB)^{-1}$ and $B^{-1}A^{-1}$ demonstrating equality.

**If asked to go deeper:** In group theory, this reversal of elements under inversion is called the anti-automorphism property of groups.

---

## Exercise 8 — verbal script

**Key idea:** Geometric interpretation of an inverse transformation as undoing distortion.

**What to say:**
Matrix $S$ is diagonal with entries 2 and $\frac{1}{2}$, so its inverse is found by reciprocating these entries, giving $\frac{1}{2}$ and 2. Geometrically, $S$ stretches the plane by 2 horizontally while compressing it by $\frac{1}{2}$ vertically. Its inverse $S^{-1}$ does the exact opposite: it compresses horizontally by $\frac{1}{2}$ and stretches vertically by 2. When we apply $S$ to the vector $(4, 6)^T$, it transforms into $(8, 3)^T$. Applying $S^{-1}$ to $(8, 3)^T$ halves the 8 back to 4 and doubles the 3 back to 6, perfectly restoring the initial vector.

**Show on screen:** The vector $(4, 6)^T \xrightarrow{S} (8, 3)^T \xrightarrow{S^{-1}} (4, 6)^T$.

**If asked to go deeper:** Because $\det(S) = 2 \times \frac{1}{2} = 1$, $S$ is a hyperbolic rotation (squeeze mapping) that preserves area while altering aspect ratio.

---

## Exercise 9 — verbal script

**Key idea:** Proper side of multiplication when solving matrix equations $AX = B$.

**What to say:**
To solve $AX = B$ for the unknown matrix $X$, we must multiply both sides by $A^{-1}$ from the left, giving $X = A^{-1}B$. Multiplying on the right would give $AXA^{-1} = BA^{-1}$, which fails to isolate $X$ because matrix multiplication is non-commutative. We invert $A$, which gives rows $(1, -2)$ and $(0, 1)$, and multiply it on the left of $B$. This yields the solution matrix $X$ with rows $(-1, -7)$ and $(2, 4)$. To verify, we multiply $A$ by $X$, which yields the original matrix $B$.

**Show on screen:** The left-multiplication isolation step $A^{-1}(AX) = A^{-1}B \implies X = A^{-1}B$ and the check $AX = B$.

**If asked to go deeper:** If the equation had been $XA = B$, we would multiply by $A^{-1}$ from the right, yielding $X = BA^{-1}$.

---

## Exercise 10 — verbal script

**Key idea:** Direct inspection of invertibility and inversion for diagonal matrices.

**What to say:**
For diagonal matrices, we determine invertibility without elimination by inspecting the diagonal entries. Matrix $D$ has entries $2, -3$, and 5. Because none of these are zero, its determinant is $-30 \neq 0$, making $D$ invertible. Matrix $E$ has a zero in position $(2,2)$, so its determinant is zero, making $E$ singular and non-invertible. To invert $D$, we simply invert each diagonal entry, yielding diagonal entries $\frac{1}{2}, -\frac{1}{3}$, and $\frac{1}{5}$. Multiplying $D$ by this candidate produces the identity matrix, confirming the inverse.

**Show on screen:** Matrices $D$ and $E$, highlighting the non-zero diagonal of $D$ and the zero entry of $E$.

**If asked to go deeper:** A diagonal matrix scales each coordinate axis independently; an entry of zero projects that axis onto the origin, permanently collapsing dimension.

---

## Exercise 11 — verbal script

**Key idea:** Parameter-dependent invertibility and geometric interpretation of singularity.

**What to say:**
We compute the determinant of $A(t)$ as $1 - t^2$. The matrix is invertible if and only if this determinant is non-zero, which means $t \neq 1$ and $t \neq -1$. For all other values, the inverse formula is $\frac{1}{1-t^2}\begin{pmatrix} 1 & -t \\ -t & 1 \end{pmatrix}$. At $t = 1$, the rows are identical and the matrix collapses the entire plane onto the line $y = x$. At $t = -1$, row 2 is $-1$ times row 1, collapsing the plane onto $y = -x$. In both cases, the formula requires dividing by zero, which is undefined because dimension has been lost.

**Show on screen:** The determinant equation $1 - t^2 \neq 0 \implies t \neq \pm 1$ and the inverse formula.

**If asked to go deeper:** The eigenvalues of $A(t)$ are $1+t$ and $1-t$; setting either eigenvalue to zero identifies the singular parameter values.

---

## Exercise 12 — verbal script

**Key idea:** Computing inverses of algebraic matrix combinations using operational identities.

**What to say:**
We find the inverses of three expressions given only $A^{-1}$, without finding $A$ itself. For $(3A)^{-1}$, we use the scalar rule $(cA)^{-1} = \frac{1}{c}A^{-1}$, multiplying $A^{-1}$ by $\frac{1}{3}$. For $(A^T)^{-1}$, transposition and inversion commute, so we transpose $A^{-1}$ directly, swapping entries $-1$ and $-3$. For $(A^2)^{-1}$, the inverse of a square is the square of the inverse, so we multiply $A^{-1}$ by itself, which yields the matrix with rows $(7, -4)$ and $(-12, 7)$. Each computation uses a direct algebraic property rather than inverting from scratch.

**Show on screen:** The three identities $(cA)^{-1} = \frac{1}{c}A^{-1}$, $(A^T)^{-1} = (A^{-1})^T$, and $(A^2)^{-1} = (A^{-1})^2$.

**If asked to go deeper:** In functional calculus, if $f(A)$ is an analytic function of an operator, its inverse is $f(A)^{-1} = (1/f)(A)$, generalizing these power and scalar rules.

---

## Exercise 13 — verbal script

**Key idea:** Undoing a composite transformation and the error of applying inverses in forward order.

**What to say:**
We invert the composite transformation $T = HS$, which applies scaling $S$ followed by shear $H$. Method 1 multiplies $H$ and $S$ to get $T$, then inverts it directly, yielding rows $\left(\frac{1}{2}, -\frac{1}{2}\right)$ and $(0, 1)$. Method 2 inverts $S$ and $H$ separately and multiplies in reverse order as $S^{-1}H^{-1}$, producing the exact same matrix. In contrast, multiplying in forward order as $H^{-1}S^{-1}$ gives entry $(1,2)$ as $-1$ instead of $-\frac{1}{2}$. This demonstrates the fundamental rule: when undoing a sequence of operations, they must be undone from the end, because undoing them in the forward order acts on coordinates that are still warped by subsequent operations.

**Show on screen:** The comparison $S^{-1}H^{-1} = T^{-1}$ versus $H^{-1}S^{-1} \neq T^{-1}$.

**If asked to go deeper:** This principle is identical to the LIFO (Last-In, First-Out) stack structure in computer science.

---

## Exercise 14 — verbal script

**Key idea:** Involutory matrices satisfying $A^2 = I$ and construction of non-trivial reflections.

**What to say:**
If a matrix satisfies $A^2 = I$, then $A \cdot A = I$. By the definition of the matrix inverse, any matrix that multiplies $A$ to give the identity is its inverse, so $A^{-1} = A$. A matrix that is its own inverse is called an involution. To find a non-trivial $2 \times 2$ example different from $\pm I$, we consider a reflection across the line $y = x$, given by the matrix with rows $(0, 1)$ and $(1, 0)$. Multiplying this matrix by itself swaps coordinates twice, returning every vector $(x, y)$ back to $(x, y)$, which confirms that $A^2 = I$.

**Show on screen:** The definition step $A \cdot A = I \implies A^{-1} = A$ and the reflection matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

**If asked to go deeper:** Any involution $A$ can be diagonalized with eigenvalues in $\{+1, -1\}$, corresponding to the decomposition of space into invariant and reflected eigenspaces.

---

## Exercise 15 — verbal script

**Key idea:** Method comparison: matrix inversion versus Gaussian elimination for solving linear systems.

**What to say:**
We solve the system $Ax = b$ using two distinct approaches. In Method 1, we invert $A$ and compute $x = A^{-1}b$, which involves computing the determinant, constructing the $2 \times 2$ inverse, and carrying out a matrix-vector product to obtain $x = \left(\frac{13}{5}, \frac{9}{5}\right)^T$. In Method 2, we perform Gaussian elimination directly on the augmented matrix: one row swap and one row operation puts the system into echelon form, followed by back-substitution to get the exact same answer. For this single system, Gaussian elimination was simpler because it avoids computing the four entries of $A^{-1}$. However, if we needed to solve for multiple right-hand sides, computing $A^{-1}$ once would be more efficient.

**Show on screen:** The two solution pathways side by side, highlighting the operation count and the final vector $\begin{pmatrix} 13/5 \\ 9/5 \end{pmatrix}$.

**If asked to go deeper:** For an $n \times n$ system, Gaussian elimination requires $\frac{2}{3}n^3$ operations, whereas computing $A^{-1}$ and multiplying takes $2n^3$ operations, making elimination three times faster.


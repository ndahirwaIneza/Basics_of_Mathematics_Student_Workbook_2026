# Presentation Notes — 02_determinants

## Topic summary

The determinant is an alternating multilinear functional that assigns a scalar volume scaling factor to any square matrix. A matrix is invertible if and only if its determinant is non-zero. Determinants behave multiplicatively under matrix products, satisfy $\det(cA) = c^n \det(A)$, and remain invariant under transposition and row addition operations. Geometrically, the determinant computes the signed oriented area or volume spanned by the column or row vectors, making it an essential diagnostic for linear independence, matrix invertibility, and uniqueness of solutions to linear systems.

---

## Exercise 1 — verbal script

**Key idea:** Determinant of a $2 \times 2$ matrix and the invertibility criterion.

**What to say:**
We evaluate the determinants of two $2 \times 2$ matrices using the formula $ad - bc$. For the first matrix, $3 \times 4 - (-2) \times 5 = 12 + 10 = 22$. Because 22 is non-zero, this matrix is invertible. For the second matrix, $1 \times 14 - 7 \times 2 = 14 - 14 = 0$. Because its determinant is zero, this matrix is singular and not invertible. A matrix is invertible if and only if its determinant is non-zero, because a zero determinant indicates that the transformation collapses 2D space onto a lower-dimensional subspace.

**Show on screen:** The calculations $12 - (-10) = 22 \neq 0$ and $14 - 14 = 0$, highlighting the invertibility conclusions.

**If asked to go deeper:** In the second matrix, row 2 is exactly twice row 1, demonstrating that linear dependence between rows always forces the determinant to vanish.

---

## Exercise 2 — verbal script

**Key idea:** Sarrus' rule for $3 \times 3$ matrices verified by cofactor expansion.

**What to say:**
To compute the determinant of this $3 \times 3$ matrix, we apply Sarrus' rule by summing three downward diagonal products and subtracting three upward diagonal products. The downward diagonals give 15, 16, and 0, which sum to 31. The upward diagonals give $-6$, 4, and 0, summing to $-2$. Subtracting gives $31 - (-2) = 33$. To verify, we expand along column 1 because it contains a convenient zero entry. Computing the two non-zero cofactors yields $11 + 22 = 33$, perfectly confirming our result.

**Show on screen:** The Sarrus diagonal groupings and the cofactor expansion along the first column.

**If asked to go deeper:** Sarrus' rule is a shortcut specific to $3 \times 3$ matrices that accounts for all $3! = 6$ permutations in the Leibniz formula, but does not generalize to $4 \times 4$ or higher dimensions.

---

## Exercise 3 — verbal script

**Key idea:** Effect of row swaps on determinant sign.

**What to say:**
First, we expand matrix $A$ along its first row, obtaining a determinant of 6. Next, matrix $B$ is created by swapping row 1 and row 2 of $A$. By the alternating property of determinants, swapping any two rows multiplies the determinant by $-1$, so we predict that $\det B$ equals $-6$. We then compute $\det B$ directly by expanding along its first row, which yields $0 - 3(1) + 1(-3) = -6$. The explicit calculation confirms our theoretical prediction.

**Show on screen:** The predicted value $\det B = -\det A = -6$ alongside the step-by-step expansion of $B$.

**If asked to go deeper:** A row swap corresponds to multiplying by a permutation matrix with determinant $-1$, reversing the orientation of the row vectors.

---

## Exercise 4 — verbal script

**Key idea:** Determinant of a triangular matrix as the product of diagonal elements.

**What to say:**
The matrix is upper triangular because all entries below the main diagonal are zeros. For any triangular or diagonal matrix, the determinant equals the product of its diagonal entries. Multiplying the diagonal entries directly gives $2 \times (-3) \times 7 = -42$. We explain this by cofactor expansion: expanding along the first column isolates $t_{11}$ times the determinant of a $2 \times 2$ triangular submatrix, which in turn reduces to the product of its diagonal entries. Repeating this process for any triangular matrix always yields the product of all main diagonal elements.

**Show on screen:** The diagonal entries 2, $-3$, 7 circled and their product $-42$.

**If asked to go deeper:** The diagonal entries of a triangular matrix are its eigenvalues, and the determinant is always the product of all eigenvalues.

---

## Exercise 5 — verbal script

**Key idea:** Evaluating determinants using Gaussian elimination and tracking operation effects.

**What to say:**
We simplify the matrix into upper triangular form using row operations while monitoring their impact on the determinant. First, subtracting $2R_1$ from $R_2$ preserves the determinant. Second, adding $R_1$ to $R_3$ also preserves the determinant. Third, adding $2R_2$ to $R_3$ creates our final zero in position $(3,2)$, completing the upper triangular form. Because all three operations were row replacements of the form $R_i \leftarrow R_i + c R_j$, none of them altered the determinant. We read off the determinant by multiplying the diagonal entries: $1 \times (-3) \times (-7) = 21$.

**Show on screen:** The sequence of matrices $A \to A_1 \to A_2 \to A_3$ and the final diagonal product.

**If asked to go deeper:** Row replacement corresponds to multiplying by a unit lower triangular matrix, which has determinant 1 and therefore preserves the determinant of the original matrix.

---

## Exercise 6 — verbal script

**Key idea:** Singular parameter values and geometric interpretation of zero determinant.

**What to say:**
We calculate the determinant of $A(t)$ as $t \times t - 1 \times 2 = t^2 - 2$. A matrix fails to be invertible if and only if its determinant is zero. Setting $t^2 - 2 = 0$ gives $t = \sqrt{2}$ and $t = -\sqrt{2}$. When the determinant is zero, the linear transformation collapses the plane onto a single line, shrinking area to zero. This loss of dimensionality means distinct vectors map to the same point, so the map is not one-to-one and cannot be inverted.

**Show on screen:** The equation $t^2 - 2 = 0 \implies t = \pm\sqrt{2}$ and the geometric collapse to a 1D line.

**If asked to go deeper:** At $t = \pm\sqrt{2}$, the rows are scalar multiples of each other ($R_2 = \pm\sqrt{2} R_1$), explicitly showing linear dependence.

---

## Exercise 7 — verbal script

**Key idea:** Applying algebraic determinant identities for scaling, transposition, powers, and signs.

**What to say:**
Given that $A$ is a $3 \times 3$ matrix with $\det A = -4$, we use algebraic properties rather than entries. For $\det(2A)$, each of the 3 rows is multiplied by 2, pulling out $2^3 = 8$, which gives $8 \times (-4) = -32$. For $\det(A^T)$, transposition preserves the determinant, so it remains $-4$. For $\det(A^2)$, the multiplicative property gives $(\det A)^2 = (-4)^2 = 16$. For $\det(-A)$, pulling out $-1$ from each of the 3 rows gives $(-1)^3 \times (-4) = -1 \times (-4) = 4$.

**Show on screen:** The formulas $c^n \det(A)$, $\det(A^T)$, and $(\det A)^2$ with substituted values.

**If asked to go deeper:** The identity $\det(cA) = c^n \det(A)$ highlights that determinant is an $n$-linear function of the matrix rows.

---

## Exercise 8 — verbal script

**Key idea:** Determinant of matrix products and commutativity of the scalar determinant map.

**What to say:**
Using the product rule, $\det(AB) = \det(A)\det(B) = 3 \times (-5) = -15$. Similarly, $\det(BA) = (-5) \times 3 = -15$. Since $\det A = 3 \neq 0$, $A$ is invertible with determinant $\frac{1}{3}$, giving $\det(A^{-1}B) = \frac{1}{3} \times (-5) = -\frac{5}{3}$. The products $AB$ and $BA$ have identical determinants even though the matrices themselves do not commute. This occurs because the determinant maps matrices to real numbers, and scalar multiplication in $\mathbb{R}$ is strictly commutative.

**Show on screen:** The product formula $\det(AB) = \det(A)\det(B) = \det(BA) = -15$ and the fraction $-\frac{5}{3}$.

**If asked to go deeper:** The determinant is a group homomorphism from $\text{GL}(n, \mathbb{R})$ to the multiplicative group $\mathbb{R}^\times$, which maps a non-abelian group into an abelian group.

---

## Exercise 9 — verbal script

**Key idea:** Parallelogram area as absolute determinant and geometric meaning of sign.

**What to say:**
We assemble vectors $u$ and $v$ as columns of a matrix. The determinant is $3(4) - 1(1) = 11$, so the geometric area of the spanned parallelogram is the absolute value, which is 11. When we reverse the order of vectors to $(v, u)$, the columns are swapped, flipping the determinant to $-11$. The sign changes because the orientation of the vector pair flips from counterclockwise to clockwise. However, the geometric area remains exactly 11 because physical area is positive and independent of orientation.

**Show on screen:** The matrices $\begin{pmatrix} 3 & 1 \\ 1 & 4 \end{pmatrix}$ and $\begin{pmatrix} 1 & 3 \\ 4 & 1 \end{pmatrix}$ with determinants $+11$ and $-11$.

**If asked to go deeper:** In differential geometry, the signed determinant represents the pullback of the standard differential 2-form $dx \wedge dy$.

---

## Exercise 10 — verbal script

**Key idea:** Row dependence inspection and its equivalence to singularity.

**What to say:**
Looking at the matrix rows, we immediately observe that row 2, which is $(2, 4, 6)$, is exactly 2 times row 1, which is $(1, 2, 3)$. When one row of a matrix is a scalar multiple of another, subtracting that multiple creates an entire row of zeros without changing the determinant. Expanding along that zero row gives $\det = 0$. In terms of invertibility, linearly dependent rows mean the rank is at most 2, strictly less than 3. By the Invertible Matrix Theorem, a square matrix is invertible if and only if its determinant is non-zero, so this matrix is singular.

**Show on screen:** Row 1 and Row 2 highlighted with the relation $R_2 = 2R_1$.

**If asked to go deeper:** The row vectors span a 2D plane in 3D space, so the 3D parallelepiped they form has zero thickness and zero volume.

---

## Exercise 11 — verbal script

**Key idea:** Strategic row elimination to create zeros and evaluate determinants efficiently.

**What to say:**
Rather than computing large products mechanically, we use row operations to create zeros. Subtracting row 1 from row 2 creates a zero in position $(2,1)$, leaving $(0, 1, 1)$. Subtracting row 1 from row 3 creates a zero in position $(3,1)$, leaving $(0, 2, 3)$. Then, subtracting twice row 2 from row 3 eliminates position $(3,2)$, leaving $(0, 0, 1)$. All of these operations are row additions of the form $R_i \leftarrow R_i + c R_j$, which do not change the determinant. The matrix is now upper triangular, so its determinant is simply $1 \times 1 \times 1 = 1$.

**Show on screen:** The intermediate steps with arrows showing the creation of zeros in the lower triangle.

**If asked to go deeper:** Row operations are equivalent to an $LU$ decomposition where $L$ is unit lower triangular with determinant 1.

---

## Exercise 12 — verbal script

**Key idea:** Parameter isolation through row operations and row dependence analysis.

**What to say:**
We apply $R_2 \leftarrow R_2 - 2R_1$ before expanding. Row 2 becomes $(0, 0, t-6)$. Expanding along this second row, which contains two zeros, immediately yields $-(t-6)$ times the $2 \times 2$ minor, which evaluates to $6 - t$. Setting this determinant to zero gives $t = 6$ as the unique value for non-invertibility. When $t = 6$, the original row 2 becomes $(2, 4, 6)$, which is exactly twice row 1. This linear dependence between the first two rows is what forces the determinant to zero.

**Show on screen:** The reduced row $(0, 0, t-6)$ and the resulting equation $\det A(t) = 6 - t = 0$.

**If asked to go deeper:** Concentrating the parameter into a single entry of a row or column makes finding eigenvalues or singular points computationally trivial.

---

## Exercise 13 — verbal script

**Key idea:** Systematic tracking of determinant scaling factors during Gaussian elimination.

**What to say:**
We evaluate the determinant using systematic Gaussian elimination. To eliminate the first column, we replace $R_2$ by $R_2 - 2R_1$ and $R_3$ by $R_3 - R_1$; both row replacements preserve the determinant with factor 1. This produces rows $(0, 1, 1)$ and $(0, -2, -1)$. Next, to eliminate position $(3,2)$, we replace $R_3$ by $R_3 + 2R_2$, another replacement preserving the determinant. The matrix is now upper triangular with diagonal entries 1, 1, and 1. Multiplying the diagonal entries gives a final determinant of 1.

**Show on screen:** The three elimination steps with explicit note: "Determinant factor: $\times 1$ at each step".

**If asked to go deeper:** If an elimination step ever requires row swapping or scaling, the cumulative determinant formula tracks those factors as $(-1)^s \prod d_i$.

---

## Exercise 14 — verbal script

**Key idea:** Determinant criterion for uniqueness versus Rouché–Capelli cases.

**What to say:**
The determinant of coefficient matrix $A$ is $4 - 2k$. By Cramer's rule, the system $Ax = b$ has a unique solution for every right-hand side vector if and only if the determinant is non-zero, which means $k \neq 2$. When $k = 2$, the determinant is zero and row 2 is twice row 1. For $b = (1, 2)^T$, the right-hand side satisfies the exact same ratio ($2 = 2 \times 1$), making the equations identical and yielding infinitely many solutions. For $b = (1, 3)^T$, the ratio fails ($3 \neq 2 \times 1$), creating the contradiction $0 = 1$ and yielding no solution.

**Show on screen:** The augmented matrices for both $k=2$ cases: consistent row of zeros versus inconsistent row $\left[\begin{array}{cc|c} 0 & 0 & 1 \end{array}\right]$.

**If asked to go deeper:** This illustrates the Fredholm alternative: either $Ax = b$ has a unique solution for all $b$, or the homogeneous system has non-trivial solutions and consistency depends on orthogonality to the cokernel.

---

## Exercise 15 — verbal script

**Key idea:** Determinant invariance under similarity transformations and basis changes.

**What to say:**
We calculate $\det(B^{-1}A^TB)$ using determinant properties. By the product rule, this splits into $\det(B^{-1}) \times \det(A^T) \times \det(B)$. The determinant of $B^{-1}$ is $\frac{1}{\det B} = \frac{1}{3}$, and transposition leaves $\det A$ unchanged at $-2$. Substituting gives $\frac{1}{3} \times (-2) \times 3 = -2$. The factors involving $B$ cancel because they are real scalars that commute and multiply to 1. Geometrically, $B^{-1}A^TB$ is a change of basis (conjugation), and because changing basis and its inverse apply reciprocal area scaling factors, the net determinant of the operator is invariant.

**Show on screen:** The cancellation $\frac{1}{3} \cdot 3 = 1$ leaving $\det(A^T) = -2$.

**If asked to go deeper:** The determinant is an intrinsic property of a linear operator, completely independent of the coordinate basis chosen to represent it.


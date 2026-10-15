# Presentation Notes — 01_matrices_and_operations

## Topic summary

Matrices represent linear mappings and arrays of data whose algebra is defined through entrywise operations and row-by-column multiplication. Matrix multiplication is defined only when inner dimensions match, and unlike real numbers, it is associative but strictly non-commutative. Viewing the product $Ax$ as a linear combination of the columns of $A$ reveals the link between matrix algebra and vector spaces. Furthermore, matrix operations faithfully model geometric transformations such as rotations and scaling, where composition order directly dictates the resulting geometry.

---

## Exercise 1 — verbal script

**Key idea:** Reading matrix dimensions and indexing entries by (row, column).

**What to say:**
We start by identifying the dimensions of each matrix. Matrix $A$ has 2 rows and 3 columns, so its size is $2 \times 3$, while $B$ has 3 rows and 2 columns, making it $3 \times 2$. To read off specific entries, we recall that the first subscript indicates the row and the second indicates the column. Looking at row 1, column 2 of $A$, we get $a_{12} = -1$. In row 2, column 3, $a_{23} = 5$. For $B$, row 2, column 1 gives $b_{21} = -2$, and row 3, column 2 gives $b_{32} = 1$. Finally, we extract the second row of $A$ as the row vector $(0, 4, 5)$, and the first column of $B$ as the column vector with entries $1, -2, 4$.

**Show on screen:** The matrices $A$ and $B$, pointing to the row-column intersections for each entry and the extracted vectors.

**If asked to go deeper:** The entry $a_{ij}$ represents the coefficient of the $j$-th input variable in the $i$-th coordinate equation of the associated linear mapping.

---

## Exercise 2 — verbal script

**Key idea:** Entrywise linear combinations and dimension matching for addition.

**What to say:**
Matrix addition and scalar multiplication are performed entry by entry. Because both $A$ and $B$ are $2 \times 2$, their dimensions match and the operations are valid. To find $A+B$, we add corresponding entries, getting the matrix with rows $(5, 0)$ and $(-1, 8)$. For $A-B$, we subtract entrywise, paying close attention to signs like $2 - (-2) = 4$, which gives rows $(-3, 4)$ and $(-1, -2)$. For $3A-2B$, we scale $A$ by 3, scale $B$ by 2, and take their difference, yielding rows $(-5, 10)$ and $(-3, -1)$. Addition requires identical dimensions because every entry in one matrix must have exactly one corresponding partner in the other.

**Show on screen:** The intermediate steps of $3A - 2B$ showing scalar multiplication before subtraction.

**If asked to go deeper:** The set of all $m \times n$ matrices over $\mathbb{R}$ forms a real vector space of dimension $mn$ under these entrywise operations.

---

## Exercise 3 — verbal script

**Key idea:** Dimension compatibility condition for matrix products.

**What to say:**
Two matrices can be multiplied if and only if the inner dimensions match: an $m \times n$ matrix can multiply an $n \times p$ matrix, producing an $m \times p$ matrix. We check each pair systematically. For $AB$, $(2 \times 3)$ times $(3 \times 4)$ has matching inner dimension 3, yielding a $2 \times 4$ matrix. For $BA$, $(3 \times 4)$ times $(2 \times 3)$ fails because $4 \neq 2$, so it is undefined. Continuing through all pairs, $BC$ is defined with size $3 \times 2$, while $CB$ is undefined. $AC$ is undefined, but $CA$ is defined with size $4 \times 3$. Lastly, $AD$ is undefined because $3 \neq 2$, whereas $DA$ is defined with size $2 \times 3$.

**Show on screen:** The list of pairs with inner dimensions highlighted to illustrate matches and mismatches.

**If asked to go deeper:** The product $MN$ represents composing the linear map $N: V \to W$ with $M: W \to U$, which requires the codomain of $N$ to match the domain of $M$.

---

## Exercise 4 — verbal script

**Key idea:** Matrix multiplication algorithm and failure of commutativity.

**What to say:**
We compute the products $AB$ and $BA$ using the standard row-column dot product rule. For $AB$, we take rows of $A$ against columns of $B$, which gives the matrix with first row $(8, 2)$ and second row $(3, 1)$. Next, computing $BA$ by taking rows of $B$ against columns of $A$ yields first row $(2, 4)$ and second row $(3, 7)$. Comparing the two, we see $AB \neq BA$. This demonstrates that matrix multiplication is non-commutative. Even though both matrices are square and of the same size, changing the order of multiplication changes the resulting transformation.

**Show on screen:** The side-by-side computation of entries $(1,1)$ of $AB$ and $BA$ showing $8 \neq 2$.

**If asked to go deeper:** Although $AB \neq BA$ in general, their traces and characteristic polynomials are always identical for square matrices.

---

## Exercise 5 — verbal script

**Key idea:** Expressing matrix-vector multiplication as a linear combination of columns.

**What to say:**
We first evaluate $Ax$ directly by taking dot products of each row of $A$ with $x$, obtaining the vector with components 6 and 10. Next, we interpret this operation through the column perspective. We decompose $A$ into its two columns: column 1 is $(2, 1)^T$ and column 2 is $(-1, 3)^T$. Weighting these columns by the components of $x$, which are 4 and 2, gives 4 times the first column plus 2 times the second column. Carrying out the scalar multiplication and adding gives exactly $(6, 10)^T$. This confirms that $Ax$ is always a linear combination of the columns of $A$.

**Show on screen:** The column combination equation $4 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 2 \begin{pmatrix} -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 6 \\ 10 \end{pmatrix}$.

**If asked to go deeper:** This column perspective proves that the system $Ax=b$ has a solution if and only if $b$ lies in the column space (span of columns) of $A$.

---

## Exercise 6 — verbal script

**Key idea:** Transposition and the reversal of factors in $(AB)^T = B^T A^T$.

**What to say:**
To transpose a matrix, we swap its rows and columns. Matrix $A$ is $2 \times 3$, so $A^T$ is $3 \times 2$, and $B$ is $3 \times 2$, so $B^T$ is $2 \times 3$. Multiplying $A$ by $B$ gives the $2 \times 2$ matrix with rows $(2, 11)$ and $(8, 23)$, so $(AB)^T$ has rows $(2, 8)$ and $(11, 23)$. Next, we compute $B^T A^T$, multiplying a $2 \times 3$ matrix by a $3 \times 2$ matrix. The resulting rows are also $(2, 8)$ and $(11, 23)$. This directly verifies that $(AB)^T = B^T A^T$.

**Show on screen:** The transposition step $(AB)^T$ side-by-side with the product $B^T A^T$.

**If asked to go deeper:** The factor reversal occurs because transposition interchanges input and output spaces when viewing matrices as dual maps between vector spaces.

---

## Exercise 7 — verbal script

**Key idea:** Multiplicative and additive identities, and nilpotent decomposition of powers.

**What to say:**
Multiplying $A$ by the identity matrix $I$ from either side leaves $A$ unchanged, confirming that $I$ is the multiplicative identity. Adding the zero matrix leaves $A$ unchanged, confirming that $0$ is the additive identity. Computing powers, $A^2$ gives diagonal entries 4 and top-right entry 4, while $A^3$ gives diagonal entries 8 and top-right entry 12. Decomposing $A$ as $2I + N$, where $N$ has only a 1 in the upper right corner and squares to zero, we find the general power formula: the diagonal entries are $2^n$ and the upper right entry is $n 2^{n-1}$.

**Show on screen:** The power progression $A, A^2, A^3$ and the general formula $\begin{pmatrix} 2^n & n 2^{n-1} \\ 0 & 2^n \end{pmatrix}$.

**If asked to go deeper:** This matrix represents a Jordan block of eigenvalue 2, where higher powers follow the truncated binomial expansion since the nilpotent part satisfies $N^2 = 0$.

---

## Exercise 8 — verbal script

**Key idea:** Elementary row operations and their explicit inverses.

**What to say:**
We apply three row operations to matrix $A$ in sequence. First, $R_2 \leftarrow R_2 - 2R_1$ zeros out the first entry in row 2, yielding row $(0, 0, 3)$; its reverse operation is $R_2 \leftarrow R_2 + 2R_1$. Second, $R_3 \leftarrow R_3 + R_1$ simplifies row 3 to $(0, 3, 2)$; its reverse is $R_3 \leftarrow R_3 - R_1$. Third, interchanging rows 2 and 3 puts the matrix into upper triangular form with rows $(1, 2, -1)$, $(0, 3, 2)$, and $(0, 0, 3)$. The reverse of a row swap is the exact same row swap. Because every elementary row operation is reversible, row reduction does not lose any information.

**Show on screen:** The three matrices $A_1, A_2, A_3$ alongside their labelled reverse operations.

**If asked to go deeper:** Each elementary row operation corresponds to multiplying on the left by an invertible elementary matrix.

---

## Exercise 9 — verbal script

**Key idea:** Geometric interpretation of noncommutativity under scaling and rotation.

**What to say:**
We study two geometric operations: $S$, which doubles the $x$-coordinate, and $R$, which rotates by $90^\circ$ counterclockwise. Applying $RS$ to vector $(1, 2)^T$ means scaling first to $(2, 2)^T$, then rotating to $(-2, 2)^T$. In contrast, applying $SR$ rotates first to $(-2, 1)^T$, then scales the $x$-component to give $(-4, 1)^T$. The results are distinct because scaling acts specifically along the coordinate $x$-axis. When we rotate first, the original $y$-component becomes the new $x$-component, so a different geometric direction is stretched.

**Show on screen:** The two vectors $RSx = (-2, 2)^T$ and $SRx = (-4, 1)^T$ plotted or highlighted.

**If asked to go deeper:** Scaling along the axes commutes only with rotations that are multiples of $180^\circ$, or if the scaling is uniform ($S = cI$).

---

## Exercise 10 — verbal script

**Key idea:** Column-by-column construction of matrix multiplication.

**What to say:**
We compute $Ab_1$ and $Ab_2$ where $b_1$ and $b_2$ are the columns of $B$. Multiplying $A$ by $b_1$ gives $(-1, 2)^T$, and multiplying $A$ by $b_2$ gives $(2, 1)^T$. When we compute the full product matrix $AB$, the first column is $(-1, 2)^T$ and the second column is $(2, 1)^T$. This shows that the columns of $AB$ are precisely $Ab_1$ and $Ab_2$. The full matrix multiplication is simply performing matrix-vector multiplication on each column of $B$ in parallel and placing the results side by side.

**Show on screen:** The partitioning $AB = \begin{pmatrix} Ab_1 & Ab_2 \end{pmatrix}$ matching the calculated columns.

**If asked to go deeper:** This property enables parallel algorithms in numerical linear algebra, where matrix columns are distributed across independent processor cores.

---

## Exercise 11 — verbal script

**Key idea:** Determining commuting matrices by solving entrywise linear equations.

**What to say:**
To find all matrices $B$ that commute with $A$, we compute $AB$ and $BA$ symbolically and equate corresponding entries. Entry $(1,1)$ requires $a+c = a$, which forces $c = 0$. Entry $(1,2)$ requires $b+d = a+b$, which forces $d = a$. Entries $(2,1)$ and $(2,2)$ provide no further constraints. Therefore, any commuting matrix $B$ must have $c = 0$ and diagonal entries both equal to $a$, with $b$ free. This means $B$ has the form $\begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$, which can be written as $aI + b(A-I)$, a linear polynomial in $A$.

**Show on screen:** The four entrywise equations and the resulting general matrix form.

**If asked to go deeper:** By the Cayley–Hamilton theorem and Frobenius's theorem, any matrix commuting with a matrix with distinct eigenvalues or a single full Jordan block must be a polynomial in that matrix.

---

## Exercise 12 — verbal script

**Key idea:** Conjecturing a power formula and proving it by mathematical induction.

**What to say:**
We compute the first few powers of $A$: $A^2$ has top-right entry 2, $A^3$ has 3, and $A^4$ has 4, with 1s on the diagonal and 0 in the bottom-left. This leads to the conjecture that $A^n$ has top-right entry $n$. To prove this for all $n \ge 1$, we use induction. The base case $n=1$ is clear. For the induction step, we assume $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$ and multiply by $A$. The resulting product gives 1 on the diagonal, 0 in the lower-left, and $1 + n$ in the upper-right, which is precisely the formula for $n+1$.

**Show on screen:** The inductive multiplication step showing $(1 \cdot 1 + n \cdot 0)$ and $(1 \cdot 1 + n \cdot 1) = n+1$.

**If asked to go deeper:** Geometrically, $A$ represents a horizontal shear of factor 1; applying $n$ consecutive shears of factor 1 produces an overall shear of factor $n$.

---

## Exercise 13 — verbal script

**Key idea:** Fibonacci sequence generation via matrix powers and vector recurrence.

**What to say:**
We compute successive powers of $F$: $F^2$ has entries 2, 1, 1, 1; $F^3$ has 3, 2, 2, 1; $F^4$ has 5, 3, 3, 2; and $F^5$ has 8, 5, 5, 3. These entries are consecutive Fibonacci numbers, giving $F^n = \begin{pmatrix} f_{n+1} & f_n \\ f_n & f_{n-1} \end{pmatrix}$. When we multiply $F$ by a vector $(a, b)^T$, the result is $(a+b, a)^T$. The first component adds the two terms together, while the second component preserves the leading term. This performs one step of the Fibonacci recurrence in matrix form.

**Show on screen:** The powers of $F$ aligned with the Fibonacci sequence $0, 1, 1, 2, 3, 5, 8$.

**If asked to go deeper:** Diagonalizing $F$ using its eigenvalues $\frac{1 \pm \sqrt{5}}{2}$ directly derives Binet's closed-form formula for Fibonacci numbers.

---

## Exercise 14 — verbal script

**Key idea:** Verification of the rotation group property using trigonometric angle-sum identities.

**What to say:**
We multiply two rotation matrices $R(\alpha)$ and $R(\beta)$. Expanding the product gives entries involving products of sines and cosines. Using the angle-sum formula for cosine on the diagonal entries gives $\cos(\alpha+\beta)$, and the angle-sum formula for sine on the off-diagonal entries gives $\pm \sin(\alpha+\beta)$. The product simplifies exactly to $R(\alpha+\beta)$. Geometrically, this means rotating the plane by angle $\beta$ and then rotating by angle $\alpha$ is identical to a single rotation by $\alpha+\beta$.

**Show on screen:** The trigonometric expansion line grouping into $\cos(\alpha+\beta)$ and $\sin(\alpha+\beta)$.

**If asked to go deeper:** This proves that the set of 2D rotation matrices forms an abelian subgroup of the general linear group, known as the Lie group $\text{SO}(2)$.

---

## Exercise 15 — verbal script

**Key idea:** Associativity of matrix multiplication and computational cost of parenthesization.

**What to say:**
We compute the product of three matrices in two different ways: $(AB)C$ and $A(BC)$. First computing $AB$ gives a $2 \times 2$ matrix, which when multiplied by $C$ yields the matrix with rows $(10, 3)$ and $(2, -3)$. Evaluating $A(BC)$ by computing the $3 \times 2$ matrix $BC$ first and then multiplying by $A$ yields the exact same matrix. This demonstrates associativity: grouping does not change the result. However, counting scalar multiplications shows that $(AB)C$ requires 20 multiplications, while $A(BC)$ requires 24. Even though both parenthesizations yield the same answer, one is computationally cheaper.

**Show on screen:** The operation counts: $12 + 8 = 20$ versus $12 + 12 = 24$.

**If asked to go deeper:** In large-scale numerical computation, finding the parenthesization that minimizes total operations is solved in $O(n^3)$ time using dynamic programming.


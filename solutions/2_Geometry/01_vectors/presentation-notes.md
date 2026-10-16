# Presentation Notes — 01_vectors

## Topic summary

Vectors in $\mathbb{R}^2$ and $\mathbb{R}^3$ represent geometric quantities defined by magnitude and direction, handled algebraically as coordinate tuples. Componentwise linear operations model consecutive translations and scaling. The dot product provides an intrinsic metric to compute Euclidean lengths, orthogonal projections, and angles, establishing the algebraic test for perpendicularity. In three dimensions, the cross product generates a mutually perpendicular vector whose magnitude encodes the area of the spanned parallelogram. Together, these tools form the basis for constructing planes, defining coordinate frames, and solving geometric optimization problems.

---

## Exercise 1 — verbal script

**Key idea:** Componentwise vector addition, subtraction, scalar multiplication, and the parallelogram rule.

**What to say:**
We are given two vectors in $\mathbb{R}^3$, $u = (2, -1, 3)$ and $v = (-1, 4, 2)$. To find their sum $u+v$, we add corresponding coordinates, obtaining $(1, 3, 5)$. For $u-v$, we subtract entrywise, being careful with signs like $2 - (-1) = 3$, which gives $(3, -5, 1)$. For the linear combination $3u - 2v$, we scale $u$ by 3 to get $(6, -3, 9)$, scale $v$ by 2 to get $(-2, 8, 4)$, and take the difference, yielding $(8, -11, 5)$. We then verify that $(u+v)-v$ returns $(2, -1, 3)$, which exactly matches $u$. Geometrically, adding two vectors corresponds to placing the tail of the second vector at the head of the first, with the sum vector forming the diagonal of the parallelogram spanning both translations.

**Show on screen:** The componentwise arithmetic for $3u - 2v$ and the cancellation step $(u+v)-v = u$.

**If asked to go deeper:** Vector addition in $\mathbb{R}^3$ forms an abelian group satisfying associativity, commutativity, the existence of a zero vector, and additive inverses.

---

## Exercise 2 — verbal script

**Key idea:** Displacement vectors and computing Euclidean distance via vector length.

**What to say:**
We are given two points in space, $A = (1, 2, 3)$ and $B = (4, -2, 6)$. We first construct the displacement vector $\overrightarrow{AB}$ by subtracting the coordinates of initial point $A$ from terminal point $B$, which gives $(3, -4, 3)$. Next, we calculate its Euclidean norm by taking the square root of the sum of squared components: $\sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{9 + 16 + 9} = \sqrt{34}$. When we evaluate the distance between points $A$ and $B$ using the Cartesian distance formula, we write the exact same square root of differences squared, arriving at $\sqrt{34}$. Both calculations coincide because the distance between two points in Euclidean space is by definition the norm of their connecting displacement vector, both deriving from the 3D Pythagorean theorem.

**Show on screen:** The vector components $(3, -4, 3)$ alongside the coordinate distance formula under the radical.

**If asked to go deeper:** The Euclidean distance metric is translation invariant, meaning $d(A+v, B+v) = d(A, B)$ for any constant translation vector $v$.

---

## Exercise 3 — verbal script

**Key idea:** Vector normalization and decomposing a vector into magnitude and unit direction.

**What to say:**
We are given the 2D vector $v = (3, 4)$. To normalize it, we first find its magnitude: $\sqrt{3^2 + 4^2} = \sqrt{25} = 5$. We obtain the unit vector $e$ by dividing $v$ by its length, yielding $(3/5, 4/5)$ or $(0.6, 0.8)$. We check that $\|e\| = \sqrt{(3/5)^2 + (4/5)^2} = \sqrt{25/25} = 1$. Reconstructing $v$ via $\|v\|e$ gives $5 \cdot (3/5, 4/5) = (3, 4)$, which restores the original vector. Normalization changes the length of the vector from 5 to 1, while keeping its direction and orientation completely unchanged because the scaling factor $1/5$ is positive.

**Show on screen:** The factorization $v = \|v\|e = 5 \cdot (3/5, 4/5)$ and the unit norm check.

**If asked to go deeper:** The unit vector $e$ represents a point on the unit sphere $S^1$, separating the directional degrees of freedom from the 1-dimensional radial scaling.

---

## Exercise 4 — verbal script

**Key idea:** Testing and establishing vector orthogonality using the dot product.

**What to say:**
We evaluate the dot product of $u = (1, 2, -1)$ and $v = (2, -1, 3)$ by multiplying corresponding components and summing them: $(1)(2) + (2)(-1) + (-1)(3) = 2 - 2 - 3 = -3$. Because this scalar is non-zero, $u$ and $v$ are not perpendicular. To find an unknown parameter $a$ such that $w = (2, -1, a)$ is perpendicular to $u$, we enforce the condition $w \cdot u = 0$. This sets up the equation $(2)(1) + (-1)(2) + a(-1) = 0$, which simplifies to $2 - 2 - a = 0$, giving $a = 0$. Plugging $a = 0$ back into $w$, we check that $(2, -1, 0) \cdot (1, 2, -1) = 2 - 2 + 0 = 0$, confirming orthogonality.

**Show on screen:** The dot product calculation showing $-3 \neq 0$, and the linear equation solving for $a = 0$.

**If asked to go deeper:** The set of all vectors perpendicular to $u$ in $\mathbb{R}^3$ forms a 2-dimensional subspace, which is the nullspace of the $1 \times 3$ matrix $u^T$.

---

## Exercise 5 — verbal script

**Key idea:** Predicting angle type from the dot product sign and computing the exact angle.

**What to say:**
We consider $u = (1, 1, 0)$ and $v = (1, 0, 1)$. First, we compute their dot product: $(1)(1) + (1)(0) + (0)(1) = 1$. Because lengths are strictly positive and the dot product is positive ($1 > 0$), $\cos\theta$ must be positive, which allows us to predict immediately that the angle is acute. Next, we compute the lengths of both vectors: $\|u\| = \sqrt{1+1+0} = \sqrt{2}$ and $\|v\| = \sqrt{1+0+1} = \sqrt{2}$. The cosine formula gives $\cos\theta = 1 / (\sqrt{2}\sqrt{2}) = 1/2$. Taking the arccosine, we get $\theta = \pi/3 = 60^\circ$. This confirms our prediction since $60^\circ$ is strictly between $0^\circ$ and $90^\circ$.

**Show on screen:** The sign test $u \cdot v = 1 > 0$ paired with the final angle calculation $\theta = 60^\circ$.

**If asked to go deeper:** The dot product formula $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$ connects the purely algebraic coordinate definition with the geometric definition via the law of cosines.

---

## Exercise 6 — verbal script

**Key idea:** Orthogonal projection onto a line and geometric decomposition.

**What to say:**
We want to project $u = (4, 2)$ onto the direction $v = (1, 1)$. We first compute $u \cdot v = 4 + 2 = 6$ and $\|v\|^2 = 1^2 + 1^2 = 2$. The orthogonal projection is $(u \cdot v / \|v\|^2) v = (6/2)(1, 1) = 3(1, 1) = (3, 3)$. Then we compute the perpendicular residual $r = u - \operatorname{proj}_v u = (4, 2) - (3, 3) = (1, -1)$. Checking the dot product $r \cdot v = (1)(1) + (-1)(1) = 0$ confirms that $r$ is orthogonal to $v$. Geometrically, $(3, 3)$ is the orthogonal shadow of $u$ cast on the diagonal line through $v$, and $r = (1, -1)$ is the perpendicular line segment connecting the projection point to the tip of $u$.

**Show on screen:** The formula $\operatorname{proj}_v u = \frac{u \cdot v}{\|v\|^2}v$ leading to $(3, 3)$, followed by the dot product check $r \cdot v = 0$.

**If asked to go deeper:** The projection operator can be written as matrix multiplication $P = \frac{v v^T}{v^T v}$, which is an idempotent symmetric matrix satisfying $P^2 = P$.

---

## Exercise 7 — verbal script

**Key idea:** Identifying linear dependence by inspecting collinear vectors.

**What to say:**
Given $u = (1, 2, 3)$, $v = (2, 4, 6)$, and $w = (0, 1, 1)$, we examine their coordinates before doing any long calculation. We observe immediately that $v = 2u$, because each component of $v$ is exactly double the component of $u$. This collinearity means $2u - v + 0w = (0, 0, 0)$. By definition, since we found non-zero scalar coefficients $(2, -1, 0)$ that produce the zero vector, the three vectors are linearly dependent. No determinant or Gaussian elimination is required because any set containing two proportional vectors is automatically linearly dependent.

**Show on screen:** The coordinate comparison showing $v = 2u$ and the linear combination $2u - v + 0w = \mathbf{0}$.

**If asked to go deeper:** Geometrically, $u$ and $v$ lie on the same 1D line through the origin, so the subspace spanned by $\{u, v, w\}$ can have dimension at most 2, making three vectors in that span linearly dependent.

---

## Exercise 8 — verbal script

**Key idea:** Expressing a vector as a unique linear combination over an oblique 2D basis.

**What to say:**
We want to express $w = (5, 1)$ as $a u + b v$ with $u = (1, 1)$ and $v = (2, -1)$. Setting up the vector equation gives the system $a + 2b = 5$ and $a - b = 1$. Subtracting the equations yields $3b = 4$, so $b = 4/3$, and substituting back gives $a = 7/3$. Reconstructing $a u + b v$ with these fractions confirms $(7/3)(1, 1) + (4/3)(2, -1) = (15/3, 3/3) = (5, 1)$. Geometrically, because $u$ and $v$ are not collinear, they form a valid basis for $\mathbb{R}^2$. The pair $(a, b) = (7/3, 4/3)$ represents the unique coordinates of $w$ in the skewed coordinate grid defined by axes along $u$ and $v$.

**Show on screen:** The $2 \times 2$ linear system and the reconstruction $(7/3)(1, 1) + (4/3)(2, -1) = (5, 1)$.

**If asked to go deeper:** In matrix form, this solves $\begin{pmatrix} 1 & 2 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$; since the matrix determinant is $-3 \neq 0$, the transformation is invertible and the solution is unique.

---

## Exercise 9 — verbal script

**Key idea:** Calculating cross products, checking orthogonality, and demonstrating anticommutativity.

**What to say:**
We compute $u \times v$ for $u = (1, 2, 0)$ and $v = (0, 1, 3)$ using a $3 \times 3$ determinant with unit basis vectors $\mathbf{i}, \mathbf{j}, \mathbf{k}$ in the first row. Expanding along the top row gives $\mathbf{i}(6 - 0) - \mathbf{j}(3 - 0) + \mathbf{k}(1 - 0) = (6, -3, 1)$. We check orthogonality using dot products: $(6, -3, 1) \cdot (1, 2, 0) = 6 - 6 = 0$, and $(6, -3, 1) \cdot (0, 1, 3) = -3 + 3 = 0$. Next, computing $v \times u$ swaps rows in the determinant, giving $(-6, 3, -1)$. Comparing the results reveals $v \times u = -(u \times v)$, verifying that the cross product is anticommutative.

**Show on screen:** The determinant expansion for $u \times v$, the dot product checks, and the sign inversion for $v \times u$.

**If asked to go deeper:** The cross product is a Lie bracket on $\mathbb{R}^3$, making $(\mathbb{R}^3, \times)$ isomorphic to the Lie algebra $\mathfrak{so}(3)$ of skew-symmetric matrices.

---

## Exercise 10 — verbal script

**Key idea:** Calculating parallelogram and triangle area using the cross product.

**What to say:**
Given points $A = (0,0,0)$, $B = (2,1,0)$, and $C = (1,3,2)$, we first construct vectors $\overrightarrow{AB} = (2, 1, 0)$ and $\overrightarrow{AC} = (1, 3, 2)$. Their cross product is $\overrightarrow{AB} \times \overrightarrow{AC} = (2, -4, 5)$. The area of the parallelogram spanned by these two vectors is the length of their cross product: $\sqrt{2^2 + (-4)^2 + 5^2} = \sqrt{45} = 3\sqrt{5}$. The area of $\triangle ABC$ is half of the parallelogram area, giving $3\sqrt{5}/2$. The factor of $1/2$ appears because the diagonal $BC$ splits the parallelogram into two congruent triangles of identical base and height.

**Show on screen:** The cross product vector $(2, -4, 5)$, its norm $\sqrt{45} = 3\sqrt{5}$, and the division by 2 for the triangle.

**If asked to go deeper:** The length $\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\|\|\mathbf{v}\|\sin\theta$ corresponds directly to base times height, which is the geometric formula for parallelogram area.

---

## Exercise 11 — verbal script

**Key idea:** Decomposing a vector into parallel and perpendicular components with independent validation.

**What to say:**
We decompose $u = (3, 4)$ with respect to $v = (1, 2)$. The dot product is $u \cdot v = 3 + 8 = 11$, and $\|v\|^2 = 5$. The parallel component is $u_\parallel = (11/5)(1, 2) = (11/5, 22/5)$. The perpendicular component is $u_\perp = u - u_\parallel = (4/5, -2/5)$. We perform two checks: first, $u_\parallel + u_\perp = (15/5, 20/5) = (3, 4) = u$, confirming algebraic completeness; second, $u_\perp \cdot v = 4/5 - 4/5 = 0$, confirming orthogonality. These checks are independent because many vector pairs sum to $u$ without being orthogonal to $v$, and many vectors are orthogonal to $v$ without summing to $u$.

**Show on screen:** The components $u_\parallel = (11/5, 22/5)$ and $u_\perp = (4/5, -2/5)$, followed by both independent verification checks.

**If asked to go deeper:** This decomposition is the base case of the Gram-Schmidt orthogonalization process used to build orthonormal bases.

---

## Exercise 12 — verbal script

**Key idea:** Constructing a normal vector to a plane from three non-collinear points.

**What to say:**
We are given three points $A = (1, 0, 2)$, $B = (2, 1, 0)$, and $C = (0, 3, 1)$. We find two vectors lying in the plane by taking differences: $\overrightarrow{AB} = (1, 1, -2)$ and $\overrightarrow{AC} = (-1, 3, -1)$. To find a vector perpendicular to both, we compute their cross product: $\mathbf{i}(-1+6) - \mathbf{j}(-1-2) + \mathbf{k}(3+1) = (5, 3, 4)$. We verify perpendicularity using dot products: $(5, 3, 4) \cdot (1, 1, -2) = 5 + 3 - 8 = 0$, and $(5, 3, 4) \cdot (-1, 3, -1) = -5 + 9 - 4 = 0$. This vector $(5, 3, 4)$ acts as the normal vector for the entire plane containing $A, B, C$.

**Show on screen:** The two displacement vectors, their cross product $(5, 3, 4)$, and the two zero dot products.

**If asked to go deeper:** The Cartesian equation of this plane is $5(x-1) + 3(y-0) + 4(z-2) = 0$, which simplifies to $5x + 3y + 4z = 13$.

---

## Exercise 13 — verbal script

**Key idea:** Testing coplanarity of four points using the scalar triple product.

**What to say:**
We are given four points: $A = (0,0,0)$, $B = (1,2,0)$, $C = (0,1,1)$, and $D = (2,5,1)$. We construct $\overrightarrow{AB} = (1, 2, 0)$ and $\overrightarrow{AC} = (0, 1, 1)$. Their cross product produces the normal vector $n = (2, -1, 1)$. Next, we construct $\overrightarrow{AD} = (2, 5, 1)$ and evaluate the dot product $\overrightarrow{AD} \cdot n = (2)(2) + (5)(-1) + (1)(1) = 4 - 5 + 1 = 0$. Because $\overrightarrow{AD} \cdot n = 0$, displacement $\overrightarrow{AD}$ is perpendicular to the normal, which proves that point $D$ lies in the plane of $A, B, C$. The underlying criterion is that the volume of the parallelepiped spanned by the three vectors is zero, which occurs if and only if the vectors are coplanar.

**Show on screen:** The normal vector $n = (2, -1, 1)$, the dot product $\overrightarrow{AD} \cdot n = 0$, and the geometric conclusion.

**If asked to go deeper:** This test is equivalent to evaluating the single $3 \times 3$ determinant formed by the coordinates of $\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}$, known as the scalar triple product.

---

## Exercise 14 — verbal script

**Key idea:** Finding the closest point on a line and point-to-line distance using orthogonal projection.

**What to say:**
We want to find the closest point on the line through the origin with direction $v = (1, 2)$ to the point $P = (4, 1)$. The position vector is $p = (4, 1)$. We project $p$ onto $v$: $p \cdot v = 4 + 2 = 6$, and $\|v\|^2 = 5$, giving projection point $Q = (6/5)(1, 2) = (6/5, 12/5) = (1.2, 2.4)$. The vector from $Q$ to $P$ is $(4 - 6/5, 1 - 12/5) = (14/5, -7/5)$. The shortest distance is its norm: $\sqrt{(14/5)^2 + (-7/5)^2} = \sqrt{245/25} = 7\sqrt{5}/5$. Finally, we verify that $\overrightarrow{QP} \cdot v = (14/5)(1) + (-7/5)(2) = 0$, confirming that the shortest line from a point to a line meets it at a right angle.

**Show on screen:** The projection point $Q = (1.2, 2.4)$, the distance $7\sqrt{5}/5$, and the orthogonality check $\overrightarrow{QP} \cdot v = 0$.

**If asked to go deeper:** This minimizes the quadratic distance function $f(t) = \|P - tv\|^2$, where setting the derivative with respect to $t$ to zero reproduces the projection formula.

---

## Exercise 15 — verbal script

**Key idea:** Measuring pure direction with cosine and explaining scale invariance.

**What to say:**
Given $a = (1, 2, 1)$, $b = (2, 4, 2)$, and $c = (2, 0, 3)$, we compute lengths: $\|a\| = \sqrt{6}$, $\|b\| = 2\sqrt{6}$, and $\|c\| = \sqrt{13}$. For pair $(a, b)$, the cosine is $12 / (\sqrt{6} \cdot 2\sqrt{6}) = 12/12 = 1$, giving an angle of $0^\circ$. For $(a, c)$, the cosine is $5 / \sqrt{78} \approx 0.5661$, giving $\approx 55.52^\circ$. For $(b, c)$, the cosine is $10 / (2\sqrt{6}\sqrt{13}) = 5/\sqrt{78}$, giving the identical angle $\approx 55.52^\circ$. Ordering by increasing angle yields $(a, b) < (a, c) = (b, c)$. The value for $(a, b)$ is 1 despite differing lengths because $b = 2a$: the cosine formula normalizes both vectors into unit vectors, making the measure depend solely on direction and orientation rather than magnitude.

**Show on screen:** The three cosine calculations, the angular ordering, and the normalization formula $\mathbf{e}_a \cdot \mathbf{e}_b = 1$.

**If asked to go deeper:** The quantity $\frac{u \cdot v}{\|u\|\|v\|}$ is the cosine similarity metric commonly used in high-dimensional data analysis and machine learning to compare orientations irrespective of scale.


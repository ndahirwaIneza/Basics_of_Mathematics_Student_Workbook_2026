# Exercise 4

**Problem:** Find $A^{-1}$ using the Gauss–Jordan method for
$$A=\begin{pmatrix}1&2\\3&5\end{pmatrix}.$$
Show the augmented matrix $[A\mid I]$ after successive operations and explain why obtaining $I$ on the left gives the inverse on the right.

---

## Relevant theorem / definition

The Gauss–Jordan inversion method transforms the augmented matrix $[A \mid I]$ into $[I \mid A^{-1}]$ using elementary row operations:
$$
[A \mid I] \xrightarrow{\text{row operations}} [I \mid A^{-1}]
$$
Each row operation corresponds to multiplying on the left by an elementary matrix $E_k$. If $E_k \cdots E_1 A = I$, then $E = E_k \cdots E_1 = A^{-1}$, and applying the same operations to $I$ yields $E I = A^{-1}$.

---

## Solution

The initial augmented matrix is:
$$
[A \mid I] = \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 5 & 0 & 1 \end{array}\right]
$$

Step 1: Eliminate the entry in position $(2,1)$ using pivot $(1,1) = 1$:
Apply $R_2 \leftarrow R_2 - 3R_1$:
$$
R_2 - 3R_1 = \left[\begin{array}{cc|cc} 3 - 3(1) & 5 - 3(2) & 0 - 3(1) & 1 - 3(0) \end{array}\right] = \left[\begin{array}{cc|cc} 0 & -1 & -3 & 1 \end{array}\right]
$$
The augmented matrix becomes:
$$
\left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & -1 & -3 & 1 \end{array}\right]
$$

Step 2: Scale row 2 to make the pivot equal to $+1$:
Apply $R_2 \leftarrow -1 \cdot R_2$:
The augmented matrix becomes:
$$
\left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & 3 & -1 \end{array}\right]
$$

Step 3: Eliminate the entry in position $(1,2)$ using pivot $(2,2) = 1$:
Apply $R_1 \leftarrow R_1 - 2R_2$:
$$
R_1 - 2R_2 = \left[\begin{array}{cc|cc} 1 - 2(0) & 2 - 2(1) & 1 - 2(3) & 0 - 2(-1) \end{array}\right] = \left[\begin{array}{cc|cc} 1 & 0 & -5 & 2 \end{array}\right]
$$
The augmented matrix is now in reduced row echelon form:
$$
\left[\begin{array}{cc|cc} 1 & 0 & -5 & 2 \\ 0 & 1 & 3 & -1 \end{array}\right]
$$

Reading the right-hand block gives:
$$
A^{-1} = \begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix}
$$

Explanation of why $I$ on the left yields $A^{-1}$ on the right:
Every elementary row operation is equivalent to multiplying the entire augmented matrix from the left by an elementary matrix $E_i$. The complete sequence of operations represents multiplication by a combined invertible matrix $E = E_m \cdots E_2 E_1$.
Applying this to the partitioned block matrix:
$$
E [A \mid I] = [EA \mid EI]
$$
Because the reduction transforms the left block into the identity matrix, we have $EA = I$, which by definition means $E = A^{-1}$. The right block simultaneously transforms into $EI = E = A^{-1}$, directly producing the inverse matrix.

---

## Result

$$
A^{-1} = \begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Verification by multiplication $A A^{-1}$:
$$
A A^{-1} = \begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix} \begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix} = \begin{pmatrix} 1(-5)+2(3) & 1(2)+2(-1) \\ 3(-5)+5(3) & 3(2)+5(-1) \end{pmatrix} = \begin{pmatrix} -5+6 & 2-2 \\ -15+15 & 6-5 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

**Pass 2 — Numerical check:** Check via the $2 \times 2$ formula:
$\det(A) = 1(5) - 2(3) = 5 - 6 = -1$.
$$
A^{-1} = \frac{1}{-1} \begin{pmatrix} 5 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix}
$$
Matches the Gauss–Jordan result.

**Pass 3 — Consistency check:** Check reverse product $A^{-1} A$:
$$
A^{-1} A = \begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix} = \begin{pmatrix} -5+6 & -10+10 \\ 3-3 & 6-5 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

---

## Exam tip

In Gauss–Jordan, always work in two phases: first eliminate downwards to obtain an upper triangular matrix, then eliminate upwards to obtain the identity matrix.


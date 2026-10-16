# Exercise 14

**Problem:** Assume that a square matrix $A$ satisfies
$$A^2=I.$$
Show that
$$A^{-1}=A.$$
Then give an example of a $2\times2$ matrix different from $I$ and $-I$ that satisfies this condition, and verify it by multiplication.

---

## Relevant theorem / definition

A square matrix $A$ such that $A^2 = I$ is called an involution (or an involutory matrix). By definition, if a matrix $B$ satisfies $AB = BA = I$, then $B$ is the unique inverse of $A$.

---

## Solution

1. Proof that $A^{-1} = A$:
   We are given the condition:
   $$
   A^2 = I
   $$
   By the definition of matrix powers, $A^2 = A \cdot A$. Substituting this gives:
   $$
   A \cdot A = I
   $$
   By the definition of the matrix inverse, a matrix $B$ is the inverse of $A$ if $A B = B A = I$. Setting $B = A$, we have:
   $$
   A \cdot A = I
   $$
   Because the inverse of an invertible matrix is unique, it follows directly from the definition that $A$ is invertible and its inverse is $A$ itself:
   $$
   A^{-1} = A
   $$

2. Example of a $2 \times 2$ involutory matrix different from $I$ and $-I$:
   Some reflections are involutions, but not every involution is a Euclidean reflection. Applying any involution twice returns every vector to its starting value. Consider the reflection matrix across the line $y = x$ (which swaps the coordinate axes):
   $$
   A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
   $$
   Note that $A \neq I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and $A \neq -I = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$.

3. Verification by multiplication:
   $$
   \begin{align}
   A^2 &= \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \\
   &= \begin{pmatrix} 0(0) + 1(1) & 0(1) + 1(0) \\ 1(0) + 0(1) & 1(1) + 0(0) \end{pmatrix} \\
   &= \begin{pmatrix} 0 + 1 & 0 + 0 \\ 0 + 0 & 1 + 0 \end{pmatrix} \\
   &= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
   \end{align}
   $$
   Since $A^2 = I$, we confirm that $A^{-1} = A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

---

## Result

$$
A^2 = I \implies A \cdot A = I \implies A^{-1} = A
$$

$$
\text{Example: } A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad A \neq \pm I, \quad A^2 = I
$$

---

## Verification

**Pass 1 — Algebraic check:** Determinant of an involution: $\det(A^2) = (\det A)^2 = \det(I) = 1 \implies \det A = \pm 1$. For our example $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $\det A = 0(0) - 1(1) = -1$, which is consistent with $\det A = \pm 1$.

**Pass 2 — Numerical check:** Alternative reflection example: $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (reflection across the $x$-axis).
$$
A^2 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$
This provides a second valid example confirming the theorem.

**Pass 3 — Consistency check:** Since $A = A^{-1}$, the eigenvalues of $A$ must satisfy $\lambda = \lambda^{-1} \implies \lambda^2 = 1 \implies \lambda = \pm 1$. The eigenvalues of $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ are $+1$ and $-1$.

---

## Exam tip

Matrices satisfying $A^2 = I$ are involutions: applying the operation twice returns every vector to its initial position. The chosen coordinate-swap matrix is specifically a reflection.

# Exercise 7

**Problem:** For
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}2&0\\0&3\end{pmatrix}$$
compute $(AB)^{-1}$ and $B^{-1}A^{-1}$. Check that the results are the same and explain the meaning of the reversed order.

---

## Relevant theorem / definition

For any invertible matrices $A$ and $B$ of the same size, the inverse of their product is the product of their inverses in reverse order:
$$
(AB)^{-1} = B^{-1} A^{-1}
$$

---

## Solution

The given matrices are:
$$
A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}
$$

1. Computation of $(AB)^{-1}$:
   Compute $AB$:
   $$
   AB = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 1(2)+1(0) & 1(0)+1(3) \\ 0(2)+1(0) & 0(0)+1(3) \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ 0 & 3 \end{pmatrix}
   $$
   Compute the determinant of $AB$:
   $$
   \det(AB) = 2(3) - 3(0) = 6
   $$
   Invert using the $2 \times 2$ formula:
   $$
   (AB)^{-1} = \frac{1}{6} \begin{pmatrix} 3 & -3 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \end{pmatrix}
   $$

2. Computation of $B^{-1}A^{-1}$:
   Invert $B$ (diagonal matrix):
   $$
   B^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{3} \end{pmatrix}
   $$
   Invert $A$ (shear matrix):
   $$
   A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}
   $$
   Compute the product $B^{-1}A^{-1}$:
   $$
   B^{-1}A^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{3} \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2}(1) + 0 & \frac{1}{2}(-1) + 0 \\ 0 + \frac{1}{3}(0) & 0 + \frac{1}{3}(1) \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \end{pmatrix}
   $$

3. Comparison and explanation of reversed order:
   Both computations give the exact same matrix:
   $$
   (AB)^{-1} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \end{pmatrix} = B^{-1}A^{-1}
   $$
   Meaning of the reversed order:
   When transforming a vector $\mathbf{x}$ by $AB$, the transformation $B$ acts first, followed by $A$:
   $$
   \mathbf{y} = A(B\mathbf{x})
   $$
   To undo this composite process and recover $\mathbf{x}$ from $\mathbf{y}$, we must first undo the last transformation that was performed ($A$) by applying $A^{-1}$, yielding $B\mathbf{x} = A^{-1}\mathbf{y}$. Only then can we undo the initial transformation ($B$) by applying $B^{-1}$, giving $\mathbf{x} = B^{-1}(A^{-1}\mathbf{y})$.
   Algebraically, when we multiply $(AB)$ by $(B^{-1}A^{-1})$, the inner terms cancel first:
   $$
   (AB)(B^{-1}A^{-1}) = A(B B^{-1})A^{-1} = A I A^{-1} = A A^{-1} = I
   $$
   If the order were not reversed, $A^{-1}B^{-1}$ would leave $A B A^{-1} B^{-1}$, which does not simplify to $I$ because matrices do not commute.

---

## Result

$$
(AB)^{-1} = B^{-1}A^{-1} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \end{pmatrix}
$$

---

## Verification

**Pass 1 — Algebraic check:** Verify $(AB)(B^{-1}A^{-1}) = I$:
$$
\begin{pmatrix} 2 & 3 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \end{pmatrix} = \begin{pmatrix} 2(1/2)+3(0) & 2(-1/2)+3(1/3) \\ 0(1/2)+3(0) & 0(-1/2)+3(1/3) \end{pmatrix} = \begin{pmatrix} 1 & -1+1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

**Pass 2 — Numerical check:** Compute the incorrect order $A^{-1}B^{-1}$:
$$
A^{-1}B^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1/2 & 0 \\ 0 & 1/3 \end{pmatrix} = \begin{pmatrix} 1/2 & -1/3 \\ 0 & 1/3 \end{pmatrix} \neq (AB)^{-1}
$$
Entry $(1,2)$ is $-1/3 \neq -1/2$, proving that the reversed order is essential.

**Pass 3 — Consistency check:** Determinant check: $\det((AB)^{-1}) = \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6} = \frac{1}{\det(AB)}$.

---

## Exam tip

Remember the "socks and shoes" rule: $(AB)^{-1} = B^{-1}A^{-1}$; the operation applied last must be undone first.


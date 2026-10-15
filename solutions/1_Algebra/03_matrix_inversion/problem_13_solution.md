# Exercise 13

**Problem:** The matrices
$$S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad H=\begin{pmatrix}1&1\\0&1\end{pmatrix}$$
describe nonuniform scaling and shear. For $T=HS$, find $T^{-1}$ in two ways:

1. first compute $T$, then its inverse,
2. use $(HS)^{-1}=S^{-1}H^{-1}$.

Compare the results. Additionally compute $H^{-1}S^{-1}$ and verify that the incorrect order gives a different matrix. Explain the rule: “when undoing a composition of operations, we undo them from the end.”

---

## Relevant theorem / definition

For invertible square matrices $A$ and $B$, the inverse of their product requires reversing the order of the inverse factors:
$$
(AB)^{-1} = B^{-1} A^{-1}
$$
In general, $B^{-1} A^{-1} \neq A^{-1} B^{-1}$ when $A$ and $B$ do not commute.

---

## Solution

The given matrices are:
$$
S = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}, \qquad H = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}
$$

1. Method 1 — Compute $T$ first, then invert:
   $$
   T = HS = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(2)+1(0) & 1(0)+1(1) \\ 0(2)+1(0) & 0(0)+1(1) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}
   $$
   Compute the determinant of $T$:
   $$
   \det(T) = 2(1) - 1(0) = 2
   $$
   Apply the $2 \times 2$ inverse formula:
   $$
   T^{-1} = \frac{1}{2} \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & 1 \end{pmatrix}
   $$

2. Method 2 — Use $(HS)^{-1} = S^{-1}H^{-1}$:
   Compute $S^{-1}$ and $H^{-1}$:
   $$
   S^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix}, \qquad H^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}
   $$
   Multiply in reverse order ($S^{-1} H^{-1}$):
   $$
   S^{-1} H^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2}(1)+0 & \frac{1}{2}(-1)+0 \\ 0+1(0) & 0+1(1) \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & 1 \end{pmatrix}
   $$
   Both methods yield the identical matrix.

3. Computing the incorrect order $H^{-1}S^{-1}$:
   $$
   H^{-1}S^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1\left(\frac{1}{2}\right)+0 & 0+(-1)(1) \\ 0+0 & 0+1(1) \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -1 \\ 0 & 1 \end{pmatrix}
   $$
   Notice that:
   $$
   H^{-1}S^{-1} = \begin{pmatrix} \frac{1}{2} & -1 \\ 0 & 1 \end{pmatrix} \neq \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & 1 \end{pmatrix} = T^{-1}
   $$

4. Explanation of the rule:
   In the composite mapping $T\mathbf{x} = H(S\mathbf{x})$, the transformation $S$ acts first on $\mathbf{x}$, and the transformation $H$ acts second on the result. To undo this composition, the last operation applied ($H$) must be undone first by applying $H^{-1}$. This returns the intermediate state $S\mathbf{x}$. Only then can the first operation ($S$) be undone by applying $S^{-1}$. Reversing the order of inversion is mandatory because transformations do not commute: undoing them in the forward order attempts to invert the initial operation while the distorting effects of the later operation are still active.

---

## Result

$$
T^{-1} = (HS)^{-1} = S^{-1}H^{-1} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & 1 \end{pmatrix}
$$

$$
H^{-1}S^{-1} = \begin{pmatrix} \frac{1}{2} & -1 \\ 0 & 1 \end{pmatrix} \neq T^{-1}
$$

---

## Verification

**Pass 1 — Algebraic check:** Verify $T T^{-1} = I$:
$$
T T^{-1} = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2(1/2)+1(0) & 2(-1/2)+1(1) \\ 0(1/2)+1(0) & 0(-1/2)+1(1) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$

**Pass 2 — Numerical check:** Check the incorrect order product $T (H^{-1}S^{-1})$:
$$
\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} \frac{1}{2} & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -2 + 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \neq I
$$
The product fails to produce the identity matrix, confirming $H^{-1}S^{-1}$ is not the inverse.

**Pass 3 — Consistency check:** Both $S$ and $H$ are upper triangular, so their product $T$ is upper triangular. The inverse of an upper triangular matrix must also be upper triangular, with diagonal entries equal to the reciprocals of the diagonal entries of $T$: $\frac{1}{2}$ and $1$.

---

## Exam tip

When inverting a chain of operations, always reverse the sequence: $(A B C)^{-1} = C^{-1} B^{-1} A^{-1}$.


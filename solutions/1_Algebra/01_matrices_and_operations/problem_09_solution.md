# Exercise 9

**Problem:** Let
$$S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.$$
The matrix $S$ describes nonuniform scaling, while $R$ describes a $90^\circ$ counterclockwise rotation.
For
$$x=\begin{pmatrix}1\\2\end{pmatrix}$$
compute $RSx$ and $SRx$. Compare the results and explain geometrically why the order of these transformations matters.

---

## Relevant theorem / definition

For linear maps represented by matrices, composition of maps corresponds to matrix multiplication: $(T_2 \circ T_1)(x) = T_2(T_1(x)) = (M_2 M_1)x$, applied from right to left. Noncommutativity of matrices reflects the order dependence of geometric transformations.

---

## Solution

1. Computation of $RSx$:
   Apply scaling $S$ to $x$ first:
   $$
   Sx = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2(1) + 0(2) \\ 0(1) + 1(2) \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \end{pmatrix}
   $$
   Now apply rotation $R$ to the result:
   $$
   RSx = R(Sx) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 \\ 2 \end{pmatrix} = \begin{pmatrix} 0(2) - 1(2) \\ 1(2) + 0(2) \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \end{pmatrix}
   $$

2. Computation of $SRx$:
   Apply rotation $R$ to $x$ first:
   $$
   Rx = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 0(1) - 1(2) \\ 1(1) + 0(2) \end{pmatrix} = \begin{pmatrix} -2 \\ 1 \end{pmatrix}
   $$
   Now apply scaling $S$ to the result:
   $$
   SRx = S(Rx) = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(-2) + 0(1) \\ 0(-2) + 1(1) \end{pmatrix} = \begin{pmatrix} -4 \\ 1 \end{pmatrix}
   $$

3. Comparison:
   $$
   RSx = \begin{pmatrix} -2 \\ 2 \end{pmatrix} \neq \begin{pmatrix} -4 \\ 1 \end{pmatrix} = SRx
   $$

4. Geometric explanation:
   The scaling $S$ stretches vectors specifically along the coordinate $x$-axis by a factor of 2 while leaving the $y$-axis unchanged.
   - In $RSx$, the initial vector $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ has its $x$-component doubled to become $\begin{pmatrix} 2 \\ 2 \end{pmatrix}$. The subsequent $90^\circ$ counterclockwise rotation sends this stretched $x$-component into the $y$-direction, resulting in $\begin{pmatrix} -2 \\ 2 \end{pmatrix}$.
   - In $SRx$, the vector is rotated $90^\circ$ first, mapping $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ to $\begin{pmatrix} -2 \\ 1 \end{pmatrix}$. The original $y$-component (2) is now on the negative $x$-axis (as $-2$). When $S$ is applied, it stretches this newly positioned $x$-component by 2 to get $-4$, while leaving the $y$-component at 1.
   Because nonuniform scaling acts along fixed Cartesian axes, rotating before scaling changes which geometric part of the vector undergoes stretching.

---

## Result

$$
RSx = \begin{pmatrix} -2 \\ 2 \end{pmatrix}, \qquad SRx = \begin{pmatrix} -4 \\ 1 \end{pmatrix}, \qquad RSx \neq SRx
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the matrix products directly:
$$
RS = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 2 & 0 \end{pmatrix} \implies (RS)x = \begin{pmatrix} 0 & -1 \\ 2 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \end{pmatrix}
$$
$$
SR = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix} \implies (SR)x = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} -4 \\ 1 \end{pmatrix}
$$

**Pass 2 — Numerical check:** Norm check: $\|x\|^2 = 1^2 + 2^2 = 5$. Since $R$ is an isometry (orthogonal matrix), $\|Rx\|^2 = (-2)^2 + 1^2 = 5$. Scaling then gives $\|SRx\|^2 = (-4)^2 + 1^2 = 17$. For $RSx$, $\|Sx\|^2 = 2^2 + 2^2 = 8$, and rotation preserves norm: $\|RSx\|^2 = (-2)^2 + 2^2 = 8$. Since $8 \neq 17$, the two vectors cannot be equal.

**Pass 3 — Consistency check:** The determinants are $\det(S) = 2$ and $\det(R) = 1$. Both composite transformations scale area by $\det(RS) = \det(SR) = 2$, but their action on individual directional vectors differs.

---

## Exam tip

Geometric transformations apply from right to left: in $RSx$, $S$ acts first, followed by $R$.


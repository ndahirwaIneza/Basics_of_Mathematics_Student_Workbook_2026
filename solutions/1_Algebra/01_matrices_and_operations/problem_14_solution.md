# Exercise 14

**Problem:** The matrix for a rotation through an angle $\theta$ is
$$R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}.$$
Compute $R(\alpha)R(\beta)$ and, using the angle-sum formulas for sine and cosine, show that
$$R(\alpha)R(\beta)=R(\alpha+\beta).$$
Explain the result geometrically.

---

## Relevant theorem / definition

The trigonometric angle-sum identities state that:
$$
\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta
$$
$$
\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta
$$
A planar rotation matrix $R(\theta)$ rotates any vector $\mathbf{v} \in \mathbb{R}^2$ counterclockwise around the origin by an angle $\theta$.

---

## Solution

The matrices for rotations by $\alpha$ and $\beta$ are:
$$
R(\alpha) = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}, \qquad R(\beta) = \begin{pmatrix} \cos\beta & -\sin\beta \\ \sin\beta & \cos\beta \end{pmatrix}
$$

Compute the matrix product $R(\alpha)R(\beta)$:
$$
\begin{align}
R(\alpha)R(\beta) &= \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix} \begin{pmatrix} \cos\beta & -\sin\beta \\ \sin\beta & \cos\beta \end{pmatrix} \\
&= \begin{pmatrix} \cos\alpha\cos\beta - \sin\alpha\sin\beta & -\cos\alpha\sin\beta - \sin\alpha\cos\beta \\ \sin\alpha\cos\beta + \cos\alpha\sin\beta & -\sin\alpha\sin\beta + \cos\alpha\cos\beta \end{pmatrix} \\
&= \begin{pmatrix} \cos\alpha\cos\beta - \sin\alpha\sin\beta & -(\sin\alpha\cos\beta + \cos\alpha\sin\beta) \\ \sin\alpha\cos\beta + \cos\alpha\sin\beta & \cos\alpha\cos\beta - \sin\alpha\sin\beta \end{pmatrix}
\end{align}
$$

Substitute the angle-sum identities:
- Entry $(1,1)$: $\cos\alpha\cos\beta - \sin\alpha\sin\beta = \cos(\alpha+\beta)$
- Entry $(1,2)$: $-(\sin\alpha\cos\beta + \cos\alpha\sin\beta) = -\sin(\alpha+\beta)$
- Entry $(2,1)$: $\sin\alpha\cos\beta + \cos\alpha\sin\beta = \sin(\alpha+\beta)$
- Entry $(2,2)$: $\cos\alpha\cos\beta - \sin\alpha\sin\beta = \cos(\alpha+\beta)$

Thus:
$$
R(\alpha)R(\beta) = \begin{pmatrix} \cos(\alpha+\beta) & -\sin(\alpha+\beta) \\ \sin(\alpha+\beta) & \cos(\alpha+\beta) \end{pmatrix} = R(\alpha+\beta)
$$

Geometric explanation:
The matrix product $R(\alpha)R(\beta)$ represents applying a counterclockwise rotation by $\beta$ followed by a counterclockwise rotation by $\alpha$ about the origin. Successive rotations around the same fixed point in the two-dimensional plane add their respective angles together, producing an overall net rotation of $\alpha + \beta$. Furthermore, since $(\alpha + \beta) = (\beta + \alpha)$, planar rotations commute: $R(\alpha)R(\beta) = R(\beta)R(\alpha) = R(\alpha+\beta)$.

---

## Result

$$
R(\alpha)R(\beta) = \begin{pmatrix} \cos(\alpha+\beta) & -\sin(\alpha+\beta) \\ \sin(\alpha+\beta) & \cos(\alpha+\beta) \end{pmatrix} = R(\alpha+\beta)
$$

---

## Verification

**Pass 1 — Algebraic check:** Identity check: $R(\alpha)R(-\alpha) = R(\alpha - \alpha) = R(0) = \begin{pmatrix} \cos 0 & -\sin 0 \\ \sin 0 & \cos 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$. This confirms that $R(-\alpha) = R(\alpha)^{-1} = R(\alpha)^T$, the defining property of the special orthogonal group $\text{SO}(2)$.

**Pass 2 — Numerical check:** Let $\alpha = 90^\circ$ and $\beta = 90^\circ$:
$$
R(90^\circ) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \implies R(90^\circ)^2 = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = R(180^\circ)
$$
Matches $R(90^\circ + 90^\circ) = R(180^\circ)$.

**Pass 3 — Consistency check:** Determinant check: $\det(R(\theta)) = \cos^2\theta + \sin^2\theta = 1$. The product gives $\det(R(\alpha)R(\beta)) = \det(R(\alpha))\det(R(\beta)) = 1 \cdot 1 = 1$, and $\det(R(\alpha+\beta)) = \cos^2(\alpha+\beta) + \sin^2(\alpha+\beta) = 1$.

---

## Exam tip

Rotations in 2D commute because they share the same axis of rotation (the origin), meaning $R(\alpha)R(\beta) = R(\beta)R(\alpha) = R(\alpha+\beta)$.


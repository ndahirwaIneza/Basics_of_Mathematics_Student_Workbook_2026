# Exercise 8

**Problem:** Check whether $w=(5,1)$ can be written as
$$w=au+bv,$$
where $u=(1,1)$ and $v=(2,-1)$. If so, find $a,b$, reconstruct $w$ from them, and explain the geometric meaning of the existence of such coefficients.

---

## Relevant theorem / definition

A vector $\mathbf{w}$ is a linear combination of vectors $\mathbf{u}$ and $\mathbf{v}$ if there exist scalars $a, b \in \mathbb{R}$ such that $\mathbf{w} = a\mathbf{u} + b\mathbf{v}$. In $\mathbb{R}^2$, two non-collinear vectors form a basis:
$$
\det\begin{pmatrix} \mathbf{u} & \mathbf{v} \end{pmatrix} \neq 0.
$$
If vectors $\mathbf{u}, \mathbf{v}$ form a basis for $\mathbb{R}^2$, every vector $\mathbf{w} \in \mathbb{R}^2$ can be expressed uniquely as a linear combination of $\mathbf{u}$ and $\mathbf{v}$.

---

## Solution

1. Setting up the vector equation:
   $$
   a(1, 1) + b(2, -1) = (5, 1)
   $$
   This yields the linear system:
   $$
   \begin{cases}
   a + 2b = 5 \\
   a - b = 1
   \end{cases}
   $$

2. Solving the system:
   Subtract the second equation from the first:
   $$
   (a + 2b) - (a - b) = 5 - 1 \implies 3b = 4 \implies b = \frac{4}{3}
   $$
   Substitute $b = \frac{4}{3}$ into the second equation:
   $$
   a = 1 + b = 1 + \frac{4}{3} = \frac{7}{3}
   $$

3. Reconstructing $w$ from $a$ and $b$:
   $$
   a u + b v = \frac{7}{3}(1, 1) + \frac{4}{3}(2, -1) = \left(\frac{7}{3} + \frac{8}{3}, \frac{7}{3} - \frac{4}{3}\right) = \left(\frac{15}{3}, \frac{3}{3}\right) = (5, 1) = w
   $$

4. Geometric meaning:
   The vectors $u$ and $v$ point in different directions:
   $$
   \det\begin{pmatrix} 1 & 2 \\ 1 & -1 \end{pmatrix} = (1)(-1) - (2)(1) = -3 \neq 0
   $$
   Thus, $\{u, v\}$ forms an oblique basis for the plane $\mathbb{R}^2$. The existence and uniqueness of the pair $(a, b) = \left(\frac{7}{3}, \frac{4}{3}\right)$ means that $w$ can be uniquely located in the grid spanned by $u$ and $v$ by taking a displacement of $\frac{7}{3}$ units along the direction of $u$ followed by a displacement of $\frac{4}{3}$ units along the direction of $v$.

---

## Result

$$
a = \frac{7}{3}, \qquad b = \frac{4}{3}
$$

$$
w = \frac{7}{3}(1, 1) + \frac{4}{3}(2, -1) = (5, 1)
$$

---

## Verification

**Pass 1 — Algebraic check:** Using Cramer's rule:
$$
D = \begin{vmatrix} 1 & 2 \\ 1 & -1 \end{vmatrix} = -3, \quad D_a = \begin{vmatrix} 5 & 2 \\ 1 & -1 \end{vmatrix} = -5 - 2 = -7, \quad D_b = \begin{vmatrix} 1 & 5 \\ 1 & 1 \end{vmatrix} = 1 - 5 = -4
$$
$$
a = \frac{D_a}{D} = \frac{-7}{-3} = \frac{7}{3}, \qquad b = \frac{D_b}{D} = \frac{-4}{-3} = \frac{4}{3}
$$

**Pass 2 — Numerical check:** Plugging values into equation 1: $\frac{7}{3} + 2\left(\frac{4}{3}\right) = \frac{7 + 8}{3} = \frac{15}{3} = 5$. Equation 2: $\frac{7}{3} - \frac{4}{3} = \frac{3}{3} = 1$.

**Pass 3 — Consistency check:** Since $\det(u, v) = -3 \neq 0$, the vectors are linearly independent in $\mathbb{R}^2$, guaranteeing that a unique solution must exist for any target vector $w$.

---

## Exam tip

Solve $2 \times 2$ systems by elimination or Cramer's rule, and always plug the fractional values back into both original equations to avoid sign errors.


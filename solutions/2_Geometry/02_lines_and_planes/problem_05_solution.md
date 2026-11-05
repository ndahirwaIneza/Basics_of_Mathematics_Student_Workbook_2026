# Exercise 5

**Problem:** Analyze the position of

$$
L_1:(x,y,z)=(1,1,0)+t(1,2,1),
$$

$$
L_2:(x,y,z)=(2,0,1)+s(0,1,-1).
$$

If they intersect, give the intersection point. If not, determine whether they are parallel or skew. Justify the classification.

---

## Relevant theorem / definition

Two lines in space with directions $\mathbf{d}_1, \mathbf{d}_2$ are:

- parallel (or identical) if $\mathbf{d}_1 \parallel \mathbf{d}_2$;
- intersecting if the directions are not parallel and the system $\mathbf{r}_1(t) = \mathbf{r}_2(s)$ has a solution;
- skew if the directions are not parallel and the system has no solution.

Equivalently, non-parallel lines are coplanar (hence intersecting) if and only if $(P_2 - P_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2) = 0$.

---

## Solution

Step 1 — Parallelism test:

$$
\mathbf{d}_1 = (1,2,1), \qquad \mathbf{d}_2 = (0,1,-1)
$$

If $\mathbf{d}_1 = k\mathbf{d}_2$, the first components would give $1 = 0 \cdot k$, which is impossible. The lines are not parallel.

Step 2 — Intersection test: set the coordinates equal.

$$
\begin{cases}
1 + t = 2 \\
1 + 2t = s \\
t = 1 - s
\end{cases}
$$

From the first equation, $t = 1$. The second gives $s = 1 + 2(1) = 3$. The third requires $t = 1 - 3 = -2$, contradicting $t = 1$.

The system has no solution, so the lines have no common point.

Step 3 — Classification: the directions are not parallel and the lines do not meet, so $L_1$ and $L_2$ are skew.

---

## Result

$$
L_1 \text{ and } L_2 \text{ are skew (not parallel, no common point)}
$$

---

## Verification

**Pass 1 — Algebraic check:** Coplanarity test with $\mathbf{w} = P_2 - P_1 = (2,0,1) - (1,1,0) = (1,-1,1)$:

$$
\mathbf{d}_1 \times \mathbf{d}_2 =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 2 & 1 \\
0 & 1 & -1
\end{vmatrix}
= \mathbf{i}(-2 - 1) - \mathbf{j}(-1 - 0) + \mathbf{k}(1 - 0) = (-3,1,1)
$$

$$
\mathbf{w} \cdot (\mathbf{d}_1 \times \mathbf{d}_2) = 1(-3) + (-1)(1) + 1(1) = -3 \neq 0
$$

The lines are not coplanar, confirming that they are skew.

**Pass 2 — Numerical check:** With $t = 1$ and $s = 3$ (values that satisfy the first two equations), $\mathbf{r}_1(1) = (2,3,1)$ and $\mathbf{r}_2(3) = (2,3,-2)$. The $z$-coordinates differ by $3$, so these candidate points do not coincide.

**Pass 3 — Consistency check:** The distance between skew lines is $\dfrac{|\mathbf{w} \cdot (\mathbf{d}_1 \times \mathbf{d}_2)|}{\|\mathbf{d}_1 \times \mathbf{d}_2\|} = \dfrac{3}{\sqrt{11}} > 0$, which is strictly positive, as expected for lines without a common point.

---

## Exam tip

Always test parallelism first: "no common point" means parallel if the directions are proportional and skew if they are not.


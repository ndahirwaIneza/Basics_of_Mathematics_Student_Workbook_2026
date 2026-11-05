# Exercise 2

**Problem:** Given

$$
L:(x,y,z)=(2,-1,3)+t(1,2,-2).
$$

State a point on the line and its direction vector, check whether $P=(4,3,-1)$ lies on $L$, and find the point corresponding to $t=-1$.

---

## Relevant theorem / definition

The parametric form $\mathbf{r}(t) = \mathbf{r}_0 + t\,\mathbf{d}$ describes the line through the point $\mathbf{r}_0$ (obtained at $t = 0$) with direction $\mathbf{d}$. A point $P$ lies on the line if and only if one single value of $t$ satisfies all coordinate equations simultaneously.

---

## Solution

Point and direction (read off at $t = 0$ and from the coefficient of $t$):

$$
\mathbf{r}_0 = (2,-1,3), \qquad \mathbf{d} = (1,2,-2)
$$

Membership of $P=(4,3,-1)$: solve $\mathbf{r}(t) = P$ coordinate by coordinate.

$$
\begin{cases}
2 + t = 4 \\
-1 + 2t = 3 \\
3 - 2t = -1
\end{cases}
\implies
\begin{cases}
t = 2 \\
t = 2 \\
t = 2
\end{cases}
$$

All three equations give the same value $t = 2$, so $P \in L$.

Point for $t = -1$:

$$
\mathbf{r}(-1) = (2,-1,3) + (-1)(1,2,-2) = (2-1,\ -1-2,\ 3+2) = (1,-3,5)
$$

---

## Result

$$
\mathbf{r}_0 = (2,-1,3), \qquad \mathbf{d} = (1,2,-2)
$$

$$
P = (4,3,-1) \in L \ (t = 2), \qquad \mathbf{r}(-1) = (1,-3,5)
$$

---

## Verification

**Pass 1 — Algebraic check:** $P - \mathbf{r}_0 = (2,4,-4) = 2(1,2,-2) = 2\mathbf{d}$. The vector from the base point to $P$ is a multiple of the direction vector, which is exactly the condition $P \in L$.

**Pass 2 — Numerical check:** $\mathbf{r}(-1) - \mathbf{r}_0 = (1,-3,5) - (2,-1,3) = (-1,-2,2) = -\mathbf{d}$, consistent with $t = -1$.

**Pass 3 — Consistency check:** The points $\mathbf{r}(-1)$, $\mathbf{r}_0$, $P$ correspond to $t = -1, 0, 2$. The distance from $\mathbf{r}_0$ to $P$ should be $2\|\mathbf{d}\| = 2 \cdot 3 = 6$; indeed $\|(2,4,-4)\| = \sqrt{4+16+16} = 6$.

---

## Exam tip

To test whether a point lies on a parametric line, solve for $t$ in every coordinate; one mismatching value of $t$ means the point is not on the line.


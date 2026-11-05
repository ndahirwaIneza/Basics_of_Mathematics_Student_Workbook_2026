# Exercise 8

**Problem:** Find the intersection point of

$$
(x,y,z)=(1,0,2)+t(1,2,-1)
$$

with the plane $x+y+z=4$. Check the result by substituting it into both descriptions.

---

## Relevant theorem / definition

Substituting the parametric coordinates of a line into the plane equation gives one linear equation in $t$. If $\mathbf{n} \cdot \mathbf{v} \neq 0$, it has exactly one solution $t_0$, and the intersection point is $\mathbf{r}(t_0)$.

---

## Solution

Direction test: $\mathbf{n} \cdot \mathbf{v} = (1,1,1) \cdot (1,2,-1) = 1 + 2 - 1 = 2 \neq 0$, so there is exactly one intersection point.

Coordinates of a general point on the line:

$$
x = 1 + t, \qquad y = 2t, \qquad z = 2 - t
$$

Substitute into $x + y + z = 4$:

$$
\begin{align}
(1 + t) + 2t + (2 - t) &= 4 \\
3 + 2t &= 4 \\
t &= \frac{1}{2}
\end{align}
$$

Intersection point:

$$
\mathbf{r}\left(\tfrac12\right) = \left(1 + \tfrac12,\ 2 \cdot \tfrac12,\ 2 - \tfrac12\right) = \left(\tfrac32,\ 1,\ \tfrac32\right)
$$

Check in both descriptions:

- Plane: $\frac32 + 1 + \frac32 = 4$.
- Line: $\left(\frac32, 1, \frac32\right) - (1,0,2) = \left(\frac12, 1, -\frac12\right) = \frac12(1,2,-1)$, a multiple of the direction vector, so the point lies on the line with $t = \frac12$.

---

## Result

$$
\left(\frac{3}{2},\ 1,\ \frac{3}{2}\right) \qquad (t = \tfrac12)
$$

---

## Verification

**Pass 1 — Algebraic check:** Using the general formula $t_0 = \dfrac{d - \mathbf{n} \cdot \mathbf{p}}{\mathbf{n} \cdot \mathbf{v}} = \dfrac{4 - (1 + 0 + 2)}{2} = \dfrac12$, the same parameter value is obtained.

**Pass 2 — Numerical check:** At $t = 0$ the left-hand side is $3 < 4$, and at $t = 1$ it is $5 > 4$; the line crosses the plane between these values, consistent with $t_0 = \frac12$.

**Pass 3 — Consistency check:** The intersection point is the midpoint of $\mathbf{r}(0) = (1,0,2)$ and $\mathbf{r}(1) = (2,2,1)$: $\frac{(1,0,2) + (2,2,1)}{2} = \left(\frac32, 1, \frac32\right)$, matching $t_0 = \frac12$.

---

## Exam tip

Substitute the parametric coordinates into the plane equation and solve the single resulting equation for $t$; never set up a $3 \times 3$ system for this case.


# Exercise 1

**Problem:** Find the equation of the line through $A=(1,2)$ and $B=(4,-1)$ in parametric and general form. Identify a direction vector and an example of a normal vector. Check that both points satisfy the equation you obtain.

---

## Relevant theorem / definition

A line through $A$ with direction vector $\mathbf{d}$ has parametric form $\mathbf{r}(t) = A + t\,\mathbf{d}$. In the plane, a vector $\mathbf{n} = (a,b)$ with $\mathbf{n} \cdot \mathbf{d} = 0$ is a normal vector, and the line has general form $a(x - x_A) + b(y - y_A) = 0$.

---

## Solution

Direction vector:

$$
\mathbf{d} = \overrightarrow{AB} = B - A = (4-1,\ -1-2) = (3,-3)
$$

Parametric form:

$$
(x,y) = (1,2) + t(3,-3), \qquad t \in \mathbb{R}
$$

that is, $x = 1 + 3t$, $y = 2 - 3t$.

Normal vector: swap the components of $\mathbf{d}$ and change one sign, giving $(3,3)$; a simpler multiple is

$$
\mathbf{n} = (1,1), \qquad \mathbf{n} \cdot \mathbf{d} = 1 \cdot 3 + 1 \cdot (-3) = 0
$$

General form through $A=(1,2)$ with normal $(1,1)$:

$$
\begin{align}
1(x - 1) + 1(y - 2) &= 0 \\
x + y - 3 &= 0
\end{align}
$$

Check of both points:

- $A=(1,2)$: $1 + 2 - 3 = 0$.
- $B=(4,-1)$: $4 - 1 - 3 = 0$.

---

## Result

$$
(x,y) = (1,2) + t(3,-3), \qquad x + y - 3 = 0
$$

$$
\mathbf{d} = (3,-3), \qquad \mathbf{n} = (1,1)
$$

---

## Verification

**Pass 1 — Algebraic check:** Eliminate $t$ from the parametric form: $x + y = (1 + 3t) + (2 - 3t) = 3$, which is exactly the general form.

**Pass 2 — Numerical check:** $t = 0$ gives $A=(1,2)$ and $t = 1$ gives $(4,-1) = B$. The value $t = 2$ gives $(7,-4)$, and $7 + (-4) - 3 = 0$, so a third point of the line also satisfies the general equation.

**Pass 3 — Consistency check:** The slope from $\mathbf{d}$ is $\frac{-3}{3} = -1$, and the general form gives $y = -x + 3$, also with slope $-1$. The normal $(1,1)$ is perpendicular to the direction $(1,-1)$.

---

## Exam tip

In 2D, a normal vector is obtained from $\mathbf{d} = (d_1, d_2)$ instantly as $(d_2, -d_1)$ or $(-d_2, d_1)$; always confirm with $\mathbf{n} \cdot \mathbf{d} = 0$.


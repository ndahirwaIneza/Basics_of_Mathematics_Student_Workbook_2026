# Exercise 15

**Problem:** Let

$$
L:p+tv,\qquad \Pi:n\cdot x=d.
$$

State the conditions distinguishing the three cases: one intersection point, parallel with no common points, and the line contained in the plane. Then illustrate each case with your own simple numerical example.

---

## Relevant theorem / definition

Substituting the line into the plane equation gives

$$
\mathbf{n} \cdot (\mathbf{p} + t\mathbf{v}) = d \iff (\mathbf{n} \cdot \mathbf{v})\,t = d - \mathbf{n} \cdot \mathbf{p}
$$

a linear equation in $t$ whose solution count decides the relative position.

---

## Solution

General criterion, read from $(\mathbf{n} \cdot \mathbf{v})\,t = d - \mathbf{n} \cdot \mathbf{p}$:

1. $\mathbf{n} \cdot \mathbf{v} \neq 0$: exactly one solution
$$
t_0 = \frac{d - \mathbf{n} \cdot \mathbf{p}}{\mathbf{n} \cdot \mathbf{v}}
$$
so the line meets the plane in exactly one point $\mathbf{p} + t_0\mathbf{v}$.

2. $\mathbf{n} \cdot \mathbf{v} = 0$ and $\mathbf{n} \cdot \mathbf{p} \neq d$: the equation reads $0 = d - \mathbf{n} \cdot \mathbf{p} \neq 0$, which has no solution. The line is parallel to the plane with no common points.

3. $\mathbf{n} \cdot \mathbf{v} = 0$ and $\mathbf{n} \cdot \mathbf{p} = d$: the equation reads $0 = 0$, satisfied by every $t$. The line lies in the plane.

Geometric meaning: $\mathbf{n} \cdot \mathbf{v} = 0$ says that the direction is perpendicular to the normal, that is, parallel to the plane; $\mathbf{n} \cdot \mathbf{p} = d$ says that the starting point is on the plane.

Examples with the plane $\Pi : x + y + z = 3$, so $\mathbf{n} = (1,1,1)$, $d = 3$:

Case 1 — one point: $\mathbf{p} = (0,0,0)$, $\mathbf{v} = (1,1,1)$.

$$
\mathbf{n} \cdot \mathbf{v} = 3 \neq 0, \qquad t_0 = \frac{3 - 0}{3} = 1, \qquad \text{intersection } (1,1,1)
$$

Check: $1 + 1 + 1 = 3$.

Case 2 — parallel, no common points: $\mathbf{p} = (0,0,0)$, $\mathbf{v} = (1,-1,0)$.

$$
\mathbf{n} \cdot \mathbf{v} = 1 - 1 + 0 = 0, \qquad \mathbf{n} \cdot \mathbf{p} = 0 \neq 3
$$

Every point $(t,-t,0)$ gives $x + y + z = 0 \neq 3$.

Case 3 — contained: $\mathbf{p} = (1,1,1)$, $\mathbf{v} = (1,-1,0)$.

$$
\mathbf{n} \cdot \mathbf{v} = 0, \qquad \mathbf{n} \cdot \mathbf{p} = 3 = d
$$

Every point $(1 + t,\ 1 - t,\ 1)$ gives $(1 + t) + (1 - t) + 1 = 3$.

---

## Result

$$
\begin{align}
\mathbf{n} \cdot \mathbf{v} \neq 0 &: \ \text{one intersection point} \\
\mathbf{n} \cdot \mathbf{v} = 0,\ \mathbf{n} \cdot \mathbf{p} \neq d &: \ \text{parallel, no common points} \\
\mathbf{n} \cdot \mathbf{v} = 0,\ \mathbf{n} \cdot \mathbf{p} = d &: \ \text{line contained in the plane}
\end{align}
$$

---

## Verification

**Pass 1 — Algebraic check:** The three cases are mutually exclusive and exhaustive: either $\mathbf{n} \cdot \mathbf{v} \neq 0$, or $\mathbf{n} \cdot \mathbf{v} = 0$ and then exactly one of $\mathbf{n} \cdot \mathbf{p} \neq d$, $\mathbf{n} \cdot \mathbf{p} = d$ holds. This matches the three possible solution sets of a linear equation $at = b$: one solution, none, or all $t$.

**Pass 2 — Numerical check:** In case 2, the distance from the line to the plane is $\frac{|0 - 3|}{\sqrt3} = \sqrt3$ for every point of the line (for example $(5,-5,0)$ gives $\frac{|0 - 3|}{\sqrt3} = \sqrt3$), confirming a constant positive gap.

**Pass 3 — Consistency check:** The criterion reproduces earlier exercises: in Exercise 7, $\mathbf{n} \cdot \mathbf{v} = 0$ and $\mathbf{n} \cdot \mathbf{p} = d$ (contained); in Exercise 8, $\mathbf{n} \cdot \mathbf{v} = 2 \neq 0$ (one point); in Exercise 14, line 2 has $\mathbf{n} \cdot \mathbf{v} = 0$ and $\mathbf{n} \cdot \mathbf{p} = 1 \neq 0$ (parallel).

---

## Exam tip

Compute $\mathbf{n} \cdot \mathbf{v}$ first; only if it is zero do you need the second test $\mathbf{n} \cdot \mathbf{p} \overset{?}{=} d$.


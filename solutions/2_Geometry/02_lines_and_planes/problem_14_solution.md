# Exercise 14

**Problem:** From the point $P=(0,0,1)$, two lines are drawn with direction vectors

$$
v_1=(2,1,-1),\qquad v_2=(2,1,0).
$$

For each line, analyze its position relative to the plane $z=0$.

For the line that intersects the plane, find the intersection point. For the other line, explain how you can recognize parallelism without solving an equation.

---

## Relevant theorem / definition

A line with direction $\mathbf{v}$ meets the plane with normal $\mathbf{n}$ in exactly one point if and only if $\mathbf{n} \cdot \mathbf{v} \neq 0$. If $\mathbf{n} \cdot \mathbf{v} = 0$, the line is parallel to the plane or lies in it, depending on whether a point of the line satisfies the plane equation.

---

## Solution

The plane $z = 0$ has normal $\mathbf{n} = (0,0,1)$, so $\mathbf{n} \cdot \mathbf{v}$ is simply the $z$-component of $\mathbf{v}$.

Line 1: $L_1 : (0,0,1) + t(2,1,-1)$.

$$
\mathbf{n} \cdot \mathbf{v}_1 = -1 \neq 0
$$

The line crosses the plane in exactly one point. Its coordinates are $(2t,\ t,\ 1 - t)$; setting $z = 0$:

$$
1 - t = 0 \implies t = 1
$$

$$
L_1 \cap \Pi = (2,1,0)
$$

Line 2: $L_2 : (0,0,1) + s(2,1,0)$.

$$
\mathbf{n} \cdot \mathbf{v}_2 = 0
$$

The direction is horizontal, so the line is parallel to the plane or lies in it. The starting point $P$ has $z = 1 \neq 0$, so it is not in the plane. Hence $L_2$ is parallel to the plane with no common points.

Recognizing parallelism without solving: the $z$-component of $\mathbf{v}_2$ is $0$, so moving along $L_2$ never changes the height. Every point of $L_2$ has the form $(2s, s, 1)$ and stays at height $z = 1$, at constant distance $1$ above the plane.

---

## Result

$$
L_1 \cap \{z = 0\} = (2,1,0), \qquad L_2 \parallel \{z = 0\}, \ \text{distance } 1
$$

---

## Verification

**Pass 1 — Algebraic check:** For $L_2$, setting $z = 0$ gives $1 + 0 \cdot s = 0$, that is, $1 = 0$, an equation with no solution, confirming that there is no common point.

**Pass 2 — Numerical check:** $(2,1,0) - P = (2,1,-1) = 1 \cdot \mathbf{v}_1$, so $(2,1,0)$ lies on $L_1$ at $t = 1$, and its $z$-coordinate is $0$.

**Pass 3 — Consistency check:** The two directions differ only in the $z$-component ($-1$ versus $0$). This single difference decides between "crossing" and "parallel", exactly as the criterion $\mathbf{n} \cdot \mathbf{v} \neq 0$ versus $= 0$ predicts.

---

## Exam tip

For coordinate planes, the test $\mathbf{n} \cdot \mathbf{v}$ reduces to reading one component of $\mathbf{v}$, so the classification takes one glance.


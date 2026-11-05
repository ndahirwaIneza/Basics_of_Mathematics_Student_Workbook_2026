# Exercise 13

**Problem:** Given the sphere

$$
x^2+y^2+z^2=25
$$

and the plane $z=3$, find the equation of the intersection curve and its radius. Then describe what happens for $z=c$ depending on $c$.

---

## Relevant theorem / definition

The intersection of a sphere of radius $R$ centered at the origin with a plane at distance $d$ from the origin is:
- A **circle** of radius $r = \sqrt{R^2 - d^2}$ if $d < R$.
- A **single point** (tangency) if $d = R$.
- The **empty set** $\emptyset$ if $d > R$.

In 3D Cartesian coordinates, an intersection curve is specified by a system of two simultaneous surface equations.

---

## Solution

1. Substitute the equation of the plane $z = 3$ into the equation of the sphere:

$$
x^2 + y^2 + 3^2 = 25
$$

$$
x^2 + y^2 + 9 = 25 \implies x^2 + y^2 = 16
$$

2. Characterize the intersection curve:
   The intersection curve is given by the system:

$$
\begin{cases}
x^2 + y^2 = 16 \\
z = 3
\end{cases}
$$

   This is a circle situated entirely in the horizontal plane $z = 3$, centered at the point $(0, 0, 3)$, with radius:

$$
r = \sqrt{16} = 4
$$

3. General analysis for the cutting plane $z = c$:
   Substitute $z = c$ into the sphere's equation:

$$
x^2 + y^2 + c^2 = 25 \implies x^2 + y^2 = 25 - c^2
$$

   The nature of the solution set depends on the value of $25 - c^2$:

   - **Case 1: $|c| < 5$ (i.e. $-5 < c < 5$):**
     Here $25 - c^2 > 0$. The intersection is a non-degenerate circle in the plane $z = c$, centered at $(0, 0, c)$, with radius:

$$
r(c) = \sqrt{25 - c^2}
$$

     - For $c = 0$, the circle lies in the $xy$-plane and attains the maximum possible radius $r = 5$ (great circle / equator).
     - As $|c|$ increases toward $5$, the radius $r(c)$ strictly decreases toward $0$.

   - **Case 2: $|c| = 5$ (i.e. $c = 5$ or $c = -5$):**
     Here $25 - c^2 = 0$, so $x^2 + y^2 = 0 \implies x = 0$ and $y = 0$.
     The intersection degenerates to a single point:
     - For $c = 5$: the north pole $(0, 0, 5)$.
     - For $c = -5$: the south pole $(0, 0, -5)$.
     The plane is tangent to the sphere at these points.

   - **Case 3: $|c| > 5$ (i.e. $c > 5$ or $c < -5$):**
     Here $25 - c^2 < 0$. Since $x^2 + y^2 \ge 0$ for all real $(x, y)$, there are no real solutions.
     The intersection is the empty set $\emptyset$ (the plane does not meet the sphere).

---

## Result

$$
\text{Intersection for } z = 3: \quad \begin{cases} x^2 + y^2 = 16 \\ z = 3 \end{cases}, \qquad \text{Radius: } r = 4
$$

$$
\text{For } |c| < 5: \quad \text{Circle in plane } z=c \text{ with center } (0,0,c) \text{ and radius } r(c) = \sqrt{25 - c^2}
$$

$$
\text{For } |c| = 5: \quad \text{Single point: } (0, 0, 5) \text{ for } c=5, \quad (0, 0, -5) \text{ for } c=-5 \text{ (tangent planes)}
$$

$$
\text{For } |c| > 5: \quad \text{Empty set } \emptyset \text{ (no intersection)}
$$

---

## Verification

**Pass 1 — Algebraic check:** By the Pythagorean theorem applied to the right triangle with vertices at the sphere's center $(0,0,0)$, the circle's center $(0,0,c)$, and any point on the boundary circle $(x,y,c)$:

$$
d^2 + r^2 = R^2 \iff c^2 + r^2 = 5^2 \iff r = \sqrt{25 - c^2}
$$

For $c = 3$, $r = \sqrt{25 - 9} = \sqrt{16} = 4$.

**Pass 2 — Numerical check:** Test four quadrant points on the circle for $z = 3$: $(\pm 4, 0, 3)$ and $(0, \pm 4, 3)$. For $(\pm 4, 0, 3)$:

$$
(\pm 4)^2 + 0^2 + 3^2 = 16 + 0 + 9 = 25
$$

For $(0, \pm 4, 3)$:

$$
0^2 + (\pm 4)^2 + 3^2 = 0 + 16 + 9 = 25
$$

All points satisfy the sphere equation and $z = 3$.

**Pass 3 — Consistency check:** The distance from the center $(0,0,0)$ to the plane $z = c$ is $d = |c|$. The classical condition for plane-sphere intersection states that intersection is a circle if and only if $d < R = 5$, a tangent point if $d = 5$, and disjoint if $d > 5$, perfectly matching our derived trichotomy.

---

## Exam tip

Always state the 3D intersection curve as a system of two equations ($x^2 + y^2 = 16$ and $z = 3$); writing only $x^2 + y^2 = 16$ defines a 3D cylinder rather than a circle in space.

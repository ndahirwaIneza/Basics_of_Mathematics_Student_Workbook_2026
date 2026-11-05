# Presentation Notes — 02_lines_and_planes

## Topic summary

Lines and planes are described by two kinds of vectors: a direction vector says where a line goes, and a normal vector says how a plane is tilted. A line is "point plus multiples of a direction", and a plane is "all points whose difference from a fixed point is perpendicular to the normal". Almost every question in this set reduces to one dot product or one cross product: the cross product of two in-plane vectors gives a normal, the dot product of a direction with a normal decides whether a line crosses a plane, and projecting onto the unit normal gives distances. Intersections are found by substituting the parametric form of a line into an equation and solving for the parameter.

---

## Exercise 1 — verbal script

**Key idea:** Direction from two points, normal by swapping components, then general form.

**What to say:**
The direction vector is the difference of the two points, $B - A = (3,-3)$, so the parametric form is $(1,2) + t(3,-3)$. In the plane, a normal is obtained by swapping the components and changing one sign; after simplifying, $(1,1)$ works because its dot product with $(3,-3)$ is zero. Using that normal through $A$ gives $x + y - 3 = 0$. Both points satisfy it: $1 + 2 = 3$ and $4 - 1 = 3$. Eliminating $t$ from the parametric form gives the same equation, so the two forms describe one line.

**Show on screen:** $\mathbf{d} = (3,-3)$, $\mathbf{n} = (1,1)$ with $\mathbf{n} \cdot \mathbf{d} = 0$, and the final $x + y - 3 = 0$.

**If asked to go deeper:** The coefficients $(a,b)$ of any general equation $ax + by + c = 0$ are always a normal vector of the line.

---

## Exercise 2 — verbal script

**Key idea:** Parametric form as "point plus direction" and membership testing via one common $t$.

**What to say:**
At $t = 0$ the line passes through $(2,-1,3)$, and the coefficient vector of $t$ is the direction $(1,2,-2)$. To test whether $P = (4,3,-1)$ is on the line, I solve each coordinate equation for $t$: all three give $t = 2$, so $P$ is on the line. Equivalently, $P$ minus the base point is $(2,4,-4)$, which is exactly twice the direction vector. For $t = -1$ I subtract the direction once and get $(1,-3,5)$.

**Show on screen:** The three equations each giving $t = 2$, and $P - \mathbf{r}_0 = 2\mathbf{d}$.

**If asked to go deeper:** If the three coordinates had produced different values of $t$, the point would be off the line, and its distance could be found by projection.

---

## Exercise 3 — verbal script

**Key idea:** Point–normal form $\mathbf{n} \cdot (X - P) = 0$.

**What to say:**
A plane is all points $X$ such that the vector from $P$ to $X$ is perpendicular to the normal. Writing this as a dot product gives $2(x - 1) + (y + 2) - (z - 3) = 0$, which expands to $2x + y - z + 3 = 0$. Substituting $P$ gives $2 - 2 - 3 + 3 = 0$. The normal vector reappears as the coefficients of $x, y, z$; it fixes the tilt of the plane, while the point fixes where it sits.

**Show on screen:** The expansion line by line, highlighting the coefficients $(2,1,-1)$.

**If asked to go deeper:** Changing only the constant term produces a family of parallel planes sharing the same normal.

---

## Exercise 4 — verbal script

**Key idea:** Two in-plane vectors, cross product as normal.

**What to say:**
From the three points I build two vectors lying in the plane: $\overrightarrow{AB} = (-1,1,0)$ and $\overrightarrow{AC} = (-1,0,1)$. Their cross product is perpendicular to both, so it is a normal; the determinant gives $(1,1,1)$. Using point $A$, the plane is $x + y + z = 1$. All three points give a sum of $1$. As a quick sanity check, the normal has zero dot product with both vectors, and the equation is symmetric, as it should be for these symmetric points.

**Show on screen:** The $3 \times 3$ determinant for the cross product and the check $\mathbf{n} \cdot \overrightarrow{AB} = \mathbf{n} \cdot \overrightarrow{AC} = 0$.

**If asked to go deeper:** Half the length of the cross product, $\frac{\sqrt3}{2}$, is the area of triangle $ABC$.

---

## Exercise 5 — verbal script

**Key idea:** Parallelism test first, then the intersection system, confirmed by the coplanarity test.

**What to say:**
First I check the directions $(1,2,1)$ and $(0,1,-1)$: they are not multiples of each other, so the lines are not parallel. Next I equate the coordinates. The first equation gives $t = 1$, the second then gives $s = 3$, but the third would need $t = -2$, a contradiction. So the lines have no common point and are not parallel, which means they are skew. To confirm, the scalar triple product of the connecting vector with $\mathbf{d}_1 \times \mathbf{d}_2$ is $-3$, not zero, so the lines do not lie in a common plane.

**Show on screen:** The inconsistent system and the triple product $(1,-1,1) \cdot (-3,1,1) = -3$.

**If asked to go deeper:** The distance between the skew lines is $\frac{3}{\sqrt{11}}$.

---

## Exercise 6 — verbal script

**Key idea:** Normals decide parallelism and give the angle.

**What to say:**
The normals are $(1,1,1)$ and $(1,-1,0)$. They are not proportional, because one has a zero third component and the other does not, so the planes intersect. Their dot product is $1 - 1 + 0 = 0$, so the cosine of the angle is zero and the planes are perpendicular. Normals are enough because tilting a plane tilts its normal by the same amount, and shifting a plane, which is all that the constants $1$ and $2$ do, changes no angles.

**Show on screen:** $\mathbf{n}_1 \cdot \mathbf{n}_2 = 0 \Rightarrow \varphi = 90^\circ$.

**If asked to go deeper:** The intersection line has direction $\mathbf{n}_1 \times \mathbf{n}_2 = (1,1,-2)$.

---

## Exercise 7 — verbal script

**Key idea:** $\mathbf{n} \cdot \mathbf{v}$ decides crossing versus parallel; one point decides parallel versus contained.

**What to say:**
The direction $(1,-1,0)$ and the normal $(1,1,1)$ have dot product zero, so the line does not cross the plane: it is either parallel or contained. The base point $(1,1,0)$ gives $1 + 1 + 0 = 2$, which matches the right-hand side, so the line lies in the plane. Substituting the general point gives $2 = 2$ for every $t$. The dot product $\mathbf{n} \cdot \mathbf{v}$ is the rate of change of the plane expression along the line; zero means the line never moves towards or away from the plane.

**Show on screen:** $(1 + t) + (1 - t) + 0 = 2$ for all $t$.

**If asked to go deeper:** If the base point had given a value other than $2$, the line would be parallel at constant distance $\frac{|\mathbf{n} \cdot \mathbf{p} - d|}{\|\mathbf{n}\|}$.

---

## Exercise 8 — verbal script

**Key idea:** Substitute the parametric line into the plane and solve for $t$.

**What to say:**
First, $\mathbf{n} \cdot \mathbf{v} = 2 \neq 0$, so there is exactly one intersection point. I substitute $x = 1 + t$, $y = 2t$, $z = 2 - t$ into $x + y + z = 4$, which gives $3 + 2t = 4$ and $t = \frac12$. The point is $\left(\frac32, 1, \frac32\right)$. It satisfies the plane, and its difference from the base point is half the direction vector, so it is on the line too.

**Show on screen:** $3 + 2t = 4 \Rightarrow t = \frac12$ and the final point.

**If asked to go deeper:** The general formula is $t_0 = \frac{d - \mathbf{n} \cdot \mathbf{p}}{\mathbf{n} \cdot \mathbf{v}}$.

---

## Exercise 9 — verbal script

**Key idea:** Distance as projection onto the unit normal.

**What to say:**
For the line, I substitute $P$ into $3x + 4y - 10$, getting $8$, and divide by the length of the normal, $5$, so the distance is $\frac85$. For the plane, $Q$ gives $5$ in $2x - 2y + z - 4$, and the normal has length $3$, so the distance is $\frac53$. Both formulas are the same idea: the shortest route to a line or plane is along the normal, so the distance is the length of the projection of any connecting vector onto the unit normal. The numerator measures how badly the point fails the equation, and dividing by $\|\mathbf{n}\|$ turns that into a length.

**Show on screen:** The two formulas side by side with the common form $\frac{|\mathbf{n} \cdot X_0 + c|}{\|\mathbf{n}\|}$.

**If asked to go deeper:** I can confirm each distance by constructing the foot of the perpendicular and measuring it, which I did in the verification.

---

## Exercise 10 — verbal script

**Key idea:** Projection along the normal line; reflection doubles the step.

**What to say:**
I go from $P$ along the normal: $(2 + t, 1 + t, 3 + t)$. Substituting into the plane gives $6 + 3t = 3$, so $t = -1$. The projection is $P - \mathbf{n} = (1,0,2)$. For the reflection, I take the same step twice: $P - 2\mathbf{n} = (0,-1,1)$. The midpoint of $P$ and its reflection is $(1,0,2)$, which lies on the plane and is exactly the projection.

**Show on screen:** $t_0 = -1$, $P' = P + t_0\mathbf{n}$, $P'' = P + 2t_0\mathbf{n}$.

**If asked to go deeper:** The distance $\sqrt3$ from the formula matches $\|P - P'\|$, and the two points lie on opposite sides of the plane.

---

## Exercise 11 — verbal script

**Key idea:** Line direction plus a vector to the extra point give two in-plane directions.

**What to say:**
The line gives a point $A = (1,0,2)$ and direction $(1,1,-1)$. A second direction must point from the line to $P$: $\overrightarrow{AP} = (-1,2,-1)$, which is not parallel to the first one. Their cross product is $(1,2,3)$, so the plane is $x + 2y + 3z = 7$. The point $P$ gives $0 + 4 + 3 = 7$, and substituting the whole line gives $7$ for every $t$, because the $t$-terms cancel.

**Show on screen:** The cross product determinant and the identity $(1 + t) + 2t + 3(2 - t) = 7$.

**If asked to go deeper:** If $P$ had been on the line, the two directions would be parallel and infinitely many planes would contain both.

---

## Exercise 12 — verbal script

**Key idea:** Intersection line from elimination, cross-checked by $\mathbf{n}_1 \times \mathbf{n}_2$.

**What to say:**
Subtracting the equations gives $y = 1$. Then $x + z = 2$, and with $z$ free, $z = t$ and $x = 2 - t$. The line is $(2,1,0) + t(-1,0,1)$. Geometrically, the direction must be perpendicular to both normals, so it is parallel to their cross product, which is $(2,0,-2)$. That is $-2$ times the vector from elimination, so both methods give the same line.

**Show on screen:** Elimination result and $(2,0,-2) = -2(-1,0,1)$.

**If asked to go deeper:** Any non-zero multiple of a direction vector is equally valid; only the line itself matters.

---

## Exercise 13 — verbal script

**Key idea:** Closest point equals foot of the perpendicular.

**What to say:**
The normal is $(1,2,2)$ with length $3$. Moving from $P$ along the normal, $(3 + t, 2t, 2t)$, and substituting into the plane gives $3 + 9t = 4$, so $t = \frac19$. The closest point is $\left(\frac{28}{9}, \frac29, \frac29\right)$, and the distance is $\frac19 \cdot 3 = \frac13$, the same as the distance formula. The segment from $P$ to this point is $\frac19\mathbf{n}$, a multiple of the normal, so it is perpendicular to the plane.

**Show on screen:** $t_0 = \frac19$, the point $Q$, and $\overrightarrow{PQ} = \frac19\mathbf{n}$.

**If asked to go deeper:** Any other plane point is farther by Pythagoras, since its distance squared is $D^2$ plus the squared in-plane offset.

---

## Exercise 14 — verbal script

**Key idea:** For the plane $z = 0$, the test $\mathbf{n} \cdot \mathbf{v}$ is just the $z$-component of $\mathbf{v}$.

**What to say:**
The normal of $z = 0$ is $(0,0,1)$, so I only need the $z$-component of each direction. The first direction has $z$-component $-1$, so the line descends and must hit the plane; setting $1 - t = 0$ gives $t = 1$ and the point $(2,1,0)$. The second direction has $z$-component $0$, so that line stays at height $1$ forever: it is parallel to the plane at distance $1$. No equation solving is needed to see this.

**Show on screen:** $v_1$ versus $v_2$ with the $z$-components highlighted.

**If asked to go deeper:** Trying to intersect line 2 gives $1 = 0$, the algebraic sign of parallelism.

---

## Exercise 15 — verbal script

**Key idea:** Full classification from $(\mathbf{n} \cdot \mathbf{v})\,t = d - \mathbf{n} \cdot \mathbf{p}$.

**What to say:**
Substituting the line into the plane always gives the linear equation $(\mathbf{n} \cdot \mathbf{v})\,t = d - \mathbf{n} \cdot \mathbf{p}$. If $\mathbf{n} \cdot \mathbf{v}$ is non-zero, there is exactly one $t$, so one intersection point. If it is zero, the left side vanishes: when $\mathbf{n} \cdot \mathbf{p} \neq d$ we get a false statement and the line is parallel with no common points, and when $\mathbf{n} \cdot \mathbf{p} = d$ every $t$ works and the line lies in the plane. With the plane $x + y + z = 3$, direction $(1,1,1)$ from the origin gives one point $(1,1,1)$; direction $(1,-1,0)$ from the origin gives a parallel line; and direction $(1,-1,0)$ from $(1,1,1)$ gives a contained line.

**Show on screen:** The three-case table and the three examples.

**If asked to go deeper:** These are exactly the three solution types of a single linear equation $at = b$: one solution, none, or all real $t$.


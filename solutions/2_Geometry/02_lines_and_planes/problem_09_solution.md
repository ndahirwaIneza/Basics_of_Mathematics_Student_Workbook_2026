# Exercise 9

**Problem:** Compute:

1. the distance from $P=(2,3)$ to the line $3x+4y-10=0$,
2. the distance from $Q=(2,-1,3)$ to the plane $2x-2y+z-4=0$.

Compare the two formulas and explain their common connection with the normal direction.

---

## Relevant theorem / definition

Distance from $(x_0, y_0)$ to the line $ax + by + c = 0$:

$$
D = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}
$$

Distance from $(x_0, y_0, z_0)$ to the plane $ax + by + cz + e = 0$:

$$
D = \frac{|ax_0 + by_0 + cz_0 + e|}{\sqrt{a^2 + b^2 + c^2}}
$$

---

## Solution

1. Point to line, with $\mathbf{n} = (3,4)$, $\|\mathbf{n}\| = 5$:

$$
D_1 = \frac{|3 \cdot 2 + 4 \cdot 3 - 10|}{\sqrt{3^2 + 4^2}} = \frac{|6 + 12 - 10|}{5} = \frac{8}{5}
$$

2. Point to plane, with $\mathbf{n} = (2,-2,1)$, $\|\mathbf{n}\| = 3$:

$$
D_2 = \frac{|2 \cdot 2 - 2 \cdot (-1) + 3 - 4|}{\sqrt{2^2 + (-2)^2 + 1^2}} = \frac{|4 + 2 + 3 - 4|}{3} = \frac{5}{3}
$$

Common connection: both formulas have the same structure

$$
D = \frac{|\mathbf{n} \cdot X_0 + \text{const}|}{\|\mathbf{n}\|} = \left|(X_0 - X_1) \cdot \frac{\mathbf{n}}{\|\mathbf{n}\|}\right|
$$

where $X_1$ is any point of the line or plane. The shortest path from a point to a line in the plane, or to a plane in space, runs along the normal direction. The distance is therefore the length of the projection of $X_0 - X_1$ onto the unit normal. The numerator measures how far the equation is from being satisfied; dividing by $\|\mathbf{n}\|$ converts this into an actual length. The only difference between the two cases is the number of coordinates.

---

## Result

$$
D_1 = \frac{8}{5}, \qquad D_2 = \frac{5}{3}
$$

---

## Verification

**Pass 1 — Algebraic check (foot of the perpendicular, line):** Move from $P$ along $-\mathbf{n}$: $F = P - \frac{8}{25}(3,4) = \left(\frac{26}{25}, \frac{43}{25}\right)$. Then $3 \cdot \frac{26}{25} + 4 \cdot \frac{43}{25} = \frac{78 + 172}{25} = 10$, so $F$ is on the line, and $\|P - F\| = \frac{8}{25} \cdot 5 = \frac85$.

**Pass 2 — Numerical check (foot of the perpendicular, plane):** $F' = Q - \frac{5}{9}(2,-2,1) = \left(\frac89, \frac19, \frac{22}{9}\right)$. Then $2 \cdot \frac89 - 2 \cdot \frac19 + \frac{22}{9} - 4 = \frac{16 - 2 + 22}{9} - 4 = 4 - 4 = 0$, so $F'$ lies on the plane, and $\|Q - F'\| = \frac59 \cdot 3 = \frac53$.

**Pass 3 — Consistency check:** Scaling the equations, for example to $6x + 8y - 20 = 0$, doubles both numerator and denominator and leaves $D_1$ unchanged; a distance cannot depend on how the equation is scaled.

---

## Exam tip

Bring the equation to the form "expression $= 0$" before substituting; forgetting the constant term or using the wrong sign is the most common error.


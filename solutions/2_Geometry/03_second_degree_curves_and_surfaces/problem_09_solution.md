# Exercise 9

**Problem:** Consider

$$
\frac{x^2}{9}+\frac{y^2}{4}+\frac{z^2}{16}=1.
$$

Give the semiaxis lengths, describe the cross-section $z=0$, and explain how the cross-sections $z=c$ change for $|c|<4$.

---

## Relevant theorem / definition

The canonical equation of a triaxial ellipsoid centered at the origin is:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c_0^2} = 1
$$

where $a, b, c_0 > 0$ are the semiaxis lengths along the $x$-, $y$-, and $z$-axes, respectively. A planar cross-section obtained by setting $z = c$ yields a two-dimensional curve in that cutting plane.

---

## Solution

1. Identify the semiaxis lengths:
   Comparing $\frac{x^2}{9} + \frac{y^2}{4} + \frac{z^2}{16} = 1$ with the standard form:
   - $a^2 = 9 \implies a = 3$ (semiaxis along the $x$-axis)
   - $b^2 = 4 \implies b = 2$ (semiaxis along the $y$-axis)
   - $c_0^2 = 16 \implies c_0 = 4$ (semiaxis along the $z$-axis)

2. Describe the cross-section by the plane $z = 0$:
   Substitute $z = 0$ into the surface equation:

$$
\frac{x^2}{9} + \frac{y^2}{4} + 0 = 1 \iff \frac{x^2}{9} + \frac{y^2}{4} = 1
$$

   In the coordinate plane $z = 0$ (the $xy$-plane), this cross-section is an ellipse centered at $(0,0,0)$ with horizontal semiaxis $a = 3$ and vertical semiaxis $b = 2$. This is the largest horizontal cross-section (the equatorial ellipse).

3. Analyze the horizontal cross-sections $z = c$ for $|c| < 4$:
   Substitute $z = c$ into the equation:

$$
\frac{x^2}{9} + \frac{y^2}{4} = 1 - \frac{c^2}{16}
$$

   Because $|c| < 4$, we have $c^2 < 16$, which implies:

$$
1 - \frac{c^2}{16} > 0
$$

   Dividing both sides by this positive factor gives the canonical form of the cross-sectional curve:

$$
\frac{x^2}{9\left(1 - \frac{c^2}{16}\right)} + \frac{y^2}{4\left(1 - \frac{c^2}{16}\right)} = 1
$$

   In each horizontal plane $z = c$, the cross-section is an ellipse centered at $(0, 0, c)$ with semiaxis lengths:

$$
a(c) = 3\sqrt{1 - \frac{c^2}{16}}, \qquad b(c) = 2\sqrt{1 - \frac{c^2}{16}}
$$

4. Geometric evolution as $|c|$ changes:
   - **At $c = 0$:** The semiaxes attain their maximum values $a(0) = 3$ and $b(0) = 2$.
   - **As $|c|$ increases toward $4$:** The scaling factor $\sqrt{1 - c^2/16}$ strictly decreases from $1$ toward $0$. The ellipses shrink homothetically toward the $z$-axis.
   - **Constant eccentricity/shape:** The ratio of the semiaxes is invariant:

$$
\frac{a(c)}{b(c)} = \frac{3\sqrt{1 - c^2/16}}{2\sqrt{1 - c^2/16}} = \frac{3}{2} = 1.5
$$

     All horizontal cross-sections are geometrically similar ellipses.
   - **At $|c| = 4$ ($c = \pm 4$):** The factor becomes $0$, so the cross-section degenerates to a single point: $(0, 0, 4)$ (the north pole) and $(0, 0, -4)$ (the south pole).
   - **For $|c| > 4$:** $1 - c^2/16 < 0$, meaning the cutting plane does not intersect the ellipsoid.

---

## Result

$$
\text{Semiaxis lengths: } a = 3 \ (x\text{-axis}), \quad b = 2 \ (y\text{-axis}), \quad c_0 = 4 \ (z\text{-axis})
$$

$$
\text{Cross-section } z = 0: \quad \text{Ellipse } \frac{x^2}{9} + \frac{y^2}{4} = 1 \text{ in the plane } z = 0
$$

$$
\text{Cross-sections } z = c \ (|c| < 4): \quad \text{Similar ellipses with semiaxes } a(c) = 3\sqrt{1 - \frac{c^2}{16}}, \ b(c) = 2\sqrt{1 - \frac{c^2}{16}}
$$

---

## Verification

**Pass 1 — Algebraic check:** The area of an ellipse with semiaxes $a(c)$ and $b(c)$ is $A(c) = \pi a(c) b(c) = 6\pi \left(1 - \frac{c^2}{16}\right)$. Integrating $A(c)$ from $c = -4$ to $c = 4$:

$$
V = \int_{-4}^4 6\pi \left(1 - \frac{c^2}{16}\right) dc = 6\pi \left[ c - \frac{c^3}{48} \right]_{-4}^4 = 6\pi \left( \left(4 - \frac{64}{48}\right) - \left(-4 + \frac{64}{48}\right) \right) = 6\pi \left(8 - \frac{8}{3}\right) = 32\pi
$$

By the standard volume formula for an ellipsoid, $V = \frac{4}{3}\pi a b c_0 = \frac{4}{3}\pi(3)(2)(4) = 32\pi$, confirming exact agreement.

**Pass 2 — Numerical check:** At height $c = 2$, $1 - \frac{2^2}{16} = 1 - \frac{1}{4} = \frac{3}{4}$. The semiaxes are $a(2) = 3\sqrt{3/4} = \frac{3\sqrt{3}}{2} \approx 2.598$ and $b(2) = 2\sqrt{3/4} = \sqrt{3} \approx 1.732$. Testing the boundary point $(0, \sqrt{3}, 2)$:

$$
\frac{0^2}{9} + \frac{(\sqrt{3})^2}{4} + \frac{2^2}{16} = 0 + \frac{3}{4} + \frac{4}{16} = \frac{3}{4} + \frac{1}{4} = 1
$$

**Pass 3 — Consistency check:** The surface is symmetric under coordinate reflections $(x,y,z) \mapsto (\pm x, \pm y, \pm z)$, which is confirmed by $a(c) = a(-c)$ and $b(c) = b(-c)$.

---

## Exam tip

To find the cross-section $z = c$, treat $z$ as a constant and move $c^2/c_0^2$ to the right-hand side; the remaining 2D equation reveals both the curve family and its scaling factor.

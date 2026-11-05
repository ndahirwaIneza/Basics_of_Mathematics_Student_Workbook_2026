# Exercise 12

**Problem:** A certain surface has the following properties:
- the cross-section $z=0$ is a point,
- for $z>0$, the cross-sections $z=\text{const}$ are circles with increasing radius,
- vertical cross-sections through the $Oz$ axis are parabolas.

Propose a simple equation for such a surface and justify your choice.

---

## Relevant theorem / definition

A surface of revolution with axis of symmetry $Oz$ has the general Cartesian form:

$$
F\left(x^2 + y^2, z\right) = 0 \iff z = f\left(\sqrt{x^2 + y^2}\right) = f(\rho)
$$

where $\rho = \sqrt{x^2 + y^2}$ is the radial distance from the $Oz$ axis. Planar sections through the rotation axis have equation $z = f(\rho)$ in coordinate plane $(\rho, z)$.

---

## Solution

1. Translate the geometric conditions into algebraic constraints:
   - **Condition 1:** The horizontal cross-section at $z = 0$ is a single point:

$$
\{(x, y) : (x, y, 0) \in S\} = \{(0, 0)\}
$$

   - **Condition 2:** For every constant $c > 0$, the cross-section $z = c$ is a circle centered on the $z$-axis:

$$
x^2 + y^2 = [r(c)]^2
$$

     with radius $r(c)$ strictly increasing with $c$, meaning $r'(c) > 0$.
   - **Condition 3:** Any vertical plane containing the $Oz$ axis has Cartesian equation $y = kx$ (for $k \in \mathbb{R}$) or $x = 0$. The cross-section in this plane must be a parabola symmetric about $Oz$.

2. Relate radius to height using the parabolic condition:
   In any vertical plane through $Oz$, let $\rho \ge 0$ denote the radial distance from $Oz$, so that $x^2 + y^2 = \rho^2$.
   A parabola symmetric about $Oz$ with vertex at the origin has the form:

$$
z = a \rho^2 \qquad (a > 0)
$$

   or equivalently:

$$
\rho^2 = \frac{z}{a}
$$

3. Substitute $\rho^2 = x^2 + y^2$:

$$
z = a(x^2 + y^2)
$$

   Choosing the simplest scaling parameter $a = 1$ yields:

$$
z = x^2 + y^2
$$

4. Step-by-step verification of all three properties for $z = x^2 + y^2$:
   - **Check property 1 ($z = 0$):**

$$
x^2 + y^2 = 0 \implies x = 0 \quad \text{and} \quad y = 0
$$

     The intersection is exclusively the single point $(0, 0, 0)$.
   - **Check property 2 ($z = c > 0$):**

$$
x^2 + y^2 = c = (\sqrt{c})^2
$$

     This is a circle in the plane $z = c$ with radius $r(c) = \sqrt{c}$. Because $\frac{dr}{dc} = \frac{1}{2\sqrt{c}} > 0$ for all $c > 0$, the radius is strictly increasing as $c$ increases.
   - **Check property 3 (vertical cross-sections through $Oz$):**
     - For $x = 0$ (the $yz$-plane): $z = y^2$, a standard parabola with vertex at $(0,0,0)$.
     - For $y = 0$ (the $xz$-plane): $z = x^2$, a standard parabola with vertex at $(0,0,0)$.
     - For any plane $y = kx$:

$$
z = x^2 + (kx)^2 = (1 + k^2)x^2
$$

       Letting $u = x\sqrt{1 + k^2}$ denote the horizontal coordinate along the line of intersection in the plane, this becomes $z = u^2$, which is an identical upward-opening parabola.

---

## Result

$$
z = x^2 + y^2
$$

$$
\text{Surface type: Circular paraboloid (elliptic paraboloid of revolution)}
$$

---

## Verification

**Pass 1 — Algebraic check:** Verify the rotational invariance: rotating $(x, y)$ by angle $\theta$ maps $x \mapsto x\cos\theta - y\sin\theta$ and $y \mapsto x\sin\theta + y\cos\theta$. Then $(x\cos\theta - y\sin\theta)^2 + (x\sin\theta + y\cos\theta)^2 = x^2 + y^2 = z$, confirming perfect rotational symmetry.

**Pass 2 — Numerical check:** At height $z = 4$, the horizontal circle has radius $r(4) = \sqrt{4} = 2$. At height $z = 9$, the radius is $r(9) = \sqrt{9} = 3 > 2$. In the plane $y = x$, at $x = 2$, $z = 2^2 + 2^2 = 8$, while the horizontal distance from the axis is $\rho = \sqrt{2^2 + 2^2} = \sqrt{8}$, confirming $z = \rho^2 = 8$.

**Pass 3 — Consistency check:** If instead the vertical cuts were straight lines $z = a\rho$, the surface would be a cone $z^2 = a^2(x^2 + y^2)$. The parabolic relationship $z \propto \rho^2$ uniquely identifies the circular paraboloid.

---

## Exam tip

When translating geometric cross-sections into an equation, identify rotational symmetry first to write $\rho^2 = x^2 + y^2$, then apply the profile curve equation $z = f(\rho)$.

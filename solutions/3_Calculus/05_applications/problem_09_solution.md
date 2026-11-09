# Exercise 9

**Problem:** A closed cylinder has fixed volume $V$.

1. Write the volume constraint.
2. Eliminate one of the variables.
3. Express the surface area as a function of the radius $r$.
4. Find the relation between the height $h$ and the radius $r$ for which the material usage is minimal.

Interpret the obtained relation geometrically.

---

## Relevant theorem / definition

For a right circular cylinder of radius $r$ and height $h$, the volume is $V = \pi r^2 h$ and the total surface area is $A = 2\pi r^2 + 2\pi rh$. A critical point $r_0$ of a differentiable function $A(r)$ on $(0, \infty)$ where $A''(r) > 0$ everywhere is the unique global minimum.

---

## Solution

1. Volume constraint:
   The volume $V$ of a closed cylinder with base radius $r > 0$ and height $h > 0$ is fixed:

   $$
   V = \pi r^2 h
   $$

2. Elimination of one variable:
   Express the height $h$ in terms of the independent variable $r$ and the fixed parameter $V$:

   $$
   h = \frac{V}{\pi r^2}
   $$

3. Surface area as a function of $r$:
   The total surface area comprises two circular bases and the lateral surface:

   $$
   A(r, h) = 2\pi r^2 + 2\pi r h
   $$

   Substitute $h = \frac{V}{\pi r^2}$:

   $$
   A(r) = 2\pi r^2 + 2\pi r \left(\frac{V}{\pi r^2}\right) = 2\pi r^2 + \frac{2V}{r}
   $$

   The geometric domain is $r \in (0, \infty)$.

4. Relation between $h$ and $r$ minimizing material usage:
   Compute the first derivative of $A(r)$ with respect to $r$:

   $$
   A'(r) = 4\pi r - \frac{2V}{r^2}
   $$

   Set $A'(r) = 0$ to determine the critical point:

   $$
   4\pi r = \frac{2V}{r^2} \implies 2\pi r^3 = V
   $$

   Substitute $V = \pi r^2 h$ into this optimality condition:

   $$
   2\pi r^3 = \pi r^2 h
   $$

   Divide both sides by $\pi r^2$ (since $r > 0$):

   $$
   h = 2r
   $$

   Verify second-order sufficiency:

   $$
   A''(r) = 4\pi + \frac{4V}{r^3}
   $$

   Because $r > 0$ and $V > 0$, $A''(r) > 0$ for all $r \in (0, \infty)$. Thus $A(r)$ is strictly convex, guaranteeing that $h = 2r$ is the unique global minimum.

5. Geometric interpretation:
   The relation $h = 2r$ states that the cylinder's height equals its base diameter ($d = 2r$). A vertical cross-section containing the central axis of the cylinder is therefore a square with side lengths $2r \times 2r$. This square aspect ratio minimizes boundary surface area per unit of enclosed volume.

---

## Result

$$
V = \pi r^2 h
$$

$$
A(r) = 2\pi r^2 + \frac{2V}{r}
$$

$$
h = 2r \quad (\text{height equals base diameter; square axial cross-section})
$$

---

## Verification

**Pass 1 — Algebraic check:** Apply the three-term AM-GM inequality to the split $A(r) = 2\pi r^2 + \frac{V}{r} + \frac{V}{r}$ for $r > 0$ and $V > 0$:

$$
A(r) = 2\pi r^2 + \frac{V}{r} + \frac{V}{r} \ge 3\sqrt[3]{2\pi r^2 \cdot \frac{V}{r} \cdot \frac{V}{r}} = 3\left(2\pi V^2\right)^{1/3}
$$

The product inside the cube root simplifies to $2\pi V^2$, which is constant and independent of $r$. Equality in AM-GM holds if and only if all three summands are equal:

$$
2\pi r^2 = \frac{V}{r} \iff V = 2\pi r^3
$$

Substituting $V = \pi r^2 h$ yields $\pi r^2 h = 2\pi r^3 \implies h = 2r$ (since $r > 0$). This algebraically confirms $h = 2r$ as the global minimum without differentiation.

**Pass 2 — Numerical check:** Let $V = 2\pi \approx 6.283$. Then $2\pi r^3 = 2\pi \implies r = 1$, which gives $h = \frac{2\pi}{\pi(1)^2} = 2 = 2r$. The area is $A(1) = 2\pi(1)^2 + \frac{2(2\pi)}{1} = 6\pi \approx 18.8495$.
- Test $r = 0.8$: $h = \frac{2}{0.64} = 3.125 \implies A(0.8) = 2\pi(0.64) + 2\pi(0.8)(3.125) = 1.28\pi + 5\pi = 6.28\pi \approx 19.729 > 6\pi$.
- Test $r = 1.2$: $h = \frac{2}{1.44} \approx 1.389 \implies A(1.2) = 2\pi(1.44) + 2\pi(1.2)(1.389) = 2.88\pi + 3.333\pi = 6.213\pi \approx 19.52 > 6\pi$.
Both perturbations increase the surface area.

**Pass 3 — Consistency check:** As $r \to 0^+$, $A(r) \to \infty$ (infinitely tall, thin needle). As $r \to \infty$, $A(r) \to \infty$ (infinitely wide, flat coin). Since $A(r) > 0$ and continuous on $(0, \infty)$, a minimum must exist in the interior, and $h = 2r$ is the unique solution.

---

## Exam tip

For closed cylindrical containers, the optimal design always has diameter equal to height ($h = 2r$), whereas for open-top containers the optimal ratio is $h = r$.

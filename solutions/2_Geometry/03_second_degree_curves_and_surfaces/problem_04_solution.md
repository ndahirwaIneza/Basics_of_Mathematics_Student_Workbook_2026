# Exercise 4

**Problem:** For

$$
y^2=12x,
$$

identify the vertex, axis of symmetry, and opening direction. Find points on the parabola for $x=3$ and use them to make a sketch.

---

## Relevant theorem / definition

The canonical equation of a parabola with vertex at the origin opening along the positive $x$-axis is:

$$
y^2 = 2px \qquad (p > 0)
$$

- Vertex: $(0,0)$.
- Axis of symmetry: $y = 0$ ($x$-axis).
- Focus: $F\left(\frac{p}{2}, 0\right)$.
- Directrix: $x = -\frac{p}{2}$.
- Focal chord (latus rectum) length through the focus: $2p$.

---

## Solution

1. Determine the canonical parameter:

$$
2p = 12 \implies p = 6
$$

2. Identify vertex, axis, and opening direction:
   - **Vertex:** $(0,0)$, where $x = 0$ and $y = 0$.
   - **Axis of symmetry:** $y = 0$ ($x$-axis), since substituting $-y$ for $y$ yields $(-y)^2 = y^2 = 12x$, leaving the equation invariant.
   - **Opening direction:** For real $y$, $y^2 \ge 0$, which requires $12x \ge 0 \implies x \ge 0$. The curve exists only in the right half-plane ($x \ge 0$) and extends to $+\infty$, so it opens to the right.
   - **Focus and directrix:** $F = \left(\frac{6}{2}, 0\right) = (3, 0)$, directrix $x = -3$.

3. Find points on the parabola for $x = 3$:

$$
y^2 = 12(3) = 36 \implies y = \pm \sqrt{36} = \pm 6
$$

   The two points on the parabola are $P_1 = (3, 6)$ and $P_2 = (3, -6)$. Because $x = 3$ is the abscissa of the focus, the segment $P_1P_2$ is the focal chord, with vertical span $6 - (-6) = 12 = 2p$.

4. Sketch characterization:
   The parabola is tangent to the $y$-axis at the origin and opens symmetrically across the positive $x$-axis, passing through the points $(3, 6)$ and $(3, -6)$.

```text
               y
               ^
               |       * P1(3, 6)
               |     .
               |   .'
               |  /
  -------------+-V-----------* F(3,0)-----> x
     x = -3    |(0,0)
               |  \
               |   '.
               |     .
               |       * P2(3, -6)
```

---

## Result

$$
\text{Vertex: } (0,0), \qquad \text{Axis of symmetry: } y = 0 \ (x\text{-axis})
$$

$$
\text{Opening direction: to the right } (x \ge 0)
$$

$$
\text{Points for } x = 3: \quad P_1(3, 6) \quad \text{and} \quad P_2(3, -6)
$$

---

## Verification

**Pass 1 — Algebraic check:** Verify the geometric focus-directrix definition for point $P_1(3, 6)$:
- Distance to focus $F(3, 0)$:

$$
d(P_1, F) = \sqrt{(3 - 3)^2 + (6 - 0)^2} = \sqrt{0 + 36} = 6
$$

- Distance to directrix line $x = -3$:

$$
d(P_1, \text{directrix}) = |3 - (-3)| = 6
$$

  Both distances are equal, fulfilling the defining property of a parabola.

**Pass 2 — Numerical check:** Compute another point: for $x = 12$, $y^2 = 12(12) = 144 \implies y = \pm 12$. The distance from $(12, 12)$ to directrix $x=-3$ is $12 - (-3) = 15$, and to focus $F(3,0)$ is $\sqrt{(12-3)^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15$.

**Pass 3 — Consistency check:** Since $y = \pm 2\sqrt{3}\sqrt{x}$, the slope of the upper branch is $\frac{dy}{dx} = \frac{\sqrt{3}}{\sqrt{x}}$. As $x \to 0^+$, the tangent slope tends to $+\infty$ (vertical tangent at the vertex), and as $x \to \infty$, the slope tends to $0$, consistent with standard parabolic flaring.

---

## Exam tip

The linear term directly indicates both the axis of symmetry and the opening direction: $y^2 = 12x$ has linear variable $x$ with positive coefficient $+12$, which immediately implies symmetry across the $x$-axis and opening toward positive $x$.

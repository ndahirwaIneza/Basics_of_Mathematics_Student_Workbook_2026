# Exercise 15

**Problem:** Consider the two equations:

$$
4x^2+9y^2-8x+36y+4=0,
$$

$$
4x^2+y^2=z^2.
$$

For the first equation, reduce it to canonical form, recognize the curve, give its most important features, and make a sketch.

For the second equation, do not begin by using a ready-made name for the surface. First describe the cross-sections $z=c$ and the cross-sections by the planes $x=0$ and $y=0$, paying attention to the different scales along the axes. Only then identify the surface and make a sketch.

---

## Relevant theorem / definition

- An equation of the form $\frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1$ is an ellipse with center $(x_0, y_0)$ and semiaxes $a, b$.
- A second-degree surface whose horizontal cross-sections are similar ellipses scaling linearly with $|z|$ and whose vertical axial cross-sections are pairs of straight lines intersecting at the origin is an **elliptic cone**.

---

## Solution

### Part 1: Equation $4x^2+9y^2-8x+36y+4=0$

1. Group the terms by variable and factor leading coefficients:

$$
4(x^2 - 2x) + 9(y^2 + 4y) + 4 = 0
$$

2. Complete the squares:
   - For $x$: $x^2 - 2x = (x - 1)^2 - 1$
   - For $y$: $y^2 + 4y = (y + 2)^2 - 4$

3. Substitute back into the equation:

$$
\begin{align}
4\left[(x - 1)^2 - 1\right] + 9\left[(y + 2)^2 - 4\right] + 4 &= 0 \\
4(x - 1)^2 - 4 + 9(y + 2)^2 - 36 + 4 &= 0 \\
4(x - 1)^2 + 9(y + 2)^2 - 36 &= 0 \\
4(x - 1)^2 + 9(y + 2)^2 &= 36
\end{align}
$$

4. Divide both sides by $36$:

$$
\frac{(x - 1)^2}{9} + \frac{(y + 2)^2}{4} = 1
$$

5. Curve recognition and key features:
   - **Type:** Ellipse with axes parallel to the coordinate axes.
   - **Center:** $(x_0, y_0) = (1, -2)$.
   - **Horizontal semiaxis:** $a = \sqrt{9} = 3$ (major axis, parallel to the $x$-axis along $y = -2$).
   - **Vertical semiaxis:** $b = \sqrt{4} = 2$ (minor axis, parallel to the $y$-axis along $x = 1$).
   - **Vertices:**
     - Major axis endpoints: $(1 \pm 3, -2) \implies (-2, -2)$ and $(4, -2)$.
     - Minor axis endpoints: $(1, -2 \pm 2) \implies (1, 0)$ and $(1, -4)$.
   - **Linear eccentricity:** $c = \sqrt{a^2 - b^2} = \sqrt{9 - 4} = \sqrt{5} \approx 2.236$.
   - **Foci:** $(1 \pm \sqrt{5}, -2)$.

6. Sketch of the ellipse:

```text
                     y
                     ^
                     | (1, 0)
               .-----+-----.
            .-'      |      '-.
          .'         |         '.
  -------+-----------+-----------+-----> x
       (-2,-2)    (1,-2)       (4,-2)
          '.         |         .'
            '-.      |      .-'
               '-----+-----'
                     | (1, -4)
```

---

### Part 2: Equation $4x^2+y^2=z^2$

1. Horizontal cross-sections $z = c$:
   Substitute $z = c$ into the equation:

$$
4x^2 + y^2 = c^2
$$

   - **If $c = 0$:**

$$
4x^2 + y^2 = 0 \implies x = 0 \quad \text{and} \quad y = 0
$$

     The cross-section is the single point $(0, 0, 0)$ (the apex).
   - **If $c \neq 0$:** Divide both sides by $c^2$:

$$
\frac{4x^2}{c^2} + \frac{y^2}{c^2} = 1 \iff \frac{x^2}{(|c|/2)^2} + \frac{y^2}{|c|^2} = 1
$$

     In the horizontal plane $z = c$, this is an **ellipse** centered at $(0, 0, c)$ with:
     - Semiaxis along $x$: $a(c) = \frac{|c|}{2}$
     - Semiaxis along $y$: $b(c) = |c|$
     - **Scale difference:** The semiaxis along $y$ is twice as long as the semiaxis along $x$:

$$
\frac{b(c)}{a(c)} = \frac{|c|}{|c|/2} = 2
$$

       The ellipse is stretched along the $y$-direction by a factor of 2 compared to the $x$-direction, and its dimensions grow strictly linearly with $|c|$.

2. Vertical cross-section by the plane $x = 0$ ($yz$-plane):

$$
y^2 = z^2 \iff z^2 - y^2 = 0 \iff (z - y)(z + y) = 0 \implies z = \pm y
$$

   This cross-section consists of two straight lines intersecting at the origin with slope $\pm 1$ ($45^\circ$ to the $y$-axis).

3. Vertical cross-section by the plane $y = 0$ ($xz$-plane):

$$
4x^2 = z^2 \iff z^2 - 4x^2 = 0 \iff (z - 2x)(z + 2x) = 0 \implies z = \pm 2x
$$

   This cross-section consists of two straight lines intersecting at the origin with slope $\pm 2$. Because the slope is twice as steep as in the $yz$-plane, the surface opens narrower in the $x$-direction and wider in the $y$-direction.

4. Identification of the surface:
   Since the cross-sections parallel to the $xy$-plane are ellipses with a constant axis ratio $b/a = 2$ whose linear dimensions expand proportionally to $|z|$, and the principal vertical cuts are pairs of straight lines meeting at $(0,0,0)$, this surface is an **elliptic cone** opening along the $z$-axis with apex at the origin.

5. Sketch of the elliptic cone:

```text
                  z
            \     ^     /
             \    |    /      ellipse in z = c (stretched along y)
              \---+---/
               \  |  /
  --------------\-+-/------------> x
                / | \         apex at (0,0,0)
               /  |  \
              /---+---\       ellipse in z = -c
             /    |    \
            /     |     \
```

---

## Result

$$
\text{Curve 1: } \frac{(x - 1)^2}{9} + \frac{(y + 2)^2}{4} = 1 \quad \implies \text{Ellipse, center } (1, -2), \text{ semiaxes } a=3, b=2
$$

$$
\text{Surface 2: Cross-sections } z = c \ (|c| > 0) \implies \text{ellipses } \frac{x^2}{(|c|/2)^2} + \frac{y^2}{|c|^2} = 1 \text{ with axis ratio } \frac{b}{a} = 2
$$

$$
x=0 \implies z = \pm y \ (\text{slope } \pm 1), \qquad y=0 \implies z = \pm 2x \ (\text{slope } \pm 2)
$$

$$
\text{Surface 2 identified as: Elliptic cone with apex at } (0,0,0) \text{ opening along } Oz
$$

---

## Verification

**Pass 1 — Algebraic check:** For curve 1, expanding the canonical form gives $4(x^2 - 2x + 1) + 9(y^2 + 4y + 4) = 36 \iff 4x^2 + 9y^2 - 8x + 36y + 4 + 36 - 36 = 0 \iff 4x^2 + 9y^2 - 8x + 36y + 4 = 0$. For surface 2, test homogeneity: $4(tx)^2 + (ty)^2 = t^2(4x^2 + y^2) = t^2 z^2 = (tz)^2$, which confirms that the surface is generated by straight lines through the origin (a cone).

**Pass 2 — Numerical check:**
- On the ellipse, the minor vertex $(1, 0)$ satisfies $4(1)^2 + 9(0)^2 - 8(1) + 36(0) + 4 = 4 - 8 + 4 = 0$.
- On the elliptic cone, at $z = 4$, the semiaxes are $a = 2$ and $b = 4$. Check boundary points: $(2, 0, 4) \implies 4(4) + 0 = 16 = 4^2$; $(0, 4, 4) \implies 0 + 16 = 16 = 4^2$. Both lie exactly on the surface.

**Pass 3 — Consistency check:** The standard form of a quadric cone is $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c_0^2} = 0$. Rewriting $4x^2 + y^2 = z^2$ as $\frac{x^2}{(1/2)^2} + \frac{y^2}{1^2} - \frac{z^2}{1^2} = 0$ matches the canonical cone with $a = 1/2$, $b = 1$, and $c_0 = 1$.

---

## Exam tip

When analyzing an unknown quadratic surface, determine the vertical cuts first ($x=0$ and $y=0$) to find whether they are parabolas or lines, then use the horizontal slices ($z=c$) to establish the shape and scaling of the cross-sections.

# Exercise 3

**Problem:** For

$$
\frac{x^2}{25}+\frac{y^2}{9}=1,
$$

find the semiaxis lengths, the intercepts with the coordinate axes, and make a sketch. Explain along which axis the ellipse is more stretched and how this is visible in the equation.

---

## Relevant theorem / definition

The canonical equation of an ellipse centered at the origin with axes aligned with the coordinate axes is:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
$$

where $a > 0$ and $b > 0$ denote the horizontal and vertical semiaxis lengths. If $a > b$, the ellipse is elongated horizontally with focal points along the $x$-axis.

---

## Solution

1. Identify the semiaxis lengths:
   - Comparing $\frac{x^2}{25} + \frac{y^2}{9} = 1$ with standard form gives $a^2 = 25$ and $b^2 = 9$.
   - Semiaxis along $x$: $a = \sqrt{25} = 5$.
   - Semiaxis along $y$: $b = \sqrt{9} = 3$.

2. Compute the intercepts with the coordinate axes:
   - Setting $y = 0$:

$$
\frac{x^2}{25} = 1 \implies x^2 = 25 \implies x = \pm 5
$$

     The $x$-intercepts (vertices on the major axis) are $(-5, 0)$ and $(5, 0)$.
   - Setting $x = 0$:

$$
\frac{y^2}{9} = 1 \implies y^2 = 9 \implies y = \pm 3
$$

     The $y$-intercepts (co-vertices on the minor axis) are $(0, -3)$ and $(0, 3)$.

3. Axis of greater stretching and algebraic explanation:
   The ellipse is more stretched along the $x$-axis. In the canonical equation, each denominator represents the square of the maximum reach along that coordinate direction. Since $25 > 9$, we have $a = 5 > b = 3$. To keep the sum $\frac{x^2}{25} + \frac{y^2}{9} = 1$ bounded by 1, the variable with the larger denominator is allowed to take on larger numerical values ($|x| \le 5$ versus $|y| \le 3$).

4. Sketch of the curve:
   The ellipse is symmetric with respect to both the $x$-axis, the $y$-axis, and the origin $(0,0)$.

```text
                     y
                     ^
                     | (0, 3)
               .-----+-----.
            .-'      |      '-.
          .'         |         '.
        /            |            \
  -----+-------------+-------------+-----> x
    (-5, 0)          |           (5, 0)
        \            |            /
          '.         |         .'
            '-.      |      .-'
               '-----+-----'
                     | (0, -3)
```

---

## Result

$$
\text{Horizontal semiaxis: } a = 5, \qquad \text{Vertical semiaxis: } b = 3
$$

$$
x\text{-intercepts: } (\pm 5, 0), \qquad y\text{-intercepts: } (0, \pm 3)
$$

$$
\text{More stretched along the } x\text{-axis because } 25 > 9 \implies a = 5 > b = 3
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the focal distance $c = \sqrt{a^2 - b^2} = \sqrt{25 - 9} = \sqrt{16} = 4$. Foci are $F_1 = (-4, 0)$ and $F_2 = (4, 0)$. For any point $P$ on the ellipse, the sum of focal distances must equal $2a = 10$. Test $P = (0, 3)$:

$$
d(P, F_1) + d(P, F_2) = \sqrt{(-4 - 0)^2 + (0 - 3)^2} + \sqrt{(4 - 0)^2 + (0 - 3)^2} = \sqrt{16 + 9} + \sqrt{16 + 9} = 5 + 5 = 10
$$

**Pass 2 — Numerical check:** Test an intermediate point with $x = 4$:

$$
\frac{4^2}{25} + \frac{y^2}{9} = 1 \implies \frac{y^2}{9} = 1 - \frac{16}{25} = \frac{9}{25} \implies y^2 = \frac{81}{25} \implies y = \pm \frac{9}{5} = \pm 1.8
$$

Check: $\frac{16}{25} + \frac{3.24}{9} = 0.64 + 0.36 = 1.00$.

**Pass 3 — Consistency check:** Since $a > b$, the ratio of axes is $\frac{a}{b} = \frac{5}{3} \approx 1.67 > 1$, confirming horizontal elongation. Setting $b \to a = 5$ would yield the circle of radius 5, which encloses this ellipse.

---

## Exam tip

The larger denominator always identifies the major axis; the square root of that denominator gives the maximum distance from the center along that coordinate axis.

# Exercise 1

**Problem:** Recognize the curves

$$
x^2+y^2=9,
$$

$$
\frac{x^2}{16}+\frac{y^2}{9}=1,
$$

$$
y^2=8x,
$$

$$
\frac{x^2}{9}-\frac{y^2}{4}=1.
$$

For each one, identify the most important features and make a sketch. Explain which parts of the equation let you recognize the type of curve.

---

## Relevant theorem / definition

The general second-degree curve in the plane is given by $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$. When axes are aligned with coordinate axes ($B=0$):
- Circle: $x^2 + y^2 = R^2$ ($A = C > 0$).
- Ellipse: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($A, C > 0$, $A \neq C$).
- Parabola: $y^2 = 2px$ or $x^2 = 2py$ (one quadratic term, one linear term).
- Hyperbola: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ or $\frac{y^2}{b^2} - \frac{x^2}{a^2} = 1$ ($A$ and $C$ have opposite signs).

---

## Solution

### 1. Curve $x^2+y^2=9$

- **Recognition:** Both variables $x$ and $y$ appear squared with equal positive coefficients ($1$) and no linear or cross terms. This is a circle in canonical form centered at the origin.
- **Key features:**
  - Center: $(0,0)$.
  - Radius: $R = \sqrt{9} = 3$.
  - Intercepts: $(\pm 3, 0)$ on the $x$-axis, $(0, \pm 3)$ on the $y$-axis.
- **Sketch characterization:**
  Symmetric about both axes and the origin. A circle of radius 3 centered at $(0,0)$.

```text
               y
               ^
               |   (0, 3)
           .---+---.
        .-'    |    '-.
       /       |       \
  ----+--------+--------+----> x
  (-3,0)       |      (3,0)
       \       |       /
        '-.    |    .-'
           '---+---'
               |   (0, -3)
```

---

### 2. Curve $\frac{x^2}{16}+\frac{y^2}{9}=1$

- **Recognition:** Both variables are squared with positive, unequal coefficients ($\frac{1}{16}$ and $\frac{1}{9}$), summed to 1. This is an ellipse in canonical form centered at the origin.
- **Key features:**
  - Center: $(0,0)$.
  - Semiaxis lengths: horizontal $a = \sqrt{16} = 4$, vertical $b = \sqrt{9} = 3$.
  - Intercepts: $(\pm 4, 0)$ on the $x$-axis, $(0, \pm 3)$ on the $y$-axis.
  - Linear eccentricity: $c = \sqrt{a^2 - b^2} = \sqrt{16 - 9} = \sqrt{7}$.
  - Foci: $F_1 = (-\sqrt{7}, 0)$, $F_2 = (\sqrt{7}, 0)$ along the major axis ($x$-axis).
- **Sketch characterization:**
  Elongated horizontally because $a = 4 > b = 3$. Smooth closed oval passing through $(\pm 4, 0)$ and $(0, \pm 3)$.

```text
                  y
                  ^
                  |  (0, 3)
             .----+----.
          .-'     |     '-.
        /         |         \
  -----+----------+----------+-----> x
     (-4, 0)      |        (4, 0)
        \         |         /
          '-.     |     .-'
             '----+----'
                  |  (0, -3)
```

---

### 3. Curve $y^2=8x$

- **Recognition:** The variable $y$ is squared while $x$ appears to the first power. This defines a parabola with a horizontal axis of symmetry.
- **Key features:**
  - Vertex: $(0,0)$.
  - Axis of symmetry: $y = 0$ ($x$-axis).
  - Opening direction: $x = \frac{y^2}{8} \ge 0$, so it opens to the right.
  - Parameter: $2p = 8 \implies p = 4$.
  - Focus: $(\frac{p}{2}, 0) = (2, 0)$. Directrix: $x = -2$.
  - Guide points: for $x = 2$, $y = \pm 4$; for $x = 8$, $y = \pm 8$.
- **Sketch characterization:**
  U-shaped curve lying entirely in the half-plane $x \ge 0$, opening symmetrically about the positive $x$-axis.

```text
               y
               ^
               |       * (2, 4)
               |     .
               |   .'
               |  /
  -------------+-V-----------*--------> x
        x = -2 |(0,0)      (2,0)
               |  \
               |   '.
               |     .
               |       * (2, -4)
```

---

### 4. Curve $\frac{x^2}{9}-\frac{y^2}{4}=1$

- **Recognition:** Both variables are squared, but their terms have opposite signs ($+$ for $x^2$, $-$ for $y^2$). This is a hyperbola opening along the $x$-axis.
- **Key features:**
  - Center: $(0,0)$.
  - Transverse semiaxis: $a = \sqrt{9} = 3$ (along $x$-axis).
  - Conjugate semiaxis: $b = \sqrt{4} = 2$ (along $y$-axis).
  - Vertices: $(-3, 0)$ and $(3, 0)$.
  - $y$-intercepts: none (setting $x=0$ yields $-\frac{y^2}{4} = 1$, no real solution).
  - Asymptotes: lines obtained by setting the right-hand side to 0:

$$
\frac{x^2}{9} - \frac{y^2}{4} = 0 \implies y = \pm \frac{2}{3}x
$$

  - Linear eccentricity: $c = \sqrt{a^2 + b^2} = \sqrt{9 + 4} = \sqrt{13}$. Foci: $(\pm\sqrt{13}, 0)$.
- **Sketch characterization:**
  Two separate branches opening left ($x \le -3$) and right ($x \ge 3$), approaching the asymptotes $y = \pm \frac{2}{3}x$ as $|x| \to \infty$.

```text
               y
        \      ^      /   asymptotes y = ±(2/3)x
         \     |     /
     branch\   |   / branch
       (  \    |    /  )
  -----+---+---+---+---+-----> x
    (-3,0)  \  |  /  (3,0)
             \ | /
              \|/
               |
```

---

## Result

$$
x^2+y^2=9: \quad \text{Circle, center } (0,0), \text{ radius } R=3
$$

$$
\frac{x^2}{16}+\frac{y^2}{9}=1: \quad \text{Ellipse, center } (0,0), \text{ semiaxes } a=4, b=3
$$

$$
y^2=8x: \quad \text{Parabola, vertex } (0,0), \text{ opens right along } y=0, \text{ focus } (2,0)
$$

$$
\frac{x^2}{9}-\frac{y^2}{4}=1: \quad \text{Hyperbola, center } (0,0), \text{ vertices } (\pm 3,0), \text{ asymptotes } y = \pm \frac{2}{3}x
$$

---

## Verification

**Pass 1 — Algebraic check:** Substitute representative points into each equation: for the circle, $(3,0) \implies 3^2+0^2=9$; for the ellipse, $(0,3) \implies 0 + \frac{9}{9} = 1$; for the parabola, $(2,4) \implies 4^2 = 16 = 8(2)$; for the hyperbola, $(3,0) \implies \frac{9}{9} - 0 = 1$.

**Pass 2 — Numerical check:** For the hyperbola asymptotes, evaluate $x=30$: the curve gives $y = 2\sqrt{\frac{900}{9}-1} = 2\sqrt{99} \approx 19.8997$, while the asymptote gives $y = \frac{2}{3}(30) = 20$. The relative discrepancy is $<0.5\%$.

**Pass 3 — Consistency check:** The signs of the quadratic terms dictate boundedness: circle and ellipse have identical positive signs, bounding $(x,y)$ to compact regions $[-3,3]\times[-3,3]$ and $[-4,4]\times[-3,3]$; parabola has one variable unbounded in one direction; hyperbola has opposite signs, unbounded as $|x| \to \infty$.

---

## Exam tip

Identify curve types instantly by quadratic signs: same sign and equal coefficients gives a circle, same sign and unequal coefficients gives an ellipse, opposite signs gives a hyperbola, and only one squared variable gives a parabola.

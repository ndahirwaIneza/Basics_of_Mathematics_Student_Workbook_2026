# Exercise 10

**Problem:** Compare

$$
z=x^2+y^2
$$

and

$$
z=x^2-y^2.
$$

For each surface, describe the cross-sections $x=0$, $y=0$, and $z=c$, then make a qualitative sketch.

---

## Relevant theorem / definition

- An **elliptic (circular) paraboloid** $z = \frac{x^2}{a^2} + \frac{y^2}{b^2}$ has vertical cross-sections that are parabolas opening in the same direction, and horizontal cross-sections that are ellipses (or circles).
- A **hyperbolic paraboloid** $z = \frac{x^2}{a^2} - \frac{y^2}{b^2}$ has vertical cross-sections that are parabolas opening in opposite directions, and horizontal cross-sections that are hyperbolas (or intersecting lines at $z=0$).

---

## Solution

### 1. Surface $z = x^2 + y^2$ (Circular Paraboloid)

1. Cross-section by the plane $x = 0$:

$$
z = 0^2 + y^2 \implies z = y^2
$$

   This is a parabola in the $yz$-plane with vertex at $(0,0,0)$ opening upwards along the positive $z$-axis.

2. Cross-section by the plane $y = 0$:

$$
z = x^2 + 0^2 \implies z = x^2
$$

   This is a parabola in the $xz$-plane with vertex at $(0,0,0)$ opening upwards along the positive $z$-axis.

3. Cross-sections by the planes $z = c$:
   - **For $c > 0$:** $x^2 + y^2 = c$, which is a circle in the horizontal plane $z = c$ centered at $(0,0,c)$ with radius $R = \sqrt{c}$.
   - **For $c = 0$:** $x^2 + y^2 = 0 \implies (0,0,0)$, which is a single point (the global minimum / vertex).
   - **For $c < 0$:** $x^2 + y^2 = c < 0$, which has no real solutions (empty set). The surface lies entirely in the upper half-space $z \ge 0$.

4. Qualitative sketch: A bowl-shaped surface with circular contours expanding as height $z$ increases.

```text
               z
               ^
          \    |    /     z = c (circle)
           \   |   /
            \  |  /
             '-+-'
               | (0,0,0)
  -------------+-------------> x
```

---

### 2. Surface $z = x^2 - y^2$ (Hyperbolic Paraboloid)

1. Cross-section by the plane $x = 0$:

$$
z = 0^2 - y^2 \implies z = -y^2
$$

   This is a parabola in the $yz$-plane with vertex at $(0,0,0)$ opening **downwards** along the negative $z$-axis.

2. Cross-section by the plane $y = 0$:

$$
z = x^2 - 0^2 \implies z = x^2
$$

   This is a parabola in the $xz$-plane with vertex at $(0,0,0)$ opening **upwards** along the positive $z$-axis.

3. Cross-sections by the planes $z = c$:
   - **For $c > 0$:** $x^2 - y^2 = c \iff \frac{x^2}{c} - \frac{y^2}{c} = 1$. This is a hyperbola in the plane $z = c$ with vertices at $(\pm\sqrt{c}, 0, c)$, opening along the $x$-axis with asymptotes $y = \pm x$.
   - **For $c = 0$:** $x^2 - y^2 = 0 \iff (x - y)(x + y) = 0$. This represents a pair of intersecting straight lines $y = x$ and $y = -x$ in the plane $z = 0$.
   - **For $c < 0$:** $x^2 - y^2 = c \iff y^2 - x^2 = -c = |c|$. This is a hyperbola in the plane $z = c$ with vertices at $(0, \pm\sqrt{|c|}, c)$, opening along the $y$-axis with asymptotes $y = \pm x$.

4. Qualitative sketch: A saddle surface. The origin $(0,0,0)$ is a saddle point (minimax point).

```text
               z
               ^
          \    |    /     curves UP along x (z = x^2)
           \   |   /
            \  |  /
  -------------+-------------> x
              /|\
             / | \        curves DOWN along y (z = -y^2)
            /  |  \
```

---

## Result

$$
z = x^2 + y^2: \quad \text{Circular paraboloid (bowl)}
$$

$$
x=0 \implies z = y^2 \text{ (upward parabola)}, \quad y=0 \implies z = x^2 \text{ (upward parabola)}, \quad z=c>0 \implies x^2+y^2=c \text{ (circle)}
$$

$$
z = x^2 - y^2: \quad \text{Hyperbolic paraboloid (saddle)}
$$

$$
x=0 \implies z = -y^2 \text{ (downward parabola)}, \quad y=0 \implies z = x^2 \text{ (upward parabola)}, \quad z=c \implies x^2-y^2=c \text{ (hyperbola / lines)}
$$

---

## Verification

**Pass 1 — Algebraic check:** The Hessian matrix of $f(x,y) = x^2 + y^2$ is $H = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$ with $\det(H) = 4 > 0$ and $f_{xx} = 2 > 0$, confirming a strict local minimum at $(0,0)$. For $g(x,y) = x^2 - y^2$, the Hessian is $H = \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}$ with $\det(H) = -4 < 0$, confirming a saddle point.

**Pass 2 — Numerical check:** For $z = x^2 + y^2$, evaluate $(x,y) = (2, 3) \implies z = 4 + 9 = 13 > 0$. For $z = x^2 - y^2$, evaluate $(2, 3) \implies z = 4 - 9 = -5 < 0$, and $(3, 2) \implies z = 9 - 4 = +5 > 0$, demonstrating that $z$ changes sign across the lines $y = \pm x$.

**Pass 3 — Consistency check:** Gaussian curvature $K$: for $z = x^2 + y^2$, $K = \frac{4}{(1 + 4x^2 + 4y^2)^2} > 0$ everywhere (elliptic geometry). For $z = x^2 - y^2$, $K = \frac{-4}{(1 + 4x^2 + 4y^2)^2} < 0$ everywhere (hyperbolic geometry).

---

## Exam tip

To quickly identify the shape of $z = Ax^2 + By^2$, check the signs of $A$ and $B$: matching signs produce a bowl (elliptic paraboloid), while opposite signs produce a saddle (hyperbolic paraboloid).

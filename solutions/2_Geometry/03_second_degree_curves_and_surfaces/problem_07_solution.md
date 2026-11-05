# Exercise 7

**Problem:** Determine the type of object described by:
1. $4x^2+9y^2=36$,
2. $x^2-y^2=1$,
3. $x^2-4y=0$,
4. $x^2+y^2+1=0$.

In the last case, explain why there are no real points.

---

## Relevant theorem / definition

A second-degree equation $Ax^2 + Cy^2 + Dx + Ey + F = 0$ (with $B = 0$) is classified by the sign of $AC$:
- $AC > 0$: Elliptic type (ellipse, single point, or empty set over $\mathbb{R}$).
- $AC < 0$: Hyperbolic type (hyperbola or pair of intersecting lines).
- $AC = 0$ (with one non-zero quadratic coefficient and linear dependency in the other): Parabolic type (parabola).

For any real number $u \in \mathbb{R}$, $u^2 \ge 0$.

---

## Solution

### 1. Equation $4x^2+9y^2=36$

Divide both sides by $36$:

$$
\frac{4x^2}{36} + \frac{9y^2}{36} = 1 \iff \frac{x^2}{9} + \frac{y^2}{4} = 1
$$

- Both quadratic coefficients are strictly positive ($A = 4, C = 9 \implies AC > 0$) and unequal.
- Standard form: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ with $a = 3$ and $b = 2$.
- **Object:** Ellipse centered at $(0,0)$ with horizontal major axis of length $2a = 6$ and vertical minor axis of length $2b = 4$.

---

### 2. Equation $x^2-y^2=1$

Write in canonical form:

$$
\frac{x^2}{1^2} - \frac{y^2}{1^2} = 1
$$

- The quadratic coefficients have opposite signs ($A = 1, C = -1 \implies AC = -1 < 0$).
- Here $a = b = 1$, so the asymptotes are $y = \pm x$, which are mutually perpendicular.
- **Object:** Equilateral (rectangular) hyperbola centered at $(0,0)$ with vertices at $(-1, 0)$ and $(1, 0)$, opening horizontally.

---

### 3. Equation $x^2-4y=0$

Solve for the linear variable $y$:

$$
y = \frac{1}{4}x^2 \iff x^2 = 4y
$$

- Exactly one variable is squared ($x^2$) while the other is linear ($y$).
- Canonical form: $x^2 = 2py$ with $2p = 4 \implies p = 2$.
- **Object:** Parabola with vertex at $(0,0)$, axis of symmetry along the $y$-axis ($x = 0$), opening upwards ($y \ge 0$), with focus at $(0, 1)$ and directrix $y = -1$.

---

### 4. Equation $x^2+y^2+1=0$

Rearrange the equation:

$$
x^2 + y^2 = -1
$$

**Why there are no real points:**
For any real numbers $x \in \mathbb{R}$ and $y \in \mathbb{R}$:

$$
x^2 \ge 0 \qquad \text{and} \qquad y^2 \ge 0
$$

Summing these two inequalities gives:

$$
x^2 + y^2 \ge 0
$$

Adding $1$ to both sides yields:

$$
x^2 + y^2 + 1 \ge 1 > 0 \qquad \text{for all } (x, y) \in \mathbb{R}^2
$$

The left-hand side is strictly positive for every choice of real coordinates $(x, y)$, so it can never equal zero.
- **Object:** Empty set $\emptyset$ (also termed an imaginary or degenerate ellipse / circle).

---

## Result

$$
4x^2+9y^2=36: \quad \text{Ellipse, center } (0,0), \text{ semiaxes } a=3, b=2
$$

$$
x^2-y^2=1: \quad \text{Equilateral hyperbola, center } (0,0), \text{ vertices } (\pm 1, 0), \text{ asymptotes } y = \pm x
$$

$$
x^2-4y=0: \quad \text{Parabola, vertex } (0,0), \text{ axis } x=0, \text{ opens upwards}
$$

$$
x^2+y^2+1=0: \quad \text{Empty set } \emptyset \text{ (no real points, since } x^2+y^2+1 \ge 1 > 0 \text{ for all } x,y \in \mathbb{R})
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the conic discriminant $\delta = -4AC$ (from $B^2 - 4AC$ with $B=0$):
- (1) $\delta = -4(4)(9) = -144 < 0 \implies$ ellipse.
- (2) $\delta = -4(1)(-1) = 4 > 0 \implies$ hyperbola.
- (3) $\delta = -4(1)(0) = 0 \implies$ parabola.
- (4) $\delta = -4(1)(1) = -4 < 0 \implies$ elliptic type, but constant term $F = 1 > 0$ means the level set is below the minimum value $0$, giving no real solutions.

**Pass 2 — Numerical check:** For (3), test $x = 4 \implies y = \frac{1}{4}(16) = 4$; checking $4^2 - 4(4) = 16 - 16 = 0$. For (4), evaluating at the origin $(0,0)$ gives $0^2 + 0^2 + 1 = 1 \neq 0$, which is the minimum value achievable.

**Pass 3 — Consistency check:** Over the complex numbers $\mathbb{C}$, $x^2 + y^2 = -1$ defines a circle of radius $R = \sqrt{-1} = i$. Over the real field $\mathbb{R}$, a sum of squares cannot equal a strictly negative quantity.

---

## Exam tip

Before doing algebraic operations on a second-degree curve, verify that the right-hand constant allows real solutions; a sum of non-negative squares set to a negative number is always the empty set.

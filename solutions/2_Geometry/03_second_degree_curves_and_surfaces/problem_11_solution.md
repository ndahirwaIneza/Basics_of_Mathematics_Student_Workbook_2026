# Exercise 11

**Problem:** Compare

$$
x^2+y^2-z^2=1
$$

and

$$
x^2+y^2-z^2=-1.
$$

For several values $z=c$, check whether the cross-section exists and what its radius is. Based on this, describe qualitatively the difference between the surfaces and make sketches.

---

## Relevant theorem / definition

The standard hyperboloids of revolution around the $z$-axis are:
- **Hyperboloid of one sheet:** $x^2 + y^2 - z^2 = 1 \iff x^2 + y^2 = 1 + z^2$. It is a single connected surface.
- **Hyperboloid of two sheets:** $x^2 + y^2 - z^2 = -1 \iff x^2 + y^2 = z^2 - 1$. It consists of two disconnected components separated by a gap along the axis of symmetry.

Both surfaces share the same asymptotic cone $x^2 + y^2 - z^2 = 0$.

---

## Solution

### 1. Surface $x^2+y^2-z^2=1$ (Hyperboloid of One Sheet)

Express the horizontal cross-sections at height $z = c$:

$$
x^2 + y^2 = 1 + c^2
$$

Because $1 + c^2 \ge 1 > 0$ for all real numbers $c$, a real cross-section exists for **every** $c \in \mathbb{R}$. Each cross-section is a circle with radius:

$$
r(c) = \sqrt{1 + c^2}
$$

Evaluate at representative heights:
- $z = 0$: $r(0) = \sqrt{1 + 0} = 1$ (the narrowest section, known as the throat or waist circle).
- $z = \pm 1$: $r(\pm 1) = \sqrt{1 + 1} = \sqrt{2} \approx 1.414$.
- $z = \pm \sqrt{3}$: $r(\pm \sqrt{3}) = \sqrt{1 + 3} = 2$.
- $z = \pm 3$: $r(\pm 3) = \sqrt{1 + 9} = \sqrt{10} \approx 3.162$.

**Qualitative shape:**
A single connected, hollow hourglass-shaped surface. It has no gaps along the $z$-axis; it narrows to a minimum radius of $1$ at the equatorial plane $z=0$ and widens continuously as $|z| \to \infty$.

```text
               z
        \      ^      /
         )     |     (
        (   ---|---   )      z = c (circle)
         '.    |    .'
           |---+---|         z = 0 (waist circle, r = 1)
         .'    |    '.
        (   ---|---   )
         )     |     (
        /      |      \------> x
```

---

### 2. Surface $x^2+y^2-z^2=-1$ (Hyperboloid of Two Sheets)

Express the horizontal cross-sections at height $z = c$:

$$
x^2 + y^2 = c^2 - 1
$$

The existence of real points requires $c^2 - 1 \ge 0 \iff |c| \ge 1$.

Evaluate across regions and specific heights:
- **For $|c| < 1$ (e.g. $z = 0$, $z = \pm 0.5$):** $c^2 - 1 < 0$. No real points exist. The slab $-1 < z < 1$ is completely empty.
- **For $z = \pm 1$:** $c^2 - 1 = 0 \implies x^2 + y^2 = 0$. The cross-section degenerates to single points: the vertices $(0, 0, 1)$ and $(0, 0, -1)$.
- **For $|c| > 1$:** The cross-section is a circle of radius:

$$
r(c) = \sqrt{c^2 - 1}
$$

  - $z = \pm \sqrt{2}$: $r = \sqrt{2 - 1} = 1$.
  - $z = \pm 2$: $r = \sqrt{4 - 1} = \sqrt{3} \approx 1.732$.
  - $z = \pm \sqrt{5}$: $r = \sqrt{5 - 1} = 2$.

**Qualitative shape:**
Two separate, disconnected convex sheets (two oppositely oriented bowls): an upper sheet opening upwards for $z \ge 1$ with vertex at $(0, 0, 1)$, and a lower sheet opening downwards for $z \le -1$ with vertex at $(0, 0, -1)$.

```text
               z
        \      ^      /      upper sheet (z >= 1)
         \     |     /
          '.---+---.'
               * (0, 0, 1)
               |
  -------------+-------------> x   gap: no points for -1 < z < 1
               |
               * (0, 0, -1)
          .----+----.
         /     |     \       lower sheet (z <= -1)
        /      |      \
```

---

## Result

$$
x^2+y^2-z^2=1: \quad \text{Hyperboloid of one sheet (connected), exists for all } z, \ r(c) = \sqrt{1 + c^2} \ge 1
$$

$$
x^2+y^2-z^2=-1: \quad \text{Hyperboloid of two sheets (disconnected), exists only for } |z| \ge 1, \ r(c) = \sqrt{c^2 - 1}
$$

---

## Verification

**Pass 1 — Algebraic check:** Intersections with the coordinate axes:
- For $x^2 + y^2 - z^2 = 1$: setting $x=y=0$ gives $-z^2 = 1$, which has no real solutions (no $z$-axis intersection, confirming the tube surrounds the axis). Setting $z=0$ gives $x^2 + y^2 = 1$ (the waist circle).
- For $x^2 + y^2 - z^2 = -1$: setting $z=0$ gives $x^2 + y^2 = -1$ (no real intersection with the $xy$-plane). Setting $x=y=0$ gives $-z^2 = -1 \implies z = \pm 1$ (two real vertices along the $z$-axis).

**Pass 2 — Numerical check:** At $z = 2$:
- Surface 1 has radius $r_1 = \sqrt{1 + 4} = \sqrt{5} \approx 2.236$.
- Surface 2 has radius $r_2 = \sqrt{4 - 1} = \sqrt{3} \approx 1.732$.
Notice that $r_1^2 - r_2^2 = (1 + c^2) - (c^2 - 1) = 2$ is constant for all $|c| \ge 1$.

**Pass 3 — Consistency check:** For large $|z|$, $\sqrt{1 + z^2} \approx |z|$ and $\sqrt{z^2 - 1} \approx |z|$. Both surfaces approach the common asymptotic cone $x^2 + y^2 = z^2$ from opposite sides: the one-sheeted hyperboloid from outside ($r > |z|$) and the two-sheeted hyperboloid from inside ($r < |z|$).

---

## Exam tip

The sign on the right-hand side determines the sheet topology: a positive constant ($+1$) leaves a waist and forms one connected sheet; a negative constant ($-1$) creates an empty zone around the center and splits the surface into two sheets.

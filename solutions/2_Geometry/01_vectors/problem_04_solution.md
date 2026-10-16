# Exercise 4

**Problem:** For $u=(1,2,-1)$ and $v=(2,-1,3)$ compute $u\cdot v$ and determine whether the vectors are perpendicular. Then find $a$ so that $w=(2,-1,a)$ is perpendicular to $u$, and check the result.

---

## Relevant theorem / definition

The dot product of two vectors $\mathbf{u} = (u_1, u_2, u_3)$ and $\mathbf{v} = (v_1, v_2, v_3)$ in $\mathbb{R}^3$ is defined as
$$
\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3.
$$
Two non-zero vectors $\mathbf{u}$ and $\mathbf{v}$ are perpendicular (orthogonal), denoted $\mathbf{u} \perp \mathbf{v}$, if and only if their dot product equals zero:
$$
\mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0.
$$

---

## Solution

1. Computation of $u \cdot v$:
   $$
   u \cdot v = (1)(2) + (2)(-1) + (-1)(3) = 2 - 2 - 3 = -3
   $$

2. Perpendicularity of $u$ and $v$:
   Since $u \cdot v = -3 \neq 0$, the vectors $u$ and $v$ are not perpendicular.

3. Determination of $a$ such that $w = (2, -1, a) \perp u$:
   Set the dot product $w \cdot u$ to zero:
   $$
   w \cdot u = (2)(1) + (-1)(2) + (a)(-1) = 0
   $$
   Simplify the linear equation:
   $$
   2 - 2 - a = 0 \implies -a = 0 \implies a = 0
   $$
   Thus, the vector is $w = (2, -1, 0)$.

4. Verification of perpendicularity for $w$ and $u$:
   $$
   w \cdot u = (2)(1) + (-1)(2) + (0)(-1) = 2 - 2 + 0 = 0
   $$
   The condition $w \cdot u = 0$ holds.

---

## Result

$$
u \cdot v = -3 \implies u \text{ and } v \text{ are not perpendicular}
$$

$$
a = 0 \implies w = (2, -1, 0)
$$

---

## Verification

**Pass 1 — Algebraic check:** The dot product is symmetric: $v \cdot u = (2)(1) + (-1)(2) + (3)(-1) = 2 - 2 - 3 = -3 = u \cdot v$.

**Pass 2 — Numerical check:** For $w = (2, -1, 0)$ and $u = (1, 2, -1)$, substituting into the coordinate form gives $2(1) - 1(2) + 0(-1) = 0$.

**Pass 3 — Consistency check:** Since $u \cdot v = -3 < 0$, the angle between $u$ and $v$ is obtuse ($\theta > 90^\circ$), which is consistent with the vectors pointing in opposite directions along their $z$-coordinates.

---

## Exam tip

The condition for orthogonality is always $\mathbf{u} \cdot \mathbf{v} = 0$; never confuse the dot product (which produces a scalar) with the cross product (which produces a vector).


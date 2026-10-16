# Exercise 1

**Problem:** For $u=(2,-1,3)$ and $v=(-1,4,2)$ compute
$$u+v,\qquad u-v,\qquad 3u-2v.$$
Then verify that $(u+v)-v=u$, and explain geometrically what adding two vectors means.

---

## Relevant theorem / definition

Vector addition and scalar multiplication in $\mathbb{R}^n$ are defined componentwise: for $\mathbf{u} = (u_1, \dots, u_n)$, $\mathbf{v} = (v_1, \dots, v_n)$, and $c \in \mathbb{R}$,
$$
\mathbf{u} \pm \mathbf{v} = (u_1 \pm v_1, \dots, u_n \pm v_n), \qquad c\mathbf{u} = (cu_1, \dots, cu_n).
$$
Geometrically, vector addition corresponds to sequential translation: placing the initial point of $\mathbf{v}$ at the terminal point of $\mathbf{u}$ yields the resultant vector $\mathbf{u}+\mathbf{v}$ connecting the initial point of $\mathbf{u}$ to the terminal point of $\mathbf{v}$ (triangle rule / parallelogram law).

---

## Solution

1. Vector sum $u+v$:
   $$
   u+v = (2 + (-1), -1 + 4, 3 + 2) = (1, 3, 5)
   $$

2. Vector difference $u-v$:
   $$
   u-v = (2 - (-1), -1 - 4, 3 - 2) = (3, -5, 1)
   $$

3. Linear combination $3u-2v$:
   $$
   3u = 3(2, -1, 3) = (6, -3, 9)
   $$
   $$
   2v = 2(-1, 4, 2) = (-2, 8, 4)
   $$
   $$
   3u-2v = (6 - (-2), -3 - 8, 9 - 4) = (8, -11, 5)
   $$

4. Verification of the identity $(u+v)-v=u$:
   $$
   (u+v)-v = (1, 3, 5) - (-1, 4, 2) = (1 - (-1), 3 - 4, 5 - 2) = (2, -1, 3) = u
   $$

5. Geometric interpretation:
   Adding two vectors represents the composition of two consecutive translations. When the tail of vector $v$ is attached to the head of vector $u$, the vector $u+v$ forms the diagonal of the parallelogram defined by $u$ and $v$ with origin at the tail of $u$.

---

## Result

$$
u+v = (1, 3, 5), \qquad u-v = (3, -5, 1), \qquad 3u-2v = (8, -11, 5)
$$

$$
(u+v)-v = (2, -1, 3) = u
$$

---

## Verification

**Pass 1 — Algebraic check:** By group axioms of vector addition in $\mathbb{R}^3$, $(u+v)-v = u + (v - v) = u + \mathbf{0} = u$. Also, $(u+v) + (u-v) = 2u$: $(1,3,5) + (3,-5,1) = (4,-2,6) = 2(2,-1,3) = 2u$.

**Pass 2 — Numerical check:** Recomputing the third coordinate of $3u-2v$: $3(3) - 2(2) = 9 - 4 = 5$, matching the entry in $(8, -11, 5)$.

**Pass 3 — Consistency check:** Since $u, v \in \mathbb{R}^3$, all resulting vectors belong to $\mathbb{R}^3$ and preserve linearity under coordinate projections.

---

## Exam tip

Distribute negative signs carefully across all vector components during subtraction, especially when subtracting negative numbers such as $2 - (-1) = 3$ and $6 - (-2) = 8$.


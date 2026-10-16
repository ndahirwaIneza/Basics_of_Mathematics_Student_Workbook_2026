# Exercise 6

**Problem:** Find the projection of $u=(4,2)$ onto the direction $v=(1,1)$. Then compute
$$r=u-\operatorname{proj}_v u$$
and verify that $r\cdot v=0$. Explain this result geometrically.

---

## Relevant theorem / definition

The orthogonal projection of a vector $\mathbf{u}$ onto a non-zero direction $\mathbf{v}$ is given by
$$
\operatorname{proj}_{\mathbf{v}} \mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2} \mathbf{v}.
$$
The residual vector $\mathbf{r} = \mathbf{u} - \operatorname{proj}_{\mathbf{v}} \mathbf{u}$ is the perpendicular component of $\mathbf{u}$ with respect to $\mathbf{v}$. Any vector $\mathbf{u}$ decomposes uniquely into a sum of parallel and perpendicular components: $\mathbf{u} = \mathbf{u}_{\parallel} + \mathbf{u}_{\perp}$, where $\mathbf{u}_{\parallel} = c\mathbf{v}$ and $\mathbf{u}_{\perp} \cdot \mathbf{v} = 0$.

---

## Solution

1. Computation of $\operatorname{proj}_v u$:
   Compute $u \cdot v$:
   $$
   u \cdot v = (4)(1) + (2)(1) = 4 + 2 = 6
   $$
   Compute $\|v\|^2$:
   $$
   \|v\|^2 = 1^2 + 1^2 = 2
   $$
   Compute the projection vector:
   $$
   \operatorname{proj}_v u = \frac{u \cdot v}{\|v\|^2} v = \frac{6}{2}(1, 1) = 3(1, 1) = (3, 3)
   $$

2. Computation of the perpendicular component $r$:
   $$
   r = u - \operatorname{proj}_v u = (4, 2) - (3, 3) = (4 - 3, 2 - 3) = (1, -1)
   $$

3. Verification that $r \cdot v = 0$:
   $$
   r \cdot v = (1)(1) + (-1)(1) = 1 - 1 = 0
   $$

4. Geometric explanation:
   The projection $\operatorname{proj}_v u = (3, 3)$ represents the orthogonal shadow of vector $u$ cast onto the line directed by $v$. The difference vector $r = (1, -1)$ connects the tip of the projection on the line to the tip of $u$. By construction of orthogonal projection, this connecting segment meets the line at a right angle ($90^\circ$), which geometrically guarantees that $r$ is perpendicular to $v$.

---

## Result

$$
\operatorname{proj}_v u = (3, 3)
$$

$$
r = u - \operatorname{proj}_v u = (1, -1)
$$

$$
r \cdot v = 0
$$

---

## Verification

**Pass 1 — Algebraic check:** Expanding $r \cdot v$ symbolically:
$$
r \cdot v = \left(u - \frac{u \cdot v}{\|v\|^2} v\right) \cdot v = u \cdot v - \frac{u \cdot v}{\|v\|^2} (v \cdot v) = u \cdot v - u \cdot v = 0
$$

**Pass 2 — Numerical check:** Verify the Pythagorean theorem: $\|u\|^2 = \|\operatorname{proj}_v u\|^2 + \|r\|^2$. Here $\|u\|^2 = 4^2 + 2^2 = 20$. $\|\operatorname{proj}_v u\|^2 = 3^2 + 3^2 = 18$, and $\|r\|^2 = 1^2 + (-1)^2 = 2$. Indeed, $18 + 2 = 20$.

**Pass 3 — Consistency check:** Since $\operatorname{proj}_v u = (3, 3) = 3(1, 1)$, it is clearly a scalar multiple of $v$, confirming that the parallel component is along the direction of $v$.

---

## Exam tip

Remember to divide by $\|\mathbf{v}\|^2$ (which is $v_1^2 + v_2^2$), not by $\|\mathbf{v}\|$, when computing the projection vector onto $\mathbf{v}$.


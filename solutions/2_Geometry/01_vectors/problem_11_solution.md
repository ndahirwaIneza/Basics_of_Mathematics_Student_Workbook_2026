# Exercise 11

**Problem:** Decompose $u=(3,4)$ into components parallel and perpendicular to $v=(1,2)$. Check
$$u=u_{\parallel}+u_{\perp},\qquad u_{\perp}\cdot v=0.$$
Explain why these are two independent checks of correctness.

---

## Relevant theorem / definition

Given a vector $\mathbf{u}$ and a non-zero reference vector $\mathbf{v}$, $\mathbf{u}$ admits a unique orthogonal decomposition:
$$
\mathbf{u} = \mathbf{u}_{\parallel} + \mathbf{u}_{\perp},
$$
where $\mathbf{u}_{\parallel}$ is parallel to $\mathbf{v}$ and $\mathbf{u}_{\perp}$ is perpendicular to $\mathbf{v}$:
$$
\mathbf{u}_{\parallel} = \operatorname{proj}_{\mathbf{v}} \mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2}\mathbf{v}, \qquad \mathbf{u}_{\perp} = \mathbf{u} - \mathbf{u}_{\parallel}.
$$

---

## Solution

1. Computation of $u_{\parallel}$ (parallel component):
   Compute the dot product $u \cdot v$:
   $$
   u \cdot v = (3)(1) + (4)(2) = 3 + 8 = 11
   $$
   Compute the squared norm $\|v\|^2$:
   $$
   \|v\|^2 = 1^2 + 2^2 = 1 + 4 = 5
   $$
   Compute $u_{\parallel}$:
   $$
   u_{\parallel} = \frac{u \cdot v}{\|v\|^2} v = \frac{11}{5}(1, 2) = \left(\frac{11}{5}, \frac{22}{5}\right)
   $$

2. Computation of $u_{\perp}$ (perpendicular component):
   $$
   u_{\perp} = u - u_{\parallel} = (3, 4) - \left(\frac{11}{5}, \frac{22}{5}\right) = \left(\frac{15}{5} - \frac{11}{5}, \frac{20}{5} - \frac{22}{5}\right) = \left(\frac{4}{5}, -\frac{2}{5}\right)
   $$

3. Checking the two conditions:
   - Condition 1 (Sum reconstitutes $u$):
     $$
     u_{\parallel} + u_{\perp} = \left(\frac{11}{5} + \frac{4}{5}, \frac{22}{5} - \frac{2}{5}\right) = \left(\frac{15}{5}, \frac{20}{5}\right) = (3, 4) = u
     $$
   - Condition 2 (Perpendicularity to $v$):
     $$
     u_{\perp} \cdot v = \left(\frac{4}{5}\right)(1) + \left(-\frac{2}{5}\right)(2) = \frac{4}{5} - \frac{4}{5} = 0
     $$

4. Reason why the two checks are independent:
   - The check $u = u_{\parallel} + u_{\perp}$ verifies **algebraic completeness** (the two parts sum to the total original vector without losing or adding extraneous components). However, infinitely many arbitrary pairs sum to $u$ (for example, $(0,0) + (3,4) = u$) without being perpendicular to $v$.
   - The check $u_{\perp} \cdot v = 0$ verifies **orthogonality** to the reference direction. However, infinitely many vectors are perpendicular to $v$ (for example, $(-2, 1)$) without having any relationship to $u$.
   - Only when *both* conditions hold simultaneously is the orthogonal decomposition verified as both correct and unique.

---

## Result

$$
u_{\parallel} = \left(\frac{11}{5}, \frac{22}{5}\right), \qquad u_{\perp} = \left(\frac{4}{5}, -\frac{2}{5}\right)
$$

$$
u_{\parallel} + u_{\perp} = (3, 4) = u, \qquad u_{\perp} \cdot v = 0
$$

---

## Verification

**Pass 1 — Algebraic check:** Since $u_{\parallel} = \frac{11}{5}v$, $u_{\parallel}$ is collinear with $v$. Then $u_{\parallel} \cdot u_{\perp} = \frac{11}{5}(v \cdot u_{\perp}) = \frac{11}{5}(0) = 0$, confirming the two components are orthogonal to each other.

**Pass 2 — Numerical check:** By Pythagorean theorem: $\|u\|^2 = \|u_{\parallel}\|^2 + \|u_{\perp}\|^2$. Here $\|u\|^2 = 3^2 + 4^2 = 25$. Then $\|u_{\parallel}\|^2 = \frac{121 + 484}{25} = \frac{605}{25} = \frac{121}{5}$, and $\|u_{\perp}\|^2 = \frac{16 + 4}{25} = \frac{20}{25} = \frac{4}{5}$. Adding them gives $\frac{121}{5} + \frac{4}{5} = \frac{125}{5} = 25$.

**Pass 3 — Consistency check:** The scalar projection factor is $\frac{11}{5} = 2.2 > 0$, consistent with $u$ and $v$ forming an acute angle ($u \cdot v = 11 > 0$).

---

## Exam tip

Keep fractions with a common denominator when computing $u - u_\parallel$ to eliminate arithmetic errors during subtraction.


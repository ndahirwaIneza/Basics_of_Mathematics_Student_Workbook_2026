# Exercise 10

**Problem:** Point $A$ lies on one bank of a river of width $100$ m, and point $B$ lies on the other bank, $500$ m along the bank from the point directly opposite $A$.

The cost per meter of cable underwater is twice the cost per meter of cable on land.

Build a cost function depending on the point where the cable comes out of the water, determine the domain, and find the solution that minimizes the cost.

---

## Relevant theorem / definition

For an objective function $C(x)$ on a closed interval $[a, b]$, absolute extrema occur at critical points where $C'(x) = 0$ or at the endpoints $a, b$. If $C''(x) > 0$ throughout $[a, b]$, any interior critical point is the unique global minimum on $[a, b]$.

---

## Solution

1. Geometric setup and cost function:
   Place the river in a Cartesian plane where the bank containing point $A$ lies along the line $y = 0$ with $A = (0, 0)$.
   The opposite bank lies along $y = 100$. The point directly across from $A$ is $A' = (0, 100)$, and point $B$ is located at $(500, 100)$.
   Let the cable cross underwater in a straight line from $A(0, 0)$ to a point $P(x, 100)$ on the opposite bank, where $x$ represents the downstream distance from $A'$.
   From $P(x, 100)$, the cable runs along the bank on land to $B(500, 100)$.
   The underwater length is given by the Pythagorean theorem:

   $$
   L_{\text{water}} = \sqrt{x^2 + 100^2} = \sqrt{x^2 + 10000}\quad [\text{m}]
   $$

   The distance on land is:

   $$
   L_{\text{land}} = 500 - x\quad [\text{m}]
   $$

   Let $c > 0$ denote the unit cost per meter on land; the unit cost underwater is $2c$.
   The total cost function is:

   $$
   C(x) = 2c \sqrt{x^2 + 10000} + c(500 - x) = c\left(2\sqrt{x^2 + 10000} + 500 - x\right)
   $$

2. Domain:
   The exit point $P$ must physically lie between the point directly opposite $A$ ($x = 0$) and the destination $B$ ($x = 500$):

   $$
   D_C = [0, 500]
   $$

3. Minimization of the cost function:
   Differentiate $C(x)$ with respect to $x$:

   $$
   \begin{align}
   C'(x) &= c\left(2 \cdot \frac{2x}{2\sqrt{x^2 + 10000}} - 1\right) \\
   &= c\left(\frac{2x}{\sqrt{x^2 + 10000}} - 1\right)
   \end{align}
   $$

   Set $C'(x) = 0$:

   $$
   \frac{2x}{\sqrt{x^2 + 10000}} = 1 \implies 2x = \sqrt{x^2 + 10000}
   $$

   Since $x \ge 0$, square both sides:

   $$
   4x^2 = x^2 + 10000 \implies 3x^2 = 10000 \implies x^2 = \frac{10000}{3}
   $$

   Taking the positive root:

   $$
   x = \frac{100}{\sqrt{3}} = \frac{100\sqrt{3}}{3} \approx 57.74\text{ m}
   $$

   Because $0 < 57.74 < 500$, this critical point is interior to the domain.

4. Second derivative and global optimality:
   Compute $C''(x)$:

   $$
   \begin{align}
   C''(x) &= c \cdot \frac{2\sqrt{x^2 + 10000} - 2x \cdot \frac{x}{\sqrt{x^2 + 10000}}}{x^2 + 10000} \\
   &= c \cdot \frac{2(x^2 + 10000) - 2x^2}{(x^2 + 10000)^{3/2}} \\
   &= \frac{20000c}{(x^2 + 10000)^{3/2}}
   \end{align}
   $$

   Since $C''(x) > 0$ for all $x \in [0, 500]$, the cost function is strictly convex on the entire domain. Hence, $x = \frac{100\sqrt{3}}{3}\text{ m}$ is the unique global minimum.

---

## Result

$$
C(x) = c\left(2\sqrt{x^2 + 10000} + 500 - x\right), \qquad D_C = [0, 500]
$$

$$
x = \frac{100\sqrt{3}}{3} \approx 57.74\text{ m}
$$

$$
C_{\min} = c(500 + 100\sqrt{3}) \approx 673.21c
$$

---

## Verification

**Pass 1 — Algebraic check:** The optimality condition $\frac{x}{\sqrt{x^2 + 100^2}} = \frac{1}{2}$ is equivalent to $\sin\theta = \frac{1}{2}$, where $\theta$ is the angle between the underwater path and the normal to the river bank. This gives $\theta = 30^\circ$, which is the exact Snell's law condition for refraction where the cost ratio plays the role of the refractive index $n = \frac{c_{\text{water}}}{c_{\text{land}}} = 2$.

**Pass 2 — Numerical check:** Compare the three candidate values:
- Straight across then land ($x = 0$): $C(0) = c(2 \times 100 + 500) = 700c$.
- Optimal exit point ($x = 57.74$): $C\left(\frac{100}{\sqrt{3}}\right) = c\left(2 \cdot \frac{200}{\sqrt{3}} + 500 - \frac{100}{\sqrt{3}}\right) = c(500 + 100\sqrt{3}) \approx 673.21c$.
- Direct underwater straight line to $B$ ($x = 500$): $C(500) = 2c\sqrt{500^2 + 100^2} = 2c\sqrt{260000} \approx 1019.80c$.
The critical point yields the lowest cost: $673.21c < 700c < 1019.80c$.

**Pass 3 — Consistency check:** If underwater cable cost were equal to land cost ($c_{\text{water}} = c_{\text{land}}$), the shortest Euclidean path would be optimal ($x = 500$). As underwater cost approaches infinity, $x \to 0$ (perpendicular crossing). With cost ratio 2, $x = 57.74\text{ m}$ lies strictly between 0 and 500.

---

## Exam tip

The optimal landing point $x = \frac{d}{\sqrt{k^2 - 1}}$ depends only on the river width $d$ and the cost ratio $k = \frac{c_{\text{water}}}{c_{\text{land}}}$, not on the total downstream distance $500\text{ m}$.

# Exercise 12

**Problem:** A museum wants to create a rectangular exhibition room next to an existing straight wall. The side along the wall does not need to be built. The remaining three sides are to be constructed to two different standards: the two sides perpendicular to the wall cost $300\ \mathrm{PLN/m}$ each, while the side parallel to the wall costs $500\ \mathrm{PLN/m}$. The budget is $30\,000\ \mathrm{PLN}$.

Build a model that maximizes the area of the room and prepare a complete analysis containing:

- definition of variables and units,
- mathematical model,
- domain resulting from the problem statement,
- computation of the derivative,
- determination and verification of the optimum,
- interpretation of the result,
- graph of the objective function,
- numerical verification of several values near the optimum found.

Finally, indicate which part of the solution required modeling the problem and which part was only the execution of the calculation. Produce the graph and computer calculations only after completing the mathematical solution, and treat them as verification.

---

## Relevant theorem / definition

For a differentiable function $f(x)$ on an open interval $(a, b)$, a point $x_0$ with $f'(x_0) = 0$ and $f''(x) \le 0$ for all $x \in (a, b)$ is a global maximum. For a quadratic function $f(x) = ax^2 + bx + c$ with $a < 0$, the graph is a concave parabola whose global maximum vertex occurs at $x = -\frac{b}{2a}$.

---

## Solution

1. Definition of variables and units:
   - $x$: length of each of the two walls perpendicular to the existing wall, measured in meters [$\text{m}$].
   - $y$: length of the wall parallel to the existing wall, measured in meters [$\text{m}$].
   - $c_x = 300\ \mathrm{PLN/m}$: unit cost of the perpendicular walls.
   - $c_y = 500\ \mathrm{PLN/m}$: unit cost of the parallel wall.
   - $B = 30\,000\ \mathrm{PLN}$: total construction budget.
   - $A$: floor area of the exhibition room, measured in square meters [$\text{m}^2$].

2. Mathematical model:
   The budget equation governing the construction of the three walls is:

   $$
   2 \cdot c_x \cdot x + c_y \cdot y = B
   $$

   Substitute the numerical parameters:

   $$
   2(300)x + 500y = 30000 \implies 600x + 500y = 30000
   $$

   Divide the constraint equation by 100:

   $$
   6x + 5y = 300
   $$

   Solve for $y$ in terms of $x$:

   $$
   y = 60 - \frac{6}{5}x = 60 - 1.2x
   $$

   The objective function is the floor area $A = x \cdot y$:

   $$
   A(x) = x\left(60 - \frac{6}{5}x\right) = 60x - \frac{6}{5}x^2
   $$

3. Domain resulting from the problem statement:
   Both physical dimensions must be strictly positive:

   $$
   x > 0 \quad \text{and} \quad y = 60 - 1.2x > 0 \implies x < \frac{60}{1.2} = 50
   $$

   Thus, the physically meaningful domain is:

   $$
   D_A = (0, 50)
   $$

4. Computation of the derivative:
   Differentiate $A(x)$ with respect to $x$:

   $$
   A'(x) = \frac{d}{dx}\left(60x - \frac{6}{5}x^2\right) = 60 - \frac{12}{5}x = 60 - 2.4x
   $$

5. Determination and verification of the optimum:
   Set the derivative to zero:

   $$
   60 - 2.4x = 0 \implies 2.4x = 60 \implies x = \frac{60}{2.4} = 25\text{ m}
   $$

   Substitute $x = 25\text{ m}$ into the constraint equation to determine $y$:

   $$
   y = 60 - 1.2(25) = 60 - 30 = 30\text{ m}
   $$

   Compute the maximum area:

   $$
   A(25) = 25 \cdot 30 = 750\text{ m}^2
   $$

   Verification via the second derivative:

   $$
   A''(x) = \frac{d}{dx}(60 - 2.4x) = -2.4
   $$

   Because $A''(x) = -2.4 < 0$ everywhere on $(0, 50)$, the function $A(x)$ is strictly concave, which guarantees that $x = 25\text{ m}$ is the unique global maximum.

6. Interpretation of the result:
   The optimal room design requires walls of length $x = 25\text{ m}$ extending outward from the museum wall and a front wall of length $y = 30\text{ m}$, enclosing an area of $750\text{ m}^2$.
   Examining the expenditure breakdown:
   - Cost of the two perpendicular walls: $2 \times 25\text{ m} \times 300\ \mathrm{PLN/m} = 15\,000\ \mathrm{PLN}$
   - Cost of the parallel wall: $30\text{ m} \times 500\ \mathrm{PLN/m} = 15\,000\ \mathrm{PLN}$
   The budget is allocated in exactly equal halves ($15\,000\ \mathrm{PLN}$ each, or 50% / 50%) between the perpendicular walls combined and the parallel wall. This demonstrates the economic principle of cost equipartition in linear budget allocation for rectangular areas.

7. Graph of the objective function:
   The function $A(x) = -\frac{6}{5}(x - 25)^2 + 750$ is a downward-opening parabola symmetric about the vertical line $x = 25$, with roots at $x = 0$ and $x = 50$:

   ```text
   A(x) [m^2]
     750 +-------------------------* (25, 750) -------------------------+
         |                     . '     ' .                          |
     600 |                  . '           ' .                       |
         |               . '                 ' .                    |
     450 |             . '                     ' .                  |
         |           . '                         ' .                |
     300 |         . '                             ' .              |
         |       . '                                 ' .            |
     150 |     . '                                     ' .          |
         |   . '                                         ' .        |
       0 +--*-----------------------------------------------*-------+
         0                 12.5       25       37.5        50     x [m]
   ```

8. Numerical verification near the optimum:
   Evaluating the model at several test points across the domain:

   | $x$ [m] | $y = 60 - 1.2x$ [m] | Total Cost [PLN] | Area $A = xy$ [$\text{m}^2$] | Difference from $A_{\max}$ |
   |:-------:|:-------------------:|:----------------:|:---------------------------:|:--------------------------:|
   | $10$    | $48.0$              | $30\,000$        | $480.0$                     | $-270.0$                   |
   | $20$    | $36.0$              | $30\,000$        | $720.0$                     | $-30.0$                    |
   | $24$    | $31.2$              | $30\,000$        | $748.8$                     | $-1.2$                     |
   | **$25$**| **$30.0$**          | **$30\,000$**    | **$750.0$**                 | **$0.0$ (optimum)**        |
   | $26$    | $28.8$              | $30\,000$        | $748.8$                     | $-1.2$                     |
   | $30$    | $24.0$              | $30\,000$        | $720.0$                     | $-30.0$                    |
   | $40$    | $12.0$              | $30\,000$        | $480.0$                     | $-270.0$                   |

   Every neighboring parameter choice strictly decreases the enclosed exhibition area.

9. Modeling vs. calculation classification:
   - **Modeling part:**
     - Identifying geometric dimensions ($x, y$) and economic parameters with their respective units ($[\text{m}]$, $[\mathrm{PLN/m}]$, $[\mathrm{PLN}]$).
     - Translating the worded budget restriction into the algebraic constraint $600x + 500y = 30000$.
     - Identifying that the museum wall requires no expenditure, breaking standard four-wall symmetry.
     - Formulating the area objective $A(x) = xy$ in terms of one decision variable $x$.
     - Establishing the physical validity domain $D_A = (0, 50)$ from $x > 0$ and $y > 0$.
     - Interpreting the 50/50 budget distribution in practical economic terms.
   - **Calculation part:**
     - Differentiating $A(x)$ to obtain $A'(x) = 60 - 2.4x$.
     - Solving the linear equation $A'(x) = 0$ for $x = 25$.
     - Computing the second derivative $A''(x) = -2.4$ to verify concavity.
     - Calculating the corresponding side length $y = 30$ and maximum area $750\text{ m}^2$.
     - Generating the numerical test table and plotting coordinates.

---

## Result

$$
A(x) = 60x - \frac{6}{5}x^2, \qquad D_A = (0, 50)
$$

$$
x = 25\text{ m}, \quad y = 30\text{ m}
$$

$$
A_{\max} = 750\text{ m}^2
$$

$$
\text{Budget split: } 15\,000\ \mathrm{PLN} \text{ (perpendicular walls) } / \ 15\,000\ \mathrm{PLN} \text{ (parallel wall)}
$$

---

## Verification

**Pass 1 — Algebraic check:** Rewrite $A(x)$ in vertex form by completing the square:

$$
A(x) = -\frac{6}{5}\left(x^2 - 50x\right) = -\frac{6}{5}\left((x - 25)^2 - 625\right) = -\frac{6}{5}(x - 25)^2 + 750
$$

Because $-\frac{6}{5}(x - 25)^2 \le 0$ for all real $x$, $A(x) \le 750$, with equality holding if and only if $x = 25$. This proves global optimality without calculus.

**Pass 2 — Numerical check:** By AM-GM inequality on the total budget:

$$
30000 = (600x) + (500y) \ge 2\sqrt{(600x)(500y)} = 2\sqrt{300000 xy}
$$

$$
15000 \ge \sqrt{300000 A} \implies 225\,000\,000 \ge 300\,000 A \implies A \le \frac{225\,000\,000}{300\,000} = 750
$$

Equality requires $600x = 500y = 15000$, yielding $x = 25\text{ m}$ and $y = 30\text{ m}$.

**Pass 3 — Consistency check:** At the boundaries $x = 0$ and $x = 50$, the area vanishes ($A(0) = A(50) = 0$). Symmetrical deviations from the vertex give identical area reductions: $A(25 - \delta) = A(25 + \delta) = 750 - 1.2\delta^2$, e.g., $A(24) = A(26) = 748.8\text{ m}^2$.

---

## Exam tip

When optimizing rectangular area under a linear cost budget, the total budget is always divided equally among the independent coordinate directions: half the budget goes to all walls in the $x$-direction, and half to all walls in the $y$-direction.

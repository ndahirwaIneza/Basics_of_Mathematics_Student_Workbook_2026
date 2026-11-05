# Exercise 15

**Problem:** Choose one function from the problem set and a point $x_0$ at which the derivative exists. Compute $f'(x_0)$ exactly, and then calculate
$$\frac{f(x_0+h)-f(x_0)}h$$
for $h=1$, $0.1$, and $0.01$. Compare the values with $f'(x_0)$ and explain why the difference quotient approaching a single number is consistent with the definition of the derivative, while a few computations do not replace a limit argument.

---

## Relevant theorem / definition

The derivative $f'(x_0)$ of a function $f$ at a point $x_0$ is defined as the limit of the difference quotient:
$$
f'(x_0) = \lim_{h \to 0} \frac{f(x_0+h) - f(x_0)}{h}
$$
The difference quotient $\frac{f(x_0+h) - f(x_0)}{h}$ represents the average rate of change of $f$ over the interval $[x_0, x_0+h]$ and the geometric slope of the secant line passing through $(x_0, f(x_0))$ and $(x_0+h, f(x_0+h))$.

---

## Solution

1. Choose a function and point $x_0$:
   Select $f(x) = x^2 - 3x + 1$ (from Problem 10) at $x_0 = 2$.
   Evaluate the function at $x_0 = 2$:
   $$
   f(2) = 2^2 - 3(2) + 1 = 4 - 6 + 1 = -1.
   $$

2. Compute $f'(x_0)$ exactly:
   Differentiating $f(x)$ using standard rules:
   $$
   f'(x) = 2x - 3.
   $$
   Evaluate at $x_0 = 2$:
   $$
   f'(2) = 2(2) - 3 = 1.
   $$

3. Form the general difference quotient expression:
   \begin{align}
   f(2+h) &= (2+h)^2 - 3(2+h) + 1 \\
   &= (4 + 4h + h^2) - (6 + 3h) + 1 \\
   &= -1 + h + h^2.
   \end{align}
   Subtract $f(2) = -1$:
   $$
   f(2+h) - f(2) = (-1 + h + h^2) - (-1) = h + h^2.
   $$
   For $h \neq 0$, the difference quotient is:
   $$
   \frac{f(2+h) - f(2)}{h} = \frac{h(1 + h)}{h} = 1 + h.
   $$

4. Calculate the difference quotient for $h = 1$, $0.1$, and $0.01$:
   - For $h = 1$:
     $$
     f(2+1) = f(3) = 3^2 - 3(3) + 1 = 1
     $$
     $$
     \frac{f(3) - f(2)}{1} = \frac{1 - (-1)}{1} = \frac{2}{1} = 2.0
     $$
   - For $h = 0.1$:
     $$
     f(2+0.1) = f(2.1) = (2.1)^2 - 3(2.1) + 1 = 4.41 - 6.30 + 1 = -0.89
     $$
     $$
     \frac{f(2.1) - f(2)}{0.1} = \frac{-0.89 - (-1)}{0.1} = \frac{0.11}{0.1} = 1.1
     $$
   - For $h = 0.01$:
     $$
     f(2+0.01) = f(2.01) = (2.01)^2 - 3(2.01) + 1 = 4.0401 - 6.03 + 1 = -0.9899
     $$
     $$
     \frac{f(2.01) - f(2)}{0.01} = \frac{-0.9899 - (-1)}{0.01} = \frac{0.0101}{0.01} = 1.01
     $$

5. Compare values and explain conceptual significance:
   - **Comparison:**
     $$
     h = 1 \implies \text{slope} = 2.0, \quad h = 0.1 \implies \text{slope} = 1.1, \quad h = 0.01 \implies \text{slope} = 1.01
     $$
     The discrepancy between the difference quotient and the exact derivative $f'(2) = 1$ decreases by an order of magnitude at each step: $|2.0 - 1| = 1$, $|1.1 - 1| = 0.1$, and $|1.01 - 1| = 0.01$.
   - **Consistency with the definition of the derivative:**
     As $h$ shrinks toward zero, the secant lines rotate around the fixed point of tangency $(2, -1)$, and their slopes approach the slope of the tangent line. Because the difference quotient values steadily converge toward $1$, the numerical behavior directly reflects the limit definition $\lim_{h \to 0} (1+h) = 1$.
   - **Why a few computations do not replace a limit argument:**
     Numerical sampling tests only a finite number of isolated step sizes. Discrete samples cannot determine whether the quotient converges to a limit from both sides (such as when approaching through negative $h$), nor can they rule out high-frequency oscillatory behavior (e.g., $h\sin(1/h)$) that might destabilize the quotient at smaller scales. A mathematical limit requires demonstrating that for *every* $\varepsilon > 0$, there exists a $\delta > 0$ such that all $0 < |h| < \delta$ lie within $\varepsilon$ of the target value.

---

## Result

$$
\text{Chosen function: } f(x) = x^2 - 3x + 1 \text{ at } x_0 = 2, \quad f'(2) = 1
$$

$$
h = 1: \quad \frac{f(3) - f(2)}{1} = 2.0
$$

$$
h = 0.1: \quad \frac{f(2.1) - f(2)}{0.1} = 1.1
$$

$$
h = 0.01: \quad \frac{f(2.01) - f(2)}{0.01} = 1.01
$$

$$
\text{Conclusion: The secant slope } 1+h \to 1 \text{ as } h \to 0. \text{ Sampling exhibits the trend, but only an analytical limit guarantees convergence.}
$$

---

## Verification

**Pass 1 — Algebraic check:** Compute the analytical limit of the simplified difference quotient:
$$
\lim_{h \to 0} \frac{f(2+h) - f(2)}{h} = \lim_{h \to 0} (1 + h) = 1 + 0 = 1
$$
This matches the exact derivative $f'(2) = 1$ identically.

**Pass 2 — Numerical check:** Evaluate with negative increments $h$:
- For $h = -0.1$: $f(1.9) = (1.9)^2 - 3(1.9) + 1 = 3.61 - 5.70 + 1 = -1.09$. Then $\frac{-1.09 - (-1)}{-0.1} = \frac{-0.09}{-0.1} = 0.9 = 1 - 0.1$.
- For $h = -0.01$: $f(1.99) = (1.99)^2 - 3(1.99) + 1 = 3.9601 - 5.97 + 1 = -1.0099$. Then $\frac{-1.0099 - (-1)}{-0.01} = \frac{-0.0099}{-0.01} = 0.99 = 1 - 0.01$.
The left-hand difference quotients converge to $1$ with identical error magnitude $|h|$, verifying symmetric two-sided convergence.

**Pass 3 — Consistency check:** Taylor's theorem states $f(x_0+h) = f(x_0) + f'(x_0)h + \frac{f''(x_0)}{2}h^2$ for any polynomial of degree 2. Thus $\frac{f(x_0+h)-f(x_0)}{h} - f'(x_0) = \frac{f''(x_0)}{2}h$. Since $f''(x) = 2$, $\frac{f''(2)}{2} = 1$, which proves the error is exactly equal to $h$ for every $h \neq 0$.

---

## Exam tip

Remember that the difference quotient gives the average rate of change over an interval, while the derivative is the instantaneous rate of change obtained exclusively in the limit $h \to 0$.

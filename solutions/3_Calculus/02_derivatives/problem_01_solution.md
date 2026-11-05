# Exercise 1

**Problem:** For
$$f(x)=3x^5-2x^3+7x-4$$
find $f'(x)$. Then compute $f'(0)$ and $f'(1)$, determine the signs of the obtained values, and explain what they say about the slope of the tangent line to the graph at these two points.

---

## Relevant theorem / definition

The power rule states that for any real exponent $n$, $\frac{d}{dx}(x^n) = n x^{n-1}$. Differentiation is linear:
$$
\frac{d}{dx}[a f(x) + b g(x)] = a f'(x) + b g'(x)
$$
The derivative $f'(x_0)$ equals the slope $m$ of the tangent line to the graph of $y = f(x)$ at $(x_0, f(x_0))$. If $f'(x_0) > 0$, the tangent line has positive slope and slants upward from left to right.

---

## Solution

1. Differentiate term-by-term using the power rule:
   \begin{align}
   f'(x) &= \frac{d}{dx}(3x^5) - \frac{d}{dx}(2x^3) + \frac{d}{dx}(7x) - \frac{d}{dx}(4) \\
   &= 3(5x^4) - 2(3x^2) + 7(1) - 0 \\
   &= 15x^4 - 6x^2 + 7.
   \end{align}

2. Compute $f'(0)$:
   $$
   f'(0) = 15(0)^4 - 6(0)^2 + 7 = 7.
   $$
   The value is positive ($f'(0) = 7 > 0$). This means the tangent line at $(0, -4)$ has positive slope $m = 7$, slanting upward from left to right at an angle of $\arctan(7) \approx 81.9^\circ$. The function is strictly increasing in an open neighborhood around $x = 0$.

3. Compute $f'(1)$:
   $$
   f'(1) = 15(1)^4 - 6(1)^2 + 7 = 15 - 6 + 7 = 16.
   $$
   The value is positive ($f'(1) = 16 > 0$). This means the tangent line at $(1, 4)$ has positive slope $m = 16$, slanting upward more steeply than at $x = 0$. The function is strictly increasing in an open neighborhood around $x = 1$.

---

## Result

$$
f'(x) = 15x^4 - 6x^2 + 7
$$

$$
f'(0) = 7 > 0 \quad (\text{tangent line has positive slope } m = 7\text{, slanting upward})
$$

$$
f'(1) = 16 > 0 \quad (\text{tangent line has positive slope } m = 16\text{, slanting upward})
$$

---

## Verification

**Pass 1 — Algebraic check:** Integrating $f'(x) = 15x^4 - 6x^2 + 7$ yields $\int (15x^4 - 6x^2 + 7)\,dx = 15\frac{x^5}{5} - 6\frac{x^3}{3} + 7x + C = 3x^5 - 2x^3 + 7x + C$, which recovers the original polynomial $f(x)$ with constant $C = -4$.

**Pass 2 — Numerical check:** Use the symmetric difference quotient at $x = 0$ with step size $h = 0.001$: $f(0.001) = 3(10^{-15}) - 2(10^{-9}) + 7(0.001) - 4 = -3.993000$, $f(-0.001) = -4.007000$. Then $\frac{f(0.001) - f(-0.001)}{2(0.001)} = \frac{0.014000}{0.002} = 7.000$, matching $f'(0) = 7$.

**Pass 3 — Consistency check:** Rewriting $f'(x) = 15(x^2 - \frac{1}{5})^2 + 7 - 15(\frac{1}{25}) = 15(x^2 - \frac{1}{5})^2 + \frac{32}{5}$. Since $(x^2 - \frac{1}{5})^2 \ge 0$, $f'(x) \ge 6.4 > 0$ for all $x \in \mathbb{R}$. Both evaluated values ($7$ and $16$) are strictly greater than $6.4$, consistent with the global positivity of the derivative.

---

## Exam tip

The derivative of a constant term is always zero; never accidentally leave constant terms like $-4$ in the derivative.

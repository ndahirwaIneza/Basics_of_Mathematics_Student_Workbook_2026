# Exercise 11

**Problem:** Using only
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h,$$
find the derivative of $f(x)=x^2$. Compare the result with the power rule and indicate where the limit is used in the calculation.

---

## Relevant theorem / definition

The derivative of a function $f$ at an arbitrary point $x$ is defined as the limit of the difference quotient as the increment $h$ approaches zero:
$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$
The power rule states that $\frac{d}{dx}(x^n) = n x^{n-1}$ for any real constant $n$.

---

## Solution

1. Set up the difference quotient:
   Given $f(x) = x^2$, evaluate the function at $x + h$:
   $$
   f(x+h) = (x + h)^2 = x^2 + 2xh + h^2.
   $$
   Form the difference $f(x+h) - f(x)$:
   $$
   f(x+h) - f(x) = (x^2 + 2xh + h^2) - x^2 = 2xh + h^2.
   $$

2. Divide by $h$ (for $h \neq 0$):
   Factor $h$ from the numerator to cancel the indeterminate $\frac{0}{0}$ structure:
   $$
   \frac{f(x+h) - f(x)}{h} = \frac{2xh + h^2}{h} = \frac{h(2x + h)}{h} = 2x + h.
   $$

3. Evaluate the limit as $h \to 0$:
   \begin{align}
   f'(x) &= \lim_{h \to 0} (2x + h) \\
   &= 2x + 0 \\
   &= 2x.
   \end{align}

4. Indicate where the limit is used:
   The limit is applied in the final transition from the simplified difference quotient $2x + h$ to $2x$. Directly substituting $h = 0$ at the initial step is prohibited because it produces the undefined indeterminate form $\frac{0}{0}$. After dividing out the non-zero increment $h$, the remaining expression $2x + h$ is continuous in $h$. The limit operation $\lim_{h \to 0}$ sets $h = 0$, eliminating the second-order increment $h$ and yielding the exact instantaneous rate of change $2x$.

5. Compare with the power rule:
   Applying the power rule to $f(x) = x^2$ with $n = 2$:
   $$
   \frac{d}{dx}(x^2) = 2x^{2-1} = 2x^1 = 2x.
   $$
   The result obtained from the definition is identical to that given by the power rule.

---

## Result

$$
f'(x) = \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h} = \lim_{h \to 0} (2x + h) = 2x
$$

$$
\text{Power rule comparison: } \frac{d}{dx}(x^2) = 2x^{2-1} = 2x \quad (\text{results are identical})
$$

---

## Verification

**Pass 1 — Algebraic check:** Use the alternative definition of the derivative at a point $x_0$:
$$
f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = \lim_{x \to x_0} \frac{x^2 - x_0^2}{x - x_0}
$$
Factor the difference of squares:
$$
\lim_{x \to x_0} \frac{(x - x_0)(x + x_0)}{x - x_0} = \lim_{x \to x_0} (x + x_0) = x_0 + x_0 = 2x_0
$$
Replacing $x_0$ with $x$ yields $2x$, confirming the algebraic consistency.

**Pass 2 — Numerical check:** Let $x = 3$, so the formula gives $f'(3) = 2(3) = 6$.
Compute the difference quotient for successively smaller values of $h$:
- For $h = 0.1$: $\frac{(3.1)^2 - 3^2}{0.1} = \frac{9.61 - 9}{0.1} = \frac{0.61}{0.1} = 6.1$
- For $h = 0.01$: $\frac{(3.01)^2 - 3^2}{0.01} = \frac{9.0601 - 9}{0.01} = \frac{0.0601}{0.01} = 6.01$
- For $h = 0.001$: $\frac{(3.001)^2 - 3^2}{0.001} = \frac{9.006001 - 9}{0.001} = \frac{0.006001}{0.001} = 6.001$
As $h \to 0$, $6 + h \to 6 = f'(3)$.

**Pass 3 — Consistency check:** Since $f(x) = x^2$ is an even function, its derivative must be an odd function. Indeed, $f'(-x) = 2(-x) = -2x = -f'(x)$. Furthermore, at the vertex $x = 0$, $f'(0) = 0$, and the slope is negative for $x < 0$ and positive for $x > 0$, matching the shape of a parabola opening upward.

---

## Exam tip

Never substitute $h = 0$ until after factoring and canceling $h$ from the denominator, otherwise you will obtain the meaningless indeterminate form $0/0$.

# Exercise 8

**Problem:** Compute
$$\lim_{x\to4}\frac{\sqrt{x}-2}{x-4}$$
by rationalizing the numerator. Compare the idea with Exercise 3 involving a sequence.

---

## Relevant theorem / definition

For an indeterminate form $\frac{0}{0}$ involving square roots, the algebraic conjugate identity:

$$
(\sqrt{A} - B)(\sqrt{A} + B) = A - B^2
$$

eliminates the radical from the numerator and exposes the vanishing factor responsible for division by zero.

---

## Solution

1. Test for direct substitution:
   At $x = 4$:

$$
   \sqrt{4} - 2 = 2 - 2 = 0, \qquad 4 - 4 = 0
$$

   This yields the indeterminate form $\frac{0}{0}$.

2. Rationalize the numerator by multiplying numerator and denominator by the conjugate $\sqrt{x} + 2$:

$$
   \frac{\sqrt{x}-2}{x-4} = \frac{(\sqrt{x}-2)(\sqrt{x}+2)}{(x-4)(\sqrt{x}+2)}
$$

3. Expand the numerator using $(a-b)(a+b) = a^2 - b^2$:

$$
   (\sqrt{x}-2)(\sqrt{x}+2) = (\sqrt{x})^2 - 2^2 = x - 4
$$

   Thus:

$$
   \frac{\sqrt{x}-2}{x-4} = \frac{x-4}{(x-4)(\sqrt{x}+2)}
$$

4. Cancel the non-zero common factor $(x-4)$ for $x \neq 4$:

$$
   \frac{x-4}{(x-4)(\sqrt{x}+2)} = \frac{1}{\sqrt{x}+2}
$$

5. Compute the limit by direct substitution:

$$
   \begin{align}
   \lim_{x\to4}\frac{\sqrt{x}-2}{x-4} &= \lim_{x\to4}\frac{1}{\sqrt{x}+2} \\
   &= \frac{1}{\sqrt{4}+2} \\
   &= \frac{1}{2+2} = \frac{1}{4}
   \end{align}
$$

6. Comparison with Exercise 3:
   - In Exercise 3 ($\lim_{n\to\infty}(\sqrt{n^2+5n}-n)$), the indeterminate form was $\infty - \infty$ at infinity. Conjugation transformed the difference into a sum in the denominator, allowing division by the dominant term $n$.
   - In Exercise 8, the indeterminate form is $\frac{0}{0}$ at a finite point $x = 4$. Conjugation creates the polynomial factor $(x-4)$ in the numerator, directly canceling the zero-denominator term.
   - Core unifying principle: Both problems use $(A-B)(A+B) = A^2-B^2$ to remove a square root that obstructs algebraic simplification.

---

## Result

$$
\lim_{x\to4}\frac{\sqrt{x}-2}{x-4} = \frac{1}{4}
$$

---

## Verification

**Pass 1 — Algebraic check:**
- Method A (Derivative definition): The limit represents the derivative of $g(x) = \sqrt{x}$ at $x = 4$:

$$
  g'(4) = \lim_{x\to4}\frac{\sqrt{x} - \sqrt{4}}{x-4} = \left.\frac{1}{2\sqrt{x}}\right|_{x=4} = \frac{1}{2(2)} = \frac{1}{4}
$$

- Method B (Denominator factoring): Factor $x - 4 = (\sqrt{x}-2)(\sqrt{x}+2)$ directly:

$$
  \frac{\sqrt{x}-2}{(\sqrt{x}-2)(\sqrt{x}+2)} = \frac{1}{\sqrt{x}+2} \xrightarrow{x\to4} \frac{1}{4}
$$

**Pass 2 — Numerical check:**
Evaluate at $x = 4.01$:

$$
\frac{\sqrt{4.01}-2}{4.01-4} = \frac{2.00249844 - 2}{0.01} = \frac{0.00249844}{0.01} = 0.249844
$$

Evaluate at $x = 3.99$:

$$
\frac{\sqrt{3.99}-2}{3.99-4} = \frac{1.99749844 - 2}{-0.01} = \frac{-0.00250156}{-0.01} = 0.250156
$$

Both values are within $0.0002$ of $\frac{1}{4} = 0.25$.

**Pass 3 — Consistency check:** For all $x > 0$ with $x \neq 4$, $\sqrt{x} + 2 > 0$, so $\frac{1}{\sqrt{x}+2}$ is strictly positive and bounded between 0 and $\frac{1}{2}$. The limit $\frac{1}{4}$ falls strictly inside this range.

---

## Exam tip

Multiplying by the conjugate is the standard method to remove $\frac{0}{0}$ whenever square roots create a zero difference.

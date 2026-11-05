# Exercise 7

**Problem:** Compute
$$\lim_{x\to3}\frac{x^2-4x+3}{x-3}.$$
Explain why the value of the function at $x=3$ is not needed to compute the limit.

---

## Relevant theorem / definition

The limit of a function $f(x)$ as $x \to c$ depends solely on the values of $f(x)$ in a punctured (deleted) neighborhood of $c$:

$$
0 < |x - c| < \delta
$$

The value $f(c)$ at the point itself does not need to exist, nor does it affect the value of the limit. If $f(x) = g(x)$ for all $x \neq c$, then:

$$
\lim_{x\to c} f(x) = \lim_{x\to c} g(x)
$$

---

## Solution

1. Test for direct substitution:
   At $x = 3$:

$$
   x^2 - 4x + 3 = 3^2 - 4(3) + 3 = 9 - 12 + 3 = 0
$$

$$
   x - 3 = 3 - 3 = 0
$$

   This yields the indeterminate form $\frac{0}{0}$. The function $f(x) = \frac{x^2-4x+3}{x-3}$ is undefined at $x = 3$.

2. Factor the numerator:
   Find the roots of $x^2 - 4x + 3 = 0$:

$$
   x^2 - 4x + 3 = (x - 3)(x - 1)
$$

3. Cancel the common factor for $x \neq 3$:

$$
   \frac{x^2-4x+3}{x-3} = \frac{(x-3)(x-1)}{x-3} = x - 1 \quad (\text{for } x \neq 3)
$$

4. Evaluate the limit:

$$
   \begin{align}
   \lim_{x\to3}\frac{x^2-4x+3}{x-3} &= \lim_{x\to3}(x - 1) \\
   &= 3 - 1 = 2
   \end{align}
$$

5. Why the value at $x=3$ is not needed:
   By the fundamental definition of a limit, we analyze the behavior of $f(x)$ as $x$ gets arbitrarily close to 3 without ever equaling 3 ($x \neq 3$). In the punctured neighborhood around 3, the expression $(x-3)$ is non-zero, allowing valid algebraic division to obtain $f(x) = x - 1$. Whether $f(3)$ is undefined, equal to 2, or assigned an arbitrary number such as 100 has no bearing on $\lim_{x\to3} f(x)$.

---

## Result

$$
\lim_{x\to3}\frac{x^2-4x+3}{x-3} = 2
$$

---

## Verification

**Pass 1 — Algebraic check:** Apply l'Hôpital's rule to the $\frac{0}{0}$ form:

$$
\lim_{x\to3}\frac{\frac{d}{dx}(x^2-4x+3)}{\frac{d}{dx}(x-3)} = \lim_{x\to3}\frac{2x-4}{1} = 2(3) - 4 = 2
$$

**Pass 2 — Numerical check:**
Compute values approaching $x = 3$ from both sides:
- From the left:

$$
  f(2.9) = \frac{2.9^2 - 4(2.9) + 3}{2.9 - 3} = \frac{8.41 - 11.6 + 3}{-0.1} = \frac{-0.19}{-0.1} = 1.9
$$

$$
  f(2.999) = \frac{(2.999-3)(2.999-1)}{2.999-3} = 2.999 - 1 = 1.999
$$

- From the right:

$$
  f(3.1) = \frac{3.1^2 - 4(3.1) + 3}{3.1 - 3} = \frac{9.61 - 12.4 + 3}{0.1} = \frac{0.21}{0.1} = 2.1
$$

$$
  f(3.001) = 3.001 - 1 = 2.001
$$

Both sides converge symmetrically to 2.

**Pass 3 — Consistency check:** The graph of $f(x)$ is the straight line $y = x - 1$ with a single point removed at $(3, 2)$ (a removable discontinuity). As $x \to 3$, the coordinates on the line clearly tend to $y = 2$.

---

## Exam tip

When direct substitution into a rational function produces $\frac{0}{0}$, $(x-c)$ is guaranteed to be a common factor; factor it out and cancel before evaluating.

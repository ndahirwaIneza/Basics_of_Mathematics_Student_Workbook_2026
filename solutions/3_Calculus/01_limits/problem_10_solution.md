# Exercise 10

**Problem:** Find $a$ so that
$$f(x)=\begin{cases}ax+1,&x<2,\\x^2-1,&x\ge2\end{cases}$$
is continuous at $x=2$. Explicitly compare the left-hand limit, right-hand limit, and function value.

---

## Relevant theorem / definition

A function $f(x)$ is continuous at a point $x = c$ in its domain if and only if the three following conditions are satisfied:
1. The function value $f(c)$ is defined.
2. The two-sided limit $\lim_{x\to c} f(x)$ exists, which requires:

$$
   \lim_{x\to c^-} f(x) = \lim_{x\to c^+} f(x)
$$

3. The limit equals the function value:

$$
   \lim_{x\to c^-} f(x) = \lim_{x\to c^+} f(x) = f(c)
$$

---

## Solution

1. Compute the left-hand limit as $x \to 2^-$:
   For $x < 2$, the function is defined by $f(x) = ax + 1$.
   Because polynomials are continuous everywhere:

$$
   \begin{align}
   \lim_{x\to2^-} f(x) &= \lim_{x\to2^-} (ax + 1) \\
   &= a(2) + 1 \\
   &= 2a + 1
   \end{align}
$$

2. Compute the right-hand limit as $x \to 2^+$:
   For $x > 2$, the function is defined by $f(x) = x^2 - 1$.
   Evaluating the limit:

$$
   \begin{align}
   \lim_{x\to2^+} f(x) &= \lim_{x\to2^+} (x^2 - 1) \\
   &= 2^2 - 1 \\
   &= 4 - 1 = 3
   \end{align}
$$

3. Evaluate the function value at $x = 2$:
   The definition specifies $f(x) = x^2 - 1$ for $x \ge 2$.
   Substituting $x = 2$:

$$
   f(2) = 2^2 - 1 = 4 - 1 = 3
$$

4. Explicit comparison of the three quantities:
   - Left-hand limit: $\lim_{x\to2^-} f(x) = 2a + 1$
   - Right-hand limit: $\lim_{x\to2^+} f(x) = 3$
   - Function value: $f(2) = 3$

   Notice that the right-hand limit and the function value already agree identically: $\lim_{x\to2^+} f(x) = f(2) = 3$.

5. Solve for $a$:
   For continuity at $x = 2$, the left-hand limit must equal the common value of the right-hand limit and function value:

$$
   2a + 1 = 3
$$

$$
   2a = 2 \implies a = 1
$$

   When $a = 1$:

$$
   \lim_{x\to2^-} f(x) = 2(1) + 1 = 3 = \lim_{x\to2^+} f(x) = f(2)
$$

   All three quantities are equal to 3, ensuring $f(x)$ is continuous at $x = 2$.

---

## Result

$$
a = 1
$$

---

## Verification

**Pass 1 — Algebraic check:** With $a = 1$, the function is:

$$
f(x) = \begin{cases} x + 1, & x < 2 \\ x^2 - 1, & x \ge 2 \end{cases}
$$

The value of the left branch at the boundary is $2 + 1 = 3$, and the right branch at the boundary is $2^2 - 1 = 3$. The jump size is $\Delta = |(x^2 - 1) - (ax + 1)|_{x=2} = |3 - (2a + 1)| = |2 - 2a|$. Setting $\Delta = 0$ yields $a = 1$.

**Pass 2 — Numerical check:**
With $a = 1$, test points close to 2:
- Left branch: $f(1.999) = 1.999 + 1 = 2.999$
- Right branch: $f(2.001) = (2.001)^2 - 1 = 4.004001 - 1 = 3.004001$
- At the point: $f(2) = 3$
The difference $|f(2.001) - f(1.999)| = |3.004001 - 2.999| = 0.005001 \to 0$.

**Pass 3 — Consistency check:** For any $a \neq 1$, $f$ has a jump discontinuity at $x = 2$ of magnitude $|2 - 2a| > 0$. Only $a = 1$ removes the jump and glues the straight line $y = x + 1$ smoothly into the parabola $y = x^2 - 1$ at the shared coordinate $(2, 3)$.

---

## Exam tip

To find a parameter for continuity at a piecewise boundary, equate the left-hand limit and right-hand limit directly, then verify that this value matches the function value.

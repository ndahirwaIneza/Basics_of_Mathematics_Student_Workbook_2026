# Exercise 12

**Problem:** Compute
$$\lim_{x\to0}(1+3x)^{1/x}.$$
Connect the result with the limit from Exercise 5 and show the appropriate transformation.

---

## Relevant theorem / definition

The continuous analog of the fundamental sequence limit for Euler's constant (from Exercise 5) states that for any real variable $u \to 0$:

$$
\lim_{u\to0}(1 + u)^{1/u} = e
$$

Furthermore, if $\lim_{x\to c} g(x) = L$ and $f(t) = t^k$ is continuous at $t = L$, then:

$$
\lim_{x\to c} [g(x)]^k = \left[\lim_{x\to c} g(x)\right]^k
$$

---

## Solution

1. Test for direct substitution:
   As $x \to 0$, the base is $1 + 3(0) = 1$, and the exponent is $\frac{1}{x} \to \pm\infty$. This gives the indeterminate form $1^\infty$.

2. Connect with Exercise 5:
   In Exercise 5, the fundamental sequence limit was established as:

$$
   \lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^n = e
$$

   Substituting $u = \frac{1}{n}$, as $n \to \infty$, $u \to 0^+$. Extending to continuous real values approaching zero from both sides gives the standard function limit:

$$
   \lim_{u\to0}(1 + u)^{1/u} = e
$$

3. Transform the expression:
   Let $u = 3x$. As $x \to 0$, $u \to 0$, and $x = \frac{u}{3}$.
   The exponent transforms as:

$$
   \frac{1}{x} = \frac{3}{u} = \frac{1}{u} \cdot 3
$$

   Rewrite the base and exponent:

$$
   (1 + 3x)^{1/x} = \left((1 + 3x)^{\frac{1}{3x}}\right)^3 = \left((1 + u)^{\frac{1}{u}}\right)^3
$$

4. Evaluate the limit using the continuity of the power function $f(t) = t^3$:

$$
   \begin{align}
   \lim_{x\to0}(1+3x)^{1/x} &= \lim_{u\to0}\left((1+u)^{1/u}\right)^3 \\
   &= \left(\lim_{u\to0}(1+u)^{1/u}\right)^3 \\
   &= e^3
   \end{align}
$$

---

## Result

$$
\lim_{x\to0}(1+3x)^{1/x} = e^3
$$

---

## Verification

**Pass 1 — Algebraic check:**
Take the natural logarithm of $y = (1 + 3x)^{1/x}$:

$$
\ln y = \frac{\ln(1 + 3x)}{x}
$$

As $x \to 0$, this yields $\frac{0}{0}$. Applying l'Hôpital's rule:

$$
\lim_{x\to0}\frac{\ln(1 + 3x)}{x} \stackrel{\text{H}}{=} \lim_{x\to0}\frac{\frac{3}{1 + 3x}}{1} = \frac{3}{1 + 0} = 3
$$

Since $y = \exp(\ln y)$ and the exponential function is continuous:

$$
\lim_{x\to0} y = e^3
$$

**Pass 2 — Numerical check:**
The theoretical value is $e^3 \approx 20.0855369$.
Evaluate $(1 + 3x)^{1/x}$ for small values of $x$:
- At $x = 0.01$:

$$
  (1 + 0.03)^{100} = (1.03)^{100} \approx 19.21863
$$

- At $x = 0.001$:

$$
  (1 + 0.003)^{1000} = (1.003)^{1000} \approx 19.99553
$$

- At $x = 0.0001$:

$$
  (1 + 0.0003)^{10000} = (1.0003)^{10000} \approx 20.07648
$$

- At $x = -0.0001$:

$$
  (1 - 0.0003)^{-10000} = (0.9997)^{-10000} \approx 20.09459
$$

Both sides converge toward $20.08554 \approx e^3$.

**Pass 3 — Consistency check:** General identity for forms of this type states that $\lim_{x\to0}(1 + kx)^{1/x} = e^k$. Setting $k = 3$ gives $e^3$, which is consistent with $k = 1$ yielding $e^1 = e$ from Exercise 5.

---

## Exam tip

For any limit of the form $\lim_{x\to0}(1+kx)^{1/x}$, rewrite the exponent as $\frac{1}{kx} \cdot k$ so that the base-exponent pair immediately forms the standard $e^k$ limit.

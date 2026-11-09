# Exercise 15

**Problem:** Choose one sequence and one function from this set. For the sequence, compute several values for increasingly large $n$. For the function, prepare a table of values with arguments approaching the limit point from the left and right. Sketch the behavior of both objects.

Compare the observation with the analytical result and explain why a finite number of calculations or a sketch does not constitute a proof that the limit exists.

---

## Relevant theorem / definition

1. Formal definition of a sequence limit ($\varepsilon$-$N$ criterion):

$$
   \lim_{n\to\infty} a_n = L \iff \forall \varepsilon > 0 \quad \exists N \in \mathbb{N} \quad \forall n \ge N: \quad |a_n - L| < \varepsilon
$$

2. Formal definition of a function limit ($\varepsilon$-$\delta$ criterion):

$$
   \lim_{x\to c} f(x) = L \iff \forall \varepsilon > 0 \quad \exists \delta > 0 \quad \forall x \in \mathbb{R}: \quad 0 < |x - c| < \delta \implies |f(x) - L| < \varepsilon
$$

---

## Solution

1. Selection of sequence and function:
   - Sequence (from Exercise 3):

$$
     a_n = \sqrt{n^2+5n} - n, \qquad \lim_{n\to\infty} a_n = \frac{5}{2} = 2.5
$$

   - Function (from Exercise 7):

$$
     f(x) = \frac{x^2-4x+3}{x-3}, \qquad \lim_{x\to3} f(x) = 2
$$

2. Sequence calculations for increasingly large $n$:
   - For $n = 1$:

$$
     a_1 = \sqrt{1^2 + 5(1)} - 1 = \sqrt{6} - 1 \approx 2.449490 - 1 = 1.449490
$$

   - For $n = 5$:

$$
     a_5 = \sqrt{5^2 + 5(5)} - 5 = \sqrt{50} - 5 \approx 7.071068 - 5 = 2.071068
$$

   - For $n = 10$:

$$
     a_{10} = \sqrt{10^2 + 5(10)} - 10 = \sqrt{150} - 10 \approx 12.247449 - 10 = 2.247449
$$

   - For $n = 100$:

$$
     a_{100} = \sqrt{100^2 + 5(100)} - 100 = \sqrt{10500} - 100 \approx 102.469508 - 100 = 2.469508
$$

   - For $n = 1000$:

$$
     a_{1000} = \sqrt{1000^2 + 5(1000)} - 1000 = \sqrt{1005000} - 1000 \approx 1002.496883 - 1000 = 2.496883
$$

   - For $n = 10000$:

$$
     a_{10000} = \sqrt{10^8 + 5(10000)} - 10000 \approx 10002.499688 - 10000 = 2.499688
$$

3. Function table of values approaching $x = 3$ from left and right:
   The function is $f(x) = \frac{x^2-4x+3}{x-3} = x - 1$ for $x \neq 3$.

   | Direction | $x$ | $f(x) = \frac{x^2-4x+3}{x-3}$ | $f(x)$ exact |
   |:---|:---|:---|:---|
   | Approaching from left ($x \to 3^-$) | $2.9$ | $\frac{8.41 - 11.60 + 3}{-0.1} = \frac{-0.19}{-0.1}$ | $1.9000$ |
   | | $2.99$ | $\frac{8.9401 - 11.96 + 3}{-0.01} = \frac{-0.0199}{-0.01}$ | $1.9900$ |
   | | $2.999$ | $\frac{8.994001 - 11.996 + 3}{-0.001}$ | $1.9990$ |
   | At the point | $3.0$ | $\frac{0}{0}$ | Undefined |
   | Approaching from right ($x \to 3^+$) | $3.001$ | $\frac{9.006001 - 12.004 + 3}{0.001}$ | $2.0010$ |
   | | $3.01$ | $\frac{9.0601 - 12.04 + 3}{0.01} = \frac{0.0201}{0.01}$ | $2.0100$ |
   | | $3.1$ | $\frac{9.61 - 12.40 + 3}{0.1} = \frac{0.21}{0.1}$ | $2.1000$ |

4. Geometric sketches of both objects:
   - Sequence $a_n$:
     The points $(n, a_n)$ lie in the discrete upper-right half-plane. Starting at $(1, 1.45)$, the points increase monotonically with concave curvature, asymptotic from below to the horizontal line $y = 2.5$.
     ```
       y
      3.0 |
      2.5 | - - - - - - - - - - - - - - - - - - - - - - -  y = 2.5 (asymptote)
          |                     *       *       *       *
      2.0 |             *
          |     *
      1.5 | *
      0.0 +---------------------------------------------- n
            1   5       10      50      100     500     1000
     ```
   - Function $f(x)$:
     The graph is the continuous straight line $y = x - 1$ of slope 1 with a single point deleted (a hole) at $(3, 2)$.
     ```
       y
      4.0 |                  /
      3.0 |                 /
      2.0 |            o   /      (hole at (3, 2))
      1.0 |           /
      0.0 +----------/----------------- x
         -1.0       1.0  2.0  3.0  4.0
     ```

5. Comparison of observation with analytical result:
   - Numerical values for $a_n$ climb steadily ($1.449 \to 2.071 \to 2.247 \to 2.470 \to 2.497 \to 2.4997$), clearly indicating that the terms approach $2.5$. The analytical conjugate derivation rigorously proved this limit is exactly $\frac{5}{2}$.
   - The two-sided table for $f(x)$ shows symmetric pinching ($1.999 \to \text{hole} \leftarrow 2.001$), pointing directly to 2. The analytical factoring $\frac{(x-3)(x-1)}{x-3} = x - 1$ proved the limit is exactly 2.

6. Why finite calculations or a sketch do not constitute a proof:
   - Unsampled domain points: A finite set of evaluations tests only a negligible fraction of an infinite domain. A function can appear to approach a limit across several tested points while violently oscillating on smaller scales. For example, $g(x) = \sin(\pi/x)$ evaluated at $x = \frac{1}{k}$ gives $g(1/k) = 0$ for all integers $k$, suggesting a limit of 0, whereas $g(x)$ actually oscillates infinitely between $-1$ and $+1$ as $x \to 0$ and has no limit.
   - Long-range departures: A sequence might appear stable over the first million terms, yet diverge for $n > 10^{12}$ (e.g. $s_n = 2.5 + \frac{\sin(n / 10^{12})}{10}$).
   - Machine precision and roundoff: Direct numerical calculation on floating-point hardware suffers from catastrophic cancellation errors for large $n$. For instance, evaluating $\sqrt{n^2+5n}-n$ directly at $n = 10^{16}$ in standard IEEE-754 binary64 arithmetic produces `2.0` instead of $\approx 2.5$ (and collapses to `0.0` at slightly larger $n$ such as $10^{17}$) due to rounding in the 53-bit significand when adding $5n$ to $n^2$.
   - Nature of universal quantifiers: The mathematical definition of a limit involves universal quantification ($\forall \varepsilon > 0$). Proving that $|a_n - L| < \varepsilon$ holds for every positive $\varepsilon$ requires a deductive algebraic or analytic argument that covers all infinite possibilities simultaneously.

---

## Result

$$
\lim_{n\to\infty}\left(\sqrt{n^2+5n}-n\right) = \frac{5}{2}, \qquad \lim_{x\to3}\frac{x^2-4x+3}{x-3} = 2
$$

---

## Verification

**Pass 1 — Algebraic check:**
Prove convergence via formal $\varepsilon$-$N$ and $\varepsilon$-$\delta$ bounds:
- For $a_n$: Let $s = \sqrt{n^2+5n} > n$. Since $a_n = s - n = \frac{5n}{s + n} < \frac{5n}{2n} = \frac{5}{2}$, the error is positive and simplifies by rationalizing $s - n$ a second time:

$$
  \left|a_n - \frac{5}{2}\right| = \frac{5}{2} - a_n = \frac{5}{2} - \frac{5n}{s+n} = \frac{5(s - n)}{2(s+n)} = \frac{5(s^2 - n^2)}{2(s+n)^2} = \frac{25n}{2(s+n)^2} < \frac{25n}{2(2n)^2} = \frac{25}{8n}
$$

  (using $s + n > 2n$ in the denominator). For any $\varepsilon > 0$, choosing $N = \lceil\frac{25}{8\varepsilon}\rceil$ ensures $|a_n - 2.5| < \varepsilon$ for all $n \ge N$.
- For $f(x)$:

$$
  |f(x) - 2| = |(x - 1) - 2| = |x - 3|
$$

  For any $\varepsilon > 0$, choosing $\delta = \varepsilon$ guarantees $|f(x) - 2| < \varepsilon$ whenever $0 < |x - 3| < \delta$.

**Pass 2 — Numerical check:**
For $\varepsilon = 0.01$:
- For $a_n$, theoretical $N = \lceil 25 / 0.08 \rceil = 313$. At $n = 400$: $a_{400} = \sqrt{160000 + 2000} - 400 \approx 402.4922 - 400 = 2.4922$, giving $|2.4922 - 2.5| = 0.0078 < 0.01$.
- For $f(x)$, $\delta = 0.01$. For $x = 3.008$: $|x - 3| = 0.008 < 0.01$, and $|f(3.008) - 2| = |2.008 - 2| = 0.008 < 0.01$.

**Pass 3 — Consistency check:** Counterexample test confirms the epistemological distinction: $h(x) = (x-1) + 10^{-6}\sin(10^9(x-3))$ yields values that round to $1.900, 1.990, 2.010, 2.100$ in lower-precision tables, masquerading as $x-1$, but possesses wild rapid fluctuations that only symbolic analysis can diagnose.

---

## Exam tip

Use tables of values to build intuition and formulate hypotheses, but always rely on algebraic factoring, conjugates, or $\varepsilon$-$\delta$ bounds to provide a rigorous proof.

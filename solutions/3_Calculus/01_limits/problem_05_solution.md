# Exercise 5

**Problem:** Compute
$$\lim_{n\to\infty}\left(1+\frac1n\right)^n.$$
Calculate several values for increasing $n$ and compare the observed behavior with the value of the limit. Explain why a few values do not constitute a proof.

---

## Relevant theorem / definition

The sequence $a_n = \left(1 + \frac{1}{n}\right)^n$ is strictly increasing and bounded above by 3 for all $n \in \mathbb{N}$. By the Monotone Convergence Theorem, it possesses a finite limit, which defines Euler's number $e$:

$$
e = \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n \approx 2.718281828\dots
$$

---

## Solution

1. Limit evaluation:
   The sequence $a_n = \left(1+\frac{1}{n}\right)^n$ exhibits the indeterminate form $1^\infty$, as the base $1 + \frac{1}{n} \to 1$ while the exponent $n \to \infty$. By the definition of the base of the natural logarithm:

$$
   \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n = e
$$

2. Calculate values for increasing $n$:
   - For $n = 1$:

$$
     a_1 = \left(1 + \frac{1}{1}\right)^1 = 2^1 = 2
$$

   - For $n = 2$:

$$
     a_2 = \left(1 + \frac{1}{2}\right)^2 = (1.5)^2 = 2.25
$$

   - For $n = 5$:

$$
     a_5 = \left(1 + \frac{1}{5}\right)^5 = (1.2)^5 = 2.48832
$$

   - For $n = 10$:

$$
     a_{10} = \left(1 + \frac{1}{10}\right)^{10} = (1.1)^{10} \approx 2.593742
$$

   - For $n = 50$:

$$
     a_{50} = \left(1 + \frac{1}{50}\right)^{50} = (1.02)^{50} \approx 2.691588
$$

   - For $n = 100$:

$$
     a_{100} = \left(1 + \frac{1}{100}\right)^{100} = (1.01)^{100} \approx 2.704814
$$

   - For $n = 1000$:

$$
     a_{1000} = \left(1 + \frac{1}{1000}\right)^{1000} = (1.001)^{1000} \approx 2.716924
$$

3. Comparison of observed behavior with the limit:
   The calculated values show that $a_n$ increases monotonically:

$$
   2.000000 < 2.250000 < 2.488320 < 2.593742 < 2.691588 < 2.704814 < 2.716924 < \dots < e
$$

   The increments between successive terms become progressively smaller, and the sequence approaches $e \approx 2.718282$ from below.

4. Why a few values do not constitute a proof:
   - Finite scope: Computing values at $n = 1, 2, \dots, 1000$ tests only an infinitesimal fraction of the infinite set $\mathbb{N}$. It cannot exclude the possibility that for some astronomically large $n$ the sequence turns downward, oscillates, or diverges to infinity.
   - Illusory patterns: Numerical approximations can falsely mimic convergence to a rational number or mask subtle oscillations. A mathematical limit requires satisfying the universal condition:

$$
     \forall \varepsilon > 0 \quad \exists N \in \mathbb{N} \quad \forall n \ge N: \quad \left|a_n - e\right| < \varepsilon
$$

     which demands an analytic argument holding for all arbitrarily large $n$, not empirical sampling.

---

## Result

$$
\lim_{n\to\infty}\left(1+\frac1n\right)^n = e \approx 2.718281828
$$

---

## Verification

**Pass 1 — Algebraic check:** Expand via the Binomial Theorem:

$$
\begin{align}
\left(1 + \frac{1}{n}\right)^n &= \sum_{k=0}^n \binom{n}{k} \frac{1}{n^k} \\
&= 1 + 1 + \frac{1}{2!}\left(1 - \frac{1}{n}\right) + \frac{1}{3!}\left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right) + \dots + \frac{1}{n!}\prod_{j=1}^{n-1}\left(1 - \frac{j}{n}\right)
\end{align}
$$

As $n \to \infty$, each product $\prod_{j=1}^{k-1}(1 - j/n) \to 1$, yielding the convergent series:

$$
\sum_{k=0}^\infty \frac{1}{k!} = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \dots = e
$$

**Pass 2 — Numerical check:** The asymptotic error of $a_n$ is known to be $\frac{e}{2n}$:

$$
e - a_{1000} \approx 2.718282 - 2.716924 = 0.001358
$$

Comparing with the theoretical first-order correction:

$$
\frac{e}{2000} \approx \frac{2.718282}{2000} = 0.001359
$$

The empirical error matches the asymptotic expansion to 6 decimal places.

**Pass 3 — Consistency check:** The sequence is strictly bounded by $2 \le a_n < e < 3$ for all $n \ge 1$. The computed numerical values all strictly lie inside this interval and preserve the monotonic ordering $a_1 < a_2 < a_5 < a_{10} < a_{50} < a_{100} < a_{1000}$.

---

## Exam tip

The indeterminate form $1^\infty$ does not equal 1; it represents a competition between the base approaching 1 and the exponent approaching infinity, yielding exponential constants like $e$.

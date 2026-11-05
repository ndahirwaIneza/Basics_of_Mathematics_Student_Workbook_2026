# Exercise 1

**Problem:** Compute
$$\lim_{n\to\infty}\frac{4n^2-3n+1}{2n^2+5n-7}.$$
Explain why the highest-degree terms determine the result.

---

## Relevant theorem / definition

For a rational sequence $\frac{P(n)}{Q(n)}$ where $P(n) = a_p n^p + \dots + a_0$ and $Q(n) = b_q n^q + \dots + b_0$ with $b_q \neq 0$, the limit as $n \to \infty$ is determined by the dominant powers:

$$
\lim_{n\to\infty} \frac{P(n)}{Q(n)} = \lim_{n\to\infty} \frac{a_p n^p}{b_q n^q}
$$

When $p = q$, the limit equals the ratio of leading coefficients $\frac{a_p}{b_q}$.

---

## Solution

1. Identify the indeterminate form:
   As $n \to \infty$, the numerator $4n^2 - 3n + 1 \to \infty$ and the denominator $2n^2 + 5n - 7 \to \infty$, giving the indeterminate form $\frac{\infty}{\infty}$.

2. Divide numerator and denominator by the highest power of $n$ present in the denominator, which is $n^2$:

$$
   \frac{4n^2-3n+1}{2n^2+5n-7} = \frac{\frac{4n^2}{n^2} - \frac{3n}{n^2} + \frac{1}{n^2}}{\frac{2n^2}{n^2} + \frac{5n}{n^2} - \frac{7}{n^2}} = \frac{4 - \frac{3}{n} + \frac{1}{n^2}}{2 + \frac{5}{n} - \frac{7}{n^2}}
$$

3. Evaluate the limit using the arithmetic of limits and the standard limit $\lim_{n\to\infty}\frac{1}{n^k} = 0$ for $k > 0$:

$$
   \begin{align}
   \lim_{n\to\infty}\frac{4n^2-3n+1}{2n^2+5n-7} &= \lim_{n\to\infty}\frac{4 - \frac{3}{n} + \frac{1}{n^2}}{2 + \frac{5}{n} - \frac{7}{n^2}} \\
   &= \frac{\lim_{n\to\infty} 4 - 3\lim_{n\to\infty}\frac{1}{n} + \lim_{n\to\infty}\frac{1}{n^2}}{\lim_{n\to\infty} 2 + 5\lim_{n\to\infty}\frac{1}{n} - 7\lim_{n\to\infty}\frac{1}{n^2}} \\
   &= \frac{4 - 0 + 0}{2 + 0 - 0} \\
   &= \frac{4}{2} = 2
   \end{align}
$$

4. Explanation of dominance:
   Factoring out $n^2$ reveals that every lower-order term ($n$ and constant terms) is suppressed by a factor of $\frac{1}{n}$ or $\frac{1}{n^2}$. As $n$ grows without bound, these ratios approach zero, leaving only the coefficients of the highest-degree terms $4n^2$ and $2n^2$ to dictate the value of the quotient.

---

## Result

$$
\lim_{n\to\infty}\frac{4n^2-3n+1}{2n^2+5n-7} = 2
$$

---

## Verification

**Pass 1 — Algebraic check:** Factor out $n^2$ from numerator and denominator: $\frac{n^2(4 - 3/n + 1/n^2)}{n^2(2 + 5/n - 7/n^2)} = \frac{4 - 3/n + 1/n^2}{2 + 5/n - 7/n^2}$. The cancelled factor $n^2/n^2 = 1$ is valid for all $n \ge 1$, and setting $1/n \to 0$ directly produces $4/2 = 2$.

**Pass 2 — Numerical check:** Evaluate the sequence at $n = 100$:

$$
\frac{4(10000) - 3(100) + 1}{2(10000) + 5(100) - 7} = \frac{40000 - 300 + 1}{20000 + 500 - 7} = \frac{39701}{20493} \approx 1.9373
$$

At $n = 1000$:

$$
\frac{4(10^6) - 3000 + 1}{2(10^6) + 5000 - 7} = \frac{3997001}{2004993} \approx 1.99352
$$

The values approach 2 monotonically from below as $n$ increases.

**Pass 3 — Consistency check:** Both numerator and denominator have degree 2. When degrees match, the limit of a rational sequence must be finite, non-zero, and equal to the ratio of the leading coefficients $\frac{a_2}{b_2} = \frac{4}{2} = 2$.

---

## Exam tip

For rational limits at infinity, divide every term by the highest power of $n$ in the denominator to avoid the indeterminate form $\frac{\infty}{\infty}$.

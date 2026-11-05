# Exercise 2

**Problem:** Compute
$$\lim_{n\to\infty}\frac{3n+1}{n^2+4},\qquad \lim_{n\to\infty}\frac{2n^3-n}{5n^2+1}.$$
Compare the two cases and formulate a general observation about the degrees of the polynomials in the numerator and denominator.

---

## Relevant theorem / definition

Let $P(n) = a_p n^p + \dots + a_0$ and $Q(n) = b_q n^q + \dots + b_0$ be real polynomials with $a_p \neq 0$, $b_q \neq 0$, and degrees $p = \deg(P)$, $q = \deg(Q)$. The asymptotic behavior of their quotient as $n \to \infty$ satisfies:

$$
\lim_{n\to\infty} \frac{P(n)}{Q(n)} = \begin{cases} 0 & \text{if } p < q \\ \dfrac{a_p}{b_q} & \text{if } p = q \\ \operatorname{sgn}\left(\dfrac{a_p}{b_q}\right) \cdot \infty & \text{if } p > q \end{cases}
$$

---

## Solution

1. First limit:

$$
   \lim_{n\to\infty}\frac{3n+1}{n^2+4}
$$

   The degree of the numerator is $p = 1$, and the degree of the denominator is $q = 2$.
   Divide numerator and denominator by $n^2$:

$$
   \begin{align}
   \lim_{n\to\infty}\frac{3n+1}{n^2+4} &= \lim_{n\to\infty}\frac{\frac{3}{n} + \frac{1}{n^2}}{1 + \frac{4}{n^2}} \\
   &= \frac{0 + 0}{1 + 0} \\
   &= 0
   \end{align}
$$

2. Second limit:

$$
   \lim_{n\to\infty}\frac{2n^3-n}{5n^2+1}
$$

   The degree of the numerator is $p = 3$, and the degree of the denominator is $q = 2$.
   Divide numerator and denominator by $n^2$:

$$
   \begin{align}
   \lim_{n\to\infty}\frac{2n^3-n}{5n^2+1} &= \lim_{n\to\infty}\frac{2n - \frac{1}{n}}{5 + \frac{1}{n^2}}
   \end{align}
$$

   As $n \to \infty$, the numerator $2n - \frac{1}{n} \to \infty$ and the denominator $5 + \frac{1}{n^2} \to 5$. Therefore:

$$
   \lim_{n\to\infty}\frac{2n^3-n}{5n^2+1} = +\infty
$$

   The sequence diverges to $+\infty$.

3. Comparison and general observation:
   - In the first case, the denominator grows strictly faster than the numerator ($\deg(P) < \deg(Q)$). The quotient is driven to 0 as $n \to \infty$.
   - In the second case, the numerator grows strictly faster than the denominator ($\deg(P) > \deg(Q)$). The quotient grows without bound, diverging to $+\infty$ (with sign given by $\operatorname{sgn}(a_p / b_q)$).
   - General observation: For any rational sequence $\frac{P(n)}{Q(n)}$, comparing the degrees of numerator and denominator immediately classifies its asymptotic fate: strictly smaller numerator degree yields 0, equal degrees yield the finite non-zero constant $\frac{a_p}{b_q}$, and strictly larger numerator degree yields divergence to $\pm\infty$.

---

## Result

$$
\lim_{n\to\infty}\frac{3n+1}{n^2+4} = 0, \qquad \lim_{n\to\infty}\frac{2n^3-n}{5n^2+1} = +\infty
$$

---

## Verification

**Pass 1 — Algebraic check:** Factoring powers of $n$: for the first expression, $\frac{n(3 + 1/n)}{n^2(1 + 4/n^2)} = \frac{1}{n}\frac{3 + 1/n}{1 + 4/n^2} \to 0 \cdot 3 = 0$. For the second expression, $\frac{n^3(2 - 1/n^2)}{n^2(5 + 1/n^2)} = n \frac{2 - 1/n^2}{5 + 1/n^2} \to \infty \cdot \frac{2}{5} = +\infty$.

**Pass 2 — Numerical check:**
At $n = 100$:

$$
\frac{3(100)+1}{100^2+4} = \frac{301}{10004} \approx 0.030088
$$

At $n = 1000$:

$$
\frac{3001}{1000004} \approx 0.003001 \to 0
$$

For the second sequence at $n = 100$:

$$
\frac{2(100)^3 - 100}{5(100)^2 + 1} = \frac{1999900}{50001} \approx 39.9972
$$

At $n = 1000$:

$$
\frac{2(10^9) - 1000}{5(10^6) + 1} = \frac{1999999000}{5000001} \approx 399.9997 \to +\infty
$$

**Pass 3 — Consistency check:** Since $3n+1 < n^2+4$ for all $n \ge 1$, the first sequence is bounded between 0 and 1 and decreases towards 0. For the second sequence, $2n^3 - n > 0$ and $5n^2+1 > 0$ for $n \ge 1$, and its leading term behaves as $\frac{2}{5}n$, which is positive and unbounded.

---

## Exam tip

Compare the highest power of the numerator to the highest power of the denominator before doing any algebra: smaller degree gives 0, larger degree gives infinity.

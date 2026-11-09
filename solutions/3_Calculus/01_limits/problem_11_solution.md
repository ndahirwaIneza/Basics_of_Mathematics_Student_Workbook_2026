# Exercise 11

**Problem:** Compute
$$\lim_{n\to\infty}\sqrt[n]{5^n+2^n}.$$
Explain which term dominates and why the transformation looks different from the case of a quotient of polynomials.

---

## Relevant theorem / definition

1. Squeeze Theorem for sequences: If $u_n \le a_n \le v_n$ for all $n \ge N_0$ and $\lim_{n\to\infty} u_n = \lim_{n\to\infty} v_n = L$, then $\lim_{n\to\infty} a_n = L$.
2. Standard limit: For any constant $c > 0$, $\lim_{n\to\infty} \sqrt[n]{c} = 1$.
3. Dominant exponential base: For positive bases $a > b > 0$, $\left(\frac{b}{a}\right)^n \to 0$ as $n \to \infty$.

---

## Solution

1. Identify the dominant term:
   The two exponential terms are $5^n$ and $2^n$. Because $5 > 2$, the ratio satisfies:

$$
   \frac{2^n}{5^n} = \left(\frac{2}{5}\right)^n \xrightarrow{n\to\infty} 0
$$

   Therefore, $5^n$ dominates the sum completely as $n \to \infty$.

2. Factor out the dominant term $5^n$ from inside the radical:

$$
   \sqrt[n]{5^n+2^n} = \sqrt[n]{5^n\left(1 + \left(\frac{2}{5}\right)^n\right)} = \sqrt[n]{5^n} \cdot \sqrt[n]{1 + \left(\frac{2}{5}\right)^n} = 5\left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n}
$$

3. Evaluate the limit using the Squeeze Theorem:
   For all $n \ge 1$, since $2^n > 0$:

$$
   5^n < 5^n + 2^n < 5^n + 5^n = 2 \cdot 5^n
$$

   Taking the $n$-th root of all three parts:

$$
   \sqrt[n]{5^n} < \sqrt[n]{5^n + 2^n} < \sqrt[n]{2 \cdot 5^n}
$$

$$
   5 < \sqrt[n]{5^n + 2^n} < 5 \cdot \sqrt[n]{2}
$$

4. Compute the limits of the bounding sequences:

$$
   \lim_{n\to\infty} 5 = 5
$$

$$
   \lim_{n\to\infty} \left(5 \cdot \sqrt[n]{2}\right) = 5 \cdot \lim_{n\to\infty} 2^{1/n} = 5 \cdot 2^0 = 5 \cdot 1 = 5
$$

   By the Squeeze Theorem:

$$
   \lim_{n\to\infty}\sqrt[n]{5^n+2^n} = 5
$$

5. Why the transformation looks different from a quotient of polynomials:
   - Growth mechanism: In polynomial quotients $\frac{P(n)}{Q(n)}$, dominance is governed by power terms $n^k$, and dividing by $n^k$ scales down all terms simultaneously using the algebraic rules of fractions. Here, growth is exponential ($c^n$), where the base difference $5 > 2$ drives the subdominant term to zero exponentially.
   - Outer operator: A polynomial quotient has division as the outer operation. Here, the outer operation is the $n$-th root $(\cdot)^{1/n}$, which varies with $n$. Factoring out $5^n$ extracts $\sqrt[n]{5^n} = 5$ directly outside the radical, leaving an internal factor whose exponent $\frac{1}{n}$ vanishes as $n \to \infty$. Thus, the Squeeze Theorem with constant and near-constant outer bounds provides the direct justification rather than division of fractions.

---

## Result

$$
\lim_{n\to\infty}\sqrt[n]{5^n+2^n} = 5
$$

---

## Verification

**Pass 1 — Algebraic check:**
Take the natural logarithm of $a_n = 5\left(1 + (2/5)^n\right)^{1/n}$:

$$
\ln a_n = \ln 5 + \frac{1}{n}\ln\left(1 + \left(\frac{2}{5}\right)^n\right)
$$

As $n \to \infty$, $(2/5)^n \to 0$, so $\ln(1 + (2/5)^n) \to \ln(1) = 0$. Hence:

$$
\lim_{n\to\infty}\ln a_n = \ln 5 + 0 \cdot 0 = \ln 5 \implies \lim_{n\to\infty} a_n = e^{\ln 5} = 5
$$

**Pass 2 — Numerical check:**
Compute values for increasing $n$:
- $n = 1$: $\sqrt[1]{5^1 + 2^1} = 7$
- $n = 2$: $\sqrt{5^2 + 2^2} = \sqrt{25 + 4} = \sqrt{29} \approx 5.38516$
- $n = 5$: $\sqrt[5]{5^5 + 2^5} = \sqrt[5]{3125 + 32} = \sqrt[5]{3157} \approx 5.01019831$
- $n = 10$: $\sqrt[10]{5^{10} + 2^{10}} = \sqrt[10]{9765625 + 1024} = \sqrt[10]{9766649} \approx 5.00005243$
The values converge rapidly and monotonically to 5.

**Pass 3 — Consistency check:** For any two positive constants $a, b > 0$, $\lim_{n\to\infty} \sqrt[n]{a^n + b^n} = \max(a, b)$. Since $\max(5, 2) = 5$, the result is completely consistent with the general $\ell^\infty$ norm limit $\lim_{p\to\infty} \|(a, b)\|_p = \|(a, b)\|_\infty$.

---

## Exam tip

For the $n$-th root of a sum of exponentials $\sqrt[n]{a^n + b^n + \dots}$, the limit is always simply the largest base among them.

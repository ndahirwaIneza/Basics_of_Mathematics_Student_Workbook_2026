# Exercise 3

**Problem:** Compute
$$\lim_{n\to\infty}\left(\sqrt{n^2+5n}-n\right).$$
Use the conjugate expression and explain why this transformation removes the difficulty.

---

## Relevant theorem / definition

For algebraic expressions involving square roots that result in the indeterminate form $\infty - \infty$, the difference of squares identity:

$$
(A - B)(A + B) = A^2 - B^2
$$

allows multiplying and dividing by the conjugate $(A + B)$ to rationalize the expression:

$$
A - B = \frac{A^2 - B^2}{A + B}
$$

---

## Solution

1. Identify the indeterminate form:
   As $n \to \infty$, $\sqrt{n^2+5n} \to \infty$ and $n \to \infty$. This presents the indeterminate form $\infty - \infty$. Direct subtraction is impossible because the dominant orders of magnitude ($n$) cancel, leaving lower-order terms to govern the value.

2. Multiply and divide by the conjugate expression $\sqrt{n^2+5n} + n$:

$$
   \sqrt{n^2+5n}-n = \frac{\left(\sqrt{n^2+5n}-n\right)\left(\sqrt{n^2+5n}+n\right)}{\sqrt{n^2+5n}+n}
$$

3. Expand the numerator using the difference of squares $(A-B)(A+B) = A^2 - B^2$:

$$
   \frac{\left(\sqrt{n^2+5n}\right)^2 - n^2}{\sqrt{n^2+5n}+n} = \frac{n^2 + 5n - n^2}{\sqrt{n^2+5n}+n} = \frac{5n}{\sqrt{n^2+5n}+n}
$$

4. Factor out $n$ from the radical in the denominator (since $n > 0$, $\sqrt{n^2} = n$):

$$
   \sqrt{n^2+5n}+n = \sqrt{n^2\left(1 + \frac{5}{n}\right)} + n = n\sqrt{1 + \frac{5}{n}} + n = n\left(\sqrt{1 + \frac{5}{n}} + 1\right)
$$

5. Divide numerator and denominator by $n$:

$$
   \frac{5n}{n\left(\sqrt{1 + \frac{5}{n}} + 1\right)} = \frac{5}{\sqrt{1 + \frac{5}{n}} + 1}
$$

6. Compute the limit as $n \to \infty$:

$$
   \begin{align}
   \lim_{n\to\infty}\left(\sqrt{n^2+5n}-n\right) &= \lim_{n\to\infty}\frac{5}{\sqrt{1 + \frac{5}{n}} + 1} \\
   &= \frac{5}{\sqrt{1 + 0} + 1} \\
   &= \frac{5}{1 + 1} = \frac{5}{2}
   \end{align}
$$

7. Why the transformation removes the difficulty:
   The original subtraction creates catastrophic cancellation between two unbounded terms of the same order $\mathcal{O}(n)$. Multiplying by the conjugate replaces the subtraction with an addition in the denominator ($A+B$), converting an intractable $\infty - \infty$ difference into an evaluable $\frac{\infty}{\infty}$ ratio where the dominant linear powers in numerator and denominator can be factored out and cancelled.

---

## Result

$$
\lim_{n\to\infty}\left(\sqrt{n^2+5n}-n\right) = \frac{5}{2}
$$

---

## Verification

**Pass 1 — Algebraic check:** Expand $\sqrt{n^2+5n}$ via the generalized binomial series for large $n$:

$$
\sqrt{n^2+5n} = n\left(1 + \frac{5}{n}\right)^{1/2} = n\left(1 + \frac{1}{2}\cdot\frac{5}{n} - \frac{1}{8}\cdot\frac{25}{n^2} + \mathcal{O}(n^{-3})\right) = n + \frac{5}{2} - \frac{25}{8n} + \mathcal{O}(n^{-2})
$$

Subtracting $n$:

$$
\sqrt{n^2+5n} - n = \frac{5}{2} - \frac{25}{8n} + \mathcal{O}(n^{-2}) \xrightarrow{n\to\infty} \frac{5}{2}
$$

**Pass 2 — Numerical check:**
At $n = 100$:

$$
\sqrt{100^2 + 5(100)} - 100 = \sqrt{10500} - 100 \approx 102.4695077 - 100 = 2.4695077
$$

At $n = 1000$:

$$
\sqrt{1000^2 + 5(1000)} - 1000 = \sqrt{1005000} - 1000 \approx 1002.496883 - 1000 = 2.496883
$$

At $n = 10000$:

$$
\sqrt{10^8 + 50000} - 10000 \approx 10002.499688 - 10000 = 2.499688 \to 2.5 = \frac{5}{2}
$$

**Pass 3 — Consistency check:** Since $n^2 + 5n > n^2$ for all $n > 0$, $\sqrt{n^2+5n} > n$, meaning every term is strictly positive. Furthermore, $\sqrt{n^2+5n} < \sqrt{n^2+5n+6.25} = n + 2.5$, so the sequence is strictly bounded above by $\frac{5}{2}$ and strictly increases toward it.

---

## Exam tip

Whenever you encounter $\sqrt{A} - \sqrt{B}$ yielding $\infty - \infty$, multiply numerator and denominator by $\sqrt{A} + \sqrt{B}$ to convert subtraction into addition.

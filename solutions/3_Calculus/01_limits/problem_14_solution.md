# Exercise 14

**Problem:** Compute
$$\lim_{x\to0}\frac{1-\cos x}{x^2}.$$
Justify the result without using l'Hôpital's rule, using a trigonometric identity and the fundamental limit.

---

## Relevant theorem / definition

1. Pythagorean trigonometric identity:

$$
   1 - \cos^2 x = \sin^2 x
$$

2. Fundamental trigonometric limit:

$$
   \lim_{x\to0}\frac{\sin x}{x} = 1
$$

3. Product rule for limits: If $\lim_{x\to c} f(x)$ and $\lim_{x\to c} g(x)$ exist, then $\lim_{x\to c}[f(x)g(x)] = \left[\lim_{x\to c} f(x)\right]\left[\lim_{x\to c} g(x)\right]$.

---

## Solution

1. Test for direct substitution:
   As $x \to 0$:

$$
   1 - \cos(0) = 1 - 1 = 0, \qquad 0^2 = 0
$$

   This yields the indeterminate form $\frac{0}{0}$.

2. Rationalize the trigonometric expression:
   Multiply numerator and denominator by the conjugate $(1 + \cos x)$:

$$
   \frac{1-\cos x}{x^2} = \frac{(1-\cos x)(1+\cos x)}{x^2(1+\cos x)}
$$

3. Simplify using the difference of squares and the Pythagorean identity:

$$
   (1 - \cos x)(1 + \cos x) = 1 - \cos^2 x = \sin^2 x
$$

   Substitute back into the quotient:

$$
   \frac{1-\cos x}{x^2} = \frac{\sin^2 x}{x^2(1+\cos x)}
$$

4. Group terms into products of known limits:
   Separate the expression into the square of the fundamental limit and a continuous fraction:

$$
   \frac{\sin^2 x}{x^2(1+\cos x)} = \left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x}
$$

5. Evaluate the limit using the fundamental trigonometric limit:

$$
   \begin{align}
   \lim_{x\to0}\frac{1-\cos x}{x^2} &= \lim_{x\to0}\left[\left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x}\right] \\
   &= \left(\lim_{x\to0}\frac{\sin x}{x}\right)^2 \cdot \lim_{x\to0}\frac{1}{1 + \cos x} \\
   &= (1)^2 \cdot \frac{1}{1 + \cos(0)} \\
   &= 1 \cdot \frac{1}{1 + 1} \\
   &= \frac{1}{2}
   \end{align}
$$

---

## Result

$$
\lim_{x\to0}\frac{1-\cos x}{x^2} = \frac{1}{2}
$$

---

## Verification

**Pass 1 — Algebraic check:**
Use the half-angle identity $1 - \cos x = 2\sin^2\left(\frac{x}{2}\right)$:

$$
\frac{1-\cos x}{x^2} = \frac{2\sin^2\left(\frac{x}{2}\right)}{x^2} = \frac{2\sin^2\left(\frac{x}{2}\right)}{4 \cdot \left(\frac{x}{2}\right)^2} = \frac{1}{2}\left(\frac{\sin(x/2)}{x/2}\right)^2
$$

Setting $u = \frac{x}{2} \to 0$:

$$
\lim_{u\to0}\frac{1}{2}\left(\frac{\sin u}{u}\right)^2 = \frac{1}{2}(1)^2 = \frac{1}{2}
$$

Both identities yield the identical result.

**Pass 2 — Numerical check:**
Compute values for small $x$:
- At $x = 0.1$:

$$
  \cos(0.1) \approx 0.995004165
$$

$$
  \frac{1 - 0.995004165}{0.01} = \frac{0.004995835}{0.01} \approx 0.499584
$$

- At $x = 0.01$:

$$
  \cos(0.01) \approx 0.9999500004
$$

$$
  \frac{1 - 0.9999500004}{0.0001} = \frac{0.0000499996}{0.0001} \approx 0.499996 \to 0.5 = \frac{1}{2}
$$

**Pass 3 — Consistency check:** The Taylor series expansion of $\cos x$ about $x = 0$ is $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots$. Thus:

$$
1 - \cos x = \frac{x^2}{2} - \frac{x^4}{24} + \dots \implies \frac{1 - \cos x}{x^2} = \frac{1}{2} - \frac{x^2}{24} + \dots \xrightarrow{x\to0} \frac{1}{2}
$$

---

## Exam tip

Whenever $1 - \cos x$ appears in a limit, multiply numerator and denominator by $1 + \cos x$ or substitute the half-angle formula $2\sin^2(x/2)$ to create $\sin^2 x$.

# Exercise 6

**Problem:** Compute
$$\lim_{x\to\infty}\frac{3x^2-x+1}{5x^2+4x-2}.$$
Compare the method with Exercise 1. Explain what changes when moving from $n$ to a real variable $x$, and what stays the same.

---

## Relevant theorem / definition

Heine's characterization of limits (sequential criterion): A function $f(x)$ has a limit $L$ as $x \to \infty$ if and only if for every sequence $(x_n)_{n=1}^\infty$ satisfying $x_n \to \infty$ as $n \to \infty$, the sequence of function values satisfies $\lim_{n\to\infty} f(x_n) = L$.

---

## Solution

1. Identify the indeterminate form:
   As $x \to \infty$, $3x^2 - x + 1 \to \infty$ and $5x^2 + 4x - 2 \to \infty$, producing the indeterminate form $\frac{\infty}{\infty}$.

2. Divide numerator and denominator by the highest power of $x$ in the denominator, which is $x^2$:

$$
   \frac{3x^2-x+1}{5x^2+4x-2} = \frac{\frac{3x^2}{x^2} - \frac{x}{x^2} + \frac{1}{x^2}}{\frac{5x^2}{x^2} + \frac{4x}{x^2} - \frac{2}{x^2}} = \frac{3 - \frac{1}{x} + \frac{1}{x^2}}{5 + \frac{4}{x} - \frac{2}{x^2}}
$$

3. Compute the limit using standard limits $\lim_{x\to\infty} \frac{1}{x} = 0$ and $\lim_{x\to\infty} \frac{1}{x^2} = 0$:

$$
   \begin{align}
   \lim_{x\to\infty}\frac{3x^2-x+1}{5x^2+4x-2} &= \lim_{x\to\infty}\frac{3 - \frac{1}{x} + \frac{1}{x^2}}{5 + \frac{4}{x} - \frac{2}{x^2}} \\
   &= \frac{\lim_{x\to\infty} 3 - \lim_{x\to\infty}\frac{1}{x} + \lim_{x\to\infty}\frac{1}{x^2}}{\lim_{x\to\infty} 5 + 4\lim_{x\to\infty}\frac{1}{x} - 2\lim_{x\to\infty}\frac{1}{x^2}} \\
   &= \frac{3 - 0 + 0}{5 + 0 - 0} \\
   &= \frac{3}{5}
   \end{align}
$$

4. Comparison with Exercise 1:
   - What stays the same:
     The dominant algebraic mechanism is identical. In both cases, the highest-power term ($x^2$ or $n^2$) grows faster than all lower-order terms, so dividing numerator and denominator by that power reduces all lower-order terms to zero. The arithmetic laws of limits apply equally to sequences and functions.
   - What changes:
     The variable domain transitions from the discrete natural numbers $n \in \mathbb{N}$ to the continuous real numbers $x \in \mathbb{R}$. In a function limit, $x$ can approach infinity continuously along all real paths (including non-integers). While sequences cannot be differentiated with respect to $n$, functions of a real variable $x$ are differentiable, enabling alternative continuous tools such as l'Hôpital's rule.

---

## Result

$$
\lim_{x\to\infty}\frac{3x^2-x+1}{5x^2+4x-2} = \frac{3}{5}
$$

---

## Verification

**Pass 1 — Algebraic check:** Apply l'Hôpital's rule twice to the $\frac{\infty}{\infty}$ form:

$$
\lim_{x\to\infty}\frac{3x^2-x+1}{5x^2+4x-2} \stackrel{\text{H}}{=} \lim_{x\to\infty}\frac{6x-1}{10x+4} \stackrel{\text{H}}{=} \lim_{x\to\infty}\frac{6}{10} = \frac{3}{5}
$$

**Pass 2 — Numerical check:**
Evaluate at $x = 100$:

$$
\frac{3(10000) - 100 + 1}{5(10000) + 4(100) - 2} = \frac{29901}{50398} \approx 0.593297
$$

Evaluate at $x = 1000$:

$$
\frac{3(10^6) - 1000 + 1}{5(10^6) + 4(1000) - 2} = \frac{2999001}{5003998} \approx 0.599321 \approx 0.6 = \frac{3}{5}
$$

**Pass 3 — Consistency check:** The rational function has equal degrees in numerator and denominator ($p = q = 2$). The asymptotic horizontal line is $y = \frac{a_2}{b_2} = \frac{3}{5}$, which constitutes a horizontal asymptote as $x \to +\infty$.

---

## Exam tip

The algebraic rules for dominant powers at infinity are completely identical for sequences and functions; factor out the highest power of the variable.

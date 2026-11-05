# Exercise 4

**Problem:** Analyze
$$\left(\frac23\right)^n,\qquad \left(\frac32\right)^n,\qquad (-1)^n,\qquad \frac{(-1)^n}{n}.$$
For each sequence, describe the type of behavior and justify your answer.

---

## Relevant theorem / definition

1. Geometric sequence theorem: For $a_n = q^n$ with $q \in \mathbb{R}$:
   - If $|q| < 1$, $\lim_{n\to\infty} q^n = 0$ (convergent).
   - If $q = 1$, $\lim_{n\to\infty} q^n = 1$ (convergent).
   - If $q > 1$, $\lim_{n\to\infty} q^n = +\infty$ (divergent to $+\infty$).
   - If $q \le -1$, the sequence oscillates without a limit (divergent by oscillation).

2. Squeeze theorem: If $u_n \le a_n \le v_n$ for all $n \ge N_0$ and $\lim_{n\to\infty} u_n = \lim_{n\to\infty} v_n = L$, then $\lim_{n\to\infty} a_n = L$.

---

## Solution

1. First sequence: $a_n = \left(\frac{2}{3}\right)^n$
   - Behavior: Monotonically decreasing, strictly positive, bounded, and convergent to 0.
   - Justification: This is a geometric sequence with ratio $q = \frac{2}{3}$. Because $|q| = \frac{2}{3} < 1$, each successive term is $\frac{2}{3}$ of the preceding one. By the geometric sequence limit theorem:

$$
     \lim_{n\to\infty}\left(\frac{2}{3}\right)^n = 0
$$

2. Second sequence: $b_n = \left(\frac{3}{2}\right)^n$
   - Behavior: Monotonically increasing, unbounded above, and divergent to $+\infty$.
   - Justification: This is a geometric sequence with ratio $q = \frac{3}{2} > 1$. Writing $q = 1 + \frac{1}{2}$, Bernoulli's inequality gives:

$$
     \left(\frac{3}{2}\right)^n = \left(1 + \frac{1}{2}\right)^n \ge 1 + \frac{n}{2}
$$

     As $n \to \infty$, $1 + \frac{n}{2} \to +\infty$. By comparison:

$$
     \lim_{n\to\infty}\left(\frac{3}{2}\right)^n = +\infty
$$

3. Third sequence: $c_n = (-1)^n$
   - Behavior: Bounded, oscillating, and divergent (the limit does not exist).
   - Justification: The sequence alternates indefinitely between $-1$ and $+1$:

$$
     -1, \; 1, \; -1, \; 1, \; -1, \; 1, \dots
$$

     Consider the even and odd subsequences:

$$
     c_{2k} = (-1)^{2k} = 1 \implies \lim_{k\to\infty} c_{2k} = 1
$$

$$
     c_{2k-1} = (-1)^{2k-1} = -1 \implies \lim_{k\to\infty} c_{2k-1} = -1
$$

     Because two subsequences converge to distinct limits ($1 \neq -1$), the full sequence does not possess a limit.

4. Fourth sequence: $d_n = \frac{(-1)^n}{n}$
   - Behavior: Damped oscillating, bounded, and convergent to 0.
   - Justification: The terms alternate in sign with decaying amplitude: $-1, \frac{1}{2}, -\frac{1}{3}, \frac{1}{4}, \dots$.
     For all $n \ge 1$, we establish the squeeze inequality:

$$
     -\frac{1}{n} \le \frac{(-1)^n}{n} \le \frac{1}{n}
$$

     Taking limits of the bounding sequences:

$$
     \lim_{n\to\infty} \left(-\frac{1}{n}\right) = 0, \qquad \lim_{n\to\infty} \frac{1}{n} = 0
$$

     By the squeeze theorem:

$$
     \lim_{n\to\infty}\frac{(-1)^n}{n} = 0
$$

---

## Result

$$
\lim_{n\to\infty}\left(\frac{2}{3}\right)^n = 0 \quad (\text{converges}), \qquad \lim_{n\to\infty}\left(\frac{3}{2}\right)^n = +\infty \quad (\text{diverges to } +\infty)
$$

$$
\lim_{n\to\infty}(-1)^n \quad \text{does not exist (diverges by oscillation)}
$$

$$
\lim_{n\to\infty}\frac{(-1)^n}{n} = 0 \quad (\text{converges by squeeze theorem})
$$

---

## Verification

**Pass 1 — Algebraic check:**
- For $(2/3)^n$: $\ln((2/3)^n) = n\ln(2/3) = -n\ln(1.5) \to -\infty \implies e^{-\infty} = 0$.
- For $(3/2)^n$: $\ln((3/2)^n) = n\ln(1.5) \to +\infty \implies e^{+\infty} = +\infty$.
- For $(-1)^n$: difference $|c_{n+1} - c_n| = 2$ for all $n$, violating the Cauchy criterion.
- For $(-1)^n/n$: absolute value $|d_n| = \frac{1}{n} \to 0$, which is equivalent to $d_n \to 0$.

**Pass 2 — Numerical check:**
Evaluate each at $n = 10$:

$$
\left(\frac{2}{3}\right)^{10} \approx 0.01734, \quad \left(\frac{3}{2}\right)^{10} \approx 57.665, \quad (-1)^{10} = 1, \quad \frac{(-1)^{10}}{10} = 0.1
$$

Evaluate each at $n = 11$:

$$
\left(\frac{2}{3}\right)^{11} \approx 0.01156, \quad \left(\frac{3}{2}\right)^{11} \approx 86.498, \quad (-1)^{11} = -1, \quad \frac{(-1)^{11}}{11} \approx -0.0909
$$

The first decays toward 0, the second explodes toward $+\infty$, the third flips between $1$ and $-1$, and the fourth narrows its oscillation about 0.

**Pass 3 — Consistency check:** An oscillating sequence converges if and only if its amplitude decays to 0. Sequence $(-1)^n$ has constant amplitude 1 (diverges), whereas $(-1)^n/n$ has amplitude $1/n \to 0$ (converges).

---

## Exam tip

Oscillation does not automatically imply divergence; if the amplitude of the oscillations tends to zero, the sequence converges to zero.

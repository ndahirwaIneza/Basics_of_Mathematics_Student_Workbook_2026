# Exercise 6

**Problem:** Analyze the domain, zero, and monotonicity of

$$
f(x)=\ln x-x+1.
$$

Explain why the analysis must begin with the domain.

---

## Relevant theorem / definition

1. Natural logarithm domain: The function $\ln x$ is defined if and only if its argument is strictly positive: $x \in (0, \infty)$.
2. Derivative of $\ln x$: For $x > 0$, $\frac{d}{dx}(\ln x) = \frac{1}{x}$.
3. First derivative test for global extrema: If $f$ is continuous on an open interval $I$ and has a unique critical point $c \in I$ at which $f$ attains a strict local maximum, then $f(c)$ is the unique global maximum of $f$ on $I$.

---

## Solution

1. Why the analysis must begin with the domain:
   The natural logarithm $\ln x$ is defined exclusively for strictly positive real arguments. Performing operations such as differentiation, finding zeros, or computing limits without knowing the domain is mathematically invalid, as it risks evaluating expressions at undefined points (such as $x \le 0$) or formulating false conclusions about the behavior of the function on non-existent intervals. The domain defines the universe of discourse on which every subsequent theorem (continuity, differentiability, Mean Value Theorem) operates.

2. Domain:
   The condition for the existence of $\ln x$ is:

$$
   x > 0
$$

   Thus, the domain is:

$$
   D = (0, \infty)
$$

3. Derivative and critical points:
   Differentiate $f(x)$ on its domain $(0, \infty)$:

$$
   f'(x) = \frac{d}{dx}(\ln x - x + 1) = \frac{1}{x} - 1 = \frac{1 - x}{x}
$$

   Set $f'(x) = 0$:

$$
   \frac{1 - x}{x} = 0 \iff 1 - x = 0 \iff x = 1
$$

   Since $1 \in D$, $x = 1$ is the unique critical point.

4. Monotonicity:
   For all $x \in (0, \infty)$, the denominator of $f'(x)$ satisfies $x > 0$. Hence, the sign of $f'(x)$ is determined solely by the numerator $1 - x$:
   - For $x \in (0, 1)$: $1 - x > 0 \implies f'(x) > 0$. The function is strictly increasing on $(0, 1]$.
   - For $x \in (1, \infty)$: $1 - x < 0 \implies f'(x) < 0$. The function is strictly decreasing on $[1, \infty)$.

5. Extrema and zeros:
   Because $f$ is strictly increasing on $(0, 1]$ and strictly decreasing on $[1, \infty)$, the critical point $x = 1$ is a strict global maximum on $(0, \infty)$.
   Evaluate $f$ at $x = 1$:

$$
   f(1) = \ln(1) - 1 + 1 = 0 - 1 + 1 = 0
$$

   The maximum value is $0$, achieved at $x = 1$.
   Since $f(1) = 0$ is the strict maximum:

$$
   f(x) < f(1) = 0 \quad \text{for all } x \in (0, 1) \cup (1, \infty)
$$

   Therefore, $f(x) = 0$ if and only if $x = 1$. The only zero of $f$ is $x = 1$.
   This also establishes the fundamental tangent-line inequality:

$$
   \ln x \le x - 1 \quad \text{for all } x > 0
$$

   with equality holding exclusively at $x = 1$.

6. Boundary limits:

$$
   \lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (\ln x - x + 1) = -\infty - 0 + 1 = -\infty
$$

$$
   \lim_{x \to \infty} f(x) = \lim_{x \to \infty} x\left(\frac{\ln x}{x} - 1 + \frac{1}{x}\right) = \infty(0 - 1 + 0) = -\infty
$$

---

## Result

$$
\text{Domain: } D = (0, \infty)
$$

$$
\text{Monotonicity: Strictly increasing on } (0, 1], \qquad \text{Strictly decreasing on } [1, \infty)
$$

$$
\text{Global maximum: } (1, 0)
$$

$$
\text{Unique zero: } x = 1
$$

---

## Verification

**Pass 1 — Algebraic check:** Concavity check: $f''(x) = \frac{d}{dx}\left(\frac{1}{x} - 1\right) = -\frac{1}{x^2} < 0$ for all $x \in (0, \infty)$. A strictly concave function on an interval can have at most one critical point, which must be a strict global maximum, and it can intersect any horizontal line at most twice. Since the maximum value is $0$, the line $y = 0$ is a tangent line that meets the curve at exactly one point ($x = 1$).

**Pass 2 — Numerical check:** Evaluate test points on either side of $x = 1$:
$f(0.5) = \ln(0.5) - 0.5 + 1 = -\ln(2) + 0.5 \approx -0.693 + 0.5 = -0.193 < 0$;
$f(2) = \ln(2) - 2 + 1 \approx 0.693 - 1 = -0.307 < 0$;
$f(e) = \ln(e) - e + 1 = 1 - e + 1 = 2 - e \approx 2 - 2.718 = -0.718 < 0$.
All values are strictly negative, confirming $x = 1$ is the unique zero and maximum.

**Pass 3 — Consistency check:** Check the slope at $x = 1$: $f'(1) = 0$. The tangent line to $y = \ln x$ at $x = 1$ is $y = x - 1$. The function $f(x) = \ln x - (x - 1)$ is the difference between the curve and its tangent line. Since $\ln x$ is strictly concave, it lies strictly below its tangent line everywhere except at the point of tangency, guaranteeing $f(x) \le 0$ with equality only at $x = 1$.

---

## Exam tip

Whenever a logarithm appears, write the domain condition $x > 0$ as the very first line before writing down any derivative.

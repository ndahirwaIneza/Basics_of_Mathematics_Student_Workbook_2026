# Exercise 11

**Problem:** For each integral, first write which method you choose and how you recognize it, and then compute:
1. $\int\sin(3x)\,dx$,
2. $\int x\ln x\,dx$,
3. $\int\frac{x}{\sqrt{x^2+1}}\,dx$.

---

## Relevant theorem / definition

1. Linear substitution rule:

$$
\int f(ax+b)\,dx = \frac{1}{a}F(ax+b) + C \quad (a \neq 0)
$$

2. Integration by parts:

$$
\int u\,dv = uv - \int v\,du
$$

3. Power chain substitution rule:

$$
\int [g(x)]^\alpha g'(x)\,dx = \frac{[g(x)]^{\alpha+1}}{\alpha+1} + C \quad (\alpha \neq -1)
$$

---

## Solution

### Part 1: $\int \sin(3x)\,dx$

- Method choice and recognition:
  Linear substitution ($u = 3x$). The argument of the sine function is linear in $x$ with non-zero slope $a = 3$, meaning its derivative is a pure constant.
- Computation:
  Let $u = 3x$, so $du = 3\,dx$, giving $dx = \frac{1}{3}\,du$.

$$
  \int \sin(3x)\,dx = \int \sin(u)\left(\frac{1}{3}\,du\right) = \frac{1}{3}(-\cos u) + C = -\frac{1}{3}\cos(3x) + C
$$

### Part 2: $\int x\ln x\,dx$

- Method choice and recognition:
  Integration by parts. The integrand is a product of an algebraic term ($x$) and a logarithmic term ($\ln x$). Because differentiating $\ln x$ yields a simple algebraic fraction $\frac{1}{x}$, setting $u = \ln x$ converts the integrand entirely into algebraic powers.
- Computation:
  Let:

$$
  u = \ln x \implies du = \frac{1}{x}\,dx
$$

$$
  dv = x\,dx \implies v = \frac{x^2}{2}
$$

  Applying the integration-by-parts formula:

$$
  \begin{align}
  \int x\ln x\,dx &= uv - \int v\,du \\
  &= \frac{x^2}{2}\ln x - \int \frac{x^2}{2} \cdot \frac{1}{x}\,dx \\
  &= \frac{x^2}{2}\ln x - \frac{1}{2}\int x\,dx \\
  &= \frac{x^2}{2}\ln x - \frac{1}{2}\left(\frac{x^2}{2}\right) + C \\
  &= \frac{x^2}{2}\ln x - \frac{x^2}{4} + C
  \end{align}
$$

  Domain: $x \in (0, \infty)$.

### Part 3: $\int\frac{x}{\sqrt{x^2+1}}\,dx$

- Method choice and recognition:
  Substitution. The integrand contains a composite square root with inner quadratic function $g(x) = x^2+1$. The numerator contains $x\,dx$, which is proportional to $g'(x)\,dx = 2x\,dx$.
- Computation:
  Let $u = x^2 + 1$, so $du = 2x\,dx$, which gives $x\,dx = \frac{1}{2}\,du$.
  Rewrite the integral:

$$
  \begin{align}
  \int \frac{x}{\sqrt{x^2+1}}\,dx &= \int \frac{1}{\sqrt{u}}\left(\frac{1}{2}\,du\right) \\
  &= \frac{1}{2}\int u^{-1/2}\,du \\
  &= \frac{1}{2}\left(\frac{u^{1/2}}{\frac{1}{2}}\right) + C \\
  &= \sqrt{u} + C \\
  &= \sqrt{x^2+1} + C
  \end{align}
$$

---

## Result

$$
1. \quad \int\sin(3x)\,dx = -\frac{1}{3}\cos(3x) + C
$$

$$
2. \quad \int x\ln x\,dx = \frac{x^2}{2}\ln x - \frac{x^2}{4} + C, \quad x > 0
$$

$$
3. \quad \int\frac{x}{\sqrt{x^2+1}}\,dx = \sqrt{x^2+1} + C
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiating all three results:
1. $\frac{d}{dx}\left(-\frac{1}{3}\cos(3x)\right) = -\frac{1}{3}\left(-\sin(3x) \cdot 3\right) = \sin(3x)$.
2. $\frac{d}{dx}\left(\frac{x^2}{2}\ln x - \frac{x^2}{4}\right) = \left(x\ln x + \frac{x^2}{2} \cdot \frac{1}{x}\right) - \frac{2x}{4} = x\ln x + \frac{x}{2} - \frac{x}{2} = x\ln x$.
3. $\frac{d}{dx}\left(\sqrt{x^2+1}\right) = \frac{1}{2\sqrt{x^2+1}} \cdot 2x = \frac{x}{\sqrt{x^2+1}}$.
All derivatives match their integrands identically.

**Pass 2 — Numerical check:** For part 2 at $x = 1$: the integrand is $f(1) = 1 \cdot \ln(1) = 0$. The derivative of $F(x)$ at $x = 1$ is $1 \cdot \ln(1) + \frac{1}{2} - \frac{1}{2} = 0$. For part 3 at $x = 1$: $f(1) = \frac{1}{\sqrt{2}} \approx 0.7071$, and $\left.\frac{d}{dx}\sqrt{x^2+1}\right|_{x=1} = \frac{1}{\sqrt{2}}$.

**Pass 3 — Consistency check:** For part 3, as $x \to \infty$, the integrand behaves as $\frac{x}{|x|} = 1$. The antiderivative $\sqrt{x^2+1} \approx x$ for large positive $x$, whose derivative is $1$, matching the limiting behavior.

---

## Exam tip

Whenever $\ln x$ appears in an integrand with an algebraic power, choose $u = \ln x$ in integration by parts because differentiating completely removes the logarithm.

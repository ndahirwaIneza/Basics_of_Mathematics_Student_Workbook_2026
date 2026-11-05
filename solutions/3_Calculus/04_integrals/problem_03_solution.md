# Exercise 3

**Problem:** Compute

$$
\int\left(2e^x+3\cos x-4\sin x\right)\,dx.
$$

Match each term with a known derivative and verify the entire result with one differentiation.

---

## Relevant theorem / definition

The fundamental derivatives of exponential and trigonometric functions are:

$$
\frac{d}{dx}(e^x) = e^x, \quad \frac{d}{dx}(\sin x) = \cos x, \quad \frac{d}{dx}(\cos x) = -\sin x
$$

The corresponding antiderivatives are:

$$
\int e^x\,dx = e^x + C, \quad \int \cos x\,dx = \sin x + C, \quad \int \sin x\,dx = -\cos x + C
$$

---

## Solution

1. Matching each term with a known derivative:
   - For $2e^x$: because $\frac{d}{dx}(e^x) = e^x$, an antiderivative is $2e^x$.
   - For $3\cos x$: because $\frac{d}{dx}(\sin x) = \cos x$, an antiderivative is $3\sin x$.
   - For $-4\sin x$: because $\frac{d}{dx}(\cos x) = -\sin x$, we have $\frac{d}{dx}(4\cos x) = -4\sin x$. Thus an antiderivative is $4\cos x$.

2. Integrating term by term:

$$
   \int\left(2e^x+3\cos x-4\sin x\right)\,dx = 2e^x + 3\sin x + 4\cos x + C
$$

3. Verification by one differentiation:

$$
   \begin{align}
   \frac{d}{dx}\left(2e^x + 3\sin x + 4\cos x + C\right) &= 2\frac{d}{dx}(e^x) + 3\frac{d}{dx}(\sin x) + 4\frac{d}{dx}(\cos x) + \frac{d}{dx}(C) \\
   &= 2e^x + 3\cos x + 4(-\sin x) + 0 \\
   &= 2e^x + 3\cos x - 4\sin x
   \end{align}
$$

---

## Result

$$
\int\left(2e^x+3\cos x-4\sin x\right)\,dx = 2e^x + 3\sin x + 4\cos x + C, \quad C \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiating the antiderivative term by term yields $2e^x + 3\cos x + 4(-\sin x) = 2e^x + 3\cos x - 4\sin x$, reproducing the integrand.

**Pass 2 — Numerical check:** At $x = 0$, $f(0) = 2e^0 + 3\cos(0) - 4\sin(0) = 2(1) + 3(1) - 0 = 5$. Computing $F'(0)$ for $F(x) = 2e^x + 3\sin x + 4\cos x$: $F'(0) = 2e^0 + 3\cos(0) - 4\sin(0) = 2 + 3 - 0 = 5$, which matches $f(0)$.

**Pass 3 — Consistency check:** Since $e^x$, $\sin x$, and $\cos x$ are infinitely differentiable everywhere on $\mathbb{R}$, the antiderivative $F(x)$ is continuous and smooth on $(-\infty, \infty)$ with no singular points.

---

## Exam tip

Pay close attention to trigonometric integration signs: $\int \sin x\,dx = -\cos x + C$, whereas $\int \cos x\,dx = +\sin x + C$.

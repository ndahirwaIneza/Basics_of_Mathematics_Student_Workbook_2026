# Exercise 8

**Problem:** Compute

$$
\int x\cos x\,dx.
$$

Before calculating, justify why it is convenient to differentiate $x$ and integrate $\cos x$, rather than the other way around.

---

## Relevant theorem / definition

The integration-by-parts formula states:

$$
\int u\,dv = uv - \int v\,du
$$

The standard antiderivative of the cosine function is:

$$
\int \cos x\,dx = \sin x + C
$$

---

## Solution

1. Justification of factor choices:
   - Favorable choice (differentiating $x$, integrating $\cos x$):
     Let $u = x$ and $dv = \cos x\,dx$.
     Then $du = dx$ and $v = \sin x$.
     The remaining integral is $\int v\,du = \int \sin x\,dx$, which is an elementary standard trigonometric integral. The algebraic factor $x$ has been eliminated because its derivative is constant.
   - Unfavorable choice (integrating $x$, differentiating $\cos x$):
     If we set $u = \cos x$ and $dv = x\,dx$, we obtain $du = -\sin x\,dx$ and $v = \frac{x^2}{2}$.
     The remaining integral would become $-\int \frac{x^2}{2}\sin x\,dx$. The power of $x$ increased from $1$ to $2$, making the new integral more complicated than the original.
   Therefore, assigning $u = x$ and $dv = \cos x\,dx$ is the correct choice.

2. Computing the integral:
   Let:

$$
   u = x \implies du = dx
$$

$$
   dv = \cos x\,dx \implies v = \sin x
$$

   Applying integration by parts:

$$
   \begin{align}
   \int x\cos x\,dx &= uv - \int v\,du \\
   &= x\sin x - \int \sin x\,dx \\
   &= x\sin x - (-\cos x) + C \\
   &= x\sin x + \cos x + C
   \end{align}
$$

3. Verification by differentiation:
   Apply the product rule to $x\sin x$ and differentiate $\cos x$:

$$
   \begin{align}
   \frac{d}{dx}\left(x\sin x + \cos x + C\right) &= \left[\frac{d}{dx}(x)\sin x + x\frac{d}{dx}(\sin x)\right] + \frac{d}{dx}(\cos x) + 0 \\
   &= 1 \cdot \sin x + x\cos x - \sin x \\
   &= x\cos x
   \end{align}
$$

---

## Result

$$
\int x\cos x\,dx = x\sin x + \cos x + C, \quad C \in \mathbb{R}
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiating the result gives $(x\sin x)' + (\cos x)' = (\sin x + x\cos x) - \sin x = x\cos x$, which equals the integrand.

**Pass 2 — Numerical check:** At $x = \frac{\pi}{2}$, $f\left(\frac{\pi}{2}\right) = \frac{\pi}{2}\cos\left(\frac{\pi}{2}\right) = 0$. The derivative of $F(x) = x\sin x + \cos x$ at $x = \frac{\pi}{2}$ is $F'\left(\frac{\pi}{2}\right) = \sin\left(\frac{\pi}{2}\right) + \frac{\pi}{2}\cos\left(\frac{\pi}{2}\right) - \sin\left(\frac{\pi}{2}\right) = 1 + 0 - 1 = 0$, matching $f\left(\frac{\pi}{2}\right)$.

**Pass 3 — Consistency check:** The integrand $f(x) = x\cos x$ is odd: $f(-x) = (-x)\cos(-x) = -x\cos x = -f(x)$. The antiderivative $F(x) = x\sin x + \cos x$ is even: $F(-x) = (-x)\sin(-x) + \cos(-x) = (-x)(-\sin x) + \cos x = x\sin x + \cos x = F(x)$, verifying the expected symmetry.

---

## Exam tip

Remember the priority rule LIATE (Logarithmic, Inverse trigonometric, Algebraic, Trigonometric, Exponential) to select $u$; Algebraic ($x$) takes precedence over Trigonometric ($\cos x$).

# Exercise 13

**Problem:** Using
$$\lim_{x\to0}\frac{\sin x}{x}=1,$$
compute
$$\lim_{x\to0}\frac{\sin5x}{x},\qquad \lim_{x\to0}\frac{\sin2x}{\sin3x}.$$
In each case, show how you reduce the expression to the fundamental limit.

---

## Relevant theorem / definition

The fundamental trigonometric limit states that with angles measured in radians:

$$
\lim_{u\to0}\frac{\sin u}{u} = 1
$$

By substitution, if $u(x) \to 0$ and $u(x) \neq 0$ for $x \neq 0$, then:

$$
\lim_{x\to0}\frac{\sin(u(x))}{u(x)} = 1
$$

---

## Solution

1. First limit: $\lim_{x\to0}\frac{\sin5x}{x}$
   - Test for direct substitution: As $x \to 0$, $\sin(5 \cdot 0) = 0$ and the denominator is 0, giving the indeterminate form $\frac{0}{0}$.
   - Reduction to fundamental limit: Multiply and divide the denominator by 5 so that the argument of the sine matches the denominator:

$$
     \frac{\sin5x}{x} = 5 \cdot \frac{\sin 5x}{5x}
$$

   - Let $u = 5x$. As $x \to 0$, $u \to 0$.
   - Evaluate the limit:

$$
     \begin{align}
     \lim_{x\to0}\frac{\sin5x}{x} &= \lim_{x\to0}\left(5 \cdot \frac{\sin 5x}{5x}\right) \\
     &= 5 \cdot \lim_{u\to0}\frac{\sin u}{u} \\
     &= 5 \cdot 1 = 5
     \end{align}
$$

2. Second limit: $\lim_{x\to0}\frac{\sin2x}{\sin3x}$
   - Test for direct substitution: As $x \to 0$, $\sin(2 \cdot 0) = 0$ and $\sin(3 \cdot 0) = 0$, giving the indeterminate form $\frac{0}{0}$.
   - Reduction to fundamental limit: Divide both numerator and denominator by $x$:

$$
     \frac{\sin2x}{\sin3x} = \frac{\frac{\sin 2x}{x}}{\frac{\sin 3x}{x}}
$$

     Multiply and divide each piece by its respective angle factor (2 for the numerator, 3 for the denominator):

$$
     \frac{\frac{\sin 2x}{x}}{\frac{\sin 3x}{x}} = \frac{2 \cdot \frac{\sin 2x}{2x}}{3 \cdot \frac{\sin 3x}{3x}} = \frac{2}{3} \cdot \frac{\frac{\sin 2x}{2x}}{\frac{\sin 3x}{3x}}
$$

   - Let $u = 2x$ and $v = 3x$. As $x \to 0$, $u \to 0$ and $v \to 0$.
   - Evaluate the limit using the quotient rule for limits:

$$
     \begin{align}
     \lim_{x\to0}\frac{\sin2x}{\sin3x} &= \frac{2}{3} \cdot \frac{\lim_{u\to0}\frac{\sin u}{u}}{\lim_{v\to0}\frac{\sin v}{v}} \\
     &= \frac{2}{3} \cdot \frac{1}{1} = \frac{2}{3}
     \end{align}
$$

---

## Result

$$
\lim_{x\to0}\frac{\sin5x}{x} = 5, \qquad \lim_{x\to0}\frac{\sin2x}{\sin3x} = \frac{2}{3}
$$

---

## Verification

**Pass 1 — Algebraic check:**
Apply l'Hôpital's rule to each $\frac{0}{0}$ quotient:
- For the first limit:

$$
  \lim_{x\to0}\frac{\sin 5x}{x} \stackrel{\text{H}}{=} \lim_{x\to0}\frac{5\cos 5x}{1} = 5\cos(0) = 5
$$

- For the second limit:

$$
  \lim_{x\to0}\frac{\sin 2x}{\sin 3x} \stackrel{\text{H}}{=} \lim_{x\to0}\frac{2\cos 2x}{3\cos 3x} = \frac{2\cos(0)}{3\cos(0)} = \frac{2}{3}
$$

**Pass 2 — Numerical check:**
Compute values using radian measure for small $x$:
- For the first limit at $x = 0.01$:

$$
  \frac{\sin(0.05)}{0.01} = \frac{0.049979169}{0.01} \approx 4.99792
$$

- At $x = 0.001$:

$$
  \frac{\sin(0.005)}{0.001} = \frac{0.004999979}{0.001} \approx 4.99998 \to 5
$$

- For the second limit at $x = 0.01$:

$$
  \frac{\sin(0.02)}{\sin(0.03)} = \frac{0.019998667}{0.029995500} \approx 0.666722
$$

- At $x = 0.001$:

$$
  \frac{\sin(0.002)}{\sin(0.003)} \approx \frac{0.0019999987}{0.0029999955} \approx 0.666667 \approx \frac{2}{3}
$$

**Pass 3 — Consistency check:** The first-order Taylor polynomial for sine at zero is $\sin(\alpha x) = \alpha x + \mathcal{O}(x^3)$. Substituting this gives $\frac{\sin 5x}{x} = \frac{5x + \mathcal{O}(x^3)}{x} \to 5$ and $\frac{\sin 2x}{\sin 3x} = \frac{2x + \mathcal{O}(x^3)}{3x + \mathcal{O}(x^3)} \to \frac{2}{3}$.

---

## Exam tip

For any limit of the form $\frac{\sin(\alpha x)}{\sin(\beta x)}$ as $x \to 0$, multiply and divide each term by its argument to immediately extract the coefficient ratio $\frac{\alpha}{\beta}$.

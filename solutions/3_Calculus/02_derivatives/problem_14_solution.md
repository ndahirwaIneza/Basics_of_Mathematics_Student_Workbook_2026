# Exercise 14

**Problem:** Investigate the behavior at $x=0$ of
$$f(x)=\begin{cases}x^2,&x\ge0,\\ax,&x<0.\end{cases}$$
For which values of $a$ is the function continuous? For which values do the one-sided derivatives exist and agree? For which value of $a$ is the function differentiable? Explain why continuity alone is not sufficient.

---

## Relevant theorem / definition

A function $f$ is continuous at $x = x_0$ if and only if $\lim_{x \to x_0^+} f(x) = \lim_{x \to x_0^-} f(x) = f(x_0)$.
The one-sided derivatives at $x = x_0$ are defined by:
$$
f'_+(x_0) = \lim_{h \to 0^+} \frac{f(x_0+h) - f(x_0)}{h}, \quad f'_-(x_0) = \lim_{h \to 0^-} \frac{f(x_0+h) - f(x_0)}{h}
$$
A function is differentiable at $x_0$ if and only if both one-sided derivatives exist and are equal ($f'_+(x_0) = f'_-(x_0)$).

---

## Solution

1. Investigate continuity at $x = 0$:
   - Value of the function:
     $$
     f(0) = 0^2 = 0
     $$
   - Right-hand limit ($x \to 0^+$):
     $$
     \lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (x^2) = 0^2 = 0
     $$
   - Left-hand limit ($x \to 0^-$):
     $$
     \lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (ax) = a(0) = 0
     $$
   Because $\lim_{x \to 0^+} f(x) = \lim_{x \to 0^-} f(x) = f(0) = 0$ for every real number $a$, the function $f$ is **continuous at $x = 0$ for all $a \in \mathbb{R}$**.

2. Compute the one-sided derivatives at $x = 0$:
   - Right-hand derivative ($h > 0$):
     Using $f(0+h) = f(h) = h^2$ and $f(0) = 0$:
     $$
     f'_+(0) = \lim_{h \to 0^+} \frac{f(h) - f(0)}{h} = \lim_{h \to 0^+} \frac{h^2 - 0}{h} = \lim_{h \to 0^+} h = 0.
     $$
     The right-hand derivative exists and equals $0$ for all $a \in \mathbb{R}$.
   - Left-hand derivative ($h < 0$):
     Using $f(0+h) = f(h) = ah$ and $f(0) = 0$:
     $$
     f'_-(0) = \lim_{h \to 0^-} \frac{f(h) - f(0)}{h} = \lim_{h \to 0^-} \frac{ah - 0}{h} = \lim_{h \to 0^-} a = a.
     $$
     The left-hand derivative exists and equals $a$ for all $a \in \mathbb{R}$.

3. Determine when one-sided derivatives agree and when $f$ is differentiable:
   The one-sided derivatives agree if and only if:
   $$
   f'_+(0) = f'_-(0) \iff 0 = a \iff a = 0.
   $$
   Since differentiability at a point requires both one-sided derivatives to exist and be equal, the function is **differentiable at $x = 0$ if and only if $a = 0$**, in which case $f'(0) = 0$.

4. Explain why continuity alone is not sufficient:
   Continuity ensures only that the two branches connect at $(0, 0)$ without a jump or gap. Differentiability is a stronger geometric condition requiring the graph to be smooth—that is, possessing a single, unambiguous tangent line at the connection point. When $a \neq 0$, the incoming tangent slope from the left is $a \neq 0$, while the outgoing tangent slope from the right is $0$. This mismatch produces a sharp corner (kink) at $(0,0)$. Thus, continuity is a necessary but not sufficient condition for differentiability.

---

## Result

$$
\text{Continuous at } x = 0 \text{ for: } a \in \mathbb{R} \text{ (all real values of } a\text{)}
$$

$$
\text{One-sided derivatives: } f'_+(0) = 0, \quad f'_-(0) = a \quad (\text{exist for all } a \in \mathbb{R})
$$

$$
\text{One-sided derivatives agree and } f \text{ is differentiable at } x = 0 \text{ if and only if: } a = 0
$$

$$
\text{Reason continuity is not sufficient: Continuity prevents breaks, but differentiability also requires matching directional slopes to prevent sharp corners.}
$$

---

## Verification

**Pass 1 — Algebraic check:** Apply the derivative theorem for piecewise functions. For $x > 0$, $f'(x) = 2x \implies \lim_{x \to 0^+} f'(x) = 0$. For $x < 0$, $f'(x) = a \implies \lim_{x \to 0^-} f'(x) = a$. Since $f$ is continuous at $x = 0$, $f'(0)$ exists if and only if $\lim_{x \to 0^+} f'(x) = \lim_{x \to 0^-} f'(x)$, which requires $0 = a$. When $a = 0$, both limits equal 0, matching $f'(0) = 0$.

**Pass 2 — Numerical check:** Let $a = 2$.
For $h = 0.001 > 0$: $\frac{f(0.001) - f(0)}{0.001} = \frac{(0.001)^2}{0.001} = 0.001 \to 0$.
For $h = -0.001 < 0$: $\frac{f(-0.001) - f(0)}{-0.001} = \frac{2(-0.001)}{-0.001} = 2$.
The limits $0 \neq 2$ disagree for $a = 2$.
Now let $a = 0$:
For $h = -0.001 < 0$: $\frac{0(-0.001)}{-0.001} = 0$, which matches $0$, verifying that only $a = 0$ yields differentiability.

**Pass 3 — Consistency check:** Compare with the absolute value function $g(x) = |x|$, which is continuous everywhere but fails to be differentiable at $x = 0$ because $g'_+(0) = 1 \neq -1 = g'_-(0)$. The piecewise function $f(x)$ with $a \neq 0$ exhibits the exact same corner-point behavior.

---

## Exam tip

Always evaluate one-sided derivatives using the difference quotient limit at the boundary point $x_0$ rather than relying solely on separate branch formulas.

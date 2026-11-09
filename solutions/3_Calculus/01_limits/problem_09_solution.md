# Exercise 9

**Problem:** Analyze the left-hand and right-hand limits of
$$f(x)=\frac1{x-2}$$
as $x\to2$. Does the two-sided limit exist? Interpret the result on a sketch of the graph and identify the vertical asymptote.

---

## Relevant theorem / definition

1. One-sided limits: For $f(x) = \frac{1}{g(x)}$, if $g(x) \to 0$ as $x \to c$, the sign of $g(x)$ determines the directional infinity:
   - If $g(x) \to 0$ with $g(x) < 0$ ($g(x) \to 0^-$), then $\lim_{x\to c^-} \frac{1}{g(x)} = -\infty$.
   - If $g(x) \to 0$ with $g(x) > 0$ ($g(x) \to 0^+$), then $\lim_{x\to c^+} \frac{1}{g(x)} = +\infty$.

2. Two-sided limit existence: A two-sided limit $\lim_{x\to c} f(x) = L$ exists if and only if both one-sided limits exist and are equal finite values ($L \in \mathbb{R}$):

$$
   \lim_{x\to c^-} f(x) = \lim_{x\to c^+} f(x) = L
$$

3. Vertical asymptote: The vertical line $x = c$ is a vertical asymptote of $y = f(x)$ if at least one of the one-sided limits as $x \to c$ is $+\infty$ or $-\infty$.

---

## Solution

1. Left-hand limit as $x \to 2^-$:
   When $x$ approaches 2 from the left ($x < 2$):

$$
   x - 2 < 0 \implies x - 2 \to 0^-
$$

   Taking the reciprocal of a negative quantity approaching zero:

$$
   \lim_{x\to2^-}\frac{1}{x-2} = -\infty
$$

2. Right-hand limit as $x \to 2^+$:
   When $x$ approaches 2 from the right ($x > 2$):

$$
   x - 2 > 0 \implies x - 2 \to 0^+
$$

   Taking the reciprocal of a positive quantity approaching zero:

$$
   \lim_{x\to2^+}\frac{1}{x-2} = +\infty
$$

3. Existence of the two-sided limit:
   The left-hand limit is $-\infty$ and the right-hand limit is $+\infty$.
   Because:

$$
   \lim_{x\to2^-} f(x) = -\infty \neq +\infty = \lim_{x\to2^+} f(x)
$$

   and neither limit is a finite real number, the two-sided limit $\lim_{x\to2} \frac{1}{x-2}$ does not exist.

4. Geometric interpretation, graph sketch, and vertical asymptote:
   - The line $x = 2$ is a vertical asymptote of the curve $y = f(x)$, and the line $y = 0$ (the $x$-axis) is a horizontal asymptote.
   - Left side ($x < 2$): As $x$ increases toward 2 from the left, the negative branch decreases strictly from $y = 0^-$ (passing through $(0, -0.5)$ and $(1, -1)$) and plunges downward toward $-\infty$ along the left side of the vertical asymptote $x = 2$.
   - Right side ($x > 2$): As $x$ moves right from $x = 2^+$, the positive branch descends from $+\infty$ along the right side of $x = 2$, passes through $(3, 1)$ and $(4, 0.5)$, and approaches $y = 0^+$ asymptotically as $x \to +\infty$.
   - The graph is the standard rectangular hyperbola $y = \frac{1}{x}$ shifted $2$ units to the right:

```text
                    y           :  x = 2 (vertical asymptote)
                    ^           :  (+inf)
                    |           :  |
                    |           :  |
                    |           :  \
                    |           :   * (3, 1)
                    |           :    '-.  (4, 0.5)
                    |           :       '---*---.___
  ------------------+-----------+-------------------> x  (horizontal asymptote y = 0)
       ___..---''   |           : 2   3     4
                    * (0,-0.5)  :
                    | '-._      :
                    |     * (1,-1)
                    |      \    :
                    |       |   :
                    |       |   :
                            v   :
                         (-inf) :
```

---

## Result

$$
\lim_{x\to2^-}\frac{1}{x-2} = -\infty, \qquad \lim_{x\to2^+}\frac{1}{x-2} = +\infty
$$

$$
\lim_{x\to2}\frac{1}{x-2} \quad \text{does not exist}
$$

$$
\text{Vertical asymptote: } x = 2
$$

---

## Verification

**Pass 1 — Algebraic check:**
Let $x = 2 + h$.
- For left-hand limit, take $h < 0$: $\lim_{h\to 0^-} \frac{1}{h} = -\infty$.
- For right-hand limit, take $h > 0$: $\lim_{h\to 0^+} \frac{1}{h} = +\infty$.
The signs are strictly determined by the sign of the displacement $h$.

**Pass 2 — Numerical check:**
- Left-hand evaluations:

$$
  f(1.9) = \frac{1}{1.9-2} = -10
$$

$$
  f(1.99) = \frac{1}{1.99-2} = -100
$$

$$
  f(1.999) = \frac{1}{1.999-2} = -1000 \to -\infty
$$

- Right-hand evaluations:

$$
  f(2.1) = \frac{1}{2.1-2} = +10
$$

$$
  f(2.01) = \frac{1}{2.01-2} = +100
$$

$$
  f(2.001) = \frac{1}{2.001-2} = +1000 \to +\infty
$$

**Pass 3 — Consistency check:** The denominator $g(x) = x - 2$ has a simple root (multiplicity 1) at $x = 2$. At any simple pole, a rational function must change sign across the asymptote, guaranteeing that the two one-sided limits have opposite signs.

---

## Exam tip

When evaluating $\frac{1}{0}$, always determine whether the zero in the denominator is approached through positive values ($0^+$) or negative values ($0^-$) to decide between $+\infty$ and $-\infty$.

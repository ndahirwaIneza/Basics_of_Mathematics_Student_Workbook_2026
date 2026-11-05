# Exercise 13

**Problem:** For
$$f(x)=e^{\sin(x^2)}$$
compute the derivative. First write the layers
$$x\longrightarrow x^2\longrightarrow \sin(x^2)\longrightarrow e^{\sin(x^2)}$$
and explain why differentiation moves through them in the reverse order.

---

## Relevant theorem / definition

The chain rule generalizes to a three-layer composition $f(x) = w(v(u(x)))$ as:
$$
\frac{df}{dx} = \frac{dw}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx}
$$
Standard elementary derivatives are $\frac{d}{dv}(e^v) = e^v$, $\frac{d}{du}(\sin u) = \cos u$, and $\frac{d}{dx}(x^2) = 2x$.

---

## Solution

1. Write the functional layers:
   The forward evaluation of $f(x)$ proceeds from inside to outside through three successive transformations:
   $$
   x \xrightarrow{\quad u = x^2 \quad} x^2 \xrightarrow{\quad v = \sin u \quad} \sin(x^2) \xrightarrow{\quad w = e^v \quad} e^{\sin(x^2)}
   $$
   - Layer 1 (innermost): $u(x) = x^2$
   - Layer 2 (middle): $v(u) = \sin u$
   - Layer 3 (outermost): $w(v) = e^v$

2. Explain why differentiation moves through them in reverse order:
   Evaluating the function requires moving from the inside out: one must first compute $x^2$, then apply $\sin$, and finally exponentiate.
   In contrast, differentiation measures how the final output $w$ responds to small variations in the initial input $x$. By the chain rule:
   $$
   \frac{df}{dx} = \frac{dw}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx}
   $$
   The outermost function $w$ can only be differentiated with respect to its immediate variable $v$. That rate of change is then modulated by how $v$ responds to $u$ ($\frac{dv}{du}$), which is in turn modulated by how $u$ responds to $x$ ($\frac{du}{dx}$). Thus, differentiation systematically unrolls the composite dependencies from the outside inward—the exact reverse of the evaluation order.

3. Differentiate each layer in reverse order:
   - Outermost layer:
     $$
     \frac{dw}{dv} = \frac{d}{dv}(e^v) = e^v = e^{\sin(x^2)}
     $$
   - Middle layer:
     $$
     \frac{dv}{du} = \frac{d}{du}(\sin u) = \cos u = \cos(x^2)
     $$
   - Innermost layer:
     $$
     \frac{du}{dx} = \frac{d}{dx}(x^2) = 2x
     $$

4. Multiply the layer derivatives:
   \begin{align}
   f'(x) &= \frac{dw}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx} \\
   &= e^{\sin(x^2)} \cdot \cos(x^2) \cdot 2x \\
   &= 2x \cos(x^2) e^{\sin(x^2)}.
   \end{align}

---

## Result

$$
\text{Layers: } x \xrightarrow{\quad u = x^2 \quad} x^2 \xrightarrow{\quad v = \sin u \quad} \sin(x^2) \xrightarrow{\quad w = e^v \quad} e^{\sin(x^2)}
$$

$$
f'(x) = 2x \cos(x^2) e^{\sin(x^2)}
$$

$$
\text{Reverse order reason: By the chain rule } \frac{df}{dx} = \frac{dw}{dv}\frac{dv}{du}\frac{du}{dx}, \text{ sensitivity unrolls backwards from the outermost wrapper to the inner core.}
$$

---

## Verification

**Pass 1 — Algebraic check:** Differentiate via logarithmic differentiation:
$$
\ln f(x) = \sin(x^2)
$$
Differentiating both sides using the chain rule on $\sin(x^2)$:
$$
\frac{f'(x)}{f(x)} = \cos(x^2) \cdot 2x = 2x\cos(x^2)
$$
Multiply through by $f(x) = e^{\sin(x^2)}$:
$$
f'(x) = 2x \cos(x^2) e^{\sin(x^2)}
$$
This independently confirms the derivative.

**Pass 2 — Numerical check:** Evaluate at $x = 0$:
$$
f(0) = e^{\sin(0)} = e^0 = 1, \quad f'(0) = 2(0)\cos(0)e^0 = 0
$$
Evaluate forward difference quotient with $h = 0.01$:
$f(0.01) = e^{\sin((0.01)^2)} = e^{\sin(0.0001)} \approx e^{0.0001000} \approx 1.0001000$.
$$
\frac{f(0.01) - f(0)}{0.01} = \frac{1.0001000 - 1}{0.01} = 0.0100 \to 0 \text{ as } h \to 0
$$

**Pass 3 — Consistency check:** The function $f(x) = e^{\sin(x^2)}$ is even since $(-x)^2 = x^2$. The derivative of an even function must be odd. Evaluating:
$$
f'(-x) = 2(-x)\cos((-x)^2)e^{\sin((-x)^2)} = -2x\cos(x^2)e^{\sin(x^2)} = -f'(x)
$$
Because $f'(x)$ is odd, $f'(0)$ must equal $0$, and the signs of $f'(x)$ are symmetric and opposite across the origin, confirming structural parity consistency.

---

## Exam tip

Differentiate outer wrappers first while keeping their inner arguments completely unchanged, then multiply by the inner derivatives step-by-step.

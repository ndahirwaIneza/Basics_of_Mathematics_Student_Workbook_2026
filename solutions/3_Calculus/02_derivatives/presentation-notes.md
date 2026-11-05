# Presentation Notes — Derivatives

## Topic summary

Derivatives quantify the instantaneous rate of change of a function and define the geometric slope of its tangent line. Computing derivatives systematically relies on fundamental building blocks—powers, exponentials, logarithms, and trigonometric functions—combined through linearity, the product rule, the quotient rule, and the chain rule. Beyond mechanical manipulation, calculus demands tracking domain restrictions, interpreting the sign of the derivative in terms of monotonicity and extrema, peeling back multi-layer composite functions from outside inward, and recognizing why continuity is a necessary but strictly weaker condition than differentiability.

---

## Exercise 1 — verbal script

**Key idea:** Applying the power rule term-by-term to a polynomial and interpreting derivative values as tangent slopes.

**What to say:**
We differentiate the polynomial term-by-term using the power rule, multiplying each coefficient by the old exponent and reducing the power by one. The constant term $-4$ vanishes because the rate of change of a constant is zero, giving the derivative $f'(x) = 15x^4 - 6x^2 + 7$. Evaluating at $x = 0$ gives $f'(0) = 7$, and at $x = 1$ gives $f'(1) = 16$. Both values are strictly positive, which tells us that the tangent lines at these points slant upward from left to right. Specifically, the tangent line at $x = 1$ has slope $16$, making it substantially steeper than the tangent line at $x = 0$ which has slope $7$. This positive sign confirms that the function is strictly increasing in the neighborhood of both points.

**Show on screen:** The term-by-term differentiation steps, the evaluations $f'(0) = 7$ and $f'(1) = 16$, and the conclusion about tangent slants.

**If asked to go deeper:** Completing the square on $f'(x)$ shows that $f'(x) = 15(x^2 - 1/5)^2 + 6.4 \ge 6.4 > 0$ for all real $x$, meaning the polynomial is strictly increasing on its entire domain $\mathbb{R}$.

---

## Exercise 2 — verbal script

**Key idea:** Rewriting radicals and fractions as fractional and negative powers before differentiating, followed by domain tracking.

**What to say:**
Before differentiating, we express all terms in standard power form: $2\sqrt{x}$ becomes $2x^{1/2}$, $-3/x^2$ becomes $-3x^{-2}$, and $x^{3/2}$ is already a power. For the domain of $f$, the roots require $x \ge 0$ while the denominator prohibits $x = 0$, giving $D_f = (0, \infty)$. Applying the power rule to each term yields $x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2}$, where subtracting 1 from $-2$ produces exponent $-3$. Rewriting this derivative in radical and fractional form gives $\frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}$. Inspecting the terms of the derivative, $\sqrt{x}$ in the denominator requires $x > 0$ and $x^3$ requires $x \neq 0$, so $D_{f'} = (0, \infty)$. The domain of the derivative matches the domain of the function exactly; while square root derivatives typically lose the boundary point $x = 0$, here zero was already excluded from the original domain by the inverse-square term.

**Show on screen:** The rewritten power form, the domain intersection leading to $(0, \infty)$, the derivative calculation, and the domain comparison $D_f = D_{f'} = (0, \infty)$.

**If asked to go deeper:** Because every term in $f'(x)$ is strictly positive for all $x \in (0, \infty)$, the function is strictly increasing across its entire domain without any local extrema.

---

## Exercise 3 — verbal script

**Key idea:** Demonstrating the product rule and identifying the missing term in the common erroneous formula $(uv)' = u'v$.

**What to say:**
We identify the function as a product of $u(x) = x^2 + 1$ and $v(x) = e^x$. By the product rule, the derivative of a product is $u'v + uv'$, giving $(2x)e^x + (x^2 + 1)e^x$. Factoring out $e^x$ yields $(x^2 + 2x + 1)e^x$, which factors neatly into $(x+1)^2 e^x$. If someone mistakenly writes $f'(x) = (2x)e^x$, they have differentiated only the polynomial factor while ignoring the fact that the exponential factor also changes with $x$. The missing term is $u(x)v'(x) = (x^2+1)e^x$. Geometrically, if you expand the dimensions of a rectangle with sides $u$ and $v$, the area increases by both $u'v\,\Delta x$ and $uv'\,\Delta x$; dropping the second term ignores the rate at which the second side expands.

**Show on screen:** The correct product rule expansion, the factored result $(x+1)^2 e^x$, and the highlighted missing term $(x^2+1)e^x$.

**If asked to go deeper:** Setting $f'(x) = (x+1)^2 e^x = 0$ reveals a single critical point at $x = -1$, where the derivative touches zero without changing sign, creating a horizontal inflection point rather than a local extremum.

---

## Exercise 4 — verbal script

**Key idea:** Applying the quotient rule to a rational function and explaining why the vertical asymptote must remain excluded from the derivative.

**What to say:**
We first establish the domain of $f(x) = \frac{x^2+1}{x-1}$: the denominator cannot vanish, so $x \neq 1$, giving $D_f = \mathbb{R} \setminus \{1\}$. To differentiate, we use the quotient rule: low times derivative of high minus high times derivative of low, over low squared. This gives $\frac{(2x)(x-1) - (x^2+1)(1)}{(x-1)^2}$. Expanding the numerator produces $2x^2 - 2x - x^2 - 1$, which simplifies to $x^2 - 2x - 1$. Writing $x^2 - 2x - 1$ as $(x-1)^2 - 2$ gives the alternative form $1 - \frac{2}{(x-1)^2}$. The condition $x \neq 1$ remains essential because the original curve has a vertical asymptote at $x = 1$; a function cannot possess a tangent slope where the graph itself is undefined. The derivative's denominator also vanishes at $x = 1$, ensuring $D_{f'} = \mathbb{R} \setminus \{1\}$.

**Show on screen:** The quotient rule setup, the algebraic expansion of the numerator, the simplified forms, and the explicit domain statements.

**If asked to go deeper:** As $x \to \pm\infty$, the term $\frac{2}{(x-1)^2}$ approaches zero, meaning $f'(x) \to 1$, which directly proves that the graph approaches an oblique asymptote of slope 1.

---

## Exercise 5 — verbal script

**Key idea:** Decomposing a composite power into inner and outer layers and tracing the origin of the inner derivative factor in the chain rule.

**What to say:**
We recognize $f(x) = (3x^2 - 2x + 1)^5$ as a composite function where the inner function is $u(x) = 3x^2 - 2x + 1$ and the outer function is $g(u) = u^5$. Differentiating the outer layer with respect to $u$ gives $5u^4$, and differentiating the inner layer with respect to $x$ gives $6x - 2$. By the chain rule, $f'(x) = g'(u) \cdot u'(x)$, which yields $5(3x^2 - 2x + 1)^4(6x - 2)$, or $10(3x - 1)(3x^2 - 2x + 1)^4$. The additional factor $(6x - 2)$ appears because the outer function scales rates of change relative to $u$, but $u$ is itself moving with respect to $x$. A small change $\Delta x$ shifts $u$ by approximately $(6x - 2)\Delta x$, which then gets amplified by $5u^4$. Without the inner factor, we would be computing $\frac{df}{du}$ instead of the desired rate $\frac{df}{dx}$.

**Show on screen:** The identification of $u(x)$ and $g(u)$, their separate derivatives, the chain rule product, and the explanation of the chain differential $\frac{df}{dx} = \frac{df}{du}\frac{du}{dx}$.

**If asked to go deeper:** The quadratic $3x^2 - 2x + 1$ has a negative discriminant, so it is strictly positive everywhere; therefore, $f'(x)$ changes sign solely at $x = 1/3$, giving a global minimum at that point.

---

## Exercise 6 — verbal script

**Key idea:** Combining the product rule with trigonometric derivatives and recognizing that a zero derivative produces a horizontal tangent line.

**What to say:**
The function has two terms: $x\sin x$ and $\cos x$. Differentiating the first term requires the product rule: derivative of $x$ is 1 times $\sin x$, plus $x$ times the derivative of $\sin x$, which is $\cos x$, giving $\sin x + x\cos x$. The derivative of the second term $\cos x$ is $-\sin x$. Adding them together gives $\sin x + x\cos x - \sin x$. The $\sin x$ terms cancel out completely, leaving the compact derivative $f'(x) = x\cos x$. Evaluating at $x = 0$ yields $f'(0) = 0 \cdot \cos(0) = 0$. A derivative of zero means the slope of the tangent line is zero. Therefore, at the point $(0, 1)$, the tangent line is perfectly horizontal, with the equation $y = 1$.

**Show on screen:** The product rule expansion, the cancellation of $\sin x - \sin x$, the final derivative $x\cos x$, and the horizontal tangent equation $y = 1$.

**If asked to go deeper:** Because $f(x)$ is an even function, its derivative is odd, which guarantees that $f'(0)$ must equal zero provided the derivative exists at the origin.

---

## Exercise 7 — verbal script

**Key idea:** Differentiating a composite trigonometric function using the chain rule and determining the sign of the derivative at the origin.

**What to say:**
For $f(x) = \sin(x^2 + 1)$, the outer function is $g(u) = \sin u$ and the inner function is $u(x) = x^2 + 1$. The derivative of the outer function with respect to $u$ is $\cos u$, and the derivative of the inner function with respect to $x$ is $2x$. Applying the chain rule gives $f'(x) = \cos(x^2 + 1) \cdot 2x = 2x\cos(x^2 + 1)$. To find $f'(0)$, we substitute $x = 0$: $2(0)\cos(1) = 0$. Because the value is exactly zero, it is neither positive nor negative. Geometrically, this means that the curve has a horizontal tangent at $(0, \sin 1)$.

**Show on screen:** The identification of inner and outer functions, their respective derivatives, the combined derivative $2x\cos(x^2+1)$, and the calculation $f'(0) = 0$.

**If asked to go deeper:** For small positive $x$, $2x > 0$ and $\cos(x^2+1) > 0$, making $f'(x) > 0$; for small negative $x$, $f'(x) < 0$. This sign change confirms that $(0, \sin 1)$ is a strict local minimum.

---

## Exercise 8 — verbal script

**Key idea:** Comparing the differentiation mechanisms for natural exponential functions with linear exponents versus general base exponentials.

**What to say:**
We differentiate the two exponential terms separately. For the first term $e^{2x-3}$, the natural exponential function differentiates to itself, but the exponent is an inner function $2x - 3$ whose derivative is $2$. By the chain rule, this produces $2e^{2x-3}$. For the second term $5^x$, the base is $5$ rather than $e$. We express $5^x$ as $e^{x\ln 5}$; differentiating by the chain rule brings down the constant factor $\ln 5$, giving $5^x\ln 5$. Combining the terms gives $f'(x) = 2e^{2x-3} + 5^x\ln 5$. The factor 2 arises from the internal derivative of the exponent, whereas the factor $\ln 5$ arises from the change-of-base scaling relative to the natural base $e$.

**Show on screen:** The separate differentiation of $e^{2x-3}$ and $5^x$, the final sum $2e^{2x-3} + 5^x\ln 5$, and the contrasting reasons for the factors $2$ and $\ln 5$.

**If asked to go deeper:** Both terms in the derivative are strictly positive for all real $x$, proving that $f(x)$ is strictly increasing across its entire domain $\mathbb{R}$.

---

## Exercise 9 — verbal script

**Key idea:** Differentiating a composite logarithmic function, analyzing derivative signs across intervals, and deducing local geometry.

**What to say:**
The argument $x^2 + 1$ is always greater than or equal to 1, so the logarithm is defined on all real numbers. Using the logarithmic chain rule $(\ln u)' = u'/u$, we differentiate the inner function $x^2 + 1$ to get $2x$, yielding $f'(x) = \frac{2x}{x^2 + 1}$. Since the denominator $x^2 + 1$ is strictly positive for all $x$, the sign of $f'(x)$ depends solely on the numerator $2x$. For $x < 0$, $f'(x) < 0$; for $x = 0$, $f'(0) = 0$; and for $x > 0$, $f'(x) > 0$. This sign behavior tells us that the function decreases strictly on $(-\infty, 0)$ and increases strictly on $(0, \infty)$. At $x = 0$, the derivative is zero and changes from negative to positive, which establishes a strict global minimum at $(0, 0)$. Near the origin, the graph is smooth and curves upward in a valley tangent to the $x$-axis.

**Show on screen:** The formula $f'(x) = \frac{2x}{x^2+1}$, the three-case sign breakdown, and the qualitative behavior summary around $(0,0)$.

**If asked to go deeper:** The second derivative is $f''(x) = \frac{2(1-x^2)}{(x^2+1)^2}$; at $x = 0$ we have $f''(0) = 2 > 0$, which confirms the local minimum via the second derivative test, with inflection points occurring at $x = \pm 1$.

---

## Exercise 10 — verbal script

**Key idea:** Constructing the tangent line equation from the derivative and verifying tangency through point-slope substitution.

**What to say:**
To find the tangent line to $f(x) = x^2 - 3x + 1$ at $x = 2$, we first compute the $y$-coordinate of tangency by evaluating $f(2) = 4 - 6 + 1 = -1$, giving the point $P(2, -1)$. Next, we differentiate to obtain the slope function $f'(x) = 2x - 3$. Evaluating at $x = 2$ gives $f'(2) = 2(2) - 3 = 1$, which is the slope $m$ of the tangent line. Using the point-slope form $y - y_0 = m(x - x_0)$, we substitute our values: $y - (-1) = 1(x - 2)$, which simplifies to $y = x - 3$. Finally, we verify that the point lies on the line: substituting $x = 2$ into $y = x - 3$ gives $y = -1$, exactly matching $f(2)$.

**Show on screen:** The computation of the point $(2, -1)$, the slope $f'(2) = 1$, the algebraic derivation of $y = x - 3$, and the substitution check.

**If asked to go deeper:** Equating the parabola and tangent line yields $x^2 - 3x + 1 = x - 3 \iff (x - 2)^2 = 0$; the double root at $x = 2$ algebraically characterizes the line as tangent rather than secant.

---

## Exercise 11 — verbal script

**Key idea:** Deriving the derivative of $x^2$ directly from the limit definition and identifying the algebraic removal of the indeterminate form.

**What to say:**
We start with the formal definition: $f'(x)$ is the limit as $h$ approaches zero of $\frac{f(x+h) - f(x)}{h}$. Substituting $f(x) = x^2$, the numerator becomes $(x+h)^2 - x^2$. Expanding $(x+h)^2$ gives $x^2 + 2xh + h^2$. The $x^2$ terms cancel out, leaving $2xh + h^2$. At this stage, substituting $h = 0$ would yield the undefined fraction $0/0$. Because $h$ approaches zero without equaling zero, we can factor out $h$ from the numerator and cancel it with the denominator, simplifying the difference quotient to $2x + h$. The limit is applied at this exact transition: taking $\lim_{h \to 0}(2x + h)$ lets $h$ go to zero, leaving $2x$. This matches the power rule formula $\frac{d}{dx}(x^2) = 2x^{2-1} = 2x$ completely.

**Show on screen:** The difference quotient setup, the expansion and cancellation of $x^2$, factoring out $h$, the simplified term $2x + h$, and the evaluation of the limit.

**If asked to go deeper:** Geometrically, $2xh$ represents the expansion along the two side strips of a square of area $x^2$, while $h^2$ represents the tiny corner square whose relative contribution vanishes in the limit.

---

## Exercise 12 — verbal script

**Key idea:** Formulating a multi-rule execution plan and organizing higher-order product and chain rule derivatives through common factoring.

**What to say:**
Before calculating, we establish a plan: the entire expression is a product of $(x^2+1)^3$ and $e^x$, so the primary rule is the product rule. Within the first factor, $(x^2+1)^3$ is a composite power, requiring the chain rule. Differentiating $(x^2+1)^3$ gives $3(x^2+1)^2 \cdot (2x) = 6x(x^2+1)^2$, while the derivative of $e^x$ is simply $e^x$. Substituting into the product rule gives $[6x(x^2+1)^2]e^x + [(x^2+1)^3]e^x$. Rather than expanding the brackets, which creates an unwieldy polynomial, we factor out the greatest common factors: $(x^2+1)^2$ and $e^x$. This leaves $(x^2+1)^2 e^x [6x + (x^2+1)]$, which simplifies cleanly to $(x^2+1)^2 (x^2 + 6x + 1) e^x$.

**Show on screen:** The stated plan (product rule outer, chain rule inner), the substitution into the product rule, and the common factor extraction leading to the final form.

**If asked to go deeper:** The factored form allows us to find the critical points instantly: $(x^2+1)^2$ and $e^x$ never vanish, so all stationary points come from solving the quadratic $x^2 + 6x + 1 = 0$, giving $x = -3 \pm 2\sqrt{2}$.

---

## Exercise 13 — verbal script

**Key idea:** Deconstructing a three-layer composite function into forward evaluation stages and applying the chain rule in reverse order.

**What to say:**
Evaluating $f(x) = e^{\sin(x^2)}$ proceeds from the inside out: we start with $x$, square it to get $x^2$, take the sine to get $\sin(x^2)$, and finally exponentiate to get $e^{\sin(x^2)}$. When computing the derivative, however, the chain rule moves through these layers in reverse order: $\frac{df}{dx} = \frac{dw}{dv}\frac{dv}{du}\frac{du}{dx}$. We differentiate the outermost exponential layer first with respect to its exponent, giving $e^{\sin(x^2)}$. Next, we multiply by the derivative of the middle sine layer, which is $\cos(x^2)$. Finally, we multiply by the derivative of the innermost core $x^2$, which is $2x$. Combining them gives $f'(x) = 2x\cos(x^2)e^{\sin(x^2)}$. The process is reversed because each layer's rate of change can only be measured relative to its immediate input before propagating the sensitivity back to $x$.

**Show on screen:** The forward layer chain diagram, the three-factor chain rule formula, and the combined derivative $2x\cos(x^2)e^{\sin(x^2)}$.

**If asked to go deeper:** Checking the parity of the function, $f(x)$ is even, so its derivative must be odd; substituting $-x$ into $f'(x)$ cleanly produces $-f'(x)$, validating the algebraic structure.

---

## Exercise 14 — verbal script

**Key idea:** Investigating continuity and differentiability of a piecewise function using one-sided limits and difference quotients.

**What to say:**
We analyze $f(x)$ at the junction point $x = 0$. For continuity, we compare the one-sided limits: from the right, $x^2 \to 0$; from the left, $ax \to 0$; and $f(0) = 0$. Because both limits match $f(0)$ regardless of $a$, the function is continuous at $x = 0$ for all real $a$. For differentiability, we must evaluate the one-sided derivatives using the definition. The right-hand derivative is the limit of $h^2/h$ as $h \to 0^+$, which is $0$. The left-hand derivative is the limit of $ah/h$ as $h \to 0^-$, which is $a$. These two one-sided derivatives exist for every $a$, but they agree if and only if $a = 0$. Thus, $f$ is differentiable at $x = 0$ exclusively when $a = 0$. This problem demonstrates that continuity is not sufficient for differentiability: continuity only ensures the two pieces meet without a break, whereas differentiability requires them to meet smoothly with matching directional slopes, preventing a sharp corner.

**Show on screen:** The continuity limit checks, the two one-sided difference quotient calculations $f'_+(0) = 0$ and $f'_-(0) = a$, the equality condition $a = 0$, and the geometric distinction between continuity and smoothness.

**If asked to go deeper:** When $a \neq 0$, the graph exhibits a corner point similar to the absolute value function $|x|$ at the origin, where no unique tangent line can be drawn.

---

## Exercise 15 — verbal script

**Key idea:** Demonstrating how difference quotients numerically approximate the derivative and contrasting empirical calculation with an analytical limit.

**What to say:**
We test the parabola $f(x) = x^2 - 3x + 1$ at $x_0 = 2$, where the exact derivative is $f'(2) = 1$. The difference quotient simplifies algebraically to $\frac{h + h^2}{h} = 1 + h$. Evaluating this secant slope for decreasing step sizes gives: for $h = 1$, the slope is $2.0$; for $h = 0.1$, it is $1.1$; and for $h = 0.01$, it is $1.01$. The difference between the secant slope and the exact derivative shrinks linearly with $h$: $1.0$, $0.1$, and $0.01$. This progressive convergence illustrates the definition of the derivative, showing secant lines rotating directly into the tangent line. However, a finite set of numerical calculations cannot replace a mathematical proof. Discrete calculations only test isolated positive steps; they cannot verify left-handed convergence, nor can they rule out pathological high-frequency oscillations that might occur on smaller intervals. An analytical limit guarantees convergence across all possible paths to zero.

**Show on screen:** The exact derivative $f'(2) = 1$, the algebraic form $1 + h$, the table of values for $h = 1, 0.1, 0.01$, and the conceptual explanation of why sampling does not replace a limit.

**If asked to go deeper:** The error in the secant slope is exactly $\frac{f''(2)}{2}h = h$, which directly connects the convergence rate of the difference quotient to the curvature of the graph via Taylor's theorem.

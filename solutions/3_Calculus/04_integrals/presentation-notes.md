# Presentation Notes — Integrals

## Topic summary

Integration connects two fundamental concepts in calculus: finding antiderivatives as the reverse of differentiation, and evaluating definite integrals as continuous accumulation and geometric area. Indefinite integration determines the complete infinite family of functions differing by an arbitrary constant, requiring foundational tools such as the power rule, linear substitution, and integration by parts. Definite integration calculates net signed accumulation over an interval, governed by the Fundamental Theorem of Calculus, which establishes that the instantaneous rate of area accumulation is precisely the height of the integrand. Mastery of integration depends on structurally recognizing which technique applies—reversing the chain rule through substitution or reversing the product rule through integration by parts—before carrying out computations.

---

## Exercise 1 — verbal script

**Key idea:** Integration as the inverse operation to differentiation and the geometric role of the constant of integration.

**What to say:**
We are asked to find an antiderivative of the quadratic polynomial $3x^2 - 4x + 5$, write its general family, verify by differentiation, and explain the constant $C$. Applying the power rule term by term, $3x^2$ integrates to $x^3$, $-4x$ integrates to $-2x^2$, and $5$ integrates to $5x$. Choosing $C=0$ gives one particular antiderivative, $x^3 - 2x^2 + 5x$. Adding an arbitrary real constant $C$ produces the full family of antiderivatives. When we differentiate this family, the derivative of $x^3$ is $3x^2$, the derivative of $-2x^2$ is $-4x$, the derivative of $5x$ is $5$, and the derivative of $C$ is zero, returning the original integrand. Geometrically, the constant $C$ represents a vertical shift of the graph, so the family forms an infinite stack of parallel curves that all share identical tangent slopes at every $x$.

**Show on screen:** The term-by-term integration leading to $x^3 - 2x^2 + 5x + C$, followed by the derivative verification matching $f(x)$.

**If asked to go deeper:** By the Mean Value Theorem, any two functions on an interval whose derivatives are everywhere equal must differ by a constant.

---

## Exercise 2 — verbal script

**Key idea:** Converting radical and reciprocal expressions into standard power forms and tracking the domain.

**What to say:**
Before integrating, we identify the domain of the expression. The square root requires $x \ge 0$, and the term $3/x^2$ requires $x \neq 0$, so the common domain of the integrand is the open half-line $(0, \infty)$. We then rewrite the terms as powers: $2x^{1/2} + 3x^{-2} - x^{1/3}$. Applying the power rule to each term increases each exponent by one and divides by the new exponent. This gives $\frac{4}{3}x^{3/2}$ for the first term, $-3x^{-1}$ or $-3/x$ for the second, and $-\frac{3}{4}x^{4/3}$ for the third. We add $+ C$ for the general antiderivative on $(0, \infty)$. Differentiating this result reproduces each original term, confirming that the algebra and exponent arithmetic are correct.

**Show on screen:** The power conversion $2x^{1/2} + 3x^{-2} - x^{1/3}$ and the resulting expression $\frac{4}{3}x^{3/2} - \frac{3}{x} - \frac{3}{4}x^{4/3} + C$.

**If asked to go deeper:** If the domain were extended to negative numbers for $x^{1/3}$ and $3/x^2$, the term $2\sqrt{x}$ would become complex, which is why restricting to $(0, \infty)$ is essential in real analysis.

---

## Exercise 3 — verbal script

**Key idea:** Direct integration using fundamental derivatives of exponential and trigonometric functions.

**What to say:**
We evaluate the integral by matching each term with its standard antiderivative. For $2e^x$, the exponential is its own derivative, so its antiderivative is $2e^x$. For $3\cos x$, the derivative of sine is cosine, giving $3\sin x$. For $-4\sin x$, we must be careful with the negative sign: because the derivative of cosine is negative sine, the antiderivative of $-4\sin x$ is $+4\cos x$. Putting these together and adding $+ C$ gives $2e^x + 3\sin x + 4\cos x + C$. Differentiating the entire expression in one step yields $2e^x + 3\cos x + 4(-\sin x) + 0$, which immediately matches the given integrand.

**Show on screen:** The term-by-term matching with known derivatives and the one-step verification showing the sign change on the cosine term.

**If asked to go deeper:** Because the exponential and trigonometric functions are entire functions, this antiderivative is smooth and valid across the entire real number line.

---

## Exercise 4 — verbal script

**Key idea:** Recognizing substitution as reversing the chain rule on a composite power function.

**What to say:**
In this integral, we observe a composite expression $(x^2+1)^4$ multiplied by $2x$. We choose the inner function $u = x^2 + 1$ as our substitution variable. Differentiating gives $du = 2x\,dx$, which matches the outside factor in the integrand. Substituting $u$ and $du$ transforms the problem into $\int u^4\,du$, which is a basic power integral. Evaluating it gives $\frac{1}{5}u^5 + C$. Back-substituting $x^2 + 1$ for $u$, we obtain $\frac{1}{5}(x^2+1)^5 + C$. To verify, we differentiate using the chain rule: bringing down the power 5 cancels the $1/5$, leaves $(x^2+1)^4$, and multiplying by the inner derivative $2x$ returns $2x(x^2+1)^4$.

**Show on screen:** The substitution assignment $u = x^2 + 1$, the differential $du = 2x\,dx$, and the simplified integral $\int u^4\,du$.

**If asked to go deeper:** Expanding $(x^2+1)^4$ first would also yield the correct answer, but substitution avoids polynomial expansion of high degrees and generalizes to non-integer powers.

---

## Exercise 5 — verbal script

**Key idea:** Recognizing that the substitution mechanism depends on structural relationship rather than the type of function.

**What to say:**
We compare this integral with Problem 4 to understand the structural pattern of substitution. In Problem 4, the inner quadratic $x^2+1$ appeared inside a power, whereas here $x^2$ appears in the exponent of $e$. In both cases, however, the integrand features a composite function whose inner argument is quadratic, multiplied by an outer factor proportional to $x\,dx$. Setting $u = x^2$ yields $du = 2x\,dx$, so $x\,dx = \frac{1}{2}du$. The integral becomes $\frac{1}{2}\int e^u\,du$, which integrates simply to $\frac{1}{2}e^u + C$. Back-substituting gives $\frac{1}{2}e^{x^2} + C$. Differentiating using the chain rule confirms that $\frac{1}{2}e^{x^2} \cdot 2x = xe^{x^2}$.

**Show on screen:** The side-by-side structural comparison highlighting the inner quadratic derivative in both Problem 4 and Problem 5.

**If asked to go deeper:** Any integral of the form $\int x f(x^2)\,dx$ reduces via $u = x^2$ to $\frac{1}{2}\int f(u)\,du$, regardless of whether $f$ is a power, exponential, or trigonometric function.

---

## Exercise 6 — verbal script

**Key idea:** Recognizing the structure of the derivative over the function and explaining why logarithms appear.

**What to say:**
When inspecting the rational function $2x / (x^2+5)$, we see that the denominator is $x^2 + 5$. Differentiating the denominator gives $2x$, which matches the numerator. Setting $u = x^2 + 5$ and $du = 2x\,dx$, the integral becomes $\int \frac{1}{u}\,du$. This evaluates to $\ln|u| + C$, which gives $\ln(x^2+5) + C$, dropping the absolute value since $x^2 + 5 > 0$. The logarithm appears because the power rule for integration fails at exponent $-1$, where division by zero would occur. The natural logarithm is the unique antiderivative of $u^{-1}$ on $(0, \infty)$, making any integrand of the form $g'(x)/g(x)$ inherently logarithmic.

**Show on screen:** The substitution $u = x^2+5$, the transformation to $\int \frac{1}{u}\,du$, and the final expression $\ln(x^2+5) + C$.

**If asked to go deeper:** The formula $\int \frac{g'(x)}{g(x)}\,dx = \ln|g(x)| + C$ is the logarithmic derivative rule in reverse, which is widely applied in solving first-order linear differential equations.

---

## Exercise 7 — verbal script

**Key idea:** Integration by parts as the inverse of the product rule for differentiation.

**What to say:**
Integration by parts originates from the product rule: the derivative of $uv$ is $u'v + uv'$. Integrating both sides and rearranging yields $\int u\,dv = uv - \int v\,du$. For the integral of $xe^x$, we choose $u = x$ and $dv = e^x\,dx$. Differentiating $u$ gives $du = dx$, reducing the polynomial to a constant, while integrating $dv$ yields $v = e^x$. Applying the formula gives $x e^x - \int e^x\,dx = xe^x - e^x + C$, which factors as $(x-1)e^x + C$. Differentiating by the product rule, the derivative of $x-1$ is 1 times $e^x$, plus $(x-1)e^x$, which simplifies to $e^x + xe^x - e^x = xe^x$, verifying our solution.

**Show on screen:** The derivation of the parts formula from the product rule and the factorization $(x-1)e^x + C$.

**If asked to go deeper:** Repeated integration by parts allows evaluating $\int x^n e^x\,dx$ through a reduction formula where each step decreases the power of $x$ by 1.

---

## Exercise 8 — verbal script

**Key idea:** Strategic choice of factors in integration by parts to ensure simplification of the subsequent integral.

**What to say:**
Before computing $\int x\cos x\,dx$, we must justify which factor to differentiate. If we chose $u = \cos x$ and $dv = x\,dx$, differentiating gives $-\sin x$ and integrating gives $x^2 / 2$, which creates an integral with $x^2\sin x$, making the problem harder. Instead, choosing $u = x$ and $dv = \cos x\,dx$ differentiates $x$ to $dx$, eliminating the algebraic variable, while $\cos x$ integrates to $\sin x$. The formula gives $x\sin x - \int \sin x\,dx$. Since the integral of $\sin x$ is $-\cos x$, the two negative signs cancel, yielding $x\sin x + \cos x + C$. Differentiating by the product rule confirms that $\sin x + x\cos x - \sin x = x\cos x$.

**Show on screen:** The comparison between the two assignment choices and the step showing the double negative $- (-\cos x) = +\cos x$.

**If asked to go deeper:** The LIATE rule provides a standard heuristic for selecting $u$, where Algebraic terms precede Trigonometric terms.

---

## Exercise 9 — verbal script

**Key idea:** Distinguishing between the definite integral as net signed accumulation and total geometric area.

**What to say:**
We evaluate $\int_{-1}^2 x\,dx$ using the Fundamental Theorem of Calculus: the antiderivative is $x^2/2$, giving $[x^2/2]_{-1}^2 = 4/2 - 1/2 = 3/2$. To understand this geometrically, we split the interval at the zero $x = 0$. On $[-1, 0]$, the function is below the $x$-axis, forming a triangle with base 1 and height 1, whose area is $1/2$. On $[0, 2]$, the function is above the axis, forming a triangle with base 2 and height 2, whose area is 2. The definite integral measures signed area, so the negative part cancels from the positive part: $2 - 1/2 = 3/2$. In contrast, total geometric area is strictly additive and non-negative, giving $2 + 1/2 = 5/2$.

**Show on screen:** The graph of $y=x$ on $[-1, 2]$ highlighting the lower triangle of area $1/2$, the upper triangle of area $2$, and the comparison $3/2$ vs $5/2$.

**If asked to go deeper:** In physical applications like displacement vs total distance traveled, the definite integral gives net displacement, whereas the integral of the absolute value gives total distance.

---

## Exercise 10 — verbal script

**Key idea:** Establishing a priori bounds for a definite integral to verify computations and catch errors.

**What to say:**
Before calculating, we bound the integral of $x^2 + 1$ on $[0, 2]$. Since the integrand is strictly increasing from $f(0) = 1$ to $f(2) = 5$, the minimum is 1 and the maximum is 5. Multiplying by the interval length 2 gives the rigorous estimate $2 \le \int_0^2(x^2+1)\,dx \le 10$. Computing the exact integral using antiderivative $x^3/3 + x$ gives $[8/3 + 2] - 0 = 14/3$, which is approximately $4.67$. This value lies safely within our estimated range of $2$ to $10$. This type of sanity check is invaluable in exams because it immediately detects sign errors from reversed limits, power integration mistakes like omitting the denominator, and large arithmetic slips.

**Show on screen:** The bounding inequality $1(2-0) \le I \le 5(2-0)$, followed by the exact computation $[x^3/3+x]_0^2 = 14/3$.

**If asked to go deeper:** The Mean Value Theorem for Integrals guarantees that there exists a point $c \in [0, 2]$ where $f(c) = (14/3) / 2 = 7/3$, which solves to $c = \sqrt{4/3} \approx 1.15 \in [0, 2]$.

---

## Exercise 11 — verbal script

**Key idea:** Structural classification of integrands to select the optimal integration technique.

**What to say:**
This problem tests our ability to choose the right technique based on structure. For $\sin(3x)$, the argument is linear, so we use linear substitution with $u = 3x$, introducing a factor of $1/3$ to get $-\frac{1}{3}\cos(3x) + C$. For $x\ln x$, we have a product involving a logarithm, so we choose integration by parts with $u = \ln x$ and $dv = x\,dx$; differentiating $\ln x$ removes the transcendental term, yielding $\frac{x^2}{2}\ln x - \frac{x^2}{4} + C$. For $x / \sqrt{x^2+1}$, the composite root has an inner quadratic whose derivative $2x$ matches the numerator up to a constant; substituting $u = x^2+1$ reduces it to $\frac{1}{2}\int u^{-1/2}\,du$, which evaluates to $\sqrt{x^2+1} + C$. Differentiating each result confirms our solutions.

**Show on screen:** The three integrands side by side with their corresponding method labels: linear substitution, integration by parts, and power-chain substitution.

**If asked to go deeper:** For $x\ln x$, choosing $u=x$ instead would lead to an unknown antiderivative of $\ln x$, which is why the logarithmic term must always be chosen as $u$.

---

## Exercise 12 — verbal script

**Key idea:** Using symmetry of odd and even functions over symmetric intervals to simplify definite integrals.

**What to say:**
We compare the integrals of $x$ and $|x|$ on $[-2, 2]$. The function $f(x) = x$ is odd because $f(-x) = -f(x)$. Over the symmetric interval $[-2, 2]$, the area below the axis on $[-2, 0]$ exactly cancels the area above the axis on $[0, 2]$, so we predict the integral is zero. Calculating with antiderivative $x^2/2$ confirms $[2 - 2] = 0$. In contrast, $g(x) = |x|$ is even because $|-x| = |x|$. Both triangular halves are positive, so we predict the integral is double the integral from $0$ to $2$, which is $2 \times 2 = 4$. Calculating by splitting at zero gives $2 + 2 = 4$. This demonstrates how the absolute value eliminates cancellation by reflecting negative areas into positive ones.

**Show on screen:** Sketches of $y = x$ and $y = |x|$ on $[-2, 2]$ illustrating point symmetry vs axis symmetry.

**If asked to go deeper:** The integral of any product of an odd and an even function over a symmetric interval is always zero because their product is odd.

---

## Exercise 13 — verbal script

**Key idea:** Fundamental Theorem of Calculus Part 1 and interpreting integrand height as the local rate of area accumulation.

**What to say:**
We evaluate the accumulation function $F(x) = \int_0^x (t^2+1)\,dt$. Integrating gives $F(x) = [t^3/3 + t]_0^x = \frac{1}{3}x^3 + x$. Differentiating this with respect to $x$ yields $F'(x) = x^2 + 1$, which is identically equal to the integrand evaluated at $x$. The geometric reason is intuitive: when the right boundary advances by a small width $\Delta x$, the new area added is a thin vertical strip of width $\Delta x$ and height $f(x)$. Dividing the change in area $\Delta F \approx f(x)\Delta x$ by $\Delta x$ gives the average rate of area growth. Taking the limit as $\Delta x \to 0$ proves that the instantaneous rate of area accumulation is exactly the height of the curve.

**Show on screen:** The derivation of $F(x) = \frac{1}{3}x^3 + x$, its derivative $F'(x) = x^2 + 1$, and a diagram showing the strip of area $\Delta F \approx f(x)\Delta x$.

**If asked to go deeper:** If the upper limit were a function $g(x)$, Leibniz's rule applies via the chain rule: $\frac{d}{dx}\int_0^{g(x)} f(t)\,dt = f(g(x))g'(x)$.

---

## Exercise 14 — verbal script

**Key idea:** Integrating piecewise continuous functions by partitioning the integration domain at rule boundaries.

**What to say:**
The function is defined piecewise: $x+1$ on $[-1, 1)$ and constant $2$ on $[1, 3]$. We check continuity at the boundary $x = 1$: the left limit is $1+1 = 2$, which matches the right value 2, so the function is continuous. We split the definite integral at $x = 1$ into $\int_{-1}^1 (x+1)\,dx + \int_1^3 2\,dx$. The first integral evaluates to $[x^2/2 + x]_{-1}^1 = 2$. The second integral evaluates to $[2x]_1^3 = 6 - 2 = 4$. Adding these gives 6. Geometrically, the region under the curve on $[-1, 1]$ is a triangle with base 2 and height 2, having area $1/2 \times 2 \times 2 = 2$, while on $[1, 3]$ it is a rectangle of width 2 and height 2, having area 4. The geometric sum $2 + 4 = 6$ perfectly confirms our analytic result.

**Show on screen:** The piecewise graph showing the triangle over $[-1, 1]$ and the adjacent rectangle over $[1, 3]$ summing to area 6.

**If asked to go deeper:** Even if the function had a jump discontinuity at $x = 1$, the definite integral would still exist and equal the sum of the two sub-integrals, because finite jump discontinuities do not affect integrability.

---

## Exercise 15 — verbal script

**Key idea:** Solving an initial value problem by combining substitution with initial condition evaluation.

**What to say:**
We are given $F'(x) = 2xe^{x^2}$ and the initial condition $F(0) = 3$. Recognizing the inner quadratic $x^2$ and its derivative $2x$, we use substitution with $u = x^2$ and $du = 2x\,dx$. The indefinite integral $\int e^u\,du$ gives the family of antiderivatives $F(x) = e^{x^2} + C$. To find the specific constant, we substitute $x = 0$: $F(0) = e^0 + C = 1 + C$. Setting $1 + C = 3$ gives $C = 2$, so the particular solution is $F(x) = e^{x^2} + 2$. We verify by differentiating: $\frac{d}{dx}(e^{x^2} + 2) = e^{x^2}(2x) = 2xe^{x^2}$, which satisfies the differential equation, and evaluating at $x = 0$ gives $e^0 + 2 = 3$, satisfying the initial condition.

**Show on screen:** The substitution steps leading to $e^{x^2} + C$, the calculation $1 + C = 3 \implies C = 2$, and the double verification.

**If asked to go deeper:** This can also be expressed directly as a definite integral $F(x) = F(0) + \int_0^x 2t e^{t^2}\,dt = 3 + (e^{x^2} - 1) = e^{x^2} + 2$, avoiding an intermediate arbitrary constant.

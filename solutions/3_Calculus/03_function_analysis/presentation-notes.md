# Presentation Notes — Function Analysis

## Topic summary

Function analysis synthesizes differential calculus, limit theory, and algebraic structures into an exact qualitative and quantitative portrait of a curve. By establishing the natural domain and intrinsic symmetries first, we define the valid geometric frame. The first derivative dictates monotonicity and pinpoints local extrema through critical sign changes, while the second derivative reveals concavity and inflection points where curvature reverses. Combining boundary limits with vertical, horizontal, and oblique asymptotes guarantees that the global asymptotic envelope is fully accounted for, enabling an accurate and mathematically sound reconstruction of the graph without blind plotting.

---

## Exercise 1 — verbal script

**Key idea:** Monotonicity and extrema of a cubic polynomial via the first derivative test.

**What to say:**
We begin by finding the domain, which is all real numbers since the function is a polynomial. Differentiating $x^3 - 3x^2 + 2$ gives $f'(x) = 3x^2 - 6x$, which factors conveniently into $3x(x - 2)$. Setting this to zero gives two critical points: $x = 0$ and $x = 2$. Looking at the sign of the derivative, $f'(x)$ is positive on $(-\infty, 0)$, negative on $(0, 2)$, and positive again on $(2, \infty)$. Therefore, the function increases up to $x = 0$, reaches a local maximum of $2$, decreases to $x = 2$, where it attains a local minimum of $-2$, and then increases toward infinity. We also note the inflection point at $(1, 0)$ where the second derivative $6(x-1)$ changes sign. On our sketch, we clearly mark the horizontal tangents at $(0, 2)$ and $(2, -2)$ alongside the inflection point.

**Show on screen:** The factored derivative $3x(x-2)$, the sign table, and the annotated sketch highlighting critical points $(0, 2)$ and $(2, -2)$.

**If asked to go deeper:** The inflection point $(1, 0)$ is the point of central symmetry for the cubic polynomial, meaning $f(1 + h) = -f(1 - h)$.

---

## Exercise 2 — verbal script

**Key idea:** Reconciling the calculus optimization condition with the algebraic vertex form.

**What to say:**
We approach finding the vertex of $x^2 - 4x + 1$ from two perspectives. First, using calculus, we differentiate to get $f'(x) = 2x - 4$. Setting this derivative to zero yields the unique critical point $x = 2$, and since the second derivative is $2$, which is strictly positive, this point is a global minimum with value $-3$. Second, using algebra, we complete the square to write the function in vertex form as $(x - 2)^2 - 3$. Because any real square is non-negative, the lowest possible value occurs when $(x - 2)^2 = 0$, which directly gives the vertex $(2, -3)$. Both methods arrive at the identical point because the vertex is the geometric point where the tangent is horizontal. Setting the derivative $2a(x - p)$ to zero is algebraically identical to minimizing the squared deviation $(x - p)^2$.

**Show on screen:** The side-by-side comparison between $f'(x) = 2x - 4 = 0$ and the completed square $(x - 2)^2 - 3$.

**If asked to go deeper:** The vertex formula $x = -b/(2a)$ is simply the general solution to $f'(x) = 2ax + b = 0$ for any quadratic function.

---

## Exercise 3 — verbal script

**Key idea:** Complete analysis of a homographic rational function including asymptotes and monotonicity.

**What to say:**
We analyze the rational function $f(x) = (x + 1)/(x - 2)$. The domain excludes $x = 2$, which gives a vertical asymptote where the left-hand limit is $-\infty$ and the right-hand limit is $+\infty$. Taking limits at infinity shows the horizontal asymptote is $y = 1$. The $x$-intercept is at $(-1, 0)$ and the $y$-intercept is at $(0, -1/2)$. Differentiating with the quotient rule gives $f'(x) = -3/(x - 2)^2$. Because the denominator is squared and the numerator is $-3$, the derivative is strictly negative everywhere on its domain. This means the function is strictly decreasing on $(-\infty, 2)$ and strictly decreasing on $(2, \infty)$, though never on their union. Combining these features allows us to sketch the two hyperbola branches accurately.

**Show on screen:** The quotient rule calculation showing $-3/(x-2)^2$, the asymptotic limits, and the sketch with dashed asymptote lines $x = 2$ and $y = 1$.

**If asked to go deeper:** Rewriting the function as $1 + 3/(x - 2)$ reveals it as a standard rectangular hyperbola $y = 3/x$ translated 2 units right and 1 unit up.

---

## Exercise 4 — verbal script

**Key idea:** Sign, vertical asymptotes, and domain-partitioned monotonicity for a rational function with two poles.

**What to say:**
The function $f(x) = 1/(x^2 - 1)$ has denominator zeros at $x = -1$ and $x = 1$, which split the domain into three open intervals. Computing one-sided limits at both poles shows that $x = -1$ and $x = 1$ are vertical asymptotes, while the limit as $x \to \pm\infty$ is $0$, giving a horizontal asymptote at $y = 0$. The sign is positive outside the poles and negative between them. Differentiating gives $f'(x) = -2x/(x^2 - 1)^2$, which is positive for $x < 0$ and negative for $x > 0$. This establishes that $f$ increases on $(-\infty, -1)$ and on $(-1, 0]$, reaches a local maximum at $(0, -1)$, and decreases on $[0, 1)$ and on $(1, \infty)$. We must analyze each interval separately because monotonicity is only valid on connected intervals; function values jump across vertical asymptotes, so rules cannot be applied across the disconnected domain.

**Show on screen:** The three-part interval sign chart and the demonstration of why $f(0.5) < f(2)$ despite negative derivative on each branch.

**If asked to go deeper:** The even symmetry $f(-x) = f(x)$ guarantees that the monotonicity and asymptotic behavior on the left-hand side mirror the right-hand side across the $y$-axis.

---

## Exercise 5 — verbal script

**Key idea:** Monotonicity, global maximum, and asymptotic leveling of an exponential decay product.

**What to say:**
We examine $f(x) = x e^{-x}$ on all real numbers. Differentiating using the product rule produces $f'(x) = (1 - x)e^{-x}$. Because $e^{-x}$ is strictly positive everywhere, the sign of the derivative depends entirely on $1 - x$. This gives a positive slope for $x < 1$ and a negative slope for $x > 1$, which proves that $x = 1$ is a strict global maximum with peak value $1/e$. For the asymptotic behavior as $x \to \infty$, we rewrite the expression as $x/e^x$ and apply L'Hôpital's rule to find the limit is $0$. This means the positive $x$-axis is a horizontal asymptote from above. On the graph, the curve climbs from $-\infty$, peaks at $(1, 1/e)$, and then descends toward zero. Crucially, to approach $y = 0$ asymptotically without crossing it, the curve must transition from concave down to concave up, which produces an inflection point at $x = 2$.

**Show on screen:** The factored derivative $(1-x)e^{-x}$, the L'Hôpital limit computation, and the inflection point at $(2, 2e^{-2})$.

**If asked to go deeper:** In probability theory, this function represents the probability density function of an Erlang-2 distribution, and in physics, it describes radioactive decay chains and wave packet envelopes.

---

## Exercise 6 — verbal script

**Key idea:** Role of domain determination and establishing global bounds via logarithmic analysis.

**What to say:**
We begin by emphasizing that any analysis involving $\ln x$ must start with the domain condition $x > 0$. Calculating without the domain risks evaluating non-existent points or formulating false limits. Differentiating $f(x) = \ln x - x + 1$ yields $f'(x) = 1/x - 1 = (1 - x)/x$. On the positive domain, the denominator is always positive, so $f'(x)$ is positive on $(0, 1)$ and negative on $(1, \infty)$. This makes $x = 1$ the unique global maximum with value $f(1) = 0$. Because the maximum value is zero and is attained strictly at $x = 1$, the function is strictly negative everywhere else on its domain. This immediately proves that $x = 1$ is the only zero of the function, while also rigorously establishing the standard inequality $\ln x \le x - 1$ for all positive $x$.

**Show on screen:** The derivative $(1-x)/x$, the deduction that $f(x) < 0$ for all $x \neq 1$, and the tangent-line inequality $\ln x \le x - 1$.

**If asked to go deeper:** The inequality $\ln x \le x - 1$ is the foundation for proving Gibbs' inequality in information theory and the arithmetic-geometric mean inequality.

---

## Exercise 7 — verbal script

**Key idea:** Finding global extrema and comparing boundary values on a closed bounded interval.

**What to say:**
For $f(x) = \sin x + \cos x$ restricted to $[0, 2\pi]$, we compute the derivative $f'(x) = \cos x - \sin x$. Setting this to zero requires $\sin x = \cos x$, which simplifies to $\tan x = 1$ on the open interval. This gives two critical points: $\pi/4$ and $5\pi/4$. Testing the sign of the derivative, $f'$ is positive on $[0, \pi/4]$, negative on $[\pi/4, 5\pi/4]$, and positive on $[5\pi/4, 2\pi]$. By the Extreme Value Theorem, we must compare the critical values with the endpoints $0$ and $2\pi$. The endpoints both evaluate to $1$, while $f(\pi/4) = \sqrt{2}$ and $f(5\pi/4) = -\sqrt{2}$. Since $-\sqrt{2} < 1 < \sqrt{2}$, the absolute maximum is $\sqrt{2}$ at $\pi/4$ and the absolute minimum is $-\sqrt{2}$ at $5\pi/4$. The endpoints act only as local boundary extrema, not global ones.

**Show on screen:** The four candidate evaluations ($x = 0, \pi/4, 5\pi/4, 2\pi$) and the harmonic transformation $\sqrt{2}\sin(x + \pi/4)$.

**If asked to go deeper:** Transforming $\sin x + \cos x$ into $\sqrt{2}\sin(x + \pi/4)$ using phase-amplitude form immediately confirms amplitude $\sqrt{2}$ without calculus.

---

## Exercise 8 — verbal script

**Key idea:** Concavity, inflection points, and extrema of a symmetric biquadratic polynomial.

**What to say:**
The function $f(x) = x^4 - 4x^2$ is an even polynomial, giving a symmetric W-shaped graph. Factoring the first derivative $f'(x) = 4x(x^2 - 2)$ reveals three critical points: $-\sqrt{2}$, $0$, and $\sqrt{2}$. The derivative changes from negative to positive at $\pm\sqrt{2}$, giving two symmetric global minima at height $-4$, and changes from positive to negative at $x = 0$, giving a local maximum of $0$. To analyze curvature, we take the second derivative $f''(x) = 12x^2 - 8$, which factors as $12(x^2 - 2/3)$. Setting $f''(x) = 0$ gives $x = \pm\sqrt{2/3}$. Because $f''$ changes sign across these roots, both points are genuine inflection points with value $-20/9$. The curve is concave down on $[-\sqrt{2/3}, \sqrt{2/3}]$ and concave up on the outer intervals.

**Show on screen:** The first and second derivatives, the summary table detailing sign combinations, and the annotated sketch showing the two minima, the peak, and the two inflection points.

**If asked to go deeper:** The function can be rewritten as $(x^2 - 2)^2 - 4$, which algebraically proves that the absolute minimum must be $-4$ and occurs when $x^2 = 2$.

---

## Exercise 9 — verbal script

**Key idea:** Identifying an oblique asymptote via polynomial division and remainder decay.

**What to say:**
We examine the rational function $f(x) = (x^2 + 1)/(x - 1)$. Because the numerator is degree 2 and the denominator is degree 1, an oblique asymptote is expected. Performing polynomial division gives $f(x) = x + 1 + 2/(x - 1)$. The line $x = 1$ is a vertical asymptote because the function blows up to $-\infty$ from the left and $+\infty$ from the right. For large $|x|$, the linear part $x + 1$ dominates, while the remainder term $2/(x - 1)$ has a constant numerator and an unbounded denominator, so it approaches zero. This difference converging to zero proves that $y = x + 1$ is the oblique asymptote in both directions. Furthermore, the sign of the remainder tells us the position of the curve: it stays above the asymptote for $x > 1$ and below it for $x < 1$.

**Show on screen:** The long division steps yielding $x + 1 + 2/(x - 1)$, the limit of the difference, and the dashed asymptote lines.

**If asked to go deeper:** The general limit method $m = \lim f(x)/x = 1$ and $b = \lim (f(x) - x) = 1$ confirms the exact same line without relying on polynomial division.

---

## Exercise 10 — verbal script

**Key idea:** Complete end-to-end function analysis of an odd rational function.

**What to say:**
We execute a complete, structured analysis for $f(x) = x/(x^2 + 1)$. The denominator never vanishes, so the domain is all real numbers. Evaluating $f(-x)$ yields $-f(x)$, proving odd symmetry about the origin. The only intercept is $(0, 0)$, and the limit at both infinities is zero, creating a horizontal asymptote $y = 0$. Computing the first derivative gives $(1 - x^2)/(x^2 + 1)^2$, with critical points at $-1$ and $+1$. This reveals a global minimum of $-1/2$ at $x = -1$ and a global maximum of $+1/2$ at $x = 1$. Next, the second derivative simplifies to $2x(x^2 - 3)/(x^2 + 1)^3$, which yields three inflection points: the origin $(0, 0)$ and symmetric points at $\pm\sqrt{3}$ with heights $\pm\sqrt{3}/4$. We synthesize this into a single summary table before sketching the smooth wave-like curve.

**Show on screen:** The complete multi-row summary table showing $x$, $f'$, $f''$, and the qualitative sketch with labeled extrema and inflection points.

**If asked to go deeper:** The global bounds $-1/2 \le f(x) \le 1/2$ can be verified directly from the algebraic inequality $(x \mp 1)^2 \ge 0$.

---

## Exercise 11 — verbal script

**Key idea:** Parameter-dependent bifurcation of critical points and qualitative graph structure.

**What to say:**
We study the family $f_a(x) = x^3 - 3ax$ by examining its derivative $f_a'(x) = 3(x^2 - a)$. The equation $x^2 = a$ governs the critical points and naturally splits into three cases. When $a < 0$, $x^2 = a$ has no real solutions; the derivative is strictly positive everywhere, so the function is strictly increasing with zero extrema. When $a = 0$, $f_0'(x) = 3x^2$ has a single zero at $x = 0$, but the derivative does not change sign, making the origin a stationary inflection point rather than an extremum. When $a > 0$, the derivative has two distinct roots $\pm\sqrt{a}$, producing a local maximum at $-\sqrt{a}$ with value $2a^{3/2}$ and a local minimum at $\sqrt{a}$ with value $-2a^{3/2}$. This qualitative restructuring illustrates a bifurcation: shifting the derivative parabola downward creates a region of negative slope that births a peak and a trough.

**Show on screen:** The three derivative parabolas for $a < 0$, $a = 0$, and $a > 0$ placed directly above their corresponding cubic curves.

**If asked to go deeper:** In dynamical systems, the normal form $\dot{x} = 3ax - x^3$ represents a supercritical pitchfork bifurcation where one stable equilibrium branches into two stable states and an unstable saddle.

---

## Exercise 12 — verbal script

**Key idea:** Geometric effect of the absolute value and origin of non-differentiable corner points.

**What to say:**
We start with the smooth parabola $g(x) = x^2 - 4$, which opens upward with roots at $\pm 2$ and vertex at $(0, -4)$. Applying the absolute value leaves the graph unchanged where $g(x) \ge 0$, but reflects the negative segment on $(-2, 2)$ upward across the $x$-axis. This flips the minimum $(0, -4)$ into a smooth local maximum at $(0, 4)$. Crucially, at the roots $x = \pm 2$, the derivative ceases to exist. Calculating one-sided limits at $x = 2$ shows the left slope is $-4$ while the right slope is $+4$. Because the left and right slopes disagree, the curve makes an abrupt angular turn. Geometrically, each zero is a sharp V-shaped corner where no unique tangent line can be drawn, making them singular critical points that act as global minima.

**Show on screen:** The superposition of the original parabola and the reflected absolute value graph, with the corners at $(\pm 2, 0)$ highlighted.

**If asked to go deeper:** At any point where a differentiable function $g$ crosses the axis with non-zero slope ($g(x_0) = 0, g'(x_0) \neq 0$), the absolute value $|g(x)|$ is guaranteed to have a non-differentiable corner with one-sided derivatives $\pm g'(x_0)$.

---

## Exercise 13 — verbal script

**Key idea:** Complete analysis of $(\ln x)/x$ and necessary geometric landmarks for sketching.

**What to say:**
We analyze $f(x) = (\ln x)/x$ on the domain $x > 0$. The zero occurs at $x = 1$. Computing the derivative with the quotient rule gives $(1 - \ln x)/x^2$, which vanishes only when $\ln x = 1$, or $x = e$. The derivative is positive for $x < e$ and negative for $x > e$, meaning $x = e$ is a strict global maximum with height $1/e \approx 0.368$. At the boundaries, the limit as $x \to 0^+$ is $-\infty$, creating a vertical asymptote at the $y$-axis, while the limit as $x \to \infty$ is $0$ by L'Hôpital's rule, creating a horizontal asymptote. To correctly sketch this curve, five pieces of information are indispensable: the domain restriction $x > 0$, the vertical plunge along $x = 0$, the zero crossing at $(1, 0)$, the horizontal tangent at the peak $(e, 1/e)$, and the inflection point at $x = e^{3/2}$, which allows the curve to switch to concave up and flatten asymptotically against $y = 0$.

**Show on screen:** The quotient rule derivative, the L'Hôpital limit, and the annotated sketch featuring the five critical landmarks.

**If asked to go deeper:** The fact that $x = e$ is the global maximum immediately proves that $e^\pi > \pi^e$, since $f(e) > f(\pi)$ implies $\ln(e)/e > \ln(\pi)/\pi$.

---

## Exercise 14 — verbal script

**Key idea:** Reconstructing monotonicity and cubic shape from a derivative, and comparing with an antiderivative.

**What to say:**
We are given the derivative $f'(x) = (x - 1)(x + 2)$ without the function itself. Because this is an upward-opening parabola with roots at $-2$ and $1$, the derivative is positive outside the roots and negative between them. This tells us $f$ is strictly increasing on $(-\infty, -2]$, strictly decreasing on $[-2, 1]$, and strictly increasing on $[1, \infty)$, with a local maximum at $x = -2$ and a local minimum at $x = 1$. The qualitative shape is an ascending cubic curve with undetermined vertical height. When we differentiate the specific polynomial $g(x) = x^3/3 + x^2/2 - 2x$, we obtain exactly $x^2 + x - 2$, verifying that $g$ is an exact antiderivative with constant $C = 0$. Evaluating $g$ pins down the vertical position: the local maximum is at $(-2, 10/3)$, the origin $(0, 0)$ lies on the descending branch, and the local minimum is at $(1, -7/6)$.

**Show on screen:** The sign chart of $f'(x)$, the qualitative cubic curve, and the exact graph of $g(x)$ with coordinates $(-2, 10/3)$ and $(1, -7/6)$.

**If asked to go deeper:** The net vertical descent $g(-2) - g(1) = 9/2 = 4.5$ equals the definite integral of $(x - 1)(x + 2)$ over $[-2, 1]$, linking the geometry of the curve directly to the area under the derivative.

---

## Exercise 15 — verbal script

**Key idea:** Diagnosing erroneous monotonicity claims and correcting quadratic sign charts.

**What to say:**
We examine a common error where a student concluded that $f'(x) = 3(x - 1)(x + 1)$ is positive between its zeros and negative outside them. We explain that merely finding the zeros does not determine the sign; one must examine the leading coefficient. Because the leading coefficient is $+3 > 0$, the derivative is a parabola that opens upward, meaning it is negative between $-1$ and $+1$ and positive outside them. The student inverted every single sign. As a result, the student called regions of increase decreasing, and misclassified the local maximum at $x = -1$ as a minimum and the local minimum at $x = 1$ as a maximum. Additionally, writing monotonicity on a union of disconnected sets is mathematically improper. To conclusively prove the correct signs, we evaluate test points: $f'(-2) = +9$, $f'(0) = -3$, and $f'(2) = +9$, confirming that $f$ increases, decreases, and increases.

**Show on screen:** The student's incorrect claim side-by-side with the correct upward-opening parabola and the three test point evaluations.

**If asked to go deeper:** A quick sanity check using end behavior shows that since $f(x) = x^3 - 3x$ tends to $+\infty$ as $x \to \infty$, decreasing throughout the entire tail $(1, \infty)$ would be incompatible with an infinite limit, refuting the student's assertion while the derivative sign $f'(x) = 3(x - 1)(x + 1) > 0$ proves the actual increase on $[1, \infty)$.

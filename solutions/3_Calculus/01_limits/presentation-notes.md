# Presentation Notes — Limits of Sequences and Functions

## Topic summary

Limits capture the asymptotic behavior of mathematical objects as their argument either grows without bound or approaches a specific point in the domain. The fundamental computational strategy revolves around identifying indeterminate forms—such as $\frac{\infty}{\infty}$, $\infty - \infty$, $\frac{0}{0}$, and $1^\infty$—and resolving them through targeted algebraic transformations including dominant power division, conjugate multiplication, polynomial factoring, and reduction to foundational limits like $\frac{\sin x}{x} \to 1$ and $(1 + 1/n)^n \to e$. By connecting sequence limits to function limits via Heine's criterion, one-sided limits to vertical asymptotes, and boundary matching to continuity, these exercises establish that limit evaluation is a unified deductive technique across discrete and continuous mathematics.

---

## Exercise 1 — verbal script

**Key idea:** Dividing numerator and denominator by the highest power of $n$ to isolate the ratio of leading coefficients.

**What to say:**
As $n$ approaches infinity, both the numerator and denominator grow without bound, creating the indeterminate form infinity over infinity. To resolve this, we divide every term in both numerator and denominator by the highest power present in the denominator, which is $n^2$. This transforms the fraction into $(4 - 3/n + 1/n^2)$ over $(2 + 5/n - 7/n^2)$. As $n$ grows, every term with $n$ or $n^2$ in the denominator tends to zero. This leaves four divided by two, which simplifies to 2. The highest-degree terms dominate because their quadratic growth completely outpaces the linear and constant terms, rendering lower-order terms negligible in the limit.

**Show on screen:** The fraction after dividing through by $n^2$, highlighting the vanishing terms $\frac{3}{n}, \frac{1}{n^2}, \frac{5}{n}, \frac{7}{n^2} \to 0$ and the final ratio $\frac{4}{2} = 2$.

**If asked to go deeper:** In asymptotic notation, the lower-order terms are $o(n^2)$, meaning their relative contribution $\frac{o(n^2)}{n^2}$ strictly vanishes as $n \to \infty$.

---

## Exercise 2 — verbal script

**Key idea:** Classifying asymptotic behavior by comparing the polynomial degrees of numerator and denominator.

**What to say:**
We evaluate two contrasting limits to see how relative polynomial degrees dictate the asymptotic outcome. In the first limit, the numerator has degree 1 and the denominator has degree 2. Dividing through by $n^2$ gives $(3/n + 1/n^2)$ over $(1 + 4/n^2)$, which approaches zero over one, or zero. In the second limit, the numerator has degree 3 and the denominator has degree 2. Dividing through by $n^2$ leaves $(2n - 1/n)$ over $(5 + 1/n^2)$, where the numerator continues to grow linearly without bound, driving the quotient to positive infinity. This establishes our general rule: when the denominator has higher degree the limit is zero, when degrees are equal the limit is the ratio of leading coefficients, and when the numerator has higher degree the sequence diverges to infinity.

**Show on screen:** The two limits side by side with the degree comparisons $1 < 2 \implies 0$ and $3 > 2 \implies +\infty$, followed by the three-branch degree classification rule.

**If asked to go deeper:** The growth rate of polynomials forms a strict hierarchy where the degree alone determines the asymptotic equivalence class of the sequence.

---

## Exercise 3 — verbal script

**Key idea:** Multiplying and dividing by the algebraic conjugate to eliminate the indeterminate form $\infty - \infty$.

**What to say:**
Direct evaluation yields infinity minus infinity, which is indeterminate because the dominant terms cancel each other out. To resolve this difficulty, we multiply and divide by the conjugate expression, the square root of $n^2+5n$ plus $n$. In the numerator, the difference of squares identity eliminates the radical, producing $(n^2+5n) - n^2$, which simplifies cleanly to $5n$. In the denominator, factoring $n$ out of the square root gives $n$ times the quantity square root of $1 + 5/n$ plus 1. Cancelling $n$ from numerator and denominator leaves 5 over the square root of $1 + 5/n$ plus 1. Taking the limit as $n$ goes to infinity gives 5 over $1 + 1$, which equals five halves, or 2.5.

**Show on screen:** The conjugate multiplication step showing $(n^2+5n) - n^2 = 5n$ in the numerator and the factored $n$ in the denominator.

**If asked to go deeper:** A generalized binomial expansion of $\sqrt{n^2+5n} = n + \frac{5}{2} - \frac{25}{8n} + \mathcal{O}(n^{-2})$ confirms that subtracting $n$ leaves $\frac{5}{2}$ as the constant leading term.

---

## Exercise 4 — verbal script

**Key idea:** Classifying sequences by geometric growth rates and using the squeeze theorem to handle damped oscillation.

**What to say:**
We analyze four sequences to distinguish between convergence, divergence, and oscillation. For $(2/3)^n$, the common ratio has absolute value strictly less than 1, so the sequence decays monotonically to zero. For $(3/2)^n$, the ratio exceeds 1, so the sequence grows exponentially without bound toward positive infinity. For $(-1)^n$, the terms alternate indefinitely between $-1$ and $+1$; its even subsequence approaches 1 while its odd subsequence approaches $-1$, so no limit exists. Finally, for $(-1)^n/n$, the sequence alternates in sign, but its amplitude is divided by $n$. Trapping the expression between $-1/n$ and $+1/n$, both of which approach zero, the squeeze theorem guarantees that the sequence converges to zero.

**Show on screen:** The four sequences grouped into decay to 0, divergence to $+\infty$, bounded divergence by oscillation, and damped oscillation trapped by the squeeze theorem.

**If asked to go deeper:** A sequence converges if and only if it satisfies the Cauchy criterion, which $(-1)^n$ fails because the distance between adjacent terms remains fixed at 2.

---

## Exercise 5 — verbal script

**Key idea:** Identifying the indeterminate form $1^\infty$ as the definition of Euler's number $e$ and distinguishing numerical trends from analytic proof.

**What to say:**
As $n$ approaches infinity, the base $1 + 1/n$ approaches 1 while the exponent $n$ tends to infinity, generating the indeterminate form $1^\infty$. By definition, this sequence converges to Euler's number $e$, approximately 2.71828. Calculating numerical values for $n = 1, 2, 5, 10, 100,$ and $1000$ shows terms steadily climbing from 2 up to approximately 2.7169. However, calculating a few terms never constitutes a mathematical proof. A finite sample cannot rule out that the sequence might change behavior at larger scales, nor can it verify the universal epsilon condition for all infinite indices. A complete proof requires showing that the sequence is strictly increasing and bounded above by 3, which guarantees convergence by the Monotone Convergence Theorem.

**Show on screen:** The table of computed values approaching 2.71828 alongside the binomial expansion showing term-by-term monotonicity and the upper bound of 3.

**If asked to go deeper:** Expanding $(1 + 1/n)^n$ via the binomial theorem expresses each term as a sum where every component increases monotonically with $n$, establishing convergence to the series $\sum_{k=0}^\infty \frac{1}{k!}$.

---

## Exercise 6 — verbal script

**Key idea:** Transferring dominant term techniques from sequences to continuous functions via Heine's sequential characterization.

**What to say:**
We evaluate the limit of a rational function as the continuous real variable $x$ approaches infinity. Just as in Exercise 1, this has the indeterminate form infinity over infinity. Dividing numerator and denominator by $x^2$ yields $(3 - 1/x + 1/x^2)$ over $(5 + 4/x - 2/x^2)$. As $x$ approaches infinity, every term containing $1/x$ vanishes, leaving three fifths. The algebraic mechanics are identical to sequence limits because polynomials follow the exact same asymptotic laws whether the variable is discrete or continuous. What changes is that $x$ moves continuously through real numbers, meaning we can also verify the result using differential calculus tools like l'Hôpital's rule.

**Show on screen:** The side-by-side comparison between the $n$-sequence algebraic cancellation and the continuous $x$-function l'Hôpital verification yielding $3/5$.

**If asked to go deeper:** Heine's theorem ensures that $\lim_{x\to\infty} f(x) = L$ if and only if for every sequence $x_n \to \infty$, the image sequence $f(x_n)$ converges to $L$.

---

## Exercise 7 — verbal script

**Key idea:** Factoring a polynomial to remove the indeterminate form $0/0$ at a removable discontinuity.

**What to say:**
Direct substitution of $x = 3$ gives zero over zero, which is undefined. We factor the quadratic numerator into $(x-3)(x-1)$. Because a limit investigates the behavior of the function near 3 without ever evaluating at 3 itself, $x-3$ is non-zero in the punctured neighborhood. We can safely cancel $(x-3)$ from numerator and denominator, reducing the function to $x - 1$. Taking the limit as $x$ approaches 3 of $x - 1$ gives $3 - 1$, which is 2. The value $f(3)$ is not needed because limits depend exclusively on points where $x$ is close to 3, not at $x$ equals 3 itself.

**Show on screen:** The factoring step $\frac{(x-3)(x-1)}{x-3} = x-1$, pointing to the cancelled factor and the hole at $(3, 2)$ on the line $y = x - 1$.

**If asked to go deeper:** Geometrically, the function represents the line $y = x - 1$ with a removable singularity at $x = 3$, which can be continuously extended by defining $f(3) = 2$.

---

## Exercise 8 — verbal script

**Key idea:** Rationalizing the numerator to cancel the factor $(x-4)$ causing the $0/0$ indeterminate form.

**What to say:**
Substituting $x = 4$ yields zero over zero. To eliminate this difficulty, we rationalize the numerator by multiplying and dividing by the conjugate, square root of $x$ plus 2. The numerator simplifies via difference of squares to $(\sqrt{x})^2 - 2^2$, which is $x - 4$. Since $x$ is approaching 4 but not equal to 4, we cancel $(x-4)$ from numerator and denominator, leaving 1 divided by the square root of $x$ plus 2. Substituting $x = 4$ gives 1 divided by $2 + 2$, which evaluates to one fourth. This uses the same difference of squares identity as Exercise 3, but here it resolves a zero-over-zero form at a finite point rather than infinity minus infinity.

**Show on screen:** The conjugate multiplication $(\sqrt{x}-2)(\sqrt{x}+2) = x-4$, the cancellation with the denominator, and the final value $1/4$.

**If asked to go deeper:** This limit is by definition the derivative of $g(x) = \sqrt{x}$ evaluated at $x = 4$, which equals $\frac{1}{2\sqrt{4}} = \frac{1}{4}$.

---

## Exercise 9 — verbal script

**Key idea:** Determining directional infinities from the sign of the denominator to show non-existence of a two-sided limit and locate a vertical asymptote.

**What to say:**
We evaluate the one-sided limits of $1/(x-2)$ as $x$ approaches 2. When $x$ approaches 2 from the left, $x$ is less than 2, so $x - 2$ is negative and approaches zero from below, yielding negative infinity. When $x$ approaches 2 from the right, $x$ is greater than 2, so $x - 2$ is positive and approaches zero from above, yielding positive infinity. Because the left-hand limit is negative infinity and the right-hand limit is positive infinity, they do not agree, so the two-sided limit does not exist. Geometrically, the vertical line $x = 2$ is a vertical asymptote. The graph plunges down to negative infinity on the left and shoots up to positive infinity on the right.

**Show on screen:** The sign analysis of $x-2$ for $x < 2$ and $x > 2$, along with the sketch of the hyperbola showing opposite branches around $x = 2$.

**If asked to go deeper:** Because the pole at $x = 2$ has odd multiplicity 1, the function changes sign across the singularity; an even multiplicity pole like $\frac{1}{(x-2)^2}$ would tend to $+\infty$ on both sides.

---

## Exercise 10 — verbal script

**Key idea:** Enforcing continuity at a boundary by equating the left-hand limit, right-hand limit, and function value.

**What to say:**
For a function to be continuous at $x = 2$, three quantities must exist and be equal: the left-hand limit, the right-hand limit, and the function value $f(2)$. For $x$ less than 2, the left-hand limit of $ax + 1$ evaluates to $2a + 1$. For $x$ greater than or equal to 2, the right-hand limit of $x^2 - 1$ evaluates to $2^2 - 1$, which is 3, and the function value $f(2)$ is also 3. To make the function continuous, we set the left-hand limit equal to 3, giving $2a + 1 = 3$. Subtracting 1 gives $2a = 2$, so $a = 1$. With $a = 1$, the linear piece connects seamlessly to the parabola at the point $(2, 3)$.

**Show on screen:** The three-way continuity equality $\lim_{x\to 2^-} f(x) = \lim_{x\to 2^+} f(x) = f(2)$ leading to $2a + 1 = 3 \implies a = 1$.

**If asked to go deeper:** Continuity ensures that there is no jump discontinuity at $x = 2$, though the function is not differentiable there since the left derivative is 1 and the right derivative is 4.

---

## Exercise 11 — verbal script

**Key idea:** Factoring the dominant exponential base and applying the squeeze theorem to evaluate an $n$-th root limit.

**What to say:**
We evaluate the $n$-th root of $5^n + 2^n$ as $n$ approaches infinity. Because 5 is strictly greater than 2, $5^n$ dominates the sum while $(2/5)^n$ decays to zero. We can establish clean bounds using the squeeze theorem: $5^n$ is strictly less than $5^n + 2^n$, which is strictly less than $5^n + 5^n$, or $2$ times $5^n$. Taking the $n$-th root across the inequality gives 5 on the left, and 5 times the $n$-th root of 2 on the right. As $n$ goes to infinity, the $n$-th root of 2 approaches 1, so the upper bound approaches 5. Trapped between 5 and a sequence approaching 5, the limit must equal 5. This differs from polynomial quotients because we factor out an exponential power under a changing root rather than dividing fractions.

**Show on screen:** The sandwich inequality $5 < \sqrt[n]{5^n+2^n} < 5\sqrt[n]{2}$ and both outer bounds converging to 5.

**If asked to go deeper:** This illustrates the general property that the $\ell^p$ norm of a finite vector converges to its $\ell^\infty$ or maximum norm as $p$ approaches infinity: $\lim_{p\to\infty}(a^p+b^p)^{1/p} = \max(a, b)$.

---

## Exercise 12 — verbal script

**Key idea:** Rewriting an indeterminate form $1^\infty$ into the standard continuous exponential limit $[(1+u)^{1/u}]^k = e^k$.

**What to say:**
As $x$ approaches zero, the expression $(1+3x)^{1/x}$ has base approaching 1 and exponent approaching infinity, giving the indeterminate form $1^\infty$. We recall from Exercise 5 that the continuous limit of $(1+u)^{1/u}$ as $u$ approaches zero is Euler's number $e$. To match this structure, we let $u = 3x$. The exponent $1/x$ can be rewritten as $3/(3x)$, or $1/(3x)$ times 3. This allows us to express the function as $[(1+3x)^{1/(3x)}]^3$. Since the inner term approaches $e$ and cubing is a continuous operation, the entire limit evaluates to $e^3$.

**Show on screen:** The exponent split $(1+3x)^{\frac{1}{3x} \cdot 3} = \left[(1+3x)^{\frac{1}{3x}}\right]^3 \to e^3$.

**If asked to go deeper:** Taking logarithms transforms this into $\lim_{x\to 0} \frac{\ln(1+3x)}{x}$, which by l'Hôpital's rule evaluates to 3, confirming the limit of the original function is $e^3$.

---

## Exercise 13 — verbal script

**Key idea:** Scaling arguments so that the angle in the sine exactly matches its divisor, enabling reduction to $\lim_{u\to 0}\frac{\sin u}{u} = 1$.

**What to say:**
Both expressions yield zero over zero as $x$ approaches zero. We reduce each to the fundamental trigonometric limit, which states that sine of $u$ over $u$ approaches 1 as $u$ approaches zero. For the first limit, we multiply and divide the denominator by 5, writing it as 5 times $\sin(5x)/(5x)$. As $x$ approaches zero, $5x$ approaches zero, so the fraction approaches 1, leaving $5 \times 1 = 5$. For the second limit, we divide numerator and denominator by $x$, then scale each by its respective coefficient: 2 in the numerator and 3 in the denominator. This gives $2/3$ times the quotient of $\sin(2x)/(2x)$ and $\sin(3x)/(3x)$. Since both sine ratios approach 1, the limit is simply two thirds.

**Show on screen:** The balanced argument adjustments: $5 \cdot \frac{\sin 5x}{5x} \to 5(1)$ and $\frac{2}{3} \cdot \frac{\sin 2x / 2x}{\sin 3x / 3x} \to \frac{2}{3} \cdot \frac{1}{1}$.

**If asked to go deeper:** For small angles in radians, sine is asymptotically equivalent to its argument, $\sin(\theta) \sim \theta$, which directly explains why the ratio of sines equals the ratio of their coefficients.

---

## Exercise 14 — verbal script

**Key idea:** Multiplying by the conjugate $1+\cos x$ to convert $1-\cos x$ into $\sin^2 x$ and applying the fundamental limit.

**What to say:**
Direct evaluation gives zero over zero, and the problem explicitly instructs us not to use l'Hôpital's rule. We resolve this by multiplying numerator and denominator by the conjugate, $1 + \cos x$. In the numerator, $(1 - \cos x)(1 + \cos x)$ expands to $1 - \cos^2 x$, which equals $\sin^2 x$ by the Pythagorean identity. We can now regroup the terms into $(\sin x / x)^2$ times $1 / (1 + \cos x)$. As $x$ approaches zero, $\sin x / x$ approaches 1 by the fundamental trigonometric limit, so its square is 1. In the second factor, $\cos(0) = 1$, so the denominator approaches $1 + 1 = 2$. Multiplying 1 by one half gives one half.

**Show on screen:** The steps $(1-\cos x)(1+\cos x) = \sin^2 x$ followed by grouping into $\left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1+\cos x} = 1^2 \cdot \frac{1}{2} = \frac{1}{2}$.

**If asked to go deeper:** Alternatively, using the half-angle formula $1 - \cos x = 2\sin^2(x/2)$ yields $\frac{2\sin^2(x/2)}{4(x/2)^2} = \frac{1}{2}\left(\frac{\sin(x/2)}{x/2}\right)^2 \to \frac{1}{2}$.

---

## Exercise 15 — verbal script

**Key idea:** Contrasting empirical tables and graphical intuition with rigorous deductive proof in limit analysis.

**What to say:**
To explore the relationship between observation and proof, we selected the sequence $\sqrt{n^2+5n}-n$ and the function $(x^2-4x+3)/(x-3)$. Computing sequence values for $n$ from 1 to 10000 shows steady growth from 1.45 toward 2.5, matching our analytical result of five halves. For the function, constructing a table from both left and right around $x = 3$ shows symmetric convergence toward 2, even though the function is undefined at 3. However, these calculations do not constitute a proof. A finite table cannot check infinitely many points, cannot detect high-frequency oscillations like $\sin(\pi/x)$, and is subject to computational roundoff errors. True mathematical proof requires deductive arguments such as algebraic factorization or formal epsilon-delta bounds that verify the limit condition across the entire continuous neighborhood.

**Show on screen:** The summary table showing sequence terms approaching 2.5 and function values pinching to 2, contrasted with the formal $\varepsilon$-$N$ and $\varepsilon$-$\delta$ definitions.

**If asked to go deeper:** The historical transition from intuitive calculus to rigorous analysis by Cauchy and Weierstrass arose precisely because empirical calculation failed on pathological functions with discontinuous or infinitely oscillating limits.

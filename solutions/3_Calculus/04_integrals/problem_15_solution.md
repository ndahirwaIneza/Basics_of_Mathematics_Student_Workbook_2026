# Exercise 15

**Problem:** The function $F$ satisfies

$$
F'(x)=2xe^{x^2}
$$

and

$$
F(0)=3.
$$

1. Recognize the method needed to find the function $F$.
2. Determine the entire family of functions with the given derivative.
3. Use the condition $F(0)=3$ to determine the correct constant.
4. Verify the final result by differentiation and substitution of $x=0$.

---

## Relevant theorem / definition

An initial value problem of the first order:

$$
F'(x) = f(x), \quad F(x_0) = y_0
$$

has the general solution given by the indefinite integral:

$$
F(x) = \int f(x)\,dx = F_0(x) + C
$$

The particular solution is obtained by substituting $x = x_0$ and solving $F_0(x_0) + C = y_0$ for the unique constant $C$.

Integration by substitution states:

$$
\int f(g(x))g'(x)\,dx = \int f(u)\,du
$$

---

## Solution

1. Recognizing the method:
   The derivative $F'(x) = 2x e^{x^2}$ is a product of an exponential function with a quadratic exponent $x^2$ and the exact derivative of that exponent, since $\frac{d}{dx}(x^2) = 2x$. This composite structure with an outside derivative factor indicates integration by substitution with $u = x^2$.

2. Determining the entire family of functions:
   Integrate $F'(x)$ with respect to $x$:

$$
   F(x) = \int 2x e^{x^2}\,dx
$$

   Let $u = x^2$, which gives $du = 2x\,dx$.
   Substitute into the integral:

$$
   F(x) = \int e^u\,du = e^u + C
$$

   Back-substitute $u = x^2$:

$$
   F(x) = e^{x^2} + C, \quad C \in \mathbb{R}
$$

3. Using the condition $F(0) = 3$ to find $C$:
   Substitute $x = 0$ into the general family:

$$
   F(0) = e^{0^2} + C = e^0 + C = 1 + C
$$

   Set this equal to the prescribed initial value $3$:

$$
   1 + C = 3 \implies C = 3 - 1 = 2
$$

   The particular solution is:

$$
   F(x) = e^{x^2} + 2
$$

4. Verification by differentiation and substitution of $x = 0$:
   - Differentiating $F(x)$ via the chain rule:

$$
     F'(x) = \frac{d}{dx}\left(e^{x^2} + 2\right) = e^{x^2} \cdot \frac{d}{dx}(x^2) + 0 = 2xe^{x^2}
$$

     This matches the differential equation $F'(x) = 2xe^{x^2}$.
   - Evaluating at $x = 0$:

$$
     F(0) = e^{0^2} + 2 = e^0 + 2 = 1 + 2 = 3
$$

     This satisfies the initial condition $F(0) = 3$.

---

## Result

$$
\text{Family of antiderivatives: } F(x) = e^{x^2} + C, \quad C \in \mathbb{R}
$$

$$
\text{Particular solution: } F(x) = e^{x^2} + 2
$$

---

## Verification

**Pass 1 — Algebraic check:** Applying the Fundamental Theorem of Calculus directly to the initial value problem:

$$
F(x) = F(0) + \int_0^x 2t e^{t^2}\,dt = 3 + \left[ e^{t^2} \right]_0^x = 3 + (e^{x^2} - e^0) = 3 + e^{x^2} - 1 = e^{x^2} + 2
$$

The result matches identically.

**Pass 2 — Numerical check:** At $x = 1$, $F(1) = e^1 + 2 = e + 2 \approx 4.71828$. Numerical derivative with step $h = 0.001$:

$$
\frac{F(1.001) - F(0.999)}{0.002} = \frac{e^{1.002001} + 2 - (e^{0.998001} + 2)}{0.002} \approx \frac{2.72373 - 2.71286}{0.002} \approx 5.435
$$

The exact derivative is $F'(1) = 2(1)e^1 = 2e \approx 5.43656$.

**Pass 3 — Consistency check:** Since $x^2 \ge 0$, $e^{x^2} \ge 1$ for all real $x$. Therefore $F(x) = e^{x^2} + 2 \ge 3$ for all $x$, with its global minimum occurring precisely at $x = 0$ where $F(0) = 3$ and $F'(0) = 0$.

---

## Exam tip

Remember that $e^0 = 1$, not $0$; when solving for $C$ with an exponential at $x = 0$, $F(0) = e^0 + C = 1 + C$.

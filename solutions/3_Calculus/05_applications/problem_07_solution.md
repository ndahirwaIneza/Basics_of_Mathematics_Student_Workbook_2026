# Exercise 7

**Problem:** Assume the model

$$
N(t)=N_0e^{kt},\qquad k>0.
$$

1. Verify by differentiation that the model satisfies the relation $N'(t)=kN(t)$.
2. Find the population doubling time.
3. Explain why the doubling time does not depend on $N_0$.

---

## Relevant theorem / definition

The chain rule for exponential functions states that $\frac{d}{dt}\left(e^{u(t)}\right) = u'(t)e^{u(t)}$. The doubling time $T_d$ is the time elapsed for a quantity to double its initial value, satisfying $N(t + T_d) = 2N(t)$ for all $t$. The per-capita growth rate is defined as $\frac{N'(t)}{N(t)}$.

---

## Solution

1. Verification of $N'(t) = kN(t)$:
   Differentiate $N(t) = N_0 e^{kt}$ with respect to $t$, treating $N_0$ and $k$ as constants:

   $$
   \begin{align}
   N'(t) &= \frac{d}{dt}\left(N_0 e^{kt}\right) \\
   &= N_0 \cdot \frac{d}{dt}\left(e^{kt}\right) \\
   &= N_0 \cdot \left(k e^{kt}\right) \\
   &= k \left(N_0 e^{kt}\right) \\
   &= k N(t)
   \end{align}
   $$

   The differential relation $N'(t) = k N(t)$ is verified.

2. Population doubling time:
   Let $T_d$ be the doubling time. By definition, at $t = T_d$, the population reaches $2N_0$:

   $$
   N(T_d) = 2N_0
   $$

   Substitute the expression for $N(T_d)$:

   $$
   N_0 e^{k T_d} = 2N_0
   $$

   Divide both sides by $N_0$ (since $N_0 > 0$):

   $$
   e^{k T_d} = 2
   $$

   Take the natural logarithm of both sides:

   $$
   \ln\left(e^{k T_d}\right) = \ln 2 \implies k T_d = \ln 2
   $$

   Solve for $T_d$:

   $$
   T_d = \frac{\ln 2}{k}
   $$

3. Independence from $N_0$:
   Algebraically, the factor $N_0$ scales both the initial state $N(0)$ and the target state $N(T_d) = 2N_0$ linearly, so dividing the target equation by $N_0$ leaves $e^{k T_d} = 2$, which depends solely on $k$.
   Conceptually, dividing the governing differential equation by $N(t)$ gives:

   $$
   \frac{N'(t)}{N(t)} = k = \text{const}
   $$

   The relative growth rate per individual is constant over time. The time required for any population size to multiply by a factor of 2 depends exclusively on the individual rate constant $k$, not on the initial scale of the population.

---

## Result

$$
N'(t) = k N(t)
$$

$$
T_d = \frac{\ln 2}{k}
$$

$$
\text{Independence from } N_0 \text{ follows from } \frac{N(t + T_d)}{N(t)} = e^{k T_d} = 2
$$

---

## Verification

**Pass 1 — Algebraic check:** Check doubling from an arbitrary time $t_0 \ne 0$:

$$
\frac{N(t_0 + T_d)}{N(t_0)} = \frac{N_0 e^{k(t_0 + T_d)}}{N_0 e^{kt_0}} = e^{k T_d} = e^{k \cdot \frac{\ln 2}{k}} = e^{\ln 2} = 2
$$

The population doubles over any interval of length $T_d$, independent of both $N_0$ and the starting time $t_0$.

**Pass 2 — Numerical check:** Let $k = 0.05\text{ yr}^{-1}$. Then $T_d = \frac{\ln 2}{0.05} \approx \frac{0.69315}{0.05} \approx 13.863\text{ yr}$. For $N_0 = 100$: $N(13.863) = 100 e^{0.05 \times 13.863} = 100 e^{0.69315} = 200$. For $N_0 = 5000$: $N(13.863) = 5000(2) = 10000$.

**Pass 3 — Consistency check:** Dimensionally, $k$ has units $[1/\text{time}]$. Therefore, $T_d = \frac{\ln 2}{k}$ has units of $[\text{time}]$, consistent with a time interval. Furthermore, as $k$ increases, growth is faster, and $T_d$ decreases proportionally.

---

## Exam tip

Remember the exact formula $T_d = \frac{\ln 2}{k}$; in quick calculations $\ln 2 \approx 0.693$ yields the well-known "rule of 70" ($T_d \approx \frac{70}{\text{growth percentage}}$).

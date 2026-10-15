# Math patterns reference

Common solution patterns for each topic in Basics of Mathematics 2026.
Use these as templates — adapt to the specific numbers in each exercise.

---

## Matrices — row operations notation

Label every elementary row operation explicitly:

```
R_2 \leftarrow R_2 - 3R_1
R_3 \leftarrow R_3 + 2R_1
R_3 \leftarrow R_3 - \tfrac{1}{2}R_2
```

For augmented matrix:

$$
\left[\begin{array}{ccc|c}
1 & 2 & 3 & 4 \\
0 & 1 & 2 & 3 \\
0 & 0 & 1 & 2
\end{array}\right]
$$

---

## Determinant — 3×3 cofactor expansion along row 1

$$
\det(A) = a_{11}
\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix}
- a_{12}
\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix}
+ a_{13}
\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}
$$

Sarrus rule (write explicitly for the student):

$$
\det(A) = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}
- a_{13}a_{22}a_{31} - a_{12}a_{21}a_{33} - a_{11}a_{23}a_{32}
$$

---

## Matrix inverse — augmented method

$$
[A \mid I] \xrightarrow{\text{row reduce}} [I \mid A^{-1}]
$$

Verification pattern:

$$
A \cdot A^{-1} =
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

For $2 \times 2$, direct formula:

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
\implies
A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$

---

## Systems — rank and solution type

For $A\mathbf{x} = \mathbf{b}$ with augmented matrix $[A|\mathbf{b}]$:

| Condition | Solution type |
|-----------|--------------|
| $\text{rank}(A) = \text{rank}([A\|\mathbf{b}]) = n$ | Unique solution |
| $\text{rank}(A) = \text{rank}([A\|\mathbf{b}]) < n$ | Infinitely many (free variables) |
| $\text{rank}(A) < \text{rank}([A\|\mathbf{b}])$ | No solution |

Free variable parametric form:

$$
\mathbf{x} = \mathbf{x}_0 + t\,\mathbf{v}, \quad t \in \mathbb{R}
$$

---

## Vectors — key identities

Dot product:

$$
\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3
$$

Cross product (use determinant form):

$$
\mathbf{u} \times \mathbf{v} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3
\end{vmatrix}
$$

Angle:

$$
\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|},
\quad \theta \in [0, \pi]
$$

Projection of $\mathbf{u}$ onto $\mathbf{v}$:

$$
\text{proj}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2}\,\mathbf{v}
$$

---

## Lines and planes — standard forms

**Line through point $P_0$ with direction $\mathbf{d}$:**

$$
\mathbf{r}(t) = \mathbf{r}_0 + t\,\mathbf{d}, \quad t \in \mathbb{R}
$$

Component form:

$$
\frac{x - x_0}{d_1} = \frac{y - y_0}{d_2} = \frac{z - z_0}{d_3}
$$

**Plane through $P_0$ with normal $\mathbf{n} = (a,b,c)$:**

$$
a(x - x_0) + b(y - y_0) + c(z - z_0) = 0
$$

Standard form: $ax + by + cz = d$ where $d = ax_0 + by_0 + cz_0$.

**Distance from point $(x_1, y_1, z_1)$ to plane $ax + by + cz = d$:**

$$
D = \frac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}
$$

---

## Conics — standard forms and identification

| Equation | Type |
|----------|------|
| $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ | Ellipse |
| $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ | Hyperbola (opens left/right) |
| $y^2 = 4px$ | Parabola |
| $x^2 + y^2 = r^2$ | Circle |

Completing the square template:

$$
x^2 + 6x = (x+3)^2 - 9
$$

For surfaces — identify by cross-sections:
- Ellipsoid: all cross-sections are ellipses.
- Paraboloid: parabolic cross-section in one direction.
- Hyperboloid of one sheet: hyperbolic cross-section in one direction, elliptic in another.

---

## Limits — method selection

| Indeterminate form | Primary method |
|--------------------|---------------|
| $\frac{0}{0}$ | Factor and cancel, or L'Hôpital |
| $\frac{\infty}{\infty}$ | Divide by highest power, or L'Hôpital |
| $0 \cdot \infty$ | Rewrite as $\frac{0}{1/\infty}$ |
| $\infty - \infty$ | Common denominator or conjugate |
| $1^\infty$, $0^0$, $\infty^0$ | Take logarithm, reduce to $\frac{0}{0}$ |

Standard limits to apply directly:

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1, \qquad
\lim_{x \to 0} \frac{e^x - 1}{x} = 1, \qquad
\lim_{x \to 0} \frac{\ln(1+x)}{x} = 1
$$

$$
\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e
$$

---

## Derivatives — rule templates

Product rule: $(uv)' = u'v + uv'$

Quotient rule: $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$

Chain rule: $[f(g(x))]' = f'(g(x)) \cdot g'(x)$

Common derivatives:

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ |
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ |

---

## Function analysis — template sequence

1. **Domain** $D_f$: find where $f(x)$ is defined (denominator $\neq 0$, argument of $\ln > 0$, etc.)

2. **Even/odd:** check $f(-x) = f(x)$ or $-f(x)$.

3. **Monotonicity:** solve $f'(x) = 0$, build sign table.

4. **Extrema:** $f'$ changes sign at critical point → local min/max.

5. **Concavity:** solve $f''(x) = 0$, build sign table.

6. **Inflection points:** $f''$ changes sign.

7. **Asymptotes:**
   - Vertical: $\lim_{x \to a} f(x) = \pm\infty$
   - Horizontal: $\lim_{x \to \pm\infty} f(x) = L$
   - Oblique: $y = mx + b$ where $m = \lim_{x\to\infty}\frac{f(x)}{x}$, $b = \lim_{x\to\infty}[f(x)-mx]$

---

## Integrals — method templates

**Substitution:** $\int f(g(x))g'(x)\,dx$

Set $u = g(x)$, $du = g'(x)\,dx$, transform integrand to $\int f(u)\,du$.

**Integration by parts:**

$$
\int u\,dv = uv - \int v\,du
$$

Priority for $u$: Logarithms → Inverse trig → Algebraic → Trig → Exponential (LIATE).

**Partial fractions:** for $\frac{P(x)}{Q(x)}$ with $\deg P < \deg Q$:

Linear factor $(x-a)$: contributes $\dfrac{A}{x-a}$

Repeated linear $(x-a)^2$: contributes $\dfrac{A}{x-a} + \dfrac{B}{(x-a)^2}$

Irreducible quadratic $(x^2+bx+c)$: contributes $\dfrac{Ax+B}{x^2+bx+c}$

**Common results:**

$$
\int x^n\,dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)
$$

$$
\int e^x\,dx = e^x + C, \qquad \int \frac{1}{x}\,dx = \ln|x| + C
$$

$$
\int \sin x\,dx = -\cos x + C, \qquad \int \cos x\,dx = \sin x + C
$$

$$
\int \frac{1}{1+x^2}\,dx = \arctan x + C, \qquad \int \frac{1}{\sqrt{1-x^2}}\,dx = \arcsin x + C
$$

---

## Applications — setup templates

**Area between curves:**

$$
A = \int_a^b [f(x) - g(x)]\,dx
$$

Confirm which function is on top before integrating.

**Volume of revolution (disk method, around $x$-axis):**

$$
V = \pi \int_a^b [f(x)]^2\,dx
$$

**Arc length:**

$$
L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx
$$

**Optimization:** set $f'(x) = 0$, solve, verify with $f''$ at critical point.
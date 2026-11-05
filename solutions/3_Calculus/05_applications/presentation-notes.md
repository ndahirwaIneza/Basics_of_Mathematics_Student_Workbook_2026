# Presentation Notes — Applications of Differential and Integral Calculus

## Topic summary

Differential and integral calculus provide the mathematical language for modeling rates of change, geometric accumulation, and optimal configurations in real-world systems. Differentiation identifies instantaneous rates, turning points, and optimal trade-offs by locating critical points and verifying concavity through second derivatives. Definite integration aggregates continuously varying quantities over intervals, transforming local rates into net accumulated changes, computing enclosed geometric areas and solid volumes, and evaluating true continuous averages. Solving applied problems requires a structured three-stage methodology: abstracting geometric and economic constraints into single-variable mathematical models with physically valid domains, executing calculus operations rigorously, and interpreting the mathematical results within their practical context.

---

## Exercise 1 — verbal script

**Key idea:** Differentiation of position yielding instantaneous velocity and acceleration, and using sign analysis to determine direction of motion.

**What to say:**
We analyze the one-dimensional motion of a point given by the cubic position function $s(t) = t^3 - 6t^2 + 9t + 2$ for $t \ge 0$. Differentiating position with respect to time gives the velocity $v(t) = 3t^2 - 12t + 9$, and differentiating velocity gives the acceleration $a(t) = 6t - 12$. The point stops when its velocity is instantaneously zero. Factoring the velocity polynomial as $3(t - 1)(t - 3) = 0$ yields stopping times at $t = 1$ and $t = 3$. To determine direction, we examine the sign of velocity across the domain: for $t \in [0, 1)$ and $t > 3$, $v(t) > 0$, meaning the point moves forward in the positive direction; for $t \in (1, 3)$, $v(t) < 0$, meaning the point moves backward in the negative direction. The point momentarily halts and reverses direction at $t = 1$ and $t = 3$.

**Show on screen:** The factorized form $v(t) = 3(t - 1)(t - 3)$ and the sign chart partitioning the time axis into intervals $[0, 1)$, $(1, 3)$, and $(3, \infty)$.

**If asked to go deeper:** At $t = 1$, $a(1) = -6 \ne 0$, showing that acceleration can be non-zero when velocity vanishes, which characterizes a true turning point rather than an inflection of position.

---

## Exercise 2 — verbal script

**Key idea:** Single-variable optimization of rectangular area under a fixed perimeter constraint using the second derivative test.

**What to say:**
We want to maximize the area of a rectangle with a given perimeter of $40$. The perimeter constraint is $2x + 2y = 40$, which simplifies to $x + y = 20$, allowing us to express the second side as $y = 20 - x$. Substituting this into the area formula produces the single-variable quadratic function $A(x) = 20x - x^2$. Since side lengths must be strictly positive, the geometric domain is the open interval $(0, 20)$. Taking the first derivative gives $A'(x) = 20 - 2x$, which vanishes at the single critical point $x = 10$. The second derivative is $A''(x) = -2$, which is strictly negative everywhere, proving that the function is strictly concave and that $x = 10$ is the unique global maximum. Substituting $x = 10$ back into the constraint gives $y = 10$, demonstrating that the area is maximized when the rectangle is a square with area $100$.

**Show on screen:** The substitution $y = 20 - x$, the derivative $A'(x) = 20 - 2x = 0$, and the second derivative verification $A''(x) = -2 < 0$.

**If asked to go deeper:** This problem exemplifies the isoperimetric theorem in two dimensions: among all quadrilaterals with a fixed perimeter, the square encloses the greatest area.

---

## Exercise 3 — verbal script

**Key idea:** Constructing a cubic volume model from geometric folds and identifying the physically valid critical point.

**What to say:**
We construct an open box from a $30\text{ cm} \times 40\text{ cm}$ sheet of cardboard by removing identical squares of side length $x$ from each corner and folding the edges upright. The resulting box has height $x$, width $30 - 2x$, and length $40 - 2x$, giving a volume function $V(x) = 4x^3 - 140x^2 + 1200x$. Because each side must have positive length, cutting two corners of length $x$ from the shorter $30\text{ cm}$ side requires $x < 15$, establishing the domain as $(0, 15)$. Differentiating and setting $V'(x) = 12x^2 - 280x + 1200 = 0$ leads to the quadratic equation $3x^2 - 70x + 300 = 0$. Solving with the quadratic formula yields two mathematical roots, but only $x = \frac{35 - 5\sqrt{13}}{3} \approx 5.66\text{ cm}$ falls inside our physical domain $(0, 15)$, while the other root around $17.68\text{ cm}$ is physically impossible. Evaluating the second derivative confirms $V''(5.66) = -40\sqrt{13} < 0$, guaranteeing a unique global maximum volume of approximately $3032\text{ cm}^3$.

**Show on screen:** The box dimension diagram ($x$, $30-2x$, $40-2x$), the domain restriction $x < 15$, and the root selection eliminating $x \approx 17.68$.

**If asked to go deeper:** The rejected critical point corresponds to a local minimum of the polynomial where both base dimensions would be negative, which has no physical meaning.

---

## Exercise 4 — verbal script

**Key idea:** Finding curve intersections, establishing the vertical order of graphs, and integrating the difference of functions to find enclosed area.

**What to say:**
To find the area bounded by $y = x$ and $y = x^2$, we must first determine the boundaries of integration and identify which curve lies above the other. Setting $x^2 = x$ gives $x(x - 1) = 0$, locating the intersection points at $(0, 0)$ and $(1, 1)$. On the open interval $(0, 1)$, testing any point or factoring $x - x^2 = x(1 - x)$ shows that the difference is strictly positive, meaning the line $y = x$ lies strictly above the parabola $y = x^2$. The enclosed area is therefore the definite integral of the upper curve minus the lower curve: $\int_0^1 (x - x^2)\,dx$. Evaluating the antiderivative $\frac{x^2}{2} - \frac{x^3}{3}$ between $0$ and $1$ gives $\frac{1}{2} - \frac{1}{3} = \frac{1}{6}$.

**Show on screen:** The algebraic factorization $x(1 - x) > 0$ proving vertical order, followed by the antiderivative evaluation $\left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{6}$.

**If asked to go deeper:** We can also integrate along the $y$-axis using horizontal strips from $y = 0$ to $y = 1$ via $\int_0^1 (\sqrt{y} - y)\,dy$, which yields the identical value of $\frac{1}{6}$ by Fubini's principle.

---

## Exercise 5 — verbal script

**Key idea:** The Fundamental Theorem of Calculus as net accumulation of change, and the distinction between displacement and total distance traveled.

**What to say:**
We are given a car's velocity $v(t) = 4t + 2\text{ m/s}$ over the first 5 seconds. Because $v(t) > 0$ on the entire interval $[0, 5]$, the car travels in a single direction without reversing. The distance traveled is the definite integral of velocity, which evaluates to $[2t^2 + 2t]_0^5 = 50 + 10 = 60\text{ meters}$. The integral of velocity gives position change because velocity is the derivative of position, $\frac{ds}{dt}$; by the Fundamental Theorem of Calculus, integrating this derivative sums the infinitesimal displacements $v(t)\,dt$ across time. If the velocity were to take negative values, the standard integral $\int v(t)\,dt$ would compute only the net displacement, where backward motion cancels forward progress. To obtain the total physical distance recorded by an odometer, one must integrate the absolute speed, $\int |v(t)|\,dt$, splitting the integral at points where velocity changes sign.

**Show on screen:** The integral setup $\int_0^5 (4t+2)\,dt = 60\text{ m}$, and the comparison equations for displacement $\Delta s = \int v\,dt$ versus total distance $d = \int |v|\,dt$.

**If asked to go deeper:** In geometric terms, displacement is the net signed area under the velocity graph, whereas distance is the total geometric area enclosed between the curve and the time axis.

---

## Exercise 6 — verbal script

**Key idea:** Calculating the average value of a continuous function via integration and geometrically interpreting the Mean Value Theorem for Integrals.

**What to say:**
We compute the average value of $f(x) = x^2$ on the interval $[0, 3]$. The formula for the average value of a function is $\frac{1}{b - a} \int_a^b f(x)\,dx$, which gives $\frac{1}{3} \int_0^3 x^2\,dx = \frac{1}{3} \cdot 9 = 3$. By the Mean Value Theorem for Integrals, there must exist a point $c \in [0, 3]$ where the function equals its average value. Setting $c^2 = 3$ and selecting the root in $[0, 3]$ yields $c = \sqrt{3} \approx 1.732$. Geometrically, this means the area under the parabolic curve on $[0, 3]$, which is $9$, equals the area of a rectangle with base length $3$ and constant height $3$. The point $c = \sqrt{3}$ is where the parabola crosses the top edge of this rectangle, meaning the area of the curve above $y = 3$ exactly balances the deficit below $y = 3$.

**Show on screen:** The average value computation $f_{\text{avg}} = 3$, the solving step $c = \sqrt{3}$, and the geometric diagram showing the rectangle of equal area $3 \times 3 = 9$.

**If asked to go deeper:** Because $f(x) = x^2$ is strictly convex, its average value $3$ is strictly lower than the midpoint of its endpoint values, which is $\frac{0 + 9}{2} = 4.5$, as predicted by Jensen's inequality.

---

## Exercise 7 — verbal script

**Key idea:** Connecting exponential growth models to proportional rates of change and demonstrating scale-invariance of the doubling time.

**What to say:**
We consider the exponential population model $N(t) = N_0 e^{kt}$ with growth constant $k > 0$. Differentiating with respect to time using the chain rule yields $N'(t) = N_0 k e^{kt} = k(N_0 e^{kt}) = k N(t)$, which proves that the instantaneous rate of growth is directly proportional to the current population size. To find the doubling time $T_d$, we set $N(T_d) = 2N_0$, leading to $N_0 e^{k T_d} = 2N_0$. Dividing both sides by $N_0$ and taking natural logarithms yields $k T_d = \ln 2$, so $T_d = \frac{\ln 2}{k}$. The doubling time does not depend on the initial population $N_0$ because $N_0$ cancels out algebraically. Intuitively, the per-capita growth rate $\frac{N'(t)}{N(t)} = k$ is constant, so every individual reproduces at the same average rate, making the relative time needed to double identical whether starting with ten individuals or ten million.

**Show on screen:** The differentiation steps confirming $N'(t) = kN(t)$, the cancellation of $N_0$ in $e^{kT_d} = 2$, and the closed-form doubling formula $T_d = \frac{\ln 2}{k}$.

**If asked to go deeper:** The inverse process of exponential decay, such as radioactive decay with rate $-k$, yields the exact same formula for half-life, $T_{1/2} = \frac{\ln 2}{k}$.

---

## Exercise 8 — verbal script

**Key idea:** Computing total cumulative server requests from an arrival rate function and analyzing the mean value of linear rates.

**What to say:**
A server receives incoming requests at a rate described by $r(t) = 100 + 20t$ requests per minute over the first 5 minutes. The total volume of requests received is the definite integral of the rate function: $\int_0^5 (100 + 20t)\,dt = [100t + 10t^2]_0^5 = 500 + 250 = 750\text{ requests}$. Dividing this total by the 5-minute interval gives an average arrival rate of $150\text{ requests per minute}$. Evaluating the rate at the endpoints gives $r(0) = 100$ and $r(5) = 200$. Notice that the average rate $150$ is exactly the arithmetic mean of the initial and final rates, $\frac{100 + 200}{2} = 150$. This exact agreement is a general property of all linear functions, whose average value over any symmetric interval equals the arithmetic mean of the endpoints and the function value at the temporal midpoint $t = 2.5$.

**Show on screen:** The definite integral evaluation to $750$ requests, the division by $5$ to obtain $150\text{ req/min}$, and the equality $r_{\text{avg}} = \frac{r(0) + r(5)}{2} = r(2.5)$.

**If asked to go deeper:** If the arrival rate were non-linear, such as quadratic or exponential, this simple arithmetic average would fail, and the true average would require the integral formula.

---

## Exercise 9 — verbal script

**Key idea:** Constrained optimization of cylinder surface area under fixed volume, proving the optimal aspect ratio has height equal to diameter.

**What to say:**
We want to minimize the surface area of a closed cylindrical can that must enclose a fixed volume $V$. The volume constraint is $V = \pi r^2 h$, from which we eliminate height as $h = \frac{V}{\pi r^2}$. Substituting this into the total surface area formula $A = 2\pi r^2 + 2\pi rh$ produces a single-variable function of the radius: $A(r) = 2\pi r^2 + \frac{2V}{r}$ for $r > 0$. Differentiating with respect to $r$ gives $A'(r) = 4\pi r - \frac{2V}{r^2}$. Setting this derivative to zero yields $4\pi r^3 = 2V$, or $2\pi r^3 = V$. Replacing $V$ with $\pi r^2 h$ simplifies directly to $h = 2r$. Because the second derivative $A''(r) = 4\pi + \frac{4V}{r^3}$ is strictly positive for all $r > 0$, this critical point represents the unique global minimum. Geometrically, $h = 2r$ means the height equals the base diameter, so the axial cross-section of the most material-efficient can is a square.

**Show on screen:** The substitution eliminating $h$, the derivative $A'(r) = 4\pi r - \frac{2V}{r^2} = 0$, and the final geometric relationship $h = 2r$.

**If asked to go deeper:** If the can were open at the top, having only one circular base, the same optimization procedure would yield $h = r$ instead of $h = 2r$.

---

## Exercise 10 — verbal script

**Key idea:** Minimizing piecewise transportation and installation costs across water and land using Pythagorean distance and convex optimization.

**What to say:**
A cable must connect point $A$ on one river bank to point $B$ on the opposite bank, located $100\text{ m}$ across and $500\text{ m}$ downstream. Underwater cable costs twice as much per meter as land cable. If the cable emerges from the water at a downstream distance $x$, the underwater distance is $\sqrt{x^2 + 100^2}$ and the land distance is $500 - x$, with $x \in [0, 500]$. The total cost function is $C(x) = c(2\sqrt{x^2 + 10000} + 500 - x)$, where $c$ is the land cost per meter. Differentiating and setting $C'(x) = 0$ gives $\frac{2x}{\sqrt{x^2 + 10000}} = 1$. Squaring both sides yields $4x^2 = x^2 + 10000$, which gives $3x^2 = 10000$ and $x = \frac{100}{\sqrt{3}} \approx 57.74\text{ meters}$. The second derivative is strictly positive, verifying a global cost minimum of approximately $673.2c$, which saves money compared to both a direct underwater line ($1019.8c$) and going straight across ($700c$).

**Show on screen:** The geometric path layout, the derivative equation $\frac{2x}{\sqrt{x^2 + 10000}} = 1$, and the solution $x = \frac{100}{\sqrt{3}}\text{ m}$.

**If asked to go deeper:** The condition $\frac{x}{\sqrt{x^2 + 100^2}} = \frac{1}{2}$ is equivalent to $\sin\theta = \frac{1}{2}$ where $\theta = 30^\circ$, which is Fermat's principle of least time and Snell's law of refraction applied to cost optimization.

---

## Exercise 11 — verbal script

**Key idea:** Slicing a solid of revolution into infinitesimal circular disks to construct and evaluate a definite volume integral.

**What to say:**
We calculate the volume generated by rotating the region under $y = \sqrt{x}$ from $x = 0$ to $x = 4$ about the $x$-axis. Using the disk method, we slice the solid perpendicular to the $x$-axis at each coordinate $x$. Each slice is a circular disk whose radius $r$ is the height of the curve, $y = \sqrt{x}$. The cross-sectional area of any circle is $\pi r^2$, which gives $A(x) = \pi y^2 = \pi (\sqrt{x})^2 = \pi x$. Multiplying by the infinitesimal slice thickness $dx$ gives the disk volume element $dV = \pi x\,dx$. Summing these disks by integrating from $0$ to $4$ yields $V = \pi \int_0^4 x\,dx = \pi \left[\frac{x^2}{2}\right]_0^4 = 8\pi \approx 25.13$. The factor $\pi y^2$ arises directly from Euclidean geometry: revolution about the axis sweeps out circles of radius $y$, each possessing cross-sectional area $\pi y^2$.

**Show on screen:** The disk slicing diagram, the substitution of $r = \sqrt{x}$ into $A(x) = \pi r^2 = \pi x$, and the integration $\pi \left[\frac{x^2}{2}\right]_0^4 = 8\pi$.

**If asked to go deeper:** The resulting paraboloid of revolution has height $4$ and base radius $2$; its volume of $8\pi$ is exactly half the volume of a cylinder with the same dimensions ($16\pi$), confirming Archimedes' classic theorem.

---

## Exercise 12 — verbal script

**Key idea:** Complete mathematical modeling, constraint reduction, derivative optimization, and budget equipartition for an exhibition room.

**What to say:**
We design a rectangular museum room adjacent to an existing wall that requires no construction. The two perpendicular sides cost $300\ \mathrm{PLN/m}$ and have length $x$, while the single parallel side costs $500\ \mathrm{PLN/m}$ and has length $y$, with a fixed budget of $30\,000\ \mathrm{PLN}$. The budget constraint is $2(300)x + 500y = 30000$, or $6x + 5y = 300$, which lets us express $y = 60 - 1.2x$. The physical domain requires positive lengths, giving $x \in (0, 50)$. The area function is $A(x) = x(60 - 1.2x) = 60x - 1.2x^2$. Differentiating yields $A'(x) = 60 - 2.4x$, which gives a unique critical point at $x = 25\text{ meters}$. Since $A''(x) = -2.4 < 0$, this point is a global maximum, giving $y = 30\text{ meters}$ and a maximum enclosed area of $750\text{ m}^2$. Notice that at optimum, the two perpendicular walls cost $2(25)(300) = 15\,000\ \mathrm{PLN}$ and the parallel wall costs $30(500) = 15\,000\ \mathrm{PLN}$, showing that the budget is split exactly 50/50 between the two coordinate directions.

**Show on screen:** The budget equation $6x + 5y = 300$, the area function $A(x) = 60x - 1.2x^2$, the optimum dimensions $(25\text{ m}, 30\text{ m})$, and the 50/50 budget breakdown table.

**If asked to go deeper:** This 50/50 cost split is an invariant property of all bilinear optimization problems with linear constraints: the optimal expenditure is always divided equally among the independent coordinate variables.

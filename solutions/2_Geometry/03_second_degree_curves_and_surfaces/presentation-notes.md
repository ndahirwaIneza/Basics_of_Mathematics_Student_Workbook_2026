# Presentation Notes — Second-Degree Curves and Surfaces

## Topic summary

Second-degree equations in two and three variables describe conic sections and quadric surfaces. In two dimensions, the signs and equality of quadratic coefficients distinguish circles, ellipses, parabolas, and hyperbolas, while completing the square determines translations and centers. In three dimensions, quadric surfaces—including spheres, ellipsoids, paraboloids, hyperboloids, cones, and cylinders—are analyzed systematically by taking planar cross-sections parallel to the coordinate planes. Slicing at fixed coordinate heights transforms spatial surfaces into families of planar conics, exposing their curvature, boundedness, scaling laws, and topological connectivity without relying on rote memorization.

---

## Exercise 1 — verbal script

**Key idea:** Recognizing conic sections from quadratic signs, relative coefficients, and linearity.

**What to say:**
We inspect the four canonical equations to identify their curve types directly from algebraic structure. In $x^2 + y^2 = 9$, both squared variables have identical positive coefficients and sum to a positive constant, defining a circle centered at $(0,0)$ with radius 3. In $x^2/16 + y^2/9 = 1$, both variables are squared with unequal positive coefficients summed to 1, producing an ellipse centered at $(0,0)$ with horizontal semiaxis 4 and vertical semiaxis 3. In $y^2 = 8x$, only $y$ is squared while $x$ appears linearly, which defines a parabola with horizontal axis $y=0$ opening rightward from vertex $(0,0)$. Finally, in $x^2/9 - y^2/4 = 1$, the squared terms have opposite signs, giving a hyperbola centered at the origin with vertices at $(\pm 3, 0)$ and asymptotes $y = \pm \frac{2}{3}x$. The sketch confirms the distinct geometric profiles: compact closed curves for the circle and ellipse, a single open branch for the parabola, and two separate unbounded branches for the hyperbola.

**Show on screen:** The four canonical equations alongside their identified parameters and the four ASCII sketches.

**If asked to go deeper:** The classification corresponds to the sign of the determinant of the $2 \times 2$ quadratic form matrix: positive for elliptic conics, zero for parabolic conics, and negative for hyperbolic conics.

---

## Exercise 2 — verbal script

**Key idea:** Completing the square in two variables to reduce a general quadratic equation to the canonical circle equation.

**What to say:**
We begin with the general equation $x^2 + y^2 - 6x + 4y - 3 = 0$ and group the $x$ and $y$ terms separately. Completing the square for $x$ yields $(x - 3)^2 - 9$, and for $y$ yields $(y + 2)^2 - 4$. Combining the constant terms gives $-9 - 4 - 3 = -16$, which we move to the right-hand side to obtain $(x - 3)^2 + (y + 2)^2 = 16$. From this canonical form, we read off the center $(3, -2)$ and radius $\sqrt{16} = 4$. To verify the result, we select two simple points on the circle by stepping 4 units along the coordinate axes from the center: $P_1 = (7, -2)$ and $P_2 = (3, 2)$. Substituting both points into the canonical form gives $16 = 16$, and substituting them into the original equation yields zero, confirming that both representations describe the exact same circle.

**Show on screen:** The square-completion steps leading to $(x-3)^2 + (y+2)^2 = 16$ and the arithmetic verification for points $P_1$ and $P_2$.

**If asked to go deeper:** Completing the square is geometrically equivalent to applying a translation $X = x - 3, Y = y + 2$ that moves the coordinate origin to the center of symmetry.

---

## Exercise 3 — verbal script

**Key idea:** Determining semiaxis lengths, intercepts, and directional stretching of a canonical ellipse.

**What to say:**
We consider the canonical ellipse $\frac{x^2}{25} + \frac{y^2}{9} = 1$. Matching this with standard form, the denominators are $a^2 = 25$ and $b^2 = 9$, which gives horizontal semiaxis $a = 5$ and vertical semiaxis $b = 3$. Setting $y = 0$ gives the $x$-intercepts at $(\pm 5, 0)$, while setting $x = 0$ gives the $y$-intercepts at $(0, \pm 3)$. The ellipse is more stretched along the $x$-axis because $25 > 9$, so $a = 5 > b = 3$. Algebraically, the larger denominator allows $x$ to reach $\pm 5$ before the first term alone exhausts the total sum of 1, whereas $y$ can reach at most $\pm 3$. The sketch shows a horizontally elongated oval symmetric about both axes with focal distance $c = \sqrt{25 - 9} = 4$.

**Show on screen:** The denominators $a^2=25$ and $b^2=9$, the four intercept coordinates, and the ellipse sketch.

**If asked to go deeper:** The linear eccentricity is $e = c/a = 4/5 = 0.8$, indicating moderate elongation compared to a circle where $e = 0$.

---

## Exercise 4 — verbal script

**Key idea:** Reading the vertex, axis, opening direction, and focal chord of a canonical parabola.

**What to say:**
We analyze the parabola $y^2 = 12x$. Matching this with $y^2 = 2px$ yields $2p = 12$, so the parameter is $p = 6$. The vertex is located at the origin $(0,0)$. Because replacing $y$ with $-y$ leaves the equation invariant, the axis of symmetry is the line $y = 0$, which is the $x$-axis. Since $y^2 \ge 0$ for all real numbers, we must have $12x \ge 0$, which requires $x \ge 0$; hence the curve opens to the right. Setting $x = 3$ gives $y^2 = 12(3) = 36$, yielding the two points $(3, 6)$ and $(3, -6)$. Because $x = p/2 = 3$ is the abscissa of the focus, the vertical chord connecting these points is the latus rectum, with length $2p = 12$.

**Show on screen:** The identification of $p=6$, the points $(3, \pm 6)$, and the sketch showing the vertex, focus $(3,0)$, and directrix $x = -3$.

**If asked to go deeper:** The geometric property $d(P, F) = d(P, \text{directrix})$ holds exactly: the distance from $(3,6)$ to focus $(3,0)$ is 6, which matches the distance to the directrix line $x = -3$.

---

## Exercise 5 — verbal script

**Key idea:** Finding vertices, asymptotes, and analyzing asymptotic convergence of a canonical hyperbola.

**What to say:**
We examine the hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$. Setting $y = 0$ gives $x^2 = 16$, yielding the $x$-intercepts at $(-4, 0)$ and $(4, 0)$, whereas setting $x = 0$ produces $-y^2/9 = 1$, which has no real solutions. To find the asymptotes, we replace the right-hand constant 1 with 0, yielding $\frac{x^2}{16} - \frac{y^2}{9} = 0$, which factors into the two straight lines $y = \pm \frac{3}{4}x$. Far from the center, the constant 1 is negligible compared to $x^2/16$, so the hyperbola approaches these lines. By rationalizing the difference $y_{\text{asymptote}} - y$, we find that the vertical gap equals $\frac{12}{x + \sqrt{x^2 - 16}}$, which tends to zero as $x \to \infty$. The sketch illustrates the two symmetric branches opening horizontally, guided by the asymptote box of dimensions $8 \times 6$.

**Show on screen:** The vertices $(\pm 4, 0)$, the asymptote equations $y = \pm \frac{3}{4}x$, and the limit showing convergence to zero.

**If asked to go deeper:** In projective geometry, the asymptotes represent the tangent lines to the hyperbola at its two ideal points at infinity.

---

## Exercise 6 — verbal script

**Key idea:** Completing the square with non-unit leading coefficients to find the center and semiaxes of a shifted ellipse.

**What to say:**
We are given $4x^2 + 9y^2 - 16x + 18y - 11 = 0$. First, we factor the leading coefficients out of each variable group: $4(x^2 - 4x) + 9(y^2 + 2y) - 11 = 0$. Completing the squares inside the brackets produces $4[(x - 2)^2 - 4] + 9[(y + 1)^2 - 1] - 11 = 0$. Distributing the constants yields $-16 - 9 - 11 = -36$, which moves to the right-hand side as $+36$. Dividing both sides by 36 gives the canonical form $\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1$. This is an ellipse centered at $(2, -1)$ with horizontal semiaxis $a = 3$ and vertical semiaxis $b = 2$. When we substitute the center coordinates $(2, -1)$ into the original equation, we obtain $-36$, which confirms that the squared terms vanish and leave precisely the balanced constant.

**Show on screen:** The factoring and completion steps leading to $\frac{(x-2)^2}{9} + \frac{(y+1)^2}{4} = 1$ and the evaluation $F(2, -1) = -36$.

**If asked to go deeper:** The center of any quadratic form without cross-terms can be confirmed by setting the gradient $\nabla F(x, y) = (8x - 16, 18y + 18)$ to $(0,0)$.

---

## Exercise 7 — verbal script

**Key idea:** Classifying second-degree curves by algebraic form and establishing the non-existence of real points.

**What to say:**
We classify four quadratic equations. First, $4x^2 + 9y^2 = 36$ divides by 36 to $\frac{x^2}{9} + \frac{y^2}{4} = 1$, which is an ellipse centered at the origin with semiaxes 3 and 2. Second, $x^2 - y^2 = 1$ is an equilateral hyperbola centered at $(0,0)$ with vertices $(\pm 1, 0)$ and perpendicular asymptotes $y = \pm x$. Third, $x^2 - 4y = 0$ simplifies to $y = \frac{1}{4}x^2$, which is an upward-opening parabola with vertex at the origin and axis $x = 0$. Fourth, for $x^2 + y^2 + 1 = 0$, both $x^2$ and $y^2$ are non-negative for all real numbers, so $x^2 + y^2 + 1 \ge 1 > 0$. Because the left-hand side is strictly positive everywhere on the real plane, it can never equal zero, meaning the solution set is the empty set.

**Show on screen:** The canonical form of each equation, the object identification, and the inequality $x^2 + y^2 + 1 \ge 1 > 0$.

**If asked to go deeper:** In the complex plane $\mathbb{C}^2$, the equation $x^2 + y^2 = -1$ defines an imaginary circle of radius $i$, with empty real trace.

---

## Exercise 8 — verbal script

**Key idea:** Completing the square in three variables to find the center and radius of a sphere.

**What to say:**
We reduce $x^2 + y^2 + z^2 - 4x + 2y - 6z - 2 = 0$ to canonical form by grouping the terms by coordinate: $(x^2 - 4x) + (y^2 + 2y) + (z^2 - 6z) - 2 = 0$. Completing the square in each variable gives $(x - 2)^2 - 4 + (y + 1)^2 - 1 + (z - 3)^2 - 9 - 2 = 0$. Combining the constant terms gives $-16$, which moves to the right as $+16$, producing $(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16$. From this, we read off the center $S = (2, -1, 3)$ and radius $R = \sqrt{16} = 4$. By shifting 4 units along the coordinate directions from the center, we find two points on the sphere: $P_1 = (6, -1, 3)$ and $P_2 = (2, 3, 3)$. Substituting both points into both forms of the equation yields an exact identity, confirming our result.

**Show on screen:** The three-variable square completion, the center $(2, -1, 3)$, radius $R = 4$, and the substitution check for $P_1$ and $P_2$.

**If asked to go deeper:** The radius invariant formula $R = \sqrt{x_0^2 + y_0^2 + z_0^2 - G}$ provides an immediate arithmetic check: $\sqrt{4 + 1 + 9 - (-2)} = \sqrt{16} = 4$.

---

## Exercise 9 — verbal script

**Key idea:** Characterizing an ellipsoid through semiaxis lengths and analyzing its family of horizontal cross-sections.

**What to say:**
We examine the ellipsoid $\frac{x^2}{9} + \frac{y^2}{4} + \frac{z^2}{16} = 1$. The semiaxis lengths along the coordinate axes are $a = 3, b = 2,$ and $c_0 = 4$. Setting $z = 0$ gives the equatorial cross-section $\frac{x^2}{9} + \frac{y^2}{4} = 1$, which is an ellipse in the $xy$-plane with semiaxes 3 and 2. For any parallel slice $z = c$ with $|c| < 4$, moving $c^2/16$ to the right gives $\frac{x^2}{9} + \frac{y^2}{4} = 1 - \frac{c^2}{16}$. Dividing through by this positive factor yields horizontal ellipses with semiaxes $a(c) = 3\sqrt{1 - c^2/16}$ and $b(c) = 2\sqrt{1 - c^2/16}$. As $|c|$ increases from 0 toward 4, these ellipses shrink homothetically while maintaining a constant axis ratio of $3/2$, until they degenerate into the pole points $(0, 0, \pm 4)$ at $|c| = 4$.

**Show on screen:** The semiaxes $a=3, b=2, c_0=4$, the slice equation with scaling factor $1 - c^2/16$, and the constant aspect ratio $a/b = 1.5$.

**If asked to go deeper:** Integrating the cross-sectional elliptical areas $A(c) = 6\pi(1 - c^2/16)$ from $c = -4$ to $4$ yields $32\pi$, matching the volume formula $V = \frac{4}{3}\pi a b c_0$.

---

## Exercise 10 — verbal script

**Key idea:** Distinguishing an elliptic paraboloid from a hyperbolic paraboloid using axial and planar cross-sections.

**What to say:**
We compare the surfaces $z = x^2 + y^2$ and $z = x^2 - y^2$. For $z = x^2 + y^2$, the vertical cuts $x = 0$ and $y = 0$ are both upward-opening parabolas, $z = y^2$ and $z = x^2$. Slicing horizontally at $z = c > 0$ yields circles of radius $\sqrt{c}$, while $z < 0$ has no real points, producing an upward-opening circular bowl. In contrast, for $z = x^2 - y^2$, the vertical cut $y = 0$ curves upward as $z = x^2$, while $x = 0$ curves downward as $z = -y^2$. Horizontal slices at $z = c > 0$ yield hyperbolas opening along $x$, at $z = 0$ yield intersecting lines $y = \pm x$, and at $z < 0$ yield hyperbolas opening along $y$. This creates a classic saddle surface where the origin is a saddle point—a minimum along $x$ and a maximum along $y$.

**Show on screen:** Side-by-side comparison of cross-sections for both paraboloids and the sketches of the bowl versus the saddle.

**If asked to go deeper:** The difference in geometry is captured by the Gaussian curvature: $K > 0$ everywhere for the elliptic paraboloid, while $K < 0$ everywhere for the hyperbolic paraboloid.

---

## Exercise 11 — verbal script

**Key idea:** Slicing hyperboloids of revolution to distinguish one-sheeted and two-sheeted topologies.

**What to say:**
We compare $x^2 + y^2 - z^2 = 1$ and $x^2 + y^2 - z^2 = -1$. Slicing horizontally at $z = c$, the first surface gives $x^2 + y^2 = 1 + c^2$. Because $1 + c^2 \ge 1 > 0$ for all real $c$, circular cross-sections exist for every height, with a minimum waist radius of 1 at $z = 0$, forming a single connected hourglass sheet. For the second surface, the slice equation is $x^2 + y^2 = c^2 - 1$. Here, no real points exist when $|c| < 1$, the cross-sections pinch to single points at $z = \pm 1$, and circles form only for $|c| > 1$. Thus, the second surface consists of two separate sheets divided by an empty gap of height 2. Both surfaces asymptotically approach the same common cone $x^2 + y^2 = z^2$.

**Show on screen:** The radius functions $r = \sqrt{1 + c^2}$ versus $r = \sqrt{c^2 - 1}$, and the sketches showing the waist circle versus the forbidden band.

**If asked to go deeper:** The hyperboloid of one sheet is a doubly ruled surface, meaning through every point there pass two straight lines lying entirely on the surface.

---

## Exercise 12 — verbal script

**Key idea:** Reconstructing the equation of a quadric surface from geometric cross-sectional constraints.

**What to say:**
We are given three geometric properties: the cross-section at $z = 0$ is a point, horizontal slices for $z > 0$ are expanding circles, and vertical cross-sections through the $z$-axis are parabolas. Because the horizontal cross-sections are circles centered on the $z$-axis, the surface possesses rotational symmetry, depending only on $\rho^2 = x^2 + y^2$. In any vertical axial plane, the radial profile curve is a parabola symmetric about $Oz$, which has the equation $z = a\rho^2$ with $a > 0$. Substituting $\rho^2 = x^2 + y^2$ and taking the simplest scaling factor $a = 1$ yields $z = x^2 + y^2$. Checking all conditions, $z = 0$ yields exclusively $(0,0,0)$, $z = c > 0$ yields circles of radius $\sqrt{c}$ that grow strictly with $c$, and any vertical plane $y = kx$ yields $z = (1 + k^2)x^2$, which confirms the parabolic profile.

**Show on screen:** The three geometric conditions, the derivation $z = a\rho^2 \implies z = x^2 + y^2$, and the verification of each property.

**If asked to go deeper:** Any choice of positive constant $a$ gives a valid circular paraboloid; choosing $a = 1$ sets the focal length of the axial parabolas to $1/4$.

---

## Exercise 13 — verbal script

**Key idea:** Computing the planar intersection of a sphere and classifying the cross-section as a function of plane height.

**What to say:**
We find the intersection of the sphere $x^2 + y^2 + z^2 = 25$ with the horizontal plane $z = 3$. Substituting $z = 3$ gives $x^2 + y^2 + 9 = 25$, which simplifies to $x^2 + y^2 = 16$. In space, this is a circle lying in the plane $z = 3$, centered at $(0, 0, 3)$ with radius $r = 4$. More generally, slicing at $z = c$ produces $x^2 + y^2 = 25 - c^2$. If $|c| < 5$, the right-hand side is positive, producing a circle of radius $\sqrt{25 - c^2}$ centered at $(0, 0, c)$, with maximum radius 5 at the equator $c = 0$. If $|c| = 5$, the circle degenerates to a single tangent point at $(0, 0, 5)$ or $(0, 0, -5)$. If $|c| > 5$, $25 - c^2 < 0$, meaning the plane and sphere do not intersect.

**Show on screen:** The system defining the 3D circle and the trichotomy of cross-sections for $|c| < 5$, $|c| = 5$, and $|c| > 5$.

**If asked to go deeper:** The relation $r = \sqrt{R^2 - d^2}$ is the 3D Pythagorean theorem connecting the sphere radius, the plane distance from the center, and the cross-sectional circle radius.

---

## Exercise 14 — verbal script

**Key idea:** Contrasting a cone and a cylinder via homogeneity, free variables, and generator geometry.

**What to say:**
We compare the cone $x^2 + y^2 = z^2$ and the cylinder $x^2 + y^2 = 4$. For the cone, horizontal slices $z = c$ yield circles of radius $|c|$ that taper to the apex $(0,0,0)$ at $z = 0$, while vertical slices $x = 0$ and $y = 0$ produce intersecting pairs of straight lines $z = \pm y$ and $z = \pm x$. For the cylinder, horizontal slices $z = c$ always yield the exact same circle of radius 2, while vertical cuts produce parallel lines $y = \pm 2$ and $x = \pm 2$. The cone radius depends linearly on $z$ because its equation is homogeneous of degree 2, meaning it is formed by straight rays radiating from the origin. In contrast, the cylinder radius is constant because $z$ does not appear in the equation, making $z$ a free parameter that translates the base circle parallel to the $z$-axis.

**Show on screen:** The comparison of cross-sections $r = |c|$ versus $r = 2$, the vertical cuts, and the sketches of the cone versus cylinder.

**If asked to go deeper:** Both the cone and cylinder have zero Gaussian curvature ($K = 0$), which means both are developable surfaces that can be unrolled onto a flat plane without distortion.

---

## Exercise 15 — verbal script

**Key idea:** Systematic reduction to canonical form and surface identification via anisotropic cross-sections.

**What to say:**
We examine two equations. For the first, $4x^2 + 9y^2 - 8x + 36y + 4 = 0$, completing the squares gives $4(x - 1)^2 + 9(y + 2)^2 = 36$, which reduces to $\frac{(x - 1)^2}{9} + \frac{(y + 2)^2}{4} = 1$. This is an ellipse centered at $(1, -2)$ with horizontal semiaxis 3 and vertical semiaxis 2. For the second equation, $4x^2 + y^2 = z^2$, we inspect cross-sections without assuming a name. Horizontal slices $z = c$ give $4x^2 + y^2 = c^2$, which can be written as $\frac{x^2}{(|c|/2)^2} + \frac{y^2}{|c|^2} = 1$; these are ellipses where the $y$-semiaxis is twice the $x$-semiaxis, scaling linearly with $|c|$. Slicing along $x = 0$ gives straight lines $z = \pm y$ with slope 1, while slicing along $y = 0$ gives $z = \pm 2x$ with steeper slope 2. Combining these cross-sections, we identify the surface as an elliptic cone opening along the $z$-axis with apex at the origin.

**Show on screen:** The completed-square ellipse form, the cross-section equations showing $b(c) = 2a(c)$, the vertical line slopes, and both sketches.

**If asked to go deeper:** The ratio of the elliptical semiaxes is the square root of the ratio of the quadratic coefficients, $\sqrt{4/1} = 2$, demonstrating that larger coefficients in quadratic forms contract the surface along that coordinate direction.

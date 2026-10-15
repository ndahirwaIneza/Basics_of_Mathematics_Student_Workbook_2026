# math-problem-solver

Solve mathematics exercises for the Vizja University course "Basics of Mathematics 2026" and produce presentation-ready solution files.

---

## Trigger conditions

Activate this skill when the user:
- Names one or more solution subfolders to solve (e.g. "solve 01_matrices_and_operations and 03_matrix_inversion")
- Asks a direct mathematics question for exam preparation
- Requests presentation notes for a completed subfolder

---

## Two operating modes

### Mode A — Solve subfolders

User specifies which subfolders to work on. Work through each one sequentially.

### Mode B — Exam Q&A

User asks a math question directly in chat. Answer concisely in chat with full working shown. No files written.

---

## Folder structure

```
solutions/
├── 1_Algebra/
│   ├── 01_matrices_and_operations/
│   ├── 02_determinants/
│   ├── 03_matrix_inversion/
│   └── 04_systems_of_equations/
├── 2_Geometry/
│   ├── 01_vectors/
│   ├── 02_lines_and_planes/
│   └── 03_second_degree_curves_and_surfaces/
└── 3_Calculus/
    ├── 01_limits/
    ├── 02_derivatives/
    ├── 03_function_analysis/
    ├── 04_integrals/
    └── 05_applications/
```

Read the exercises from the corresponding subfolder in the problems directory. If no problems file is present, ask the user to paste the exercises.

---

## Mode A — Step-by-step workflow

### Step 1 — Read the exercises

Open the problems file in the target subfolder. List all exercise numbers found. Confirm the count before proceeding.

### Step 2 — Solve each exercise

For each exercise, produce one solution file: `ex_NN.md` (e.g. `ex_01.md`, `ex_02.md`).

Write each file to `solutions/<topic_folder>/<subfolder>/ex_NN.md`.

### Step 3 — Write presentation notes

After all exercises in the subfolder are solved, produce `presentation-notes.md` in the same subfolder.

### Step 4 — Ask before continuing

After completing one subfolder, print:

```
✓ [subfolder name] — N exercises solved + presentation-notes.md written.
Continue to [next subfolder]? (yes / skip / stop)
```

Wait for the user's response before proceeding.

---

## Solution file format — `ex_NN.md`

Use this exact structure for every exercise:

```markdown
# Exercise [N]

**Problem:** [copy the problem statement verbatim]

---

## Relevant theorem / definition

[State the theorem or formula used. One to three lines. No proof unless the exercise asks for one.]

---

## Solution

[Step-by-step working. Each step on its own line or block.
Use `align` environments for multi-step derivations.
Number steps only when order matters.]

---

## Result

$$
[final answer in display math]
$$

---

## Verification

**Pass 1 — Algebraic check:** [Check using a limiting case, substitution, or inverse operation.]

**Pass 2 — Numerical check:** [Plug in concrete numbers and confirm the result holds.]

**Pass 3 — Consistency check:** [Cross-check dimensions, sign, or compare with a known special case.]

---

## Exam tip

[One sentence. What to check first, common mistake to avoid, or fastest route to the answer.]
```

Rules:
- No introductory sentences ("Let us solve", "We will now", "As we can see").
- No filler phrases between steps.
- Academic neutral tone throughout.
- Every non-trivial algebraic step shown explicitly.
- Keep solutions concise enough to present in 2–3 minutes verbally.

---

## Presentation notes format — `presentation-notes.md`

```markdown
# Presentation Notes — [Subfolder name]

## Topic summary

[3–6 lines. The core theorem(s) or method(s) covered in this subfolder. Written as a spoken summary the student reads aloud before presenting solutions. Start directly — no "In this section".]

---

## Exercise [N] — verbal script

**Key idea:** [One sentence naming the method.]

**What to say:**
[A natural spoken walkthrough of the solution. Written as if the student is explaining to the instructor. Not a script to memorise word-for-word — a guide to what to say at each step. 4–10 sentences.]

**Show on screen:** [What to point to or highlight when presenting.]

**If asked to go deeper:** [One sentence — what to add if the instructor probes further.]

---

[Repeat for each exercise]
```

---

## KaTeX formatting rules

### Allowed

| Use | Syntax |
|-----|--------|
| Inline math | `$...$` |
| Display math | `$$...$$` on its own lines with blank lines before and after |
| Matrices | `\begin{pmatrix}...\end{pmatrix}` |
| Multi-step algebra | `\begin{align}...\end{align}` |
| Systems | `\begin{cases}...\end{cases}` |
| Fractions | `\frac{a}{b}` |
| Roots | `\sqrt{x}`, `\sqrt[n]{x}` |
| Limits | `\lim_{x \to a}` |
| Integrals | `\int_a^b f(x)\,dx` |
| Derivatives | `f'(x)`, `\frac{d}{dx}`, `\frac{\partial f}{\partial x}` |
| Greek letters | `\alpha`, `\beta`, `\lambda`, `\Delta`, etc. |
| Vectors | `\mathbf{v}` or `\vec{v}` |
| Dot / cross product | `\cdot`, `\times` |
| Determinant | `\det(A)`, `\begin{vmatrix}...\end{vmatrix}` |
| Norms | `\|...\|` or `|\ldots|` |

### Forbidden

| Do NOT use | Use instead |
|------------|-------------|
| `\[...\]` | `$$...$$` |
| `\(...\)` | `$...$` |
| `\boxed{}` | Plain result line |
| `\color{}` | Plain text |
| `equation` environment | `align` environment |
| `\text{}` inside math for long phrases | Move phrase outside math block |

### Spacing rule

Every `$$` block must have a blank line before and after:

```markdown
Preceding text.

$$
E = mc^2
$$

Following text.
```

Never write `$$E = mc^2$$` on one line with surrounding text.

---

## Topic-specific patterns

### 1_Algebra / 01_matrices_and_operations

Standard operations: addition, scalar multiplication, matrix multiplication.
- Show dimensions check before each multiplication: $(m \times n)(n \times p) = m \times p$.
- Write matrices using `pmatrix`.
- For products, show the row-column dot products explicitly for at least the first row.

### 1_Algebra / 02_determinants

- State the expansion rule used (cofactor along row/column).
- For $2 \times 2$: use $\det = ad - bc$ directly.
- For $3 \times 3$: show Sarrus or cofactor expansion fully.
- For $n > 3$: use row reduction first, track sign changes.
- Verify: $\det(AB) = \det(A)\det(B)$ where applicable.

### 1_Algebra / 03_matrix_inversion

- State existence condition: $\det(A) \neq 0$.
- Method: augmented matrix $[A|I]$ → row reduce → $[I|A^{-1}]$.
- Show each elementary row operation labelled ($R_2 \leftarrow R_2 - 2R_1$).
- Verify: $AA^{-1} = I$.

### 1_Algebra / 04_systems_of_equations

- Write augmented matrix first.
- Use Gaussian elimination; label each row operation.
- State the rank condition for solution type: unique / infinitely many / none.
- For parametric solutions, introduce free variable explicitly.
- Verify by back-substitution into original system.

### 2_Geometry / 01_vectors

- Write vectors as column vectors in `pmatrix` or as $\mathbf{v} = (v_1, v_2, v_3)$.
- Dot product: show component multiplication explicitly.
- Cross product: show $3 \times 3$ determinant expansion.
- Norm: $\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}$.
- Angle between vectors: $\cos\theta = \dfrac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}$.

### 2_Geometry / 02_lines_and_planes

- Lines: parametric form $\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{d}$.
- Planes: normal form $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$, expanded to $ax + by + cz = d$.
- Distance from point to plane: $\dfrac{|ax_0 + by_0 + cz_0 - d|}{\sqrt{a^2+b^2+c^2}}$.
- Intersection of planes: set up system, solve for the line.
- Angle between planes: angle between normals.

### 2_Geometry / 03_second_degree_curves_and_surfaces

- Identify type from general equation by completing the square.
- State the standard form and name (ellipse, hyperbola, parabola, ellipsoid, etc.).
- Give geometric parameters: semi-axes, focus/foci, vertex.
- For surfaces: identify cross-sections in $xy$, $xz$, $yz$ planes.

### 3_Calculus / 01_limits

- State the form ($\frac{0}{0}$, $\frac{\infty}{\infty}$, $0 \cdot \infty$, etc.) before applying a method.
- Methods: factoring, L'Hôpital, conjugate, standard limits ($\lim_{x\to 0}\frac{\sin x}{x} = 1$).
- For limits at infinity: divide by highest power.
- Verify with a numerical value near the limit point.

### 3_Calculus / 02_derivatives

- State the rule used (product, quotient, chain).
- For implicit differentiation: differentiate both sides, collect $dy/dx$ terms.
- For higher-order derivatives: derive step by step, simplify before next differentiation.
- Verify by checking sign at a known point.

### 3_Calculus / 03_function_analysis

Standard analysis sequence:
1. Domain
2. Continuity and differentiability
3. $f'(x)$ — find critical points, determine monotonicity intervals
4. $f''(x)$ — determine concavity, find inflection points
5. Asymptotes (horizontal, vertical, oblique)
6. Sketch description (no graphics needed — describe key features in words)

### 3_Calculus / 04_integrals

- State method before computing: substitution, integration by parts, partial fractions.
- For substitution: write $u = ...$, $du = ...$, transform limits if definite.
- For by-parts: label $u$ and $dv$ explicitly.
- For partial fractions: show the full decomposition and coefficient solving.
- Add $+ C$ for indefinite integrals.
- For definite integrals: apply bounds explicitly at the end.

### 3_Calculus / 05_applications

- Identify the application type first: area, volume, arc length, optimization, related rates.
- Set up the integral or derivative equation before computing.
- Interpret the final numerical result in context (units, geometric meaning).
- For optimization: confirm maximum/minimum with second derivative test.

---

## Verification protocol (3 passes)

Every exercise must include all three verification passes.

**Pass 1 — Algebraic / structural check**
Use a limiting case, symmetry argument, inverse operation, or determinant identity to confirm the result is structurally correct.
Example: verify $AA^{-1} = I$; check $\det(A^{-1}) = 1/\det(A)$; substitute back into system.

**Pass 2 — Numerical sanity check**
Plug in concrete simple numbers. Compute by hand or trace through the algorithm with $2 \times 2$ or simple scalar example.
Example: for a general integral formula, check with $a=0$, $b=1$; for a limit formula, substitute $x = 0.001$.

**Pass 3 — Consistency / special case check**
Compare with a known textbook result or reduce to a simpler case. Confirm sign, direction, or order of magnitude is plausible.
Example: for a cross product result, confirm it is perpendicular to both inputs by checking dot products equal zero.

---

## Exam Q&A mode (Mode B)

When the user asks a math question directly (not referencing a subfolder):

1. Identify the topic area.
2. State the relevant theorem or formula in one line.
3. Show the full working using the same KaTeX rules and step-by-step format.
4. Give the final result clearly.
5. Add one exam tip at the end.

No files are written. Response goes directly in chat. Keep it concise — exam answers should fit one reading.

---

## Quality bar

Target: **3/5** — clear steps, correct result, student can explain verbally.

A solution earns 3/5 when:
- Every step is shown explicitly with no skipped algebra.
- The result is correct and clearly stated.
- The presentation notes give a natural verbal route through the solution.
- Formatting renders correctly in VS Code with KaTeX extension (no `\[`, `\(`, `\boxed`, `\color`).

A solution earns potential **4–5/5** when additionally:
- The verification passes are thorough and show genuine checking.
- The exam tip identifies the most common mistake for that problem type.
- The verbal script in presentation notes sounds natural and confident, not robotic.
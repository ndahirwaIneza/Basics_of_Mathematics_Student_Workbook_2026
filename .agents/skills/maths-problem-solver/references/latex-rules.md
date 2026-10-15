# KaTeX formatting rules — quick reference

These rules apply to all math files produced by this skill.
KaTeX is stricter than full LaTeX. When in doubt, test rendering in VS Code with the KaTeX extension before submitting.

---

## Core rule: blank lines around display math

Every `$$` block must have a blank line before and after.

**Correct:**

```markdown
The determinant is computed as follows.

$$
\det(A) = ad - bc
$$

Substituting the values gives...
```

**Wrong — will break rendering:**

```markdown
The determinant is $\det(A) = ad - bc$.
$$
\det(A) = ad - bc
$$
```

---

## Inline vs display

| Situation | Syntax |
|-----------|--------|
| Symbol or short expression in a sentence | `$x^2 + y^2 = r^2$` |
| Equation on its own line | `$$...$$` block with blank lines |
| Multi-step derivation | `$$\begin{align}...\end{align}$$` |
| System of equations | `$$\begin{cases}...\end{cases}$$` |
| Matrix | `$$\begin{pmatrix}...\end{pmatrix}$$` |
| Determinant | `$$\begin{vmatrix}...\end{vmatrix}$$` |
| Augmented matrix | `$$\left[\begin{array}{cc|c}...\end{array}\right]$$` |

---

## align environment

Use for showing algebraic steps. Each line aligned at `&=`:

```
$$
\begin{align}
(x+3)^2 - 9 + (y-1)^2 - 1 &= 0 \\
(x+3)^2 + (y-1)^2 &= 10
\end{align}
$$
```

No numbering needed — KaTeX does not require `\notag`.
Do not use the `equation` environment — use `align` instead.

---

## Matrix syntax

```
$$
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
$$
```

For augmented matrices:

```
$$
\left[\begin{array}{ccc|c}
1 & 0 & 0 & 3 \\
0 & 1 & 0 & -1 \\
0 & 0 & 1 & 2
\end{array}\right]
$$
```

---

## Row operation labels

Write row operations inline with text, not in math mode:

```
Apply $R_2 \leftarrow R_2 - 2R_1$:
```

Or in an align comment:

```
$$
\begin{align}
R_2 &\leftarrow R_2 - 2R_1 \\
R_3 &\leftarrow R_3 + R_1
\end{align}
$$
```

---

## Vectors

Column vector:

```
$$
\mathbf{v} = \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}
$$
```

Row vector inline: $\mathbf{v} = (1, -2, 3)$

Bold for vectors: `\mathbf{v}` not `\vec{v}` (both work in KaTeX; bold is cleaner in text).

Norm: `\|\mathbf{v}\|` — use `\|` not `||`.

---

## Fractions and spacing

Inline fractions: `\frac{a}{b}` — renders small, acceptable in inline.
Display fractions: use `\dfrac{a}{b}` in display mode for better readability.

Thin space before differential: `f(x)\,dx` not `f(x)dx`.

Limits on integrals: `\int_a^b` for inline, `\int\limits_a^b` only if needed (usually not).

---

## Forbidden syntax — will not render in KaTeX

| Forbidden | Reason | Alternative |
|-----------|--------|-------------|
| `\[...\]` | Not KaTeX | Use `$$...$$` |
| `\(...\)` | Not KaTeX | Use `$...$` |
| `\boxed{...}` | Not in KaTeX standard | State result as plain `**Result:**` heading |
| `\color{red}{...}` | Requires plugin | Remove colour entirely |
| `\text{long phrase}` | Breaks layout | Move phrase outside math |
| `\begin{equation}` | Use align instead | `\begin{align}` |
| `\hline` in matrices | Not supported | Use array borders only |
| `\underbrace` with complex sub | Fragile | Simplify or use plain text |
| `\tag{1}` | Not standard KaTeX | Omit equation numbers |

---

## Symbols quick reference

| Symbol | Code |
|--------|------|
| $\leq$ | `\leq` |
| $\geq$ | `\geq` |
| $\neq$ | `\neq` |
| $\approx$ | `\approx` |
| $\infty$ | `\infty` |
| $\in$ | `\in` |
| $\subset$ | `\subset` |
| $\cup$ | `\cup` |
| $\cap$ | `\cap` |
| $\forall$ | `\forall` |
| $\exists$ | `\exists` |
| $\Rightarrow$ | `\Rightarrow` |
| $\Leftrightarrow$ | `\Leftrightarrow` |
| $\partial$ | `\partial` |
| $\nabla$ | `\nabla` |
| $\det$ | `\det` |
| $\text{rank}$ | `\text{rank}` |
| $\mathbb{R}$ | `\mathbb{R}` |
| $\mathbb{Z}$ | `\mathbb{Z}` |

---

## Checklist before saving a solution file

- [ ] Every `$$` block has a blank line before and after
- [ ] No `\[`, `\(`, `\boxed`, `\color` in any block
- [ ] Matrices use `pmatrix` or `vmatrix`
- [ ] Multi-step algebra uses `align`, not `equation`
- [ ] Inline math uses `$...$` only for short expressions
- [ ] Row operations are labelled
- [ ] Three verification passes are present
- [ ] No filler phrases ("Let us", "As we can see", "Now we")
- [ ] Result is stated clearly after the working
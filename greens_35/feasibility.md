# green 35: can the source proofs be formalized?

the question for each statement in `35.lean` is whether the source paper's proof can be written out in Lean
as it stands, or whether it relies on unproved claims (computer searches, imported lemmas) that would
need to become axioms.

normalisation: `35.lean` uses functions on `[0,1]`. all the papers use `[-1/4,1/4]`, where every
constant is twice the `35.lean` constant. `verify_constants.py` recomputes the numbers quoted below.

## summary

| statement in `35.lean` | source | type of proof | verdict |
|---|---|---|---|
| `variants.c_inf_upper` (≤ 0.7549) | MV10 §4 + appendix | one explicit step function, n = 208 | **formalizable, no axioms**. finite rational arithmetic plus one general lemma |
| `variants.c_inf_upper_ae25` (≤ 0.75265) | AE25 App. B.1 | step function, n = 600 | **formalizable, no axioms**. the data is not in the paper (see below) |
| `variants.c_inf_upper_ggtw25` (≤ 0.7516) | GGTW25 §6.2 | step function, n = 1319 | **formalizable, no axioms**. same caveat about the data |
| `variants.c_2_lower` (≥ √(4/7)) | Gr01 §5 | Fourier analysis + Hölder + explicit numerics | **formalizable, no axioms**, but the paper proves a *discrete* theorem. see the decision in §2 |
| `variants.c_inf_lower` (≥ 0.64) | CS17 | elementary reduction + ~20,000 CPU-hour GPU search | **not formalizable as written.** the search must become an axiom, and the paper does not specify it precisely enough to state that axiom faithfully |
| `variants.c_inf_lower_young` | none (textbook) | Hölder `‖g‖₂² ≤ ‖g‖₁‖g‖_∞` with `‖f⋆f‖₁ = 1` | trivial. it is Hölder, not Young (docstring misnomer) |
| `green_35.upper` (open) | — | — | **already provable from GGTW25's own construction.** see §5 |
| `green_35.lower` (open) | — | — | **first disjunct already provable from Green's own proof.** see §5 |

## 1. upper bounds: MV10, AE25, GGTW25

### the proof

each upper bound is one explicit nonnegative step function `f` with `n` equal steps. the proof is
"compute `‖f⋆f‖_∞`". for step heights `a₀,…,a_{n-1}` on `[-1/4,1/4]`, `f⋆f` is continuous and
piecewise linear with knots on the cell grid. its value at the knot `k` is proportional to
`b_k = Σ_{i+j=k} a_i a_j`. so

    ‖f⋆f‖_∞ / (∫f)² = 2n · max_k b_k / (Σ a)²       (MV10 §4; the same formula is AlphaEvolve's scorer)

### checked in exact rational arithmetic

the decimal literals from the sources are treated as exact rationals:

| construction | n | score on [-1/4,1/4] | on [0,1] | `35.lean` bound | margin |
|---|---|---|---|---|---|
| MV10 (`data/mv10_208.txt`) | 208 | 1.5097202 | 0.7548601 | 0.7549 | 4.0e-5 |
| AE25 (`data/ae25_600.txt`) | 600 | 1.5052940 | 0.7526470 | 0.75265 | 3.0e-6 |
| GGTW25 (`data/ggtw25_1319.txt`) | 1319 | 1.5031636 | 0.7515818 | 0.7516 | 1.8e-5 |

all three bounds hold. MV10's coefficients are printed to only 8 decimals, and the printed values
still give 1.50972, matching the paper.

**data provenance.** neither AlphaEvolve paper prints its step function. AE25 says "see the results
colab" and GGTW25 says "see the Repository of Problems". I extracted the heights from
`google-deepmind/alphaevolve_repository_of_problems` (commit `8f44745`,
`experiments/autocorrelation_problems/autocorrelation_problems.ipynb`): cell 46 for AE25 and cell 60
for GGTW25. the notebook also has 1.5040, 1.5036, 1.5035 and 1.5033 constructions; none beats 1.5032.
licence: CC-BY 4.0, attribution kept in the file headers. this external data is part of "the existing
proof" for AE25 and GGTW25.

### Lean plan

1. a general lemma, proved once: for a step function `f = Σ a_j · 1_[x_j, x_{j+1})` on `[0,1]` with
   `n` equal cells, `f ⋆ f ≤ n · max_k b_k / (Σa)²` everywhere (after normalising `∫f = 1`).
   - `1_I ⋆ 1_J` for intervals `I`, `J` of equal length is a tent function. this follows from
     `volume (I ∩ (x - J))`.
   - convolution is bilinear over finite sums (`convolution_add` etc.; the integrability side
     conditions are trivial here).
   - on each knot interval every tent is affine, so `f⋆f` is a convex combination of two knot
     values. alternatively, bound each tent by its peak value spread over its two neighbouring
     knots.
   - `eLpNorm_le_of_ae_bound` / `eLpNormEssSup_le_of_ae_bound` turn the pointwise bound into the
     `eLpNorm ∞` bound. `IsUnitIntervalDensity` (integrable, nonnegative, support ⊆ [0,1],
     integral 1) is routine.
2. per construction, a decidable statement `∀ k, n · b_k · 10^? ≤ thr · (Σa)²` over `ℕ`, after
   scaling the decimals to integers.
   - MV10: about 43k products of 8-digit integers. `decide` in the kernel (GMP-accelerated `Nat`)
     should be fine.
   - GGTW25: about 870k products of roughly 20-digit integers. kernel `decide` may be slow. it is
     untested; split the `2n-1` knot checks into chunks if needed.
   - `native_decide` would be instant. formal-conjectures uses it in some OEIS files, but it adds
     the `Lean.ofReduceBool` axiom, so decide whether that is acceptable.
   - rounding the heights is not needed: the inputs are exact decimals.

the general lemma is the only real formalization work. it is a moderate amount of measure theory with
no dependency on anything missing from Mathlib.

## 2. `c_2_lower`: Green 2001 §5

### what the paper actually proves

Theorem 13 is **discrete**: for `f : {1,…,N} → ℝ` with `Σ f = N`, `M(f) = Σ_x (f*f)(x)² ≥ (4/7) N³`
for all sufficiently large `N`. the proof:

- embed in `ℤ_{2N+v}`
- take the test function `U = 1` on `[0,1)` and `1 − p(x−1)` on `[1,2)`; discretize it to `G` and
  smooth it to `H = (4/v)² G*(I*I)`
- `Σ f(x) H(x+v/4) = N`, then Parseval and the triangle inequality give (19)
- Lemmas 7–10 approximate `Ĥ(r)` by `(N+v) p̃(πr)` and bound it for large `|r|`
- Hölder with exponents `(4, 4/3)` gives `E(X) ≥ γ(p) N⁴ (1 − error)`
- take `v = N^{6/7}`, `X = N^{3/7}`, and the explicit `p(x) = 5/2 − 40(x−1/2)⁴`, for which
  `γ(p) > 1/7`

`35.lean` states the **continuous** inequality `‖f⋆f‖₂ ≥ √(4/7)`. the paper never states it and
never derives it. so whichever route is taken, something is added that is not in the paper.
**[decide]** which route:

- **route A, discrete-faithful.** formalize §5 as written: `ZMod (2N+v)` DFT, the smoothing `H`,
  Lemmas 7–10 with explicit constants in place of "C depending on p", and the `N → ∞` limit.
  - then prove a discrete-to-continuous bridge, which is not in the paper. smooth `f` by an
    approximate identity, use Young (`‖(f⋆f)⋆k⋆k‖₂ ≤ ‖f⋆f‖₂`), take Riemann sums of the continuous
    convolution, and rescale the support `[−ε, 1+ε] → [0,1]`.
  - this is the larger route. most of its bulk is error-term bookkeeping that the continuous
    statement does not need.
- **route B, the continuous transcription of the same proof** (recommended). it is Green's argument
  with the discretization removed. Green himself notes in the sketch of Lemma 30 that without
  discretization "we have not introduced any smoothing device".
  1. work on `AddCircle 2`. since `supp f ⊆ [0,1]`, `supp f⋆f ⊆ [0,2]`, so the circle convolution
     is the line convolution and `‖f⋆f‖₂² = 8 Σ_r |c_r(f)|⁴`. if `f⋆f ∉ L²` the bound is trivial.
     - needs: Parseval (`tsum_sq_fourierCoeff`) and `c_r(f⋆f) = 2 c_r(f)²`.
     - Mathlib has **no** convolution theorem for `fourierCoeff`. prove it directly with Fubini.
  2. the specific `p` has `p(0) = p(1) = 0`, so `U` is continuous and piecewise polynomial. hence
     `Σ|Û(r)| < ∞` and `U` equals its Fourier series uniformly (`hasSum_fourier_series_of_summable`).
     integrating against `f ∈ L¹` gives `1 = ∫ fU = Σ_{r≠0} c_r(f) conj(Û(r))`, since `Û(0) = 0`.
     this replaces (19) and all of Lemmas 7–10.
  3. compute `Û(r)` explicitly, using (26) for `|p̃(πr)|`. that means five integrations by parts,
     or an explicit antiderivative with `integral_eq_sub_of_hasDerivAt`. I checked (26) symbolically
     for r = 1…6.
  4. Hölder on `tsum` (`Real.inner_le_Lp_mul_Lq_tsum_of_nonneg`, exponents 4 and 4/3) gives
     `Σ_{r≥1} |c_r|⁴ ≥ γ(p)/32` (with these normalisations), which gives `‖f⋆f‖₂² ≥ (1+γ)/2`.
  5. numerics: `γ > 1/7` iff `Σ_{r≥1} |p̃(πr)|^{4/3} < 14^{1/3}`.
     - the sum is 2.4095472 and `14^{1/3}` = 2.4101423, a slack of **5.95e-4** (relative 2.5e-4)
     - a rigorous proof needs a truncation at a few hundred terms plus a tail bound by `ζ(8/3)`-type
       integrals, π bounds (`Real.pi_gt_d20`/`pi_lt_d20`), and rational upper bounds on `x^{4/3}`
       certified by cubing (`y³ ≥ x⁴`)
     - this is tedious but standard. it can be automated with a generated certificate and checked
       with `norm_num`, or with `decide` on rationals.

no axioms are needed either way. route B is a sizeable but well-scoped project. every ingredient
except the circle convolution theorem is in Mathlib.

## 3. `c_inf_lower`: Cloninger–Steinerberger 2017

### the mathematical part is easy

- Lemma 1: averages over cells, `supp(f_i⋆f_j) ⊆ I_i + I_j`, Fubini, and `∫_J f⋆f ≤ |J| ‖f⋆f‖_∞`
- Lemma 2: a rounding net for the simplex
- Lemma 3: discretization error `2/m + 1/m²`

all three are elementary and formalizable.

### the computation is not

the actual bound is a branch-and-bound search. it starts at `n = 3`, refines dyadically down to
`B_{24,50}`, runs about 20,000 CPU-hours on GPUs, and uses an unspecified "refined" pruning
inequality. this blocks a faithful formalization in three ways:

1. **scale.** a Lean kernel cannot redo 20,000 CPU-hours. `native_decide` would be off by many
   orders of magnitude too.
2. **under-specification.** the paper says the refined bound (eq. after "refinedLowerBound") was
   "quite a bit more effective". that suggests the plain Lemma-3 threshold does not by itself rule
   out every case. so the finite claim that was actually checked is never stated. the child count
   `N = ∏_{i=1}^n (1 + m b_i)` is written for `n` entries, but there are `2n`, and it suggests a
   mass-splitting normalisation that differs from Lemma 3's height normalisation (`Σ b_i = 4n`).
3. **a gap in the multi-scale argument.** pruning at a coarse level `n` and then refining only the
   survivors is valid only if, for every `f`, its rounding in `B_{2n,m}` is a child of its rounding
   in `B_{n,m}`. the rounding of Lemma 2 does not obviously have this property: halving cells with
   a fixed grid `1/m` breaks the parent sum. the paper does not address it. this is probably
   fixable, but the fix would be ours, not theirs.

I found no published code: the paper links none, and a web search turned up none.

**verdict.** formalize Lemmas 1–3. state the search result as an explicit axiom, which first requires
reconstructing what was checked (ideally from the authors' code). this is the "significant axiom that
also requires proof" case. its correctness can only be established by re-running a large
computation, and that computation is only described loosely.

minor typos in CS17, irrelevant to the verdict:

- Lemma 1 ranges `2 ≤ ℓ ≤ 2n`, `−n ≤ k ≤ n−ℓ` vs `2 ≤ ℓ ≤ 4n`, `−2n ≤ k ≤ 2n−ℓ` in the proof
- `I_i + I_k` should read `I_i + I_j`
- the final display drops the `−2` in the index range and changes the prefactor

## 4. other material

- **MV10 lower bound 1.2748** (0.6374 on [0,1]). this is not one of the `35.lean` statements, and
  formalizing it would be hard:
  - it relies on Martin–O'Bryant's Lemmas 3.1–3.4, which are not in our files
  - it needs Bessel `J₀`, which Mathlib lacks, and an imported numerical constant `‖K‖₂² < 0.5747/δ`
  - it needs a rigorous global minimum of a 119-term cosine polynomial on `[0,1/4]`
- **Green §§4, 6–11** (B_h[g] sets) are not needed for problem 35.

## 5. statement-fidelity problems in `35.lean`

`35.lean` is byte-identical to upstream `formal-conjectures/FormalConjectures/GreensOpenProblems/35.lean`
(checked against commit `a924684`). so these findings are worth reporting upstream as well.

1. **`green_35.upper` is not open as stated.** it asks for `ub ∞ < 0.7516`.
   - GGTW25's own 1319-step function gives `c ∞ ≤ 0.7515818… < 0.7516`. the threshold is the
     *rounded* score 1.5032/2, but the true score is 1.5031636.
   - with `ub := fun _ ↦ 0.75159` (`⊤` off `∞`), the open theorem follows from the §1 lemma plus
     one computation.
   - fix: require `ub ∞ < 0.7515818` (or the exact rational), or state "strictly below the best
     known construction".
   - a web search also turned up a reported 1.50286 (0.75143), possibly from ThetaEvolve
     (arXiv 2511.23473). that is unverified, but if real it beats any threshold near 0.7516 too.
2. **`green_35.lower` is not open as stated.** its first disjunct asks for `lb 2 > √(4/7)`.
   - Green's own `p` gives `γ = 0.1429630 = 1/6.99482 > 1/7`, so his argument proves
     `c(2)² ≥ (1+γ)/2 = 0.5714815 > 4/7 = 0.5714286`. the 4/7 in Theorem 13 is Green rounding
     `γ` down to `1/7`.
   - so route B in §2, without the rounding, proves the "open" statement.
   - fix: compare against `√((1+γ(p))/2)` with Green's `p`, or a rational just above 0.57148.
     better still, cite the best published `c(2)` bound if there is a later one; I did not search
     for one.
   - the second disjunct `0.64 < lb ∞` has no slack. CS17 proves exactly 1.28.
3. `c_inf_lower_young`: the inequality is Hölder (or log-convexity of `L^p` norms), not Young's
   convolution inequality. it is a docstring nit.
4. the other docstrings check out: MV10 1.50972 → 0.75486 and AE25 1.5053 → 0.75265 are consistent
   with the exact scores above.

## 6. the `green2001.tex` transcription

`green2001.pdf` is a pdfTeX document (Green's own 30-page typeset version, 2013) with a real text
layer, not a scan. I compared §5, the only section problem 35 depends on, against `pdftotext`
output. statements, displays (14)–(29) and Theorems 6, 11, 12 and 13 match. **a second conversion
is not needed** for this purpose. §§4 and 6–11 were read but not line-checked.

errors present in the original, not introduced by the conversion:

- "γ(p) ≈ 1/6.9994" should be ≈ 1/6.9948. `S1` and `S2` are correct to the printed digits, and the
  conclusion `γ > 1/7` is unaffected.
- (28) and (29) sum over "r ≥ 0". this should be `r ≥ 1`, since the `r = 0` term diverges.
- "I*I is supported in {−v/4, v/4}" means the interval `[−v/4, v/4]`.
- §8 cites "Proposition 12". it means Theorem 12.

## 7. suggested order

1. the step-function lemma and the MV10 instance. it is the smallest end-to-end result and is
   reused by AE25 and GGTW25.
2. AE25 and GGTW25 instances. this tests kernel `decide` at n = 600 and n = 1319.
3. `c_inf_lower_young`, a warm-up for the `eLpNorm` API.
4. Green, route B (pending the decision in §2).
5. CS17: Lemmas 1–3 plus a stated axiom, only if a precise version of the search can be pinned down.
6. separately, report the §5 findings upstream to formal-conjectures.

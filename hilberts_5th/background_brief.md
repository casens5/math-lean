# brief: background results behind van den Dries–Goldbring's proof of Hilbert's 5th problem

## context

this repo (`/home/user/math-lean`) studies whether AI can turn math papers into Lean 4 proofs.
the target is `hilbert_fifth_problem` (and, through it, `hilbert_smith_conjecture.variants.riemannian`)
in `hilberts_5th/5.lean`, which is copied verbatim from google-deepmind/formal-conjectures
(`FormalConjectures/HilbertProblems/5.lean`). the Lie group notion there is
`AdmitsLieGroupStructure` / `LieGroupPresentation` from
`FormalConjecturesForMathlib/Geometry/Manifold/LieGroupPresentation.lean`: a continuous group
isomorphism onto a Hausdorff, real-analytic (`ω`) Lie group modelled on `EuclideanSpace ℝ (Fin n)`,
with **no** second-countability assumption (discrete groups count as 0-dimensional Lie groups).

the proof source is van den Dries–Goldbring, *Hilbert's 5th problem*, Enseign. Math. 61 (2015)
— transcriptions at `hilberts_5th/vandendries2016.tex` and `hilberts_5th/vandendries2016_2.md`,
original at `hilberts_5th/vandendries2016.pdf`. the paper proves the Gleason–Yamabe / Montgomery–Zippin
results itself, but treats the following five results as known background:

1. a weak Peter–Weyl theorem for compact groups (used in §4, Theorem 4.1)
2. Pontryagin's result that locally euclidean (or NSS) abelian locally compact groups are Lie
   (used in the intro sketch step (4) and Corollary 6.10)
3. Kuranishi's extension theorem: if `G` has a commutative closed normal subgroup `N` with
   `N` and `G/N` Lie, then `G` is Lie (intro, Corollary 6.10)
4. Cartan–von Neumann: a continuous injective homomorphism `G/N → GLₙ(ℝ)` makes `G/N` a Lie group
   (intro step (4), Corollary 6.10)
5. basic Lie theory: 1-parameter subgroups ↔ tangent vectors at the identity, and the exponential
   map is an analytic isomorphism from a neighbourhood of 0 onto a neighbourhood of 1
   (intro, "the case of Lie groups"; used implicitly wherever `G` is already known to be Lie)

## your task

for **each** of the five results, produce:

### a. the exact statement the paper needs
- quote the passage(s) of `vandendries2016.tex` where it is invoked (with section / lemma number),
  and state the result precisely, with every hypothesis: Hausdorff? locally compact? connected?
  σ-compact? real or complex representations? finite-dimensional? which notion of "Lie group"?
- say whether the paper needs the full classical theorem or a weaker special case, and which.
- watch for subtleties. example: in (4) the image of `G/N` in `GLₙ(ℝ)` need not be closed and the
  topology of `G/N` can be finer than the subspace topology (e.g. ℝ with the discrete topology), so
  the relevant theorem may not be the closed-subgroup theorem itself; work out exactly which
  version applies here and what it depends on (e.g. an open-mapping theorem for σ-compact groups).

### b. Lean / Mathlib status
- shallow-clone current mathlib4 (`git clone --depth 1 --filter=blob:none` with sparse checkout of
  the relevant directories) into your scratchpad and grep it. do **not** install a Lean toolchain or
  build Mathlib; the disk allowance is too small.
- for each result, report: fully in Mathlib (give declaration names and file paths), partially
  (what exists, what is missing), or absent. relevant areas include `MeasureTheory.Measure.Haar`,
  `Topology.Algebra.*`, `Analysis.Normed*.Exponential`, `Geometry.Manifold.Algebra.LieGroup`,
  `Algebra.Lie`, `RepresentationTheory`, Pontryagin duality (`Topology.Algebra.PontryaginDual`),
  matrix exponential.
- also check google-deepmind/formal-conjectures (a clone may already exist at
  `/tmp/claude-0/-home-user-math-lean/94011373-2ecf-5b3d-8422-74a77bd37347/scratchpad/fcrepo`;
  otherwise clone it) and search the web for other Lean formalizations (Lean Zulip, GitHub
  projects, blueprint projects). cite links.
- where no formalization exists, draft a Lean 4 statement in the conventions of `5.lean`
  (`IsTopologicalGroup`, `LocallyCompactSpace`, `T2Space`, `AdmitsLieGroupStructure`, etc.),
  ending in `:= by sorry`. clearly mark these as **uncompiled drafts**, and check every
  identifier you use against the Mathlib source you cloned.

### c. sources that prove it
- the original paper(s), with full bibliographic data, DOI / JSTOR / arXiv links.
- at least one modern, readable proof (textbook chapter or survey). candidates to check include
  Tao, *Hilbert's Fifth Problem and Related Topics* (AMS GSM 153, draft on his blog);
  Montgomery–Zippin, *Topological Transformation Groups*; Kaplansky, *An Introduction to
  Differential Algebra* / *Lie Algebras and Locally Compact Groups*; Hofmann–Morris;
  Hilgert–Neeb, *Structure and Geometry of Lie Groups*; Knapp; Folland, *A Course in Abstract
  Harmonic Analysis*; Duistermaat–Kolk. use vandendries2016's own bibliography as a starting point.
- for each source: is it freely available (and where)? how self-contained is the proof? what
  prerequisites does it rely on? rate it as a formalization source (low / medium / high) with a
  one-paragraph justification.
- verify citations on the web; do not cite from memory. if you cannot confirm a reference, say so.

### d. hidden dependencies
while reading, note any **other** facts the paper uses without proof (e.g. invariance of domain /
Brouwer dimension theory, needed for "locally euclidean ⇒ bounded in dimension" in Corollary 7.7
and for matching the chart dimension `n` in the Lean statement). list them with the same a/b/c
treatment, briefly.

## output

write the report to `hilberts_5th/background_results.md`:
- a summary table first: result | precise form needed | Mathlib status | best proof source |
  formalization difficulty
- then one section per result with a/b/c, then a section for hidden dependencies (d)
- end with a recommended order of attack for formalizing the full chain toward
  `hilbert_fifth_problem`, and which pieces could reasonably be left as `sorry`'d axioms.

state clearly whenever something is uncertain or unverified. do not commit or push; the parent
session will handle git.

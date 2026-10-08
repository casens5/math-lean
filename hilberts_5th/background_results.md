# Background results behind van den Dries–Goldbring's proof of Hilbert's 5th problem

Report for `hilbert_fifth_problem` in `hilberts_5th/5.lean`. The source is L. van den Dries and
I. Goldbring, *Hilbert's 5th problem*, Enseign. Math. (2) 61 (2015), 3–43,
doi:[10.4171/LEM/61-1/2-2](https://doi.org/10.4171/LEM/61-1/2-2). Below it is "the paper" or [vdDG].
Section and lemma numbers refer to `hilberts_5th/vandendries2016.tex`.

**What was checked, and how.**

- **Mathlib.** A sparse clone of `leanprover-community/mathlib4` master at commit `49fd9dee36e7` (2026-10-08), searched with grep. No Lean toolchain was installed and nothing was built.
- **formal-conjectures.** A fresh full clone of `google-deepmind/formal-conjectures` at `2d9a2f6a2fe7` (2026-10-08). It pins Lean `v4.33.1` and Mathlib rev `0df444a360ea`. `5.lean` and `LieGroupPresentation.lean` are byte-identical to the copies here.
- **TauCeti.** A clone of [TauCetiProject/TauCeti](https://github.com/TauCetiProject/TauCeti) at `9345f0100d16` (2026-10-08). It pins Lean `v4.35.0-rc3` and Mathlib rev `0f64d30a9a45`. This is an AI-written library incubated by the Lean FRO. It turned out to hold most of the relevant formal material. I found no `sorry` in the directories I inspected.
- **Web.** Most article and blog hosts were blocked by the session's egress proxy: ams.org, numdam, arXiv, Wikipedia, terrytao.wordpress.com, JSTOR, Springer and Zulip. Only GitHub was reachable. Citations below were therefore checked through web-search result snippets, which show publisher or catalogue records. Anything I could only see second-hand is marked **(unverified)**.
- **Drafts.** Every Lean statement marked **UNCOMPILED DRAFT** has had its identifiers grepped against the Mathlib clone above, or against formal-conjectures for `AdmitsLieGroupStructure` and `LieGroupPresentation`. None has been compiled.

---

## 0. Summary table

| # | Result | Precise form the paper needs | Mathlib status (master 2026-10-08) | Best proof source | Formalization difficulty |
|---|---|---|---|---|---|
| 1 | Weak Peter–Weyl | For a **compact Hausdorff** group `G` and `a ≠ 1`, there is a continuous homomorphism `G → GLₙ(ℝ)` not killing `a`. Real, finite-dimensional, no countability. Point separation only; L² completeness is not needed. | **Partial.** Haar measure and the spectral theorem for compact self-adjoint operators are present; no Peter–Weyl. **Fully done in TauCeti**: `TauCeti.exists_contRepresentation_apply_ne` (with `𝕜 = ℝ` allowed). | Tao, GSM 153, Ch. 4 (= blog 254A Notes 3). Folland, *Course in Abstract Harmonic Analysis*, Ch. 5. Hofmann–Morris, Ch. 3. | **Low** if TauCeti is ported or bridged. Medium–high from scratch. |
| 2 | "Pontryagin": abelian NSS ⇒ Lie | A **commutative**, closed (hence locally compact Hausdorff) group `N` with NSS is Lie. In the paper's context §6 already gives `N` a finite-dimensional `𝔏(N)` with `exp` a local homeomorphism, so only the *elementary* consequence is needed: for abelian `N`, `exp` is a continuous homomorphism, which gives exp-charts. No duality and no structure theorem. | **Absent.** `PontryaginDual` is defined, with "dual of compact is discrete"; there is no duality theorem and no LCA structure theorem. | Given §§5–6: a half-page argument (§2(a) below). Classical: Pontryagin 1934 (Ann. Math. 35); Morris, LMS LN 29; Hewitt–Ross I (9.8). | **Low–medium** given §§5–6 of the paper. High for the classical theorem from scratch. |
| 3 | Kuranishi extension | Only the **central** case is used: `G` connected, locally compact, NSS; `N = Z(G)` closed central; `N` and `G/N` Lie ⇒ `G` Lie. The paper states it for commutative normal `N`. | **Absent.** Not in TauCeti either. | Tao, GSM 153, §2.6 "Central extensions of Lie groups, and cocycle averaging" (Thm 2.6.1) (unverified content). Gleason 1951 Thm 3.1; Iwasawa 1949. Kuranishi 1950 (PAMS 1). | **High.** Needs local cross-sections, cocycles and analytic smoothing. Best left as a `sorry`'d axiom first. |
| 4 | Cartan / von Neumann | A **locally compact Hausdorff** `H` (here `H = G₀/Z(G₀)`) with a **continuous injective** homomorphism `H → GLₙ(ℝ)` is Lie. The image need **not** be closed and the topology of `H` can be finer than the subspace topology, so the closed-subgroup theorem does **not** apply directly. The right theorem is "von Neumann's theorem" (Tao 254A Notes 2, Thm 4): locally compact + injective continuous hom into a Lie group ⇒ Lie, proved by a *local* Cartan theorem. It needs no σ-compactness. In the paper's setting there is a third, lighter route through §6 (see §4(a)). | **Partial.** `NormedSpace.exp` (analytic, strict derivative at 0), the analytic inverse function theorem, `LieGroup … ω` on units of a Banach algebra, and the open mapping theorem for σ-compact groups are present. The closed-subgroup theorem, the von Neumann theorem and 1-ps classification are absent. **TauCeti** has the closed-subgroup theorem and 1-ps classification for C^∞ Lie groups, but not von Neumann's theorem. | Tao 254A Notes 2 / GSM 153 Ch. 3 (Thm "von Neumann"). Tao blog 2011-05-27. von Neumann 1929 (Math. Z. 30). Cartan 1930. | **Medium** by the §6 route, given §§5–6 plus Mathlib's matrix exp. Medium–high standalone. |
| 5 | Basic Lie theory (1-ps ↔ `T₁G`, `exp` an analytic local iso) | For a Hausdorff, **real-analytic** Lie group modelled on `ℝⁿ` with **no second countability**: continuous 1-ps are analytic and are `t ↦ exp(tv)` for a unique `v ∈ T₁G`; the paper's `+` on `𝔏(G)` (Trotter limit) is vector addition in `T₁G`; and `exp` is an analytic diffeomorphism near 0. It is used only inside the proofs of 2–4; the logical chain of the paper never needs it for a general Lie group. | **Partial.** `GroupLieAlgebra` (tangent space at 1 with bracket), `LieGroup`, global integral curves under a uniform-time hypothesis, matrix / Banach-algebra exp. No Lie-group exponential and no 1-ps classification. **TauCeti** has `lieExp`, `mulInvariantExp`, 1-ps classification, the local inverse, Trotter, BCH, the closed-subgroup theorem and automatic smoothness, but **only C^∞, not ω**. | Hilgert–Neeb, *Structure and Geometry of Lie Groups* (2012), Chs. 9–10. Tao GSM 153, Ch. 2. Duistermaat–Kolk, *Lie Groups*. | **Medium.** The C^∞ part largely exists in TauCeti; the ω upgrade is open. |
| d | Hidden dependencies | Invariance of domain / dimension; existence of κ-rich nonstandard extensions; "open Lie subgroup ⇒ Lie"; Riesz; Haar; ω versus C^∞; and others (§6). | Mixed; see §6. Invariance of domain is **absent** from master; Mathlib PR #36770 is unmerged and conditional on Brouwer. κ-saturation is **absent**. | Tao 2011 blog "Brouwer's fixed point and invariance of domain…"; Hatcher §2.B. | Invariance of domain: **medium–high**. Saturated ultrapowers: **high**, so avoid NSA. |

---

## 1. Weak Peter–Weyl theorem

### 1a. Exact statement the paper needs

**Where it is used.**

- Introduction: "Von Neumann used it [Haar measure] to extend the Peter-Weyl theorem for compact Lie groups to all compact groups … (In our treatment of H5 we use a weak form of this extended Peter-Weyl theorem.)"
- **Theorem 4.1** (§4): "Let `G` be compact and `U` an open neighborhood of 1 in `G`. Then there is a continuous injective group morphism `G/N → GLₙ(ℝ)` for some `n` and some closed normal subgroup `N` of `G` contained in `U`." Its proof begins: "The Peter-Weyl theorem yields for any `a ≠ 1` in `G` a continuous group morphism `φₐ : G → GL_{nₐ}(ℝ)` that does not have `a` in its kernel `Nₐ`." It then uses compactness of `G \ U` to take finitely many `a`'s and the direct sum of the `φₐ`.
- **Corollary 4.2** follows from Theorem 4.1 together with the NSS fact (5) of §2: "continuous `φ : G → H` injective near 1 and `H` NSS ⇒ `G` NSS" for `G/N → GLₙ(ℝ)`, and "`GLₙ(ℝ)` has NSS".
- Corollary 4.2 is used in **Lemma 5.4**, applied to the compact subgroup `H = G_U(Q)` of `G`. Lemma 5.4 is the engine for Corollary 5.5, Lemmas 5.6–5.9, Theorem 5.8, Lemma 5.10 (vector-space structure on `𝔏(G)`), Lemma 6.5 and Lemma 7.1. So it sits under the whole NSS ⇒ Lie and locally Euclidean ⇒ NSS chain.
- Theorem 4.1 is also used directly in Lemma 8.1 (Yamabe's theorem). That is **not** needed for `hilbert_fifth_problem`.

**Precise form.** Let `G` be a compact Hausdorff topological group. The paper includes Hausdorff in "compact" (§1: "We include being hausdorff as part of compactness"). For every `a ∈ G` with `a ≠ 1` there exist `n ∈ ℕ` and a continuous group homomorphism `φ : G → GLₙ(ℝ)` with `φ(a) ≠ 1`.

- No connectedness, metrizability or second countability is assumed. The compact groups `G_U(Q)` produced in §3 are arbitrary compact subgroups of an arbitrary locally compact group.
- Representations are **real** and finite-dimensional. The usual complex unitary version gives this through the realification `U(n) ↪ GL_{2n}(ℝ)`.
- Only **point separation** by finite-dimensional representations is needed. The full Peter–Weyl theorem (matrix coefficients dense in `C(G)` or complete in `L²(G)`) is not, although every known proof of point separation goes through density of representative functions.
- Theorem 4.1 is a formal consequence. It also needs that the kernels are closed, which is automatic, and that `G \ U` is compact, which holds because `U` is open.
- Subtlety: `G/N → GLₙ(ℝ)` is a continuous injection from a compact group into a Hausdorff group, hence a closed embedding. Unlike result 4, there is no topology issue here. The paper does not even need the embedding, only NSS of `G/N`.

### 1b. Lean / Mathlib status

**Mathlib master: partial (ingredients only).**

- Haar measure: `MeasureTheory.Measure.haarMeasure`, `MeasureTheory.Measure.haar`, `isHaarMeasure_haarMeasure`, `haarMeasure_unique` in `Mathlib/MeasureTheory/Measure/Haar/Basic.lean`; `MeasureTheory.integral_mul_left_eq_self` in `Mathlib/MeasureTheory/Group/Integral.lean`.
- Compact operators and the spectral theorem for compact self-adjoint operators: `ContinuousLinearMap.orthogonalComplement_iSup_eigenspaces_eq_bot` and `ContinuousLinearMap.finite_dimensional_eigenspace` in `Mathlib/Analysis/InnerProductSpace/Spectrum.lean`. The Fredholm alternative is in `Mathlib/Analysis/Normed/Operator/Compact/FredholmAlternative.lean`.
- Continuous representations: `ContRepresentation` in `Mathlib/RepresentationTheory/Continuous/Basic.lean`.
- `Mathlib/RepresentationTheory/` has no Peter–Weyl theorem; grep for "Peter" or "Weyl" finds nothing relevant.

**formal-conjectures:** nothing.

**TauCeti: done, and sorry-free in the inspected files.**

- `TauCeti/RepresentationTheory/Compact/RepresentativeDensity.lean`:
  ```lean
  variable {𝕜 G : Type*} [RCLike 𝕜] [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
    [CompactSpace G]
  theorem exists_contRepresentation_apply_ne [T1Space G] (x y : G) (hxy : x ≠ y) :
      ∃ (n : ℕ) (π : ContRepresentation 𝕜 G (EuclideanSpace 𝕜 (Fin n))),
        Continuous π ∧ π x ≠ π y
  ```
  With `𝕜 = ℝ`, this is exactly the needed statement, up to converting `EuclideanSpace ℝ (Fin n) →L[ℝ] …` into `GL (Fin n) ℝ`. The file also has `TauCeti.dense_representativeSubmodule` (uniform density of representative functions) and `TauCeti.exists_isRepresentative_apply_ne`.
- The full L² Peter–Weyl theorem is `TauCeti.peterWeylBasis` / `TauCeti.stdPeterWeylBasis` (a `HilbertBasis` of `L²(G)`) in `TauCeti/RepresentationTheory/Compact/PeterWeyl.lean`.
- Caveat: TauCeti pins a newer Lean and Mathlib (`v4.35.0-rc3`) than formal-conjectures (`v4.33.1`). Using it means porting the files or bumping formal-conjectures.
- On the web I also found TauCeti PR [#13317](https://github.com/TauCetiProject/TauCeti/pull/13317) "Peter-Weyl block projections", which belongs to the same effort. I found no other Lean formalization of Peter–Weyl.

**UNCOMPILED DRAFT** (bridging statement in the conventions of `5.lean`):

```lean
open scoped Topology in
/-- Weak Peter–Weyl, real form (used in [vdDG, Thm 4.1]). UNCOMPILED DRAFT. -/
theorem exists_continuousMonoidHom_GL_ne_one {G : Type*} [Group G] [TopologicalSpace G]
    [IsTopologicalGroup G] [CompactSpace G] [T2Space G] {a : G} (ha : a ≠ 1) :
    ∃ (n : ℕ) (φ : G →ₜ* GL (Fin n) ℝ), φ a ≠ 1 := by
  sorry

/-- [vdDG, Theorem 4.1]. UNCOMPILED DRAFT. -/
theorem exists_closed_normal_le_and_injective_GL {G : Type*} [Group G] [TopologicalSpace G]
    [IsTopologicalGroup G] [CompactSpace G] [T2Space G] {U : Set G} (hU : IsOpen U)
    (h1 : (1 : G) ∈ U) :
    ∃ (N : Subgroup G) (n : ℕ) (φ : G →ₜ* GL (Fin n) ℝ),
      IsClosed (N : Set G) ∧ (N : Set G) ⊆ U ∧ φ.toMonoidHom.ker = N := by
  sorry
```

Identifiers checked:

- `GL` is the notation for `Matrix.GeneralLinearGroup` (`Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.lean`), which unfolds to `(Matrix n n R)ˣ`. Its topological-group instance comes from `Units` (`Mathlib/Topology/Algebra/Group/Units.lean`).
- `→ₜ*` is `ContinuousMonoidHom`.
- `MonoidHom.ker` is standard.
- In the second draft, `N.Normal` follows from `N` being a kernel.

### 1c. Sources

**Originals.**

- F. Peter, H. Weyl, *Die Vollständigkeit der primitiven Darstellungen einer geschlossenen kontinuierlichen Gruppe*, Math. Ann. 97 (1927), 737–755, doi:[10.1007/BF01447892](https://doi.org/10.1007/BF01447892). Compact *Lie* groups. Verified through search snippets: Wikipedia and Altmetric.
- J. von Neumann, *Zum Haarschen Maß in topologischen Gruppen*, Compositio Math. 1 (1934/35), 106–114 ([numdam CM_1935__1__106_0](https://www.numdam.org/item/CM_1935__1__106_0)). This gives Haar measure on compact groups. Verified through the numdam record snippet.
- The extension of Peter–Weyl to arbitrary compact groups is usually credited to J. von Neumann, *Almost periodic functions in a group. I*, Trans. AMS 36 (1934), 445–492. The pages are corroborated by a secondary citation of p. 447; journal record and DOI **unverified**.

**Modern proofs.**

- **Tao, *Hilbert's Fifth Problem and Related Topics*, AMS GSM 153 (2014), doi:[10.1090/gsm/153](https://doi.org/10.1090/gsm/153), Ch. 4 "Haar measure, the Peter–Weyl theorem, and compact or abelian groups".** Chapter titles verified from the AMS listing. Blog version: [254A Notes 3: Haar measure and the Peter–Weyl theorem](https://terrytao.wordpress.com/2011/09/27/254a-notes-3-haar-measure-and-the-peter-weyl-theorem/). A draft PDF appears in search results at `terrytao.wordpress.com/wp-content/uploads/2012/03/hilbert-book.pdf`; it could not be fetched.
  - Availability: the blog is free.
  - Self-containment: proves Haar measure and Peter–Weyl through compact convolution operators; needs the spectral theorem for compact self-adjoint operators.
  - **Rating: high.** It is the same compact-operator route TauCeti followed, and its prerequisites (Haar, `L²`, compact operators, spectral theorem) are all in Mathlib.
- G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press (2015/2016), ISBN 978-1-4987-2713-6, Ch. 5 "Analysis on Compact Groups", §5.2 "The Peter–Weyl theorem". Chapter structure verified; theorem numbers not.
  - Availability: not free.
  - Self-containment: standard analytic proof, assumes Haar measure (Ch. 2) and basic functional analysis.
  - **Rating: high.** The proof is short and uses exactly the convolution-operator route.
- K. H. Hofmann, S. A. Morris, *The Structure of Compact Groups*, 4th ed., De Gruyter Studies in Math. 25 (2020), doi:[10.1515/9783110695991](https://doi.org/10.1515/9783110695991), Ch. 3 "The Ideas of Peter and Weyl". Chapter verified via a library TOC.
  - Availability: not free.
  - **Rating: medium.** Encyclopaedic and Banach-algebraic in style. Good for the corollary "compact groups embed in products of `U(n)`".
- The proof actually implemented in TauCeti cites Bump, *Lie Groups*, 2nd ed., Ch. 2, and Folland §§3.2, 4.4 (per TauCeti file headers).

---

## 2. Pontryagin: commutative NSS (or locally Euclidean) groups are Lie

### 2a. Exact statement the paper needs

**Where it is used.**

- Introduction, "Further relevant history": "Another important partial solution of H5 is for the case of commutative `G`, due to Pontrjagin, and we shall need this as well."
- Introduction, step (4): "Since `N` has NSS, it is locally euclidean by (3). But `N` is also commutative, and hence a Lie group (Pontrjagin)."
- **Corollary 6.10** ("`G` is a Lie group"), which is proved only by reference to step (4).

**What `N` is.** After replacing `G` by `G₀` (§6: `G₀` is open since `G` is locally Euclidean), Lemma 6.9 gives `N = ker(Ad) = center(G₀)`. So `N` is:

- commutative;
- **central** (even more than commutative);
- closed in `G₀`, hence locally compact Hausdorff;
- NSS, because a subgroup of an NSS group is NSS (fact (5) of §2 with the inclusion).

Applying §6 (Corollaries 6.3 and 6.8, Lemma 6.7) to `N` itself shows:

- `𝔏(N)` is a finite-dimensional real vector space;
- `exp_N : ξ ↦ ξ(1)` maps a compact neighbourhood `𝒦` of `o` homeomorphically onto a neighbourhood `K` of `1`.

**Precise form needed.** If `N` is a commutative, locally compact Hausdorff group with NSS, then `N` is a (real-analytic) Lie group. In the paper's context the hypotheses are even stronger: the conclusions of §6 are already available for `N`.

**Weaker special case that suffices (my analysis).** For commutative `N`, any two 1-ps commute, so

  `(ξ(1/s)η(1/s))^{[st]} = ξ([st]/s) η([st]/s) → ξ(t)η(t)`.

Hence `ξ + η = ξ·η` pointwise, and `exp_N : 𝔏(N) → N` is a **continuous group homomorphism**. By Corollary 6.3 and Lemma 6.7 it is a homeomorphism near 0. Therefore:

- its image is an open subgroup `N° ≅ 𝔏(N)/Γ` with `Γ = ker exp_N` discrete;
- the charts `x ↦ g·exp_N(v)` have translation transition maps, so they are analytic;
- multiplication in charts is vector addition.

So `N` is an analytic Lie group of dimension `dim 𝔏(N)`. No duality, Fourier analysis or classification of LCA groups is needed; the "Pontryagin" step reduces to roughly half a page plus §6.

The classical theorem is much stronger: every LCA group with NSS is `≅ ℝᵃ × 𝕋ᵇ × D` with `D` discrete, and every locally connected finite-dimensional LCA group is Lie. It is **not** needed.

### 2b. Lean / Mathlib status

**Mathlib: absent.**

- `Mathlib/Topology/Algebra/PontryaginDual.lean` defines `PontryaginDual A := A →ₜ* Circle`, proves its local compactness, and proves "compact ⇒ dual discrete".
- It has no duality theorem, no structure theorem for LCA groups and no "abelian NSS ⇒ Lie".
- Two lemmas are useful for the elementary route:
  - `Subgroup.dense_or_isCyclic` / `AddSubgroup.dense_or_isCyclic` (`Mathlib/Topology/Algebra/Order/ArchimedeanDiscrete.lean`): closed subgroups of ℝ.
  - Discreteness of kernels.

**TauCeti:** has Bochner's theorem on LCA groups (`TauCeti/Analysis/Bochner/LocallyCompactGroup.lean`) and Pontryagin-measure and Fourier files (`TauCeti/Analysis/Fourier/Pontryagin/*`, `TauCeti/RepresentationTheory/Continuous/Pontryagin/*`). I found no structure theorem for LCA groups and no "abelian NSS ⇒ Lie".

**formal-conjectures:** nothing.

**UNCOMPILED DRAFT:**

```lean
open scoped Topology Manifold ContDiff

/-- No small subgroups. UNCOMPILED DRAFT. -/
def HasNoSmallSubgroups (G : Type*) [Group G] [TopologicalSpace G] : Prop :=
  ∃ U ∈ 𝓝 (1 : G), ∀ H : Subgroup G, (H : Set G) ⊆ U → H = ⊥

/-- "Pontryagin" in the form needed by [vdDG, Cor. 6.10]: a commutative locally compact
Hausdorff group with no small subgroups admits a Lie group structure. UNCOMPILED DRAFT. -/
theorem admitsLieGroupStructure_of_commGroup_of_hasNoSmallSubgroups {A : Type*} [CommGroup A]
    [TopologicalSpace A] [IsTopologicalGroup A] [LocallyCompactSpace A] [T2Space A]
    (h : HasNoSmallSubgroups A) : AdmitsLieGroupStructure A := by
  sorry

/-- Classical locally Euclidean form, with the chart dimension matched (needs invariance of
dimension, see §6). UNCOMPILED DRAFT. -/
theorem nonempty_lieGroupPresentation_of_commGroup {A : Type*} [CommGroup A]
    [TopologicalSpace A] [IsTopologicalGroup A] [T2Space A] {n : ℕ}
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) A] : Nonempty (LieGroupPresentation A n) := by
  sorry
```

`AdmitsLieGroupStructure` and `LieGroupPresentation` come from formal-conjectures; `𝓝` needs `open scoped Topology`. In a proof it is easier to apply the first draft to `↥N` for a subgroup `N` carrying `[IsMulCommutative N]` (`Mathlib/Algebra/Group/Semigroup.lean`) than to require `CommGroup`.

### 2c. Sources

**Original.**

- L. Pontrjagin, *The theory of topological commutative groups*, Ann. of Math. (2) 35 (1934), no. 2, 361–388, doi:[10.2307/1968438](https://doi.org/10.2307/1968438). Verified through search snippets (nLab and numdam bibliographies). A Russian version, Uspekhi Mat. Nauk 1936, no. 2, 177–195, is also listed.
- The vdDG paper gives no bibliography item for Pontryagin. Which paper or book contains exactly "locally euclidean commutative ⇒ Lie" is **unverified**; it is classically attributed to Pontryagin's 1934 paper and his book *Topological Groups* (Princeton, 1939).

**Modern sources.**

- **The paper itself, §§2–6, plus the half-page argument in §2a above.**
  - Availability: free (vdDG preprint at [math.uci.edu/~isaac/h5.pdf](https://www.math.uci.edu/~isaac/h5.pdf), per search result).
  - **Rating: high.** Once §§5–6 are formalized, this route needs only translation charts and closed subgroups of ℝ.
- Tao, GSM 153, Ch. 4 (title includes "compact or abelian groups") and 254A Notes 3.
  - Content beyond the chapter title is **unverified**.
  - **Rating: medium** (it probably proceeds through Pontryagin duality / Peter–Weyl).
- S. A. Morris, *Pontryagin Duality and the Structure of Locally Compact Abelian Groups*, LMS Lecture Note Ser. 29, CUP (1977), doi:[10.1017/CBO9780511600722](https://doi.org/10.1017/CBO9780511600722). Verified bibliographic record.
  - Self-containment: avoids measure theory; full duality and structure theory.
  - **Rating: low–medium.** Much more than needed, and duality itself is a large formalization project.
- E. Hewitt, K. A. Ross, *Abstract Harmonic Analysis I*, Springer Grundlehren 115, Theorem (9.8): compactly generated LCA groups are `ℝᵃ × ℤᵇ × F` with `F` compact. The theorem number is verified only through an arXiv citation (arXiv:2310.19020).
  - **Rating: low** as a formalization source, because it is too heavy.

---

## 3. Kuranishi's extension theorem

### 3a. Exact statement the paper needs

**Where it is used.**

- Introduction: "we are going to use a result of Kuranishi [14]: if `G` has a commutative closed normal subgroup `N` such that `N` and `G/N` are Lie groups, then `G` is a Lie group. Gleason [4] and Iwasawa [11] establish this without assuming commutativity of `N`, but we don't need this stronger version…"
- Introduction, step (4): "Apply the Kuranishi theorem to conclude that `G` is a Lie group."
- **Corollary 6.10**, by reference to step (4).

**Precise form needed.** Let `G` be a **connected**, locally compact Hausdorff group. In the application `G = G₀`, and `G` has NSS and is locally Euclidean by §6. Let `N ⊆ G` be a **closed central** subgroup; Lemma 6.9 gives `ker Ad = center(G)` for connected `G`. If `N` and `G/N` (quotient topology) are Lie groups, then `G` is a Lie group.

- **Only the central case is used**, although the paper states the commutative-normal version.
- Connectedness, NSS and local Euclideanity of `G` are all available and may be used.
- No second countability is assumed. A connected locally compact group is σ-compact anyway, being generated by a compact neighbourhood.
- "Lie" means "admits a compatible real-analytic structure", as in `LieGroupPresentation`.

**Subtlety.** The *general* extension theorem (non-abelian `N`) follows from the Main Theorem plus fact (6) of §2 ("Note also that the Main Theorem and (6) yield the Gleason–Iwasawa result"). But the Main Theorem's proof uses the central case, so the central case is a genuine input and cannot be derived from the paper.

**Bibliographic discrepancy.**

- The published title of [14] is "On **Euclidean local groups** satisfying certain conditions". The paper's bibliography (also in the PDF) has "On local euclidean groups …".
- Gutman–Manners–Varjú (arXiv:1605.08948) remark, citing Gleason, that "Kuranishi actually proved a weaker statement in [Kur50]". So exactly what Kuranishi proved is **unverified** here.

### 3b. Lean / Mathlib status

**Absent in Mathlib, TauCeti and formal-conjectures.**

- Ingredients present in Mathlib: quotient groups and their topology (`QuotientGroup.instLocallyCompactSpace`, `QuotientGroup.isOpenMap_coe`), `Subgroup.center`, group cohomology (`Mathlib/RepresentationTheory/Homological/GroupCohomology`, algebraic only).
- Missing: local cross-sections of `G → G/N`, continuous or analytic cocycles, and the "averaging" argument.

**UNCOMPILED DRAFT:**

```lean
/-- Central-extension form of Kuranishi's theorem, as used in [vdDG, Cor. 6.10].
UNCOMPILED DRAFT. -/
theorem admitsLieGroupStructure_of_central_extension {G : Type*} [Group G] [TopologicalSpace G]
    [IsTopologicalGroup G] [LocallyCompactSpace G] [T2Space G] [ConnectedSpace G]
    (N : Subgroup G) [N.Normal] (hNc : N ≤ Subgroup.center G) (hN : IsClosed (N : Set G))
    (hNLie : AdmitsLieGroupStructure N) (hQLie : AdmitsLieGroupStructure (G ⧸ N)) :
    AdmitsLieGroupStructure G := by
  sorry

/-- Kuranishi's commutative form as stated in [vdDG, Introduction]. UNCOMPILED DRAFT. -/
theorem admitsLieGroupStructure_of_commutative_extension {G : Type*} [Group G]
    [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G] [T2Space G]
    (N : Subgroup G) [N.Normal] [IsMulCommutative N] (hN : IsClosed (N : Set G))
    (hNLie : AdmitsLieGroupStructure N) (hQLie : AdmitsLieGroupStructure (G ⧸ N)) :
    AdmitsLieGroupStructure G := by
  sorry
```

Identifiers checked:

- `Subgroup.center` (`Mathlib/GroupTheory/Subgroup/Center.lean`).
- `Subgroup.Normal`.
- `IsMulCommutative`.
- `G ⧸ N` with its quotient topology.
- `↥N` with its subspace topology.

`[ConnectedSpace G]` in the first draft is a harmless simplification matching the use. Dropping it gives the true but harder Gleason–Iwasawa-style statement for central `N`.

### 3c. Sources

**Originals.**

- M. Kuranishi, *On Euclidean local groups satisfying certain conditions*, Proc. Amer. Math. Soc. 1 (1950), 372–380, MR 0036238, Zbl 0038.01701. Title, volume and pages are verified through Tao's GSM 153 bibliography and a ScienceDirect reference list. The AMS DOI `10.1090/S0002-9939-1950-0036238-7` follows the AMS pattern but is **unverified** (ams.org blocked). The paper is free on ams.org, which was not reachable to confirm.
- A. M. Gleason, *On the structure of locally compact groups*, Duke Math. J. 18 (1951), 85–104 (the paper's pages; a Bourbaki listing gives 85–110), doi:[10.1215/S0012-7094-51-01808-X](https://doi.org/10.1215/S0012-7094-51-01808-X). Theorem 3.1 is the general extension theorem (per Gutman–Manners–Varjú). DOI verified through a search snippet.
- K. Iwasawa, *On some types of topological groups*, Ann. of Math. (2) **50** (1949), 507–558, MR 0029911.
  - The paper's bibliography misprints this as "Ann. of Math. 2 (1949), 507–557"; the error is also in the PDF.
  - The volume and pages are confirmed by nLab and Bourbaki bibliographies.
  - DOI **unverified**. (Do not confuse it with 10.2307/1969548, which formal-conjectures uses for Gleason 1952.)

**Modern proofs.**

- **Tao, GSM 153, §2.6 "Central extensions of Lie groups, and cocycle averaging" (chapter DOI [10.1090/gsm/153/16](https://doi.org/10.1090/gsm/153/16)), Theorem 2.6.1.** Blog version: [Central extensions of Lie groups, and cocycle averaging](https://terrytao.wordpress.com/2011/06/07/central-extensions-of-lie-groups-and-cocycle-averaging/) (2011-06-07).
  - The chapter existence, DOI and the use of "[Tao14, Thm 2.6.1]" for the central case (by Gutman–Manners–Varjú, [arXiv:1605.08948](https://arxiv.org/abs/1605.08948), Thm 3.6 and its footnote) are verified through search snippets. The exact hypotheses of Theorem 2.6.1 are **unverified**, because the blog was blocked.
  - Availability: blog free.
  - Self-containment: the snippets say the smooth structures of `H` and `K` are combined "after a little bit of cohomology" (cocycle averaging with Haar measure).
  - **Rating: medium.** It is the most modern and shortest proof, and it is targeted exactly at the central case, but it needs Lie theory (§5), local cross-sections and Haar integration of cocycles.
- Gutman–Manners–Varjú, arXiv:1605.08948, §3: a short discussion; they note they only need the central and discrete-extension cases.
  - **Rating: low** as a proof source, because it cites rather than proves.
- D. Montgomery, L. Zippin, *Topological Transformation Groups*, Interscience 1955; Dover reprint 2018. Chapters I–VI verified from a library record; where (or whether) the extension theorem appears is **unverified**.
  - **Rating: low–medium**: old-fashioned and dense.

---

## 4. Cartan–von Neumann: a continuous injection into `GLₙ(ℝ)` makes `G/N` a Lie group

### 4a. Exact statement the paper needs

**Where it is used.**

- Introduction, step (4): "the adjoint representation … yields an injective continuous group morphism `G/N → GLₙ(ℝ)` … The injective continuous group morphism `G/N → GLₙ(ℝ)` makes `G/N` a Lie group (E. Cartan, von Neumann)."
- **Corollary 6.10**, through Lemma 6.9 (continuity of `Ad : G → Aut(𝔏(G)) ≅ GLₙ(ℝ)` and `ker Ad = center(G)` for connected `G`).

**Precise form needed.** Let `H` be a locally compact Hausdorff topological group; in the application `H = G₀/Z(G₀)` with the quotient topology. Let `φ : H → GLₙ(ℝ)` be a continuous injective homomorphism. Then `H` is a real-analytic Lie group, and `φ` is then an analytic immersion.

**Subtleties.**

1. The image `φ(H)` need **not** be closed. Example: `G = ℝ ⋉ ℂ²` with `t` acting by `(e^{it}, e^{iαt})`, `α ∉ ℚ`. Its `Ad`-image contains a dense line of a 2-torus. So the closed-subgroup (Cartan) theorem cannot be applied to `φ(H) ⊆ GLₙ(ℝ)`.
2. The topology of `H` can be strictly finer than the subspace topology of `φ(H)`. The extreme case is `ℝ` with the discrete topology `→ ℝ`. That case is consistent with the target statement, because discrete groups count as 0-dimensional Lie groups (`admitsLieGroupStructure_of_discreteTopology`). It shows that the conclusion must give `H` its own topology, not the subspace one.
3. Local compactness of `H` is essential: `ℚ ⊂ ℝ` is a counterexample without it.

**Three proof routes.**

- **(A) "von Neumann's theorem" (Tao).** "If `G` is a Lie group, and `H` is a locally compact group with an injective continuous homomorphism `ρ : H → G`, then `H` also has the structure of a Lie group." Tao, 254A Notes 2, Theorem 4, quoted verbatim in a search snippet.
  - The proof uses a *local* version of Cartan's theorem. Take a compact neighbourhood `K` of `1` in `H`. Then `ρ|_K` is a homeomorphism onto `ρ(K)` (compact to Hausdorff), so `ρ(K)` is a compact local subgroup of `G`. A local Cartan theorem then makes it a submanifold near `1`, and translation spreads the structure.
  - It needs **no σ-compactness and no open mapping theorem**, and it covers example 2 automatically.
  - Tao also states the linear case separately: "any locally compact Hausdorff group with a faithful finite-dimensional linear representation is a Lie group; after giving `H` this Lie structure, `ρ` becomes smooth (even analytic) and non-degenerate".
- **(B) Open-mapping route.**
  - `G₀` is connected and locally compact, hence σ-compact; so `H` is σ-compact.
  - `φ(H)` is a path-connected subgroup of `GLₙ(ℝ)`, hence an *analytic (integral) subgroup* carrying its own Lie topology. This is Yamabe's arcwise-connected-subgroup theorem, or Hilgert–Neeb's "initial subgroup" theorem for subgroups with countably many components.
  - One shows `φ : H → φ(H)_{Lie}` is continuous, then applies the open mapping theorem for continuous surjections from σ-compact groups onto Baire groups. This is in Mathlib as `MonoidHom.isOpenMap_of_sigmaCompact`.
  - Heavier: it needs integral subgroups (Frobenius) and the continuity argument.
- **(C) In-paper route (my analysis, lightest given §§5–6).**
  - Since `φ` is injective and `GLₙ(ℝ)` has NSS (fact (3) of §2), `H` has NSS by fact (5).
  - §6 applied to `H` gives `𝔏(H)` finite-dimensional and `exp_H` a homeomorphism near 0.
  - `𝔏(φ) : 𝔏(H) → 𝔏(GLₙ) ≅ 𝔤𝔩ₙ(ℝ)` is linear (§2: `𝔏(φ)(ξ+η) = 𝔏(φ)ξ + 𝔏(φ)η`) and injective; let `𝔥` be its image. Here a continuous 1-ps of `GLₙ` is `t ↦ exp(tX)`, which is result 5 for `GLₙ` only.
  - For small `X, Y ∈ 𝔥`: `exp X · exp Y = φ(exp_H ξ · exp_H η) = φ(exp_H ζ) = exp(𝔏(φ)ζ)`, so `log(exp X exp Y) ∈ 𝔥`.
  - Hence the charts `g·exp_H(𝔏(φ)⁻¹ v)` (`v ∈ 𝔥` small) have transition maps `v ↦ log_{GL}(φ(g'⁻¹g)·exp v)` restricted to `𝔥`. These are analytic: matrix `exp` and `log` are analytic, by the analytic inverse function theorem. Multiplication in charts is analytic for the same reason.
  - No closedness of `φ(H)`, no σ-compactness and no BCH series are needed.

**Conclusion for the brief's question.** The theorem actually needed is **not** the closed-subgroup theorem. It is von Neumann's theorem for locally compact groups with a faithful continuous finite-dimensional representation. In the paper's context it can be derived from §6 plus the analytic local inverse of the matrix exponential (route C). The open-mapping version (B) is a valid alternative here because `G₀/Z` is σ-compact, but it is not needed.

### 4b. Lean / Mathlib status

**Mathlib: partial (ingredients).**

- Matrix and Banach-algebra exponential:
  - `NormedSpace.exp` (`Mathlib/Analysis/Normed/Algebra/Exponential.lean`), including `NormedSpace.exp_analytic` and `NormedSpace.exp_add_of_commute`;
  - `hasStrictFDerivAt_exp_zero` (`Mathlib/Analysis/SpecialFunctions/Exponential.lean`);
  - `Matrix.exp_add_of_commute` (`Mathlib/Analysis/Normed/Algebra/MatrixExponential.lean`).
- Inverse function theorem: `HasStrictFDerivAt.toOpenPartialHomeomorph` (`Mathlib/Analysis/Calculus/InverseFunctionTheorem/FDeriv.lean`). Its **analytic** version is `OpenPartialHomeomorph.analyticAt_symm` / `analyticAt_symm'` (`Mathlib/Analysis/Calculus/FDeriv/Analytic.lean`).
- `GLₙ` as an analytic Lie group: the instance `LieGroup 𝓘(𝕜, R) n Rˣ` for all `n : ℕ∞ω` (so including `ω`) and every complete normed ring `R` (`Mathlib/Geometry/Manifold/Instances/UnitsOfNormedAlgebra.lean`).
  - Caveat: Mathlib's norms on `Matrix n n ℝ` are scoped instances, so it is easier to use `(EuclideanSpace ℝ (Fin n) →L[ℝ] EuclideanSpace ℝ (Fin n))ˣ`. formal-conjectures' `LieDeriv.lean` hits the same problem.
  - The model is `𝓘(ℝ, R)`, not `𝓡 m`, so re-modelling on `EuclideanSpace ℝ (Fin m)` is needed for `LieGroupPresentation`.
- Open mapping: `MonoidHom.isOpenMap_of_sigmaCompact` (`Mathlib/Topology/Algebra/Group/OpenMapping.lean`), with `BaireSpace.of_t2Space_locallyCompactSpace` for the Baire target.
- Compact-to-Hausdorff homeomorphism: `Continuous.homeoOfEquivCompactToT2`.
- **Absent:** the closed-subgroup theorem, von Neumann's theorem, analytic subgroups, and the classification of continuous 1-ps of `GLₙ`.

**TauCeti: partial.**

- Cartan's closed-subgroup theorem: `TauCeti.Lie.isEmbeddedLieSubgroup_of_isClosed` (`TauCeti/Geometry/Lie/Subgroup/Embedded.lean`), for `[LieGroup I ∞ G]`, finite-dimensional, real.
- Continuous 1-ps of units of a Banach algebra: `TauCeti.existsUnique_eq_expUnitHom` and `TauCeti.continuousMonoidHom_eq_expUnitHom_of_hasDerivAt` (`TauCeti/Geometry/Lie/Exponential/OneParameter.lean`). Note these need differentiability at 0.
- General Lie groups: `existsUnique_eq_mulInvariantOneParameterSubgroup` (`…/Exponential/Classification.lean`), for continuous 1-ps.
- NSS of `Aˣ`: `TauCeti.eq_one_of_forall_norm_pow_sub_one_le` and `ContinuousMonoidHom.exists_mem_nhds_one_forall_le_ker` (`TauCeti/Analysis/Normed/Algebra/NoSmallSubgroups.lean`). This is exactly fact (3) of §2 of the paper.
- Automatic smoothness of continuous homomorphisms: `TauCeti.Lie.contMDiff_of_continuous_monoidHom`.
- **Missing:** von Neumann's theorem itself (locally compact domain), and anything at ω regularity.

**UNCOMPILED DRAFT:**

```lean
/-- von Neumann's theorem, linear form: a locally compact Hausdorff group with a faithful
continuous real representation admits a Lie group structure. Used in [vdDG, Cor. 6.10] for
`H = G₀ ⧸ center G₀`. UNCOMPILED DRAFT. -/
theorem admitsLieGroupStructure_of_injective_GL {H : Type*} [Group H] [TopologicalSpace H]
    [IsTopologicalGroup H] [LocallyCompactSpace H] [T2Space H] {n : ℕ}
    (φ : H →ₜ* GL (Fin n) ℝ) (hφ : Function.Injective φ) : AdmitsLieGroupStructure H := by
  sorry

/-- von Neumann's theorem, general form (Tao, 254A Notes 2, Thm 4). UNCOMPILED DRAFT. -/
theorem admitsLieGroupStructure_of_injective {H L : Type*} [Group H] [TopologicalSpace H]
    [IsTopologicalGroup H] [LocallyCompactSpace H] [T2Space H] [Group L] [TopologicalSpace L]
    (hL : AdmitsLieGroupStructure L) (φ : H →ₜ* L) (hφ : Function.Injective φ) :
    AdmitsLieGroupStructure H := by
  sorry
```

### 4c. Sources

**Originals.**

- J. von Neumann, *Über die analytischen Eigenschaften von Gruppen linearer Transformationen und ihrer Darstellungen*, Math. Z. 30 (1929), 3–42, doi:[10.1007/BF01187749](https://doi.org/10.1007/BF01187749). Verified through the Springer record snippet. It covers closed linear groups. A secondary source (Wieting, Reed College essay) says von Neumann proved that a locally compact group with a faithful continuous finite-dimensional real representation is Lie; that attribution is **unverified** against the original.
- É. Cartan, *La théorie des groupes finis et continus et l'Analysis situs*, Mémorial des Sciences Mathématiques 42, Gauthier-Villars, 1930 ([numdam MSM_1952__42__1_0](https://numdam.org/item/MSM_1952__42__1_0/), a later printing). This is the closed subgroups of Lie groups. Verified through a numdam / defence-library record snippet; the exact location of the theorem inside the memoir is unverified.

**Modern proofs.**

- **Tao, [254A Notes 2: Building Lie structure from representations and metrics](https://terrytao.wordpress.com/2011/09/08/254a-notes-2-building-lie-structure-from-representations-and-metrics/) (2011-09-08) = GSM 153, Ch. 3.** Theorem 4 ("von Neumann's theorem") and the Cartan theorem statement were seen verbatim in search snippets; the full text could not be fetched. See also [Locally compact groups with faithful finite-dimensional representations](https://terrytao.wordpress.com/2011/05/27/locally-compact-groups-with-faithful-finite-dimensional-representations/) (2011-05-27), whose Theorem 1 is the linear case and which notes the argument also works for local groups.
  - Availability: free.
  - Self-containment: uses Lie-group basics (Ch. 2 of the book).
  - **Rating: high.** The local-Cartan argument needs no countability and matches `LieGroupPresentation`.
- J. Hilgert, K.-H. Neeb, *Structure and Geometry of Lie Groups*, Springer Monographs in Math. (2012). §9.1 has the closed subgroup theorem (cited by TauCeti); p. 356 has the initial-subgroup theorem (per arXiv:2302.14457). The DOI `10.1007/978-0-387-84794-8` is **unverified**.
  - Availability: not free.
  - **Rating: medium** for route (B): complete and careful, but organized around C^∞ and second countability.
- The paper's §6 together with §4a route (C) of this report.
  - **Rating: high**, since it reuses work needed anyway. This is my analysis, not a published proof, so it should be checked by a human before formalizing.

---

## 5. Basic Lie theory: 1-parameter subgroups and the exponential map

### 5a. Exact statement the paper needs

**Where it appears.** Introduction, "The case of Lie groups":

- "each `ξ ∈ 𝔏(G)` is analytic … This gives the bijection `ξ ↦ ξ'(0) : 𝔏(G) → T₁(G)`";
- "The addition operation on `𝔏(G)` that makes this bijection an isomorphism … `(ξ+η)(t) = lim_{s→∞}(ξ(1/s)η(1/s))^{[st]}`";
- "the so-called exponential map `ξ ↦ ξ(1)` yields an analytic isomorphism from an open neighborhood of `o` in `𝔏(G)` onto an open neighborhood of 1 in `G`".

This passage is **motivation**. The logical chain of the Main Theorem never applies these facts to a general Lie group:

- (1)⇒(3) (Lie ⇒ locally Euclidean) is trivial.
- (3)⇒(2) is §7.
- (2)⇒(1) is §§5–6 plus results 2–4.

So result 5 is needed only *inside* the proofs of 2 (only for `ℝⁿ/Γ`, essentially trivial), 3 (the Lie theory of `N` and `G/N`) and 4 (only for `GLₙ(ℝ)`). It is also needed for the routine "open Lie subgroup ⇒ Lie" gluing, and for upgrading C^∞ to ω (§6).

**Precise form.** Let `G` be a Hausdorff group with a real-analytic manifold structure modelled on `ℝⁿ` (`IsManifold (𝓡 n) ω`, `LieGroup (𝓡 n) ω`). There is **no** second countability assumption, but `G` is first countable and locally compact. Then:

1. Every continuous homomorphism `ξ : ℝ → G` is analytic, and `ξ ↦ ξ'(0)` is a bijection from `𝔏(G)` onto `T₁G`. Equivalently, there is a unique `exp : T₁G → G` with `ξ(t) = exp(t·ξ'(0))`.
2. (Trotter / Lie product formula) `exp(t(v+w)) = lim_{k→∞} (exp(tv/k) exp(tw/k))^k`. This identifies the paper's `+` with vector addition.
3. `exp` is analytic, with derivative `id` at 0, hence an analytic diffeomorphism from a neighbourhood of 0 onto a neighbourhood of 1.

For route 4(C) only `G = GLₙ(ℝ)` (units of a Banach algebra) is needed: items 1 and 3 there are elementary. For result 3, items 1–3 are needed for the Lie groups `N` and `G/N`.

### 5b. Lean / Mathlib status

**Mathlib: partial.**

- `LieGroup` (`Mathlib/Geometry/Manifold/Algebra/LieGroup.lean`), with instances `LieGroup I ω G → LieGroup I a G`.
- `GroupLieAlgebra I G := TangentSpace I 1`, with Lie bracket via `mulInvariantVectorField` (`Mathlib/Geometry/Manifold/GroupLieAlgebra.lean`; its standing assumption is regularity `minSmoothness 𝕜 3`).
- `LeftInvariantDerivation` (`Mathlib/Geometry/Manifold/Algebra/LeftInvariantDerivation.lean`).
- Integral curves with uniqueness and a uniform-time global-existence lemma (`Mathlib/Geometry/Manifold/IntegralCurve/{ExistUnique,UniformTime}.lean`).
- Banach-algebra `exp` as in §4b.
- **Absent:** a Lie-group exponential map, one-parameter subgroups (grep for "one-parameter" or `OneParameter` in Mathlib finds nothing), the classification of continuous 1-ps, and Trotter.

**TauCeti: largely present, but C^∞ only.** All of the following assume `[FiniteDimensional ℝ E] [LieGroup I ∞ G]`, many also `[T2Space G] [BoundarylessManifold I G]`, and **no second countability** (grep found no `SecondCountable` / `SigmaCompact` in `TauCeti/Geometry/Lie`).

- `mulInvariantExp` and `lieExp` (`TauCeti/Geometry/Lie/Exponential/Basic.lean`).
- `existsUnique_eq_mulInvariantOneParameterSubgroup` and `oneParameterSubgroupEquiv` (`…/Exponential/Classification.lean`): **continuous** 1-ps classification.
- `isLocalDiffeomorphAt_lieExp_zero` and `mulInvariantLog` (`…/Exponential/LocalInverse.lean`).
- `tendsto_lieExp_smul_mul_lieExp_smul_pow` (Trotter, `…/Exponential/Trotter.lean`).
- `…/Exponential/BCH.lean`.
- `TauCeti.Lie.contMDiff_of_continuous_monoidHom` (automatic smoothness).

**The gap** is the analytic (ω) version that `LieGroupPresentation` needs: analyticity of `exp` and of the group law in exponential charts. Only `TauCeti.contDiff_exp_smul` for Banach algebras is stated as analytic.

**UNCOMPILED DRAFT** (stated without a named `exp`, since Mathlib has none):

```lean
open scoped Manifold ContDiff in
/-- Exponential map of a real-analytic Lie group (not assumed second countable): continuous
one-parameter subgroups are exactly `t ↦ E (t • v)`, and `E` is an analytic local
diffeomorphism at `0`. UNCOMPILED DRAFT. -/
theorem exists_exp_of_lieGroup {G : Type*} [Group G] [TopologicalSpace G] [T2Space G] {n : ℕ}
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) G] [IsManifold (𝓡 n) ω G] [LieGroup (𝓡 n) ω G] :
    ∃ E : EuclideanSpace ℝ (Fin n) → G,
      (∀ (v : EuclideanSpace ℝ (Fin n)) (s t : ℝ), E ((s + t) • v) = E (s • v) * E (t • v)) ∧
      (∀ φ : Multiplicative ℝ →ₜ* G, ∃! v : EuclideanSpace ℝ (Fin n),
        ∀ t : ℝ, φ (Multiplicative.ofAdd t) = E (t • v)) ∧
      ∃ e : OpenPartialHomeomorph (EuclideanSpace ℝ (Fin n)) G,
        (0 : EuclideanSpace ℝ (Fin n)) ∈ e.source ∧ (⇑e : _ → G) = E ∧
        ContMDiffOn (𝓡 n) (𝓡 n) ω e e.source ∧ ContMDiffOn (𝓡 n) (𝓡 n) ω e.symm e.target := by
  sorry
```

Identifiers checked:

- `ContMDiffOn I I' n f s` (explicit `I I'`, `n : ℕ∞ω`; `Mathlib/Geometry/Manifold/ContMDiff/Defs.lean`).
- `OpenPartialHomeomorph`.
- `Multiplicative.ofAdd`; `Multiplicative ℝ` inherits ℝ's topology (`Mathlib/Topology/Constructions.lean`).
- `𝓡 n` is scoped notation in `Manifold` for `modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n))`.
- Here `T₁G` is identified with `EuclideanSpace ℝ (Fin n)` through the chart at 1; Mathlib's `GroupLieAlgebra (𝓡 n) G` is definitionally that tangent space.

### 5c. Sources

- **J. Hilgert, K.-H. Neeb, *Structure and Geometry of Lie Groups* (Springer, 2012).** Exponential map, 1-ps, closed and initial subgroups, analytic structure.
  - Availability: not free.
  - **Rating: medium–high.** Complete and rigorous, with manifolds handled carefully. Uses second countability in places (unverified which).
- **Tao, GSM 153, Ch. 2 "Lie groups, Lie algebras, and the Baker–Campbell–Hausdorff formula"** (chapter title verified; blog [254A Notes 1](https://terrytao.wordpress.com/2011/09/01/254a-notes-1-lie-groups-lie-algebras-and-the-baker-campbell-hausdorff-formula/)).
  - Availability: free.
  - **Rating: high** for the analytic structure. It proves BCH analytically, which is exactly what ω regularity needs.
- B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., GTM 222 (2015). Matrix-group version; TauCeti cites Ch. 3.
  - **Rating: high** for the `GLₙ` case used in route 4(C).
- J. J. Duistermaat, J. A. C. Kolk, *Lie Groups*, Universitext (Springer, 2000). Bibliographic data not re-verified on the web.
  - **Rating: medium.**
- TauCeti's roadmap ([TauCetiRoadmap/RepresentationTheory/LieGroups/README.md](https://github.com/TauCetiProject/TauCetiRoadmap)) records the dependency structure actually formalized.

---

## 6. Hidden dependencies (d)

The paper uses each of the following facts without proof.

| Fact | Where used | Precise need | Mathlib / Lean status | Source | Difficulty |
|---|---|---|---|---|---|
| **Invariance of domain / Brouwer dimension theory** | Intro ("bounded in dimension (by Brouwer)"); Cor. 7.7 ("if `G` is locally euclidean, then `G` has NSS"); and **matching the chart dimension `n`** of `hilbert_fifth_problem` with `dim 𝔏(G)` (Cor. 6.8). | (i) No subspace of a locally-ℝⁿ space is homeomorphic to `[0,1]^{n+1}`. Shrink to one chart; then `[0,1]^{n+1} ↪ ℝⁿ ⊂ ℝ^{n+1}` contradicts invariance of domain. (ii) Nonempty open sets of `ℝᵐ` and `ℝⁿ` homeomorphic ⇒ `m = n`. | **Absent from master.** Mathlib issue [#33018](https://github.com/leanprover-community/mathlib4/issues/33018) "Theorem: Invariance of domain" (seen via search). Mathlib **PR #36770** (Kai Lam; unmerged; merge-ref `dd0f7de4`, 2026-06-29) adds `Mathlib/AlgebraicTopology/InvarianceOfDomain.lean` with `invariance_of_domain_open_map` and `invariance_of_dimension`, **conditional on a `BrouwerFixedPoint E` typeclass and still containing `sorry`s** in auxiliary lemmas. Brouwer itself is proved sorry-free in [harfe/fixed-point-theorems-lean4](https://github.com/harfe/fixed-point-theorems-lean4) (`brouwer_fixed_point`, Lean v4.32.0). TauCeti has singular homology of spheres and Jordan–Brouwer separation (`TauCeti/AlgebraicTopology/Singular/{Sphere,JordanBrouwer}.lean`) but no invariance of domain. | L. E. J. Brouwer, *Beweis der Invarianz des n-dimensionalen Gebiets*, Math. Ann. 71 (1912), 305–313/315 (DOI unverified), and *Beweis der Invarianz der Dimensionenzahl*, Math. Ann. 70 (1911), 161–165. Tao, [Brouwer's fixed point and invariance of domain theorems, and Hilbert's fifth problem](https://terrytao.wordpress.com/2011/06/13/brouwers-fixed-point-and-invariance-of-domain-theorems-and-hilberts-fifth-problem/) (2011): the proof PR #36770 follows; **rating high** (elementary, Brouwer + Tietze + Stone–Weierstrass). Hatcher, *Algebraic Topology*, §2.B (free online; theorem number unverified); rating medium (needs homology). | Medium (Brouwer + PR #36770 route); good candidate for an early axiom. |
| **Existence of κ-rich nonstandard extensions for arbitrary κ** | §2 ("it is enough to assume κ⁺-saturation where κ ≥ #S for each basic set S"); Appendix ("there exist ultrafilters u … such that … S* … is κ-rich"; stated, not proved). Used throughout §§2–7 (overspill, internal neighbourhoods inside monads, Lemma 3.7's transfinite argument). | κ-saturated ultrapowers for κ ≥ #𝒫(G). This needs good / countably incomplete ultrafilters (Keisler–Kunen). ℵ₁-saturation from a nonprincipal ultrafilter on ℕ may suffice for *first-countable* `G` (all locally Euclidean `G` are), but I have **not verified** this. | Mathlib has ultraproducts and Łoś (`FirstOrder.Language.Ultraproduct`, `Mathlib/ModelTheory/Ultraproducts.lean`), `Filter.Germ` and `Hyperreal` (`Mathlib/Analysis/Real/Hyperreal.lean`); **no** saturation theorems and no internal-set calculus. | Henson, *Foundations of NSA* (paper's [7]); Keisler's good ultrafilters (not checked). | **High.** Recommendation: do not formalize NSA. Use Tao's standard proofs of the Gleason–Yamabe lemmas (GSM 153, Ch. 5), or Hirschfeld/vdDG arguments rewritten with sequences and nets. |
| **Open Lie subgroup ⇒ Lie** (and re-modelling on `EuclideanSpace ℝ (Fin n)`) | Step (4): "Replacing `G` by the connected component of 1, we can assume that `G` is connected." Cor. 6.10 proves `G₀` Lie and implicitly concludes `G` Lie. | If `H ≤ G` is open and Lie, then `G` is Lie: translate charts, no countability needed. Also: a linear iso `𝔏(G) ≅ ℝᵈ` and a chart model change to `𝓡 d`. | Absent as such; `ChartedSpace` / `IsManifold` / `LieGroup` API is all there. | Folklore. | Low–medium (engineering). |
| **C^∞ ⇒ ω** (or produce ω directly) | Definition of Lie group in §1 and in `LieGroupPresentation` (`IsManifold (𝓡 n) ω`, `LieGroup (𝓡 n) ω`). | Every route must output an *analytic* structure. Routes 2 and 4(C) do so directly (translation charts; matrix exp/log). Kuranishi (3) must too. Any use of TauCeti's C^∞ theory needs the classical upgrade "every C^∞ Lie group has a compatible analytic structure" (exp charts plus analytic BCH). | Absent (TauCeti is C^∞ only; Mathlib supports `ω` in `ContMDiff` and has `Units` as an ω Lie group). | Tao GSM 153, Ch. 2 (BCH). | Medium–high. |
| `G₀` is open and generated by `exp(𝔏(G))` | §6, before Lemma 6.9 ("It is the subgroup of `G` generated by the elements `ξ(t)` … It is open in `G`"). No proof is given. | `K` (Lemma 6.7) is a path-connected neighbourhood of 1, so `⟨K⟩` is an open, hence closed, connected subgroup, equal to `G₀`. | `Subgroup.connectedComponentOfOne` (`Mathlib/Topology/Algebra/Group/Subgroup.lean`); `isOpen_connectedComponent` for locally connected spaces; `Subgroup.isOpen_of_mem_nhds`. | — | Low. |
| Riesz: a locally compact TVS is finite-dimensional | Cor. 6.3, Cor. 5.12. | Hausdorff real TVS. | **Present:** `FiniteDimensional.of_locallyCompactSpace` (`Mathlib/Topology/Algebra/Module/FiniteDimension.lean`), for T2 TVS over a complete nontrivially normed field. | — | Done. |
| Haar measure (existence) | §5 (Gleason–Yamabe lemmas). | Left Haar measure on a locally compact Hausdorff group; no σ-finiteness or second countability; only integrals of compactly supported continuous functions. | **Present:** `MeasureTheory.Measure.haar`, `haarMeasure`, `MeasureTheory.integral_mul_left_eq_self`. | — | Done. |
| Uniform continuity of compactly supported `τ` | §5, item (4). | Left/right uniform continuity on a topological group. | **Present:** `HasCompactSupport.uniformContinuous_of_continuous` (used in `Mathlib/MeasureTheory/Measure/Haar/Extension.lean`) with the group uniformity. | — | Done. |
| Urysohn-type bump `τ` | §5 setup. | Continuous `τ : G → [0,1]`, `τ(1) = 1`, support in `𝒰`. | **Present:** `exists_continuous_zero_one_of_isCompact`, `exists_continuous_one_zero_of_isCompact` (`Mathlib/Topology/UrysohnsLemma.lean`). | — | Done. |
| Closed subgroups of ℝ; compact-to-T2 bijections are homeomorphisms | Lemma 2.1, Lemma 7.6. | Standard. | **Present:** `Subgroup.dense_or_isCyclic` / `AddSubgroup.dense_or_isCyclic`; `Continuous.homeoOfEquivCompactToT2`. | — | Done. |
| Compact-open topology on `𝔏(G) = (ℝ →ₜ* G)` | §2 (Lemmas 2.8, 2.9). | Compact-open topology, continuity of evaluation, local compactness criterion. | **Present:** `ContinuousMonoidHom` topology via `ContinuousMap.compactOpen` (`Mathlib/Topology/Algebra/Group/CompactOpen.lean`, with `isClosedEmbedding_toContinuousMap` and `locallyCompactSpace_of_equicontinuousAt`). | — | Done. |
| Quotients | §2 ("`G/N` … is a locally compact group"), Lemma 7.4 (open quotient map). | `G/N` locally compact Hausdorff for closed normal `N`; `π` open. | **Present:** `QuotientGroup.instLocallyCompactSpace`, `QuotientGroup.isOpenMap_coe`, T1/T3 quotient instances in `Mathlib/Topology/Algebra/Group/Quotient.lean`. | — | Done. |
| Metrizability (Birkhoff–Kakutani) | §6 remark after Lemma 6.5 ("We do not need this metric"). | Not needed. | Absent from Mathlib (grep). | — | Not needed. |
| `GLₙ(ℝ)` has NSS | §2 fact (3); Cor. 4.2; Lemma 8.1. | As stated. | TauCeti: `TauCeti.eq_one_of_forall_norm_pow_sub_one_le`, `ContinuousMonoidHom.exists_mem_nhds_one_forall_le_ker`. Not in Mathlib (Mathlib only has the circle analogue `Circle.eq_one_of_forall_pow_mem_centeredArc_pi_div_two`). | — | Low. |

**UNCOMPILED DRAFTS for the dimension facts:**

```lean
/-- Invariance of domain. UNCOMPILED DRAFT. -/
theorem invariance_of_domain {n : ℕ} {U : Set (EuclideanSpace ℝ (Fin n))} (hU : IsOpen U)
    {f : EuclideanSpace ℝ (Fin n) → EuclideanSpace ℝ (Fin n)} (hf : ContinuousOn f U)
    (hinj : Set.InjOn f U) : IsOpen (f '' U) := by
  sorry

/-- A space modelled on `ℝⁿ` contains no copy of `[0,1]^(n+1)` ("bounded in dimension",
[vdDG, Cor. 7.7]). UNCOMPILED DRAFT. -/
theorem not_exists_isEmbedding_cube {X : Type*} [TopologicalSpace X] {n : ℕ}
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) X] :
    ¬ ∃ f : (Fin (n + 1) → unitInterval) → X, Topology.IsEmbedding f := by
  sorry

/-- The dimension of a Lie presentation agrees with the chart dimension of the input.
Needed to produce `LieGroupPresentation G n` with the *given* `n`. UNCOMPILED DRAFT. -/
theorem LieGroupPresentation.dim_eq {G : Type*} [Group G] [TopologicalSpace G] {m n : ℕ}
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) G] (p : LieGroupPresentation G m) : m = n := by
  sorry
```

Identifiers: `Topology.IsEmbedding` (`Mathlib/Topology/Defs/Induced.lean`), `unitInterval` (`Mathlib/Topology/UnitInterval.lean`), `Set.InjOn`, `ContinuousOn`.

---

## 7. Recommended order of attack toward `hilbert_fifth_problem`

**Target chain.** The input is `[IsTopologicalGroup G] [T2Space G] [ChartedSpace (EuclideanSpace ℝ (Fin n)) G]`. From it:

- locally compact (`ChartedSpace.locallyCompactSpace`) and locally connected (`ChartedSpace.locallyConnectedSpace`);
- **NSS** (§7: Lemmas 7.1, 7.5, 7.6, Cor. 7.7, plus invariance of domain);
- **`G` is Lie** (§§5–6, Cor. 6.10, plus results 2, 3, 4, plus the open-subgroup gluing);
- `LieGroupPresentation G n` with the same `n` (invariance of dimension).

**Suggested order.**

1. **Infrastructure (low risk).**
   - `HasNoSmallSubgroups`; `𝔏(G) := Multiplicative ℝ →ₜ* G` with Mathlib's compact-open topology; scalar action `(rξ)(t) = ξ(rt)`.
   - Lemmas 2.1, 2.8 and 2.9.
   - The NSS facts (1)–(6) of §2, taking (3) from TauCeti.
   - Gluing: "open Lie subgroup ⇒ Lie" and "linear re-modelling to `𝓡 d`".
2. **Decide on NSA.** I recommend replacing the nonstandard arguments of §§2–7 by standard ones (Tao GSM 153, Ch. 5 "Gleason–Yamabe"; or rewrite vdDG's monad arguments with neighbourhood filters). This avoids formalizing κ-saturated ultrapowers. If NSA is kept, "κ-rich extensions exist" is the axiom to postulate.
3. **Weak Peter–Weyl (result 1).** Port or bridge TauCeti's `exists_contRepresentation_apply_ne` (needs the Mathlib bump) to the `GL (Fin n) ℝ` draft in §1b. Then prove Thm 4.1 and Cor. 4.2 (easy).
4. **§5 (Gleason–Yamabe lemmas, Lemma 5.4 → Thm 5.8 → Lemma 5.10 → Cor. 5.11).** This is the hardest *original* part of the paper and is independent of results 2–5. It uses Haar measure, Urysohn and uniform continuity, all in Mathlib.
5. **§6 for NSS groups.** Riesz (`FiniteDimensional.of_locallyCompactSpace`), Lemma 6.7, Cor. 6.8, Lemma 6.9 (`Ad` continuous, `ker Ad = Z(G₀)`).
6. **Result 2 by the elementary route** (abelian ⇒ `exp` is a homomorphism ⇒ translation charts).
7. **Result 4 by route (C)**: §6 applied to `H = G₀/Z`, plus Mathlib's analytic matrix exp/log and the analytic inverse function theorem, plus continuous 1-ps of `GLₙ` (from TauCeti's `expUnitHom` results or a direct proof).
8. **Result 3 (central Kuranishi)**: last. Formalize via Tao §2.6 once 5 is in place for `N` and `G/N`.
9. **§7** (locally Euclidean ⇒ NSS): Lemma 7.1 (uses Lemma 5.4), Cor. 7.2, Lemmas 7.4–7.6, Cor. 7.7, plus invariance of domain.
10. **Dimension matching** `LieGroupPresentation.dim_eq` (invariance of dimension).

**Reasonable `sorry`'d axioms** (each a well-known published theorem, stated in the drafts above):

- **Kuranishi, central case** (`admitsLieGroupStructure_of_central_extension`). Highest cost-to-insight ratio; not in any Lean library.
- **Invariance of domain / dimension** (`invariance_of_domain`, `not_exists_isEmbedding_cube`, `LieGroupPresentation.dim_eq`). Likely to land in Mathlib (PR #36770 plus a Brouwer formalization); swap it in later.
- **von Neumann's theorem** (`admitsLieGroupStructure_of_injective_GL`), if route (C) is postponed.
- **Weak Peter–Weyl**, only if porting TauCeti is blocked by the version mismatch. Otherwise take it from TauCeti.
- **κ-rich nonstandard extensions**, only if the NSA presentation is kept.

The genuinely new content of vdDG (§§3, 5–7) should **not** be axiomatized; it is the point of the exercise.

**Things I could not verify.**

- The exact statements and proofs in Kuranishi 1950, Gleason 1951 and Iwasawa 1949 (ams.org, numdam and JSTOR are blocked).
- The full text of Tao's 254A Notes 2 and 3 and of GSM 153, including the hypotheses of Thm 2.6.1. Only search snippets were seen.
- The DOIs for Kuranishi 1950, Iwasawa 1949, Brouwer 1912 and Hilgert–Neeb.
- Whether ℵ₁-saturation suffices for the paper's NSA when `G` is first countable.
- Route 4(C) and the half-page argument in §2a are my own reductions, not quoted from a source. They should be checked by a human before formalizing.



# Hilbert's 5th Problem

Lou van den DRIES and Isaac GOLDBRING

**Abstract.** Assuming a modest amount of background we give full proofs of the results by Gleason, Montgomery–Zippin, and Yamabe that characterize Lie groups and generalized Lie groups among topological groups. Our treatment involves nonstandard reasoning, and we expose this method in an appendix.

**Mathematics Subject Classification (2010).** Primary: 22D05; Secondary: 03H05.

**Keywords.** Hilbert's fifth problem, Lie groups, no small subgroups, nonstandard analysis.

## 1. Introduction

A Lie group is a topological group  $G$  for which inversion  $x \mapsto x^{-1} : G \rightarrow G$  and multiplication  $(x, y) \mapsto xy : G \times G \rightarrow G$  are analytic maps with respect to some compatible real analytic manifold structure on its underlying topological space. It is a remarkable fact that then there is only one such real analytic manifold structure. This uniqueness falls under the slogan

$$\text{Algebra} \times \text{Topology} = \text{Analysis}.$$

Important Lie groups are the vector groups  $\mathbb{R}^n$ , their compact quotients  $\mathbb{R}^n/\mathbb{Z}^n$ , the general linear groups  $\text{GL}_n(\mathbb{R})$ , and the orthogonal groups  $\text{O}_n(\mathbb{R})$ . For each of these the group structure and the real analytic manifold structure is the obvious one; for example,  $\text{GL}_n(\mathbb{R})$  is open as a subset of  $\mathbb{R}^{n^2}$ , and thus an open submanifold of the analytic manifold  $\mathbb{R}^{n^2}$ . Here and throughout this paper we let  $m$  and  $n$  range over  $\mathbb{N} = \{0, 1, 2, \dots\}$ .

Hilbert's 5th problem asks for a characterization of Lie groups that is free of smoothness or analyticity requirements. A topological group is said to be *locally euclidean* if some neighborhood of its identity is homeomorphic to some  $\mathbb{R}^n$ . A Lie group is obviously locally euclidean, and the most common version of Hilbert's 5th problem (H5) can be stated as follows:

### *Is every locally euclidean topological group a Lie group?*

A positive solution to this problem was achieved in the early fifties by the combined efforts of Gleason [3] and Montgomery & Zippin [15]. Yamabe improved their results in [21] and [22]. Montgomery & Zippin exposed all of this and more in their book [16] on topological transformation groups. Kaplansky has also a nice treatment in Chapter 2 of [13]. Of course, the affirmative solution of H5 gives further substance to our crude slogan.

We are oversimplifying the story: Hilbert’s original formulation [8] is in terms of a (local) group of homeomorphisms on a topological manifold. This suggests a problem that is still open: if a locally compact group  $G$  acts continuously and faithfully on a topological manifold, is  $G$  necessarily a Lie group? See Serre [19] and Palais [18] for brief accounts that discuss this more general form of H5. Serre considers the state of H5 just before the decisive papers [3] and [15], and Palais focuses on Gleason’s contribution.

Locally euclidean topological groups are certainly locally compact. (We include being hausdorff as part of compactness and of local compactness.) Local compactness yields a powerful analytic tool, namely Haar measure, and we shall need it. *From now on  $G$  denotes a locally compact (topological) group, with identity 1, or  $1_G$  if we want to indicate  $G$ .*

A notion that has turned out to be central in the story is that of having no small subgroups:  $G$  is said to have *no small subgroups* (briefly:  $G$  has NSS) if there is a neighborhood  $U$  of 1 in  $G$  that contains no subgroup of  $G$  other than  $\{1\}$ . It is also useful to introduce a weaker variant of this property:  $G$  is said to have *no small connected subgroups* (briefly:  $G$  has NSCS) if there is a neighborhood  $U$  of 1 in  $G$  that contains no connected subgroup of  $G$  other than  $\{1\}$ . Dimension theory also plays a modest role: call a topological space *bounded in dimension* if for some  $n$  no subspace is homeomorphic to the unit cube  $[0, 1]^n$ . Recalling that throughout  $G$  is locally compact, we can now formulate the main result as characterizing Lie groups among locally compact topological groups:

**Main Theorem.** *Given  $G$ , the following are equivalent:*

- (1)  $G$  is a Lie group;
- (2)  $G$  has NSS;
- (3)  $G$  is locally euclidean;
- (4)  $G$  is locally connected and has NSCS;
- (5)  $G$  is locally connected and bounded in dimension.

In (1) and throughout this paper we take the definition of “Lie group” from the beginning of this Introduction: it only requires existence (not uniqueness) of a

compatible real analytic manifold structure. While the identity in a Lie group has a countable neighborhood base, such countability issues play no explicit role in our treatment.

We say that  $G$  *can be approximated by Lie groups* if every neighborhood of its identity contains a compact normal subgroup  $N$  of  $G$  such that  $G/N$  (with its quotient topology) is a Lie group. The following result, due to Yamabe, is closely related to the Main Theorem, and is important in the structure theory of locally compact groups.

**Theorem.** *Every locally compact group has an open subgroup that can be approximated by Lie groups.*

Hirschfeld [9] used nonstandard methods to simplify some tricky parts of the work by Gleason and Montgomery. The present paper is meant to give an account of [9] with further simplifications, and some minor corrections. We also include a proof of Yamabe's Theorem, and an appendix on nonstandard methods for readers not familiar with them. In the rest of this introduction we give more history and sketch the solution to (global) H5.

**Further relevant history.** The clearcut formulation of H5 above became only possible after basic topological notions had crystallized sufficiently in the 1920's to permit the definition of "topological group" by Schreier. The fundamental tool of Haar measure, on any locally compact group, became available soon afterwards. Von Neumann used it to extend the Peter-Weyl theorem for compact Lie groups to all compact groups, and this led to the solution of H5 for *compact* groups. (In our treatment of H5 we use a weak form of this extended Peter-Weyl theorem.) Another important partial solution of H5 is for the case of *commutative*  $G$ , due to Pontrjagin, and we shall need this as well. Finally, we are going to use a result of Kuranishi [14]:

*if  $G$  has a commutative closed normal subgroup  $N$  such that  $N$  and  $G/N$  are Lie groups, then  $G$  is a Lie group.*

Gleason [4] and Iwasawa [11] establish this without assuming commutativity of  $N$ , but we don't need this stronger version and instead obtain it as a consequence of the Main Theorem; see Section 2.

Goldbring [5] elaborated Hirschfeld's approach to solve affirmatively the *local* form of H5. (A solution to local H5 was claimed already in [12], but about 20 years ago it was found that this paper was seriously wrong; see [17].)

Gromov [6] made a remarkable use of the results from the 1950's around H5 in his proof that a finitely generated group has polynomial growth if and only if the group has a nilpotent subgroup of finite index; see also [2].

Recently, Hrushovski [\[10\]](#) and Breuillard-Green-Tao [\[1\]](#) used the solution of H5 (even the local form) and Yamabe’s theorem to elucidate the structure of finite approximate groups. In this connection, and for another full account of H5, see also Tao [\[20\]](#).

**One-parameter subgroups.** Lie theory provides a precious guide towards solving H5. It tells us that the tangent vectors at the identity of a Lie group are in a natural bijective correspondence with the 1-parameter subgroups of the Lie group. While tangent vectors require a manifold to live on, the notion of 1-parameter subgroup makes sense in any topological group.

A 1-*parameter subgroup* (or 1-*ps*) of  $G$  is a continuous group morphism  $\mathbb{R} \rightarrow G$ . The trivial 1-parameter subgroup  $o$  of  $G$  is defined by  $o(t) = 1 \in G$  for all  $t \in \mathbb{R}$ . We set

$$\mathfrak{L}(G) := \{\xi : \mathbb{R} \rightarrow G \mid \xi \text{ is a 1-ps of } G\}.$$

For  $r \in \mathbb{R}$  and  $\xi \in \mathfrak{L}(G)$  we define  $r\xi \in \mathfrak{L}(G)$  by  $(r\xi)(t) := \xi(rt)$ , and we also denote  $(-1)\xi$  by  $-\xi$ . Note that then  $0\xi = o$ ,  $1\xi = \xi$ ,  $-\xi = \xi^{-1}$ , and  $r(s\xi) = (rs)\xi$  for  $r, s \in \mathbb{R}$  and  $\xi \in \mathfrak{L}(G)$ . The operation

$$(r, \xi) \mapsto r\xi : \mathbb{R} \times \mathfrak{L}(G) \rightarrow \mathfrak{L}(G)$$

will be referred to as *scalar multiplication*.

**The case of Lie groups.** Suppose  $G$  is a Lie group. Then each  $\xi \in \mathfrak{L}(G)$  is analytic as a function from  $\mathbb{R}$  to  $G$ , and thus determines a velocity vector  $\xi'(0) \in T_1(G)$  at the point  $1 \in G$ . This gives the bijection

$$\xi \mapsto \xi'(0) : \mathfrak{L}(G) \rightarrow T_1(G)$$

mentioned above. It respects scalar multiplication:  $(r\xi)'(0) = r\xi'(0)$ . The addition operation on  $\mathfrak{L}(G)$  that makes this bijection an isomorphism of vector spaces over  $\mathbb{R}$  is as follows: for  $\xi, \eta \in \mathfrak{L}(G)$  and  $s$  ranging over  $\mathbb{R}^{>0}$ ,

$$(\xi + \eta)(t) = \lim_{s \rightarrow \infty} \left(\xi(1/s)\eta(1/s)\right)^{[st]}.$$

We make  $\mathfrak{L}(G)$  a real analytic manifold such that the  $\mathbb{R}$ -linear isomorphisms  $\mathfrak{L}(G) \cong \mathbb{R}^n$ , with  $n := \dim G = \dim_{\mathbb{R}} \mathfrak{L}(G)$ , are analytic isomorphisms. Then the so-called *exponential map*

$$\xi \mapsto \xi(1) : \mathfrak{L}(G) \rightarrow G$$

yields an analytic isomorphism from an open neighborhood of  $o$  in  $\mathfrak{L}(G)$  onto an open neighborhood of  $1$  in  $G$ .

**Sketch why NSS implies Lie.** These facts about Lie groups suggest that we should try to establish  $\mathcal{L}(G)$  as a substitute tangent space at 1, towards finding a compatible manifold structure on  $G$ . Note in this connection that the exponential map  $\xi \mapsto \xi(1) : \mathcal{L}(G) \rightarrow G$  is defined for any  $G$ . This is our clue to proving the key implication  $\text{NSS} \Rightarrow \text{Lie}$  in the Main Theorem.

Indeed, we shall take the following steps towards proving this implication. Suppose  $G$  has NSS.

- (1) Show that for any  $\xi, \eta \in \mathcal{L}(G)$  there is an  $\xi + \eta \in \mathcal{L}(G)$  given by

$$(\xi + \eta)(t) = \lim_{s \rightarrow \infty} (\xi(1/s)\eta(1/s))^{[st]}, \quad (s \text{ ranging over } \mathbb{R}^{>0})$$

and that this addition operation and the scalar multiplication make  $\mathcal{L}(G)$  a vector space over  $\mathbb{R}$ .

- (2) Equip  $\mathcal{L}(G)$  with its compact-open topology (defined below) and show that this makes  $\mathcal{L}(G)$  a *topological* vector space.
- (3) Show that the exponential map  $\xi \mapsto \xi(1) : \mathcal{L}(G) \rightarrow G$  maps some neighborhood of  $o$  in  $\mathcal{L}(G)$  homeomorphically onto a neighborhood of 1 in  $G$ . Then local compactness of  $G$  yields local compactness of  $\mathcal{L}(G)$  and hence the finite-dimensionality of  $\mathcal{L}(G)$  as a vector space over  $\mathbb{R}$ . It follows that  $G$  is locally euclidean.
- (4) Replacing  $G$  by the connected component of 1, we can assume that  $G$  is connected. Then the adjoint representation (defined below) of  $G$  on the finite-dimensional vector space  $\mathcal{L}(G)$  has as its kernel a commutative closed normal subgroup  $N$  of  $G$ , and yields an injective continuous group morphism  $G/N \rightarrow \text{GL}_n(\mathbb{R})$ . Since  $N$  has NSS, it is locally euclidean by (3). But  $N$  is also commutative, and hence a Lie group (Pontrjagin). The injective continous group morphism  $G/N \rightarrow \text{GL}_n(\mathbb{R})$  makes  $G/N$  a Lie group (E. Cartan, von Neumann). Apply the Kuranishi theorem to conclude that  $G$  is a Lie group.

Step (1) is tricky, and requires ingenious constructions due to Gleason and Yamabe. Step (2) is easy, and step (3) is of intermediate difficulty. Step (4) is a reduction of the problem to a situation that that was well-understood before 1950. New in our treatment is that we carry out steps (1) and (2) without requiring NSS: local compactness of  $G$  is enough. Some of (3) and (4) can also be done in this generality, and this is the first thing we shall take care of in the next section.

**Sketch why every locally euclidean  $G$  has NSS.** This is the other key implication in the Main Theorem, and it passes through the other equivalent conditions (4) and (5) in the Main Theorem. This goes roughly as follows. When we have done step (1) above for all  $G$ , without assuming NSS, we can use this to prove the following implications:

- if  $G$  is locally connected and has NSCS, then  $G$  has NSS;
- if  $G$  does not have NSCS, then  $G$  contains a homeomorphic copy of  $[0, 1]^n$  for all  $n$ .

It only remains to observe that if  $G$  is locally euclidean, then  $G$  is locally connected (trivially), and bounded in dimension (by Brouwer).

**Acknowledgement.** We thank Emmanuel Breuillard for suggesting that our original seminar notes from 2007 might be worth publishing, and the referee for many comments that were helpful in improving the exposition.

## 2. Preliminaries

Throughout this paper  $G$  and  $H$  are locally compact groups. A set  $U \subseteq G$  is said to be *symmetric* if  $U^{-1} = U$ . Given a closed normal subgroup  $N$  of  $G$  we give  $G/N$  its quotient topology; it makes  $G/N$  a locally compact group. We also give  $\mathbb{R}$  its usual topology, and each  $\mathbb{R}^n$  the corresponding product topology. Any  $n$ -dimensional vector space over  $\mathbb{R}$  is given the topology that makes the  $\mathbb{R}$ -linear isomorphisms with  $\mathbb{R}^n$  into homeomorphisms.

In this section we state some basic facts on  $\mathcal{L}(G)$  and its compact-open topology. We also list some some elementary facts about locally compact groups having NSS, and introduce the nonstandard setting that will enable an efficient account of the solution of H5.

### Generalities on one-parameter groups.

**Lemma 2.1.** *Suppose  $\xi \in \mathcal{L}(G)$  and  $\xi \neq o$ . Then either  $\ker \xi = \{0\}$  or  $\ker \xi = \mathbb{Z}r$  with  $r \in \mathbb{R}^{>0}$ . In the first case  $\xi$  maps each bounded interval  $(-a, a)$  ( $a \in \mathbb{R}^{>0}$ ) homeomorphically onto its image in  $G$ . In the second case  $\xi$  maps the interval  $(-\frac{r}{2}, \frac{r}{2})$  homeomorphically onto its image in  $G$ .*

*Proof.* This follows from two well-known facts: a closed subgroup of the additive group of  $\mathbb{R}$  different from  $\{0\}$  and  $\mathbb{R}$  is of the form  $\mathbb{Z}r$  with  $r \in \mathbb{R}^{>0}$ , and any continuous bijection from a compact space onto a hausdorff space is a homeomorphism.  $\square$

For  $\xi, \eta \in \mathcal{L}(G)$  we say that  $\xi + \eta$  *exists* if  $\lim_{s \rightarrow \infty} (\xi(1/s)\eta(1/s))^{[st]}$  exists in  $G$  for all  $t \in \mathbb{R}$ , with  $s$  ranging over  $\mathbb{R}^{>0}$ . In that case the map

$$t \mapsto \lim_{s \rightarrow \infty} (\xi(1/s)\eta(1/s))^{[st]} : \mathbb{R} \rightarrow G$$

is a 1-ps of  $G$ , and we define  $\xi + \eta$  to be this 1-ps.

**Lemma 2.2.** *Let  $\xi, \eta \in \mathcal{L}(G)$  and  $p, q \in \mathbb{R}$ .*

- (1)  $\xi + o$  exists and equals  $\xi$ ;
- (2)  $p\xi + q\xi$  exists and equals  $(p + q)\xi$ ;
- (3) if  $\xi + \eta$  exists, then  $\eta + \xi$  exists and equals  $\xi + \eta$ ;
- (4) if  $\xi + \eta$  exists, then  $p\xi + p\eta$  exists and equals  $p(\xi + \eta)$ .

*Proof.* We leave (1) and (2) to the reader. Note that (2) yields that  $\xi + (-\xi)$  exists and equals  $o$ . For (3), use that for  $s \in \mathbb{R}^{>0}$  and  $a = \xi(1/s)$ ,  $b = \eta(1/s)$  we have  $ba = b(ab)b^{-1}$ , so  $(ba)^n = b(ab)^n b^{-1}$ . Item (4) is easy when  $p > 0$ . To reduce the case  $p < 0$  to this case one first shows that if  $\xi + \eta$  exists, then  $(-\xi) + (-\eta)$  exists, and equals  $-(\xi + \eta)$ .  $\square$

We define the *adjoint action* of  $G$  on  $\mathcal{L}(G)$  to be the left action

$$(a, \xi) \mapsto a\xi a^{-1} : G \times \mathcal{L}(G) \rightarrow \mathcal{L}(G), \quad (a\xi a^{-1})(t) := a\xi(t)a^{-1},$$

of  $G$  on the set  $\mathcal{L}(G)$ . Then each  $a \in G$  gives a bijection

$$\text{Ad}(a) : \mathcal{L}(G) \rightarrow \mathcal{L}(G), \quad \text{Ad}(a)(\xi) := a\xi a^{-1},$$

and for  $r \in \mathbb{R}$  and  $\xi \in \mathcal{L}(G)$  we have  $\text{Ad}(a)(r\xi) = r \text{Ad}(a)(\xi)$ . If  $\xi, \eta \in \mathcal{L}(G)$  and  $\xi + \eta$  exists, then  $\text{Ad}(a)(\xi) + \text{Ad}(a)(\eta)$  exists and equals  $\text{Ad}(a)(\xi + \eta)$ .

**Corollary 2.3.** *Suppose that  $\xi + \eta$  exists for all  $\xi, \eta \in \mathcal{L}(G)$ , and that the binary operation  $+$  on  $\mathcal{L}(G)$  is associative. Then  $\mathcal{L}(G)$  with  $+$  as its addition and the usual scalar multiplication is a vector space over  $\mathbb{R}$  with  $o$  as zero element, and we have a group morphism  $a \mapsto \text{Ad}(a) : G \rightarrow \text{Aut}(\mathcal{L}(G))$  of  $G$  into the group of automorphisms of the vector space  $\mathcal{L}(G)$ .*

In the situation of this corollary the map  $a \mapsto \text{Ad}(a) : G \rightarrow \text{Aut}(\mathcal{L}(G))$  is called the *adjoint representation* of  $G$ .

Next, consider a continuous group morphism  $\phi : G \rightarrow H$ . Then we have a map

$$\mathcal{L}(\phi) : \mathcal{L}(G) \rightarrow \mathcal{L}(H), \quad \mathcal{L}(\phi)(\xi) := \phi \circ \xi,$$

and  $\mathcal{L}(\phi)(r\xi) = r\mathcal{L}(\phi)(\xi)$  for all  $r \in \mathbb{R}$  and  $\xi \in \mathcal{L}(G)$ . Also, if  $\xi, \eta \in \mathcal{L}(G)$  and  $\xi + \eta$  exists, so does  $\mathcal{L}(\phi)(\xi) + \mathcal{L}(\phi)(\eta)$  and

$$\mathcal{L}(\phi)(\xi + \eta) = \mathcal{L}(\phi)(\xi) + \mathcal{L}(\phi)(\eta).$$

If  $\phi$  is injective, so is  $\mathcal{L}(\phi)$ . In particular, if  $G$  is a subgroup of  $H$  with the subspace topology and  $\phi$  is the inclusion map, then we identify  $\mathcal{L}(G)$  with a

subset of  $\mathcal{L}(H)$  via  $\mathcal{L}(\phi)$ . With  $N = \ker(\phi)$  (a closed subgroup of  $G$ ) and  $o_H$  the trivial 1-ps of  $H$  we have

$$\mathcal{L}(\phi)^{-1}(o_H) = \mathcal{L}(N).$$

Note that assigning to each  $G$  the set  $\mathcal{L}(G)$  and to each  $\phi$  as above the map  $\mathcal{L}(\phi)$  yields a functor  $\mathcal{L}$  from the category of locally compact groups and continuous group morphisms into the category of sets.

**Generalities on NSS.** By “NSS-group” we mean a locally compact group that has NSS. Here are some examples of NSS-groups, and some basic facts about them that we shall use freely:

- (1) if  $G$  is discrete, then  $G$  has NSS;
- (2) the additive group of  $\mathbb{R}$  has NSS;
- (3)  $\mathrm{GL}_n(\mathbb{R})$  has NSS;
- (4) if  $G_1, \dots, G_n$  are NSS-groups, so is  $G_1 \times \dots \times G_n$ ;
- (5) if  $\phi : G \rightarrow H$  is a continuous group morphism,  $\phi$  is injective on a neighborhood of 1 in  $G$ , and  $H$  has NSS, then  $G$  has NSS.
- (6) if  $N$  is a closed normal subgroup of  $G$  such that  $N$  and  $G/N$  have NSS, then  $G$  has NSS.

Only the proof of (3) might not be obvious. Hint: Suppose  $A \in \mathrm{GL}_n(\mathbb{R})$  is close to the identity  $I$  of  $\mathrm{GL}_n(\mathbb{R})$ , but  $A \neq I$ . Then  $A = I + E$  where  $E \in \mathrm{M}_n(\mathbb{R})$  is close to but different from the zero matrix. Now use that

$$A^m = I + mE + \binom{m}{2}E^2 + \dots + E^m$$

is close to  $I + mE$  (for suitable  $m$ ). Note also that the Main Theorem and (6) yield the Gleason–Iwasawa result mentioned in the Introduction.

**The nonstandard setting.** A careful reading of the appendix should give enough background to work in this setting. Here we just fix notations and terminology. To each relevant “basic” set  $S$  corresponds a set  $S^* \supseteq S$ , the *star extension* of  $S$ . Among these basic sets are  $\mathbb{R}, G$ , their power sets  $\mathcal{P}(\mathbb{R}), \mathcal{P}(G)$ , and even power sets  $\mathcal{P}(\mathbb{R} \times G)$  of certain cartesian products, as needed. We make the usual Mostowski identification of the star extension  $\mathcal{P}(\mathbb{R})^*$  with a subset of  $\mathcal{P}(\mathbb{R}^*)$ , and likewise with other powersets. Thus each  $X \subseteq \mathbb{R}$  extends to  $X^*$ , an internal subset of  $\mathbb{R}^*$ . Also, any (relevant) relation  $R$  and function  $F$  on these basic sets extends to a relation  $R^*$  and function  $F^*$  on the corresponding star extensions of these basic sets. For example, the linear ordering  $<$  on  $\mathbb{R}$  extends to a linear

ordering  $<^*$  on  $\mathbb{R}^*$ , and the group operation  $p : G \times G \rightarrow G$  of  $G$  extends to a group operation  $p^* : G^* \times G^* \rightarrow G^*$ . For the sake of readability we often drop the star when indicating the star extension of a relation or function between these basic sets. As an example, for  $x, y \in \mathbb{R}^*$  we use  $x + y$  and  $x < y$  to abbreviate the cumbersome expressions  $x +^* y$  and  $x <^* y$ ; likewise, the star extension  $\xi^* : \mathbb{R}^* \rightarrow G^*$  of a 1-ps  $\xi : \mathbb{R} \rightarrow G$  is usually indicated just by  $\xi$ .

As usual in nonstandard reasoning, we leave it mainly to the context as to what are the basic sets and basic relations among them: just take what is needed by the arguments. As to the degree of saturation of the nonstandard extension, it is enough to assume  $\kappa^+$ -saturation where  $\kappa$  is any infinite cardinal such that  $\kappa \geq \#S$  for each basic set  $S$ . Actually, we use  $\kappa$ -richness rather than  $\kappa^+$ -saturation, since in the setting of the appendix  $\kappa$ -richness is easier to define but equivalent to  $\kappa^+$ -saturation.

Given an ambient hausdorff space  $S$  and  $s \in S$ , the *monad* of  $s$ , notation:  $\mu(s)$ , is by definition the intersection of all  $U^* \subseteq S^*$  with  $U$  a neighborhood of  $s$  in  $S$ ; think of the elements of  $\mu(s)$  as the points of  $S^*$  that are *infinitely close* to  $s$ . The points of  $S^*$  that are infinitely close to some  $s \in S$  are called *nearstandard*, and  $S_{\text{ns}}$  is the set of nearstandard points of  $S^*$ :

$$S_{\text{ns}} := \bigcup_{s \in S} \mu(s).$$

In particular,  $S \subseteq S_{\text{ns}}$ . Since  $S$  is hausdorff,  $\mu(s) \cap \mu(s') = \emptyset$  for distinct  $s, s' \in S$ . Thus we can define the *standard part*  $\text{st}(x)$  of  $x \in S_{\text{ns}}$  to be the unique  $s \in S$  such that  $x \in \mu(s)$ . We also introduce the equivalence relation  $\sim$  on  $S_{\text{ns}}$  whose equivalence classes are the monads:

$$x \sim y :\iff \text{st}(x) = \text{st}(y) \quad (\text{"}x \text{ and } y \text{ are infinitely close"}).$$

Notation: for  $U \subseteq S$  we let  $\text{cl}(U)$  and  $\text{int}(U)$  be the closure of  $U$  and the interior of  $U$  in the space  $S$ . We prove here two well-known basic facts.

**Lemma 2.4.** *Suppose  $U \subseteq S$  has compact closure  $\text{cl}(U)$ . Then  $U^* \subseteq S_{\text{ns}}$  and  $\text{st}(U^*) = \text{cl}(U)$ .*

*Proof.* Let  $x \in U^*$ , and suppose  $x \notin S_{\text{ns}}$ . Then each  $a \in \text{cl}(U)$  has a neighborhood  $U_a$  in  $S$  such that  $x \notin U_a^*$ . Take  $a_1, \dots, a_n \in \text{cl}(U)$  such that  $\text{cl}(U) \subseteq U_{a_1} \cup \dots \cup U_{a_n}$ . Then  $U \subseteq U_{a_1} \cup \dots \cup U_{a_n}$ , so  $x \in U^* \subseteq U_{a_1}^* \cup \dots \cup U_{a_n}^*$ , a contradiction. This argument gives  $U^* \subseteq S_{\text{ns}}$ . Let again  $x \in U^*$ . Then for each neighborhood  $V$  of  $\text{st}(x)$  in  $S$  we have  $x \in V^*$ , so  $V^* \cap U^* \neq \emptyset$ , and thus  $V \cap U \neq \emptyset$ . Thus  $\text{st}(x) \in \text{cl}(U)$ . Conversely, let  $a \in \text{cl}(U)$ . Then  $V \cap U \neq \emptyset$  for every neighborhood  $V$  of  $a$  in  $S$ , so  $V^* \cap U^* \neq \emptyset$  for such  $V$ . By richness this gives  $\mu(a) \cap U^* \neq \emptyset$ , so  $a \in \text{st}(U^*)$ .  $\square$

**Lemma 2.5.** *Suppose  $S$  is a regular hausdorff space and  $X$  is an internal subset of  $S^*$  such that  $X \subseteq S_{\text{ns}}$ . Then  $\text{st}(X) \subseteq S$  is compact.*

*Proof.* Let for each point  $p \in \text{st}(X)$  an open neighborhood  $U_p \subseteq S$  of  $p$  be given. It suffices to show that then finitely many of the  $U_p$  cover  $\text{st}(X)$ . By regularity we can pick for each  $p \in \text{st}(X)$  an open neighborhood  $V_p \subseteq S$  of  $p$  such that  $\text{cl}(V_p) \subseteq U_p$  (and thus  $\text{st}(V_p^*) \subseteq U_p$ ). From  $X \subseteq S_{\text{ns}}$  we obtain  $X \subseteq \bigcup_{p \in \text{st}(X)} V_p^*$ , which by richness yields  $X \subseteq V_{p_1}^* \cup \dots \cup V_{p_n}^*$  with  $p_1, \dots, p_n \in \text{st}(X)$ . Then  $\text{st}(X) \subseteq U_{p_1} \cup \dots \cup U_{p_n}$ .  $\square$

Note that  $G_{\text{ns}} = \bigcup_{g \in G} \mu(g)$  is a subgroup of  $G^*$ , and that the standard part map  $\text{st} : G_{\text{ns}} \rightarrow G$  is a group morphism that is the identity on  $G$ . We let  $\mu := \mu(1) = \ker(\text{st})$  denote the normal subgroup of *infinitesimals* of  $G_{\text{ns}}$ . The equivalence relation  $\sim$  on  $G_{\text{ns}}$  is given by:

$$a \sim b \iff ab^{-1} \in \mu, \quad (a, b \in G_{\text{ns}}).$$

Recall from the introduction that  $m, n$  range over  $\mathbb{N}$ . In addition we let  $i, j$  range over  $\mathbb{N}^*$ ,  $\nu$  over  $\mathbb{N}^* \setminus \mathbb{N}$ , and  $k$  over  $\mathbb{Z}^*$ . Also,  $\sigma$  will always denote a positive infinite element of  $\mathbb{R}^*$ . We adopt Landau’s “big O” and “little o” notation in the following way: for  $x, y \in \mathbb{R}^*$  with  $y > 0$ ,  $x = o(y)$  means that  $|x| < y/n$  for all  $n \geq 1$ , and  $x = O(y)$  means that  $|x| < ny$  for some  $n \geq 1$ . We also adapt it to  $G$  as follows:

$$\begin{aligned} O[\sigma] &= O_G[\sigma] := \{a \in \mu \mid a^i \in \mu \text{ for all } i = o(\sigma)\}, \\ o[\sigma] &= o_G[\sigma] := \{a \in \mu \mid a^i \in \mu \text{ for all } i = O(\sigma)\} \\ &= \{a \in \mu \mid a^i \in \mu \text{ for all } i \leq \sigma\}. \end{aligned}$$

So  $o[\sigma] \subseteq O[\sigma] \subseteq \mu \subseteq G_{\text{ns}}$ , and  $o[\sigma]$  and  $O[\sigma]$  are closed under  $a \mapsto a^\ell$ , for each  $\ell \in \mathbb{Z}$ ; in particular, these sets are symmetric. By Theorem 5.8 below,  $o[\sigma]$  and  $O[\sigma]$  are normal subgroups of  $G_{\text{ns}}$ . At this point it is clear that if  $a \in G_{\text{ns}}$  and  $b \in O[\sigma]$ ,  $c \in o[\sigma]$ , then  $aba^{-1} \in O[\sigma]$  and  $aca^{-1} \in o[\sigma]$ .

**Lemma 2.6.** *If  $a \in O[\sigma]$ , then  $a^i \in G_{\text{ns}}$  for all  $i = O(\sigma)$ .*

*Proof.* Let  $a \in O[\sigma]$ , and take a compact symmetric neighborhood  $U$  of 1 in  $G$ . If  $a^i \in U^*$  for all  $i = O(\sigma)$ , then  $a^i \in G_{\text{ns}}$  for all  $i = O(\sigma)$ , as desired. Suppose  $a^j \notin U^*$  for some  $j = O(\sigma)$ , and take  $j$  minimal with this property. Then  $a^i \in G_{\text{ns}}$  with  $\text{st}(a^i) \in U$  for  $i = 0, \dots, j$ . We cannot have  $j = o(\sigma)$ , so  $\sigma = O(j)$ . Therefore, if  $i = O(\sigma)$ , then  $i = nj + i'$  with  $i' < j$ , and thus  $a^i = (a^j)^n a^{i'} \in G_{\text{ns}}$ .  $\square$

The next lemma indicates why  $O[\sigma]$  is of interest: its elements generate the one-parameter subgroups of  $G$  in a very intuitive way.

**Lemma 2.7.** *Let  $a \in O[\sigma]$ . Then the map  $\xi_a : \mathbb{R} \rightarrow G$  defined by  $\xi_a(t) := \text{st}(a^{[\sigma t]})$  is a 1-ps of  $G$ . Moreover:*

- (1)  $\xi_a^\ell = \ell \xi_a$  for all  $\ell \in \mathbb{Z}$ ;
- (2)  $b \in \mu \implies \xi_{bab^{-1}} = \xi_a$ ;
- (3)  $\xi_a = o \iff a \in o[\sigma]$ ;
- (4)  $\mathfrak{L}(G) = \{\xi_b \mid b \in O[\sigma]\}$ .

*Proof.* It is clear that  $\xi_a$  is a group morphism. To show continuity at  $0 \in \mathbb{R}$ , let  $U$  be a neighborhood of 1 in  $G$ . Take a neighborhood  $V$  of 1 in  $G$  such that  $\text{cl}(V) \subseteq U$ . Since  $a^k \in \mu \subseteq V^*$  for all  $k = o(\sigma)$ , we have  $n \geq 1$  such that  $a^k \in V^*$  whenever  $|k| < \sigma/n$ . Also  $a^k \in G_{\text{ns}}$  for such  $k$ , so  $\text{st}(a^k) \in \text{cl}(V)$  whenever  $|k| < \sigma/n$ . Hence  $\xi_a(t) = \text{st}(a^{[\sigma t]}) \in U$  whenever  $t \in \mathbb{R}$  and  $|t| < 1/n$ . The remaining assertions follow easily. In connection with (4) we note that for  $\xi \in \mathfrak{L}(G)$  and  $b := \xi(1/\sigma)$  we have  $b \in O[\sigma]$  and  $\xi = \xi_b$ .  $\square$

**The compact-open topology.** Let  $P$  be a locally compact space,  $Q$  a hausdorff space, and  $C(P, Q)$  the set of continuous maps  $P \rightarrow Q$ . For compact  $K \subseteq P$  and open  $U \subseteq Q$ , put

$$O(K, U) := \{f \in C(P, Q) \mid f(K) \subseteq U\}.$$

We equip  $C(P, Q)$  with its *compact-open topology*; this is the topology on  $C(P, Q)$  that has the finite intersections of these sets  $O(K, U)$  as basic open sets; it makes  $C(P, Q)$  into a hausdorff space, and makes the evaluation map

$$\Phi : C(P, Q) \times P \rightarrow Q, \quad \Phi(f, p) := f(p),$$

continuous. Let  $A$  be any subset of  $P$  and  $F$  be a closed subset of  $Q$ . Then

$$\{f \in C(P, Q) \mid f(A) \subseteq F\}$$

is closed, since its complement in  $C(P, Q)$  is the union over all  $a \in A$  of the open sets

$$\{f \in C(P, Q) \mid f(a) \notin F\}.$$

A nonstandard view of the compact-open topology is as follows: Let  $f \in C(P, Q)$  and  $g \in C(P, Q)^*$ ; then

$$g \in \mu(f) \iff g(p') \in \mu(f(p)) \text{ for all } p \in P \text{ and } p' \in \mu(p).$$

We apply this to the case where  $P = \mathbb{R}$  is the real line and  $Q = G$ . Then  $\mathcal{L}(G)$  is closed in  $C(\mathbb{R}, G)$ , and below  $\mathcal{L}(G)$  is given the topology induced on it by the (compact-open) topology of  $C(\mathbb{R}, G)$ . Let  $I := [-1, 1] \subseteq \mathbb{R}$ . Let  $\xi \in \mathcal{L}(G)$ . Then every neighborhood  $U$  of 1 in  $G$  determines a neighborhood

$$N_\xi(U) := \{\eta \in \mathcal{L}(G) \mid \eta(t) \in \xi(t)U \text{ for all } t \in I\}$$

of  $\xi$  in  $\mathcal{L}(G)$ , and the collection

$$\{N_\xi(U) \mid U \text{ is a neighborhood of 1 in } G\}$$

is a neighborhood base of  $\xi$  in  $\mathcal{L}(G)$ . (These facts are easy to verify using the above characterization of monads in the compact-open topology.)

**Lemma 2.8.** *The following maps are continuous:*

- (1) *the exponential map*  $\xi \mapsto \xi(1) : \mathcal{L}(G) \rightarrow G$ ;
- (2) *the scalar multiplication map*  $(r, \xi) \mapsto r\xi : \mathbb{R} \times \mathcal{L}(G) \rightarrow \mathcal{L}(G)$ ;
- (3) *the adjoint action map*  $G \times \mathcal{L}(G) \rightarrow \mathcal{L}(G)$ .

*Proof.* Item (1) follows from the continuity of evaluation in the compact-open topology. To prove (2), let  $\xi \in \mathcal{L}(G)$  and  $r \in \mathbb{R}$ , and let  $\xi' \in \mathcal{L}(G)^*$  and  $r' \in \mathbb{R}^*$  be such that  $\xi' \in \mu(\xi)$  and  $r' \in \mu(r)$ ; it suffices to show that then  $r'\xi' \in \mu(r\xi)$ . Let  $t' \in \mathbb{R}^*$  with  $t' \in \mu(t)$ ,  $t \in \mathbb{R}$ ; then  $r't' \in \mu(rt)$ , so

$$(r'\xi')(t') = \xi'(r't') \in \mu(\xi(rt)) = \mu((r\xi)(t)).$$

This argument shows that  $r'\xi' \in \mu(r\xi)$ , as desired.  $\square$

**Lemma 2.9.** *Suppose  $\mathcal{U} \subseteq G$  is a compact neighborhood of 1 in  $G$  and contains no subgroups of  $G$  other than  $\{1\}$ . Then the set*

$$\mathcal{K} := \{\xi \in \mathcal{L}(G) \mid \xi(I) \subseteq \mathcal{U}\}$$

*is a compact neighborhood of  $o$  in  $\mathcal{L}(G)$ .*

*Proof.* Let  $\eta \in \mathcal{K}^*$ , that is,  $\eta \in \mathcal{L}(G)^*$  and  $\eta(I^*) \subseteq \mathcal{U}^*$ . If  $\epsilon \in \mathbb{R}^*$  is infinitesimal, then  $\text{st}(\eta(\mathbb{Z}\epsilon)) \subseteq \mathcal{U}$  is a subgroup of  $G$ , so  $\eta(\epsilon) \in \mu$ . Hence for each neighborhood  $V$  of 1 in  $G$  there is  $n > 0$  such that  $\eta(r) \in V^*$  for all  $r \in \mathbb{R}^*$  with  $|r| < 1/n$ . Consequently,  $\xi : \mathbb{R} \rightarrow G$  defined by  $\xi(t) = \text{st}(\eta(t))$  is a 1-ps with  $\xi(I) \subseteq \mathcal{U}$ , and  $\eta \in \mu(\xi)$ .  $\square$

## 3. Generating compact connected subgroups

Throughout this section we let  $a$  range over  $G^*$ . We say that  $a$  is *degenerate* if  $a^i \in \mu$  for all  $i$ . (Recall that  $i$  ranges over  $\mathbb{N}^*$ .)

**Lemma 3.1.**  *$G$  has NSS iff  $G^*$  has no degenerate elements other than 1.*

*Proof.* We show the contrapositives. Suppose  $G$  does not have NSS. Take an internal neighborhood  $U \subseteq \mu$  of 1 in  $G^*$ . Then  $U$  must contain a nontrivial internal subgroup  $H$  of  $G^*$ , and so any  $a \in H$  is degenerate.

Next, assume  $a \neq 1$  is degenerate. Let  $U$  be any neighborhood of 1 in  $G$ . Then  $a^{\mathbb{Z}^*} \subseteq \mu \subseteq U^*$ , so  $U^*$  contains a nontrivial internal subgroup of  $G^*$ , and thus  $U$  contains a nontrivial subgroup of  $G$ .  $\square$

At this stage we do not restrict attention to NSS-groups, so we do allow degenerate elements  $\neq 1$  in  $\mu$ . Nondegenerate elements in  $\mu$  give rise to nontrivial connected subgroups of  $G$ , by the following elementary fact:

**Lemma 3.2.** *Let  $a_1, \dots, a_v$  be an internal sequence in  $G^*$  such that  $a_i \in \mu$  and  $a_1 \cdots a_i \in G_{\text{ns}}$  for all  $i \in \{1, \dots, v\}$ . Then the set*

$$S := \{ \text{st}(a_1 \cdots a_i) \mid 1 \leq i \leq v \} \subseteq G$$

*is compact and connected (and contains 1).*

*Proof.* The compactness of  $S$  follows from Lemma 2.5. Assume  $S$  is not connected. Then we have disjoint open subsets  $U$  and  $V$  of  $G$  such that  $S \subseteq U \cup V$  and  $S$  meets both  $U$  and  $V$ . We can assume that  $1 \in U$ , so  $a_1 \in U^*$ . There are  $i \leq v$  such that  $\text{st}(a_1 \cdots a_i) \in V$ , and  $a_1, \dots, a_i \in V^*$  for such  $i$ . Take  $i \leq v$  minimal such that  $a_1 \cdots a_i \in V^*$ . Then  $i \geq 2$  and  $a_1 \cdots a_{i-1} \in U^*$ . Now  $a := \text{st}(a_1 \cdots a_{i-1}) = \text{st}(a_1 \cdots a_i) \in S$ . If  $a \in U$ , this gives  $a_1 \cdots a_i \in U^*$ , and if  $a \in V$ , it gives  $a_1 \cdots a_{i-1} \in V^*$ , and we have a contradiction in either case.  $\square$

In the rest of this section  $U$  is a compact symmetric neighborhood of  $1 \in G$ . If  $a^{\mathbb{N}^*} \subseteq U^*$  (in particular, if  $a$  is degenerate), then we set  $\text{ord}_U(a) = \infty$ ; if  $a^{\mathbb{N}^*} \not\subseteq U^*$ , then we let  $\text{ord}_U(a)$  be the largest  $j$  such that  $a^i \in U^*$  for all  $i \leq j$ . Thus  $\text{ord}_U(a) = 0$  iff  $a \notin U^*$ , and  $\text{ord}_U(a) > \mathbb{N}$  if  $a \in \mu$ . By convention,  $k = o(\infty)$  for every  $k$ .

**Lemma 3.3.** *Suppose  $a \in \mu$  and  $a^i \notin \mu$  for some  $i = o(\text{ord}_U(a))$ . Then  $U$  contains a nontrivial connected subgroup of  $G$ .*

*Proof.* By the previous lemma the set

$$G_U(a) := \left\{ \text{st}(a^k) \mid k = o(\text{ord}_U(a)) \right\}$$

is a union of connected subsets of  $U$ , each containing 1, and is thus itself a connected subset of  $U$ . It is also a subgroup of  $G$ .  $\square$

An element  $a \in \mu$  is said to be  $U$ -pure if for some  $v$  we have  $a \in O[v]$  and  $a^{v+1} \notin U^*$ ; note that then  $a$  is nondegenerate,  $\text{ord}_U(a) \neq \infty$ , and the above holds for  $v = \text{ord}_U(a)$ . If  $U$  contains no nontrivial connected subgroup of  $G$ , then by Lemma 3.3 every nondegenerate  $a \in \mu$  is  $U$ -pure.

An element  $a \in \mu$  is said to be *pure* if it is  $V$ -pure for some compact symmetric neighborhood  $V$  of 1 in  $G$ . Thus:

**Corollary 3.4.** *If  $G$  has NSCS, then every nondegenerate  $a \in \mu$  is pure.*

**Lemma 3.5.** *Let  $a \in \mu$ . Then  $a$  is pure iff there is  $v$  such that  $a \in O[v]$  and  $a^v \notin \mu$ .*

*Proof.* If  $a$  is  $U$ -pure, say, then for  $v = \text{ord}_U(a)$  we have  $a \in O[v]$  and  $a^v \notin \mu$ . Conversely, let  $v$  be such that  $a \in O[v]$  and  $a^v \notin \mu$ . If  $\text{ord}_U(a) = O(v)$ , then  $a$  is  $U$ -pure. If  $v = O(\text{ord}_U(a))$ , then  $a^v \in G_{\text{ns}}$ , and we can take a compact symmetric neighborhood  $V$  of 1 in  $G$  such that  $a^v \notin V^*$ , and then  $a$  is  $V$ -pure.  $\square$

Let  $Q$  range over internal symmetric subsets of  $G^*$  such that  $1 \in Q \subseteq \mu$ . We define  $Q^i$  to be the internal subset of  $G^*$  consisting of all  $a_1 \cdots a_i$  where  $a_1, \dots, a_i$  is an internal sequence in  $Q$ . Thus

$$Q^\infty := \bigcup_i Q^i$$

is the internal subgroup of  $G^*$  internally generated by  $Q$ .

We say that  $Q$  is *degenerate* if  $Q^\infty \subseteq \mu$ . If  $Q^\infty \not\subseteq U^*$ , then we let  $\text{ord}_U(Q)$  be the largest  $j$  such that  $Q^j \subseteq U^*$ , and if  $Q^\infty \subseteq U^*$ , then we set  $\text{ord}_U(Q) := \infty$ . Thus  $e := \text{ord}_U(Q) > \mathbb{N}$ . We set

$$G_U(Q) := \left\{ \text{st}(a) \mid a \in Q^i \text{ for some } i = o(e) \right\} = \bigcup_{i=o(e)} \text{st}(Q^i).$$

Recall that  $\text{int}(U)$  denotes the interior of  $U$  in  $G$ .

**Lemma 3.6.** *If  $e \neq \infty$ , then  $\text{st}(Q^e) \not\subseteq \text{int}(U)$ .*

*Proof.* Assume  $e \neq \infty$ , and take  $b \in Q^e$  such that  $bq \notin U^*$  for some  $q \in Q$ . One checks easily that then  $\text{st}(b) \notin \text{int}(U)$ .  $\square$

**Lemma 3.7.**  *$G_U(Q)$  is a compact connected subgroup of  $G$  contained in  $U$ . In particular, if  $Q^j \not\subseteq \mu$  for some  $j = o(e)$ , then  $U$  contains a nontrivial compact connected subgroup of  $G$ .*

*Proof.* The set  $G_U(Q)$  is the union of the increasing family of subsets  $\text{st}(Q^j)$  of  $G$  with  $j = o(e)$ . We claim: there exists  $j_0 = o(e)$  such that  $\text{st}(Q^j) = \text{st}(Q^{j_0})$  for all  $j = o(e)$  with  $j \geq j_0$ . Suppose there were no such  $j_0$ . Then transfinite recursion yields a (well-ordered) set  $J$  of elements  $j = o(e)$  such that (a) for all  $j \in J$  there is a  $g_j \in \text{st}(Q^j)$  with  $g_j \notin \text{st}(Q^i)$  whenever  $i \in J, i < j$ , and (b) for every  $i = o(e)$  there is a  $j \in J$  with  $i < j$ . From (a) we get  $\#J \leq \#G$ , where  $\#S$  denotes the cardinality of a set  $S$ . Since for every  $j \in J$  and  $n \geq 1$  there is an  $i$  with  $i > j$  and  $i < e/n$  and we are in a  $\kappa$ -rich structure with  $\kappa \geq \#G$ , we get  $i > J$  with  $i = o(e)$ , but this contradicts (b). This proves our claim.

Let  $j_0$  be as in the claim. Then  $G_U(Q) = \text{st}(Q^{j_0})$ , so  $G_U(Q)$  is compact by Lemma 2.5. As in the proof of Lemma 3.3,  $G_U(Q)$  is a union of connected subsets of  $U$ , each containing 1, and is thus itself a connected subset of  $U$ . It is also a subgroup of  $G$ .  $\square$

## 4. Compact groups

**Theorem 4.1.** *Let  $G$  be compact and  $U$  an open neighborhood of 1 in  $G$ . Then there is a continuous injective group morphism  $G/N \rightarrow \text{GL}_n(\mathbb{R})$  for some  $n$  and some closed normal subgroup  $N$  of  $G$  contained in  $U$ .*

*Proof.* The Peter-Weyl theorem yields for any  $a \neq 1$  in  $G$  a continuous group morphism  $\phi_a : G \rightarrow \text{GL}_{n_a}(\mathbb{R})$  that does not have  $a$  in its kernel  $N_a$ . As  $a$  varies over  $G \setminus U$ , the open sets  $G \setminus N_a$  cover  $G \setminus U$ , so there are  $a_1, \dots, a_m \in G \setminus U$  such that  $N := N_{a_1} \cap \dots \cap N_{a_m}$  is contained in  $U$ . Then the desired result holds for this  $N$  and  $n := n_{a_1} + \dots + n_{a_m}$ .  $\square$

**Corollary 4.2.** *Let  $G$  be compact and  $U$  a neighborhood of 1 in  $G$ . Then there is a closed normal subgroup  $N$  of  $G$  contained in  $U$  and an open set  $V$  in  $G$  such that  $N \subseteq V \subseteq U$  and every subgroup of  $G$  contained in  $V$  is contained in  $N$ .*

*Proof.* We can assume that  $U$  is open, and then we take  $N$  as in the previous theorem, so that  $G/N$  has NSS. Take an open neighborhood  $W$  of the identity

in  $G/N$  that contains no nontrivial subgroup of  $G/N$ . Let  $V := \pi^{-1}(W) \cap U$ , where  $\pi : G \rightarrow G/N$  is the natural map. Then  $V$  has the desired property.  $\square$

## 5. Gleason–Yamabe Lemmas and their Consequences

This is the most technical part of the story. The leading idea is to make  $G$  act by isometries on its space of real-valued continuous functions with compact support, and to use the Haar integral on this space.

**Gleason–Yamabe Lemmas.** Throughout this subsection we fix a compact symmetric neighborhood  $\mathcal{U}$  of 1 in  $G$  and a continuous function  $\tau : G \rightarrow [0, 1]$  such that

$$\tau(1) = 1, \quad \tau(x) = 0 \text{ for all } x \in G \setminus \mathcal{U}.$$

Let  $Q \subseteq \mathcal{U}$  be symmetric with  $1 \in Q$  and let  $e$  be a positive integer with  $Q^e \subseteq \mathcal{U}$ . Define the function  $\Delta = \Delta_{Q,e} : G \rightarrow [0, 1]$  by

- (i)  $\Delta(1) = 0$ ;
- (ii)  $\Delta(x) = i/(e + 1)$  if  $x \in Q^i \setminus Q^{i-1}$ ,  $1 \leq i \leq e$ ;
- (iii)  $\Delta(x) = 1$  if  $x \notin Q^e$ .

Then for all  $x \in G$ ,

- (iv)  $\Delta(x) = 1$  if  $x \notin \mathcal{U}$ ;
- (v)  $|\Delta(ax) - \Delta(x)| \leq 1/e$  for  $a \in Q$ .

Now use  $\tau$  to smooth  $1 - \Delta$ : define  $\theta = \theta_{Q,e} : G \rightarrow [0, 1]$  by

$$\theta(x) = \sup_{y \in G} (1 - \Delta(y))\tau(y^{-1}x) = \sup_{y \in \mathcal{U}} (1 - \Delta(y))\tau(y^{-1}x).$$

The following properties are easy consequences:

- (1)  $\theta$  is continuous, and  $\theta(x) = 0$  outside  $\mathcal{U}^2$ ;
- (2)  $0 \leq \tau \leq \theta \leq 1$ ;
- (3)  $|\theta(ax) - \theta(x)| \leq 1/e$  for  $a \in Q$ ;

For continuity of  $\theta$ , note that if  $a \in \mu$  and  $x \in G$ , then  $\theta(xa) - \theta(x)$  is infinitesimal in  $\mathbb{R}^*$ . To prove (3), let  $a \in Q$ , and note that for all  $x, y \in G$ ,

$$|(1 - \Delta(a^{-1}y)) - (1 - \Delta(y))| \leq 1/e,$$

and  $y^{-1}ax = (a^{-1}y)^{-1}x$ , so

$$\left| (1 - \Delta(y))\tau(y^{-1}ax) - (1 - \Delta(a^{-1}y))\tau((a^{-1}y)^{-1}x) \right| \leq 1/e,$$

which gives (3).

Let  $C$  be the real vector space of continuous functions  $G \rightarrow \mathbb{R}$  with compact support, with norm given by  $\|f\| = \sup_{x \in G} |f(x)|$ . We have a left action  $G \times C \rightarrow C$  of  $G$  on  $C$  given by

$$(a, f) \mapsto af, \quad (af)(x) = f(a^{-1}x).$$

More suggestively,  $(af)(ax) = f(x)$  for  $a, x \in G$ ,  $f \in C$ . It is clear that for  $a \in G$  the map  $f \mapsto af$  is an  $\mathbb{R}$ -linear isometry of  $C$  onto itself, and thus,

$$\|abf - f\| \leq \|af - f\| + \|bf - f\| \quad (a, b \in G, f \in C).$$

We have the following useful equicontinuity result:

- (4) for each  $\varepsilon \in \mathbb{R}^{>0}$  there is a neighborhood  $V_\varepsilon$  of 1 in  $G$ , independent of  $(Q, e)$ , such that  $\|a\theta - \theta\| \leq \varepsilon$  for all  $a \in V_\varepsilon$ .

To see why, let  $\varepsilon \in \mathbb{R}^{>0}$ . Uniform continuity of  $\tau$  gives a neighborhood  $U$  of 1 in  $G$  such that  $|\tau(g) - \tau(h)| < \varepsilon$  for all  $g, h \in G$  with  $gh^{-1} \in U$ . Take a neighborhood  $V_\varepsilon$  of 1 in  $G$  such that  $y^{-1}ay \in U$  for all  $(y, a) \in \mathcal{U} \times V_\varepsilon$ . Then  $|\tau(y^{-1}ax) - \tau(y^{-1}x)| < \varepsilon$  for  $x \in G$ ,  $y \in \mathcal{U}$  and  $a \in V_\varepsilon$ . This gives (4).

A second smoothing will be done by integration. Take the unique left-invariant Haar measure  $\mu$  on  $G$  such that  $\mu(\mathcal{U}^2) = 1$ . (Left-invariance means that  $\int f(ax)d\mu(x) = \int f(x)d\mu(x)$  for  $f \in C$  and  $a \in G$  and  $f \in C$ .) Then

- (5)  $0 \leq \int \theta(x)d\mu(x) \leq 1$ , by (1) and (2).

We now introduce the function

$$\phi = \phi_{Q,e} : G \rightarrow \mathbb{R}, \quad \phi(x) := \int \theta(xu)\theta(u) d\mu(u).$$

Thus  $\phi$ , a convolution of two functions in  $C$ , is continuous, and we have:

- (6)  $\phi(x) = 0$  outside  $\mathcal{U}^4$ ;
- (7)  $\phi(1) \geq \int \tau(u)^2 d\mu(u) > 0$ , by (2);
- (8)  $\|a\phi - \phi\| \leq \|a\theta - \theta\|$  for all  $a \in G$ ;
- (9) if  $a \in Q$ , then  $\|a\phi - \phi\| \leq 1/e$ , by (3) and (8).

The significance of (7) is that the positive lower bound  $\int \tau(u)^2 d\mu(u)$  on  $\phi(1)$  is independent of  $(Q, e)$ .

**Lemma 5.1.** *Let  $\varepsilon \in \mathbb{R}^{>0}$ . Then there is a neighborhood  $U = U_\varepsilon \subseteq \mathcal{U}$  of 1 in  $G$ , independent of  $(Q, e)$ , such that for all  $a \in Q$  and  $b \in U$ ,*

$$\|b \cdot (a\phi - \phi) - (a\phi - \phi)\| \leq \frac{\varepsilon}{e}.$$

*Proof.* Let  $a \in Q$ ,  $b \in \mathcal{U}$ . Then, with  $x \in G$  and  $y := b^{-1}x$ ,

$$\begin{aligned} (a\phi - \phi)(x) &= \int [\theta(a^{-1}xu) - \theta(xu)]\theta(u)d\mu(u) \\ b(a\phi - \phi)(x) &= (a\phi - \phi)(y) = \int [\theta(a^{-1}yu) - \theta(yu)]\theta(u) d\mu(u). \end{aligned}$$

By the left-invariance of our Haar measure we can replace  $u$  by  $x^{-1}yu$  in the function of  $u$  integrated in the first identity, so

$$(a\phi - \phi)(x) = \int [\theta(a^{-1}yu) - \theta(yu)]\theta(x^{-1}yu) d\mu(u).$$

Taking differences gives

$$[b \cdot (a\phi - \phi) - (a\phi - \phi)](x) = \int [(a\theta - \theta)(yu)][(\theta - y^{-1}x\theta)(u)] d\mu(u).$$

If the left hand side here is nonzero, then  $x \in \mathcal{U}^4$  or  $a^{-1}x \in \mathcal{U}^4$  or  $b^{-1}x \in \mathcal{U}^4$  or  $a^{-1}b^{-1}x \in \mathcal{U}^4$ , and thus  $x \in \mathcal{U}^6$  in all cases. Also  $y^{-1}x = x^{-1}bx$ , so by (4) we can take the neighborhood  $U_{c,\varepsilon} \subseteq \mathcal{U}$  of 1 in  $G$  so small that for all  $b \in U_\varepsilon$  and  $x \in \mathcal{U}^6$  we have  $y^{-1}x \in \mathcal{U}$  and  $\|\theta - y^{-1}x\theta\| < \varepsilon/\mu(\mathcal{U}^3)$ . Then  $U_\varepsilon$  has the desired property.  $\square$

**Lemma 5.2.** *With  $\varepsilon \in \mathbb{R}^{>0}$ , let  $U = U_\varepsilon$  be as in the previous lemma and let  $a \in Q$  and  $n \geq 1$  be such that  $a^i \in U$  for  $i = 0, \dots, n$ . Then*

$$\|(a^n\phi - \phi) - n(a\phi - \phi)\| \leq \frac{n\varepsilon}{e}.$$

*Proof.* We have  $a^n\phi - \phi = \sum_{i=0}^{n-1} a^i(a\phi - \phi)$ , so

$$(a^n\phi - \phi) - n(a\phi - \phi) = \sum_{i=0}^{n-1} a^i(a\phi - \phi) - (a\phi - \phi).$$

By the previous lemma we have for  $i = 0, \dots, n-1$ ,

$$\|a^i(a\phi - \phi) - (a\phi - \phi)\| \leq \frac{\varepsilon}{e},$$

which gives the desired result by summation.  $\square$

Suppose now that  $Q$  is a symmetric internal subset of  $G^*$  with  $1 \in Q$  and  $Q \subseteq \mu$ . Let  $e \in \mathbb{N}^*$  be such that  $e \geq 1$  and  $Q^e \subseteq \mathcal{U}^*$ . Then the constructions and results above transfer automatically to the nonstandard setting and yield internally continuous functions

$$\theta = \theta_{Q,e} : G^* \rightarrow [0, 1]^*, \quad \phi = \phi_{Q,e} : G^* \rightarrow \mathbb{R}^*$$

satisfying the internal versions of (1)–(9) and Lemmas 5.1 and 5.2. With these assumptions we have

**Corollary 5.3.** *Suppose  $a \in Q$ ,  $v = O(e)$ , and  $a \in o[v]$ . Then*

$$v\|a\phi - \phi\| \sim 0.$$

*Proof.* By Lemma 5.2 we have for each  $\varepsilon \in \mathbb{R}^{>0}$ ,

$$\|(a^v\phi - \phi) - v(a\phi - \phi)\| \leq \frac{v\varepsilon}{e},$$

so the lefthand side in this inequality is infinitesimal. Also, by (8) and (4) we have  $\|a^v\phi - \phi\| \leq \|a^v\theta - \theta\|$ , so  $\|a^v\phi - \phi\|$  is infinitesimal.  $\square$

### Consequences of the Gleason–Yamabe Lemmas.

**Lemma 5.4.** *Let  $a_1, \dots, a_v$  be an internal sequence in  $G^*$  such that all  $a_i \in o[v]$ . Then  $a_1 \cdots a_v \in \mu$ .*

*Proof.* Put  $Q := \{1, a_1, \dots, a_v, a_1^{-1}, \dots, a_v^{-1}\}$ , and towards a contradiction, suppose that  $Q^v \not\subseteq \mu$ . Take a compact symmetric neighborhood  $U$  of 1 in  $G$  such that  $Q^{v+1} \not\subseteq U^*$ , so  $\text{ord}_U(Q) \leq v$ . By decreasing  $v$  if necessary, and  $Q$  accordingly, we arrange that  $\text{ord}_U(Q) = v$  or  $\text{ord}_U(Q) = v - 1$ .

Consider first the special case that  $Q^i \subseteq \mu$  for all  $i = o(v)$ . (This occurs if  $G$  has NSCS). Take  $b \in Q^v$  such that  $\text{st}(b) \neq 1$ , and then take a compact symmetric neighborhood  $\mathcal{U} \subseteq U$  of 1 in  $G$  such that  $\text{st}(b) \notin \mathcal{U}^4$ , and put  $e := \text{ord}_{\mathcal{U}}(Q)$ , so  $v = O(e)$ . The previous subsection yields an internally continuous function  $\phi = \phi_{Q,e} : G^* \rightarrow \mathbb{R}^*$  satisfying the internal versions of (6)-(9) and Lemma 5.3. In particular,  $\phi(x) = 0$  outside  $(\mathcal{U}^*)^4$  (hence  $\phi(b^{-1}) = 0$ ), and  $\phi(1)$  is not infinitesimal. Then  $\|b\phi - \phi\|$  is not infinitesimal. Take an internal sequence  $b_1, \dots, b_v$  in  $Q$  such that  $b = b_1 \cdots b_v$ . Then Lemma 5.3 yields

$$\|b\phi - \phi\| \leq \sum_{i=1}^v \|b_i\phi - \phi\| \sim 0,$$

and we have a contradiction.

Next, assume that  $Q^i \not\subseteq \mu$  for some  $i = o(v)$ . Then we set

$$H := G_U(Q) = \{\text{st}(b) \mid b \in Q^i \text{ for some } i = o(v)\},$$

so  $H$  is a nontrivial compact subgroup of  $G$  contained in  $U$ , by Lemma 3.7. By Corollary 4.2 we can take a proper closed normal subgroup  $N$  of  $H$  and a compact symmetric neighborhood  $V \subseteq U$  of 1 in  $G$  such that  $N \subseteq \text{int}(V)$  and every subgroup of  $H$  contained in  $V$  is contained in  $N$ . Put  $\mu := \text{ord}_V(Q)$ , so  $\mathbb{N} < \mu \leq v$ , and we have the compact subgroup

$$G_V(Q) = \{\text{st}(b) \mid b \in Q^i \text{ for some } i = o(\mu)\}$$

of  $H$  with  $G_V(Q) \subseteq V$ , so  $G_V(Q) \subseteq N$ . By Lemma 3.6 we can take  $b \in Q^\mu$  with  $\text{st}(b) \notin \text{int}(V)$ . Then  $\text{st}(b) \notin N$ , so we can take a compact symmetric neighborhood  $\mathcal{U}$  of 1 in  $G$  such that  $N \subseteq \text{int}(\mathcal{U})$ ,  $\mathcal{U}^4 \subseteq V$  and  $\text{st}(b) \notin \mathcal{U}^4$ .

Put  $e := \text{ord}_{\mathcal{U}}(Q)$ . If  $e = \text{o}(\mu)$ , then  $\text{st}(Q^e) \subseteq G_V(Q) \subseteq N$ , contradicting  $\text{st}(b) \notin N$ . This shows  $\mu = \text{O}(e)$ . The rest of the proof now proceeds as in the special case considered earlier, with  $\nu$  replaced by  $\mu$ , and  $b_1, \dots, b_\nu$  by an internal sequence  $b_1, \dots, b_\mu$  in  $Q$  such that  $b = b_1 \cdots b_\mu$ .  $\square$

**Corollary 5.5.** *Let  $a_1, \dots, a_\nu$  be an internal sequence in  $G^*$  such that all  $a_i \in \text{O}[\nu]$ . Then  $a_1 \cdots a_\nu \in G_{\text{ns}}$ .*

*Proof.* If  $a_1 \cdots a_\nu \in \mathcal{U}^*$ , we are done. Assume otherwise. Take the least  $j$  with  $a_i \cdots a_{i+j} \notin \mathcal{U}^*$  for some  $i$  with  $1 \leq i < i+j \leq \nu$ . Then by the previous lemma we cannot have  $j = \text{o}(\nu)$ , and this gives  $n \geq 1$  with  $nj \leq \nu < (n+1)j$ . Hence

$$a_1 \cdots a_\nu = (a_1 \cdots a_j)(a_{j+1} \cdots a_{2j}) \cdots (a_{nj+1} \cdots a_\nu) \in (\mathcal{U}^*)^n \subseteq G_{\text{ns}}.$$

$\square$

**Lemma 5.6.** *If  $a \in \text{O}[\nu]$  and  $b \in \text{o}[\nu]$ , then  $(ab)^i \sim a^i$  for all  $i \leq \nu$ .*

*Proof.* Set  $b_i := a^i b a^{-i}$ . Then  $(ab)^i = b_1 \cdots b_i \cdot a^i$ . Assuming  $a \in \text{O}[\nu]$  and  $b \in \text{o}[\nu]$ , we have  $b_i \in \text{o}[\nu]$  for  $i \leq \nu$  by Lemma 2.6 and the remark preceding it, so  $b_1 \cdots b_i \in \mu$  for all  $i \leq \nu$ , by Lemma 5.4.  $\square$

**Lemma 5.7.** *Suppose that  $a, b \in \text{O}[\nu]$  and  $a^i \sim b^i$  for all  $i \leq \nu$ . Then  $a^{-1}b \in \text{o}[\nu]$ .*

*Proof.* If  $a \in \text{o}[\nu]$ , then  $b \in \text{o}[\nu]$ , so  $(a^{-1}b)^i \sim a^{-i} \in \mu$  for all  $i \leq \nu$ , and we are done. So we can assume that  $a \notin \text{o}[\nu]$ , and then, replacing  $\nu$  by an element of  $\mathbb{N}^*$  of the same archimedean class, we have  $a^\nu \notin \mu$ . Let  $Q := \{1, a, a^{-1}, b, b^{-1}\}$ . Then  $Q^i \subseteq \mu$  for all  $i = \text{o}(\nu)$  by Lemma 5.4, and  $Q^\nu \subseteq G_{\text{ns}}$  by Corollary 5.5. Suppose towards a contradiction that  $(a^{-1}b)^j \notin \mu$ , where  $j \leq \nu$ . Then  $\nu = \text{O}(j)$ . Take a compact symmetric neighborhood  $\mathcal{U}$  of 1 in  $G$  such that  $a^\nu \notin \mathcal{U}$  and  $(a^{-1}b)^j \notin \mathcal{U}^4$ , and put  $e = \text{ord}_{\mathcal{U}}(Q)$ , so  $e$  and  $\nu$  have the same archimedean class. As before we have the internally continuous function  $\phi = \phi_{Q,e} : G^* \rightarrow \mathbb{R}^*$  satisfying the internal versions of (6)–(9) and Lemma 5.3. Then  $\phi((a^{-1}b)^j) = 0$  and  $\varepsilon := \phi(1) > 0$  is not infinitesimal, and thus

$$\begin{aligned} \varepsilon &\leq \|(b^{-1}a)^j \phi - \phi\| \leq j \|(b^{-1}a)\phi - \phi\| \\ &= j \|a\phi - b\phi\| = j \|(a\phi - \phi) - (b\phi - \phi)\|. \end{aligned}$$

where the first equality uses the first line of the proof of Lemma 5.2. The desired contradiction will be obtained by showing that

$$j \|(a\phi - \phi) - (b\phi - \phi)\| < \varepsilon.$$

Let  $\delta \in \mathbb{R}^{>0}$ ; then Lemma 5.2 gives a compact symmetric neighborhood  $U \subseteq \mathcal{U}$  of 1 in  $G$  such that if  $k > 0$  and  $a^i, b^i \in U^*$  for all  $i \leq k$ , then

$$\begin{aligned} \|(a^k\phi - \phi) - k(a\phi - \phi)\| &\leq k\delta/e, & \|(b^k\phi - \phi) - k(b\phi - \phi)\| &\leq k\delta/e, \text{ so} \\ \left\|\frac{j}{k}(a^k\phi - \phi) - j(a\phi - \phi)\right\| &\leq j\delta/e, & \left\|\frac{j}{k}(b^k\phi - \phi) - j(b\phi - \phi)\right\| &\leq j\delta/e. \end{aligned}$$

Choose  $\delta \in \mathbb{R}^{>0}$  such that  $j\delta/e < \varepsilon/3$ , and put  $k := \min(\text{ord}_U(a), \text{ord}_U(b))$ . Then  $k < \nu$  and  $a^i, b^i \in U^*$  for all  $i \leq k$ , and therefore

$$\left\|\frac{j}{k}(a^k\phi - \phi) - j(a\phi - \phi)\right\| < \varepsilon/3, \quad \left\|\frac{j}{k}(b^k\phi - \phi) - j(b\phi - \phi)\right\| < \varepsilon/3.$$

Also  $\nu = O(k)$ , and hence  $j/k < n$  for some  $n$ . Since  $a^k \sim b^k$ , this gives

$$\|(j/k)(a^k\phi - \phi) - (j/k)(b^k\phi - \phi)\| = (j/k)\|a^k\phi - b^k\phi\| \sim 0.$$

In view of the earlier inequalities, this yields

$$\|j(a\phi - \phi) - j(b\phi - \phi)\| < \varepsilon,$$

as promised. □

Recall that  $\sigma \in \mathbb{R}^*$ ,  $\sigma > \mathbb{R}$ .

**Theorem 5.8.** *The sets  $O[\sigma]$  and  $o[\sigma]$  have the following properties:*

- (1)  $O[\sigma]$  and  $o[\sigma]$  are normal subgroups of  $G_{\text{ns}}$ ;
- (2) if  $a \in O[\sigma]$  and  $b \in \mu$ , then  $[a, b] := aba^{-1}b^{-1} \in o[\sigma]$ ;
- (3)  $O[\sigma]/o[\sigma]$  is commutative, and  $O[\sigma]/o[\sigma] \subseteq \text{center}(\mu/o[\sigma])$ .

*Proof.* As to (1), let  $a, b \in O[\sigma]$ . Then  $(ab)^i \in \mu$  for all  $i = o(\sigma)$  by Lemma 5.4, so  $ab \in O[\sigma]$ . Thus  $O[\sigma]$  is a normal subgroup of  $G_{\text{ns}}$ . For  $i = O(\sigma)$  this argument shows that  $o[\sigma]$  is a normal subgroup of  $G_{\text{ns}}$ . Item (2) follows from the previous lemma. Item (3) is immediate from (2). □

**$\mathfrak{L}(G)$  as a topological vector space.** It follows from Lemma 5.6 that for  $a \in O[\sigma]$  and  $b \in o[\sigma]$  we have  $\xi_a = \xi_{ab}$ , so we have a surjective map

$$a o[\sigma] \mapsto \xi_a : O[\sigma]/o[\sigma] \rightarrow \mathfrak{L}(G).$$

By Lemma 5.7 we also have for  $a, b ext{ ∈ } ext{O}[σ]$  that if  $ξ_a = ξ_b$ , then  $a^{-1}b ext{ ∈ } ext{o}[σ]$ , so the above map is a bijection. We make  $rak{L}(G)$  into an abelian group with group operation  $+_σ$  so that this bijection is a group isomorphism  $ext{O}[σ]/ ext{o}[σ] o rak{L}(G)$ , in other words,  $ξ_a +_σ ξ_b = ξ_{ab}$  for  $a, b ext{ ∈ } ext{O}[σ]$ . Note that  $ξ_a +_σ ξ_a = 2ξ_a$  for  $a ext{ ∈ } ext{O}[σ]$ . To show that this operation  $+_σ$  is independent of  $σ$ , we need the next lemma. In its proof we use that for  $g, h ext{ ∈ } G$  and  $[g, h] := ghg^{-1}h^{-1}$  we have  $gh = [g, h]hg$ .

**Lemma 5.9.** *Let  $a, b ext{ ∈ } ext{o}[
u]$  and  $a^
u ext{ ∈ } ext{O}[σ]$ . Then  $(ab)^
u = ca^
u b^
u$  with  $c ext{ ∈ } ext{o}[σ]$ . Likewise,  $(ba)^
u = b^
u a^
u d$  with  $d ext{ ∈ } ext{o}[σ]$ .*

*Proof.* We define  $c_i := [a^{i-1}, [b^{i-1}, a]][b^{i-1}, a] ext{ ∈ } μ$  for  $i = 1, ext{...}, 
u$ , so  $c_1 = 1$ . We claim that then  $(ab)^i = c_1 ext{ ⋯ } c_i a^i b^i$ . This is clear for  $i = 1$ . Assume the claim holds for a certain  $i < 
u$ . Then

$$\begin{aligned} (ab)^{i+1} &= c_1 \cdots c_i a^i b^i ab = c_1 \cdots c_i a^i [b^i, a] a b^{i+1} \\ &= c_1 \cdots c_i [a^i, [b^i, a]] [b^i, a] a^{i+1} b^{i+1} = c_1 \cdots c_{i+1} a^{i+1} b^{i+1}. \end{aligned}$$

This proves our claim. Now  $a^
u ext{ ∈ } ext{O}[σ]$  gives  $a ext{ ∈ } ext{O}[
uσ]$ , so  $[b^i, a] ext{ ∈ } ext{o}[
uσ]$  for  $0 ext{ ≤ } i < 
u$ , hence  $c_i ext{ ∈ } ext{o}[
uσ]$  for  $1 ext{ ≤ } i ext{ ≤ } 
u$ . Put  $c := c_1 ext{ ⋯ } c_
u$ . Then for  $1 ext{ ≤ } j ext{ ≤ } σ$ , the element  $c^j = (c_1 ext{ ⋯ } c_
u)^j$  is a product of  $j
u ext{ ≤ } 
uσ$  elements, each in  $ext{o}[
uσ]$ , so  $c^j ext{ ∈ } μ$  by Lemma 5.4, and thus  $c ext{ ∈ } ext{o}[σ]$ , as desired.

With  $a^{-1}, b^{-1}$  in place of  $a, b$ , this yields the second part. $□$

**Lemma 5.10.** *Let  $ξ, η ext{ ∈ } rak{L}(G)$ . Then  $ξ + η$  exists and equals  $ξ +_σ η$ .*

*Proof.* It suffices to show that  $ξ +_σ η = ξ +_τ η$  for all positive infinite  $τ ext{ ∈ } ℝ^*$ . Consider first the case  $τ = 
uσ$  (with  $u ext{ ∈ } ℕ^*$ ,  $u > ℕ$  by convention), and set

$$a := \xi(1/\tau), \quad b := \eta(1/\tau), \quad a_\sigma := \xi(1/\sigma), \quad b_\sigma := \eta(1/\sigma),$$

so  $a_σ = a^
u$ ,  $b_σ = b^
u$ . We have  $a, b ext{ ∈ } ext{o}[
u]$ , so  $a^
u b^
u = c(ab)^
u$  with  $c ext{ ∈ } ext{o}[σ]$  by Lemma 5.9. Setting  $d := (ab)^
u$  we have  $d = c^{-1}a_σ b_σ$ , and in view of  $a_σ, b_σ ext{ ∈ } ext{O}[σ]$  and Theorem 5.8 this gives  $d ext{ ∈ } ext{O}[σ]$ . Hence

$$\xi +_\sigma \eta = \xi_{a_\sigma b_\sigma} = \xi_{cd} = \xi_d,$$

and thus for all  $t ext{ ∈ } ℝ$ ,

$$(\xi +_\sigma \eta)(t) = \operatorname{st}(d^{[\sigma t]}) = \operatorname{st}((ab)^{[\tau t]}) = (\xi +_\tau \eta)(t).$$

Next we consider the case  $τ = (1+ε)σ$  with infinitesimal  $ε ext{ ∈ } ℝ^*$ . With  $a, b, a_σ, b_σ$  defined as before, we have  $a, b, a_σ, b_σ ext{ ∈ } ext{O}[σ] = ext{O}[τ]$  and

$$a_\sigma = a \cdot \xi(\varepsilon/\tau), \quad b_\sigma = b \cdot \eta(\varepsilon/\tau), \quad \xi(\varepsilon/\tau), \eta(\varepsilon/\tau) \in o[\sigma] = o[\tau],$$

so  $a_\sigma b_\sigma = abc$  with  $c \in o[\sigma]$  by Theorem 5.8. For  $t \in \mathbb{R}^{>0}$  we have  $[\sigma t] = [\tau t] + k$  with  $k = o(\sigma)$ , so by the definition of  $O[\sigma]$  and using Lemma 5.6,

$$(a_\sigma b_\sigma)^{[\sigma t]} \sim (a_\sigma b_\sigma)^{[\tau t]} = (abc)^{[\tau t]} \sim (ab)^{[\tau t]},$$

and thus  $\xi +_\sigma \eta = \xi +_\tau \eta$ . For arbitrary positive infinite  $\tau \in \mathbb{R}^*$  we reduce to the previous two cases by taking  $\nu, \nu' \in \mathbb{N}^* \setminus \mathbb{N}$  such that  $\nu'\tau = (1 + \varepsilon)\nu\sigma$  with infinitesimal  $\varepsilon \in \mathbb{R}^*$ .  $\square$

By Lemma 5.10 we now have the real vector space  $\mathfrak{L}(G)$  as indicated in Lemma 2.3. In Section 2 we gave it the topology induced by the compact-open topology of  $C(\mathbb{R}, G)$ . Note also that for  $\xi, \eta \in \mathfrak{L}(G)$  and  $r \in \mathbb{R}$  we have  $(\xi + \eta)(r) = (r\xi + r\eta)(1)$ , that is,

$$(\xi + \eta)(r) = \lim_{s \rightarrow \infty} \left( \xi\left(\frac{1}{s}\right) \eta\left(\frac{1}{s}\right) \right)^{[rs]} = \lim_{s \rightarrow \infty} \left( \xi\left(\frac{r}{s}\right) \eta\left(\frac{r}{s}\right) \right)^{[s]}.$$

**Corollary 5.11.**  *$\mathfrak{L}(G)$  is a topological vector space over  $\mathbb{R}$ .*

*Proof.* Lemma 2.8 gives the continuity of scalar multiplication, so it remains to establish the continuity of  $+$ . Let  $\xi, \eta \in \mathfrak{L}(G)$ , and let  $W$  be a neighborhood of  $\xi + \eta$  in  $\mathfrak{L}(G)$ . It suffices to obtain neighborhoods  $P$  and  $Q$  of  $\xi$  and  $\eta$  in  $\mathfrak{L}(G)$  such that for all  $\xi' \in P$  and  $\eta' \in Q$  we have  $\xi' + \eta' \in W$ . To get such  $P, Q$ , take a compact neighborhood  $U$  of 1 in  $G$  so small that for all  $\zeta \in \mathfrak{L}(G)$ , if  $\zeta(t) \in (\xi + \eta)(t)U$  for all  $t \in I := [-1, 1]$ , then  $\zeta \in W$ . Next, let  $\xi', \eta' \in \mathfrak{L}(G)^*$  and  $\xi \sim \xi'$  and  $\eta \sim \eta'$ . Fix some  $\nu > \mathbb{N}$ , and put

$$a := \xi(1/\nu), \quad a' := \xi'(1/\nu), \quad b := \eta(1/\nu), \quad b' := \eta'(1/\nu),$$

so  $a, a', b, b' \in O[\nu]$  and  $a^i \sim a'^i$  and  $b^i \sim b'^i$  for all  $i \leq \nu$ , so  $a\,o[\nu] = a'\,o[\nu]$  and  $b\,o[\nu] = b'\,o[\nu]$  by Lemma 5.7. Hence  $(ab)^k \sim (a'b')^k$  whenever  $|k| \leq \nu$ , so

$$\left( \xi'\left(\frac{1}{\nu}\right) \eta'\left(\frac{1}{\nu}\right) \right)^k \in \left( \left( \xi\left(\frac{1}{\nu}\right) \eta\left(\frac{1}{\nu}\right) \right)^k \right) U^* \quad \text{whenever } |k| \leq \nu.$$

By overspill (see the subsection on topological spaces and continuity in the appendix) this gives neighborhoods  $P$  and  $Q$  of  $\xi$  and  $\eta$  in  $\mathfrak{L}(G)$  such that for all  $\xi' \in P$  and  $\eta' \in Q$  we have

$$\left( \xi'\left(\frac{1}{\nu}\right) \eta'\left(\frac{1}{\nu}\right) \right)^k \in \left( \left( \xi\left(\frac{1}{\nu}\right) \eta\left(\frac{1}{\nu}\right) \right)^k \right) U^* \quad \text{whenever } |k| \leq \nu.$$

It follows that for all  $\xi' \in P$  and  $\eta' \in Q$  we have

$$(\xi' + \eta')(t) \in (\xi + \eta)(t) \cdot U \quad \text{for all } t \in I.$$

This gives  $\xi' + \eta' \in W$  for all  $\xi' \in P$  and  $\eta' \in Q$ .  $\square$

**Corollary 5.12.** *Suppose the exponential map of  $G$  maps some neighborhood of  $o$  in  $\mathfrak{L}(G)$  homeomorphically onto a neighborhood of  $1$  in  $G$ . Then  $G$  is locally euclidean and has NSS.*

*Proof.* Since  $G$  is locally compact, so is  $\mathfrak{L}(G)$ . It follows that  $\mathfrak{L}(G)$  has finite dimension as vector space over  $\mathbb{R}$ , and so we can put a norm on  $\mathfrak{L}(G)$ . With respect to this norm we take an open ball  $B$  centered at  $o$  that is homeomorphic to a neighborhood  $U$  of  $1$  in  $G$  via the exponential map of  $G$ . Take  $n > 1$  such that  $V := \{\xi(1) \mid \xi \in \frac{1}{n}B\}$  satisfies  $V^2 \subseteq U$ . We claim that then  $V$  contains no subgroup of  $G$  other than  $\{1\}$ . To see why, let  $a \in V$ ,  $a \neq 1$ . Take  $\xi \in \frac{1}{n}B$  with  $a = \xi(1)$ , and take  $m > 1$  such that  $m\xi \in B \setminus \frac{1}{n}B$ . Then  $(m\xi)(1) = a^m \in U \setminus V$ , so  $a^{\mathbb{Z}} \not\subseteq V$ . □

## 6. Consequences of NSS

In this section we assume that our locally compact group  $G$  has NSS. We shall now carry out step (3) from the sketch in the Introduction.

**Lemma 6.1.** *There is a neighborhood  $U$  of  $1$  such that for all  $x, y \in U$ ,  $x^2 = y^2 \implies x = y$ .*

*Proof.* Towards a contradiction, let  $x, y \in \mu$ ,  $x \neq y$  and  $x^2 = y^2$ . Then

$$y^{-1}(xy^{-1})y = y^{-1}x = (xy^{-1})^{-1},$$

so with  $a := xy^{-1}$  we get  $y^{-1}ay = a^{-1}$ . Then  $y^{-1}a^k y = a^{-k}$  for all  $k$ . Take a compact symmetric neighborhood  $U$  of  $1$  in  $G$  that contains no non-trivial subgroup of  $G$ . Take positive  $k$  such that  $a^i \in U^*$  for  $0 \leq i \leq k$  and  $a^{k+1} \notin U^*$ . Set  $b := \text{st}(a^k)$ , so  $b \neq 1$ ,  $b \in U$ , and  $b = b^{-1}$ , so  $\{1, b\}$  is a non-trivial subgroup of  $G$  contained in  $U$ , a contradiction. □

By a *special neighborhood* of  $G$  we mean a compact symmetric neighborhood  $U$  of  $1$  in  $G$  such that  $U$  contains no non-trivial subgroup of  $G$  and for all  $x, y \in U$ , if  $x^2 = y^2$ , then  $x = y$ .

In the rest of this section we fix a special neighborhood  $\mathcal{U}$  of  $G$  (which exists by the lemma above), and we set  $\text{ord}(a) := \text{ord}_{\mathcal{U}}(a)$ .

**Corollary 6.2.** *Suppose  $G$  is not discrete. Then  $\mathfrak{L}(G) \neq \{o\}$ .*

*Proof.* Take  $a \in \mu$  with  $a \neq 1$ , and set  $\sigma := \text{ord}(a)$ . Then  $a \in \text{O}[\sigma]$  and  $a \notin \text{o}[\sigma]$ , so  $\xi_a \in \mathfrak{L}(G)$ ,  $\xi_a \neq o$  where  $\xi_a$  is defined as in Lemma 2.6. □

Set  $\mathcal{K} := \{\xi \in \mathfrak{L}(G) \mid \xi(I) \subseteq \mathcal{U}\}$ , with  $I = [-1, 1]$ , so  $\mathcal{K}$  is a compact neighborhood of  $o$  in  $\mathfrak{L}(G)$ , by Lemma 2.9. Note that for any  $\xi \in \mathfrak{L}(G)$  there is  $\lambda \in \mathbb{R}^{>0}$  such that  $\lambda\xi \in \mathcal{K}$ . Put  $K := \{\xi(1) \mid \xi \in \mathcal{K}\}$ , so  $K$  is compact by Lemma 2.8. Note also that  $K = \bigcup_{\xi \in \mathcal{K}} \xi(I)$ , so  $K$  is pathconnected.

**Corollary 6.3.** *The vector space  $\mathfrak{L}(G)$  has finite dimension. The exponential map  $\xi \mapsto \xi(1) : \mathfrak{L}(G) \rightarrow G$  maps  $\mathcal{K}$  homeomorphically onto  $K$ .*

*Proof.* The first assertion follows from Riesz's theorem that a locally compact topological vector space over  $\mathbb{R}$  has finite dimension. For the second assertion it suffices that the exponential map is injective on  $\mathcal{K}$ . Let  $\xi, \eta \in \mathcal{K}$  and  $\xi(1) = \eta(1)$ . Then  $(\xi(1/2))^2 = (\eta(1/2))^2$ , so  $\xi(1/2) = \eta(1/2)$ , and by induction,  $\xi(1/2^n) = \eta(1/2^n)$  for all  $n$ , and thus  $\xi(i/2^n) = \eta(i/2^n)$  for all  $i \in \mathbb{Z}$  and  $n$ . By density this gives  $\xi = \eta$ .  $\square$

**Lemma 6.4.** *Let  $a \in G^*$ . Then  $\text{ord } a$  is infinite iff  $a \in \mu$ .*

*Proof.* Suppose  $\text{ord } a$  is infinite. Then  $a \in \mathcal{U}^*$  and  $a^{\mathbb{Z}} \subseteq \mathcal{U}^*$ , so  $(\text{st } a)^{\mathbb{Z}} \subseteq \mathcal{U}$ , and thus  $\text{st } a = 1$ .  $\square$

For any symmetric  $P \subseteq G$  with  $1 \in P$  we let  $\text{ord}(P)$  be the largest  $n$  such that  $P^n \subseteq \mathcal{U}$  if there is such an  $n$ , and set  $\text{ord } P := \infty$  if  $P^n \subseteq \mathcal{U}$  for all  $n$ .

We set  $\mathcal{U}_n := \{x \in G \mid \text{ord } x \geq n\}$  for  $n \geq 1$ , so  $\mathcal{U}_n \supseteq \mathcal{U}_{n+1}$ .

**Lemma 6.5.** *The sets  $\mathcal{U}_n$  have the following properties:*

- (1) *each  $\mathcal{U}_n$  is a compact symmetric neighborhood of 1 in  $G$ ;*
- (2)  *$\{\mathcal{U}_n \mid n \geq 1\}$  is a (countable) neighborhood base of 1 in  $G$ ;*
- (3)  *$\text{ord } \mathcal{U}_n \geq cn$  for all  $n \geq 1$  and some  $c > 0$  independent of  $n$ .*

*Proof.* Given  $n \geq 1$ , it is clear that  $\mathcal{U}_n \subseteq \mathcal{U}$ , that the complement of  $\mathcal{U}_n$  in  $G$  is open, and that  $\mathcal{U}_n$  is a neighborhood of 1 in  $G$ . This gives (1). For each  $v$  we consider the internal set

$$\mathcal{U}_v := \{g \in G^* \mid \text{ord } g \geq v\}.$$

Since  $v > \mathbb{N}$  by convention, we have  $\mathcal{U}_v \subseteq \mu$  by Lemma 6.4. It follows that for any neighborhood  $U$  of 1 in  $G$  we have  $\mathcal{U}_n \subseteq U$  for all sufficiently large  $n$ ; this gives (2). From  $\mathcal{U}_v \subseteq \mu$  we also obtain  $\mathcal{U}_v \subseteq O[v]$ , hence  $(\mathcal{U}_v)^i \subseteq \mu$  for all  $i = o(v)$  by Lemma 5.4, so  $\text{ord } \mathcal{U}_v \geq cv$  for some  $c \in \mathbb{R}^{>0}$ . This gives (3): nonexistence of  $c$  as in (3) gives  $v$  with  $\text{ord } \mathcal{U}_v < cv$  for all  $c \in \mathbb{R}^{>0}$ .  $\square$

Because 1 has a countable neighborhood base in  $G$ , the topology of  $G$  is induced by some metric on  $G$ . Given such a metric  $d$  on  $G$  we obtain also a metric  $d$  on  $\mathfrak{L}(G)$  by  $d(\xi, \eta) := \max_{|t| \le 1} d(\xi(t), \eta(t))$ , and one verifies easily that this metric induces the same topology on  $\mathfrak{L}(G)$  as the compact-open topology of  $C(\mathbb{R}, G)$ . We do not need this metric, but it may help in visualizing some arguments.

**Proof that  $G$  is locally euclidean..** Let  $\xi \in \mathfrak{L}(G)^*$ . We say that  $\xi$  is *infinitesimal* if  $\xi \in \mu(o)$ , the monad of  $o$  in  $\mathfrak{L}(G)^*$ . Therefore,

$$\xi \text{ is infinitesimal} \iff \xi(I^*) \subseteq \mu,$$

by the definitions and Corollary 6.3.

**Lemma 6.6.** *Let  $\xi, \eta \in \mathfrak{L}(G)^*$  be infinitesimal, with  $\eta(1) \in \mathrm{O}[\sigma]$ . Then*

$$\xi(1)\eta(1) = (\xi + \eta)(1) \cdot z \qquad \text{with } z \in \mathrm{o}[\sigma].$$

*Proof.* Put  $a := \xi(1)$ ,  $b := \eta(1)$ ,  $c := (\xi + \eta)(1)$ . Take an open neighborhood  $U$  of 1 in  $G$  with  $U \subseteq \mathcal{U}$  and take  $\nu$  with  $\sigma = \mathrm{o}(\nu)$  and put

$$W := \{w \in G^* \mid w^i \in U^* \text{ for } i = 1, \dots, \nu\}.$$

Then  $W$  is internally open in  $G^*$  and  $1 \in W \subseteq \mathrm{O}[\nu] \subseteq \mathrm{o}[\sigma]$ . By the definition of  $c$  and using transfer we have  $(\xi(\frac{1}{e})\eta(\frac{1}{e}))^e \in cW$  for all sufficiently large  $e \in \mathbb{N}^* \setminus \mathbb{N}$ , so

$$\left(\xi\left(\frac{1}{e}\right)\eta\left(\frac{1}{e}\right)\right)^e = c w_e, \qquad w_e \in \mathrm{o}[\sigma],$$

for all sufficiently large  $e \in \mathbb{N}^* \setminus \mathbb{N}$ . But also, by Lemma 5.9,

$$\left(\xi\left(\frac{1}{e}\right)\eta\left(\frac{1}{e}\right)\right)^e = a b d_e, \qquad d_e \in \mathrm{o}[\sigma],$$

for all  $e \in \mathbb{N}^* \setminus \mathbb{N}$ . Hence  $ab = c(w d^{-1})$  with  $w, d \in \mathrm{o}[\sigma]$ .  $\square$

**Lemma 6.7.**  *$K$  is a neighborhood of  $1$  in  $G$ .*

*Proof.* It is enough to show that  $\mu \subseteq K^*$ . Let  $a \in \mu$  and suppose towards a contradiction that  $a \notin K^*$ . Since  $K$  is compact we have  $K = \bigcap_n K\mathcal{U}_n$ , and so  $K^* = \bigcap_\nu K^*\mathcal{U}_\nu$  by transfer. Take  $\nu$  maximal with  $a \in K^*\mathcal{U}_\nu$ . Then  $a = bc$  with  $b \in K^*$  and  $c \in \mathcal{U}_\nu \subseteq \mu$ , and  $\operatorname{ord} c = \nu$ . With  $\xi := \xi_c \in \mathfrak{L}(G)$  defined by  $\xi(t) = \operatorname{st}(c^{[\nu t]})$  we have  $\xi \in \mathcal{K}$ , and thus for  $d := \xi(1/\nu) \in K^*$  we have  $c^i \sim d^i$  for all  $i \le \nu$ , and thus  $c = du$  with  $u \in \mathrm{o}[\nu]$  by Lemma 5.7. Hence  $a = bdu$ . By Lemma 6.6 we have  $bd = gh$  with  $g \in K^*$  and  $h \in \mathrm{o}[\nu]$ . Hence  $a = g(hu)$  with  $\nu = \mathrm{o}(\operatorname{ord}(hu))$ , contradicting the maximality of  $\nu$ .  $\square$

From Lemma 6.7 and Corollaries 5.12 and 6.3 we obtain:

**Corollary 6.8.**  *$G$  is locally euclidean of dimension  $\dim_{\mathbb{R}} \mathfrak{L}(G)$ .*

**The adjoint representation.** Take an  $\mathbb{R}$ -linear isomorphism  $\mathcal{L}(G) \cong \mathbb{R}^n$  of vector spaces. It induces a group isomorphism

$$\text{Aut}(\mathcal{L}(G)) \cong \text{GL}_n(\mathbb{R}) \subseteq \mathbb{R}^{n^2},$$

and we give the set  $\text{Aut}(\mathcal{L}(G))$  the topology that makes this bijection into a homeomorphism, and thus into an isomorphism of topological groups. It is clear that this topology on  $\text{Aut}(\mathcal{L}(G))$  does not depend on the initial choice of  $\mathbb{R}$ -linear isomorphism  $\mathcal{L}(G) \cong \mathbb{R}^n$ .

Let  $G_o$  be the connected component of 1 in  $G$ . It is the subgroup of  $G$  generated by the elements  $\xi(t)$  with  $\xi \in \mathcal{L}(G)$  and  $t \in \mathbb{R}$ . It is open in  $G$ .

**Lemma 6.9.** *The group morphism  $\text{Ad} : G \rightarrow \text{Aut}(\mathcal{L}(G))$  is continuous, and  $\ker(\text{Ad}) = \{a \in G : a \text{ commutes with all elements of } G_o\}$ . In particular, if  $G$  is connected, then  $\ker(\text{Ad}) = \text{center}(G)$ .*

*Proof.* One checks easily that if  $a \in \mu$  and  $\xi \in \mathcal{L}(G)$ , then  $a\xi a^{-1} \in \mu(\xi)$  in  $\mathcal{L}(G)^*$ . Applying this to the  $\xi$  from a basis of the vector space  $\mathcal{L}(G)$ , we see that  $\text{Ad}$  is continuous at 1. Since  $\text{Ad}$  is a group morphism, it follows that  $\text{Ad}$  is continuous. Clearly,  $\ker(\text{Ad})$  consists of those  $a \in G$  that commute with all elements of the form  $\xi(t)$  with  $\xi \in \mathcal{L}(G)$  and  $t \in \mathbb{R}$ . □

As indicated in the Introduction, step (4) of “Sketch why NSS implies Lie”, we may now conclude:

**Corollary 6.10.**  *$G$  is a Lie group.*

## 7. Locally Euclidean implies NSS

In these last two sections we revert to the assumption that  $G$  is just a locally compact group, not necessarily locally euclidean or having NSS.

**Lemma 7.1.** *Let  $U$  be a neighborhood of 1 in  $G$ . Then  $U$  contains a compact subgroup  $H$  of  $G$  and a neighborhood  $V$  of 1 in  $G$  such that  $H$  contains every subgroup of  $G$  contained in  $V$ .*

*Proof.* Shrinking  $U$  we arrange that  $\text{cl}(U)$  is compact. Take an internal neighborhood  $V$  of 1 in  $G^*$  such that  $V \subseteq \mu$ . Let  $S$  be the internal subgroup of  $G^*$  that is internally generated by the union of the internal subgroups of  $G^*$  that are contained in  $V$ . Then  $S \subseteq \mu$  by Lemma 5.4, and so the internal closure  $H$  of  $S$  in  $G^*$  is an internal subgroup of  $G^*$  contained in  $U^*$ . By transfer, there is a neighborhood  $V$  of 1 in  $G$  and a closed subgroup  $H$  of  $G$  such that  $H \subseteq U$  and  $H$  contains every subgroup of  $G$  contained in  $V$ . □

**Corollary 7.2.** *If  $\mathfrak{L}(G) = \{o\}$ , then there is a neighborhood base of  $1$  in  $G$  consisting of compact open subgroups of  $G$ .*

*Proof.* Let  $U$  be a neighborhood of  $1$  in  $G$ , and take  $H$  and  $V$  as in the previous lemma. If  $\mathfrak{L}(G) = \{o\}$ , then every  $a \in \mu$  is degenerate, hence  $a^{\mathbb{Z}^*} \subseteq H^*$  for each  $a \in \mu$ , so  $H$  is open.  $\square$

**Corollary 7.3.** *If  $G$  is connected and  $G \neq \{1\}$ , then  $\mathfrak{L}(G) \neq \{o\}$ .*

We define a topological space to be *totally disconnected* if its connected components are all singletons.

**Lemma 7.4.** *Let  $N$  be a totally disconnected closed normal subgroup of  $G$  and let  $\pi : G \to G/N$  be the canonical map. Then the induced map  $\mathfrak{L}(\pi) : \mathfrak{L}(G) \to \mathfrak{L}(G/N)$  is surjective.*

*Proof.* Let  $H := G/N$ , and  $\eta \in \mathfrak{L}(H)$  with  $\eta(1) \neq 1_H$ . Fix  $\nu$  and put  $h := \eta(1/\nu) \in \mu(1_H)$ . Take a compact symmetric neighborhood  $V$  of  $1_H$  in  $H$  such that  $\eta(1) \notin V$ . Take a compact symmetric neighborhood  $U$  of  $1$  in  $G$  such that  $\pi(U) \subseteq V$ . Since  $\pi$  is an open map we have  $\pi(\mu) \supseteq \mu(1_H)$ . Take  $a \in \mu$  with  $\pi(a) = h$ . Then  $\pi(a^\nu) = h^\nu = \eta(1)$ , so  $a^\nu \notin U$ , so  $\sigma := \text{ord}_U(a) \le \nu$ . We have  $\pi(\text{st}(a^k)) = \text{st}(h^k) = 1_H$  for all  $k = o(\sigma)$ , so the connected subgroup  $G_U(a) = \{\text{st}(a^k) \mid k = o(\sigma)\}$  of  $G$  is contained in  $N$ . But  $N$  is totally disconnected, so  $G_U(a) = \{1\}$ , that is,  $a \in O[\sigma]$ . Also  $a \notin o[\sigma]$ , so  $\xi \neq o$  where  $\xi = \xi_a \in \mathfrak{L}(G)$  is defined by  $\xi(t) = \text{st}(a^{[\sigma t]})$ . If  $\sigma = o(\nu)$ , then  $\pi(\xi(t)) = \text{st}(h^{[\sigma t]}) = 1$  for all  $t$ , so  $\xi \in \mathfrak{L}(N) \subseteq \mathfrak{L}(G)$ , that is  $\xi = o$ , a contradiction. Thus  $\sigma = (r + \epsilon)\nu$  with  $r \in \mathbb{R}^{>0}$  and infinitesimal  $\epsilon \in \mathbb{R}^*$ . Hence  $\pi(\xi(t)) = \text{st}(h^{[\nu rt]}) = (r\eta)(t)$  for all  $t \in \mathbb{R}$ , that is,  $\mathfrak{L}(\pi)(\xi) = r\eta$ , and thus  $\mathfrak{L}(\pi)(\frac{1}{r}\xi) = \eta$ .  $\square$

Recall: a topological space is *locally connected* iff every neighborhood of any point in it contains a connected neighborhood of that point.

**Lemma 7.5.** *If  $G$  is locally connected and has NSCS, then  $G$  has NSS.*

*Proof.* Suppose  $G$  is locally connected and has NSCS. Take a compact symmetric neighborhood  $U$  of  $1$  in  $G$  that contains no connected subgroup of  $G$  other than  $\{1\}$ . By Lemma 7.1 we can take an open neighborhood  $V \subseteq U$  of  $1$  in  $G$  and a compact subgroup  $N_1$  of  $G$  such that  $N_1 \subseteq U$  and all subgroups of  $G$  contained in  $V$  are contained in  $N_1$ . Since  $N_1 \subseteq U$  we have  $\mathfrak{L}(N_1) = \{o\}$ , so  $N_1$  is totally disconnected by Corollary 7.2, and we have a compact subgroup  $N$

of  $N_1$  such that  $N$  is open in  $N_1$  and  $N \subseteq V$ . Take an open subset  $W$  of  $V$  such that  $N = N_1 \cap W$ . Note that the set

$$\{a \in W \mid aNa^{-1} \subseteq W\}$$

is open. But if  $a \in W$  and  $aNa^{-1} \subseteq W$ , then  $aNa^{-1} \subseteq N_1$ , so  $aNa^{-1} \subseteq N$ . Thus the normalizer  $G_1$  of  $N$  in  $G$  is open in  $G$ . Let  $H := G_1/N$ , and let  $\pi : G_1 \rightarrow H$  be the canonical map. Next we show that  $H$  has NSS.

Let  $a \in \mu \cap G_1^*$ . If  $a$  is degenerate, then  $a \in N_1^*$ , so  $a \in N^*$  and  $\pi(a) = 1_H$ . Suppose  $a$  is pure, and put  $v := \text{ord}_U(a)$ . Then  $a^{v+1} \notin U^*$ . Take an open neighborhood  $V'$  of 1 in  $G$  such that  $V'N \subseteq V \subseteq U$ , so  $\pi(a)^{v+1} \notin \pi(V')$ , while  $\pi(a)^i \in \mu(1_H)$  for all  $i = o(v)$ . Thus  $\pi(a)$  is pure in  $H$ . Thus all infinitesimals of  $H$  other than  $1_H$  are pure, that is,  $H$  has NSS. Thus  $\mathcal{L}(H)$  is finite-dimensional, and by Lemma 7.4 the  $\mathbb{R}$ -linear map

$$\mathcal{L}(\pi) : \mathcal{L}(G_1) = \mathcal{L}(G) \rightarrow \mathcal{L}(H)$$

is continuous and surjective with kernel  $\mathcal{L}(N) = \{o\}$ , and thus a homeomorphism. (So far we have not used that  $G$  is locally connected.)

Take a special neighborhood  $\mathcal{V}$  of  $H$ , as defined in Section 6. As  $G$  is locally connected, we can take a connected neighborhood  $\mathcal{U}$  of 1 in  $G_1$  such that

$$\pi(\mathcal{U}) \subseteq \{\eta(1) \mid \eta \in \mathcal{L}(H), \eta(I) \subseteq \mathcal{V}\}, \quad I := [-1, 1].$$

Let  $x \in \mathcal{U}$ . Then  $\pi(x) = \eta(1)$  for a unique  $\eta \in \mathcal{L}(H)$  with  $\eta(I) \subseteq \mathcal{V}$ , and there is a unique  $\xi \in \mathcal{L}(G_1)$  such that  $\pi \circ \xi = \eta$ , so  $x = \xi(1)x(N)$  with  $x(N) \in N$ . The map that assigns to each  $x \in \mathcal{U}$  the above  $\eta \in \mathcal{L}(H)$  is continuous, by Corollary 6.3. Since  $\mathcal{L}(\pi) : \mathcal{L}(G_1) \rightarrow \mathcal{L}(H)$  is a homeomorphism, it follows that the map  $x \mapsto x(N) : \mathcal{U} \rightarrow N$  is continuous. But  $N$  is totally disconnected and  $1(N) = 1$ , so  $x(N) = 1$  for all  $x \in \mathcal{U}$ . We now use this to derive  $\mathcal{U} \cap N = \{1\}$ . Let  $x \in \mathcal{U} \cap N$ , so  $\pi(x) = 1$ . Then  $\eta := o_H$  satisfies  $\pi(x) = \eta(1)$ ,  $\eta(I) \subseteq \mathcal{V}$ , and as  $\pi \circ o_G = o_H$  we get  $x = o_G(1) = 1$ . From  $\mathcal{U} \cap N = \{1\}$  we obtain that  $\pi$  is injective on some neighborhood of 1 in  $G_1$ , so  $G_1$  has NSS, and thus  $G$  has NSS.  $\square$

Recall that a topological space is *bounded in dimension* if for some  $n$  it does not contain a homeomorphic copy of  $[0, 1]^n$ .

**Lemma 7.6.** *If  $G$  is bounded in dimension, then  $G$  has NSCS.*

*Proof.* Suppose  $G$  does not have NSCS. Let  $U, V$  range over compact symmetric neighborhoods of 1 in  $G$ . We claim that for every  $n$  and  $U$ , some compact

subgroup of  $G$  contained in  $U$  contains a homeomorphic copy of the  $n$ -cube  $[0, 1]^n$ . Assume this holds for a certain  $n$  and let  $U$  be given. By Lemma 7.1 we can take  $V \subseteq U$  and a compact subgroup  $H \subseteq U$  of  $G$  that contains every subgroup of  $G$  contained in  $V$ . Since  $V$  contains a nontrivial connected compact subgroup of  $G$ , Corollary 7.3 yields a nontrivial  $\xi \in \mathcal{L}(H)$ . By decreasing  $V$  if necessary we can assume that  $\xi(\mathbb{R}) \not\subseteq V$ . Take a compact subgroup  $G(V) \subseteq V$  of  $G$  with a homeomorphism

$$\eta : [0, 1]^n \rightarrow \eta([0, 1]^n) \subseteq G(V).$$

Then  $\xi(\mathbb{R}) \not\subseteq G(V)$ , so  $\{t \in \mathbb{R} \mid \xi(t) \in G(V)\}$  is a proper closed subgroup of the additive group of  $\mathbb{R}$ , hence equals  $\mathbb{Z}r$  for some real  $r \geq 0$ . Replacing  $\xi$  by  $s\xi$  for a some real  $s > 0$  we arrange that for  $I := [-1, 1]$ :  $\xi(I) \subseteq V$ ,  $\xi$  is injective on  $I$  and  $\xi(I) \cap G(V) = \{1\}$ . Since  $G(V) \subseteq H$  we can define

$$\zeta : [0, 1] \times [0, 1]^n \rightarrow H, \quad \zeta(s, t) := \xi(s)\eta(t) \text{ for } s \in [0, 1], t \in [0, 1]^n.$$

It is easy to check that then  $\zeta : [0, 1]^{n+1} \rightarrow \zeta([0, 1]^{n+1})$  is injective and continuous, and thus a homeomorphism. □

**Corollary 7.7.** *If  $G$  is bounded in dimension and locally connected, then  $G$  has NSS. In particular, if  $G$  is locally euclidean, then  $G$  has NSS.*

*Proof.* Use Lemmas 7.6 and 7.5. □

This concludes the proof of the Main Theorem.

## 8. Yamabe’s Theorem

We keep the convention that  $G$  is a locally compact group, and use the results above to derive Yamabe’s Theorem on approximating some open subgroup of  $G$  by Lie groups. This doesn’t involve any nonstandard methods.

**Lemma 8.1.** *Let  $U$  be a neighborhood of 1 in  $G$ . Then there is an open subgroup  $G'$  of  $G$  and a compact normal subgroup  $N'$  of  $G'$  such that  $N' \subseteq U$  and  $G'/N'$  has NSS.*

![A diamond-shaped commutative diagram with nodes G at the top, U on the left, G' on the right, and N' at the bottom. G is connected to U and G', and U is connected to N', and G' is connected to N'.](adc652b19ecea71dd56a9f5821ae7cc0_img.jpg)

A diamond-shaped commutative diagram with nodes G at the top, U on the left, G' on the right, and N' at the bottom. G is connected to U and G', and U is connected to N', and G' is connected to N'.

*Proof.* By Lemma 7.1 we can take a compact subgroup  $H \subseteq U$  of  $G$  and an open neighborhood  $W \subseteq U$  of 1 in  $G$  such that every subgroup of  $G$  contained in  $W$  is a subgroup of  $H$ . Since  $H$  is compact, Theorem 4.1 yields a compact normal subgroup  $N' \subseteq W$  of  $H$  and a continuous injective group morphism  $H/N' \rightarrow \mathrm{GL}_n(\mathbb{R})$ . Since  $\mathrm{GL}_n(\mathbb{R})$  has NSS, it follows that  $H/N'$  has NSS. The latter gives an open  $W' \subseteq W$  such that  $N' \subseteq W'$  and every subgroup of  $G$  contained in  $W'$  is a subgroup of  $N'$ . Set

$$G' := \text{the normalizer of } N' \text{ in } G = \{g \in G \mid gN'g^{-1} = N'\},$$

so  $G'$  is a subgroup of  $G$  and  $N'$  is a normal subgroup of  $G'$ . We claim that  $G'$  and  $N'$  have the desired properties.

Since  $N'$  is compact and  $W'$  is open, we have a symmetric neighborhood  $V$  of 1 in  $G$  such that  $VN'V \subseteq W'$ . Then for all  $g \in V$ , the subgroup  $gN'g^{-1}$  of  $G$  is contained in  $W'$ , so  $gN'g^{-1} \subseteq N'$ , which by symmetry of  $V$  gives  $gN'g^{-1} = N'$ . Consequently,  $V \subseteq G'$  and thus  $G'$  is open. It remains to show that  $G'/N'$  has NSS. This holds because  $VN' \subseteq W'$  is a neighborhood of  $N'$  in  $G'$ , so every subgroup of  $G'$  contained in  $VN'$  is contained in  $W'$  and thus in  $N'$ .  $\square$

Let  $G_o$  be the connected component of 1 in  $G$ . (This was defined earlier in Section 6, but there we assumed  $G$  to have NSS.) It is clear that  $G_o$  is a closed normal subgroup of  $G$  and is contained in every open subgroup of  $G$ . It is also easy to verify that  $G/G_o$  is totally disconnected.

Recall from the Introduction that “ $G$  can be approximated by Lie groups” means that every neighborhood of 1 in  $G$  contains a compact normal subgroup  $N$  of  $G$  such that  $G/N$  is a Lie group.

**Theorem 8.2.** *Suppose  $G/G_o$  is compact. Then  $G$  can be approximated by Lie groups.*

*Proof.* Let  $U$  be a neighborhood of 1 in  $G$ . By Lemma 8.1 and its proof we obtain  $G'$  and  $N'$  as in that lemma and an open neighborhood  $W'$  of  $N'$  such that any subgroup of  $G$  contained in  $W'$  is a subgroup of  $N'$ . Note that  $G_o \subseteq G'$  since  $G'$  is clopen in  $G$ . Consequently,  $G'/G_o$  is an open subgroup of the compact group  $G/G_o$ , and thus of finite index in  $G/G_o$ . Hence  $G'$  has finite index in  $G$ , so  $G = g_1G' \cup \dots \cup g_nG'$  where  $g_1, \dots, g_n \in G$ . Given  $g \in G$  we have  $g = g_i a$  with  $1 \leq i \leq n$  and  $a \in G'$ , so  $gN'g^{-1} = g_i(aN'a^{-1})g_i^{-1} = g_iN'g_i^{-1}$ , since  $N'$  is normal in  $G'$ . Thus

$$N := \bigcap_{i=1}^n g_i N' g_i^{-1} = \bigcap_{g \in G} g N' g^{-1}$$

is a compact normal subgroup of  $G$  and  $N \subseteq N' \subseteq U$ . It remains to show that  $G/N$  has NSS. Let

$$W := \bigcap_{i=1}^n g_i W' g_i^{-1},$$

an open subset of  $G$  containing  $N$ . If  $H \subseteq W$  is any subgroup of  $G$ , then for each  $i$  we have  $g_i^{-1} H g_i \subseteq W'$ , so  $g_i^{-1} H g_i \subseteq N'$ , and thus  $H \subseteq N$ .  $\square$

**Corollary 8.3.** *If  $G$  is connected, then  $G$  can be approximated by Lie groups.*

**Lemma 8.4.** *Let  $X$  be a compact space and  $x \in X$ . Then the connected component of  $x$  in  $X$  is the intersection of all compact open subsets of  $X$  that contain  $x$ .*

*Proof.* Let  $\{C_\lambda \mid \lambda \in \Lambda\}$  be the collection of all compact open subsets of  $X$  that contain  $x$  and put  $C := \bigcap_\lambda C_\lambda$ . Consider a decomposition

$$C = A \cup B, \quad A, B \text{ closed in } X, \quad A \cap B = \emptyset.$$

Since  $X$  is normal we can take disjoint open  $U, V \subseteq X$  with  $A \subseteq U$  and  $B \subseteq V$ . Then  $C$  and  $X \setminus (U \cup V)$  are disjoint, which gives a finite subset  $\Lambda_0$  of  $\Lambda$  such that  $D := \bigcap_{\lambda \in \Lambda_0} C_\lambda$  and  $X \setminus (U \cup V)$  are disjoint. Then  $D$  is compact and open, and  $x \in D$ . We have  $D = (U \cap D) \cup (V \cap D)$ , and only one of the compact open sets  $U \cap D, V \cap D$  contains  $x$ , say  $U \cap D$ . Then  $U \cap D = C_\lambda$  for a certain  $\lambda \in \Lambda$ , and then  $B \cap C_\lambda = \emptyset$ , so  $B = \emptyset$ . This argument shows that  $C$  is connected. It follows that  $C$  is the connected component of  $x$  in  $X$ .  $\square$

**Corollary 8.5.** *Let  $X$  be a compact space,  $C$  a connected component of  $X$ , and  $F$  a closed subset of  $X$  such that  $C \cap F = \emptyset$ . Then there is a compact open subset  $D$  of  $X$  such that  $C \subseteq D$  and  $D \cap F = \emptyset$ .*

**Lemma 8.6.** *Every compact open neighborhood of 1 in  $G$  contains a compact open subgroup of  $G$ .*

*Proof.* Let  $U$  be a compact open neighborhood of 1 in  $G$ . Set  $F = U^2 \setminus U$ , so  $F$  is closed. Now  $U$  is compact,  $G \setminus F$  is open, and  $U \subseteq G \setminus F$ , so we have an open symmetric neighborhood  $V$  of 1 in  $G$  with  $V \subseteq U$  and  $UV \subseteq G \setminus F$ . Then  $UV \subseteq U^2$  gives  $UV \subseteq U$ . Hence  $V^n \subseteq UV^n \subseteq U$  for all  $n$ . Thus  $H := \bigcup_n V^n$  is an open subgroup of  $G$  contained in  $U$ . But open subgroups are also closed, and  $U$  is compact, so  $H$  is compact.  $\square$

**Lemma 8.7.** *Suppose  $G$  is totally disconnected. Then every compact neighborhood of 1 contains a compact open subgroup of  $G$ .*

*Proof.* Let  $U$  be a compact neighborhood of 1. Take an open neighborhood  $V \subseteq U$  of 1 in  $G$ , and set  $F = U \setminus V$ . As  $\{1\}$  is a connected component of  $U$ , Corollary 8.5 yields compact  $D \subseteq U$ , open in  $U$ , such that  $1 \in D$  and  $D \cap F = \emptyset$ . Then  $D \subseteq V$ , so  $D$  is open in  $G$ . Apply Lemma 8.6 to  $D$ .  $\square$

**Corollary 8.8.**  *$G$  has an open subgroup  $G'$  such that  $G'/G_0$  is compact.*

*Proof.* Apply Lemma 8.7 to  $G/G_0$  in the role of  $G$ .  $\square$

Combining Theorem 8.2 and Lemma 8.8, we obtain Yamabe's Theorem as stated in the Introduction.

## 9. Appendix on nonstandard methods

This appendix is for readers not familiar with nonstandard methods. For another exposition, see [2]; for a detailed treatment, see [7].

**The basic set-up.** Suppose a mathematical structure is given by certain ambient sets, together with certain relations between them. (This covers almost anything. For example, a group is a set with a ternary relation on it, namely the graph of its group operation; a topological space is given by two sets, the set of points of the space, and the set of open subsets of the space, together with the membership relation between points and open sets.) More precisely, let  $S_1, \dots, S_p$  ( $p \in \mathbb{N}^{\geq 1}$ ) be the ambient sets, assumed to be nonempty and called *basic sets*, and let  $R_1, \dots, R_q$  ( $q \in \mathbb{N}$ ) be the relations between  $S_1, \dots, S_p$  describing our mathematical structure: for each index  $j \in \{1, \dots, q\}$  we are given indices  $i(1), \dots, i(n) \in \{1, \dots, p\}$  such that

$$R_j \subseteq S_{i(1)} \times \cdots \times S_{i(n)}.$$

These relations  $R_j$  are referred to as the *basic relations* or as the *primitives* of the structure. Often these primitives are (graphs of) functions

$$f : S_{i(1)} \times \cdots \times S_{i(n)} \rightarrow S_{i(n+1)}.$$

Using nonstandard analysis to study this structure includes three things:

(NA1) Each basic set  $S_i$  is extended to a set  $S_i^* \supseteq S_i$ , and to each basic relation  $R_j$  as displayed above is associated a corresponding relation

$$R_j^* \subseteq S_{i(1)}^* \times \cdots \times S_{i(n)}^*$$

whose intersection with  $S_{i(1)} \times \cdots \times S_{i(n)}$  is the original relation  $R_j$ . Thus our original structure  $\mathbf{S} = (S_1, \dots, S_p; R_1, \dots, R_q)$  gets extended to a structure

$\mathbf{S}^* = (S_1^*, \dots, S_p^*; R_1^*, \dots, R_q^*)$ . This *nonstandard extension*  $\mathbf{S}^*$  of  $\mathbf{S}$  might contain useful “ideal” elements that are missing in  $\mathbf{S}$ .

(NA2) Any *elementary statement* about the original structure  $\mathbf{S}$  is true in  $\mathbf{S}$  if and only if it is true in  $\mathbf{S}^*$ : the *transfer principle*. After the example below we explain in a separate subsection what elementary statements are.

(NA3) The structure  $\mathbf{S}^*$  enjoys a certain logical compactness property—it is  $\kappa$ -rich,  $\kappa$  being an infinite cardinal—that  $\mathbf{S}$  typically does not.

We define “ $\kappa$ -rich” below. For many nonstandard arguments, it is enough to have (NA3) for  $\kappa = \aleph_0$ . For our purpose it is enough to have  $\kappa \geq \#S_i$  for  $i = 1, \dots, p$ . A key fact is that for any  $\mathbf{S}$  and any infinite cardinal  $\kappa$ , there is always an extension  $\mathbf{S}^*$  such that (NA1), (NA2), and (NA3) hold. At the end of this appendix we indicate one way—not the most constructive one, but easy to describe—to obtain such extensions  $\mathbf{S}^*$ , namely ultrapowers.

**Example.** In applications, one of the basic sets will often be  $\mathbb{R}$ , with its usual ordering and (the graphs of) addition and multiplication among the primitives. We can express by an elementary statement that  $\mathbb{R}$  with these primitives is an ordered field. Then by transfer,  $\mathbb{R}^*$  with the corresponding starred primitives will be an ordered field extension of  $\mathbb{R}$ .

Often we also have the subset  $\mathbb{Z}$  of  $\mathbb{R}$  as a primitive, and then we can express by an elementary statement the fact that  $\mathbb{Z}$  is (the underlying subset of) a subring of the field  $\mathbb{R}$  and that for every  $r \in \mathbb{R}$  there exists a unique  $k \in \mathbb{Z}$  with  $k \leq r < k + 1$ . Then by transfer the set  $\mathbb{Z}^*$  is a subring of the field  $\mathbb{R}^*$  and there is for each  $r \in \mathbb{R}^*$  a unique  $k \in \mathbb{Z}^*$  with  $k \leq r < k + 1$ ; the latter expression abbreviates  $k \leq^* r <^* k +^* 1$ : we omit stars when the context invites the reader to insert them mentally.

One manifestation of (NA3) here is that there are  $x \in \mathbb{R}^*$  such that  $x > n$  for every  $n$ . This is because for any  $n_1, \dots, n_m \in \mathbb{N}$  there is an  $x \in \mathbb{R}^*$  (even an  $x \in \mathbb{R}$ ) with  $x > n_1, \dots, x > n_m$ . Such an element  $x > \mathbb{R}$  is said to be *positive infinite*, and its reciprocal is then a *positive infinitesimal*:  $0 < 1/x < 1/n$  for all  $n \geq 1$ .

**Elementary statements.** Let a structure  $\mathbf{S} = ((S_i); (R_j))$  as above be given. For each basic set  $S_i$  we take *variables* that we consider as ranging over  $S_i$ ; these are just the symbols  $v_i^0, v_i^1, v_i^2, \dots$ . We also fix for each element  $a \in S_i$  a *name*  $(a, i)$  for  $a$  in its role as element of  $S_i$ . This allows us to form so-called *atomic  $\mathbf{S}$ -formulas*: these are expressions of the form  $v_i^m = v_i^n$ , or of the form  $v_i^m = c$  where  $c$  is the name of an element of  $S_i$ , or of the form  $R_j(t_1, \dots, t_n)$  where  $R_j \subseteq S_{i(1)} \times \dots \times S_{i(n)}$  is a primitive, and  $t_k$  is for  $k = 1, \dots, n$  either a variable ranging over  $S_{i(k)}$ , or the name of a particular element of  $S_{i(k)}$ .

Arbitrary **S**-formulas are constructed, starting with atomic **S**-formulas, using the logical symbols for negation, disjunction, conjunction, existential quantification, and universal quantification: in other words, if  $\phi, \psi$  are **S**-formulas and  $v$  is a variable, then

$$\neg\phi, \quad (\phi \vee \psi), \quad (\phi \wedge \psi), \quad \exists v\phi, \quad \forall v\phi$$

are also **S**-formulas; in the latter two, the occurrences of  $v$  are said to be bound by the quantifier  $\exists v$ , respectively,  $\forall v$ . An **S**-*sentence* (or *elementary statement about* **S**) is an **S**-formula in which all occurrences of variables are bound by quantifiers. We have a recursive definition of what it means for such a sentence to be true in **S**. This recursion just reflects the usual meaning of the logical symbols: for example, an **S**-sentence  $\exists v\phi$ , with  $v = v_i^n$ , is true in **S** iff for some  $a \in S_i$  the *shorter* **S**-sentence obtained by replacing the free (=non-bound) occurrences of  $v$  in  $\phi$  by the name of  $a$  is true in **S**.

Let in addition an extension **S**\* of **S** as in (NA1) be given. Then we have **S**\*-formulas and **S**\*-sentences, using the names we gave to elements  $a \in S_i$  as well as names for new elements in  $S_i^* \setminus S_i$ . Every **S**-formula is considered as an **S**\*-formula by reading each  $R_j$  in the atomic subformulas as standing for  $R_j^*$ . In particular, every **S**-sentence is also an **S**\*-sentence, but in an **S**\*-sentence each variable  $v_i^n$  ranges of course over  $S_i^*$ . In this way we make sense of the requirement (NA2).

**Definable sets.** Let **S** be as before. Let  $\phi(v(1), \dots, v(n))$  be an **S**-formula, that is, an **S**-formula  $\phi$  together with distinct variables  $v(1), \dots, v(n)$  that include all variables occurring free in  $\phi$ . Let  $v(k)$  range over  $S_{i(k)}$  for  $k = 1, \dots, n$ . Then we say that  $\phi(v(1), \dots, v(n))$  defines the subset of  $S_{i(1)} \times \dots \times S_{i(n)}$  consisting of those  $(a_1, \dots, a_n) \in S_{i(1)} \times \dots \times S_{i(n)}$  for which the **S**-sentence obtained from  $\phi$  by replacing the free occurrences of  $v(k)$  by the name of  $a_k \in S_{i(k)}$  for  $k = 1, \dots, n$  is true in **S**.

A set  $X \subseteq S_{i(1)} \times \dots \times S_{i(n)}$  is said to be **S**-*definable* if it is defined in this way by some **S**-formula  $\phi(v(1), \dots, v(n))$  as above. Every primitive  $R_j \subseteq S_{i(1)} \times \dots \times S_{i(n)}$  is **S**-definable, and so is every finite subset of  $S_{i(1)} \times \dots \times S_{i(n)}$ .

If  $X, Y \subseteq S_{i(1)} \times \dots \times S_{i(n)}$  are **S**-definable, then so are  $X \cup Y, X \cap Y, X \setminus Y$ . An **S**-definable map is a map  $f : X \rightarrow Y$  where  $X \subseteq S_{i(1)} \times \dots \times S_{i(m)}$  and  $Y \subseteq S_{i(m+1)} \times \dots \times S_{i(m+n)}$  are **S**-definable and the graph of  $f$  is **S**-definable as a subset of  $S_{i(1)} \times \dots \times S_{i(m)} \times S_{i(m+1)} \times \dots \times S_{i(m+n)}$ . If  $f : X \rightarrow Y$  is **S**-definable and  $X' \subseteq X$  is **S**-definable, then the image  $f(X') \subseteq Y$  is **S**-definable set. Likewise with inverse images.

Let  $\mathbf{S}^*$  be an extension of  $\mathbf{S}$  satisfying (NA1) and (NA2). Let an  $\mathbf{S}$ -definable set  $X \subseteq S_{i(1)} \times \dots \times S_{i(n)}$  be given. Then we have an  $\mathbf{S}^*$ -definable set  $X^* \subseteq S_{i(1)}^* \times \dots \times S_{i(n)}^*$  with  $X = X^* \cap (S_{i(1)} \times \dots \times S_{i(n)})$ : an  $\mathbf{S}$ -formula that defines  $X$  will define, in its role of  $\mathbf{S}^*$ -formula, the set  $X^*$ . (This is independent of the choice of  $\mathbf{S}$ -formula defining  $X$ .) Note that if  $X$  is finite, then  $X^* = X$ . The transfer principle (NA2) extends to elementary statements about  $\mathbf{S}$  that use the  $\mathbf{S}$ -definable sets  $X$  as primitives, with  $X$  to be read as  $X^*$  in construing the statement to be about  $\mathbf{S}^*$ .

The sets  $X^*$  above are in general not the only  $\mathbf{S}^*$ -definable sets. For example, any  $a \in S_i^* \setminus S_i$  yields an  $\mathbf{S}^*$ -definable set  $\{a\} \subseteq S_i^*$  that is not of the form  $X^*$  for any  $\mathbf{S}$ -definable  $X \subseteq S_i$ .

**Richness.** Let now  $\kappa$  be an infinite cardinal. Our structure  $\mathbf{S}$  is said to be  *$\kappa$ -rich* if for all  $i(1), \dots, i(n) \in \{1, \dots, p\}$  and every family  $(X_\lambda)_{\lambda \in \Lambda}$  of  $\mathbf{S}$ -definable subsets of  $S_{i(1)} \times \dots \times S_{i(n)}$  with the finite intersection property and  $\#\Lambda \le \kappa$  we have  $\bigcap_\lambda X_\lambda \neq \emptyset$ . (It is enough to require this for  $n = 1$ .) Here the “finite intersection property” means that  $X_{\lambda_1} \cap \dots \cap X_{\lambda_m} \neq \emptyset$  for all  $\lambda_1, \dots, \lambda_m \in \Lambda$ . We often apply richness in its dual form as a covering property: if  $\mathbf{S}$  is  $\kappa$ -rich and an  $\mathbf{S}$ -definable set  $X \subseteq S_{i(1)} \times \dots \times S_{i(n)}$  is covered by  $\mathbf{S}$ -definable sets  $X_\lambda \subseteq S_{i(1)} \times \dots \times S_{i(n)}$  with  $\lambda \in \Lambda$  and  $\#\Lambda \le \kappa$ , then  $X$  is already covered by finitely many of these  $X_\lambda$ .

Note that, as an ordered set,  $\mathbb{R}$  is not  $\aleph_0$ -rich, since  $\bigcap_n (n, +\infty) = \emptyset$ . Thus our initial structure  $\mathbf{S}$  will usually not be rich in any way. Suppose  $\mathbf{S}^*$  is an extension of  $\mathbf{S}$  such that (NA1), (NA2), and (NA3) hold, so  $\mathbf{S}^*$  is  $\kappa$ -rich. Thus if  $X \subseteq S_{i(1)}^* \times \dots \times S_{i(n)}^*$  is  $\mathbf{S}^*$ -definable and infinite, then  $\#X > \kappa$ .

**Power sets and internal sets.** We now come to a point that is very characteristic of the nonstandard setting: for certain basic sets  $S$  of our structure  $\mathbf{S}$  we often include also its power set  $\mathcal{P}(S)$  as a basic set, and the membership relation  $\in_S := \{(x, Y) \in S \times \mathcal{P}(S) \mid x \in Y\}$  as a primitive. Then we can quantify over elements of  $\mathcal{P}(S)$ , which gives enormous expressive power. For example, with  $\mathbb{R}$  and  $\mathcal{P}(\mathbb{R})$  as basic sets, together with the membership relation between them and the ordering on  $\mathbb{R}$  as primitives, we can express by an elementary statement the fact that every nonempty subset of  $\mathbb{R}$  with an upperbound in  $\mathbb{R}$  has a least upperbound in  $\mathbb{R}$ .

Let  $S$  and  $\mathcal{P}(S)$  be among the basic sets of our structure  $\mathbf{S}$ , with  $\in_S$  among the primitives. Given  $Y \in \mathcal{P}(S)$ , the formula  $v \in_S c_Y$ , with  $v$  a variable ranging over  $S$  and  $c_Y$  the name of  $Y$  as element of  $\mathcal{P}(S)$ , defines the subset  $Y$  of  $S$ , so  $Y$  is not only an element in our structure  $\mathbf{S}$ , but also an  $\mathbf{S}$ -definable subset of  $S$ . In particular, *every* subset of  $S$  is now  $\mathbf{S}$ -definable!

Next, let an extension  $\mathbf{S}^*$  of  $\mathbf{S}$  be given that satisfies (NA1) and (NA2). Then  $S^*$  and  $\mathcal{P}(S)^*$  are basic sets of  $\mathbf{S}^*$ , and the star extension  $\in_S^*$  of  $\in_S$  is among the primitives. We arrange that the elements of  $\mathcal{P}(S)^*$  are subsets of  $S^*$  and  $\in_S^*$  is the appropriate membership relation by replacing each  $P \in \mathcal{P}(S)^*$  with  $\{a \in S^* \mid a \in_S^* P\}$  (“Mostowski collapse”). This identifies  $\mathcal{P}(S)^*$  with a subset of  $\mathcal{P}(S^*)$ . A set  $X \subseteq S^*$  such that  $X \in \mathcal{P}(S)^*$  via this identification is traditionally called an *internal subset of  $S^*$* . We leave it to the reader to check that this is equivalent to being an  $\mathbf{S}^*$ -definable subset of  $S^*$ . A drawback of this identification is that it destroys the set inclusion  $\mathcal{P}(S) \subseteq \mathcal{P}(S)^*$ : with the above identification a set  $Y \in \mathcal{P}(S)$  turns into  $Y^* \subseteq S^*$ , as is easily verified, and usually  $Y \neq Y^*$ .

To illustrate the above for  $S = \mathbb{R}$  with its ordering among the primitives: the least upperbound property of  $\mathbb{R}$  now yields by transfer the fact that every nonempty internal subset of  $\mathbb{R}^*$  with an upperbound in the ordered set  $\mathbb{R}^*$  has a least upperbound in  $\mathbb{R}^*$ . (Also, every nonempty internal subset of  $\mathbb{R}^*$  that is contained in  $\mathbb{N}^*$  has a least element, and, if it has an upperbound in  $\mathbb{R}^*$ , a largest element.) If our nonstandard extension  $\mathbf{S}^*$  is  $\aleph_0$ -rich, it follows for example that the subset  $\mathbb{R}$  of  $\mathbb{R}^*$  is *not* internal, since it has an upperbound in  $\mathbb{R}^*$  but not a least one.

**Internal sequences.** These powerset conventions on a basic set  $S$  apply also to any finite cartesian product of basic sets. For example, a sequence  $a_1, \dots, a_v$  in  $S^*$  with  $v \in \mathbb{N}^*$ , is formally the set of pairs

$$\{(i, a_i) \mid i \in \mathbb{N}^*, 1 \leq i \leq v\} \subseteq \mathbb{R}^* \times S^*.$$

To refer to this sequence as being *internal* will have an obvious meaning if we have, say,  $\mathbb{R}, S, \mathcal{P}(\mathbb{R}), \mathcal{P}(\mathbb{R} \times S)$  among the basic sets, and the ordering on  $\mathbb{R}$  and the various membership relations as primitives. It is best left to the reader in such cases to decide what to take as basic sets and primitives in order for the use of terms like “internal” to make sense.

**Products of internal sequences in groups.** Let now a group  $G$  be part of our structure  $\mathbf{S}$ : its underlying set is one of the basic sets, and its product operation is a primitive. For any  $n$  and any sequence  $a_1, \dots, a_n$  in  $G$  there is a unique sequence  $b_0, \dots, b_n$  in  $G$  such that  $b_0 = 1_G$  and  $b_{i+1} = b_i a_{i+1}$  for all  $i \in \mathbb{N}$  with  $0 \leq i < n$ . By transfer this yields for an appropriate nonstandard extension  $G^*$ : for any  $v \in \mathbb{N}^*$  and any internal sequence  $a_1, \dots, a_v$  in  $G^*$  there is a unique internal sequence  $b_0, \dots, b_v$  in  $G^*$  such that  $b_0 = 1_G$  and  $b_{i+1} = b_i a_{i+1}$  for all  $i \in \mathbb{N}^*$  with  $0 \leq i < v$ ; in this case we use of course  $a_1 \cdots a_v$  as a

suggestive notation for  $b_v$ ; if all  $a_i$  are equal to a fixed  $a \in G$ , then we write this “product” as  $a^v$ .

Given any symmetric  $X \subseteq G$ , the smallest subgroup of  $G$  that contains  $X$  (usually called the subgroup of  $G$  generated by  $X$ ) is

$$\{a_1 \cdots a_n \mid a_1, \dots, a_n \text{ is a sequence in } X\}.$$

By transfer, this yields: given any internal symmetric  $X \subseteq G^*$ , the smallest internal subgroup of  $G^*$  that contains  $X$  (which deserves to be called the internal subgroup internally generated by  $X$ ) is

$$\{a_1 \cdots a_v \mid v \in \mathbb{N}^*, a_1, \dots, a_v \text{ is an internal sequence in } X\}.$$

**Topological spaces and continuity.** To include a (nonempty) topological space  $(S, \tau)$  in  $\mathbf{S}$ , where  $\tau$  is the set of open sets of the space, we take  $S$  and  $\mathcal{P}(S)$  as basic sets, together with the membership relation  $\in_S \subseteq S \times \mathcal{P}(S)$  and  $\tau \subseteq \mathcal{P}(S)$  as primitives. (Of course there may be further primitives involving  $S$ .) Let  $\mathbf{S}^*$  be an extension of  $\mathbf{S}$  satisfying (NA1) and (NA2). Then we have  $(S^*, \tau^*)$  as part of  $\mathbf{S}^*$ , with  $\tau^* \subseteq \mathcal{P}(S^*)$  after Mostowski collapse. However,  $\tau^*$  is not in general the set of open sets for a topology on the set  $S^*$ . The sets in  $\tau^*$  are by definition the *internally open* subsets of  $S^*$ ; their complements in  $S^*$  are the *internally closed* subsets of  $S^*$ . By transfer, there is for each internal subset  $X$  of  $S^*$  a smallest internally closed subset of  $S^*$  containing  $X$ , and we call this the *internal closure* of  $X$  in  $S^*$ . An *internal neighborhood* of a point  $x \in S^*$  is by definition an internal set  $U \subseteq S^*$  that contains some internally open  $V \subseteq S^*$  with  $x \in V$ .

Let a point  $x \in S$  be given. The *monad*  $\mu(x)$  of  $x$  is by definition the intersection of all sets  $U^*$  with  $U$  a neighborhood of  $x$  in  $S$ . These sets  $U^*$  are among the internal neighborhoods of  $x$ . Now assume that our extension  $\mathbf{S}^*$  is  $\kappa$ -rich with  $\kappa \geq \mathcal{P}(S)$ . Then there are internal neighborhoods of  $x$  that are contained in every such  $U^*$ , that is, there are internal neighborhoods of  $x$  contained in  $\mu(x)$ . Another useful consequence (“overspill”): if  $X \subseteq S^*$  is internal and  $\mu(x) \subseteq X$ , then  $U^* \subseteq X$  for some neighborhood  $U$  of  $x$  in  $S$ .

Let the topological space  $(S', \tau')$  also be part of our structure  $\mathbf{S}$  as explained above; of course we allow  $(S, \tau) = (S', \tau')$ . To deal with the set  $C(S, S')$  of continuous functions  $f : S \rightarrow S'$  we include  $\mathcal{P}(S \times S')$  and  $\in_{S \times S'}$  as part of  $\mathbf{S}$ . Then  $C(S, S')$  is an  $\mathbf{S}$ -definable subset of  $\mathcal{P}(S \times S')$ , where a function is identified with its graph. After Mostowski collapse, the  $\mathbf{S}^*$ -definable set  $C(S, S')^* \subseteq \mathcal{P}(S^* \times S'^*)$  consists of the (graphs of) functions  $g : S^* \rightarrow S'^*$  with the property that  $g^{-1}(U) \in \tau^*$  for all  $U \in \tau'^*$ . It is these functions  $g$  that are called *internally continuous*.

**Ultrapowers.** Fix an infinite index set  $\Lambda$  (often  $\Lambda = \mathbb{N}$ ). An *ultrafilter on  $\Lambda$*  is by definition a collection  $\mathbf{u}$  of subsets of  $\Lambda$  such that for all  $A, B \subseteq \Lambda$ :

- (1)  $\varnothing \notin \mathbf{u}, \Lambda \in \mathbf{u},$
- (2)  $A, B \in \mathbf{u} \implies A \cap B \in \mathbf{u},$
- (3)  $A \in \mathbf{u}, A \subseteq B \implies B \in \mathbf{u},$
- (4)  $A \in \mathbf{u}$  or  $\Lambda \setminus A \in \mathbf{u}.$

An ultrafilter  $\mathbf{u}$  on  $\Lambda$  defines a finitely additive measure  $\mu : \mathcal{P}(\Lambda) \rightarrow \mathbb{R}$  on the boolean algebra  $\mathcal{P}(\Lambda)$  of all subsets of  $\Lambda$ , by setting  $\mu(A) = 0$  if  $A \notin \mathbf{u}$  and  $\mu(A) = 1$  if  $A \in \mathbf{u}$ . So  $\mu(\Lambda) = 1$ , and this measure only takes the values 0 and 1. Any finitely additive measure  $\mu : \mathcal{P}(\Lambda) \rightarrow \mathbb{R}$  taking its values in  $\{0, 1\}$  with  $\mu(\Lambda) = 1$  arises from a unique ultrafilter  $\mathbf{u}$  on  $\Lambda$  in this way. The conditions (1), (2), (3) above define the notion of a *proper filter on  $\Lambda$* . It is routine to check that ultrafilters on  $\Lambda$  are exactly the proper filters on  $\Lambda$  that are maximal with respect to inclusion. Thus by Zorn, every proper filter on  $\Lambda$  is contained in an ultrafilter on  $\Lambda$ .

Given  $\lambda \in \Lambda$ , we have the ultrafilter  $\mathbf{u}(\lambda) := \{A \subseteq \Lambda \mid \lambda \in A\}$ , and ultrafilters of this form are called *principal*. If an ultrafilter  $\mathbf{u}$  on  $\Lambda$  is not principal, it has no finite subset of  $\Lambda$  as an element, and thus

$$\text{cofinite}(\Lambda) := \{A \subseteq \Lambda \mid \Lambda \setminus A \text{ is finite}\} \subseteq \mathbf{u}.$$

Since  $\text{cofinite}(\Lambda)$  is a proper filter on  $\Lambda$ , there do exist ultrafilters  $\mathbf{u}$  on  $\Lambda$  with  $\text{cofinite}(\Lambda) \subseteq \mathbf{u}$ , and these are called *nonprincipal*.

Let  $\mathbf{u}$  be an ultrafilter on  $\Lambda$ . This allows us to extend functorially each set  $S$  to a set  $S^*$  as follows. Elements  $(x_\lambda)$  and  $(y_\lambda)$  of the set  $S^\Lambda$  are said to be  $\mathbf{u}$ -equivalent if  $\{\lambda \in \Lambda \mid x_\lambda = y_\lambda\} \in \mathbf{u}$ , that is,  $x_\lambda = y_\lambda$  for almost all  $\lambda$  in the sense of the measure associated to  $\mathbf{u}$ . This defines an equivalence relation on  $S^\Lambda$ , and we define  $S^*$  to be the set of equivalence classes  $(x_\lambda)/\mathbf{u}$ . We identify  $S$  with a subset of  $S^*$  via the diagonal embedding  $S \rightarrow S^*$ , which sends  $x \in S$  to the equivalence class  $(x_\lambda)/\mathbf{u}$  with  $x_\lambda = x$  for all  $\lambda$ .

Given sets  $S_1, \dots, S_n$  and a relation  $R \subseteq S_1 \times \dots \times S_n$ , we have a relation  $R^* \subseteq S_1^* \times \dots \times S_n^*$  such that for all  $(x_{1\lambda}) \in S_1^\Lambda, \dots, (x_{n\lambda}) \in S_n^\Lambda$ ,

$$((x_{1\lambda})/\mathbf{u}, \dots, (x_{n\lambda})/\mathbf{u}) \in R^* \iff (x_{1\lambda}, \dots, x_{n\lambda}) \in R \text{ for } \mathbf{u}\text{-almost all } \lambda.$$

Then  $R^* \cap (S_1 \times \dots \times S_n) = R$ , and so (NA1) holds with this definition of starring sets and relations among them. Also (NA2) holds by a well-known theorem of Łoś; its proof is easy and can be found in most basic texts on model theory. If  $\mathbf{u}$  is principal, then  $S^* = S$  for all  $S$ , and we get nothing new. But if  $\mathbf{u}$  is nonprincipal and  $\Lambda$  is countable, then (NA3) holds in the sense that  $\mathbf{S}^*$  is

$\aleph_0$ -rich. This is adequate for many applications. For any infinite cardinal  $\kappa$  and any set  $\Lambda$  with  $\#\Lambda \geq \kappa$  there exist ultrafilters  $\mathbf{u}$  on  $\Lambda$  such that for any initial structure  $\mathbf{S}$  the extension  $\mathbf{S}^*$  resulting from  $\mathbf{u}$  as above is  $\kappa$ -rich.

## References

- [1] E. BREUILLARD, B. GREEN and T. TAO, The structure of approximate groups. *Publ. Math. IHES* **116** (2012), 115–221. [Zbl 1260.20062](#) [MR 3090256](#)
- [2] L. VAN DEN DRIES and A.J. WILKIE, Gromov’s theorem on groups of polynomial growth and elementary logic. *J. Algebra* **89** (1984), 349–374. [Zbl 0552.20017](#) [MR 0751150](#)
- [3] A.M. GLEASON, Groups without small subgroups. *Ann. of Math.* **56** (1952), 193–212. [Zbl 0049.30105](#) [MR 0049203](#)
- [4] A.M. GLEASON, On the structure of locally compact groups. *Duke Math. J.* **18** (1951), 85–104.
- [5] I. GOLDBRING, Hilbert’s fifth problem for local groups. *Ann. of Math.* **172** (2010), 1269–1314. [Zbl 1219.22004](#) [MR 2680491](#)
- [6] M. GROMOV, Groups of polynomial growth and expanding maps. *Publ. Math. IHES* **53** (1981), 53–73. [Zbl 0474.20018](#) [MR 0623534](#)
- [7] C.W. HENSON, Foundations of Nonstandard Analysis: A Gentle Introduction to Nonstandard Extensions; Nonstandard Analysis: Theory and Applications. L. O. ARKERYD, N.J. CUTLAND, and C.W. HENSON, eds., NATO Science Series C:, Springer, 2001. [Zbl 0910.03040](#) [MR 1603228](#)
- [8] D. HILBERT, Mathematische Probleme. *Nachr. Akad. Wiss. Göttingen* (1900), 253–297. [JFM 31.0068.03](#)
- [9] J. HIRSCHFELD, The nonstandard treatment of Hilbert’s fifth problem. *Trans. AMS* **321** (1990), 379–400. [Zbl 0705.03033](#) [MR 0967314](#)
- [10] E. HRUSHOVSKI, Stable group theory and approximate subgroups. *Journal of the American Mathematical Society* **25** (2012), 189–243. [Zbl 1259.03049](#) [MR 2833482](#)
- [11] K. IWASAWA, On some types of topological groups. *Ann. of Math.* **2** (1949), 507–557. [Zbl 0034.01803](#) [MR 0029911](#)
- [12] R. JACOBY, Some theorems on the structure of locally compact local groups. *Ann. of Math.* **66** (1957), 36–69. [Zbl 0084.03202](#) [MR 0089997](#)
- [13] I. KAPLANSKY, *Lie Algebras and Locally Compact Groups*. University of Chicago Press, 1971. [Zbl 0223.17001](#) [MR 0276398](#)
- [14] M. KURANISHI, On local euclidean groups satisfying certain conditions. *Proc. Amer. Math. Soc.* **1** (1950), 372–380. [Zbl 0038.01701](#) [MR 0036238](#)
- [15] D. MONTGOMERY and L. ZIPPIN, Small subgroups of finite-dimensional groups. *Ann. of Math.* **56** (1952), 213–241. [Zbl 0049.30106](#) [MR 0049204](#)
- [16] D. MONTGOMERY and L. ZIPPIN, *Topological Transformation Groups*. Interscience, New York, 1955. [Zbl 0068.01904](#) [MR 0073104](#)

- [17] P. OLVER, Non-associative local Lie groups. *Journal of Lie Theory* **6** (1996), 23–51. [Zbl 0862.22005](#) [MR 1406004](#)
- [18] PALAIS, Gleason's Contribution to the Solution of Hilbert's Fifth Problem. *Notices of the AMS* **56** (2009), 1243–1248.
- [19] J.-P. SERRE, Le cinquième problème de Hilbert. Etat de la question en 1951. *Bull. Soc. Math. France* **80** (1952), 1–10. [Zbl 0046.25302](#) [MR 0049205](#)
- [20] T. TAO, *Hilbert's fifth problem and related topics*, American Mathematical Society, 2014. [Zbl 1298.22001](#) [MR 3237440](#)
- [21] H. YAMABE, On the conjecture of Iwasawa and Gleason. *Ann. of Math.* **58** (1953), 48–54. [Zbl 0053.01601](#) [MR 0054613](#)
- [22] H. YAMABE, A generalization of a theorem of Gleason. *Ann. of Math.* **58** (1953), 351–365. [Zbl 0053.01602](#) [MR 0058607](#)

(Reçu le 23 juin 2013)

Lou van den DRIES, University of Illinois, Department of Mathematics, 1409 W. Green Street, Urbana, IL 61801, USA

*e-mail:* [vddries@math.uiuc.edu](mailto:vddries@math.uiuc.edu)

Isaac GOLDBRING, University of Illinois at Chicago, Department of Mathematics, Statistics, and Computer Science, Science and Engineering Offices (M/C 249), 851 S. Morgan St., Chicago, IL 60607, USA

*e-mail:* [isaac@math.uic.edu](mailto:isaac@math.uic.edu)

\section*{Annals of Mathematics}

The Group of Isometries of a Riemannian Manifold
Author(s): S. B. Myers and N. E. Steenrod
Source: Annals of Mathematics, Second Series, Vol. 40, No. 2 (Apr., 1939), pp. 400-416
Published by: Annals of Mathematics
Stable URL: http://www.jstor.org/stable/1968928
Accessed: 25/04/2013 15:36

Your use of the JSTOR archive indicates your acceptance of the Terms \& Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

\title{
THE GROUP OF ISOMETRIES OF A RIEMANNIAN MANIFOLD
}

\author{
By S. B. Myers and N. E. Steenrod
}
(Received February 23, 1938; Revised November 7, 1938)

\section*{1. Introduction}

In the classical theory of groups of motions (isometries) of a Riemannian space, ${ }^{1}$ neither "whole" groups nor "whole" spaces were ever considered, but only "group germs" and spaces in the neighborhood of a point. Furthermore one assumed given a Lie group germ of motions and then deduced theorems concerning the structure of the space. The present paper contains a study of the total group of isometries of a Riemannian manifold in the large. The manifold $M$ is taken of class $C^{r}(r \geqq 2)$; and by an isometry is meant any distance preserving transformation. A natural topology is defined in the group $G$ of all isometries. The motion of a point under the group is studied and is found to describe a submanifold of class $C^{1}$. This leads to the introduction of parameters in $G$ from which it follows that $G$ is locally euclidean. It is then proved that, under these parameters, $G$ is a Lie group of transformations of $M$. The same proposition is proved for any closed subgroup of $G$. Thus the classical theory of Lie groups of motions applies to any closed group of motions.

\section*{2. Lie Groups}

An $r$-parameter Lie group is a topological group whose group space is an $r$-dimensional manifold in which coördinate neighborhoods of class $C^{1}$ (see §3) have been introduced in such a way that the law of composition $C=B \cdot A$ is described locally by functions $\gamma^{i}=\phi^{i}\left(\alpha^{1}, \cdots, \alpha^{r} ; \beta^{1}, \cdots, \beta^{r}\right)$ of class $C^{1}$ ( $(\alpha),(\beta),(\gamma)$ being coördinates for neighborhoods of $A, B, C$ respectively). ${ }^{2}$

An $r$-parameter Lie group of transformations is an $r$-parameter Lie group realized as a group of homeomorphisms of an $n$-dimensional manifold $M$ of class $C^{1}$ (see §3) such that the functions $\bar{x}^{i}=f^{i}\left(x^{1}, \cdots, x^{n} ; \alpha^{1}, \cdots, \alpha^{r}\right)$ describing locally the effect of the transformation $A=(\alpha)$ on the point $P=(x)$ of $M$ have the derivatives $\partial^{2} f^{i} / \partial x^{k} \partial \alpha^{j}$ continuous in $(x, \alpha) .^{3}$

\section*{3. $n$-dimensional Riemannian manifolds}

Consider an ordinary $n$-dimensional manifold $M$; i.e. a connected Hausdorff space each point having a neighborhood which is an $n$-cell. $M$ is said to be

\footnotetext{
${ }^{1}$ See, for example, L. P. Eisenhart, Riemannian Geometry, (1926), Chapt. 6.
${ }^{2}$ It is usually demanded that the $\phi$ 's be analytic; but Garrett Birkhoff has shown how to introduce analytic parameters in a group of class $C^{1}$ : Analytical groups, Trans. Amer. Math. Soc., vol. 43 (1938), pp. 61-101.
${ }^{3}$ It would be sufficient to require that the $\alpha$-derivatives exist at the identity and that these derivatives should satisfy a Lipschitz condition in the $x$ 's.
}
of class $C^{r}$ if to each sufficiently small $n$-cell neighborhood of each point can be attached a coördinate system such that in the region of overlapping of two neighborhoods the transformation between coördinates of the two neighborhoods is of class $C^{r}$ and non-singular. $M$ is a Riemannian manifold of class $C^{r}$ $(r \geqq 1)$ if it is a manifold of class $C^{r+1}$ and if each coördinate neighborhood is provided with a real, positive definite, symmetric quadratic differential form of class $C^{r}$ such that in the region of overlapping of two neighborhoods with respective coördinate systems ( $x$ ) and ( $y$ ) and quadratic forms $g_{i j} d x^{i} d x^{j}$ and $h_{i j} d y^{i} d y^{j}$ we have
$$
g_{i j} d x^{i} d x^{j}=h_{i j} d y^{i} d y^{\prime} \quad(\text { summation } i, j=1, \cdots, n)
$$
under the transformation $y^{i}=y^{i}(x)$.
Arc length along a curve $x^{i}=x^{i}(t)$ is defined in invariant fashion as
$$
s=\int\left(g_{i j} \frac{d x^{i}}{d t} \frac{d x^{j}}{d t}\right)^{\frac{1}{2}} d t .
$$
Here the integral is the Lebesgue integral evaluated along any absolutely continuous representation of a curve admitting such a representation. Such a curve we call an admissible curve. By defining the distance $\rho$ between two points as the greatest lower bound of the lengths of admissible arcs joining the points, we can make $M$ into a metric space satisfying the usual axioms. The topology induced by this metric is equivalent to the original manifold-topology. A second kind of length of an arc $A B$, metric arc length, can be defined as the least upper bound of $\sum_{0}^{n} \rho\left(P_{i}, P_{i+1}\right),\left(P_{0}=A, P_{n+1}=B\right)$, for all ordered subdivisions $P_{1}, P_{2}, \ldots, P_{n}$ of the arc $A B$ and for all $n$. If an arc has finite metric arc length, it is said to be rectifiable.

It has been shown that on a Riemannian manifold a necessary and sufficient condition that an arc be rectifiable is that the functions defining it be of bounded variation. ${ }^{4}$ Thus metric arc length and integral arc length are defined for the same class of arcs, and rectifiable and admissible are equivalent terms. Furthermore it can be proved that the two kinds of arc length are equal. ${ }^{5}$

By a direction at $P$, we shall mean a unit contravariant vector at $P$. That is, a direction at $P$ associates with each admissible coördinate system ( $x$ ) containing $P:\left(x_{0}\right)$ a set of components $(u)=\left(u_{1}, \cdots, u_{n}\right)$ of a contravariant vector, satisfying $g_{i j}\left(x_{0}\right) u^{i} u^{j}=1$. An arc $x^{i}=x^{i}(s)$, where $s$ is the arc length measured from $P$, is said to issue from $P$ in the direction $(u)$ if $x^{i \prime}(0)=u^{i}$. The angle $\theta$ between two directions ( $u$ ) and ( $v$ ) at $P$ is defined as
$$
\cos \theta=g_{i j}\left(x_{0}\right) u^{i} v^{j} .
$$
The space of directions at $P$ is the subspace $g_{i j}\left(x_{0}\right) u^{i} u^{j}=1$ of the $n$-dimensional number space of the variables $(u)$. This space is homeomorphic to the $(n-1)$ -sphere.

\footnotetext{
${ }^{4}$ S. B. Myers, Arc length in metric and Finsler manifolds, Annals of Math., vol. 39 (1938), pp. 463-471.
${ }^{5}$ M. Morse, Functional topology and abstract variational theory, Memorial des Sc. Math., No. 92 (1938), see p. 67.
}

Geodesics are extremals in the calculus of variations problem associated with integral arc length. The following are some important local properties of geodesics. ${ }^{6}$
(A) Points on geodesics are functions of class $C^{r}$ of initial point, initial direction, and length. That is, if $g$ is a geodesic arc $x^{i}=g^{i}(s), 0 \leqq s \leqq l$, issuing from $P:\left(x_{0}\right)$, the equations of the geodesics issuing from points $(\bar{x})$ near $P$ are given by
$$
\begin{equation*}
x^{i}=X^{i}(s, \bar{x}, u), \tag{3.1}
\end{equation*}
$$
where
$$
X^{i}(0, \bar{x}, u) \equiv \bar{x}^{i}, \quad X_{s}^{i}(0, \bar{x}, u) \equiv u^{i}, \quad X^{i}\left(s, x_{0}, x_{0}^{\prime}\right) \equiv g^{i}(s) .
$$
Here $X^{i}$ and $X_{s}^{i}$ are functions of class $C^{r}, s$ represents arc length, while $(s, \bar{x}, u)$ is a set near ( $s, x_{0}, x_{0}^{\prime}$ ). In particular, the equations of geodesics through ( $x_{0}$ ) are given by
$$
\begin{equation*}
x^{2}=X^{i}\left(s, x_{0}, u\right) . \tag{3.2}
\end{equation*}
$$
(B) The equations (3.1) can also be written as
$$
\begin{equation*}
x^{i}=F^{i}(\bar{x}, y) \tag{3.3}
\end{equation*}
$$
where $y^{i}=u^{i} s$. The functions $F^{i}$ are of class $C^{r}$ for $(\bar{x}, y)$ near or at $\left(x_{0}, 0\right)$, and the determinant $\left|F_{y^{j}}^{i}\right| \neq 0$ and $=\delta_{j}^{i}$ at $(\bar{x}, 0)$. Thus the $y$ 's can be used as coördinates near $P:(\bar{x})$, and they are called normal coördinates with $(\bar{x})$ as origin. Every point $P$ on the manifold $M$ has a sphere neighborhood in which normal coördinates with $P$ as origin can be used. Such a neighborhood contains no point conjugate to $P$, is simply covered by the geodesics through $P$, and these geodesics furnish a proper absolute minimum on $M$ to the length of arcs joining their ends. A neighborhood of this type we shall call an $N$-neighborhood of $P$.
(C) For every point $P$ there exists a constant $\delta>0$ such that every sphere neighborhood about $P$ of radius $<\delta$ is an $N$-neighborhood of all its points. Such a neighborhood will be designated as a $\sigma$-neighborhood of $P$.
(D) Let $M_{r}$ be any regular $r$-dimensional submanifold of $M$ of class $C^{r}$ through $P:\left(x_{0}\right)$, with local equations
$$
\begin{equation*}
x^{i}=m^{i}\left(\alpha_{1}, \cdots, \alpha_{r}\right), \quad m^{i}(0)=x_{0}^{i} \quad\left\|m_{\alpha_{\mu}}^{i}\right\| \text { of rank } r . \tag{3.4}
\end{equation*}
$$
Then the equations of the geodesics perpendicular to $M_{r}$ at points of $M_{r}$ near $P_{0}$ can be written
$$
\begin{equation*}
x^{i}=M^{i}(s, \alpha, u), \tag{3.5}
\end{equation*}
$$

\footnotetext{
${ }^{6}$ See J. H. C. Whitehead, On the covering of a complete space by the geodesics through a point, Annals of Math., vol. 36 (1935), pp. 680-685. See also S. S. Cairns, Normal coördinates for extremals transversal to a manifold, Amer. Jour. of Math., vol. 60 (1938), pp. 423-435.
}
where
$$
M^{i}(0, \alpha, u) \equiv m^{i}(\alpha), \quad M_{s}^{i}(0, \alpha, u) \equiv u^{i}
$$
for ( $\alpha$ ) near ( 0 ) and ( $u$ ) satisfying
$$
\begin{equation*}
g_{i j}[m(\alpha)] m_{\alpha_{\mu}}^{i} u^{j}=0 . \tag{3.6}
\end{equation*}
$$
The functions $M^{i}$ are of class $C^{r}$.
(E) The equations of geodesics perpendicular to $M_{r}$ can also be written as
$$
\begin{equation*}
x^{i}=N^{i}(\alpha, z) \quad(z)=\left(z_{r+1}, \cdots, z_{n}\right) \tag{3.7}
\end{equation*}
$$
where $N^{i}(\alpha, 0) \equiv m^{i}(\alpha)$. The functions $N^{i}$ are of class $C^{r}$ for $(\alpha, z)$ near $(0,0)$ and the jacobian of (3.7) does not vanish. For ( $\alpha$ ) constant, the $z$ 's are normal coördinates in the geodesic ( $n-r$ )-dimensional surface perpendicular to $M_{r}$ at ( $\alpha$ ).

To complete our summary of properties of Riemannian manifolds, we state a useful definition and a few lemmas.

Let $P_{k}$ be a set of points converging to $P$, and let $d_{k}$ denote a direction at $P_{k}$. Then we shall say that the directions $d_{k}$ converge to a limit direction $d$ at $P$ if no matter what coördinate system ( $x$ ) about $P$ we use, the components $(u)_{k}$ of $d_{k}$ in that system converge to the components $(u)$ of $d$. To test for such convergence it is sufficient to use just one coördinate system; for the property $(u)_{k} \rightarrow(u)$ is clearly preserved under contravariant transformations.

Lemma 1. Every sequence of directions at a convergent sequence of points has a convergent subsequence.

For if $\sum_{i j} g_{i j}\left(x_{k}\right) u_{k}^{i} u_{k}^{j}=1$, for all $k$ as $k \rightarrow \infty$ and $\left(x_{k}\right) \rightarrow\left(x_{0}\right)$, then standard properties of positive definite quadratic forms show that $\left(u_{k}\right)$ remains bounded.

Lemma 2. If a sequence of functions $x^{i}=x_{k}^{i}(s)$ representing geodesics arcs converges as $k \rightarrow \infty$ to a function $x^{i}=x_{0}^{i}(s)$ representing a geodesic arc, then $x_{k}^{i \prime}(s) \rightarrow x_{0}^{i \prime}(s)$.

This follows from Lemma 1 and (A).
Lemma 3. For a compact set $N$ covered by a coördinate system $(x)$, corresponding to an arbitrary $\epsilon>0$ there exists a $\delta>0$ independent of $Q$ in $N$ such that if two directions at $Q$ form an angle $<\delta$, their respective components $(u)$ and $(v)$ satisfy $\left|v^{i}-u^{i}\right|<\epsilon$.

For if $(u)$ and $(v)$ form an angle $\gamma$, we have
$$
g_{i j}(x)\left(v^{i}-u^{i}\right)\left(v^{j}-u^{j}\right)=2(1-\cos \gamma)=4 \sin ^{2} \frac{\gamma}{2} .
$$
Properties of positive definite quadratic forms enable one to see that $\left|v^{i}-u^{i}\right|$ can be made arbitrarily small by suitable restriction of $\gamma$.

Any property of Riemannian manifolds stated and used later without proof is provable from properties (A)-(E) and lemmas (1)-(3) of this section.

\section*{4. Isometries}

An isometry of a metric space is defined as a distance preserving homeomorphism of the space into itself. On the other hand, one might naturally
define an isometry of a Riemannian manifold $M$ as a homeomorphism of $M$ into itself preserving integral arc length.

Theorem 1. The distance preserving homeomorphisms of a Riemannian manifold $M$ are identical with the homeomorphisms preserving integral arc-length.

For if a homeomorphism of $M$ into itself preserves distance, it preserves metric arc length, hence integral arc length. Also, if a homeomorphism preserves integral arc length, it preserves distance, since the latter is defined as the greatest lower bound of integral arc length.

We note from the minimizing properties of short geodesic arcs that an isometry carries geodesics into geodesics.

Theorem 2. An isometry of a Riemannian manifold of class $C^{1}$ is a transformation of class $C^{1}$.

Necessary and sufficient conditions that a rectifiable arc $C: x^{i}=x^{i}(s)$ have a derivative $x^{i \prime}$ with respect to $s$ at a point $P$ are the following:
(1) The direction $(p)$ of the geodesic $P Q$ at $P$ converges to a direction $\left(p_{0}\right)$ as $Q \rightarrow P$ on $C$.
(2) $\operatorname{Lim}(\Delta r / \Delta s)$ exists, where $\Delta r=\rho(P, Q)$ and $\Delta s=$ length of $P Q$ on $C$.

The sufficiency of these conditions follows from the fact that using normal coördinates ( $y$ ) about $P$, and denoting by ( $\Delta y$ ) the normal coördinates of $Q$, we have
$$
\begin{equation*}
\frac{\Delta y^{i}}{\Delta s}=\frac{\dot{\Delta y} y^{i}}{\Delta r} \cdot \frac{\Delta r}{\Delta s}=p^{i} \frac{\Delta r}{\Delta s} . \tag{4.1}
\end{equation*}
$$
The necessity of conditions is proved as follows. Let $h_{i j}(y)$ be the coefficients of the fundamental quadratic form in the coördinates $(y)$. Then
$$
\Delta r=\Delta r\left(h_{i j}(0) p^{i} p^{j}\right)^{\frac{1}{2}}=\left(h_{i j}(0) p^{i} \Delta r p^{j} \Delta r\right)^{\frac{1}{2}}=\left(h_{i j}(0) \Delta y^{i} \Delta y^{j}\right)^{\frac{1}{2}} .
$$
Hence
$$
\lim \frac{\Delta r}{\Delta s}=\left(h_{i j}(0) \frac{d y^{i}}{d s} \frac{d y^{\lambda}}{d s}\right)^{\frac{1}{2}} .
$$
From (4.1) it follows that $\lim p^{i}$ also exists.
Now the first of the two conditions is invariant under an isometry because of the continuity in points and directions of the transformations of geodesics effected by an isometry. The second condition is obviously invariant. Hence if $C$ has a direction at $P$, its image $\bar{C}$ has a direction at $\bar{P}$, so that we may say that an isometry carries a direction into a direction. Furthermore, the new direction varies continuously with the old direction and the point at which it is taken.

Under these circumstances, an isometry must be of class $C^{1}$. For consider the curve
$$
\begin{equation*}
x^{1}=a(s, c), \quad(c)=\left(c^{2}, \cdots, c^{n}\right) ; \quad x^{k}=c^{k} \quad(k=2, \cdots, n), \tag{4.2}
\end{equation*}
$$
where $a(s, c)$ is obtained by solving
$$
\begin{equation*}
s=\int_{c^{1}}^{x^{1}}\left(g_{11}\left(x^{1}, c^{2}, \cdots, c^{n}\right)\right)^{\frac{1}{2}} d x^{1} \tag{4.3}
\end{equation*}
$$
for $x^{1}$. The function $a(s, c)$ is of class $C^{1}$. Hence after performing the isometry $y^{i}=y^{i}(x)$, the curve $y^{i}=y^{i}[a(s, c), c]$ has a derivative $D$ with respect to $s$. But $\partial a / \partial s$ exists, hence $\partial y^{i} / \partial x^{1}$ exists, and
$$
D=\frac{\partial y^{i}}{\partial x^{1}}[a(s, c), c] \frac{\partial a}{\partial s}(s, c) .
$$
Furthermore $D$ is continuous in $(s, c)$. Also $\partial a / \partial s$ is continuous in $(s, c)$ and $\neq 0$. Hence $\partial y^{i} / \partial x^{1}$ is continuous in ( $s, c$ ). But (4.3) is continuous in $x^{1}$ and $c$; hence $\partial y^{i} / \partial x^{1}$ is continuous in ( $x^{1}, c$ ). Similarly $\partial y^{i} / \partial x^{k}(k=2, \cdots, n)$ exists and is continuous.

An immediate consequence of this theorem is that an isometry transforms vectors and tensors according to the usual laws, transforms the space of directions at a point linearly, and preserves angles.

Theorem 3. If an isometry $T$ leaves fixed $n+1$ points so close together that $n$ of them lie in an $N$-neighborhood of the other, and if the points are linearly independent (i.e. not in the same $(n-1)$-dimensional geodesic hypersurface), then $T$ is the identity.

Suppose $T$ leaves fixed the $n+1$ linearly independent points $P_{0}, P_{1}, \ldots, P_{n}$, of which $P_{1}, \ldots, P_{n}$ lie in the $N$-neighborhood $\sigma$ of $P_{0}$. Then the short geodesics $P_{0} P_{1}, P_{0} P_{2}, \cdots, P_{0} P_{n}$ are fixed under $T$, so are their initial directions, and hence the linear homogeneous transformation of the space of directions at $P_{0}$ induced by $T$ is the identity. Hence all geodesic arcs issuing from $P_{0}$ are fixed; since length is preserved, they are pointwise fixed. Thus any $N$-neighborhood of $P_{0}$ is pointwise fixed. If $Q$ is a point in an $N$-neighborhood of $P_{0}$, any $N$-neighborhood of $Q$ is similarly pointwise fixed. But $P_{0}$ can be joined to any point $P$ in $M$ by a broken geodesic arc with a finite number of pieces, each corner being in an $N$-neighborhood of the preceding corner. Thus $P$ is fixed.

Corollary. There is at most one isometry which carries $n+1$ points $P_{i}$ of the kind described in the theorem into $n+1$ points $Q_{i}$.

For if we had two such isometries $T$ and $T^{\prime}$, then by the theorem, $T^{-1} T^{\prime}$ would leave fixed $P_{i}$, and so would be the identity.

\section*{5. The group of isometries and its topology}

The isometries of $M$ form a group, which we shall call $G$. A sequence of isometries $T_{k}$ will be said to converge to an isometry $T$ if for every $P$ in $M$, $T_{k}(P) \rightarrow T(P)$. With this notion of convergence, the group can be shown
to be continuous. It can also be shown ${ }^{7}$ that if $T_{k}(P)$ converges to a point $\bar{P}$, there exists a subsequence $T_{k}^{\prime}$ of $T_{k}$ converging to an isometry $T$ such that $T(P)=\bar{P}$. If $T_{k}(P)$ converges to $P, T$ leaves $P$ fixed; the sequence $T_{k}^{\prime} T^{-1}$ takes $P$ into the same set of points as $T_{k}^{\prime}$, and converges to the identity. It follows that if $M$ is compact, $G$ is compact (i.e. every sequence of isometries in $G$ has a subsequence converging to an isometry in $G$ ). In these properties, $G$ could be replaced by a closed subgroup $H$ of $G$.

Without difficulty, we can now topologize, in fact metrize, $G$ so that we obtain the above notion of convergence. Consider any set of $n+1$ points of the kind used in Theorem 3. Then the distance $d(T, \bar{T})$ between two isometries $T$ and $\bar{T}$ will be defined as the maximum of the distance $\rho[T(P), \bar{T}(P)]$ as $P$ ranges over the given set of $n+1$ points. This distance can be shown to satisfy the usual metric axioms. Obviously the previous notion of convergence of isometries $T_{i}$ to $T$ implies $d\left(T_{i}, T\right) \rightarrow 0$; we must show that $d\left(T_{i}, T\right) \rightarrow 0$ implies $T_{i}(P) \rightarrow T(P)$ for all $P$ on $M$. This will not only show that convergence in this new topology is equivalent to the previous notion of convergence, but also that the new topology is independent of the particular set of $n+1$ points used.

If it were not true that from $d\left(T_{i}, T\right) \rightarrow 0$ follows $T_{i}(P) \rightarrow T(P)$ for all $P$, there would exist a point $Q$, an $\epsilon>0$, and a subsequence $T_{i}^{\prime}$ of $T_{i}$ such that
$$
\begin{equation*}
\rho\left[T_{i}^{\prime}(Q), T(Q)\right]>\epsilon \quad \text { for all } i . \tag{5.1}
\end{equation*}
$$
But we know that $T_{i}^{\prime}(P) \rightarrow T(P)$ for all $P$ on the given set of $n+1$ points; hence $T_{i}^{\prime}$ must contain a subsequence $T_{i}^{\prime \prime}$ such that there exists an isometry $T^{\prime}$ with $T_{i}^{\prime \prime}(P) \rightarrow T^{\prime}(P)$ for all $P$. Now $T^{\prime}(P)=T(P)$ for $P$ on the given set of $n+1$ points; hence by the corollary to Theorem $3, T^{\prime}=T$. This contradicts (5.1), and the proof is complete.

We could equally well have defined $d(T, \bar{T})$ as the maximum of $\rho[T(P), \bar{T}(P)]$ for all $P$ on a compact subset of $M$ containing an open set. If $M$ is compact, an obvious choice of the subset is $M$ itself.

Lemma 4. If a sequence of isometries $T_{k}$ converges to an isometry $T$, as a sequence of transformations of the space of directions at any point $P_{0}$ it converges uniformly.

Without loss of generality, assume $T=$ identity. Let $T_{k}\left(P_{0}\right)=P_{k}$. Then $T_{k}$ transforms each geodesic arc issuing from $P_{0}$ in a direction $(u)_{0}$ into a sequence of geodesic arcs issuing from $P_{k}$ and satisfying the hypotheses of Lemma 2, hence $(u)_{k}=T_{k}(u)_{0} \rightarrow(u)_{0}$. Also, $T_{k}$ transforms the compact space of directions at $P_{0}$ in a one-to-one continuous manner and this continuity of $T_{k}$ in direction is uniform in $k$. That is, for an arbitrary $\epsilon>0$ there exists a $d>0$ independent of $k$ such that, if $\left|v_{0}^{i}-u_{0}^{i}\right|<d$, then $\left|v_{k}^{i}-u_{k}^{i}\right|<\epsilon$. For we simply choose $d$ so small that, if $\left|v_{0}^{i}-u_{0}^{i}\right|<d$, then the angle between

\footnotetext{
${ }^{7}$ Van Dantzig and van der Waerden, Über metrisch homogene Räume, Abh. Math. Sem. Hamburg, vol. 6 (1928), pp. 374-376.
}
$(v)_{0}$ and $(u)_{0}$ is less than the $\delta$ of Lemma 3; the angle between $(v)_{k}$ and $(u)_{k}$ will also be less than $\delta$, and Lemma 3 tells us that $\left|v_{k}^{i}-u_{k}^{i}\right|<\epsilon$ independent of $k$ (for $k$ large enough).

Now let $\epsilon$ be arbitrary again. By what we have just shown, we can choose a finite set of directions at $P_{0}, \epsilon / 3$-dense in the direction space at $P_{0}$, whose transforms at $P_{k}$ are also $\epsilon / 3$-dense in the direction space at $P_{k}$. Now let $N$ be taken so large that for $k>N$ each of our finite set of directions at $P_{k}$, say $(v)_{k}$ is within $\epsilon / 3$ of its limit direction at $P_{0}$, i.e. $\left|v_{k}^{i}-v_{0}^{i}\right|<\epsilon / 3$ for $k>N$. But for an arbitrary direction $(u)_{k}$ at $P_{k}$, we have (for one of the $(v)_{k}$ 's) $\left|u_{k}^{i}-v_{k}^{i}\right|<\epsilon / 3$ and $\left|u_{0}^{i}-v_{0}^{i}\right|<\epsilon / 3$. Thus $\left|u_{k}^{i}-u_{0}^{i}\right|<\epsilon$ for $k>N$. This proves the lemma.

\section*{6. The set of equivalent points}

Two points are said to be equivalent under a closed subgroup $H$ of $G$ if there exists an isometry of $H$ taking one point into the other. According to §5, the set $\gamma$ of points equivalent under $H$ to a point $P_{0}$ of $M$ is closed. We shall find properties of the group $H$ by a study of the set of points $\gamma$.

The point $P_{0}$ is said to be a limit point of equivalent points $P_{k}$ from a direction ( $u$ ) if $P_{k} \rightarrow P_{0}$ and the directions at $P_{0}$ of the short geodesics $P_{0} P_{k}$ converge to the direction $(u)$.

Theorem 4. If $P_{0}:\left(x_{0}\right)$ is a limit point of equivalent points $P_{k}$ from a direction $\left(u_{0}\right)$, it is also a limit point of equivalent points from the opposite direction $\left(-u_{0}\right)$.

Let us pass immediately to a sequence $T_{k}$ such that the isometries $T_{k}$ taking $P_{0}$ into $P_{k}$ converge to the identity. We consider three sets of directions: the direction $\left(u_{k}\right)$ of the geodesic $P_{0} P_{k}$ at $P_{0}$, the direction $\left(v_{k}\right)$ of the geodesic $P_{0} P_{k}$ at $P_{k}$, and the direction ( $w_{k}$ ) at $P_{0}$ which is transformed into ( $v_{k}$ ) by $T_{k}$. We note that $\left(u_{k}\right) \rightarrow\left(u_{0}\right)$. The equations of the geodesics through $P_{0}$ are given by (3.2). If we differentiate with respect to $s$, we obtain
$$
\begin{equation*}
x^{i \prime}=X_{s}^{i}\left(s, x_{0}, u\right) . \tag{6.1}
\end{equation*}
$$
Now $v_{k}^{i}=X_{s}^{i}\left(s_{k}, x_{0}, u_{k}\right)$ and $u_{0}^{i}=X_{s}^{i}\left(0, x_{0}, u_{0}\right)$ where $s_{k}$ is the distance $P_{0} P_{k}$. As $k \rightarrow \infty, s_{k} \rightarrow 0$, and $\left(u_{k}\right) \rightarrow\left(u_{0}\right)$. The continuity of the functions (6.1) tells us that $\left(v_{k}\right) \rightarrow\left(u_{0}\right)$.

But by Lemma 4, if $k$ is large enough, $\left|v_{k}^{i}-w_{k}^{i}\right|<\epsilon$ for a given $\epsilon>0$. Hence $\left(w_{k}\right)$ also converges to $\left(u_{0}\right)$. Now the geodesic $h_{k}$ issuing from $P_{0}$ in the direction $\left(w_{k}\right)$ is transformed by $T_{k}$ into the extension of the geodesic $P_{0} P_{k}$. Hence there is a point on $h_{k}$ equivalent to $P_{0}$ at a distance of $\rho\left(P_{0}, P_{k}\right)$ before it. Thus $P_{0}$ is a limit of equivalent points from the direction ( $-u_{0}$ ).

Theorem 5. The set of point of $M$ equivalent to $P_{0}$ under a closed subgroup $H$ of $G$ is locally euclidean or discrete.

First, if the set $\gamma_{n}$ of points near $P_{0}$ equivalent to $P_{0}$ is an $n$-cell, the theorem is true. The total set of points equivalent to $P_{0}$ is, in this case, the whole of $M$; for the set is homogeneous, hence open in $M$, and at the same time closed in $M$.

In general, arbitrarily close to $P_{0}$ is a point not equivalent to $P_{0}$ and hence
not a limit point of points equivalent to $P_{0}$. Let $Q$ be such a point in a small $\sigma$-neighborhood $\sigma$ of $P_{0}$. (Henceforth everything will take place inside $\sigma$ ). Let $r$ be the distance from $Q$ to a nearest point $A$ equivalent to $P_{0}$. The set of points $P$ such that $\rho(Q, P)<r$ contains no point equivalent to $P_{0}$. The locus $\Sigma$ of points $P$ such that $\rho(Q, P)=r$ will be entirely within $\sigma$ if $Q$ was taken close enough to $P_{0}$. The set $\Sigma$ is homeomorphic to an $(n-1)$-sphere, and is given by equations
$$
\begin{equation*}
x^{i}=X^{i}\left(r, x_{Q}, u\right)=x^{i}(u) \tag{6.2}
\end{equation*}
$$
where
$$
\begin{equation*}
g_{i j}\left(x_{Q}\right) u^{i} u^{j}=1 . \tag{6.3}
\end{equation*}
$$
These are obtained from (3.1) by substituting $(\bar{x})=\left(x_{Q}\right), s=r$. Locally we can put (6.3) into parametric form $u^{i}=u^{i}\left(\alpha_{1}, \cdots, \alpha_{n-1}\right)$, obtaining a local representation of class $C^{1}$ for $\Sigma: x^{i}=x^{i}[u(\alpha)]=f^{i}(\alpha)$. This representation is regular; i.e., $\left\|f_{\alpha_{\mu}}^{i}\right\|$ is of rank $n-1$; otherwise we would have $\operatorname{det}\left(\left\|X_{s}^{i}\right\| \cdot\left\|X_{u}^{i}{ }^{i} u_{\alpha_{\mu}}^{i}\right\|\right)=0$ contradicting the fact that $Q$ has no conjugate point in $\sigma$. Hence at every one of its points, in particular at $A, \Sigma$ is a regular manifold of class $C^{1}$ and has a tangent $(n-1)$-dimensional space $\tau$ of directions.

Now it can be seen that $A$ cannot be a limit point of equivalent points from any direction but those of $\tau$. For suppose the contrary, then by Theorem 4, $A$ is a limit point of equivalent points from two opposite directions. The geodesic ray $g$ issuing from $A$ in one of these two directions, say $(u)$, goes into the interior of $\Sigma$; it lies within this interior for a certain length $d$. Geodesics from $A$ in directions in a small neighborhood of ( $u$ ) have the same property with the same number $d$. Since $A$ is a limit point of equivalent points from the direction $(u)$, there exists a sequence of equivalent points $A_{k}$ converging to $A$ such that the directions at $A$ of the geodesics $A A_{k}$ converge to ( $u$ ); this sequence must be interior to $\Sigma$, contradicting the fact that $A$ was the nearest point to $Q$ equivalent to $P_{0}$.

Thus the point $A$ can be a limit point of equivalent points only from directions in an ( $n-1$ )-dimensional space of directions, and the same statement must apply to $P_{0}$. Let $\tau_{n-1}$ be this space of directions at $P_{0}$, and let $H_{n-1}$ be a regular $(n-1)$-dimensional submanifold of $M$ of class $C^{2}$ and tangent to $\tau_{n-1}$ at $P_{0}$. We will set up a homeomorphism between the set $\gamma_{n}$ of points equivalent to $P_{0}$ near it in $M$ and a subset of the points of $H_{n-1}$ near $P_{0}$.

The geodesics issuing from points of $H_{n-1}$ near $P_{0}$ perpendicular to $H_{n-1}$ simply cover a neighborhood of $P_{0}$ in $M$ according to (E). To every point $P$ equivalent to $P_{0}$ in a sufficiently small neighborhood of $P_{0}$ we make correspond the foot of the unique perpendicular geodesic from $P$ to $H_{n-1}$. We will show that this correspondence $C$ is $1-1$ in a small neighborhood of $P_{0}$.

If two points $P$ and $Q$ equivalent to $P_{0}$ correspond under $C$ to the same point $B$ of $H_{n-1}, P$ and $Q$ both lie on the geodesic through $B$ perpendicular to $H_{n-1}$. If this situation occurs in an arbitrarily small neighborhood of $P_{0}$,
there exists a sequence of points $P_{k}$ equivalent to $P_{0}$ converging to $P_{0}$, each of which lies on a geodesic $P_{k} Q_{k}$, perpendicular to $H_{n-1}$, containing another point $Q_{k}$ equivalent to $P_{0}$, while $\rho\left(P_{k}, Q_{k}\right) \rightarrow 0$. Choosing a sequence of isometries $T_{k}$ converging to the identity such that $T_{k}$ takes $P_{0}$ into $P_{k}$, let $h_{k}$ be the geodesic that $T_{k}$ takes into $P_{k} Q_{k}$. Then by Lemma 4, if $k$ is large enough the difference between the direction of $h_{k}$ at $P_{0}$ and the direction of $P_{k} Q_{k}$ at $H_{n-1}$ will be less than $\epsilon$ (arbitrary). Also, for $k$ large enough, the difference between the direction of $P_{k} Q_{k}$ at $H_{n-1}$ and its direction at $P_{k}$ is $<\epsilon$. This follows from the fact that the functions $\partial M^{i} / \partial s$ of (3.5) are continuous in $s$ uniformly in ( $\alpha$ ). The directions of a subsequence $P_{k}^{\prime} Q_{k}^{\prime}$ of the geodesics $P_{k} Q_{k}$ at $H_{n-1}$ converge to a direction ( $u$ ) perpendicular to $H_{n-1}$ at $P_{0}$. Hence the directions of $P_{k}^{\prime} Q_{k}^{\prime}$ at $P_{k}^{\prime}$, and also the directions of $h_{k}^{\prime}$ at $P_{0}$, converge to $(u)$. Thus $P_{0}$ is a limit point of equivalent points $R_{k}=T_{k}^{-1}\left(Q_{k}^{\prime}\right)$ from a direction perpendicular to $H_{n-1}$ at $P_{0}$, which contradicts the definition of $H_{n-1}$.

Hence there exists a compact neighborhood $\sigma_{n}$ of $P_{0}$ in $M$ in which the set $\bar{\gamma}_{n}$ of points equivalent to $P_{0}$ is in a $1-1$ correspondence $C$ with a subset $\bar{\gamma}_{n-1}$ of an ( $n-1$ )-cell in $H_{n-1}$ containing $P_{0}$. As a transformation from $\bar{\gamma}_{n}$ to $\bar{\gamma}_{n-1}, C$ is continuous. Since $\bar{\gamma}_{n}$ is compact, $C$ is bicontinuous, hence a homeo-morphism.

We will say that the set $\gamma_{n}$ has the property $A_{n-p}(1 \leqq p \leqq n)$ if
(1) $P_{0}$ is a limit point of equivalent points from at most an $(n-p)$-dimensional space of directions $\tau_{n-p}$; and
(2) $\gamma_{n}$ is homeomorphic to a subset $\gamma_{n-p}$ of an $(n-p)$-dimensional regular submanifold $H_{n-p}$ of $M$ of class $C^{2}$ tangent to $\tau_{n-p}$ at $P_{0}$, the homeomorphism being obtained by making a point $P$ of $\gamma_{n}$ correspond to the foot of the perpendicular geodesic from $P$ to $H_{n-p}$.

We have already proved that either $\gamma_{n}$ is an $n$-cell, or else it has property $A_{n-1}$. We now prove generally that if $\gamma_{n}$ has property $A_{n-p}$, either it is an ( $n-p$ )-cell, or else it has property $A_{n-p-1}$.

Assume $\gamma_{n}$ has property $A_{n-p}$, but is not an $(n-p)$-cell. There will be a sequence of points $P_{k}$ in $H_{n-p}$ converging to $P_{0}$ no one of them in $\gamma_{n-p}$. The set $\gamma_{n-p}$ is closed (since $\gamma_{n}$ is closed). Hence around each $P_{k}$ can be found a sphere neighborhood in $H_{n-p}$ containing no points of $\gamma_{n-p}$. Let $r_{k}$ be the upper bound of the radii of such sphere neighborhoods of the point $P_{k}$; then the $(n-p-1)$-sphere $R_{k}$ of radius $r_{k}$ about $P_{k}$ in $H_{n-p}$ has a point $W_{k}$ of $\gamma_{n-p}$ on it, but no points of $\gamma_{n-p}$ interior to it. Erect all geodesics in $M$ in directions perpendicular to $H_{n-p}$ at the points of this sphere and its interior $\sigma_{k}$. There will be $p$ linearly independent such directions at each point. By (E), if $P_{k}$ is close enough to $P_{0}$, these geodesics simply cover an $n$-dimensional cell. The geodesics perpendicular to $H_{n-p}$ at the points of $R_{k}$ form an ( $n-1$ )-dimensional cylindrical boundary $S_{k}$ of the $n$-cell (topologically the product of an $(n-p-1)$-sphere by a $p$-plane). Then $S_{k}$ contains a point $Z_{k}$ equivalent to $P_{0}$, but in the interior of the $n$-cell bounded by $S_{k}$ are no points equivalent to $P_{0}$. Using (D) and (E), it can be shown that $S_{k}$ is a regular manifold of
class $C^{1}$. Following reasoning used previously, $Z_{k}$ can be a limit point of equivalent points at most from directions in the $(n-1)$-plane of directions $\lambda_{k}$ tangent to $S_{k}$ at $Z_{k}$.

Now as $k \rightarrow \infty$, a subsequence $\lambda_{k}^{\prime}$ of $\lambda_{k}$ will converge to an ( $n-1$ )-dimensional space of directions $\lambda_{0}$ at $P_{0}$ containing $p$ linearly independent directions perpendicular to $H_{n-p}$ at $P_{0}$. Let $T_{k}$ be a sequence of isometries converging to the identity and taking $P_{0}$ into $Z_{k}^{\prime}$, and let $\xi_{k}$ be the $(n-1)$-dimensional space of directions at $P_{0}$ which $T_{k}$ takes into $\lambda_{k}^{\prime}$. The point $P_{0}$ can be a limit point of equivalent points at most from directions in $\xi_{k}$. By Lemma 4, since $\lambda_{k}^{\prime}$ converges to $\lambda_{0}$, so does $\xi_{k}$. Choose a value of $k$ so large that $\xi_{k}$ contains $p$ linearly independent directions each almost perpendicular to $H_{n-p}$ at $P_{0}$. Then the intersection of $\xi_{k}$ and $\tau_{n-p}$ (the plane of directions tangent to $H_{n-p}$ at $P_{0}$ ) is at most ( $n-p-1$ )-dimensional. Thus we have proved that $P_{0}$ is a limit point of equivalent points from at most an ( $n-p-1$ )-dimensional space of directions $\tau_{n-p-1}$, the first part of property $A_{n-p-1}$.

Now let $H_{n-p-1}$ be a regular ( $n-p-1$ )-dimensional manifold of class $C^{2}$ tangent to $\tau_{n-p-1}$ at $P_{0}$. Set up the correspondence $C$ between points of $\gamma_{n}$ and the feet of the geodesics drawn from the points of $\gamma_{n}$ perpendicular to $H_{n-p-1}$. If $C$ is not 1-1 in some small neighborhood of $P_{0}$, there would be a sequence of pairs of points $P_{k}$ and $Q_{k}$ of $\gamma_{n}$ converging to $P_{0}$ such that the geodesic drawn from $P_{k}$ perpendicular to $H_{n-p-1}$ and the geodesic drawn from $Q_{k}$ perpendicular to $H_{n-p-1}$ would intersect $H_{n-p-1}$ at the same point $D_{k}$. Thus $P_{k}$ and $Q_{k}$ would lie on the geodesic $(p+1)$-surface $G_{k}$ perpendicular to $H_{n-p-1}$ at $D_{k}$. Draw the geodesic $P_{k} Q_{k}$.

Now we shall show that a subsequence of the directions ( $u_{k}$ ) of $P_{k} Q_{k}$ at $P_{k}$ converges to a direction at $P_{0}$ tangent to $G_{0}$, the geodesic surface perpendicular to $H_{n-p-1}$ at $P_{0}$. Let us use the coördinates ( $\alpha, z$ ) of ( E ) ( $\S 3$ ) based on $H_{n-p-1}$ at $P_{0}$. The equations of $G_{k}$ are $\alpha_{\mu}=$ constant . Writing the equations of the geodesics $P_{k} Q_{k}$ as
$$
\alpha_{\mu}=\alpha_{\mu}(s), \quad z_{r}=z_{r}(s),
$$
by the law of the mean, at some point on $P_{k} Q_{k}$ between $P_{k}$ and $Q_{k}$ we must have $\alpha_{\mu}^{\prime}=0$. As $k \rightarrow \infty, P_{k}$ and $Q_{k}$ approach $P_{0}, \rho\left(P_{k}, Q_{k}\right) \rightarrow 0$, and $\left(u_{k}\right)$ has at least one limiting direction $\left(u_{0}\right)$ at $P_{0}$. By the continuity of the functions (6.1), the first $n-p-1$ components of $\left(u_{0}\right)$ must be zero (in the coördinate system ( $\alpha, z$ )). Hence ( $u_{0}$ ) is tangent to $G_{0}$, and so a subsequence of ( $u_{k}$ ) converges to a direction perpendicular to $H_{n-p-1}$.

Following the usual procedure, we now let $T_{k}$ be a sequence of isometries converging to the identity and taking $P_{0}$ into $P_{k}$, and let $\left(v_{k}\right)$ denote the direction which $T_{k}$ takes into $\left(u_{k}\right)$. Then by Lemma 4, since $\left(u_{k}\right)$ converges to $\left(u_{0}\right)$, so does $\left(v_{k}\right)$. But this means that $P_{0}$ is a limit point of equivalent points $B_{k}=T_{k}^{-1}\left(Q_{k}\right)$ from the direction ( $u_{0}$ ) perpendicular to $H_{n-p-1}$ at $P_{0}$, contradicting the definition of $H_{n-p-1}$.

Thus the correspondence $C$ between points of $\gamma_{n}$ and points of a subset
$\gamma_{n-p-1}$ of $H_{n-p-1}$ is $1-1$. It is easily shown to be continuous, and so is a homeomorphism.

This completes the proof that if $\gamma_{n}$ has property $A_{n-p}$, then either it is an $(n-p)$-cell, or else it has property $A_{n-p-1}$. But this brings to a conclusion the proof of Theorem 5. For it is now clear that either $\gamma_{n}$ is a $q$-cell for some $q$ between 0 and $n$, or else it has property $A_{0}$. The latter means that $\gamma_{n}$ consists entirely of $P_{0}$. Since the total set of points equivalent to $P_{0}$ is homogeneous it is everywhere locally euclidean or it is discrete.

In order to prove that $\gamma_{n}$ is a manifold of class $C^{1}$ we shall need the following lemma.

Lemma 5. Let $x^{i}=x^{i}(t)$ be an arc $C$ issuing from a point $P_{0}:\left(x_{0}\right)$. Let $Q$ be a nearby point on $C$, with coördinates $\left(x_{0}+\Delta x\right)$, and let $\Delta r$ be the distance from $P_{0}$ to $Q$. Then if the direction ( $p$ ) of the geodesic $P_{0} Q$ converges as $Q \rightarrow P_{0}$ to a unique limiting direction $\left(p_{0}\right)$ at $P_{0}$, the ratio $\Delta x^{i} / \Delta r$ approaches $p_{0}^{i}$.

Transform from the coördinates $(x)$ to normal coördinates $(y)$ with $P_{0}$ as origin. Call the new coördinates of $Q(\Delta y)$. The components of directions issuing from $P_{0}$ are the same in the coördinate system ( $y$ ) as in the system ( $x$ ). Now $\Delta y^{i}=p^{i} \Delta r$. Therefore $\lim \left(\Delta y^{i} / \Delta r\right)=\lim p^{i}=p_{0}^{i}$. Transform back to the coördinates $(x)$, and use the fact that the jacobian of the transformation at $P_{0}$ is the unit matrix.

Theorem 6. The set of points of $M$ equivalent to $P$ under a closed subgroup $H$ of $G$ is a regular submanifold of $M$ of class $C^{1}$.

Let $P_{0}$ be an arbitrary point of the manifold $S$ of equivalent points. Suppose $S$ is $r$-dimensional. We know that $P_{0}$ is a limit point of $S$ only from directions in a certain $r$-plane $\tau_{r}$ of directions at $P_{0}$. Let $M_{r}$ be a regular $r$-dimensional submanifold of $M$ of class $C^{2}$ tangent to $\tau_{r}$ at $P_{0}$. Transform from given coördinates ( $x$ ) to the coördinates ( $\alpha, z$ ) of ( E ) (see §3), based on $M_{r}$ about $P_{0}$. The equations of $M_{r}$ are $z^{r+1}=\cdots=z^{n}=0$, while $(\alpha)=$ constant represents a geodesic $(n-r)$-dimensional manifold normal to $M_{r}$. We know from the proof of Theorem 5 that there is a homeomorphism between points of $S$ and $M_{r}$ neighboring $P_{0}$ in which a point of $S$ corresponds to the foot of the perpendicular geodesic from it to $M_{r}$. Corresponding points in $S$ and $M_{r}$ now have the same ( $\alpha$ ) coördinates. We can use ( $\alpha$ ) as parameters in $S$, and write the equations of $S$ as
$$
\alpha^{\mu}=\alpha^{\mu} \quad(\mu=1, \cdots, r), \quad z^{\tau}=z^{\tau}(\alpha) \quad(\tau=r+1, \cdots, n) .
$$

Let $\bar{P}:(\bar{\alpha}, \bar{z})$ be any point of $S$ near $P_{0}$. Consider the curve $C$ on $S$ through $\bar{P}$ defined by
$$
\alpha^{1}=t, \quad \alpha^{\rho}=\bar{\alpha}^{\rho}(\rho=2, \cdots, r), \quad z^{\tau}=z^{\tau}\left(t, \bar{\alpha}^{2}, \cdots, \bar{\alpha}^{r}\right), \quad\left(t \text { near } \bar{\alpha}^{1}\right) .
$$

Let $Q$ be a nearby point on $C$. Denote the geodesic $\bar{P} Q$ by $\cdot g$, its direction at $\bar{P}$ by (h). Let ( $\bar{h}$ ) be any limiting direction of (h) as $Q \rightarrow \bar{P}$; we shall prove that $(\bar{h})$ is unique.

By the law of the mean, at some point on $g$ between $\bar{P}$ and $Q$ the $\rho^{\text {th }}$ com-
ponent $(\rho=2, \cdots, r)$ of the direction of $g$ is zero. Letting $Q \rightarrow \bar{P}$, and using the continuity of (6.1), it follows that $\bar{h}^{\rho}=0(\rho=2, \cdots, r)$. Also we know that $(\bar{h})$ must lie in a certain $r$-plane $\bar{\tau}_{r}$ of directions at $\bar{P}$. This $r$-plane can be made arbitrarily close to the corresponding $r$-plane $\tau_{r}$ at $P_{0}$ by taking $\bar{P}$ close enough to $P_{0}$, using Lemma 4 in the usual way. The conditions that a direction (d) at $P_{0}$ lie in $\tau_{r}$ are $d^{r+1}=\cdots=d^{n}=0$. Hence the $n-r$ linear homogeneous conditions that $(\bar{h})$ lie in $\bar{\tau}_{r}$ must also be linearly independent on $\left(\bar{h}^{r+1}, \ldots, \bar{h}^{n}\right)$.

Thus $\bar{h}^{2}, \cdots, \bar{h}^{n}$ are determined in terms of $\bar{h}^{1}$, which must be $\neq 0$. The fact that $(\bar{h})$ is a unit vector furnishes the proof of its uniqueness.

We now apply Lemma 5 which gives $\lim \left(\Delta z^{\tau} / \Delta r\right)=\bar{h}^{1}$ as $Q \rightarrow \bar{P}$. This together with $\lim \left(\Delta \alpha^{1} / \Delta r\right)=\bar{h}^{1} \neq 0$ proves the existence of $\partial z^{\tau} / \partial \alpha^{1}$ at $(\bar{\alpha})$. Similarly $\partial z^{\tau} / \partial \alpha^{\rho}$ exists.

The continuity of these derivatives follows from the facts already mentioned concerning the continuous variation of $\bar{\tau}_{r}$ with ( $\bar{\alpha}$ ).

Thus the $z^{\tau}(\alpha)$ are of class $C^{1}$ near $P_{0}$. We can transform back to the original coördinates $(x)$ and obtain a local representation of $S: x^{i}=x^{i}(\alpha)$ of class $C^{1}$, with functional matrix of rank $r$. This proves Theorem 6.

\section*{7. Closed groups of isometries}

Let $M^{n+1}$ be the product manifold of $M$ taken with itself $n+1$ times. A point of $M^{n+1}$ is an ordered set of $n+1$ points of $M$. Coördinate neighborhoods in $M^{n+1}$ are the products of $n+1$ coördinate neighborhoods in $M$ and the fundamental form in such a neighborhood is the sum of the quadratic forms of the corresponding neighborhoods in $M$. Thus $M^{n+1}$ is a Riemannian manifold of the same class as $M$. Furthermore, if $T$ is an isometry of $M$, the transformation
$$
\begin{equation*}
T\left(P_{0}, P_{1}, \cdots, P_{n}\right)=\left(T\left(P_{0}\right), T\left(P_{1}\right), \cdots, T\left(P_{n}\right)\right) \tag{7.1}
\end{equation*}
$$
is an isometry of $M^{n+1}$. Thus if $H$ is a group of isometries of $M$ we can also consider it as a group of isometries of $M^{n+1}$. If $H$ is a closed group of isometries of $M$, it is a closed group of isometries of $M^{n+1}$. This follows from the fact that any limit of isometries of type (7.1) is again of this type.

Let us choose $P_{0}, P_{1}, \ldots, P_{n}$ in a $\sigma$-neighborhood of $P_{0}$ in $M$ so that the only isometry of $M$ leaving them fixed is the identity. Then if $H$ is a set of isometries of $M$, and $\gamma$ is the set of points of $M^{n+1}$ into which $\bar{P}=\left(P_{0}, P_{1}, \cdots, P_{n}\right)$ is mapped by $H$, the transformation sending $T \in H$ into $T(\bar{P}) \in \gamma$ is a $1-1$ mapping of $H$ onto all of $\gamma$. This mapping is bicontinuous. For clearly $T_{k} \rightarrow T$ implies $T_{k}(\bar{P}) \rightarrow T(\bar{P})$, since $T_{k}\left(P_{i}\right) \rightarrow T\left(P_{i}\right)$. Conversely if $T_{k}(\bar{P}) \rightarrow T(\bar{P})$, from any subsequence of $\left\{T_{k}\right\}$ we can choose a new subsequence $\left\{T_{k}^{\prime}\right\}$ converging to a limit $T_{0}$; and as $T_{0}(\bar{P})=T(\bar{P})$ we must have $T_{0}=T$. This implies that $T_{k} \rightarrow T$. Thus we have proved

Lemma 6. The transformation sending $T \in H$ into $T(\bar{P})$ in the product manifold $M^{n+1}$, where $\bar{P}=\left(P_{0}, P_{1}, \cdots, P_{n}\right)$ is a set of points of $M$ as in Theorem 3,
is a $1-1$ bicontinuous transformation of the set $H$ of isometries of $M$ onto the set of points into which $\bar{P}$ is mapped by $H$.

As an immediate consequence we have
Theorem 7. If $H$ is a closed group of isometries of $H$, it is in 1-1 bicontinuous correspondence with a manifold of class $C^{1}$ imbedded in $M^{n+1}$. Hence $H$ is locally euclidean.

\section*{8. Lie groups of isometries}

Our object in this section is to show that the parameters introduced in $H$ in §7 make of $H$ a Lie group of transformations of $M$. We shall need the following results.

Suppose, under the isometry $T_{0}$, the point $P$ is transformed into $T_{0}(P)=Q$. Let $U$ be a $\sigma$-neighborhood of $Q$ with coördinates $(y)$. Choose a $\sigma$-neighborhood $V$ of $P$ with coördinates $(x)$ such that $T_{0}(\bar{V}) \subset U$. Then, if $T$ is in a neighborhood $W$ of $T_{0}$, this transformation is given by functions
$$
\begin{equation*}
y^{i}=f^{i}\left(x^{1}, \cdots, x^{n} ; T\right)=f^{i}(x ; T) \tag{8.1}
\end{equation*}
$$
which are continuous in $(x ; T)$ by definition of the topology in the group of isometries. We now consider the differentiability properties of these functions.

If $M$ is of class $C^{r}$ (analytic) the functions (3.1) $x^{i}=X^{i}(r, \bar{x}, u)$ defined in $V$ are of class $C^{r}$ (analytic). Locally the equations $g_{i j}(\bar{x}) u^{i} u^{j}=1$ ( $g_{i j}$ is the fundamental form in $V$ ) can be put in parametric form
$$
\begin{equation*}
u^{i}=u^{i}\left(\alpha_{1}, \cdots, \alpha_{n-1}\right) \tag{8.2}
\end{equation*}
$$
obtaining a representation of class $C^{r}$ (analytic) of (3.1)
$$
\begin{equation*}
x^{i}=X^{i}(r, \bar{x}, u(\alpha)) . \tag{8.3}
\end{equation*}
$$
As there is no pair of conjugate points in $V$, $\operatorname{det}\left(\left\|X_{r}^{i}\right\| \cdot\left\|X_{u^{i}}^{i} u_{\alpha_{p}}^{i}\right\|\right) \neq 0$. Hence we can solve (8.3) obtaining functions $r(\bar{x}, x)$ and $\alpha_{\rho}(\bar{x}, x)$ of class $C^{r}$ (analytic) for $(\bar{x})$ and $(x)$ in $V,(\bar{x}) \neq(x)$. Substituting these latter in (8.2) we obtain
$$
\begin{equation*}
u^{i}(\bar{x}, x)=u^{i}(\alpha(\bar{x}, x)) \tag{8.4}
\end{equation*}
$$
of class $C^{r}$ (analytic).
Choose a point $P_{0} \neq P$ in $V$ and let $g_{1}, \cdots, g_{n}$ be a set mutually orthogonal geodesics issuing from $P_{0}$. Choose a point $P_{k}$ on $g_{k}$ so that the part of $g_{k}$ joining $P_{0}$ to $P_{k}$ is in $V$. The cosine of the angle between the geodesics $P_{0} P$ and $P_{0} P_{k}$ is $g_{i j}\left(x_{0}\right) u^{i}\left(x_{0}, x\right) u^{j}\left(x_{0}, x_{k}\right)$ where $(x)$ are the coördinates of $P$ and $\left(x_{k}\right)$ are coördinates of $P_{k}$. These cosines we denote by $\pi_{k}(x)$; they are of class $C^{r}$ (analytic).

In the neighborhood $U$ of $Q$ let the equations (3.1) of the geodesics be written $y^{i}=Y^{i}(r, \bar{y}, v)$ again of class $C^{r}$ (analytic). Corresponding to (8.4) the direction of the geodesic from ( $\bar{y}$ ) to ( $y$ ) is given by functions $v^{i}(\bar{y}, y$ ). Set
$$
\begin{equation*}
v_{k}^{j}(T)=v^{j}\left[f\left(x_{0} ; T\right) ; f\left(x_{k} ; T\right)\right] . \tag{8.5}
\end{equation*}
$$

Denote by $\bar{g}_{i j}(y)$ the fundamental form in $U$.
Since isometries preserve angles (§4), the direction $(v)$ of the geodesic from $f\left(x_{0} ; T\right)$ to $f(x ; T)$ must satisfy
$$
\begin{equation*}
\bar{g}_{i j}\left[f\left(x_{0} ; T\right)\right] v^{i} v_{k}^{j}(T)=\pi_{k}(x) . \tag{8.6}
\end{equation*}
$$
Since $g_{1}, \cdots, g_{n}$ are mutually orthogonal, $T g_{1}, \cdots, T g_{n}$ are also. Hence $\operatorname{det}\left\{\bar{g}_{i j}\left[f\left(x_{0} ; T\right)\right] v_{k}^{j}(T)\right\} \neq 0$. We can therefore solve (8.6) for the $v^{i}$ obtaining them as linear functions of the $\pi_{k}(x)$ :
$$
\begin{equation*}
v^{i}=a^{i k}(T) \pi_{k}(x) . \tag{8.7}
\end{equation*}
$$
It is to be observed that $a^{i k}(T)$ is of class $C^{r}$ (analytic) in the functions $f\left(x_{0} ; T\right)$, $\cdots, f\left(x_{n} ; T\right)$.

Since isometries preserve distance $r\left(x_{0} ; x\right)=\bar{r}\left[f\left(x_{0} ; T\right) ; f(x ; T)\right]$ where $\bar{r}(\bar{y}, y)$ is the distance from ( $\bar{y}$ ) to ( $y$ ). Since the point $T(P)$ must bear the same relation to $T g_{1}, \cdots, T g_{n}$ as $P$ bears to $g_{1}, \cdots, g_{n}$ we obtain the following representation of the functions $f^{i}(x ; T)$ :
$$
\begin{equation*}
f^{i}(x ; T)=Y^{i}\left[r\left(x_{0} ; x\right), f\left(x_{0} ; T\right), a^{k}(T) \pi_{k}(x)\right] . \tag{8.8}
\end{equation*}
$$
Since $Y^{i}, r, \pi_{k}$ are of class $C^{r}$ (analytic) in $(x)$ we obtain
Lemma 7. The functions $f^{i}(x ; T)$ are of class $C^{r}$ (analytic) in $(x)$ and their derivatives are continuous in $(x ; T)$.

As an immediate consequence we have
Theorem 8. An isometry of a Riemannian manifold of class $C^{r}$ (analytic) is of class $C^{r}$ (analytic). ${ }^{8}$

We shall draw some further consequences of this representation. Suppose the neighborhood $W$ is given coördinates $\left(\beta^{1}, \cdots, \beta^{r}\right)=(\beta)$ so that $f^{i}(x ; T)$ can be written $f^{i}(x ; \beta)$. Suppose furthermore that the derivatives $\partial f^{i} / \partial \beta^{k}$ $(i=1, \cdots, n ; k=1, \cdots, r)$ exist at the points $P_{0}, \cdots, P_{n}$ for all $(\beta)$ in $W$. We can then differentiate (8.8) obtaining
$$
\begin{equation*}
\frac{\partial f^{i}(x ; \beta)}{\partial \beta^{k}}=\frac{\partial Y^{i}}{\partial \bar{y}^{j}} \frac{\partial f^{j}\left(x_{0} ; \beta\right)}{\partial \beta^{k}}+\frac{\partial Y^{i}}{\partial v^{j}} \pi_{l}(x) \frac{\partial a^{j l}(\beta)}{\partial \beta^{k}} . \tag{8.9}
\end{equation*}
$$
Since $a^{j l}$ is of class $C^{r}$ in $f\left(x_{0} ; \beta\right), \cdots, f\left(x_{n} ; \beta\right), \partial a^{j l} / \partial \beta^{k}$ exists. It follows that $\partial f^{i} / \partial \beta^{k}$ exists for ( $x$ ) in the open set $V$ and is of class $C^{r-1}$ in ( $x$ ) and these additional derivatives are continuous in $(x ; \beta)$.

We see therefore that the existence of $\partial f^{i} / \partial \beta^{k}$ at $P_{0}, \cdots, P_{n}$ implies its existence in an open set of $M$. Let us show that this extends to all of $M$. Suppose we have proved the differentiability with respect to the $\beta$ 's of the functions representing the transformation ( $\beta$ ) at all points $P$ in an open set $A \subset M$. Suppose $A$ has a boundary point $P$. As above, let $Q=T_{0}(P), U$ a neighborhood of $Q, V$ a neighborhood of $P$ so that $T(\bar{V}) \subset U$ for $T \in W$. We then choose

\footnotetext{
${ }^{8}$ The first proof of this for the analytic case was given us by Professor Marston Morse. Our proof has much in common with his.
}
the points $P_{0}, P_{1}, \cdots, P_{n}$ in the intersection $A \cdot V$ and reason as before that $f^{i}(x ; \beta)$ is differentiable in $(\beta)$ for $(x)$ in an open set about $P$. There is a largest open set of $M$ in which the transformation ( $\beta$ ) is differentiable in ( $\beta$ ) (i.e. the sum of all open sets in which this holds). This set is non-vacuous and we have just seen that it has no boundary point. It is therefore the whole of $M$. Thus we have

Lemma 8. If the functions determining the transformation $T \in W$ of $M$ are differentiable in ( $\beta$ ) at a set of points $P_{0}, P_{1}, \ldots, P_{n}$ as in Theorem 3, then they are differentiable in ( $\beta$ ) at every point of $M$. Furthermore these derivatives are of class $C^{r-1}$ (analytic) in ( $x$ ) and these $x$-derivatives are continuous in $(x ; \beta)$.

We are now prepared to prove
Theorem 9. The parameters introduced into $H$ in §7 make of $H$ a Lie group.
Suppose $A_{0}, B_{0}$ are isometries in $H$ and $C_{0}=B_{0} A_{0}$. Let $\left(\alpha^{1}, \cdots, \alpha^{r}\right)=(\alpha)$, $(\beta),(\gamma)$ be coördinates for neighborhoods of $A_{0}, B_{0}, C_{0}$ respectively as provided in §7. Then for $A, B$ near to $A_{0}, B_{0}$ the coördinates of $C=B A$ are given by functions $\gamma^{i}=\phi^{i}(\alpha ; \beta)$ which we must prove to be of class $C^{1}$.

Under the imbedding of $H$ in $M^{n+1}$, the isometry $A_{0}$ corresponds to the point $A_{0}(\bar{P})$. Let $(x)=\left(x^{1}, \cdots, x^{m}\right)(m=n(n+1))$ be coördinates for a neighborhood of $A_{0}(\bar{P})$; and let ( $y$ ) be coördinates for a neighborhood of $C_{0}(\bar{P})$. Then the isometry $B$ (near $B_{0}$ ) acting on $M^{n+1}$ is given near $A_{0}(\bar{P})$ by functions $y^{i}=$ $F^{i}(x ; \beta)$. The functions $x^{i}=x^{i}(\alpha)$ defining the imbedding of the neighborhood ( $\alpha$ ) in $M^{n+1}$ are of class $C^{1}$ with functional matrix of rank $r$. Similarly for the functions $y^{i}=y^{i}(\gamma)$ defining the imbedding of ( $\gamma$ ) in $M^{n+1}$. Accordingly we can solve these latter for the $\gamma^{\prime}$ 's in terms of $r$ of the $y^{\prime} \mathrm{s}: \gamma^{i}=\gamma^{i}\left(y^{j_{1}}, \cdots, y^{j_{r}}\right)$. We obtain in this way a representation of $\phi^{i}(\alpha ; \beta)$ :
$$
\begin{equation*}
\phi^{i}(\alpha ; \beta)=\gamma^{i}\left(F^{j_{1}}(x(\alpha) ; \beta), \cdots, F^{j_{r}}(x(\alpha) ; \beta)\right) . \tag{8.10}
\end{equation*}
$$
By Lemma $7, \partial F^{j} / \partial x^{k}$ exists and is continuous in $(x ; \beta)$. Since $\gamma^{i}$ and $x^{i}(\alpha)$ are of class $C^{1}$, it follows that $\partial \phi^{i} / \partial \alpha^{k}$ exists and is continuous in $(\alpha ; \beta)$.

For the moment, let $A_{0}$ be the identity. Then the functions $F^{j}(\bar{P} ; \beta)$ define the imbedding of the neighborhood $(\beta)$ of $B_{0}$ in $M^{n+1}$. We know that these are of class $C^{1}$. Hence $\partial F^{j} / \partial \beta^{k}$ exists at the point $\bar{P}$. This means that at the points $P_{0}, \cdots, P_{n}$ of $M$ the transformation ( $\beta$ ) of $M$ is differentiable in ( $\beta$ ). By Lemma 8, this holds at every point of $M$. It follows that $\partial F^{j} / \partial \beta^{k}$ exists at every point of $M^{n+1}$ and is continuous in $(x ; \beta)$. It then follows from (8.10) that $\partial \phi^{i} / \partial \beta^{k}$ exists and is continuous in $(\alpha ; \beta)$. This proves Theorem 9.

We have just seen that the functions $f^{i}(x ; \beta)$ defining the transformation $B$ of $M$ have $\beta$-derivatives for all points ( $x$ ) in $M$. By Lemma 8, if $M$ is at least of class $C^{2}, \partial f^{i} / \partial \beta^{k}$ has $x$-derivatives continuous in $(x ; \beta)$. This concludes the proof of our principal result.

Theorem 10. Any closed group of isometries of a Riemannian manifold of class $C^{r}(r \geqq 2)$ is a Lie group of isometries.
9. Remarks. We have seen that the parameters we have introduced in $H$ make it a Lie group of class $C^{1}$. If the class of $M$ is >2, the question arises if
$H$ is of a higher class. This reduces to the same question about a manifold of equivalent points. We have not settled this point.

The classical theory of motions concerns itself with Lie group germs of isometries in the neighborhood of a point of a Riemannian manifold. This suggests the question: Is any locally compact group germ of local isometries a Lie group germ? We hope to consider this in a later paper.

University of Michigan, Princeton University.
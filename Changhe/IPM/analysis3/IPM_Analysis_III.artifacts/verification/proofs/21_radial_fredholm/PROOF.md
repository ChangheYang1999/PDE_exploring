# A conditional radial-weight Fredholm theorem for the full fixed-normalization coupling

Status: proved under the exact margin hypothesis below. No numerical margin
is asserted. This independently audits G1 to G3 and Theorem R of the theory author's
snapshot in `../20_frozen_origin_global/evidence/lead_snapshot.md`.

## Statement

Let ell>0. Let V:R2->R2 be C1, globally Lipschitz, V(0)=0, and
div V=2ell. Assume the usual IPM parity: V1 odd in x and even in y, V2 even
in x and odd in y. Let a,c be bounded continuous real functions, tending
to0 both as X->0 and |X|->infinity. Require a odd in both coordinates and
c even in both. In the application a=rho_x,c=rho_y.

Let mu be a smooth real function on R with M=sup|mu'|<2, and put
w(X)=exp(mu(log|X|)). Let X_w be complex L2(w dX) restricted to functions
even in x and odd in y; the real subspace has the same conclusion. Define
Sij by the Fourier multiplier xi_i xi_j/|xi|^2, and set

 T=a S12-c S11,
 Lfix=V.grad-1+T,
 D_w={h in X_w:V.grad h in X_w in distributions away from0}.

The derivative's distributional realization on all of R2 agrees with this
one after closure of the core described below. Give D_w its graph norm.
Put b0=1+ell,
 b_+=(sqrt(a^2+c^2)-c)/2,
 q=V.X/|X|^2,
 kappa_w=b0+mu'(log|X|)q/2.

Assume the exact global hypothesis

 m_* = inf_{X !=0}(kappa_w(X)-b_+(X)) >0.

Then Lfix:D_w->X_w is closed and Fredholm of index0. There is a compact
operator K:X_w->X_w such that

 m_*||h||_w <= ||Lfix h||_w+||K h||_w  for all h in D_w.

Consequently Lfix is bijective if and only if its kernel is zero. This
statement supplies no numerical norm of its inverse and does not concern
the additional, generally unbounded, strain functional or a nonlinear map.

## Weighted boundedness without a weighted singular-integral theorem

Let J be multiplication by sqrt(w), unitary from X_w to unweighted L2.
Off its diagonal, Sij has a kernel Kij with
|Kij(Z)|<=C|Z|^{-2}; its possible constant multiple of the identity cancels
in every commutator. The extra kernel of J Sij J^{-1}-Sij is

 Cij(X,Y)=Kij(X-Y)(sqrt(w(X)/w(Y))-1).

Since |mu'|<=M,
sqrt(w(X)/w(Y)) <= max((r/s)^{M/2},(s/r)^{M/2}), r=|X|,s=|Y|.
We apply the elementary Schur test with positive auxiliary function h(X)=1/r.
For s<r/2, integration of |Cij(X,Y)|h(Y)/h(X) is bounded by a constant
times
 r^{M/2-1} integral_0^{r/2} s^{-M/2} ds,
which is finite uniformly in r because M<2. For s>2r the corresponding
bound is
 r^{1-M/2} integral_{2r}^infinity s^{M/2-2} ds,
also uniformly finite. The transposed Schur integrals have the same bounds,
since the majorant uses the symmetric maximum of the radius ratios.

On comparable radii, split |X-Y|<min(r,s)/2 from its complement. In the
first part the mean value theorem bounds the weight ratio minus1 by
C_M |X-Y|/min(r,s). Thus the kernel is bounded by
C_M/(r|X-Y|) when Y is integrated at fixed X, and by the analogous formula
when X is integrated at fixed Y. The near-diagonal integral is uniformly
bounded. On the comparable-radius complement, |X-Y| is bounded below by
a fixed multiple of r and the region has area O(r^2), so its Schur
integrals are bounded too. This proves boundedness of Cij, hence of Sij
on L2(w), directly from unweighted Fourier boundedness.

The weight is also A2, although this fact is not needed for this proof.
For centered balls, w(r)/w(R)<=max((r/R)^M,(R/r)^M) gives
average_{B_R}w <=2w(R)/(2-M), and the same for w^{-1}.
Their product is at most4/(2-M)^2. A ball of radius less than half its
distance from0 has bounded weight oscillation. Every other ball is contained
in a centered ball whose radius is at most three times its own, which gives
a uniform A2 constant by the centered estimate and the area ratio.

## Compact conjugation after multiplication by a vanishing coefficient

If m is continuous and vanishes at0 and infinity, then m Cij is compact
on L2. First truncate m to an annulus. The operator-norm error tends to0
by the boundedness just proved. For X in that fixed annulus and Y close
to0, the squared kernel is bounded by C(1+s^{-M}), integrable in two
dimensions since M<2. For |Y| large it is bounded by
C(s^{-4}+s^{M-4}), also integrable since M<2. These two kernel portions
are Hilbert-Schmidt. On the remaining bounded annulus the weight is smooth
with bounded derivative, so the kernel is O(|X-Y|^{-1}). Its part with
|X-Y|<eta has Schur norm O(eta); the rest is Hilbert-Schmidt. Taking eta
to0 proves compactness. No behavior of the weight derivatives at0 is
used here beyond the global logarithmic Lipschitz bound.

It follows that J T J^{-1}=T+K_w with K_w compact on unweighted L2.

## The exact principal-symbol bound modulo a compact operator

Let Rj be the bounded self-adjoint multiplier xi_j/|xi| on complex L2,
so Sij=RiRj and R1^2+R2^2=I. For every continuous function m vanishing
at infinity, [m,Rj] is compact. Here is a direct proof sufficient for
this statement. Approximate m uniformly by compact smooth functions;
the commutator changes in norm by at most2||m-m_n||_infinity. For compact
smooth m_n its kernel has the factor m_n(X)-m_n(Y). On a bounded set
this makes its near-diagonal singularity O(|X-Y|^{-1}), whose truncated
Schur norm tends to0. Outside a large bounded set, at least one variable
is in supp(m_n) and the kernel's square is integrable, with norm tending
to0 as the truncation radius grows. The remaining truncated kernel is
Hilbert-Schmidt. Thus each commutator, and its uniform limit, is compact.

Introduce the real symmetric matrix

 H(X)=[[-c(X),a(X)/2],[a(X)/2,0]].

Its largest eigenvalue is exactly b_+(X), which is continuous and vanishes
at infinity. Moving each multiplier coefficient past an Rj changes the
operator only by a compact term, so

 Re<Tg,g> <= integral b_+(X)(|R1g|^2+|R2g|^2)dX+Re<K1g,g>.

Moving b_+ back past the Rj and using their square sum gives

 Re<Tg,g> <= integral b_+|g|^2+Re<K2g,g>,

with K2 compact. This proof does not assume that b_+ or a matrix square
root built from it is smooth at zeros of (a,c). Combining it with the
weighted conjugation result supplies the corresponding bound in X_w.
Projection onto the parity subspace preserves the quadratic forms and
compactness. An arbitrary epsilon loss is unnecessary, though harmless.

## Transport core and adjoint domain

The bound |V(X)|<=C|X| implies |V.grad log w|<=CM. Therefore both the
weighted divergence div V+V.grad log w and the transport energy coefficient
are bounded. Cut off a maximal-domain function first near0 and then near
infinity using radial cutoffs. Their V derivatives are uniformly bounded
and supported on regions escaping every compact annulus; the resulting
errors tend to0 in X_w by absolute continuity of the integral.
On a fixed annulus the weight is smooth, bounded above and below. Ordinary
mollification approximates the function and its transport derivative:
the commutator of a C1 Lipschitz vector field with mollification is
uniformly bounded on L2 and converges to0 there. To verify the latter,
write its kernel as

 grad eta_epsilon(X-Y).(V(X)-V(Y))
                  + eta_epsilon(X-Y)div V(Y).

The constant part of the first-order Taylor expansion cancels the second
term; the remainder tends to0 on smooth inputs, and the uniform Lipschitz
bound extends convergence to L2 by density. Thus compact smooth functions
away from0, projected to parity, form a core. This proves closedness of
the maximal transport realization.

Integration by parts on this core gives the adjoint

 (V.grad)^*=-V.grad-div V-V.grad log w.

The added multiplier is bounded. The same cutoff and mollifier argument
for the distributional adjoint proves that its maximal domain is exactly
D_w. Adding the bounded operator T does not change either adjoint domain.
The distinction between distributions on the punctured plane and closure
on the full plane creates no extra state here. Since M<2, w^{-1} is locally
integrable, so convergence in X_w implies convergence in L1 on compact
sets. The cutoff and mollifier approximants and their transport derivatives
therefore converge in distributions on the whole plane. Their limiting
identity is precisely the full distributional derivative identity; no
point-supported derivative term is left at0.

## Fredholm estimate, cokernel and index

On the core, integration by parts yields

 Re<(V.grad-1)h,h>_w=-integral kappa_w |h|^2w.

Combine this with the principal-symbol bound and pass to D_w by core
approximation. Then
 Re<Lfix h,h>_w <=-m_*||h||_w^2+Re<K h,h>_w,
which implies the stated estimate by Cauchy-Schwarz. Since K is compact,
this estimate gives a finite-dimensional kernel and closed range. More
explicitly, a normalized sequence in the kernel has a convergent K-image
and is therefore Cauchy by the estimate. On the orthogonal complement of
the kernel, failure of a bound ||h||<=C||Lfix h|| would give a normalized
sequence with Lfix h->0; compactness and the estimate give a convergent
subsequence in the kernel, a contradiction. Closedness then proves closed
range.

The adjoint has the same domain, and its quadratic real part agrees with
that of Lfix. The same compact estimate therefore gives a finite-dimensional
adjoint kernel, which is the cokernel. Thus Lfix is Fredholm.
For 0<=s<=1 let L_s=V.grad-1+sT. Its margin is at least m_* because
b_+>=0. The preceding argument applies to every s; the domains and graph
norms are fixed because T is bounded. Hence this is a norm-continuous path
of Fredholm maps D_w->X_w. At s=0 the transport estimate and its adjoint
have no compact error and are bounded below by m_*. Their ranges are
closed, and the adjoint kernel is zero, so L_0 is bijective. Its index is0,
and index constancy gives index0 for Lfix. The index constancy used here
follows by splitting the domain by a finite-dimensional kernel and the
target by a finite-dimensional cokernel at each fixed parameter: the
remaining block is invertible, remains so under a small operator-norm
perturbation, and a finite-dimensional Schur complement has index equal
to the fixed difference of those two finite dimensions. Compactness of
the parameter interval joins these local conclusions.

## Scope of application to the modal trial

The exact modal trial's regularity, parity and sublinear tails give the
regularity and vanishing coefficient hypotheses above. They do not supply
the global positive margin: a sampled grid does not establish its infimum.
Nor does this theorem bound the strain functional, make the center jet
continuous, prove injectivity, or estimate the nonlinear transport term.
Any reported global inverse must establish those additional properties in
its actual domain rather than transfer this conditional theorem to the
jet-plus-remainder space without a new argument.

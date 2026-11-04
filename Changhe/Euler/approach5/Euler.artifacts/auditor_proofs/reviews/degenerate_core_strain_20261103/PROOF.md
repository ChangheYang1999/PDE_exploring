# Strain, zero spectra and the degenerate carrier core

Status: independent reconstruction of C32 and the two reduced models in the team records, checked against the focused configured-model review. Final verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md). All consequences involving a strain bound retain that additional hypothesis. No upper bound is inferred from decay alone.

## 1. Setting and compact core

Let 0<c<1/2 and omega be real. Let U in C2(R3;R3), P in C1 solve

    (1-c)U+(B.grad)U+omega JU+grad P=0, div U=0,
    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, kappa=1+c, d=3c.

Assume U=o(|y|) uniformly. The equation upgrades P to C2. The carrier is complete in both directions and points strictly outward outside a sufficiently large ball Q. Its backward flow Psi has a compact full invariant core

    K=intersection_(t>=0) Psi_t(Q),
    Z=K intersect ({B=0} union {W=0}).

K consists of precisely the points whose forward B-orbits are bounded. To justify the useful last assertion, an orbit outside a sufficiently large ball has radial derivative at least c|y|/2 and escapes; hence every bounded forward orbit stays inside the chosen ball. Conversely membership in the nested intersection means that every forward iterate remains in Q. Every backward orbit enters Q in finite time by the same radial inequality. The determinant det D Psi_t=exp(-dt) makes K Lebesgue-null. Each vortical component E has K_E=K intersect closure(E) and Z_E=K_E intersect Z, as in A430.

The exact curl identity is

    [B,W]=-kappa W,
    D Phi_s W=exp(kappa s) W composed with Phi_s,             (1)

where Phi is the forward carrier flow. No pressure normalization or decay of DU is imposed.

## 2. Strain control and its strictly conditional coverage consequence

Write S=(DU+DU^T)/2. For every finite backward orbit segment and every vector v0,

    |D Psi_t(x)v0|
      <=|v0| exp(integral_0^t [-c-lambda_min(S(Psi_s x))] ds). (2)

Indeed v'=(-cI+omega J-DU)v and every skew part disappears from v.v'. Thus

    (log|v|)'=-c-v.Sv/|v|^2<=-c-lambda_min(S).

Integrating and taking the supremum over unit initial vectors proves (2). For an ergodic invariant probability mu on K, Birkhoff and Oseledets give

    lambda_top(mu)<=-c+integral[-lambda_min(S)] dmu.           (3)

The integrand is continuous and bounded on K. This proof covers full-flow-ergodic measures without assuming time-one ergodicity, using continuous-time Birkhoff averages. In particular the maximal exponent Gamma_Z over the degenerate measures is at most max_Z(-c-lambda_min(S)); the same holds on each compact Z_E.

For U in C^r, integer r>=2, the pointwise extra condition

    lambda_min(S(y))>-(c+r a) for every y in Z               (4)

has a uniform strict margin by compactness. It implies Gamma_Z<r a. The A399 formula Lambda_core=max(a,Gamma_Z) and A417 then give the stated full vortical coverage when W is not identically zero. When W is identically zero, vortical coverage is empty. Applying (4) separately on every compact Z_E yields Gamma_E<r a for every E and the componentwise A431 coverage; no uniform margin across components is needed. At r=2 the threshold is -(2-3c). This is a sufficient strain condition, not a consequence of decay and not a necessary coverage criterion.

If a degenerate ergodic measure has top exponent at least 2a, (3) requires mean compressive strain

    integral[-lambda_min(S)] dmu >= c+2a=2-3c.               (5)

When Gamma_Z or Gamma_E is at least 2a, an attaining measure exists by the previously proved compact projective variational argument; (5) applies to such a measure. It is not an inequality for every invariant probability merely because the maximum is large.

## 3. Vortical carrier zeros and sharp strain bounds

At p with B(p)=0 and w=W(p)!=0, put D=DB(p), e=w/|w| and let T be the orthogonal compression of S(p) to e-perpendicular. Equation (1) gives D w=kappa w. The skew part of DU is one half cross product with w, so it kills w. Therefore

    S w=w+omega Jw, e.S e=1, trace T=-1.

Write the two real eigenvalues of T as -1/2 plus or minus delta, delta>=0. The line Rw is D-invariant. The map induced by -D on R3/Rw is represented on e-perpendicular by the orthogonal compression -Pi D restricted to that plane; the plane itself need not be invariant. This quotient has trace a and symmetric part -(cI+T). Its eigenvalues mu1,mu2 consequently satisfy

    mu1+mu2=a, Re mu_i<=a/2+delta.

For a complex eigenvector the real part of its eigenvalue is its Hermitian Rayleigh quotient for the symmetric part, giving the same estimate. The remaining eigenvalue of -D is -kappa. Hence

    a/2<=lambda_top(delta_p)<=a/2+delta.                    (6)

In particular lambda_top>=2a requires delta>=3a/2.

There is also an exact formula. Orient e-perpendicular by the unit vector e, and let J_e v=e cross v on that plane. Orthogonal compression of the cross-product matrix of any vector z has coefficient z.e relative to J_e: its normal part vanishes after projection and its tangential part rotates only into the discarded normal direction. Thus the skew part of the backward quotient is b J_e, where

    b=omega(e.e3)-|w|/2.

Its symmetric traceless part has eigenvalues plus or minus delta. In an oriented orthonormal basis the quotient is a/2 times identity plus

    [[t1,t2-b],[t2+b,-t1]], t1^2+t2^2=delta^2.

The square of this traceless matrix is (delta^2-b^2) times identity. Therefore

    lambda_top(delta_p)=a/2+sqrt(max(delta^2-b^2,0)).         (6a)

The third backward eigenvalue -kappa cannot be maximal. In particular lambda_top>=2a is equivalent to delta^2-b^2>=9a^2/4. For delta>0 the upper bound in(6) is attained exactly when b=0. When omega=0, b=-|w|/2 is nonzero, so the upper bound is strict at every such vortical zero with delta>0. The affine family below shows that it is still the sharp supremum. These are exact local formulas; they give no upper bound on delta from global decay.

Sharpness has an omega qualification. Consider the entire affine exact solutions

    U=N y, N=[[s,-q,0],[q,-1-s,0],[0,0,1]], q!=0,
    P=[q^2-s(s+1)](y1^2+y2^2)/2
        -omega(2s+1)y1 y2-y3^2.                            (7)

Here div U=0, W=2q e3 and B(0)=0. Direct multiplication gives the momentum matrix N+N^2+omega(JN-NJ), whose negative quadratic potential is exactly (7). Thus these are full Euler examples, with linear growth. The quotient of -DB is

    [[-c-s,q-omega],[omega-q,1+s-c]].

For omega!=0 choose q=omega. Its top eigenvalue is a/2+|s+1/2|, attaining (6) at any delta=|s+1/2|. For omega=0 that choice would give W=0 and is not a vortical example. With nonzero q tending to zero the upper bound is approached at every delta>0; at delta=0 it is attained for any q!=0, because the quotient eigenvalues have real part a/2. No uniform improvement of (6) follows. These affine fields are not uniformly sublinear and are not counterexamples to the global target.

## 4. Index and the fast direction inside the core

For large R the homotopy Ay+sU(y), 0<=s<=1, never vanishes on |y|=R, since |Ay|>=c|y| and U is uniformly sublinear. Thus B has boundary degree sign det A=+1. If all its zeros are isolated, compactness makes their set finite and their indices sum to +1. The finiteness condition is essential: an infinite compact closed set of isolated zeros would have a zero accumulation point, contradicting isolation at that point.

At a vortical zero with L=lambda_top(delta_p)>a, the quotient eigenvalues are real L and a-L<0; a complex pair would have real part only a/2. The forward spectrum and determinant are therefore

    kappa, L-a, -L;  det DB(p)=kappa L(a-L)<0.               (8)

The zero is hyperbolic and has index -1. Conversely a nondegenerate vortical zero of index +1 has L<a: a real quotient pair with positive product and positive sum lies in (0,a), while a complex pair has real part a/2. This converse does not cover degenerate isolated zeros. More generally, (6a) gives

    det DB(p)=kappa(a^2/4+b^2-delta^2).

Thus degeneracy is exactly delta^2-b^2=a^2/4, and then L=a. A nondegenerate vortical zero has index -1 exactly when L>a and index +1 exactly when L<a. The index sum supplies no bound on the magnitude of L.

Every forward-stable point of any carrier zero lies in K by the bounded-orbit definition. For a zero satisfying (8), the C1 stable-manifold theorem gives a one-dimensional forward stable manifold, tangent to the eigenline of -DB with eigenvalue L. All of it lies in K. Thus this fast backward direction is realized by a curve in the core and cannot be discarded by choosing a smaller trapping ball. This is a stable-manifold statement, not a claim that arbitrary large L occurs in a decaying profile.

## 5. The complete vortex line through a vortical zero

Let gamma'=W(gamma), gamma(0)=p, where B(p)=0 and W(p)!=0. A048 gives completeness of the frozen-vorticity flow under the present global hypotheses. Its proof uses (1) and backward carrier confinement, not a bound on DW at infinity. Uniqueness and (1) give

    Phi_s(gamma(tau))=gamma(exp(kappa s)tau),
    B(gamma(tau))=kappa tau W(gamma(tau)).                  (9)

The vector W never vanishes on this orbit. If it returned to p at nonzero tau, the second formula would give 0=kappa tau W(p), impossible. The same formula shows that p is its only carrier zero. Also Psi_t gamma(tau) tends to p as t tends to infinity.

For tau0>0, the positive branch tau>=tau0 is exactly the forward carrier orbit of gamma(tau0), after the parameter change tau=tau0 exp(kappa s). The negative branch is identical with absolute values of tau. If the branch is bounded, it lies in K, and (9) gives |W(gamma(tau))|<=C/|tau|. Its limit set is nonempty, compact, connected and invariant under the full carrier flow; continuity puts it in {W=0} intersect K. These are the usual elementary limit-set properties of a bounded continuous full orbit.

If the branch is unbounded, the outward radial estimate forces |gamma(tau)| to tend to infinity. The precise power comparison needs the additional condition that U be bounded, as is true under decay. With that condition, r(s)=|Phi_s x| satisfies

    (log r)'=c+O(1/r).

After entering a large exterior region r grows at least exp(cs/2), so the error is integrable. Hence r is comparable to exp(cs). Since c r-|U|<=|B|<=sqrt(c^2+omega^2)r+|U|, |B| is comparable to r. Using (9),

    |gamma(tau)| is comparable to |tau|^(c/kappa),
    |W(gamma(tau))| is comparable to |gamma(tau)|^(-1/c).   (10)

The constants depend on the branch and the profile. Uniform sublinearity alone is sufficient for escape but has not been used to assert these exact comparability constants.

## 6. Nonflat irrotational equilibria

At p with B(p)=W(p)=0, put D=DB(p), N=DW(p). C2 velocity is enough for the following first-order expansion: B(p+h)=Dh+o(|h|), W(p+h)=Nh+o(|h|), while DB and DW are continuous. Substituting in (1) yields

    N D-D N=-kappa N, or D N-N D=kappa N.                   (11)

Thus N maps every generalized eigenspace E_mu(D) into E_(mu+kappa)(D), since

    [D-(mu+kappa)I]^m N=N(D-mu I)^m.

If N!=0, some eigenvalue and that eigenvalue plus kappa both occur. That resonant pair must be real. Otherwise its two nonreal members and both conjugates would give four distinct eigenvalues of a real 3 by3 matrix. The third eigenvalue is real by the trace. Hence for some real lambda,

    spec D={lambda,lambda+kappa,-a-2lambda}.

N is nilpotent, because successive nonzero applications would keep shifting a finite real spectrum upward by kappa. The top backward exponent is

    max(-lambda,a+2lambda)>=a/3.                            (12)

There is no upper bound in this necessary algebraic condition. Jordan blocks do not change the exponential rates. When (11) has no resonant pair its only solution is N=0. Conversely a resonance alone does not assert existence of an Euler jet or a global profile; N is the actual derivative of curl U, not an arbitrary matrix introduced independently.

For omega=0 a separate scalar excludes nonstationary invariant probabilities without any nonflatness premise. Put

    Ht=P+|U|^2/2+(Ay).U, F=c|y|^2/2-Ht/a.

The Lamb identity gives grad F=B+omega Jy-(B cross W)/a, and therefore, everywhere,

    BF=|B|^2+omega B.Jy.                                   (13)

An invariant compactly supported probability has integral BF=0. At omega=0 it must be carried by {B=0}. In the decaying class the already proved nonrotating Liouville theorem gives U=0. At nonzero omega (13) has no sign. It is not an additional exponent bound.

## 7. An irrotational neighborhood of the whole core

If W=0 on an open neighborhood O of K, then W=0 everywhere. Indeed the nested compact sets Psi_t(Q) eventually lie in O: otherwise choose times tending to infinity and points outside O, take a compact subsequential limit, and use nesting to put that limit in K outside O. Every x first enters Q under Psi and subsequently enters O. Equation (1) and invertibility of D Psi show W(x)=0.

Since div U=0 and curl U=0, each velocity component is harmonic. Under decay, Liouville gives U=0. Under uniform sublinearity alone it gives a constant velocity: the interior gradient estimate on arbitrarily large balls bounds |DU(p)| by a constant times R^-1 sup_(B_R(p))|U|, whose limit is zero. Constants solve the profile equation with the linear pressure

    P(y)=-[((1-c)I+omega J)u].y.

Thus a nonzero decaying profile has K intersect closure{W!=0} nonempty. In fact, for a full global Euler profile, every nonempty vortical component E has nonempty K_E by A430: a backward orbit starting in E stays in E, enters Q and has a nonempty limit set in K intersect closure(E). The weaker intersection statement alone would not imply this componentwise conclusion without the transport and invariance hypotheses. Neither statement says that W is nonzero at some point of K: all of K may in principle lie on the boundary of the vortical set.

## 8. A compactly supported field exact near its entire core

This reduced construction is not a full Euler solution. Fix 2/5<c<1/2 and

    |omega|<sqrt((5c-2)(2-c)).

Choose N>=1 and 0<epsilon<1 so that s=(1-epsilon)N/(N+1) satisfies

    4c^2 s^2>omega^2+(c+2a)^2.                              (14)

Such a choice exists because s can approach1 and
4c^2-(c+2a)^2=(5c-2)(2-c). With zeta=y1+i y2 define real harmonic polynomials phi,psi by

    phi+i psi=c(1-epsilon) sum_(j=1)^N
                  [1-j/(N+1)] zeta^(2j)/j.

At cylindrical radius r=1,

    c+phi_r=c[epsilon+(1-epsilon)F_N(2theta)]>=c epsilon,
    F_N(theta)=|sum_(j=0)^N exp(i j theta)|^2/(N+1)>=0.      (15)

The equality follows by multiplying the finite sum with its conjugate and counting terms of each difference j-l. Continuity gives the same strict radial sign on a thin closed outer annulus 1<=r<=1+2h.

Choose smooth cutoffs with 0<=chi,eta<=1, chi=1 for r<=1+h and0 for r>=1+2h, eta=1 for |y3|<=1 and0 for |y3|>=2. Set

    U=curl(0,0,eta(y3)chi(r)psi(y1,y2)).

It is smooth, compactly supported and divergence-free. Its third component is zero, and its radial component is eta chi phi_r; differentiating chi contributes only to the angular component. Consequently B3=c y3, and for r>=1

    B_r=(1-eta chi)c r+eta chi(cr+phi_r)>0

where chi may be nonzero; where chi=0 the assertion is B_r=cr. Every bounded forward orbit therefore has y3=0 and r<1. The compact core lies in the region where U=grad phi. The full Euler equation holds on an open neighborhood of that core with

    P=-a phi-(Ay).grad phi-|grad phi|^2/2.                  (16)

The gradient of the middle term includes A^T grad phi, which supplies the rotation term. At zero,

    DB(0)=A+diag(2cs,-2cs,0),
    lambda_top(delta_0)=-c+sqrt(4c^2s^2-omega^2)>2a.

The zero belongs to the core. For c=9/20,omega=1/10,N=5,epsilon=1/10, this rate is (sqrt713-18)/40>1/5. This exact example shows that incompressibility, decay and validity of Euler on a neighborhood of the entire core, taken together, do not imply Gamma_Z<2a. It gives no countertest for the componentwise condition: W vanishes on an open neighborhood of K, so K_E is empty for every vortical component of this field. The global component-invariance argument in Section7 is unavailable because this field fails Euler outside that neighborhood.

The equation must fail elsewhere. Extend the pressure in (16) smoothly to the whole space, and let R be the full momentum residual. Compact support of U and divergence-free integration by parts give

    integral U.R=(1-5c/2) integral |U|^2<0.                 (17)

The pressure and rotation contributions integrate to zero. Thus the residual cannot vanish identically. Section7 supplies a second obstruction: the field has an irrotational neighborhood of its core but is nonzero. Neither argument supplies an exact decaying Euler counterexample.

## 9. Exact singular exterior equilibria for every rotation rate

For rho=|y|>0 put

    H2=(3y3^2-rho^2)/(2rho^5),
    H4=(35y3^4-30y3^2rho^2+3rho^4)/(8rho^9),
    phi=q H2+h H4,
    q=(L+7c)/6, h=-(L+5c)/10, L>0.

Both multipoles are harmonic away from zero; for example they are the second and fourth axial derivatives of 1/rho divided by 2! and4!, respectively. Thus U=grad phi with pressure (16) is exact full rotating Euler on the punctured space for every omega, is irrotational, and satisfies U=O(rho^-4) at infinity. Its flux through any sphere is zero, since both angular Legendre polynomials have zero spherical mean, or by direct angular integration of their radial derivatives.

At p=e3, axial differentiation gives U(p)=-c e3 and Hess phi(p)=diag((L+c)/2,(L+c)/2,-L-c). Therefore B(p)=0 and

    det(z I-DB(p))
      =(z+L)[(z-(3c+L)/2)^2+omega^2].                     (18)

The zero is nondegenerate of index -1 and its top backward exponent is exactly L. The singularity at zero prevents an entire profile. Any punctured-domain integration retains the inner boundary term; zero total velocity flux is not a replacement for regularity there. These local/exterior examples realize arbitrary growth without answering the entire decaying-profile question.

## 10. Verification and limits

The statements above were reconstructed by hand before any computation. The source checker has been read in full. Its forty random first-jet tests include floating-point eigenvalues and are only diagnostic illustrations; the universal strain estimate is (2)-(6). The exact model identities and countercontrols can be reproduced separately. The reproduction ran from 2026-11-03T03:25:10.695523Z to 03:25:14.199953Z on one permitted CPU worker; all 22 check groups passed. Its exact identities and negative controls support the algebra only, and its finite floating-point samples prove no universal claim. Actual times, script hash and output are in the team records and in the team records.

Dependencies already audited: A006/A048 carrier and vortex completeness; A014 vortex-period obstruction; A095/A415 affine Euler examples; A399/A417 compact growth and coverage; A430-A432 componentwise localization. The only additional standard theorem in Section4 is the C1 stable-manifold theorem at a hyperbolic zero. All density, pressure and boundary statements used here have their hypotheses written explicitly.

No currently checked identity yields an upper strain bound on Z from decay alone. That is a report of the present deductions, not a theorem excluding every future pressure, energy or geometric argument. The additional strain condition (4), arbitrary sign-changing helicity, the flat stratum and unrestricted C2 coverage remain open.

# Boundary regularity in each hypothetical nonzero multipole band

Status: CONFIRMED in A638 after complete independent reconstruction and postread. A623 already proves that all the relevant ACTUAL low multipoles vanish in this full-profile class without density. The conditional band argument below is valid but supplies no remaining case of the original conjecture.

## 1. Exact setting and statements

Let2/5<c<1/2, omega in R, Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, p=(1-c)/c. Let U in C2(R3;R3), P in C1(R3) solve

    ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    div U=0, U.curl U=0,

with uniform U->0 and DU=O(r^(1/2)), or the explicit natural velocity and derivative bounds. Let V be its actual tail, W=curl V, k=(Ax).V and E=grad k on D=R3 minus {0}. Let Theta_n be an actual low pressure multipole with (n+5)c<3 and n>=0. Put l=n+2.

For omega!=0 choose a nonzero azimuthal mode Phi of Theta_n with frequency m, and put sigma=|Phi|^2, b=2(n+3)c, beta=a/b. A band C is a connected component of {sigma>0}. If E cross grad sigma=0 throughout C, then k=W=V=0 on C. Without that extra rank assumption exactly one of the following holds:

1. V=0 on C, hence W=E=0 there.
2. C1={x in C:E cross grad sigma!=0} is nonempty, open and invariant under every exp(tA). It is irrotational, V=-E/a there, k is harmonic there and V cross grad sigma!=0 there.

Thus every band contains a nonempty open irrotational invariant set. Tail vorticity cannot be dense in any band. For omega=0 the identical statements hold for a nonzero real Theta_n with sigma=Theta_n, b=(n+3)c, beta=a/b, and bands the components of {sigma!=0}.

If tail vorticity were dense throughout D, these conclusions would imply every low Theta_n is0. Actual original exterior density is equivalent to this density by A603 under the current natural-profile hypotheses. The stronger density-free conclusion A623 supersedes this last corollary.

## 2. Compatibility and precise scalar boundary orders

The independent A610 and A609 proofs supply

    W.grad sigma=0 on D,
    E cross grad sigma=0 on {W!=0},
    W!=0 implies k!=0 and sigma!=0.                           (1)

For the real scalar at omega0 the same statements use its signed version. These conclusions use the explicit polynomial scalar weight, whose reciprocal is integrable and locally A2 by A608. They impose no A2 assumption on the actual S=P2-|V|^2/2. We will also use the exact identity

    E=-aV+(Ax) cross W.                                      (2)

For omega!=0 and j=|m|, the scalar angular part is a positive constant times

    (1-z^2)^j [P_l^(j)(z)]^2,

where P_l^(j) denotes the j-th ordinary derivative of the Legendre polynomial. That derivative has l-j simple roots in (-1,1), is nonzero at both endpoints, and l>=2. Thus sigma has quadratic vanishing on each interior nodal cone and order2j at the axis if j>0. If j=0, some interior cone exists. If j>0 and no interior cone exists, the axis is still nonempty. Consequently every band is a proper open subset of D and has a boundary point in D. Near an off-axis boundary point the zero set is a single smooth cone with two connected sides. Near an axial boundary point the zero set is just the axis and its local complement is connected.

These standard spherical harmonic properties were checked in A610. Their use requires a single azimuthal harmonic mode; a general combination can have different nodal geometry. For omega0 and a real harmonic multipole, A610 separately proves that each nodal domain on the sphere has at least one regular boundary point. The proof uses the local leading harmonic Taylor term in conformal coordinates to show that critical zeros are isolated and hence finite. If the boundary of a nodal domain were entirely among those finitely many points, connectedness of the punctured sphere would force the harmonic to have a single sign away from them, contradicting its zero spherical mean. This supplies a regular nodal boundary point without assuming it.

## 3. C1 regularity eliminates the component constant

Suppose rank holds throughout a band C. Since Ax.grad sigma=-b sigma and sigma!=0, grad sigma is nowhere0 there. Thus E=lambda grad sigma. The identity Ax.E=-ak implies

    lambda=beta k/sigma,
    grad(k |sigma|^-beta)=0.

Connectedness gives k=d_C |sigma|^beta for one constant d_C. At a boundary point x0 in D continuity gives sigma(x0)=k(x0)=0. Since k is C1, there is a finite L with |k(x)|<=L|x-x0| in a small ball.

For omega!=0, first suppose x0 is off the axis. The band contains one side of the local cone. Along an inward transverse segment of length comparable to epsilon, sigma>=C epsilon^2. Therefore

    |d_C| C^beta epsilon^(2beta)<=L' epsilon.

But2beta=a/((n+3)c)<1, so d_C=0. If x0 is on the axis, j>0 and the band contains the punctured ball off that axis. Along x=x0+epsilon e1, sigma>=C epsilon^(2j). The same comparison gives d_C=0 because

    2j beta=j a/((n+3)c)<= (n+2)a/((n+3)c)<a/c<1/2.

For omega0 choose the regular boundary point from Section2. On its appropriate connected side, |sigma|>=C epsilon along an inward normal segment. Then |d_C| C^beta epsilon^beta<=L' epsilon. Since beta=a/((n+3)c)<1, again d_C=0.

Thus k=E=0 on C. If W were nonzero anywhere there, (1) would force k!=0 at that point. Hence W=0 throughout C, and (2) gives V=0. This proves the extra-rank conclusion with only C1 regularity for k.

## 4. The rank-failure set and density consequence

Both k and sigma have exact twisted homogeneity. The map exp(tA) preserves {sigma!=0} and each of its connected components, because the orbit t to exp(tA)x is a continuous path within that set. Gradients transform by the same invertible transpose-inverse matrix with nonzero scalar prefactors. Consequently vanishing or nonvanishing of E cross grad sigma is preserved. The set C1 in Section1 is therefore open and invariant.

By (1), C1 is contained in {W=0}. On this open set (2) gives V=-E/a. Its divergence freedom gives Delta k=0 distributionally and hence classically by harmonic regularity. Moreover V cross grad sigma=-(E cross grad sigma)/a!=0 there. If C1 is empty, Section3 gives V=0 on the entire band. If V=0 throughout the band, (2) gives E=0 there and C1 is empty. These two cases are mutually exclusive and exhaustive.

The nonempty invariant open irrotational set is C itself in the first case and C1 in the second. It prevents density of {W!=0} in that band, proving the stated corollaries. No density premise is used to construct this open set.

## 5. The proposed S-to-multipole relation and the present scope

Suppose omega!=0 and, on a whole sigma-band whose boundary contains an interior nodal cone, the actual S satisfies

    S=C_sigma sigma^(b0/b), b0=2(1-c).

Its continuity makes S0 at the boundary, and its C1 regularity gives a Lipschitz upper bound there. On a transverse segment the right side has order

    2b0/b=2p/(n+3)<1,

since1<p<3/2 and n>=0. Thus C_sigma must be0. At an axial boundary the exponent instead is2j p/(n+3), which can exceed1; no identical scalar argument is asserted there. The k argument in Section3 works at both kinds of boundary because its exponent is smaller.

The old C41 remarks that these hypothetical bands leave unresolved cases are superseded in the actual full-profile class: A623 excludes every nonzero low actual Theta_n without density or A2 for S. A vanishing finite list of actual moments still does not exclude the all-zero-moment class. This proof does not establish automatic A2, symmetry of a general S, or global continuation of an arbitrary local irrotational tail.

## 6. Verification record

C41 Proposition38 and Remark39 have been read completely. The scalar degrees, boundary orders, connected-component argument, Lipschitz comparison and all invariance claims are reconstructed here. The only analytic dependencies are the already independently confirmed actual compatibility/localization A609-A610, nodal facts included in A610, density equivalence A603 and the stronger scope comparison A623. No computation is used. Existing configured-model C40 comparison has been read and agrees with the dependencies; this is not a claimed focused response on C41.

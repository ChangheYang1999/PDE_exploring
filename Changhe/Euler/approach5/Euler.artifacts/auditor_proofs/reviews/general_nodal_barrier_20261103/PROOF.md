# An elliptic obstruction for a smooth zero barrier, including infinitely flat nodes

Status: CONFIRMED as A486 at the exact prescribed-metric and prescribed-vorticity scope below, 2026-11-03T05:32:48.087030+00:00. Full postwrite reading and the coordinator-supplied focused review are complete. General Euler periodic orbits are not reduced to this ansatz.

## 1. Exact local theorem

Use Euclidean coordinates (theta,h,z) and the product metric. Let I be an open interval, b in C3(I), and let w in C3 on a planar neighborhood of the curve theta=b(h). Assume, on a strip after shrinking near any point of that curve,

    w(b(h),h)=w_theta(b(h),h)=0,
    w(theta,h)>0 for 0<theta-b(h)<epsilon.            (1)

Put W=(w,0,-z w_theta). Suppose a C2 vector field V on a three-dimensional neighborhood of the curve (b(h),h,0) satisfies

    curl V=W, div V=0, V.W=0.                        (2)

Then b is locally constant, and there is a continuous function ell(h) such that

    w_h(theta,h)=ell(h)w(theta,h)^3                  (3)

on a sufficiently small positive strip. These statements hold on every compact subinterval on which a common simply connected tubular region and reference section can be chosen. In particular a barrier with b'(h0)!=0 cannot have such a reconstruction near that point. No assumption that the zero has finite order is made.

There is a stronger conclusion when the scalar transport law

    nu w_theta-sigma h w_h=-kappa w,                 (4)

holds in the strip, where nu!=0, sigma and kappa are fixed finite real numbers. In that case no V satisfying (2) exists at all, even if the barrier is fixed. Thus no positive scalar nodal pattern obeying (4) can be reconstructed in this ansatz near its smooth zero barrier.

The theorem uses no pressure equation, global decay, carrier completeness or third derivative of V. The coordinates and metric are part of its hypotheses. The fixed similarity relation B=Ay+U is not asserted.

## 2. The potential and a common scalar identity

Set V0=(0,-z w,0). Direct differentiation gives curl V0=W, V0.W=0 and div V0=-z w_h. By (2) and the local Poincare lemma, V=V0+grad q for a C3 potential q on a smaller simply connected tubular region. The two remaining equations are

    w q_theta-z w_theta q_z=0,
    Delta q=z w_h.                                  (5)

In the positive strip h and I0=z w are invariants of the W-characteristics. Choose a C3 reference section theta=b(h)+epsilon0 inside the strip, with0<epsilon0<epsilon. On a smaller h interval its w_ref(h) is strictly positive. Define

    Q(h,I0)=q(b(h)+epsilon0,h,I0/w_ref(h)).

This is C3 near I0=0: w_ref is C3 and bounded away from zero, b is C3, and q is C3. For any fixed interior (theta,h), the segment in theta joining it to the reference section stays within the positive interval. The minimum of w along that compact segment is positive. Therefore, for all sufficiently small |z|, the characteristic with invariant I0=z w stays inside the three-dimensional tubular region while reaching the section. The required z width may depend on the interior point and may tend to zero at the barrier. This is sufficient to differentiate at z=0. No uniform characteristic travel time or uniform z width at the barrier is assumed.

Integrating the first equation of (5) yields

    q(theta,h,z)=Q(h,z w(theta,h))

locally near z=0 at every interior point. Consequently, with k(h)=Q_I(h,0) in C2 and ell(h)=Q_III(h,0) continuous,

    q_z(theta,h,0)=k(h)w(theta,h),
    q_zzz(theta,h,0)=ell(h)w(theta,h)^3.

Differentiate Delta q=z w_h once in z and use the C3 mixed derivatives of q. On the entire positive strip,

    k Delta_(theta,h)w+(2k'-1)w_h+k''w+ell w^3=0.     (6)

Only third derivatives of q occur. Although q is C3 on that region, the proof does not extend Q across the zero set in its characteristic coordinates.

## 3. An elementary Hopf barrier forces k=0

Fix h0 in the interval and suppose k(h0)!=0. On a smaller interval |k| is bounded below by a positive number. Divide (6) by k to obtain

    Lw=Delta w+d(h)w_h+gamma(theta,h)w=0,          (7)
    d=(2k'-1)/k,
    gamma=k''/k+(ell/k)w^2.

Both lower coefficients are bounded on the intersection of a small closed neighborhood of (b(h0),h0) with the positive strip. Differentiating the boundary identity w(b(h),h)=0 gives w_h+b'w_theta=0, so (1) implies Dw=0 on the barrier.

Because b is C3, the positive side of its graph has an interior tangent disk at p=(b(h0),h0), with center x0 and radius R, lying inside the local coordinate neighborhood. Shrink the disk if needed; w>0 in it and w(p)=0. Let gamma_-=min(gamma,0), and define L_-=Delta+d partial_h+gamma_-. Equation (7) and positivity of w imply

    L_- w=(gamma_--gamma)w<=0.

In the annulus R/2<|x-x0|<R consider

    phi(x)=exp(-alpha|x-x0|^2)-exp(-alpha R^2)>0.

If |d|<=B and |gamma_-|<=C0, then

    L_- phi>=exp(-alpha|x-x0|^2)
       [alpha^2 R^2-4alpha-2alpha B R-C0]>0

for sufficiently large alpha. Here the dimension is two, and phi<=exp(-alpha|x-x0|^2) was used for the nonpositive zeroth-order term. The inner circle is compactly inside the positive region, so choose delta>0 such that w>=delta phi there. On the outer circle phi=0 and w>=0. Thus f=w-delta phi is nonnegative on both annular boundaries and satisfies L_- f<0 inside.

If f had a negative interior minimum, its gradient would vanish and its Hessian would be nonnegative. Since gamma_-<=0, the zeroth-order term gamma_- f would also be nonnegative there. This would give L_-f>=0, a contradiction. Hence w>=delta phi throughout the annulus. Along the inward normal at p this implies

    partial_inward w(p)>=2delta alpha R exp(-alpha R^2)>0.

But Dw(p)=0. This contradiction shows k(h0)=0. Since h0 was arbitrary, k is identically zero on the interval, and (6) becomes (3).

This explicit barrier proof applies to infinitely flat zeros. It uses no nonzero Hessian of w at the boundary and no unproved unique-continuation theorem.

## 4. Why the zero barrier cannot move

Suppose b'(h0)>0. On a sufficiently small one-sided interval h<h0, the vertical line theta=b(h0) lies in the positive strip, while w(b(h0),h0)=0. The positive function f(h)=w(b(h0),h) obeys f'=ell(h)f^3 by (3). Since ell and f are bounded there, |f'|<=C f. Integrating gives a positive lower bound at h0 from any interior point, contradicting f(h0)=0. If b'(h0)<0, use h>h0 and the same argument in reverse time. Thus b' vanishes everywhere in the interval and b is constant.

More precisely, once the barrier is constant and a positive rectangle is available, (3) implies

    w(theta,h)=w(theta,h*)/
       sqrt(1-2w(theta,h*)^2 integral_(h*)^h ell(q)dq)

where the denominator is positive. This is only a necessary condition. No sufficiency for a general V is claimed.

## 5. Adding transport excludes even a fixed barrier

If (4) also holds, substitute (3) to obtain, at each fixed h,

    w_theta=-(kappa/nu)w+(sigma h ell(h)/nu)w^3.       (8)

The right side is locally Lipschitz as a function of w, and w reaches zero at the finite endpoint theta=b(h). Equivalently |w_theta|<=C_h w on a small interval where w is bounded. Integrating toward the endpoint gives a strictly positive endpoint value from any positive interior value, a contradiction. This proves the transport-enhanced nonreconstruction statement without needing the intermediate conclusion that b is constant.

## 6. Consequence for arbitrary nonnegative angular nodal shapes

Let sigma>0,nu!=0,kappa>0 and p=kappa/sigma. Let F in C3(R/(2pi Z)) be nonnegative, nonzero, and have at least one zero. For h>0 put

    w(theta,h)=h^p F(theta+(nu/sigma)log h).

It satisfies (4) exactly. Choose one component (a0,b0) of {F>0} on the universal angular cover. Its finite left endpoint a0 satisfies F(a0)=F'(a0)=0 by nonnegativity and C1 regularity. For every h0>0, the curve

    theta=b(h)=a0-(nu/sigma)log h

is a smooth zero barrier, w=w_theta=0 on it, and w>0 immediately on its chosen side. The preceding theorem applies near (b(h0),h0,0). Therefore no C2 incompressible helicity-free V can have curl V=(w,0,-z w_theta) there.

This covers F=sin^2, higher even-order zeros, and angular profiles with infinitely flat zero endpoints. The argument only uses h>0, so no regularity assumption on an extension across h=0 is needed. If one additionally wants the entire carrier model with h<=0 extension, that extension's regularity must be checked separately. Positive angular profiles with no zeros fall outside this nodal theorem; their W trajectories at z=0 are closed circles and fail the separate closed-vortex condition used in the campaign.

## 7. Research scope and verification plan

The theoretical question is whether LIT111's incompressible curl obstruction depended on its particular quadratic sine-squared zero. The proposed answer is no for this product-coordinate ansatz: the elliptic boundary argument replaces the Hessian test and requires only a smooth barrier with w=w_theta=0.

The remaining general periodic-orbit problem is different. Adapted coordinates change the Euclidean metric, may introduce other components of W, and must preserve the actual relation B=Ay+U. The preceding proof has not controlled those terms. It rules out a broad reduced pattern, not all flat periodic Euler orbits and not either witness type of A471 in general.

No computation is needed or used. The proof is based on the LIT111 potential reduction, whose exact common-Q domain and C3 regularity are supplied here, followed by an explicit elementary elliptic barrier and one-dimensional differential inequalities. The focused coordinator and literature-agent reviews have been read and checked through working files. No new model client or delegated computation is used.

The direct velocity proof in the team records, with r=1, gives these conclusions for C2 w and b and the more general continuous transport coefficients stated there. The present C3 potential proof is retained as an independent argument.

## Final audit record

A486, 2026-11-03T05:32:48.087030+00:00: all displayed mathematical arguments were independently reconstructed and the edited proof was read in full. The coordinator-supplied 212-line review was read in full and its findings independently checked. The coordinator is configured for the primary model; the review identifies a coordinator subagent without independent runtime model attestation. No new model client or remote computation was used. Earlier snapshots and metadata remain in verification; the current reconstruction record states the exact current scope.

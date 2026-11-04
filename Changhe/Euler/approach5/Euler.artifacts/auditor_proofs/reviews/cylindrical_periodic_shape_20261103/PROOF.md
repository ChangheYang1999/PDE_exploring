# Periodic angular shapes in a Euclidean cylindrical annulus

Status: CONFIRMED as a necessary-pair theorem, A743. The scalar test retains one exception; the full obstruction is proved separately in A744-A745. No velocity is constructed at the exceptional pair.

## 1. Exact statement

Let R>0, p>0 and beta!=0. Let F be a nonconstant real C2 function on the circle of length2pi. Let I be a nonempty open interval compactly contained in (0,infinity). Give the collar

    (R/(2pi Z)) times I times(-epsilon,epsilon)

the metric r(h)^2 dtheta^2+dh^2+dz^2, r(h)=R+h, with orientation r dtheta dh dz. This is a Euclidean cylindrical annulus, with an orientation choice. Set

    chi=theta+beta log h, w=h^p F(chi),
    W=w partial_theta-z w_theta partial_z.

The components here are contravariant coordinate components. If a C2 field V on this whole collar satisfies

    curl V=W, div V=0, <V,W>=0,                       (1)

then necessarily

    p=1/2, beta^2=1/24.                              (2)

Thus (1) is impossible for every other p>0,beta!=0. This is only a necessary condition at (2). In particular it excludes the prescribed transport shapes with p=(1+c)/(2(1-2c))>7/2 in the campaign range2/5<c<1/2, provided that their exact vorticity has the displayed cylindrical form. No reduction of a general periodic Euler orbit to that form is assumed or proved.

F may be nonvanishing, may change sign, and may have infinitely many zeros. No finite vanishing order is assumed. The conclusion is local in the positive h interval and uses the full angular shape. It does not require any extension to h=0.

## 2. Scalar reduction and angular integration

Write v=V^z. The complete metric calculation in the neighboring warped-nodal proof gives, using the h component of curl and helicity,

    v_theta=(w_theta/w)(v+z v_z)

on each nonzero phase interval. Its characteristics preserve z w and give

    v=w R_j(h,z w),
    k_j(h)=R_j(h,0), ell_j(h)=partial_I^2 R_j(h,0).

A fixed interior phase defines R_j as a C2 function. Thus k_j is C2 and ell_j continuous. Curl and divergence imply, by one z derivative of divergence,

    v_hh+(1/r)v_h+r^(-2)v_thetatheta+v_zz=r w_h+2w.

At z=0 this becomes

    (k_j w)_hh+(1/r)(k_j w)_h+r^(-2)(k_j w)_thetatheta
                                  +ell_j w^3=r w_h+2w.       (3)

For clarity, the metric factors follow directly from

    v_h-partial_z V^h=r w,
    partial_z(r^2 V^theta)=v_theta,
    partial_theta(r V^theta)+partial_h(r V^h)+partial_z(rv)=0.

Substituting the first two equations into the z derivative of the third gives the asserted scalar equation. No arbitrary-coordinate vector-Laplacian formula is used.

Choose a component D of the complement of {F=F'=0} containing a nonzero value, or the whole circle if this set is empty. Continuity of v_theta at each simple zero matches adjacent k_j to one k(h) on D. The simple zeros are locally finite in D, so a finite chain connects any two interior points. The cubic coefficients ell_j need not match. The argument is precisely the one detailed in the neighboring periodic-shape proof and is restated below where countable integration matters.

Dividing (3) by h^p gives, on each nonzero interval,

    A F''+B F'+C F+E_j F^3=0,                        (4)

with

    A=k(r^(-2)+beta^2/h^2),
    B=2beta k'/h+beta(2p-1)k/h^2+beta k/(h r)-beta r/h,
    C=k''+(2p/h+1/r)k'+[p(p-1)/h^2+p/(h r)]k
                                                    -p r/h-2,
    E_j=ell_j h^(2p).

Multiply by F' and integrate over D. The A and C boundary terms vanish at degenerate endpoints or by periodicity. Every E_j integral vanishes at its interval endpoints, or by periodicity if F has no zeros. In the case of infinitely many nodal intervals,

    E_j F^3 F'=-(A F''+B F'+C F)F'

is a bounded common integrable expression, so countable additivity is justified without a bound on the individual ell_j. Since F is nonconstant on D, the integral of (F')^2 is positive. Hence B=0. Put n=2p-1>-1. Then

    2k'+(n/h+1/r)k=r.                                (5)

The function k cannot vanish identically on any open interval. Restrict to an interval where it is nonzero. There is a nonzero phase interval on which F and F^3 are linearly independent, since F is nonconstant. Comparing (4)/A at two h values forces

    C/A=L                                             (6)

for one real constant L.

## 3. The two necessary identities

Equation (5) gives k'=[r-(n/h+1/r)k]/2. Differentiating and substituting into C yields

    C=(r^(-2)-h^(-2))k/4-[5+n r/h]/4.                (7)

This follows by collecting k', k and constant terms; the exact symbolic check in verification gives zero difference from the full expression in (4). It can also be checked by differentiating (5) and multiplying (7) by4h^2r^2. Combining (6)-(7) yields

    k[(1-4L)h^2-(1+4L beta^2)r^2]
                                    =h r^2(5h+n r).   (8)

All these identities hold on an open positive h interval. Comparisons of polynomial coefficients below are identities on that interval, not asymptotic assertions about a domain endpoint.

Rescale h=R x,k(h)=R^2 K(x); a constant shift beta log R can be absorbed into F. Equations (5) and (8) then have R=1. Write h again for x, let r=1+h, b=beta^2>0 and s=1+4Lb. Define

    D=(1-4L)h^2-s(1+h)^2,
    N=h(1+h)^2[5h+n(1+h)].

D is not the zero polynomial. If it were, its constant term would give s=0 and its quadratic coefficient L=1/4, contradicting s=1+b>0. We may therefore restrict to a nonempty subinterval where D!=0 and obtain k=N/D.

Substitute this into (5), multiply by D^2 and collect the resulting polynomial. Its constant and linear coefficients are respectively

    -s(s+n^2+2n),
    -s(5s+5n^2+18n+20).                              (9)

These two exact coefficients can be obtained directly from N,D and their first two Taylor coefficients at0. Evaluating coefficients at0 is legitimate for a polynomial identity even though the profile is defined only on a positive interval. The complete polynomial and an independent symbolic derivation of (7) are retained in verification.

If s!=0, (9) first gives s=-n^2-2n, and then8n+20=0. This would imply n=-5/2, contradicting n>-1. Therefore

    s=0, L=-1/(4b).

Now D=(1+1/b)h^2. Equation (8) gives

    k=t(1+h)^2[5h+n(1+h)]/h,
    t=b/(1+b)>0.                                    (10)

## 4. The surviving branches

Inserting (10) into the left side of (5), its Laurent coefficient of h^(-2) is t n(n-2). Since the right side1+h has no negative powers, n is either0 or2. This coefficient comparison is again an identity of rational functions on an open interval. It does not require that the original field be defined near0.

If n=2, direct expansion gives

    2k'+(2/h+1/(1+h))k=t(24/h+73+49h),

which cannot equal1+h since t>0. If n=0, the left side is25t(1+h). Hence t=1/25, and

    b=1/24, p=(n+1)/2=1/2.

Returning to the unscaled variables gives

    k=(R+h)^2/5, L=-6.

These values do satisfy the two necessary identities (5)-(6). The exact follow-up script checks both branches and this residual. Thus the initial proposed exclusion of every p>0 was too strong at the level of this test. The corrected necessary condition (2) is proved by the complete case analysis.

The remaining angular equation at this pair is F''-6F+M F^3=0 on each nonzero interval, with suitable constants M. Periodic nonconstant solutions of such an equation are not excluded by the calculation. This scalar calculation alone does not decide whether a full C2 velocity satisfying (1) exists at this pair. A744-A745 subsequently exclude it using the full Poisson equation. No claimed counterexample or sufficiency inference is based on it.

## 5. Scope, dependencies and computation record

The proof uses only the metric equations (1), the exact two-component form of W and full angular periodicity. It does not use Euler momentum, pressure, decay, a carrier field or the profile relation B=Ay+U. The metric is genuinely Euclidean cylindrical, but arbitrary tubular coordinates around a periodic orbit need not have this metric and need not preserve the exact form of W. High-growth flat periodic witnesses of A471 therefore remain open in general.

The common C2 characteristic reduction and countable angular integration are written in full in the neighboring periodic and warped-nodal proofs. The metric component identities and all coefficients needed for the present conclusion are displayed above. The scripts use exact rational-symbolic arithmetic as a check of explicit identities; no floating-point certificate is used.

The first computation ran2026-11-03T04:56:50.663652Z to04:56:51.230102Z,0.566431seconds. Its original all-positive-p pass criterion failed because the pair (2) survives. The branch follow-up ran2026-11-03T05:00:34.969171Z to05:00:35.320659Z,0.351473seconds, and passed its narrower stated criterion. Both ran locally on the one assigned CPU at low priority with one thread. The theoretical questions, original criterion, failure record, scripts and complete outputs are retained alongside this proof. No new computation is running.

The full postwrite audit and the independently written LIT114 proof were read completely by 2026-11-03T05:04:41.183919Z. They agree on the exact metric, scalar reduction, countable angular integration, parameter exception and limited scope. LIT114 is pinned in verification. The full current submission and this proof were reread at the final audit recorded in the team records. The necessary-pair conclusion is CONFIRMED as A743.

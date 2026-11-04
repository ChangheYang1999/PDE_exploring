# Signed level-band concentration and the critical core-return example

Status: CONFIRMED A709-A711 after complete source and independent-proof postreads. Date: 2026-11-03T10:24:14.872490+00:00.

## 1. Exact actual-profile conclusion

Let 2/5<c<1/2, omega be any finite real number, p=(1-c)/c, d=p-1 and eta=d/(2p). Put Jx=(-x2,x1,0), A=cI-omega J. Assume U in C2(R3;R3), P in C1(R3), div U=0,

    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

Let V,W,P2 be the actual tails and canonical pressure of A209-A210 and A530-A531. Set S=P2-|V|^2/2, h=S|S2, G=W|S2. For a nonzero profile there are C0,t0>0 such that

    integral_{|h|<t}|G|dA >= C0 t^eta, 0<t<t0.       (1.1)

If h and G are both nonzero at some point, there are sigma in {1,-1}, constants b>a>0, C1,t1>0 such that

    integral_{at<=sigma h<=bt}|G|dA >= C1 t^eta,
    0<t<t1.                                        (1.2)

Consequently integral_{sigma h>0}|G||h|^(-eta)dA diverges. This does not require a hypothesis on the area of {h=0}. No assertion is made that a nonzero profile must possess a point with hG!=0.

Separately, the kinematic example in Sections4-5 has finite-time core return and every subcritical reciprocal scalar moment finite, while the critical moment diverges logarithmically. It fails Poisson and is singular at zero. It tests the critical exponent in the flux mechanism only, not sharpness of actual-profile nonexistence.

## 2. The stopped-flow inequality and signed bands

The complete proof of A705 supplies a C1 volume-preserving partial W flow F_t by exact scattering conjugacy. A360 gives almost-everywhere finite positive lifetime with endpoint0 on {W!=0}. The every-curve scalar transport is A531. These actual inputs permit selection of a measurable positive-volume set B inside 1<|z|<2, with lifetimes at most a fixed finite T. If |S|<M on B, it remains so along every surviving curve.

A radial cutoff changing from0 on B to1 near its terminal origin gives at least unit total variation on each curve. Integration over B and [0,T], followed by ordinary change of variables on the surviving open flow domains, gives

    |B| <= C T epsilon^(-d)
            integral_{|h|<M(2epsilon)^(2p)} |G|dA.  (2.1)

This is the A705 inequality, rechecked with radial measure r^2drdA and |W|=r^(-p-1)|G|. The division by epsilon for the cutoff gradient leaves exponent1-p=-d. No terminal flow map or global W completeness is used. Substitution t=M(2epsilon)^(2p) proves (1.1), already independently recorded as A708.

If h and G are nonzero together, continuity and homogeneity give a positive-volume annular open set on which W!=0 and

    0<m0<=sigma S<=m1<infinity.

Select a positive-volume bounded-lifetime B from that set. Scalar constancy preserves both inequalities. When epsilon<r<2epsilon, they imply

    m0 epsilon^(2p)<=sigma h<=m1(2epsilon)^(2p).

The same change of variables therefore replaces the sublevel set in (2.1) by this level band. Put t=epsilon^(2p), a=m0, b=2^(2p)m1. Then b>a and the inequality is precisely (1.2), with positive constants independent of t.

## 3. Disjoint bands force critical divergence

On the band in (1.2), |h|^(-eta)>=(bt)^(-eta). Its critical weighted integral is therefore at least C1 b^(-eta)>0. Choose t_n=t_* q^n, with t_*<t1 and 0<q<a/b. Then b t_(n+1)<a t_n, so the bands are pairwise disjoint and all lie in the same strict sign of h. Adding their uniform positive lower bounds proves the claimed divergence.

There is no zero-level term in this argument. If instead W is nonzero only where S=0, no point with hG!=0 exists and the signed-band argument is inapplicable. A708 still gives the sublevel estimate; A706 excludes this alternative only under its explicit zero-set clause. These cases must not be conflated.

## 4. An exact finite-time core-return field

Set omega=0, retain 1<p<3/2, d=p-1, and let r,theta,phi be spherical coordinates. For a positive constant K define on D=R3 minus{0}

    V=r^(-p-1)Jx=r^(-p)sin(theta)e_phi,
    W=r^(-p-1)[2cos(theta)e_r+d sin(theta)e_theta],
    m=4p/d=2/eta>12,
    Sstar=-K r^(-2p)sin(theta)^m.                   (4.1)

The Cartesian formula for V is smooth on D and divergence-free. Direct spherical curl gives the displayed W: its radial component is r^(-p-1)(sin(theta))^(-1)partial_theta(sin(theta)^2), and its polar component is -r^(-1)partial_r(r V_phi). Thus W=curl V and div W=0. Its two components are orthogonal to V, so V.W=0. Since c d=1-2c,

    cx cross W=(1-2c)V.

The scalar Sstar is at least C12 on D, including the axis, because m>12 and the transverse dependence is a positive smooth factor times the m-th power of cylindrical radius. At c=3/7, p=4/3, m=16 and it is smooth on D. Differentiating off the axis gives

    W.grad Sstar=r^(-p-2)Sstar[-4p cos(theta)+d m cos(theta)]=0.

The identity extends to the axis by continuity. Hence Sstar is constant on every W curve.

For the time-changed field X=r^(p+2)W, use parameter t. Its equations are

    theta'=d sin(theta), (log r)'=2cos(theta), phi'=0.

Every off-axis solution has

    tan(theta/2)=exp(d(t-t_*)),
    r=C sech(d(t-t_*))^(2/d), C>0.                  (4.2)

Indeed sin(theta)=sech(d(t-t_*)) and integration of dlogr/dtheta=(2/d)cot(theta) gives r=C sin(theta)^(2/d). Both ends t->+/-infinity approach0. The W parameter tau satisfies d tau/dt=r^(p+2); its integral is finite at both ends by the exponential decay in (4.2). Thus every off-axis W curve has finite physical lifetime and both endpoints0. The axis is a volume-null exception. W is smooth and divergence-free on D, so its ordinary partial flow is a C1 volume-preserving diffeomorphism wherever defined. This example meets the exact flow inputs of the critical-flux proof without any scattering realization claim.

## 5. Exact reciprocal threshold and explicit pressure failure

On the unit sphere

    |G|^2=4cos(theta)^2+d^2 sin(theta)^2,

so d<=|G|<=2. Near either pole, |Sstar| is comparable to theta^m and dA is comparable to theta dtheta dphi. Consequently for beta>=0,

    integral_S2 |G||Sstar|^(-beta)dA < infinity
          if and only if m beta<2,
          if and only if beta<eta.

At beta=eta the divergence is logarithmic. The sublevel mass integral_{|Sstar|<t}|G| is bounded above and below by positive constants times t^(2/m)=t^eta. The same reciprocal threshold holds without the factor |G| because it is bounded above and below. Thus arbitrary subcritical reciprocal assumptions do not exclude this example within the stated kinematic class.

To show a distinct necessary equation fails, put

    T0=integral_S2 |V|^2=8pi/3,
    I_m=integral_S2 sin(theta)^m dA>0,
    K=1+(p+1)T0/(2p I_m),
    Pstar=|V|^2/2+Sstar.

The exact annular radial Poisson identity, rederived in A707, would require for tangential V

    integral_S2 Sstar=-(p+1)T0/(2p)

if -Delta Pstar=partial_i partial_j(V_i V_j) held. The specified K instead makes that integral equal to the required number minus I_m. This is a nonzero discrepancy on a test supported away from the origin, independently of the singularity there. Pstar is not the canonical pressure. Neither this example nor the threshold computation is an Euler-profile counterexample.

## 6. Dependencies and verification

The actual statements use A705-A708, A360 and A531 with all exact hypotheses repeated above. The kinematic family is the A548 field, but its curl, transport, complete time change, finite physical lifetimes, angular mass and pressure failure were recalculated directly here. The five-section LIT176 source and the complete A548 proof were read. No numerical calculation or formal build was needed. Existing configured-model focused comparison remains requested through working files; a requested review is not a completed response and provider runtime is not independently attested.

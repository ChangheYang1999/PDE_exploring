# Canonical comparison without the actual-profile rank equation

## 1. Exact countertest and scope

Let D=R3 minus{0}, r=|x|, n=x/r, mu=x3/r, Jx=e3 cross x, p=10/9, c=9/19, A=cI-omega J, d=5/4 and A0=9/4. For every finite real omega set

    V=r^(-p)(e3+d mu n),
    P2=r^(-2p)(-1035+2250mu^2)/608,
    E=|V|^2, S=P2-E/2, X=Ax, k=X.V.

Then V,P2 are smooth on D, V is divergence free and helicity free, P2 is its canonical pressure, and

    DV X=-((1-c)I+omega J)V,
    Delta P2=-tr((DV)^2), X.grad S=-2(1-c)S,
    (curl V).grad S=0.

The vorticity is nonzero off the polar axis and

    (608/1339)|S|<=E<=(19/2)|S|, S<0 on D.         (1)

Nevertheless the rank equation grad k cross grad S=0 and the complete profile momentum equation fail for every omega. A smooth entire divergence-free helicity-free extension also has natural velocity and gradient decay, exterior dense vorticity and a fixed comparison with its own canonical pressure, but still fails momentum. These examples test omitted equations. Neither is a nonzero Euler profile satisfying the campaign hypotheses.

## 2. Velocity identities, density and the global ratio

In spherical coordinates V=r^-p(A0 mu e_r-sin(theta)e_theta). Its divergence is

    r^(-p-1)[(2-p)A0-2]mu=0.

The Cartesian formula is smooth on D including the axes. Axisymmetric vector covariance gives DV Jx=JV, while ordinary homogeneity gives DV x=-pV. Since cp=1-c, both imply the twisted velocity equation for every omega.

The only curl component is

    W=(p-1+A0)r^(-p-1)sin(theta)e_phi
      =(85/36)r^(-19/9)sin(theta)e_phi.             (2)

It is nonzero exactly off the axis. V has no azimuthal component, so V.W=0. S is axisymmetric, so W.grad S=0. Ordinary scalar degree-2p gives its twisted homogeneity for every omega.

Direct squaring and subtraction give

    E=r^(-20/9)(16+65mu^2)/16,
    S=r^(-20/9)(-1339+1015mu^2)/608.

The largest angular coefficient of S is-324/608<0. For t=mu^2,

    E/|S|=38(16+65t)/(1339-1015t), 0<=t<=1.

Its derivative has positive numerator38(65*1339+16*1015). The endpoint values are608/1339 and19/2. This proves(1) with constants attained on the equator and axis; there are no scalar zeros to remove.

## 3. Exact Poisson calculation and canonical pressure

Write DV=r^(-p-1)T. Differentiation gives

    T=-p e3 tensor n+d n tensor e3+d mu I
                                      -d(p+2)mu n tensor n.

With d=p/(2-p), contraction yields

    tr(T^2)=-2p^2/(2-p)
                  +2p^2(5-p)/(2-p)^2 mu^2.         (3)

One can check the contraction directly with tensor inner products. Alternatively rotational invariance makes it a quadratic polynomial in mu; at mu=0 the nonzero off-diagonal entries are-p,d, giving-2pd; at mu=1 the eigenvalues are-pA0,d,d. The two values determine exactly(3).

For P2=r^-2p(u+vmu^2),

    Delta P2=r^(-2p-2)[lambda u+2v+(lambda-6)vmu^2],
    lambda=2p(2p-1)=220/81,
    u=-1035/608, v=1125/304.

The constant coefficient is25/9=2p^2/(2-p), and the mu^2 coefficient is-875/72=-2p^2(5-p)/(2-p)^2. This verifies the Poisson equation exactly.

For canonical normalization put Gamma=1/(4pi|x|) and Pcan=partial_i partial_j Gamma*(V_iV_j), in the distributional kernel sense. The stress is locally integrable at0 since2p<3. At fixed x!=0 the contribution near0 is integrable, the contribution near x is the usual distributional principal value with its local contact term, and the far integral converges because D2Gamma=O(r^-3) and the stress is O(r^-2p). Smooth local Taylor subtraction justifies the principal value and local regularity. Scaling and rotational covariance preserve this definition, giving Pcan degree-2p and axisymmetry.

There is also an ordinary potential construction here: Gamma*(V_iV_j) converges away from0 since2p>2 at infinity and2p<3 at0, and its two distributional derivatives give the same pressure. Its degree is2-2p before differentiation. Thus no convention for an infinite undifferentiated far integral is needed for this particular example.

The difference Pcan-P2 is smooth harmonic on D and ordinarily homogeneous of degree-20/9. Its angular part would be a sphere eigenfunction with eigenvalue220/81, strictly between2 and6 and hence absent from the spectrum ell(ell+1). Therefore the difference is zero. This fixes canonical pressure, rather than selecting a convenient harmonic addition. The locally integrable homogeneous extension of P2 also agrees with the canonical distribution at0: any difference supported at0 would be a sum of delta derivatives of integer degree-3-j, incompatible with degree-20/9. No singular products of DV at0 are asserted.

## 4. Explicit rank, closedness and momentum failures

There is no azimuthal velocity, so k=K r^(1-p)mu with K=cA0=81/76. At the equator let s0=-1339/608. Then

    grad k=-K r^-p e_theta,
    grad S=-2p s0 r^(-2p-1)e_r,
    grad k cross grad S=-2p K s0 r^(-3p-1)e_phi!=0.

This is inside the open vortical set; continuity gives an open band of failure. Thus even vortical rank is missing, despite dense vorticity and every listed reduced tail identity.

Set h=-S and eta=(p-1)/(2p)=1/20. At the equator Dh=-2ph e_r/r and V=-r^-p e_theta. Using(2),

    curl(h^-eta V)=h^-eta W-eta h^(-eta-1)Dh cross V
                 =A0(1339/608)^(-eta)r^-2 e_phi!=0.

The form is smooth on D. Its lack of a potential comes from failure of closedness, not a zero-set regularity defect; pressure removal alone cannot fix a failed curl equation.

The linear profile terms vanish by homogeneity. At the equator the radial component of DV V is d r^(-2p-1), as is also immediate from T e3=d e_r there. The radial pressure gradient is-2pu r^(-2p-1). Their sum is

    (DV V+grad P2).e_r=(d-2pu)r^(-2p-1)
                     =(765/152)r^(-29/9)!=0.       (4)

This holds for every omega. V is also singular at0. The example is neither an entire profile nor an actual natural tail of a globally zero-helicity profile to which A413/A604 rank applies.

## 5. Entire smooth cutoff and its actual canonical pressure

Choose a smooth radial chi equal to0 for r<=1 and1 for r>=2, and define the vector potential

    B=(9/8)chi(r)r^-p Jx, U=curl B,

with B=0 on the unit ball. The constant pieces and smooth cutoff give an entire C-infinity field. The identity

    curl(r^-p Jx)=(2-p)r^-p e3+p x3x r^(-p-2)

and(9/8)(2-p)=1,(9/8)p=5/4 show U=V outside B2. Curl construction gives div U=0. The potential is axisymmetric azimuthal, so U is poloidal and curl U azimuthal; U.curl U=0 everywhere, including axes by continuity. The unchanged exterior and smooth compact core give the full natural U/DU bounds.

Let P be U's own canonical pressure. The compact stress difference F=U tensor U-V tensor V is supported in B2 and is L1, using2p<3. For r>=4,

    Q=P-P2=partial_i partial_j Gamma*F_ij,
    |Q|<=Cr^-3, |grad Q|<=Cr^-4.                   (5)

All kernels are smooth away from the compact support, so these bounds follow by absolute integration. P is smooth by local canonical-pressure regularity and tends to0. Thus Pinf=0, fixed by the canonical normalization.

Because |S|>= (81/152)r^-2p and2p<3, at sufficiently large radii(5) gives |Q|<=|S|/2. On that exterior U=V and

    |S|/2<=|P-|U|^2/2|<=3|S|/2.

Combining with(1) proves

    [1216/(3*1339)]|P-|U|^2/2|<=|U|^2
                              <=19|P-|U|^2/2|.

Its vorticity is dense in the exterior by(2). Yet the radial momentum residual at large equatorial points is

    (765/152)r^(-29/9)+O(r^-4),

nonzero eventually since29/9<4. The linear profile terms still vanish there. This proves failure of the full equation for every omega, even after the origin singularity and canonical pressure are repaired.

## 6. Verdict and limits

LIT270's punctured example, canonical normalization, exact comparison, rank and momentum failures, and smooth entire countertest are CONFIRMED. All six submitted and independent sections were read and all coefficients were checked by hand. No new computation was needed. The author's exact Fraction search is supporting evidence only, not used to infer an identity or nonexistence.

The classical sphere spectrum and distributional Newtonian kernel are named external inputs; the absolute integrability, scaling, harmonic ambiguity and possible origin-supported defect were checked explicitly. Formal sources are absent because no formal build was used. The source and hash are in the team records.

The example refutes an inference of rank from the LISTED REDUCED equations and comparisons. It does not refute A413, LIT267, LIT268 or LIT269 at their full hypotheses, and it neither proves nor disproves the campaign conjecture. Existing configured model file exchanges provide model comparison, with actual provider runtime independently unattested.

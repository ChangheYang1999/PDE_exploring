# Exact surface defects at the critical integrating-factor exponent

Status: CONFIRMED A713 after complete source and independent-proof postreads. Date: 2026-11-03T10:24:55.152381+00:00.

## 1. Statement and exact class

Let 2/5<c<1/2, omega be any finite real number, p=(1-c)/c in(1,3/2), a=1-2c, t=omega/c, beta=(p-1)/(2p), nu=1/beta>6. Write Jx=(-x2,x1,0), A=cI-omega J, D=R3 minus{0}. In spherical coordinates r,theta,phi put z=cos(theta), s=sin(theta),

    F=z(1-z^2), H=-(2-p)t(1-z^2)^2/4,
    V=r^(-p)[tF e_r+(H/s)e_theta+(F/s)e_phi],
    S=-K r^(-2p)|F|^nu, K>0, W=curl V.

Then V is smooth on D and not identically zero, S is at least C6, and

    div V=0, Ax cross W=aV, V.W=0, W.grad S=0.

Both V and S have the usual twisted degrees -p and -2p. Near every nonzero equatorial point, |S| is comparable to |x3|^nu, so nu beta=1. There the integrating factor |S|^(-beta)V is not locally integrable if omega!=0. If omega=0, it is locally bounded away from the axis but has the nonzero surface curl measure in Section3. An explicit K makes the assigned Pstar=S+|V|^2/2 violate Poisson on an annular test.

This is a kinematic endpoint countertest, not an entire Euler profile, not a canonically pressured tail and not an optimality theorem for all global nodal hypotheses. The same example has additional axial zeros. At c=3/7, nu=8 and S,Pstar are smooth on D for every omega.

## 2. Direct verification of the leading equations

With n=x/r, the Cartesian angular formula is

    V=r^(-p)[z Jn+(t/4)(1-z^2)((p+2)z n+(2-p)e3)].

It proves removability of both apparent pole singularities and ordinary homogeneous axisymmetry, hence the stated twisted homogeneity for every omega. Direct spherical divergence and curl yield

    div V=r^(-p-1)[(2-p)tF-H'],
    W=r^(-p-1)[-F'e_r+(p-1)F e_theta/s
                    +(-(p-1)H/s+t sF')e_phi].

Since H'=(2-p)tF, incompressibility holds. On the unit sphere Ax=c e_r-omega s e_phi. Its cross product with W has components a tF,aH/s,aF/s, using c(p-1)=a and ct=omega. Homogeneity extends this identity to D. Dotting with W gives zero helicity.

For any scalar r^(-2p)f(z), the displayed W gives

    W.grad(r^(-2p)f(z))
       =r^(-3p-2)[2p F'f-(p-1)F f'].

For f=-K|F|^nu, F f'=nu F'f off F=0, and nu(p-1)=2p. The expression vanishes and extends to all zeros by continuity, since nu>6 implies f=f'=0 there. The same power inequality gives the stated C6 regularity; nu=8 removes the absolute power altogether. No pressure equation was used.

## 3. The two different critical surface failures

Off F=0, direct cancellation of radial powers gives

    Y=|S|^(-beta)V
      =K^(-beta)r^(-1)[t sgn(F)e_r
            +H e_theta/(s|F|)+sgn(F)e_phi/s].       (3.1)

At a fixed nonzero equatorial point, r and s are bounded above and below, |F| is comparable to |x3|, and H is bounded away from0 whenever t!=0. Its polar component therefore gives |Y|>=C/|x3| nearby. Integrating across the equatorial surface proves failure of local L1. A distributional curl cannot be obtained from Y by ordinary locally integrable-field testing in this case.

If t=0, H=0 and (3.1) instead reduces, with cylindrical radius rho, to

    Y=K^(-beta)sgn(x3)e_phi/rho.

On a neighborhood of a nonzero equatorial point avoiding the axis, choose a smooth local azimuthal angle phi, so grad phi=e_phi/rho and curl grad phi=0. The distributional derivative of sgn(x3) is2 delta_{x3=0}e3, giving

    curl Y=2K^(-beta)delta_{x3=0} e3 cross grad phi
          =-2K^(-beta)delta_{x3=0} e_rho/rho.        (3.2)

This is a nonzero surface measure, with its sign fixed by e3 cross e_phi=-e_rho. Testing against a nonnegative radial-component test verifies it directly. The formula is local away from the axis and makes no claim about the additional axial defect.

The exact smooth regularization obeys

    curl[(S^2+epsilon^2)^(-beta/2)V]
      =epsilon^2(S^2+epsilon^2)^(-beta/2-1)W.

Its right side tends to zero off the zeros, but the usual candidate majorant |S|^(-beta)|W| behaves as C/|x3| at the equator and is not integrable. Thus dominated convergence is unavailable and (3.2) survives. Local integrability of Y alone does not repair this curl defect.

## 4. An explicit annular pressure contradiction

Use angular surface measure on S2 and define

    R0=integral V_r^2, T0=integral |V_T|^2,
    I0=integral |F|^nu>0,
    Q0=[(3p-2)R0+(p+1)T0]/(2p)>0,
    K=1+Q0/I0.

All are finite exact integrals and V is nonzero, so the indicated inequalities are strict. If Pstar=S+|V|^2/2 satisfied -Delta Pstar=partial_i partial_j(V_i V_j), the annular radial identity, rederived in A707, would give integral_S2 S=-Q0. The chosen K instead gives -K I0=-Q0-I0. This is a nonzero discrepancy on an annular test supported away from zero. It is independent of the singularity of V at the origin.

For arbitrary K, Sections1-3 remain valid. Only K=Q0/I0 could satisfy the mean constraint, and no full pressure compatibility is asserted even at that value. The artificial scalar here must not be substituted for the canonical pressure deficit of an actual profile.

## 5. Verification and limits

The complete six-section LIT140 source was read; all coordinates, curl components, signs, critical powers and the annular mean were independently reconstructed. No symbolic or numerical calculation was necessary. The velocity is the previously audited A514 family, but no unchecked calculation from that family is needed above. The critical equatorial surface failure is local; the extra axis zeros prevent an optimality claim for the whole global surface-chart theorem. Existing configured-model comparison is requested through working files without a new client, agent or unverified completed-response claim.

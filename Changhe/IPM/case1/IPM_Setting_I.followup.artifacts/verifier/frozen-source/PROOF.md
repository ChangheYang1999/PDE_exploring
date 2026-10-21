# Frozen fifth-order source examples

Independent check dated 2026-10-20. This result is local to a frozen linear operator with a specified homogeneous potential. The examples do not satisfy the global growth assumption for IPM profiles.

## Statement

Write R=(s^2+y^2)^(1/2) and define

    L_g v = (A s partial_s + y partial_y - 1)v + g U_2[v].

In this statement the potential convention is Delta Phi=v and U_2=-partial_s^2 Phi. Set

    V_A(s,y) = integral_0^y (s^2+t^2)^((A-1)/2) dt,
    Phi_V(s,y) = (A+1)^(-2) integral_0^y (s^2+t^2)^((A+1)/2) dt,

    Q_A(s,y) = s integral_0^y (s^2+t^2)^((2A-3)/2) dt,
    Phi_Q(s,y) = s/[(2A-1)(2A+1)] integral_0^y (s^2+t^2)^((2A-1)/2) dt.

The choices (v,A,g)=(V_(5/2),5/2,21/4), (Q_(7/4),7/4,27/8), and (Q_2,2,5) satisfy L_g v=0 as tempered distributions. They are odd in y and smooth on s!=0. The first two belong to C^(2,1/2) locally and to no C^(2,beta) for beta>1/2 on a neighborhood meeting s=0. The third belongs to C^(2,alpha) for every alpha<1 but not C^(2,1).

For G_j(s)=partial_y^j v(s,0)/j! and Z_j(r)=r^((j-1)/A)G_j(-r), r>0, their traces are

| Example | Z_3 | Z_5 |
| --- | --- | --- |
| Q_(7/4) | -r^(9/14)/12 | 3r^(-3/14)/160 |
| Q_2 | -r/6 | 1/40 |
| V_(5/2) | r^(3/10)/4 | -3r^(-9/10)/160 |

Thus the third normalized traces vanish while the fifth either diverge or tend to a nonzero constant. This refutes an inference of fifth-trace vanishing from the stated class regularity and smoothness on the left for this frozen problem at these three parameter pairs. It does not refute a stronger regularity theorem, a nonlinear profile theorem, or the corresponding inference at every A.

## Differential identities

For a radial power in two dimensions,

    Delta R^m = m^2 R^(m-2),
    Delta(s R^m) = m(m+2)s R^(m-2).

Apply these identities to partial_y Phi_V and partial_y Phi_Q. They give partial_y(Delta Phi-v)=0. Both differences vanish on y=0 for s!=0 by oddness and smoothness, proving Delta Phi=v there.

Let f=partial_y v and phi=partial_y Phi. Differentiating the frozen equation in y cancels the two terms f from y partial_y v-v. For V the differentiated residual is

    (A-1)(A s^2+y^2)R^(A-3)
      - [g/(A+1)](A s^2+y^2)R^(A-3),

which vanishes for g=A^2-1. For Q it is

    (A-1)s(2A s^2+3y^2)R^(2A-5)
      - [g/(2A+1)]s(2A s^2+3y^2)R^(2A-5),

which vanishes for g=(A-1)(2A+1). The original residual vanishes at y=0, so its y derivative and its value there prove L_g v=0 for s!=0. The regularity proved below makes v C^2 and Phi C^4. All terms of both equations therefore extend continuously across s=0. Equality on its dense complement implies equality everywhere, and hence distributional equality. Polynomial growth of the integral formulas proves temperedness. This argument does not apply a divergent full-plane kernel to these growing fields: the displayed potentials are part of their definition.

## Regularity, including the entire line s=0

For fixed y>0, put I_m(s,y)=integral_0^y(s^2+t^2)^(m/2)dt. Substitution t=|s|z, subtraction of the large-z binomial terms, and integration of those terms give a convergent expansion for 0<|s|<y of the form

    I_m(s,y) = sum_j binom(m/2,j) s^(2j) y^(m-2j+1)/(m-2j+1)
               + c_m |s|^(m+1),
    c_m = sqrt(pi) Gamma(-(m+1)/2)/(2 Gamma(-m/2)),

when m is not an odd integer. The formula for c_m follows by t=z^2 in the subtracted constant integral, or equivalently by continuing the convergent beta integral. All differentiated series converge uniformly on |s|<=epsilon y with epsilon<1. For m=3/2 and m=1/2 both gamma ratios are finite and nonzero.

Consequently V_(5/2) has, transverse to the line at y>0, a nonzero |s|^(5/2) term in addition to a smooth function. Q_(7/4) has a nonzero s|s|^(3/2) term. Their second derivatives are locally 1/2-Hölder and not beta-Hölder for any beta>1/2 across that line. Reflection gives the same conclusion at y<0.

The origin requires a uniform check, not just a fixed-y expansion. Both fields are homogeneous of degree 5/2. Their second derivatives are homogeneous of degree 1/2 and, by the preceding expansions, have 1/2-Hölder angular restrictions on the unit circle. A function homogeneous of degree beta in (0,1) with bounded beta-Hölder angular restriction is beta-Hölder on a disk: for points at distance delta, if the smaller radius is at most 2delta, use homogeneity and the triangle inequality; otherwise compare their radii and angles, with angular distance at most C delta/r. Both estimates are bounded by C delta^beta. This proves the joint C^(2,1/2) assertion through the origin and line. Nonzero transverse coefficients prove the failure of higher Hölder exponents. The same reasoning with the higher-degree potentials gives C^(4,1/2) for Phi.

For Q_2 there is an explicit formula, for s!=0:

    Q_2 = (s/2)[y sqrt(s^2+y^2)+s^2 asinh(y/|s|)].

On compact subsets of y>0 this is a smooth function plus -(s^3/2)log|s|. Thus its second s derivative contains -3s log|s|, which is alpha-Hölder for every alpha<1 and is not Lipschitz. To verify the same estimate at the origin, use its homogeneity of degree three. On the unit circle each second derivative is Lipschitz apart from terms of the form z log|z|, which have modulus at most C delta(1+|log delta|). Comparing radii and angles as above, when r>2delta the angular contribution is at most C delta(1+log(r/delta)); bounded r makes this at most C_alpha delta^alpha. When r<=2delta, homogeneity bounds each second derivative by C delta. This establishes C^(2,alpha) jointly for every alpha<1, with non-Lipschitz behavior already seen at fixed y>0. Applying the same calculation to the degree-five Phi_Q yields C^(4,alpha). These arguments justify the distributional extensions used above.

## Trace computation and scope

Expanding the integrands in y at fixed s=-r<0 gives

    G_3(V_A)=(A-1)r^(A-3)/6,
    G_5(V_A)=(A-1)(A-3)r^(A-5)/40,
    G_3(Q_A)=-(2A-3)r^(2A-4)/6,
    G_5(Q_A)=-(2A-3)(2A-5)r^(2A-6)/40.

Multiplication by the prescribed r powers gives the table. For Q_2 direct differentiation gives

    partial_y^4 Q_2(-r,kappa r) = 3kappa (1+kappa^2)^(-5/2)/r.

This cone blowup is separate from its lack of smoothness on s=0 away from the origin. The examples are smooth at every axis point s<0 but not throughout a punctured neighborhood. Their growth degrees are 5/2, 5/2 and 3. Hence they are outside the admissible sublinear global class. The source slope g=27/8 of Q_(7/4), for example, differs from the R12 zero-B_3 value 3A(4A-3)/(8A-1)=21/13 at A=7/4. They do not realize those R12 data.

For the quoted frozen fifth-order criterion alpha>3-4/A, the thresholds are 5/7, 1 and 7/5 at A=7/4, 2 and 5/2, respectively. These examples lie below the threshold. For 1<A<=4/3 every class exponent alpha>0 exceeds it; this argument makes no counterclaim in that range. The criterion itself is not proved here.

## Evidence and dependencies

Fresh symbolic checks from the y derivatives of the displayed potentials, all trace constants and the cone derivative are in code/check_frozen.py and verification/symbolic.json. The proof uses the binomial expansion, gamma/beta finite-part identity and elementary homogeneous Hölder estimates. No formal proof-assistant run is claimed. The proof verifies the frozen examples in the lead's draft_fred31_v2, not its separate nonlinear source estimates.

## Homogeneous uniqueness and localization

For the three examples U_2=-((As partial_s+y partial_y-1)v)/g follows from the proved equation. It is the unique distributional solution of -Delta U_2=partial_s^2 v with the same homogeneity and parities. The difference of two such solutions is distributionally harmonic and therefore smooth, including at the origin. A smooth homogeneous function of degree 5/2 is zero: Taylor expansion through degree three and scaling eliminate every possible Taylor term and remainder. For Q_2 the difference has degree three and is a homogeneous harmonic polynomial; its parity would have to be odd in both s and y. Every monomial with those parities has even total degree, so the difference again vanishes.

Let chi be smooth, compactly supported and equal to one near the origin. The compact inverse U_2[chi v] is well-defined. On that neighborhood,

    Delta(U_2[chi v]-U_2[v])=-partial_s^2((chi-1)v)=0.

The difference is a smooth harmonic function there. The local transport parts of chi v and v coincide, so L_g(chi v)=g(U_2[chi v]-U_2[v]) is smooth near the origin. This justifies use of the cut-off examples as frozen solutions with smooth forcing. It does not provide an IPM nonlinear correction.

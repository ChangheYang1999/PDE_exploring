# Next two transverse resonances of the curved simple-endpoint family

Status: independent proof and exact controls CONFIRMED; external model review pending. The original preparation, recorded before calculation, is preserved in verification/PROOF_preparation.md. The theorem and its full arbitrary-parameter coefficient proof appear below.

Fix beta=2, s=y_*-y, Ck!=0 and B=s+ks^2-(Ck/260)s^13. Use the analytic fields of P303 and impose H=-k^7/231 as proved necessary and sufficient in P306 for the next vorticity coefficient to be analytic. Let v1=v=-(B''+eta)/2, theta1=T/2,theta2=D/24, omega0=eta,omega1=gamma/6. The homogeneous constant in D is free, and gamma has an additional free homogeneous constant. This packet asks whether both can be selected so that theta3, the coefficient of x^6 in temperature, and omega2, the coefficient of x^5 in vorticity, are analytic through s=0.

Use coefficients without factorials:

    W2=B+sum_{j>=1} v_j(s)x^(2j),
    W1=(2beta+B')x+sum_{j>=1} v_j'(s)x^(2j+1)/(2j+1),
    Theta=sum_{l>=1} theta_l(s)x^(2l),
    Omega=sum_{j>=0} omega_j(s)x^(2j+1).

The divergence relation is automatic because d_y=-d_s. The Poisson relation gives

    v_{j+1}=-(omega_j+v_j''/(2j+1))/(2j+2),       (1)

with v0''=B''. Expanding W.gradTheta-(beta-2)Theta=0 at x^(2l) gives

    B theta_l'-[(4l-1)beta+2+2lB']theta_l
      = sum_{a=1}^{l-1} [2(l-a)v_a'theta_{l-a}/(2a+1)
                         -v_a theta_{l-a}'].    (2)

Expanding W.gradOmega+Omega-Theta_x=0 at x^(2j+1) gives

    B omega_j'-[(2j+1)(2beta+B')+1]omega_j
      = -(2j+2)theta_{j+1}
        +sum_{a=1}^j [(2(j-a)+1)v_a'omega_{j-a}/(2a+1)
                       -v_a omega_{j-a}'].      (3)

These formulas follow by multiplying monomials with indices a+(l-a)=l or a+(j-a)=j. For l=1,2 and j=0,1 they recover exactly P303/P306, with the indicated factorial conversions. Thus (1)-(3) determine the next equations without any full-plane inverse assumption.

Put T/C=s^10 tau and Y=s^6 rho, with tau,rho the analytic units defined in P303. At beta2 the homogeneous factors for(2)and(3)are respectively

    Z_theta_l=(T/C)^l=s^(10l)tau^l,
    Z_omega_j=(T/C)^j Y=s^(10j+6)tau^j rho.

Indeed their logarithmic derivatives are l(8+2B')/B and [j(8+2B')+(5+B')]/B, respectively. For an analytic RHS R, the equation B f'-a(s)f=R is equivalent to(f/Z)'=R/(BZ). Since B=s times a unit, R/(BZ) is meromorphic with finitely many negative Laurent powers. Analytic f exists precisely when its residue is zero, provided the leading negative power of its primitive is no worse than the zero of Z. In these recurrences every RHS is analytic, so its worst pole is s^-(m+1) for Z=s^m times a unit; the worst primitive has pole s^-m, and the condition suffices. A nonzero residue forces an s^m log|s| term. When the residue vanishes, the free addition is a constant times Z.

First compute v2 from(1)using omega1. Equation(2)with l=3 has m=30 and an analytic solution theta3 iff its computed residue vanishes. Then equation(3)with j=2 has m=26. Only the coefficients of theta3 through degree26 affect this residue; its own homogeneous constant starts in degree30 and cannot change it. If the first residue is nonzero, the meromorphic part still determines coefficients through degree26, because its logarithmic term begins at degree30; this permits calculation of the two compatibility conditions simultaneously, without asserting an analytic intermediate theta3.

Both residues are affine in the homogeneous constant of D and the homogeneous constant of gamma: the new forcing uses the fixed v1,theta1,omega0 multiplied only by one of D,gamma,v2 at a time, and theta3 is obtained linearly. Therefore evaluating the two residues at(0,0),(1,0),(0,1) determines their exact affine coefficients. A fourth evaluation at a different pair checks that implementation property but is not its proof. The eventual calculation must report the determinant and consistency conditions, including dependence on C and k. Results for a finite set of C,k values alone cannot prove a general identity. No claim concerning all simple endpoints or global B2 follows.

Verification will use a separate finite Fraction-series implementation of(1)-(3), supported by exact symbolic differentiation of the monomial recurrences. No teammate code, JavaScript/TypeScript, servers, RLScience cluster, Lean/Lake or GPU is used. The full proof of any eventual parameter statement must be supplied after the coefficient calculation is independently checked.

## Theorem and complete coefficient argument

The calculation described above has a positive result. For every real C,k with Ck nonzero, the P306 choice H=-k^7/231 admits unique choices of the two homogeneous constants in theta2 and omega1 for which theta3 and omega2 are analytic. The additional homogeneous constant of theta3 is arbitrary and does not affect this compatibility. The homogeneous constant of omega2 is arbitrary after compatibility. This concerns only the finite set of local equations(1)-(3) through l=3,j=2.

Here and below a prime denotes d/ds. Set t=T/C=s^10 tau, Y=s^6 rho, Z=tY, and

    J'=t/(BY),  J(0)=0.

Then eta=Y(H-CJ). Choose the scalar primitives with zero constant term in their Laurent series. Normalize the free parameters by

    theta2(E)=theta2(0)+E t^2,
    omega1(E,F)=omega1(0,0)-4E ZJ+F Z.

The second equality follows by variation of constants in(3)withj=1: the change from E is -4t^2, and t^2/(BZ)=J'. It fixes the meanings of E and F. In particular they are not the unnormalized homogeneous constants of D and gamma in earlier packets.

Let r_T(E,F) be the residue obstructing theta3 and r_O(E,F) the residue obstructing omega2. When theta3 has a logarithm, use its uniquely prescribed coefficients through degree26 to define r_O. Its log starts atdegree30, so this definition agrees with the actual analytic equation whenever r_T=0. The precise affine coefficient matrix is

    r_T(E,F)=alpha+(12Ck/25)E,
    r_O(E,F)=delta-(9k^8/1925)E-(9Ck/20)F.       (4)

Here alpha=r_T(0,0) and delta=r_O(0,0) are fixed real finite Laurent coefficients depending on C,k. Their large explicit rational expressions are not required for existence. The determinant is -27C^2k^2/125, nonzero. Therefore

    E=-25alpha/(12Ck),
    F=(20/(9Ck))(delta-(9k^8/1925)E)             (5)

make both residues zero, uniquely. It remains to prove(4)for arbitraryC,k; finite numerical samples alone do not do this.

Write B0=sP, P=1+ks, and a=-Ck/260, so B=B0+a s^13. The corresponding unperturbed analytic units are t0=s^10/P^6 and Y0=s^6/P^4. The actual t/t0 and Y/Y0 are1+O(s^12), with convergent power series. This follows directly by subtracting their logarithmic derivatives: t'/t-(t0'/t0)=O(s^11) and Y'/Y-(Y0'/Y0)=O(s^11). Also J-J0=O(s^16), where

    J0'=s^3/P^3,
    J0=s^4/4-(3k/5)s^5+...,
    [s^n]J0=(-1)^(n-4) binom(n-2,2) k^(n-4)/n, n>=4.   (6)

All expressions used below have a pole of order at most12 before multiplication by J. Relative corrections of order12 cannot change a residue of a pole of order12 or less. The only contributions requiring separate treatment come from the explicit derivatives B''-B0''=156a s^11 and B'''-B0'''=1716a s^10. Their coefficients will be included explicitly. This bookkeeping uses convergent analytic units, not a divergent asymptotic expansion.

Put q=t'/t=(8+2B')/B and h=Y'/Y=(5+B')/B, so Z'/Z=q+h. The first variation of v2 is ZJ for E and -Z/4 for F. Dividing the theta3 forcing by B t^3 gives the following two exact functions:

    g_F=(C/20)(Y/t)(7+2B')/B^2,

    g_E=[-(2/3)B'''+B''q]/(Bt)
         +(2H/3)(Y/t)(7+2B')/B^2
         -(13C/15)J(Y/t)(7+2B')/B^2
         +13C/(15B^2).                          (7)

To verify(7), insert the variations in(2)withl=3, use v1=-(B''+eta)/2 and eta=Y(H-CJ), and use YJ'=t/B. In particular q-2h/3=2(7+2B')/(3B). No equation beyond those already stated is used.

For g_F, the unperturbed expression is(C/20)s^-6(9+4ks); all perturbations begin atdegree6. Thus Res g_F=0. For g_E the curvature term at B0 is2k s^-12(10+4ks)P^4 and has zero residue. The explicit derivative correction has residue

    (-(2/3)*1716+156*10)a=416a.

The H term is(2H/3)s^-6(9+4ks)and has zero residue. From(6), the J term has residue

    -(13C/15)(9*(-3k/5)+4k*(1/4))=286Ck/75.

The last term has residue-26Ck/15. Adding them and substituting a=-Ck/260 gives12Ck/25. This proves the first row of(4), for anyH, including the tunedH.

For the second row, separate the omega2 variation into its -6theta3 term and the remaining forcing. If I_F'=g_F and I_E'=g_E, then the theta3 variations are t^3 I_F and t^3 I_E. Their quotients by B t^2Y are J'I_F and J'I_E. A free theta3 homogeneous addition gives an analytic J' and has no residue. Residue integration by parts gives

    Res(J'I_E)=-Res(J g_E),
    Res(J'I_F)=-Res(J g_F).                      (8)

The possible logarithm in I_E begins at its constant-power primitive. After multiplication by J=O(s^4), its derivative has no s^-1 contribution, so(8)is valid for the Laurent coefficients at issue even before the theta3 resonance is removed.

For the F variation, the nonthermal part after division by B t Z is

    h_F=[-B'''/2+B''(q+h)/2-eta'/4
          +(9/20)eta(q+h)]/(Bt).                (9)

Its curvature residue is

    (-1716/2+156*16/2)a=390a.

At B0 the curvature term is k s^-12(16+6ks)P^4 and has zero residue. The eta contribution in(9)is exactly

    (Y/t)(H-CJ)(46+11B')/(10B^2)+C/(4B^2).

Its residue is287Ck/100-Ck/2=237Ck/100, by(6). The H contribution again has zero residue. The thermal contribution from(8)is6Res(Jg_F)=-33Ck/25. Thus

    Res variation_F r_O=390a+237Ck/100-33Ck/25
                       =-9Ck/20.              (10)

For the E variation, direct substitution into(3)gives the nonthermal part

    -4J h_F-(2B''+9eta/5)J'/(Bt).

Using(8), its complete residue is therefore

    Res[6Jg_E-4J h_F-(2B''+9eta/5)J'/(Bt)].      (11)

After multiplication by J, the worst curvature pole is of order8. Consequently all a-dependent corrections are beyond the residue in(11), including the explicit derivative terms. Also the terms involving C J inside eta start atdegree2 in(11), so they contribute no residue. At B0, retain only eta=H Y0. Then(11)reduces to the residue of

    k s^-12 P^4(56+24ks)J0
      +(H/5)s^-6(66+36ks)J0
      -4k s^-8 P^2 -(9H/5)s^-2 P^-2.

The third term has zero residue. Formula(6)gives

    [s^11] P^4(56+24ks)J0 = -(6/385)k^7,

by multiplying the degree-five polynomial and summing its six rational contributions. The H terms total-63Hk/25. Hence the E coefficient before tuning is

    -6k^8/385-63Hk/25.

With H=-k^7/231 this is-9k^8/1925, proving the second row of(4). Equations(4)-(5)now establish the theorem without extrapolating from samples.

## Analytic realization and scope

Every coefficient defined so far is analytic in a two-sided neighborhood of s=0 after the indicated residues vanish. This follows from the analytic integrating factors and the meromorphic primitive criterion proved above. Thus the compatible coefficients can be realized by an analytic local polynomial stream. With y=y_*-s and arbitrary constant d, take

    Psi=(B-beta*y+d)x+v1*x^3/3+v2*x^5/5+v3*x^7/7,
    Theta=theta1*x^2+theta2*x^4+theta3*x^6,
    Omega=-Delta Psi,

where v3 is given by(1)withj=2. Its vorticity coefficients at x,x^3,x^5 are precisely omega0,omega1,omega2. The velocity from this stream gives W2=B+v1*x^2+v2*x^4+v3*x^6 using W=beta X+U-(0,d) for this local realization, and W1 as above. No claim that this freely chosen local d equals a global canonical U2(0) is made. Therefore the thermal residual is O(x^8) and the vorticity residual is O(x^7), with analytic coefficient functions. The Poisson relation is exact by definition.

This is a realization of finite transverse jets. It does not solve the two transport equations on a neighborhood, specify a global full-plane inverse, attach to the moving-center temperature jet, or construct a global B2 profile. In particular it is not evidence of the decisive YES endpoint. It shows that the P306 tuned subfamily encounters no new obstruction at these next two equations. The earlier profile-sign restriction Ck<0 for A/C>0,H/A>0 persists; this packet neither weakens it nor extends it to other endpoint families.

Dependencies: P303 supplies the analytic T,eta,D family and its fourth-jet residue cancellation; P306 supplies the necessary and sufficient choiceH=-k^7/231foranalyticgamma. Equations(1)-(11)and their local convergence arguments are proved here. The rational samples are checks of these formulas, not premises of the general theorem.

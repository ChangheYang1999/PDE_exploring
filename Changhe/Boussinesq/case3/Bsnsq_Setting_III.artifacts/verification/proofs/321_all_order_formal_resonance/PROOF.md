# Arbitrary-order transverse compatibility in the curved local family

Status: independent mathematical argument confirmed, with exact symbolic and rational controls and actual Opus5.5 review. Initially prepared 2026-10-22T08:36:42.295764+00:00.

## Exact setting and statement
Use P308's beta=2 recurrence, Ck nonzero, B=s+ks^2+a s^13 with a=-Ck/260, H=-k^7/231, t=T/C and Y as in that proof. Let q=t'/t=(8+2B')/B and h=Y'/Y=(5+B')/B. Let J'=t/(BY), J(0)=0, eta=Y(H-CJ). For each integer n>=2 suppose the hierarchy has been solved analytically through theta_n and omega_(n-1), with all coefficients strictly preceding theta_n and omega_(n-1) fixed. The two newest homogeneous constants can be selected uniquely to make the next two equations compatible, and the resulting sequence defines a formal series in x with coefficients that are analytic germs in s. This is a local formal claim only. The independent verification evidence and its limits are recorded in SUMMARY.md.

The coefficients use no factorials: W2=B+sum(v_j x^(2j)), W1=(4+B')x+sum(v_j' x^(2j+1)/(2j+1)), Theta=sum(theta_l x^(2l)), Omega=sum(omega_j x^(2j+1)), with d_y=-d_s. The exact equations are

    v_(j+1)=-(omega_j+v_j''/(2j+1))/(2j+2),
    B theta_l'-[8l+2l B']theta_l
      =sum_(a=1)^(l-1)[2(l-a)v_a' theta_(l-a)/(2a+1)-v_a theta_(l-a)'],
    B omega_j'-[(2j+1)(4+B')+1]omega_j
      =-(2j+2)theta_(j+1)
       +sum_(a=1)^j[(2(j-a)+1)v_a' omega_(j-a)/(2a+1)-v_a omega_(j-a)'].

Here v0=B, theta1=Ct/2, omega0=eta. These follow by Cartesian coefficient multiplication and the convention Omega=-Delta Psi; the full derivation is also given in P308. P303/P306 supply the stated analytic base germs; their exact hypotheses Ck!=0 and tuned a,H are retained.

Throughout, Res denotes the coefficient of s^-1 in the forcing divided by B times the normalized homogeneous factor. The pole bound12 below applies to the variation functions g_E, g_F and h_F. It does not apply to the fixed full forcing: the thermal constant residue alpha_n comes from a meromorphic function with pole order at most10(n+1)+1.

The two variations are normalized as

    delta theta_n=E t^n,
    delta omega_(n-1)=-2n E t^(n-1)Y J+F t^(n-1)Y.

The second identity follows directly from the -2n theta_n term of its scalar ODE. The Poisson recurrence then gives delta v_n=E Z J-F Z/(2n), where Z=t^(n-1)Y; previous v_j, j<n, are fixed. The next thermal and vorticity compatibility residues are affine in E,F. For n>=2 their forcings contain the varied coefficients only once in each product, paired with fixed first-order coefficients. The exception n=1 is excluded.

Let z=Z'/Z=(n-1)q+h and K=(Y/t)(7+2B')/B^2. Divide the thermal variation by B t^(n+1). Direct multiplication of the recurrence gives

    g_F=C K/[2n(2n+1)],
    g_E=n[-B'''/3+B''q/2]/(Bt)+(nH/3)K-C A_n J K+C A_n/B^2,
    A_n=n/3+1/(2n+1).

Indeed the variation from a=1 is [(2n/3)v1'-n q v1]/(Bt), with v1=-(B''+eta)/2; the variation from a=n is C(Y/t)[(2z/(2n+1)-q)J+2J'/(2n+1)]/(2B). Substitution of eta'=h eta-Ct/B and 3q-2h=2(7+2B')/B gives the formula.

The unperturbed units for B0=s(1+ks) are t0=s^10/(1+ks)^6, Y0=s^6/(1+ks)^4 and J0'=s^3/(1+ks)^3. The true unit ratios differ by O(s^12), J-J0=O(s^16). The residue bookkeeping of P308 applies uniformly in n because g_E and g_F have poles of order at most12, independent of n. Explicit B'' and B''' corrections must still be retained. Res g_F=0. Res g_E=208n a+(12/5)A_n Ck=12Ck/[5(2n+1)], after inserting a=-Ck/260. This coefficient is nonzero for every integer n>=2.

For the F variation of the nonthermal part of the next vorticity equation, division by B t^n Y gives

    h_F=[-(2n-1)B'''/6+B''z/2+p_n eta'+r_n eta z]/(Bt),
    p_n=(3-2n)(n+1)/(6n),
    r_n=[n(2n+1)-1]/[2n(2n+1)].

The a=1 variation contributes (2n-1)v1'/3-v1 z. The a=n variation contributes -eta z/[2n(2n+1)]+eta'/(2n), proving this formula. The thermal part contributes 2(n+1) Res(J g_F) by residue integration by parts. Before thermal compatibility, define r_O using the meromorphic part of the primitive, omitting its logarithmic term. That logarithm begins at degree10(n+1), above the next vorticity indicial degree10n+6; after division it contributes only a multiple of J' log|s|=O(s^3 log|s|), which has no s^-1 term. Thus the resulting coefficient is affine in E,F even before compatibility and is the actual vorticity residue after E is fixed to make r_T zero.

The explicit-curvature residue of h_F is (208n-26)a. Write q and h over B, and use eta'=h eta-Ct/B. The remaining eta residue is Ck(3N0/5-N1/4+2p_n), where

    N0=10r_n(n-1)+6(p_n+r_n),
    N1=4r_n(n-1)+2(p_n+r_n).

The thermal contribution is -22(n+1)Ck/[5n(2n+1)]. For explicit algebra, 3N0/5-N1/4+2p_n-22(n+1)/[5n(2n+1)]=(n+1)(8n-9)/(10n). The curvature term divided by Ck is -(8n-1)/10. Adding them, substituting a=-Ck/260 and combining rational functions gives

    (208n-26)a+Ck[3N0/5-N1/4+2p_n-22(n+1)/(5n(2n+1))]
       = -9Ck/(10n).

Consequently, with alpha_n, delta_n the fixed residues at E=F=0 and b_n the finite off-diagonal coefficient, the two compatibility residues are

    r_T=alpha_n+[12Ck/(5(2n+1))]E,
    r_O=delta_n+b_n E-[9Ck/(10n)]F.

The determinant is -54C^2 k^2/[25n(2n+1)], nonzero. E is fixed first, then F. The coefficient b_n need not be calculated to establish solvability. For completeness it is

    b_n=-k^8(2n+5)/[385(2n+1)].

Here is its finite coefficient proof. The E variation of the nonthermal vorticity integrand is

    h_E=-2n J h_F-[n B''+(n-1/(2n+1))eta]J'/(Bt).

This follows from the same Cartesian terms: differentiating the extra factor J gives precisely the second term. Consequently b_n is the residue of 2(n+1)Jg_E+h_E. After multiplication by J all a corrections start beyond the residue, and the terms in eta containing C J also start beyond it. With P=1+ks and J0'=s^3/P^3 the remaining expression is

    4n k s^-12 P^4(7+3ks)J0
      +H s^-6[(2n(n+1)/3)(9+4ks)-2n(N0+N1 ks)]J0
      -2n k s^-8 P^2-(n-1/(2n+1))H s^-2 P^-2.

P308's explicitly proved finite convolution [s^11]P^4(56+24ks)J0=-(6/385)k^7 gives the first residue as -(3n/385)k^8. The third term has no residue. Using [s^4]J0=1/4 and [s^5]J0=-3k/5 gives the two H residues together as -3Hk(n+1)(6n-5)/[5(2n+1)]. Substitution H=-k^7/231 gives the displayed b_n. No new infinite sum identity is used.

## Induction and complete local scope
P303 and P306 give analytic theta1, theta2, omega0, omega1 for the stated a,H, with free constants in theta2 and omega1. This is n=2. At each step the two chosen variations preserve every earlier equation. The next thermal equation has homogeneous factor t^(n+1), of order10(n+1); the next vorticity factor is t^n Y, of order10n+6. For analytic forcing, division by B times the factor is meromorphic with a finite pole. A primitive gives an analytic solution exactly when its residue vanishes: the worst pole of the primitive is no worse than the zero order of the factor. The factors and primitives converge as germs. After compatibility, each new solution retains its own homogeneous constant, furnishing the inputs to the next induction step.

The new thermal homogeneous constant starts at degree10(n+1), above the vorticity indicial degree10n+6, and its contribution after division is a constant multiple of J', which is analytic. It therefore cannot obstruct the current vorticity equation. Each later step changes only newly introduced coefficients, so coefficients already fixed stay fixed. Induction thus gives one consistent formal series in the ring of analytic germs in s with a formal variable x. Using the Poisson recurrence and the divergence representation from P308, the two transport equations and Poisson relation hold coefficient by coefficient.

There is no claim of a common s-neighborhood, coefficient-growth bound with n or convergence in x. This construction does not solve the PDE on an open neighborhood, implement the full-plane inverse, attach to the moving-center jet, or construct a global profile. General B2 remains OPEN. No formalization is performed. Independent symbolic and Fraction checks will not import or execute teammate code. No JavaScript/TypeScript, servers, RLScience cluster or Lean/Lake builds; writes only in verification.

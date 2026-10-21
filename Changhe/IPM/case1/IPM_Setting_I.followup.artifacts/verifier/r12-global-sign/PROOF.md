# The R12 fifth finite part is negative for every nonresonant A>1

Date: 2026-10-20. Status: complete proof written before the new numerical checks. This extends the parameter range of the exact formula in ../fifth-order/PROOF.md. It is a theorem about prescribed axis data, not about all coupled profiles.

## Statement and definitions

Fix A>1, A!=2, and let

    S_A=6A(4A-3)/(8A-1), L=sqrt(S_A), u=x/L,
    w=-Ax(1-u^2)/(1+u^2), g=x^2/(1+u^2), h=A+1-w'.

Here 0<x<L. Define the velocity coefficients and transport hierarchy by

    a_2=(g'-w'')/2, b_3=-a_2'/3,
    a_4=(b_3'+G_3')/4, b_5=-a_4'/5,
    wG_3'+(3h-1)G_3=F_3, F_3=-a_2g'-b_3g,
    wG_5'+(5h-1)G_5=F_5,
    F_5=-a_2G_3'-3b_3G_3-a_4g'-b_5g.

Select G_3 by G_3/H_3->0 as x->L, where

    H_j=x^(2j+(j-1)/A)(1+u^2)^(-j)(1-u^2)^(-(j-1)/A).

The normalization is H_j/x^(2j+(j-1)/A)->1 as x->0. The finite part removes divergent powers at x=0 without adding a finite constant. Define

    B_3=-FP int_0^L F_3/(wH_3) dx,
    B_5=-FP int_0^L F_5/(wH_5) dx,
    B_5,nat=L^(6+4/A) B_5.

Then B_3=0 for these selected axis data and

    B_5<0, B_5,nat<0

for every A in (1,2) union (2,infinity). In particular this sign statement applies to the computed parameter near10.15. It is exact; no numerical agreement is used as a nonvanishing certificate. At A=2 the direct resonant finite part is positive, +11/1474560, and is not the continuous nonresonant value. The fifth logarithmic coefficient is zero there. The sign theorem therefore explicitly excludes A=2.

## Derivation and the unrestricted parameter range

Differentiation gives w g'=(w'-A)g and H_j'/H_j=(1-jh)/w. On L^2=S_A the source-selected third solution is

    G_3=10A u^2/[(8A-1)(1+u^2)^3].                     (1)

This identity is verified by substituting in its displayed first-order equation and clearing denominators. The right side is analytic and even at the center and bounded at the source. Since H_3 diverges there, it is the unique selected solution. Its center homogeneous coefficient is zero, which is B_3=0 under the chosen zero source constant. The identity is rational in A and holds for every A>1; its derivation imposes no upper bound on A.

Substitution of (1) gives

    F_5=u^2(c_0+c_2u^2+c_4u^4)
               /[15(4A-3)(8A-1)(1+u^2)^6],
    c_0=2076A^2+741A-36,
    c_2=-3060A^2+305A-70,
    c_4=1400A^2-950A+50.

Thus with p_5=10+4/A,

    B_5=1/[15A(4A-3)(8A-1)L^p_5]
       FP int_0^1 u^(1-p_5)(c_0+c_2u^2+c_4u^4)
                                  (1-u^2)^(4/A-1)du.   (2)

The source endpoint is integrable for every A>0 because 4/A>0. At the center, put t=u^2 in the integral and a=-4-2/A, q=4/A. The three monomials in (2) have finite parts (1/2)Beta(a+j,q), j=0,1,2. Indeed, subtraction and explicit integration of finitely many Taylor monomials of (1-t)^(q-1) continue the convergent Euler integral from Re(a)>0 to each non-pole a. At a non-pole this continuation equals exactly the constant term of the cutoff integral. The substitution t=u^2 maps each divergent power to its corresponding power and preserves that constant term.

For A>1, a lies in (-6,-4). Its only integer in the interior is -5, corresponding to A=2. Hence for every A>1,A!=2 the finite-part substitution is nonresonant. The beta recurrence then reduces (2) to

    B_5=P(A) Beta(-4-2/A,4/A)
          /[15A(2A-1)(3A-2)(4A-3)(8A-1)L^(10+4/A)],   (3)
    P(A)=1248A^4-548A^3+297A^2-178A+84.

All denominators used in this rational reduction are nonzero on A>1. In particular a+q=-4+2/A lies in (-4,-2), so neither a+q nor a+q+1, the beta recurrence denominators needed at j<=2, is zero. An integer value a+q=-3 at A=2 is already the excluded resonance; for all other A the gamma quotient is finite. The rational substitution and reduction in this paragraph are precisely the symbolic identities proved in ../fifth-order/PROOF.md and its exact check code; they are supplied here with their domain checked explicitly. The earlier restriction A<4 was a restriction on the applications of that topic, not a singularity or hypothesis of (1)-(3).

## Manifestly negative gamma representation

Put z=2/A, so 0<z<2. For z!=1, gamma recurrence gives

    Beta(-4-z,2z)
       =- [Gamma(2-z)Gamma(2z)/Gamma(1+z)]
                 (2-z)(3-z)(4-z)
                    /[(1+z)(2+z)(3+z)(4+z)].          (4)

To check the sign and recurrence, start with

    Gamma(-4-z)= -Gamma(1-z)/[z(z+1)(z+2)(z+3)(z+4)],
    Gamma(-4+z)= Gamma(1+z)/[z(z-1)(z-2)(z-3)(z-4)].

Divide, multiply by Gamma(2z), and use (z-1)Gamma(1-z)=-Gamma(2-z). The three remaining factors z-2,z-3,z-4 have negative product. This yields exactly (4). All gamma arguments in (4) are positive and all displayed rational factors after the minus sign are positive for 0<z<2. Thus the beta factor is strictly negative.

Finally, with v=A-1>0,

    P(1+v)=1248v^4+4444v^3+6141v^2+3764v+903>0.

All factors in the denominator of (3), and the natural-unit rescaling, are positive. This proves both strict signs on the entire stated range.

## Resonance and limits

Formula (4) has the continuous value -1/20 at z=1. Substitution in (3) gives the nonresonant limit -11/1474560 as A->2 along L^2=S_A. At A=2,L=2, however, the integrand (2) is a Laurent polynomial with no u^(-1) term. Integrating those monomials directly and retaining their constant term gives +11/1474560, as established exactly in ../fifth-order/PROOF.md. Thus the nonresonant limit differs from the resonant finite part; the sign theorem must not be applied there by continuity. A vanishing fifth logarithmic coefficient, rather than B_5=0, is the relevant fifth smoothness condition at this resonance.

As A->infinity, z->0, formula (4) gives Beta(-4-z,2z)~ -1/(2z)=-A/4. The rational prefactor P(A)/[15A(2A-1)(3A-2)(4A-3)(8A-1)] is asymptotic to13/(30A), and L^2~3A. Therefore

    A^2 B_5,nat -> -13/1080.

This limit is a consistency check of the sign and scaling, not a uniform lower bound away from zero on the unbounded parameter range.

## Dependencies and scope

The proof uses the exact axis hierarchy, the explicitly selected third solution, rational substitution, the finite-part Euler integral and elementary gamma recurrence. The previous fifth-order topic supplies exact rational verification of the algebra and the resonant value. New checks compare (4) with the continued beta value, and reproduce the reported natural-unit scale using the stated parameter. These computations check the implementation; strict negativity is proved by the positive factors in (4).

No coupled full-plane realization of these axis data has been established. Even nonzero B_5 does not by itself exclude smoothness: for a smooth even center at a nonresonant parameter the condition is ell_5+B_5=0, where ell_5=lim_(x->L) G_5/H_5, and a separate theorem is needed to force ell_5=0. For large A, such a source endpoint is not supplied by baseline C^(2,alpha) regularity. Thus this exact sign repairs a numerical-only nonvanishing statement for this prescribed axis family, but gives no unrestricted NO_inf endpoint.

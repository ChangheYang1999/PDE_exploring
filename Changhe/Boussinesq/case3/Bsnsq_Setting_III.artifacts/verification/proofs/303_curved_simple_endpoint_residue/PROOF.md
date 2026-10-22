# Curved simple ends with either infinite ratio sign

Status: independent local analytic proof. This audits the new construction in lead astra/z453_simple, section8. It is a theorem about four necessary axis equations, not the full PDE.

## Statement and notation
Fix beta=2, epsilon in {-1,1}, y_*, A,C,H real nonzero with C and H of the sign of A, and k real nonzero. There exist real analytic functions b,T,eta,v,D on a full neighborhood of y_* satisfying

 b T_y+(8-2b_y)T=0,
 b eta_y+(5-b_y)eta=T,
 eta=-b_yy-2v,
 b D_y+(16-4b_y)D=8v_y T-12v T_y.

On the chosen side y=y_*-epsilon s, s>0, these have

 b=epsilon B(s), B=s+k s^2+a s^13, a=-epsilon Ck/260,
 T=C s^10(1+O(s)), eta=H s^6(1+O(s)),
 I_2=D/T^2= -120k/(11C) s^-11(1+o(1)).

In particular A I_2 has either infinite sign as k varies at either specified end, while T and eta have the sign of A and b_y(y_*)=-1. This does not prescribe two ends simultaneously or a material center.

## Complete proof
Use the signed coordinate s=epsilon(y_*-y). Thus d_y=-epsilon d_s, b_y=-B_s, b_yy=epsilon B_ss. Define q=(8+2B_s)/B and p=(5+B_s)/B. Since B/s is an analytic unit, q-10/s and p-6/s extend analytically. Set tau=exp integral_0^s(q-10/u)du and rho=exp integral_0^s(p-6/u)du, where integrals mean the unique analytic primitives vanishing at zero. Let T=C s^10 tau, Y=s^6 rho, eta=Y(H-integral_0^s T/(BY)du), v=-(eta+epsilon B_ss)/2. The last integrand is analytic of order3. Differentiation gives T_s=qT and eta_s=p eta-T/B and the first three original equations exactly. These are analytic on a signed neighborhood with the stated leading terms.

Substitute D=T^2 I into the fourth equation. The T equation cancels the I term because beta=2. Division away from zero gives

 I_s=f=[-4B_sss+6B_ss q+epsilon(6eta q-4eta_s)]/(BT).

All factors are analytic units times known integer powers, so f has a convergent Laurent expansion with pole order at most12. It has a meromorphic primitive precisely when its s^-1 coefficient vanishes. We compute that coefficient exactly.

First put a=0, B0=s(1+ks). Direct integration gives T0=C s^10/(1+ks)^6, Y0=s^6/(1+ks)^4 and eta0=Y0(H-CJ), with J'=s^3/(1+ks)^3,J(0)=0. The curvature part of f is 12k(10+4ks)(1+ks)^4/(C s^12). Its numerator has degree5, so there is no s^-1 coefficient. The eta part is

 epsilon[(36+16ks)(H/C-J)/s^6+4/(s^2(1+ks)^2)].

Here J=s^4/4-3k s^5/5+O(s^6). Its residue is epsilon(108k/5-4k-8k)=epsilon48k/5. Thus a purely quadratic B has a nonzero residue when k is nonzero, an actual obstruction to smooth D.

Now restore a s^13. The differences q-q0 and p-p0 are O(s^11), and integration gives T/T0=1+O(s^12), Y/Y0=1+O(s^12). Consequently eta-eta0=O(s^18) and eta_s-eta0_s=O(s^17). Every change in the eta part of f is O(s^6), so its residue is unchanged. The relative denominator change is O(s^12); since the original curvature term has order-12 this affects only O(1) terms. In its numerator the only new term of order10 comes from

 -4(13*12*11)a s^10+6(13*12)a s^11*(10/s)=2496a s^10.

All other new numerator terms are O(s^11), including 2k(q-q0). Division by BT=C s^11(1+O(s)) therefore changes the residue by2496a/C. The total residue is epsilon48k/5+2496a/C, zero exactly for a=-epsilon Ck/260. These analytic order estimates include all higher powers and prove exact cancellation, not only formal truncation.

Integrate the now residue-free convergent Laurent series termwise. The primitive I has pole order at most11; an arbitrary real constant may be added. Then D=T^2 I is real analytic since T^2 has order20. The fourth equation holds away from zero by construction, and through zero by analyticity. The leading term of f is120k/C s^-12, so I=-120k/(11C)s^-11(1+o(1)). For sufficiently small positive s, the analytic units have positive values, hence T,eta retain the signs of C,H and B>0. This completes the proof.

## Scope and dependencies
Only analytic primitives, convergent Laurent series and explicit differentiation are used. The independently audited P296 curvature formula predicts D/T~-120k/11 s^-1 consistently, but is not needed for existence here. Local arithmetic is beta/1=2 and1/1=1, positive integers of odd sum. No all-orders transverse realization, full-plane inverse, global symmetry extension, far field or actual B2 profile is asserted. General B2 remains OPEN.
